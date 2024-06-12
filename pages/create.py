from flet import *

class CreateView(View): 

    def __init__(self, page: Page):
        super().__init__()
        self.route = "/create"

        self.page = page
        self.page.splash = None

        self.vertical_alignment = MainAxisAlignment.CENTER
        self.horizontal_alignment = CrossAxisAlignment.CENTER

        self.input = TextField(
            label="Value",
            input_filter=NumbersOnlyInputFilter(),
            prefix=Text("Rp"),
            autofocus=True,
            on_submit=self.create
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
                            Text("Create a new gift card", size=20, weight=FontWeight.BOLD),
                            Text("Enter the value of the gift card."),
                        ]),
                        self.input,
                        FilledButton(
                            text="Create",
                            on_click=self.create
                        )
                    ],
                    spacing=20
                ),
                padding=15,
                width=300
            )
        ]

    def create(self, e):
        gift_card = self.page.db.create_gift_card(int(self.input.value))
        
        self.page.go("/gift_card/" + gift_card.code)