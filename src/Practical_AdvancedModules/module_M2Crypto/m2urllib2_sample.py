__author__ = 'wenychan'

from M2Crypto import m2urllib2
from M2Crypto.SSL import Context

def usage():
    opener = m2urllib2.build_opener()
    response = opener.open('www.google.com')
    print 'html: ', response.read()
    print 'info: ', response.info()
    print 'url: ', response.geturl()


def usage1():
    context = Context();
    context.set_allow_unknown_ca(False)

    # add client site certificate and private key
    # to support Client verification
    context.load_cert(certfile='cert.pem', keyfile='key.pem')

    # add server site trusted CA certifications
    # to support server verification
    context.load_verify_info(capath='./')
    opener = m2urllib2.build_opener(context)
    response = opener.open("https://sjmcm1csa2/")

    print 'html: ', response.read()
    print 'info: ', response.info()
    print 'url: ', response.geturl()

if __name__ == '__main__':
    # usage()

    usage1()