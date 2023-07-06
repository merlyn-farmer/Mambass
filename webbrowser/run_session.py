import time

from functions.group_id import group_id_list
from functions.locations import get_points
from functions.model_profile import model_profile
from functions.pars_data import parser, scan_photos_id
from webbrowser.multilogin_api import create_profile, update_profile_proxy, update_profile_geo, create_driver, \
    update_profile_group


def new_session(session_name, proxy_host, proxy_port, proxy_type, proxy_username, proxy_password, latitude, longitude,
                port, city, group_ids):
    """Creating new session"""
    profile_id = create_profile(session_name=session_name, port=port)
    time.sleep(2)
    update_profile_proxy(profile_id=str(profile_id), proxy_port=proxy_port, proxy_username=proxy_username,
                         proxy_host=proxy_host,
                         proxy_password=proxy_password, proxy_type=proxy_type, port=str(port))
    latitude, longitude = get_points(city)

    update_profile_geo(profile_id, latitude, longitude, port)
    update_profile_group(profile_id, port, group_ids)
    time.sleep(2)
    driver = create_driver(profile_id, port)

    return driver


def start_session(port, city, group_id):
    """Starting session"""
    email, password, reserve, session_name, proxy_host, proxy_port, proxy_username, proxy_password = parser(
        "data/data.xlsx")
    group_ids = group_id_list(group_id, port)
    latitude, longitude = get_points(city)
    proxy_host = proxy_host
    proxy_type = "SOCKS"
    proxy_username = proxy_username
    proxy_password = proxy_password
    proxy_port = proxy_port

    photos_folder = scan_photos_id(session_name)
    print(f'port - {port}, session_name - {session_name}')
    driver = new_session(session_name, proxy_host, proxy_port, proxy_type, proxy_username, proxy_password, latitude,
                         longitude, port, city, group_ids)

    return email, password, reserve, driver, photos_folder, session_name
