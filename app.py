from output_decorator import StringDecorator
from ip_master import UserInfoChecker
from system_info_checker import SystemInfoChecker


def main():
    sd = StringDecorator()
    sd.string_decorate()
    sd.string_decorate(text='User Info Checker')
    sd.string_decorate(
        text='Program for get IP address and all info of user'
    )
    sd.string_decorate(symbol='-')
    sys_info = SystemInfoChecker()
    print(f'Information of user {sys_info.get_username()}:')
    # app ----------------------------------------
    ip = UserInfoChecker()
    for k, v in ip.data.items():
        print(f'{k}: {v}')
    # --------------------------------------------

    sd.string_decorate(symbol='=')
    sd.string_decorate(text='https://github.com/saneksking/')
    sd.string_decorate(symbol='=')


if __name__ == '__main__':
    main()
