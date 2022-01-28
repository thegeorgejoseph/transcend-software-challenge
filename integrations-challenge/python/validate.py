import re
import logging
import http.client

#Implementing a simple check using Regex to see if the identifier is a valid email - we can prevent future crashes if something as simple as the identifier is not
# in the right format
def validateEmail(identifier):
    regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    if re.fullmatch(regex, identifier):
          return True
    else:
        return False
    
    
def logger():
    logging.basicConfig(filename="std.log",format='%(asctime)s %(message)s', filemode='w') 
    http.client.HTTPConnection.debuglevel = 1
    
    logging.basicConfig()
    logging.getLogger().setLevel(logging.DEBUG)
    requests_log = logging.getLogger("requests.packages.urllib3")
    requests_log.setLevel(logging.DEBUG)
    requests_log.propagate = True
    return