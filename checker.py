import grequests
from requests import Response

class Status:
    incorrect_url: int = -2
    fail: int = -1
    redirect: int = 0
    succes: int = 1

class Checker:
    def __init__(self, url_list: list) -> None:
        self.urls = url_list
        self.requests: dict = {}
        self.responses: list = []
        self.a:list = []
        self.raw_responses: list = []
        print("")
        
    def parse_code(code) -> Status:
        if(code!=None):
            if(code.status_code==200):
                return Status.succes
            if(code.status_code==404):
                return Status.fail
            if(code.status_code in [302,303,307,308]):
                return Status.redirect
        return Status.incorrect_url
    def check(self) -> list:
        for domain in self.urls:
            self.requests[domain] = grequests.get(domain)
        raw_responses = grequests.map(self.requests.values())
        for index, response in enumerate(raw_responses):
            response: Response = response
            self.responses.append({list(self.urls.keys())[index]:Checker.parse_code(response)})
        return self.responses