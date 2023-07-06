import time

from functions.locations import get_points
from functions.model_profile import model_profile
from functions.pars_data import parser, scan_photos_id
from webbrowser.multilogin_api import create_profile, update_profile_proxy, update_profile_geo, create_driver


def new_session(session_name, proxy_host, proxy_port, proxy_type, proxy_username, proxy_password, latitude, longitude,
                port, city):
    """Creating new session"""
    profile_id = create_profile(session_name=session_name, port=port)
    time.sleep(2)
    update_profile_proxy(profile_id=str(profile_id), proxy_port=proxy_port, proxy_username=proxy_username,
                         proxy_host=proxy_host,
                         proxy_password=proxy_password, proxy_type=proxy_type, port=str(port))
    latitude, longitude = get_points(city)
    update_profile_geo(profile_id, latitude, longitude, port)
    time.sleep(2)
    driver = create_driver(profile_id, port)

    return driver


def start_session(port, city):
    """Starting session"""
    email, password, reserve, session_name, proxy_host, proxy_port, proxy_username, proxy_password = parser(
        "data/data.xlsx")

    latitude, longitude = get_points(city)
    proxy_host = proxy_host
    proxy_type = "SOCKS"
    proxy_username = proxy_username
    proxy_password = proxy_password
    proxy_port = proxy_port

    photos_folder = scan_photos_id(session_name)

    driver = new_session(session_name, proxy_host, proxy_port, proxy_type, proxy_username, proxy_password, latitude,
                         longitude, port, city)

    return email, password, reserve, driver, photos_folder
