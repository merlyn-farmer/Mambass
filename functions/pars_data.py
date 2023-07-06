import re

import pandas as pd


def scan_photos_id(session_name):
    result = re.search(r"/(.+?)/", session_name)
    if result:
        photo_id = result.group(1)
        return photo_id


def parser(file):
    """parsing session excel"""
    df = pd.read_excel(file, dtype=str)
    row = df.iloc[0]
    email, passw, reserv, name, p_ip, p_port, p_login, p_pass = row[0], row[1], row[2], row[3], \
        row[4], row[5], row[6], row[7]
    parsed_df = df.iloc[1:]
    parsed_df.to_excel(file, index=False)

    return email, passw, reserv, name, p_ip, p_port, p_login, p_pass
