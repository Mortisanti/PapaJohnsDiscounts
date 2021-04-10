import requests
import json

pj_url = 'https://www.papajohns.com/'
validate_url = 'https://www.papajohns.com/order/validate-promo'
store_search_url = 'https://www.papajohns.com/order/storesSearch'

headers1 = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Cache-Control': 'max-age=0',
    'TE': 'Trailers',
}

headers2 = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Referer': 'https://www.papajohns.com/order/stores-near-me?target=/menu&searchType=DELIVERY',
    'Request-Source': 'freight',
    'X-Requested-With': 'XMLHttpRequest',
    'ADRUM': 'isAjax:true',
    'Connection': 'keep-alive',
}

headers3 = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
}

# 
params2 = (
    ('searchType', 'DELIVERY'),
    ('target', '/menu'),
    ('latitude', '25.7659471'),
    ('longitude', '-80.20099669999999'),
    ('country', 'usa'),
    ('locationType', 'HOME'),
    ('university-state', '10'),
    ('university-province', ''),
    ('us-campus', ''),
    ('canada-campus', ''),
    ('campus-dorm', ''),
    ('campus-roomnumber', ''),
    ('military-state', '10'),
    ('military-province', ''),
    ('us-base', ''),
    ('canada-base', ''),
    ('military-building', ''),
    ('military-buildingnumber', ''),
    ('military-roomnumber', ''),
    ('input-autocomplete', '400 Southwest 8th Street'),
    ('streetaddress', '400 Southwest 8th Street'),
    ('aptstefloor', 'NON'),
    ('residential-us-city', 'Miami'),
    ('residential-state', 'FL'),
    ('zipcode', '33130'),
    ('residential-canada-city', ''),
    ('residential-province', ''),
    ('postalcode', '33130'),
)

params3 = (
    ('promo-code', 'HEATWIN'),
)


# Start a session; needed to handle reception and storage of cookies.
# The cookies are a necessity in order for the website to check the "user's" location.
# The location is a necessity because the promo code is restricted to Central and South Florida.
s = requests.Session()

s.get(pj_url, headers=headers1)
s.get(store_search_url, headers=headers2, params=params2)
r = s.get(validate_url, headers=headers3, params=params3)
result_dict = json.loads(r.text)
promo_status = result_dict['isPromoApplied']

if promo_status == 'true':
    print("The promo code HEATWIN is valid.")
else:
    print("The promo code HEATWIN is invalid.")