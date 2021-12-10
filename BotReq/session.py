import re as re
import requests

import requests
import re

 
class Session:
    def __init__(self,url):
        self.session = requests.session()
        self.sessionUrl = url
        res = self.session = self.session.get(url)
        self.sessionText = res.text

    
    #todo doc
    def findElementByRegex(self,searchString):
        if(self.session== None):
            raise ValueError("session was None, before calling findElement() call createSession() to create a session.")
        return re.findall(searchString,self.sessionText,re.MULTILINE)
    
    #todo doc
    def getCookies(self):
        print(self.session.cookies.get_dict())