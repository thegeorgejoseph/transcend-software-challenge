import mailgunDatapoints as dp
import json

class Testing:
    def __init__(self):
        self.identifier = 'mike@transcend.io'
        
    #testing access logic with seed input
    def test_access(self):
        return dp.access(self.identifier)['data'][0] == "484848@sandbox7743ee8a12e6444883a136ec1e3b41f2.mailgun.org"
    
    #most cases of errors are in mailing logic, testing with seed input
    def test_mailing_list(self):
        f = open("cache.json")
        cache = json.load(f)
        return cache["111@sandbox7743ee8a12e6444883a136ec1e3b41f2.mailgun.org"][0] == "bar2@example.com"
    
    def main(self):
        access_test = self.test_access()
        mailing_test = self.test_mailing_list()
        if access_test and mailing_test:
            print("All Tests Passed")
        elif access_test is False:
            print("Error in Access")
        elif mailing_test is False:
            print("Specific error in Mailing List")
        
if __name__ == "__main__":
    tester = Testing()
    tester.main()
    