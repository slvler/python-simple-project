from car import Car
from bus import Bus

from bmw import Bmw

from password_generated import password_generated

# ('md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512',
#  'blake2b', 'blake2s',
#  'sha3_224', 'sha3_256', 'sha3_384', 'sha3_512',
#  'shake_128', 'shake_256')

password = password_generated(text="zzzz")

password.md5_encrypt()
password.sha1_encrypt()
password.sha224_encrypt()
password.sha256_encrypt()
password.sha384_encrypt()
password.sha384_encrypt()
password.sha512_encrypt()
password.blake2b_encrypt()
password.blake2s_encrypt()
password.sha3_224_encrypt()
password.sha3_256_encrypt()
password.sha3_384_encrypt()
password.sha3_512_encrypt()