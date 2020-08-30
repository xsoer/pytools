import base64
import hashlib
from Crypto import Random
from Crypto.Cipher import AES


class AESCipher(object):

    def __init__(self, key):
        self.bs = 32
        self.key = hashlib.sha256(key.encode()).digest()

    def encrypt(self, raw):
        raw = self._pad(raw)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(raw))

    def decrypt(self, enc):
        enc = base64.b64decode(enc)
        iv = enc[:AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return self._unpad(cipher.decrypt(enc[AES.block_size:])).decode('utf-8')

    def _pad(self, s):
        return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)

    @staticmethod
    def _unpad(s):
        return s[:-ord(s[len(s)-1:])]


# from Crypto.Cipher import AES
# from Crypto import Random
from binascii import a2b_hex


def get_sign_nature(timestamp):
    BS = 16

    def pad(s): return s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
    key_str = "WenhaiSearchEnRule"  # 16进制秘钥 这个得保密
    plain = timestamp
    iv = Random.new().read(AES.block_size)
    obj = AES.new(a2b_hex(key_str), AES.MODE_ECB, iv)
    plain = pad(plain)
    result = obj.encrypt(plain).encode("hex").upper()
    return result


# if __name__ == "__main__":
    # print get_sign_nature("1448674598637")


if __name__ == "__main__":
    aes = AESCipher("WenhaiSearchEnRule")
    aes.encrypt("A14D0E8D555B476_1538114863566")
    # print(get_sign_nature("A14D0E8D555B476_1538114863566"))
