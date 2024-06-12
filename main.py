from flet import *

from router import router
from services.db import Database

async def main(page: Page):
    page.title = "Secured Gift Card"
    page.theme = Theme(
        color_scheme_seed=colors.BLUE
    )
    page.theme_mode = ThemeMode.LIGHT

    page.db = Database()

    def route_change(route):
        page.views.clear()
        print(page.route)
        page.views.append(
            router(page, page.route)
        )   
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop

    page.go("/")

if __name__ == "__main__":
    app(
        target=main,
        assets_dir="assets",
        upload_dir="uploads",
    )