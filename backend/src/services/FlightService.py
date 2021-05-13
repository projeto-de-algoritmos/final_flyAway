from typing import List
from ..configs.ApiConnection import SkyscannerFlights, SkyscannerCountries
from ..utils.scripts import mergeSort


class FlightService():
    def __init__(self):
        self.skyscannerFlights = SkyscannerFlights()
        self.skyscannerCountries = SkyscannerCountries()

    def getFlights(self, outBound, inBound) -> List:
        nodes = []
        edges = []
        requestData = self.skyscannerFlights.connect(outBound, inBound)

        nodes = self.getPlaces(requestData)
        edges = self.createEdges(requestData)

        return {
            "nodes": nodes,
            "edges": edges
        }

    def getCountry(self) -> List:
        countries = []
        sorted_countries = []
        requestData = self.skyscannerCountries.connect()

        for node in requestData['Countries']:
            countries.append({
                "name": node['Name'],
                "code": node['Code']
            })

        sorted_countries = mergeSort(countries)

        return sorted_countries


    def getPlaces(self, requestData):
        places = []

        for node in requestData['Places']:
            if node['Type'] == "Station":
                places.append({
                    "id": node['PlaceId'],
                    "cityName": node['CityName'],
                    "cityIdStr": node['CityId'],
                    "name": node['Name'],
                    "country": node['CountryName'],
                    "label": f'{node["CityName"]} - { node["IataCode"]}'
                })

        return places

    def createEdges(self, requestData):
        edges = []

        for quote in requestData['Quotes']:
            edge = (quote['OutboundLeg']['OriginId'], quote['OutboundLeg']['DestinationId'], quote['MinPrice'])
            edges.append({
                "from": edge[0],
                "to": edge[1],
                "label": f'R$ {str(edge[2])}'
            })

        return edges
    