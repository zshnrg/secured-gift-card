from flet import *

from pages.menu import MenuView
from pages.create import CreateView
from pages.gift_card import GiftCardView
from pages.activate import ActivateView
from pages.redeem import RedeemView

def router(page: Page, route: str):
    troute = TemplateRoute(route)
    if troute.match('/'):
        return MenuView(page)
    elif troute.match('/create'):
        return CreateView(page)
    elif troute.match('/gift_card/:code'):
        return GiftCardView(page, troute.code)
    elif troute.match('/activate'):
        return ActivateView(page)
    elif troute.match('/redeem'):
        return RedeemView(page)