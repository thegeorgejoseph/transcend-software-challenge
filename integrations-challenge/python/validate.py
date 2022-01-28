import re

#Implementing a simple check using Regex to see if the identifier is a valid email - we can prevent future crashes if something as simple as the identifier is not
# in the right format
def validateEmail(identifier):
    regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    if re.fullmatch(regex, identifier):
          return True
    else:
        return False