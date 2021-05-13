import requests
import json

class SkyscannerFlights():

    def connect(self, outBound, inBound):
        url = f'https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/browseroutes/v1.0/US/BRL/pt-BR/{outBound}/{inBound}/anytime/anytime'

        headers = {
            'x-rapidapi-key': "1e1bf49c20mshbe6efec48c3580dp19cf0djsn75e54d6d7ad2",
            'x-rapidapi-host': "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com"
        }
        response = requests.get(url, headers=headers)

        return response.json()

class SkyscannerCountries():

    def connect(self):
        url = f'https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/reference/v1.0/countries/pt-BR'

        headers = {
            'x-rapidapi-key': "1e1bf49c20mshbe6efec48c3580dp19cf0djsn75e54d6d7ad2",
            'x-rapidapi-host': "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com"
        }
        response = requests.get(url, headers=headers)

        return response.json()