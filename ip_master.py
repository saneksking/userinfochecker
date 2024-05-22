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

    def get_hostname(self):
        return self.data['hostname']

    def get_city(self):
        return self.data['city']

    def get_region(self):
        return self.data['region']

    def get_country(self):
        return self.data['country']

    def get_loc(self):
        return self.data['loc']

    def get_org(self):
        return self.data['org']

    def get_postal(self):
        return self.data['postal']

    def get_timezone(self):
        return self.data['timezone']

    def all_user_info(self):
        return self.data
