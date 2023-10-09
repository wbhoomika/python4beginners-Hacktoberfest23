import requests

def countryInfo():
    """basic country info api call"""
    name = input('enter county name')
    url = f'https://restcountries.com/v3.1/name/{name}'

    try:
        req = requests.get(url)
        data = req.json()
        capital = data[0]['capital']
        flags = data[0]['flags']
       
        print( {
            "country": name,
            "capital": capital,
            "flag": flags['alt']
        } )
    
    except requests.exceptions.HTTPError as e:
        print('HTTP Error:', e)
    except requests.exceptions.RequestException as e:
        print('Request Error:', e)

countryInfo()