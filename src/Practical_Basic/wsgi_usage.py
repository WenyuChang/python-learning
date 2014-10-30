__author__ = 'wenychan'

# Our tutorial's WSGI server
from wsgiref.simple_server import make_server
from cgi import parse_qs, escape


def application(environ, start_response):

    # the environment variable CONTENT_LENGTH may be empty or missing
    try:
        request_body_size = int(environ.get('CONTENT_LENGTH', 0))
    except (ValueError):
        request_body_size = 0

    ###########################################################################
    # GET
    # Returns a dictionary containing lists as values.
    d = parse_qs(environ['QUERY_STRING'])

    # In this idiom you must issue a list containing a default value.
    var1 = d.get('var1', [''])[0] # Returns the first var1 value.
    var2 = d.get('var2', []) # Returns a list of var2.

    # Always escape user input to avoid script injection
    var1 = escape(var1)
    var2 = [escape(var) for var in var2]
    ###########################################################################



    ###########################################################################
    # POST
    # When the method is POST the query string will be sent
    # in the HTTP request body which is passed by the WSGI server
    # in the file like wsgi.input environment variable.
    request_body = environ['wsgi.input'].read(request_body_size)
    d = parse_qs(request_body)

    var1 = d.get('var1', [''])[0] # Returns the first var1 value.
    var2 = d.get('var2', []) # Returns a list of var2.

    # Always escape user input to avoid script injection
    var1 = escape(var1)
    var2 = [escape(var) for var in var2]
    ###########################################################################


    # Sorting and stringifying the environment key, value pairs
    response_body = ['%s: %s' % (key, value) for key, value in sorted(environ.items())]
    response_body = '\n'.join(response_body)
    status = '200 OK'
    response_headers = [('Content-Type', 'text/plain'), ('Content-Length', str(len(response_body)))]
    start_response(status, response_headers)

    return [response_body]

# Instantiate the WSGI server.
# It will receive the request, pass it to the application
# and send the application's response to the client
httpd = make_server(
   'localhost', # The host name.
   8051, # A port number where to wait for the request.
   application # Our application object name, in this case a function.
   )

# Wait for a single request, serve it and quit.
httpd.handle_request()
