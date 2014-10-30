
from M2Crypto import EC
from M2Crypto.EVP import MessageDigest
def bigint(string):
    return int(string.encode('hex'), 16)

# raw data
myhash = "hello world"

# digest data using sha256
md = MessageDigest('sha256')
md.update(myhash)
myhash = md.digest()
print '#'*30
print '#'*10, myhash
print '#'*30


# sign digested data using EC key pair
# load_key can also load private key, and use load_pub_key to load public key
# return (r,s)
# load key from string
# privKey = open('Cesium-ECC-PrivateKey.pem','rb')
# privKey = privKey.read()
# bio = BIO.MemoryBuffer(privKey)
# key = EC.load_key_bio(bio)

key = EC.load_key('Cesium-ECC-ECParam.pem')
sigr, sigs = key.sign_dsa(myhash)
print '#'*30
print '#'*10, 'sigr: ', sigr
print '#'*10, 'sigs: ', sigs
print '#'*30
result = key.verify_dsa(myhash, sigr, sigs)
print 'verify: ', result

print


# sign digested data using EC key pair
# return single blob
print '#'*30
data = key.sign_dsa_asn1(myhash)
print data
print '#'*30
result = key.verify_dsa_asn1(myhash, data)
print 'verify: ', result



