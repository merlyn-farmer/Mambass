import os
import time

import openpyxl

from functions.config import config_data


def check_gmail():
    workbook = openpyxl.load_workbook('data/data.xlsx')
    worksheet = workbook['Sheet1']
    count_email = 0
    for cell in worksheet['A2:A' + str(worksheet.max_row)]:
        for row in cell:
            if row.value:
                count_email += 1

    return count_email


def check():
    count_email = None

    if os.path.exists(config_data.get_photos_dir):
        msg = 'Путь в норме'
        print(msg)
    else:
        msg = 'Путь не верный'
        print(msg)

    time.sleep(0.5)
    try:
        count_email = check_gmail()
        msg = f'Кол-во почт в программе: {count_email}'
        print(msg)
    except Exception as ex:
        print(ex)

    time.sleep(0.5)

    return count_email
