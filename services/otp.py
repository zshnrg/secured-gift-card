import datetime
import random

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