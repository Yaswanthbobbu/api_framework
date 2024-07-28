from dataclasses import dataclass

import requests


@dataclass
class APIResponse:
    status_code: int
    text: str
    as_dict: dict
    headers: dict


class APIRequest:
    def post_request(self, url, payload, headers):
        response = requests.post(url=url, json=payload, headers=headers, verify=False)
        return self.__get_responses(response)

    def get_request(self, url, headers):
        response = requests.get(url=url, headers=headers, verify=False)
        return self.__get_responses(response)

    def put_request(self, url, payload, headers):
        response = requests.put(url=url, json=payload, headers=headers, verify=False)
        return self.__get_responses(response)

    def delete_request(self, url, headers):
        response = requests.delete(url=url, headers=headers, verify=False)
        return self.__get_responses(response)

    @staticmethod
    def __get_responses(response):
        status_code = response.status_code
        text = response.text
        try:
            as_dict = response.json()
        except ValueError:
            as_dict = {}
        headers = response.headers
        return APIResponse(status_code, text, as_dict, headers)

    # def call_method(method, endpoint, payload, token):
    #     uri = "https://api.test.productselect.skf.com" + endpoint
    #     headers = {
    #         "content-type": "application/json",
    #         "Authorization": token
    #     }
    #     if method == 'GET':
    #         api_response = requests.request("GET", uri)
    #         return api_response
    #
    #     if method == 'POST' or 'PUT':
    #         body = payload
    #         api_response = requests.request(method, uri, data=payload, headers=headers)
    #         return api_response
