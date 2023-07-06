import re
import time
import traceback

from functions.check_mail import check
from functions.config import Config, config_data
from functions.model_profile import model_profile
from webbrowser.google_auth import google_auth
from webbrowser.login_mamba import mamba_login, send_code
from webbrowser.run_session import start_session
from functions.logs import log_dispatcher


email, password, reserve, driver, photos_folder, session_name = None, None, None, None, None, None


def registration(port, city, i_func_name=0, group_id=None):

    all_func_name = ['start_session(port, city, group_id)', 'google_auth(driver, email, password, reserve)',
                     'mamba_login(driver, email)', 'send_code(driver)',
                     'model_profile(driver=driver, photos_folder=photos_folder)',
                     'log_dispatcher.info(to_write=session_name)']

    for i in range(len(all_func_name)):
        try:
            if i_func_name == 0:
                print(all_func_name[i_func_name])
                global email, password, reserve, driver, photos_folder, session_name
                email, password, reserve, driver, photos_folder, session_name = eval(f'{all_func_name[i_func_name]}')
                i_func_name += 1
                time.sleep(5)
                print('first finaly')
            else:
                print(i)
                print(all_func_name[i_func_name])
                time.sleep(8)
                eval(f'{all_func_name[i_func_name]}')

                i_func_name += 1

        except IndexError:
            i_func_name *= 0
            raise StopIteration

        except Exception as ex:
            error_traceback = traceback.format_exc()
            print(error_traceback)
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
                raise StopIteration

            elif pattern_next.search(command):
                registration(port, city, i_func_name=int(i_func_name + 1))

            elif pattern_re.search(command):
                registration(port, city, i_func_name=i_func_name)

            elif pattern_ky.search(command):
                print('Панки хой!')
                registration(port, city, i_func_name=i_func_name)

            elif pattern_exit.search(command):
                return

            else:
                command = input('Ты ввёл не корректную команду, я не местный.Доступные команды:\n'
                                're, skip, next\n'
                                'Скрипт закроется после ввода любого текста, впредь пиши правильно')
                raise Exception('uncorrect command')


if __name__ == '__main__':
    mail_count = check()
    if mail_count:
        for _ in range(mail_count):
            print('SKIP sucsesfull')
            try:
                registration(config_data.get_port, config_data.get_city, group_id=config_data.get_group_id)
                time.sleep(20)
            except StopIteration:
                pass