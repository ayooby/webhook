import cgi,requests,logging
#ssdsdsd
form = cgi.FieldStorage()

logging.basicConfig(filename='posts.log',level=logging.DEBUG)
logging.debug(form["username"])
logging.debug(form)
