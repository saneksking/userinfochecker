import requests


class UserInfoChecker:
    def __init__(self):
        self.api_url: str = 'https://ipinfo.io/json'
        self.data: dict = self.__init()

    def __init(self):
        response = requests.get(self.api_url)
        if response.status_code == 200:
            data: dict = response.json()
            del data['readme']
        else:
            data: dict = {
                'ip': '',
                'hostname': '',
                'city': '',
                'region': '',
                'country': '',
                'loc': '',
                'org': '',
                'postal': '',
                'timezone': ''
            }
        return data

    def get_ip_address(self):
        return self.data['ip']

    def all_user_info(self):
        return self.data
