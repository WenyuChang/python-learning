__author__ = 'wenychan'

import urllib2
import urllib


def usage():
    response = urllib2.urlopen('http://www.google.com')
    print response
    # Get the Headers.
    # This returns a dictionary-like object that describes the page fetched,
    # particularly the headers sent by the server
    print '#'*30
    print response.info()

    # Get the date part of the header
    print '#'*30
    print "The Date is: ", response.info()['date']

    # Get the server part of the header
    print '#'*30
    print "The Server is: ", response.info()['server']

    # Get the URL. This gets the real URL.
    print '#'*30
    print "The URL is: ", response.geturl()

    # Get only the length
    print '#'*30
    html = response.read()
    print "Get the length :", len(html)

    # Get all data
    print '#'*30
    # print html

    # do something
    response.close()  # best practice to close the file


def usage1():
    # download files with urllib2
    # file to be written to
    file = "downloaded_file.html"
    url = "http://www.pythonforbeginners.com/"
    response = urllib2.urlopen(url)

    with open(file, 'wb') as f:
        f.write(response.read())


def usage2():
    # Urllib2 Requests
    # Specify the url
    url = 'http://www.google.com'
    # This packages the request (it doesn't make it)
    # request = urllib2.Request(url)
    # Sends the request and catches the response
    response = urllib2.urlopen(request)
    # Extracts the response
    html = response.read()
    # Print it out
    print html


    # Prepare the data
    query_args = { 'q':'query string', 'foo':'bar' }
    # This urlencodes your data (that's why we need to import urllib at the top)
    data = urllib.urlencode(query_args)
    # Send HTTP POST request
    request = urllib2.Request(url, data)
    response = urllib2.urlopen(request)
    print response.info()
    html = response.read()
    # Print the result
    print html

def usage3():
    # Define the url
    url = 'http://www.google.com/#q=my_search'
    # Add your headers
    headers = {'User-Agent' : 'Mozilla 5.10'}
    # Create the Request.
    request = urllib2.Request(url, None, headers)
    # Getting the response
    response = urllib2.urlopen(request)
    # Print the headers
    print response.headers

    # another example
    req = urllib2.Request('http://www.google.com/')
    req.add_header('User-agent', 'Mozilla 5.10')
    res = urllib2.urlopen(req)
    html = res.read()
    print html

def usage5():
    query_args = { 'q':'query string', 'foo':'bar' } # you have to pass in a dictionary
    encoded_args = urllib.urlencode(query_args)
    print 'Encoded:', encoded_args
    url = 'http://python.org/?' + encoded_args
    print urllib2.urlopen(url).read()

def usage6():
    from urllib2 import URLError
    req = urllib2.Request('http://www.pretend_server.org')
    try:
        urllib2.urlopen(req)
    except URLError as e:
        print e.reason


def usage7():
    # basic usage of Urllib2 handler and opener
    # usage of authentication

    # create a password manager
    password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()

    # Add the username and password.
    # If we knew the realm, we could use it instead of ``None``.
    username = 'wenychan'
    password = '123456'
    top_level_url = "http://example.com/foo/"
    a_url = top_level_url
    password_mgr.add_password(None, top_level_url, username, password)

    handler = urllib2.HTTPBasicAuthHandler(password_mgr)

    # create "opener" (OpenerDirector instance)
    opener = urllib2.build_opener(handler)

    # use the opener to fetch a URL
    opener.open(a_url)

    # Install the opener.
    # Now all calls to urllib2.urlopen use our opener.
    urllib2.install_opener(opener)

def usage8():
    # extends HTTPSHandler
    # and make it support client verification
    import httplib
    class HTTPSClientAuthHandler(urllib2.HTTPSHandler):
        def __init__(self, key, cert):
            urllib2.HTTPSHandler.__init__(self)
            self.key = key
            self.cert = cert

        def https_open(self, req):
            # Rather than pass in a reference to a connection class, we pass in
            # a reference to a function which, for all intents and purposes,
            # will behave as a constructor
            return self.do_open(self.getConnection, req)

        def getConnection(self, host, timeout=300):
            return httplib.HTTPSConnection(host, key_file=self.key, cert_file=self.cert)

    opener = urllib2.build_opener(HTTPSClientAuthHandler('C:/Users/wenychan/Desktop/new/key.pem', 'C:/Users/wenychan/Desktop/new/cert.pem'))
    response = opener.open("https://sjmcm1csa2/")
    print 'html: ', response.read()
    print 'info: ', response.info()
    print 'url: ', response.geturl()

def usage9():
    # extends HTTPSHandler
    # and make it support client verification
    # also add trusted CAs to support Server verification
    import httplib
    import socket
    import ssl
    CERT_PATH = 'C:/Users/wenychan/Desktop/tttttt'
    CERT_CHAIN_CONCATED_FILE = CERT_PATH+'/111.pem'

    class ValidHTTPSConnection(httplib.HTTPSConnection):
        "This class allows communication via SSL."
        default_port = httplib.HTTPS_PORT
        def __init__(self, host, *args, **kwargs):
            httplib.HTTPSConnection.__init__(self, host, *args, **kwargs)

        def connect(self):
            "Connect to a host on a given (SSL) port."
            sock = socket.create_connection((self.host, self.port), self.timeout, self.source_address)
            if self._tunnel_host:
                self.sock = sock
                self._tunnel()
            self.sock = ssl.wrap_socket(sock, self.key_file, self.cert_file, ca_certs=CERT_CHAIN_CONCATED_FILE, cert_reqs=ssl.CERT_REQUIRED)
            # self.sock = ssl.wrap_socket(sock, self.key_file, self.cert_file, cert_reqs=ssl.CERT_NONE)

    class ValidHTTPSHandler(urllib2.HTTPSHandler):
        def __init__(self, key, cert, cacert):
            urllib2.HTTPSHandler.__init__(self)
            self.key = key
            self.cert = cert
            self.cacert = cacert

        def https_open(self, req):
            return self.do_open(self.getConnection, req)

        def getConnection(self, host, timeout=300):
            return ValidHTTPSConnection(host, key_file=self.key, cert_file=self.cert)

    opener = urllib2.build_opener(ValidHTTPSHandler('C:/Users/wenychan/Desktop/new/key.pem', 'C:/Users/wenychan/Desktop/new/cert.pem', None))
    response = opener.open("https://sjmcm1csa2/")
    print 'html: ', response.read()
    print 'info: ', response.info()
    print 'url: ', response.geturl()

if __name__ == '__main__':
    usage()

    # usage1()

    # usage2()

    # usage3()

    # usage5()

    # usage6()

    # usage7()

    # usage8()

    # usage9()