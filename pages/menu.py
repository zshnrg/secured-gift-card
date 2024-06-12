from flet import *

class MenuView(View):
    def __init__(self, page: Page):
        super().__init__()
        self.route = "/"

        self.page = page
        self.page.splash = None

        self.vertical_alignment = MainAxisAlignment.CENTER
        self.horizontal_alignment = CrossAxisAlignment.CENTER
        
        self.controls = [
            Row(
                [
                    Card(
                        content=Container(
                            content=Column(
                                [
                                    Text("Create", size=20, weight=FontWeight.BOLD),
                                    Text("Create a new gift card code and value.")
                                ]
                            ),
                            padding=15,
                            width=200,
                            on_click=lambda e: self.page.go("/create")
                        )
                    ),
                    Card(
                        content=Container(
                            content=Column(
                                [
                                    Text("Redeem", size=20, weight=FontWeight.BOLD),
                                    Text("Redeem a gift card that you received.")
                                ]
                            ),
                            padding=15,
                            width=200,
                            on_click=lambda e: self.page.go("/redeem")
                        )
                    ),
                    Card(
                        content=Container(
                            content=Column(
                                [
                                    Text("Activate", size=20, weight=FontWeight.BOLD),
                                    Text("Activate a gift card that you bought.")
                                ]
                            ),
                            padding=15,
                            width=200,
                            on_click=lambda e: self.page.go("/activate")
                        )
                    )
                ],
                alignment=MainAxisAlignment.CENTER
            )
        ]