from flet import *

class RedeemView(View):
    def __init__ (self, page: Page):
        super().__init__()
        self.route = "/redeem"

        self.page = page
        self.page.splash = None

        self.vertical_alignment = MainAxisAlignment.CENTER
        self.horizontal_alignment = CrossAxisAlignment.CENTER

        self.input = TextField(
            label="Code",
            autofocus=True,
            on_submit=self.redeem,
        )

        self.otp = TextField(
            label="OTP",
            on_submit=self.submit_otp
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
                            Text("Redeem a gift card", size=20, weight=FontWeight.BOLD),
                            Text("Enter the code of the gift card."),
                        ]),
                        self.input,
                        FilledButton(
                            text="Redeem",
                            on_click=self.redeem
                        )
                    ],
                    spacing=20
                ),
                padding=15,
                width=300
            )
        ]

    def redeem(self, e):
        gift_card = self.page.db.get_gift_card(self.input.value)
        self.controls[0].content.controls.pop()
        self.controls[0].content.controls.pop()

        
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
        
        if gift_card.status == "inactive":
            self.controls[0].content.controls.append(
                Container(
                    content=Text("Gift card not activated, please activate first", color=colors.RED_400),
                    padding=15,
                    bgcolor=colors.RED_50,
                    border=border.all(1, colors.RED_400),
                    border_radius=5,
                    width=300
                )
            )
            self.page.update()
            return
        
        if gift_card.status == "redeemed":
            self.controls[0].content.controls.append(
                Container(
                    content=Text("Gift card already redeemed", color=colors.RED_400),
                    padding=15,
                    bgcolor=colors.RED_50,
                    border=border.all(1, colors.RED_400),
                    border_radius=5,
                    width=300
                )
            )
            self.page.update()
            return
        
        self.controls[0].content.controls.append(
            self.otp,
        )
        self.controls[0].content.controls.append(   
            FilledButton(
                text="Redeem",
                on_click=self.submit_otp
            )
        )
        self.page.update()

    def submit_otp(self, e):
        gift_card = self.page.db.get_gift_card(self.input.value)
        if gift_card.redeem(self.otp.value):
            self.controls[0].content.controls.pop()
            self.controls[0].content.controls.pop()
            self.controls[0].content.controls.append(
                Container(
                    content=Text("Gift card redeemed successfully", color=colors.GREEN_600),
                    padding=15,
                    bgcolor=colors.GREEN_50,
                    border=border.all(1, colors.GREEN_600),
                    border_radius=5,
                    width=300
                )
            )
            self.page.update()
        else:
            self.controls[0].content.controls.pop()
            self.controls[0].content.controls.pop()
            self.controls[0].content.controls.append(
                Container(
                    content=Text("Invalid OTP, gift card cannot be redeemed", color=colors.RED_400),
                    padding=15,
                    bgcolor=colors.RED_50,
                    border=border.all(1, colors.RED_400),
                    border_radius=5,
                    width=300
                )
            )
            self.page.update()
        

