from cryptography.fernet import Fernet
from typing import Optional

KEY_1='IRB6Oxid26XsDps9PYoBzBqhotcdCPnUdt4_CZKRcgs='

class Crypto:
    def __init__(self, key: Optional[str] = b'IRB6Oxid26XsDps9PYoBzBqhotcdCPnUdt4_CZKRcgs='):
        if key is None:
            key = Fernet.generate_key()
        self.fernet = Fernet(key)

    def encrypt(self, data: str) -> str:
        return self.fernet.encrypt(data.encode()).decode()

    def decrypt(self, data: str) -> str:
        return self.fernet.decrypt(data.encode()).decode()
