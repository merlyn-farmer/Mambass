import re
import time

from functions.check_mail import check
from functions.config import Config, config_data
from functions.model_profile import model_profile
from webbrowser.google_auth import google_auth
from webbrowser.login_mamba import mamba_login
from webbrowser.run_session import start_session

email, password, reserve, driver, photos_folder = None, None, None, None, None


def registration(port, city, i_func_name=0):

    all_func_name = ['start_session(port, city)', 'google_auth(driver, email, password, reserve)',
                     'mamba_login(driver, email)', 'model_profile(driver=driver, photos_folder=photos_folder)',
                     'print("finaly!")']
    for _ in range(len(all_func_name)):
        try:
            if i_func_name == 0:
                print(all_func_name[i_func_name])
                global email, password, reserve, driver, photos_folder
                email, password, reserve, driver, photos_folder = eval(f'{all_func_name[i_func_name]}')
                i_func_name += 1
                time.sleep(5)
                print('first finaly')
            else:
                print(all_func_name[i_func_name])
                eval(f'{all_func_name[i_func_name]}')
                time.sleep(8)
                i_func_name += 1

        except Exception as ex:
            print(ex)
            command = input('Ожидаю команду...\n')
            print(i_func_name)
            pattern_skip = re.compile(r"skip", re.IGNORECASE)
            pattern_next = re.compile(r"next", re.IGNORECASE)
            pattern_re = re.compile(r"re", re.IGNORECASE)
            pattern_ky = re.compile(r"ку", re.IGNORECASE)
            pattern_exit = re.compile(r"exit", re.IGNORECASE)

            if pattern_skip.search(command):
                print('skip..')

                i_func_name *= 0
                return

            elif pattern_next.search(command):
                registration(port, city, i_func_name=int(i_func_name + 1))

            elif pattern_re.search(command):
                registration(port, city, i_func_name=i_func_name)

            elif pattern_ky.search(command):
                registration(port, city, i_func_name=i_func_name)

            elif pattern_exit.search(command):
                return

            else:
                command = input('Ты ввёл не корректную команду, я не местный.Доступные команды:\n'
                                're, skip, next\n'
                                'Скрипт закроется после ввода любого текста, впредь пиши правильно')
                raise Exception('uncorrect command')

    # try:
    #     email, password, reserve, driver, photos_folder = start_session(port, city)
    #     i_func_name += 1
    #     google_auth(driver, email, password, reserve)
    #     i_func_name += 1
    #     mamba_login(driver, email)
    #     i_func_name += 1
    #     time.sleep(3)
    #     model_profile(driver=driver, photos_folder=photos_folder)
    #     i_func_name += 1
    #
    # except Exception as ex:
    #     print(ex)


if __name__ == '__main__':
    mail_count = check()
    if mail_count:
        for _ in range(mail_count):
            registration(config_data.get_port, config_data.get_city)
            time.sleep(20)
