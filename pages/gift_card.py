from flet import *
from services.db import Database

from io import BytesIO
import qrcode
import base64

def generateQRCode(data):
    qr = qrcode.make(data)
    buffered = BytesIO()

    qr.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode()

    return (img_str)


class GiftCardView(View):
    def __init__(self, page: Page, code: str):
        super().__init__()
        self.route = "/gift_card/" + code

        self.page = page
        self.page.splash = None

        self.vertical_alignment = MainAxisAlignment.CENTER
        self.horizontal_alignment = CrossAxisAlignment.CENTER

        self.spacing = 20

        self.gift_card = self.page.db.get_gift_card(code)
        
        if not self.gift_card:
            print("Gift card not found")
            self.page.go("/")
            return
        

        self.controls = [
            Container(
                Column(
                    [
                        IconButton(
                            icon=icons.ARROW_BACK,
                            on_click=lambda e: self.page.go("/")
                        ),
                        Column(
                            [
                                Row(
                                    [
                                        Text("Gift Card", size=20, weight=FontWeight.BOLD),
                                        Text("Rp" + str(self.gift_card.value), size=20, weight=FontWeight.BOLD, color=colors.GREEN_400),
                                    ],
                                    alignment=MainAxisAlignment.SPACE_BETWEEN
                                ),
                                Container(
                                    content=Column(
                                        [
                                            Text("Insert this code to redeem the gift card."),
                                            Text(self.gift_card.code, size=36, weight=FontWeight.BOLD),
                                        ],
                                        horizontal_alignment=CrossAxisAlignment.CENTER
                                    ),
                                ),
                                Image(
                                    src_base64=generateQRCode(self.gift_card.signature),
                                    width=260
                                )
                            ]
                        )
                    ],
                ),
                padding=15,
                width=300
            )
        ]