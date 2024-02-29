""" This app checks the price of biticoin using  http://www.coindesk.com/api 
As an alternative, it can use a different API that provides mock data: https://claraj.github.io/mock-bitcoin/currentprice.json. 
Or use  https://api.coindesk.com/v1/bpi/currentprice.json"""

import requests

# url = 'http://www.coindesk.com/api' # API Not functional
# url = 'https://claraj.github.io/mock-bitcoin/currentprice.json'

url = 'https://api.coindesk.com/v1/bpi/currentprice.json'


def main():
    number_of_bitcoin = input('How money bitcoin do you want to convert? ')
    response, error = make_api_request(url) # Handle exceptions in program?
    if error:
        print(error)
        print("Could not get api response")
        return
    if response:
        rate, error = get_rate_from_api_response(response)
        if error:
            print(error)
            print("Api response not structured as expected")
            return
        if rate:
            print_current_rate(rate)
            rate = convert_string_to_float(rate)
            number_of_bitcoin = convert_string_to_float(number_of_bitcoin)
            total = calculate_bitcoin_total(rate, number_of_bitcoin)
            print_total(total)


def print_current_rate(rate):
    print(f'The rate of the USD is ${rate}')


def calculate_bitcoin_total(rate, user_bitcoin):
    return rate * user_bitcoin


def print_total(total):
    print(f'The total amount of USD of your bitcoin is $ {total}')


def convert_string_to_float(str):
    return float(str)


def make_api_request(url):
    try:
        response = requests.get(url).json()
        return response, None
    except Exception as e:
        return None, e


def get_rate_from_api_response(response):
    try:
        rate = response['bpi']['USD']['rate_float']
        return rate, None
    except Exception as e:
        return None, e
    

if __name__ == '__main__':
    main()
