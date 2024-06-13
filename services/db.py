import random
import base64

from services.signature import Signature
from services.otp import OTP

class GiftCard:
    def __init__(self, value: int, code: str):
        self.value = value
        self.code = code
        self.status = "inactive"
        self.signature = None
        self.otp = OTP()

    def activate(self):
        self.status = "active"
        self.otp.refresh()

        return self.otp.code
    
    def set_signature(self, signature):
        self.signature = signature

    def validate_signature(self, signature):
        return self.signature == signature
    
    def redeem(self, otp):
        if self.otp.is_expired():
            return False
        
        if not self.otp.is_valid(otp):
            return False
        
        self.status = "redeemed"
        return True

class Database:
    def __init__(self):
        self.gift_cards = {}
        self.signature = Signature()
        self.signature.generate_key_pair()

    def create_gift_card(self, value: int):
        # Generate a random character code of length 6
        code = "".join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", k=6))
        
        # Check if the code is unique
        while self.get_gift_card(code):
            code = "".join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", k=6))

        gift_card = GiftCard(value, code)
        signature = self.signature.sign((code + str(value)).encode())
        gift_card.set_signature(base64.b64encode(signature).decode())

        self.gift_cards[code] = gift_card
        return gift_card
    
    def get_gift_card(self, code: str):
        return self.gift_cards.get(code)
    
    def activate_gift_card(self, code: str):
        gift_card = self.get_gift_card(code=code)
        if gift_card:
            return gift_card.activate()
        return None