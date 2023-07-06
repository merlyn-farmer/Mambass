import requests

domain = '5sim.biz'
apikey = 'eyJhbGciOiJSUzUxMiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MTQ0OTQ5NjUsImlhdCI6MTY4Mjk1ODk2NSw' \
         'icmF5IjoiYTI4ODM2NzIxMDI4NTMzOWRmYzk5ZmE0YWUzNmI4ZTkiLCJzdWIiOjE2MTczNzV9.qz5KfbQyOvc' \
         'hxeEPnEO--faVgNn-8O-R4iiXSoilZc8qMDg2SIM7lY4QthQA3kDUIvdvOBSPb5Digbx49jgvOVaxgbLQbD1a' \
         'RaYpz0L_-uAwbusa6OHPIkmROz2qmMqRl8fBe-GzBT24HJowZEzEHd4rm7AlTzH5dDYVpeqCsqdmTWNkOWrgo8' \
         'FWnGsy9q3EP2bCAJchqN6h8M1XmC_1saoTXD51GxDaJtRiYVFtaDBvJwQkBQmfZdyjXRGraZ7Hv_KWu4PS7Yfs' \
         'NAy1asTs509d9kAvn_v1LBZjY1E33hFQa6BKdchHlis5-Gq5KuiznmfgFhCMvAxO1uAyWC6k9g'
product = 'mamba'


def country_number(countries):
    country = None
    operator = None

    match countries:
        case "eng":
            country = 'england'
            operator = 'virtual26'
        case "lit":
            country = 'lithuania'
            operator = 'virtual26'
        case "ger":
            country = 'germany'
            operator = 'virtual26'
        case "aus":
            country = 'austria'
            operator = 'virtual38'

    return country, operator


def five_sim_buy(country, operator):
    phone = None
    num_id = None

    url_buy = f'https://{domain}/v1/user/buy/activation/{country}/{operator}/{product}'
    headers = {
        'Authorization': f'Bearer {apikey}',
        'Accept': 'application/json'
    }
    buy = requests.get(url_buy, headers=headers)
    print(buy)
    try:
        phone = buy.json()['phone']
        num_id = buy.json()['id']
        print(num_id)
    except:
        pass
    # gr - +49, eng - +44, aus - +61, Lithuania - +370

    if country == 'lit':
        phone = phone[4:]
        print(phone)
    else:
        print(phone)
        phone = phone[3:]

    return phone, num_id


def five_sim_check(num_id):
    headers = {
        'Authorization': f'Bearer {apikey}',
        'Accept': 'application/json'
    }
    url_check = f'https://{domain}/v1/user/check/{num_id}'
    check = requests.get(url_check, headers=headers)
    print(check.text)
    try:
        sms_code = check.json()["sms"][0]["code"]
        print(sms_code)
        return sms_code

    except:
        print("Код не пришел")
        return False
