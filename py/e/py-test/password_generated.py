import hashlib


class password_generated:

    def __init__(self, text):
        self.text = text

    def md5_encrypt(self):
        result = hashlib.md5(self.text.encode('utf-8')).hexdigest()
        print(result)

    def sha1_encrypt(self):
        result = hashlib.sha1(self.text.encode('utf-8')).hexdigest()
        print(result)

    def sha224_encrypt(self):
        result = hashlib.sha224(self.text.encode('utf-8')).hexdigest()
        print(result)

    def sha256_encrypt(self):
        result = hashlib.sha256(self.text.encode('utf-8')).hexdigest()
        print(result)

    def sha384_encrypt(self):
        result = hashlib.sha384(self.text.encode('utf-8')).hexdigest()
        print(result)

    def sha512_encrypt(self):
        result = hashlib.sha512(self.text.encode('utf-8')).hexdigest()
        print(result)

    def blake2b_encrypt(self):
        result = hashlib.blake2b(self.text.encode('utf-8')).hexdigest()
        print(result)

    def blake2s_encrypt(self):
        result = hashlib.blake2s(self.text.encode('utf-8')).hexdigest()
        print(result)

    def sha3_224_encrypt(self):
        result = hashlib.sha3_224(self.text.encode('utf-8')).hexdigest()
        print(result)

    def sha3_256_encrypt(self):
        result = hashlib.sha3_256(self.text.encode('utf-8')).hexdigest()
        print(result)

    def sha3_384_encrypt(self):
        result = hashlib.sha3_384(self.text.encode('utf-8')).hexdigest()
        print(result)

    def sha3_512_encrypt(self):
        result = hashlib.sha3_512(self.text.encode('utf-8')).hexdigest()
        print(result)
