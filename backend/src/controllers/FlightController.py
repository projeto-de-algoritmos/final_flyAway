from ..services.FlightService import FlightService
from fastapi import HTTPException
import requests

class FlightController():
    def __init__(self, currency, locale, originCountry, quotes, places):
        self.flightService = FlightService()
        self.currency = currency
        self.locale = locale
        self.rootURL = "https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/browseroutes/v1.0
        self.originCountry = originCountry
        self.quotes = []
        self.places = []

    async def getFlights(self, rootURL, currency, locale, rootURL, originCountry, sourceCountry, destinationCountry, date, returnDate):

        url = rootURL + "/" + originCountry + "/" + currency + "/" + locale + "/" + sourceCountry + "/" destinationCountry + "/" + date.strftime("%Y-%m-%d")

        querystring = {"inboundpartialdate": returnDate.strftime("%Y-%m-%d")}
        
        headers = {
            'x-rapidapi-key': "1e1bf49c20mshbe6efec48c3580dp19cf0djsn75e54d6d7ad2",
            'x-rapidapi-host': "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com"
        }

        result = requests.request("GET", url, headers=headers, params=querystring)
        """getFlights Controller

        Raises:
            HTTPException: caso não encontrar lança exception

        Returns:
            [Object]: Retorna um array de objetos validado pela service
        """
        try:
            result = await self.flightService.getFlights()
            return result
        except Exception:
            raise HTTPException(status_code=404, detail=Exception)
