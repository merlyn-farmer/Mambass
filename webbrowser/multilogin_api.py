from selenium import webdriver

import json
import requests


def create_profile(session_name, port):
    """create profile"""
    x = {
        "name": f"{session_name}",
        "browser": "mimic",
        "os": "win",
        "enableLock": True
    }
    header = {
        "accept": "application/json",
        "Content-Type": "application/json"
    }
    url = f"http://localhost:{port}/api/v2/profile"
    req = requests.post(url, data=json.dumps(x), headers=header)

    return json.loads(req.content).get("uuid")


def update_profile_proxy(profile_id, proxy_type, proxy_host, proxy_port, proxy_username, proxy_password, port):
    """update profile proxy"""
    url = f'http://localhost:{port}/api/v2/profile/' + profile_id
    header = {
        "accept": "application/json",
        "Content-Type": "application/json"
    }
    data = {
        "network": {
            "proxy": {
                "type": proxy_type,
                "host": proxy_host,
                "port": proxy_port,
                "username": proxy_username,
                "password": proxy_password
            }
        }
    }
    r = requests.post(url, json.dumps(data), headers=header)
    print(r.status_code)


def update_profile_geo(profile_id, latitude, longitude, port):
    """update profile geo"""
    url = f'http://localhost:{port}/api/v2/profile/' + profile_id
    header = {
        "accept": "application/json",
        "Content-Type": "application/json"
    }
    data = {
        "geolocation": {
            "mode": "ALLOW",
            "fillBasedOnExternalIp": False,
            "lat": latitude,
            "lng": longitude,
            "accuracy": "100"
        },
        "mediaDevices": {
            "mode": "REAL"
        },
    }
    r = requests.post(url, json.dumps(data), headers=header)
    print(r.status_code)


def update_profile_group(profile_id, port, group_id):
    """Update profile group"""
    url = f'http://localhost:{port}/api/v2/profile/' + profile_id
    header = {
        "accept": "application/json",
        "Content-Type": "application/json"
    }
    data = {
        "group": group_id,
    }
    r = requests.post(url, json.dumps(data), headers=header)


def create_driver(session, port):
    """create driver"""
    mla_url = f'http://127.0.0.1:{port}/api/v1/profile/start?automation=true&profileId=' + session
    resp = requests.get(mla_url)
    js_data = resp.json()
    print(js_data)
    options = webdriver.ChromeOptions()
    options.add_argument("--use-fake-ui-for-media-stream")
    options.add_argument("--use-fake-device-for-media-stream")
    driver = webdriver.Remote(command_executor=js_data['value'], options=options)
    return driver
