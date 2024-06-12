import datetime
import random
import base64

from services.signature import Signature

class OTP:
    def __init__(self):
        self.code = None
        self.expiration_time = None

    def generate(self):
        # Generate OTP 6 digits of string
        return str(random.randint(100000, 999999))
    
    def is_expired(self):
        return datetime.datetime.now() > self.expiration_time
    
    def is_valid(self, otp: str):
        return otp == self.code
    
    def refresh(self):
        self.code = self.generate()
        self.expiration_time = datetime.datetime.now() + datetime.timedelta(days=1)


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
    
    def print_gift_cards(self):
        print("Gift Cards:")
        for code, gift_card in self.gift_cards.items():
            print(code, gift_card.value, gift_card.status)