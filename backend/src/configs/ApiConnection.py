import requests

class ApiConnection():
    def __init__(self):
        self.Url = ""
        self.headers = {}
   
    def connect(self, inBound, outBound):
        self.Url = f'https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/browseroutes/v1.0/US/USD/en-US/{inBound}/{outBound}/anytime/anytime'
        
        self.headers = {
            'x-rapidapi-key': "1e1bf49c20mshbe6efec48c3580dp19cf0djsn75e54d6d7ad2",
            'x-rapidapi-host': "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com"
        }

        response = requests.request("GET", Url, headers=headers)

        return response