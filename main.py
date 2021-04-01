import requests
from bs4 import BeautifulSoup as BS
from datetime import datetime

# Define the headers for our request, as well as the URL we will be sending the request to
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0'}
url = 'https://betsapi.com/t/57721/MIA-Heat'

# Parse the page's content to retrieve the last game's date and outcome and return both
def get_latest_game():
    src = response.content
    soup = BS(src, 'lxml')
    tables = soup.find_all('table')
    rows = tables[1].find_all('tr')
    columns = rows[0].find_all('td')
    game_date = columns[1]['data-dt']
    outcome = columns[4].text
    return game_date, outcome

# Get current date and time, reformat to match format of the last game's date pulled from the site
# Parse both to turn them into datetime objects and return their values
def format_and_parse_dates(game_date):
    today_string = datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ')
    todays_date_parsed = datetime.strptime(today_string, '%Y-%m-%dT%H:%M:%SZ')
    games_date_parsed = datetime.strptime(game_date, '%Y-%m-%dT%H:%M:%SZ')
    return todays_date_parsed, games_date_parsed

# Get the difference between current date/time and the last game's date/time; returns x days, hh:mm:ss
# To make it easer for our compare function below, convert the duration to seconds and return the value
def get_seconds_since_win(todays_date_parsed, games_date_parsed):
    difference = abs(todays_date_parsed - games_date_parsed)
    seconds_since_win = (difference.days * 86400) + difference.seconds
    return seconds_since_win

# Compare the last game's outcome to known outcomes that the website provides and provide an appropriate result.
# If, and only if, the outcome is "W" for "win", run the get_seconds_since_win function to calculate the duration
# and check if it's below the 36-hour mark.
def compare(outcome):
    # It seems like the promo code is valid for more than 24 hours, so 36 hours is arbitrary until a closer duration is determined, if ever
    thirty_six_hours = 129600
    if outcome == 'W':
        if get_seconds_since_win(todays_date_parsed, games_date_parsed) < thirty_six_hours:
            result = "The Miami Heat recently won! Promo code HEATWIN is valid."
    elif outcome == 'L':
        result = "The Miami Heat recently lost."
    elif outcome == '-':
        result = "The Miami Heat's latest game was postponed."
    elif outcome == 'D':
        result = "The Miami Heat's latest game ended in a draw."
    return result

# Send GET request using predetermined URL and headers
response = requests.get(url, headers=headers)
# If the response from the page is 200 (OK), proceed; otherwise, tell the user there is no response
if response.status_code == 200:
    game_date, outcome = get_latest_game()
    todays_date_parsed, games_date_parsed = format_and_parse_dates(game_date)
    result = compare(outcome)
    print(result)
else:
    print("No response from webpage.")