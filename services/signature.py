from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes, serialization

class Signature:
    def __init__(self):
        self.private_key = None
        self.public_key = None

    def generate_key_pair(self):
        self.private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048
        )
        self.public_key = self.private_key.public_key()

    def sign(self, message):
        return self.private_key.sign(
            message,
            padding.PKCS1v15(),
            hashes.SHA3_256()
        )

    def verify(self, signature, message):
        try:
            self.public_key.verify(
                signature,
                message,
                padding.PKCS1v15(),
                hashes.SHA3_256()
            )
            return True
        except Exception as e:
            return False

    def get_private_key(self):
        return self.private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption()
        )

    def get_public_key(self):
        return self.public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )

# test
if __name__ == "__main__":
    signature = Signature()
    signature.generate_key_pair()
    message = b"hello, world"
    signature_ = signature.sign(message)
    assert signature.verify(signature_, message)
    print("Success!")