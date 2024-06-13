from flet import *
import numpy as np
import cv2
import base64

class ActivateView(View):
    def __init__(self, page: Page):
        super().__init__()
        self.route = "/activate"

        self.page = page
        self.page.splash = None

        self.vertical_alignment = MainAxisAlignment.CENTER
        self.horizontal_alignment = CrossAxisAlignment.CENTER

        self.input = TextField(
            label="Code",
            autofocus=True,
            on_submit=self.activate,
            on_change=self.handle_on_change
        )

        self.controls = [
            Container(
                content=Column(
                    [
                        IconButton(
                            icon=icons.ARROW_BACK,
                            on_click=lambda e: self.page.go("/")
                        ),
                        Column([
                            Text("Activate a gift card", size=20, weight=FontWeight.BOLD),
                            Text("Enter the code of the gift card."),
                        ]),
                        self.input,
                    ],
                    spacing=20
                ),
                padding=15,
                width=300
            )
        ]

    def handle_on_change(self, e):
        if len(self.controls[0].content.controls) > 3:
            self.controls[0].content.controls.pop()
            self.page.update()

    def activate(self, e):
        gift_card = self.page.db.get_gift_card(self.input.value)
        
        if not gift_card:
            self.controls[0].content.controls.append(
                Container(
                    content=Text("Gift card not found", color=colors.RED_400),
                    padding=15,
                    bgcolor=colors.RED_50,
                    border=border.all(1, colors.RED_400),
                    border_radius=5,
                    width=300
                )
            )
            self.page.update()
            return
        
        if gift_card.status == "active":
            self.controls[0].content.controls.append(
                Container(
                    content=Text("Gift card already activated", color=colors.RED_400),
                    padding=15,
                    bgcolor=colors.RED_50,
                    border=border.all(1, colors.RED_400),
                    border_radius=5,
                    width=300
                )
            )
            self.page.update()
            return
        
        # Read QR code from camera
        self.controls[0].content.controls.append(
            Container(
                content=Text("Scan the QR code to verify", color=colors.ON_SECONDARY_CONTAINER),
                padding=15,
                bgcolor=colors.SECONDARY_CONTAINER,
                border=border.all(1, colors.ON_SECONDARY_CONTAINER),
                border_radius=5,
                width=300
            )
        )
        self.page.update()
        data = self.read_qr_code()

        self.controls[0].content.controls.pop()
        self.page.update()
        
        if not gift_card.validate_signature(data):
            self.controls[0].content.controls.append(
                Container(
                    content=Text("Invalid signature, gift card cannot be activated", color=colors.RED_400),
                    padding=15,
                    bgcolor=colors.RED_50,
                    border=border.all(1, colors.RED_400),
                    border_radius=5,
                    width=300
                )
            )
            self.page.update()
            return
        
        otp = gift_card.activate()
        print(f"Gift card activated. OTP: {otp}")
        self.controls[0].content.controls.append(
            Container(
                content=Text(f"Gift card activated. OTP: {otp}", color=colors.GREEN_600),
                padding=15,
                bgcolor=colors.GREEN_50,
                border=border.all(1, colors.GREEN_600),
                border_radius=5,
                width=300
            )
        )
        self.page.update()

    def read_qr_code(self):
        cap = cv2.VideoCapture(0)
        
        self.image = Image(
            src_base64="",
            width=300,
            height=300
        )

        self.controls[0].content.controls.append(self.image)
        while True:
            ret, frame = cap.read()
            success, encoded_image = cv2.imencode('.jpg', frame)
            base64_image = base64.b64encode(encoded_image).decode()
            if not ret:
                continue
            
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            detector = cv2.QRCodeDetector()
            data, vertices, _ = detector.detectAndDecode(gray)

            if data:
                cv2.polylines(frame,[np.int32(vertices)],True,(255,0,0),2,cv2.LINE_AA)
                
                cap.release()
                cv2.destroyAllWindows()
                self.controls[0].content.controls.remove(self.image)
                self.page.update()
                return data
            
            # Display the resulting in self.image
            self.image.src_base64 = base64_image
            self.page.update()

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        
        if cap.isOpened():
            cap.release()
            cv2.destroyAllWindows()
        
