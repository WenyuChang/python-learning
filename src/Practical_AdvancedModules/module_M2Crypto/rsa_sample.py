__author__ = 'wenychan'

from M2Crypto import BIO, RSA

rsa_key_file = open('filepath', 'rb').read()
rsa_key = RSA.load_key_string(rsa_key_file)

# bio = BIO.MemoryBuffer(rsa_key_file)
# rsa_key = RSA.load_key_bio(bio)

rsa_key.private_decrypt('string to be encrypt', RSA.pkcs1_padding)
rsa_key.public_decrypt('string to be encrypt', RSA.pkcs1_padding)

rsa_key.private_encrypt('string to be encrypt', RSA.pkcs1_padding)
rsa_key.public_encrypt('string to be encrypt', RSA.pkcs1_padding)