import requests
import json
import time
from settings import *


class ApiMethodRequest:
    def __init__(self, method, parameters, api_version):
        self.method = method
        self.parameters = parameters
        self.api_version = api_version

        self.request_url = ""

        self.generate_request_url()

    def generate_request_url(self):
        parameters = self.parameters
        parameters["v"] = self.api_version
        parameters["access_token"] = TOKEN

        parameters_str = "&".join([(parameter + "=" + str(self.parameters[parameter])) for parameter in self.parameters])

        self.request_url = API_METHOD_URL + self.method + "?" + parameters_str

    def is_error(self):
        if self.request_url != "":
            while True:
                response_json = json.loads(requests.get(self.request_url).text)
                if "response" in response_json:
                    time.sleep(DELAY_TIME)
                    return False
                if response_json["error"]["error_code"] != 6: return True
                time.sleep(ERROR_DELAY_TIME)

    def do_request(self):
        if self.request_url != "":
            while True:
                response_json = json.loads(requests.get(self.request_url).text)
                if "response" in response_json:
                    time.sleep(DELAY_TIME)
                    return response_json
                time.sleep(ERROR_DELAY_TIME)
                print(response_json["error"]["error_code"])
                print(response_json)
