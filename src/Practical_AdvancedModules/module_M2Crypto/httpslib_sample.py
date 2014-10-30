__author__ = 'wenychan'

from M2Crypto import httpslib, SSL, X509, EVP, m2
from M2Crypto.SSL import Context


# using httpslib in M2Crypto
class MyHTTPS(httpslib.HTTPSConnection):
    def connect(self):
        self.sock = SSL.Connection(self.ssl_ctx)
        self.sock.set_post_connection_check_callback(None)
        if self.session:
            self.sock.set_session(self.session)
        self.sock.connect((self.host, self.port))

def send_request(context):
    https = MyHTTPS('sjmcm1csa2', 443, ssl_context=context)
    https.putrequest('GET', '')
    https.putheader('Accept', 'text/html')
    https.putheader('Accept', 'text/plain')
    https.putheader('Connection', 'close')
    https.endheaders()
    response = https.getresponse()
    print 'header: ', response.getheaders()
    print 'html: ', response.read()

    https.request('POST', '/aaa/bbb/ccc', 'data')
    response = https.getresponse()
    print 'header: ', response.getheaders()
    print 'html: ', response.read()

def usage():
    # form context by passing cert and private key file
    context = Context();
    context.set_allow_unknown_ca(False)
    context.load_cert(certfile='cert.pem', keyfile='key.pem')

    # make server verification
    # capath should contain hash soft link to CA certifiates
    context.load_verify_info(capath='./')
    context.set_verify(SSL.verify_peer, 3)
    # context.set_verify(SSL.verify_none, 3)

    # using MyHTTPS to send request
    send_request(context)

def usage1():
    # form context by passing cert and private key content
    context = Context();
    context.set_allow_unknown_ca(False)

    cert_file = open('/opt/cisco/creds/id.cert', 'rb').read().encode('ascii')
    cert_file = X509.load_cert_string(cert_file)
    key_file = open('/opt/cisco/creds/id.cert', 'rb').read().encode('ascii') # pem-encoded pkey
    key_file = EVP.load_key_string(key_file)
    m2.ssl_ctx_use_x509(context.ctx, cert_file.x509)
    m2.ssl_ctx_use_pkey_privkey(context.ctx, key_file.pkey)

    # make server verification
    # capath should contain hash soft link to CA certifiates
    context.load_verify_info(capath='./')
    context.set_verify(SSL.verify_peer, 3)
    # context.set_verify(SSL.verify_none, 3)

    # using MyHTTPS to send request
    send_request(context)


if __name__ == '__main__':
    usage()

    # usage1()