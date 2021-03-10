from typing import List
from ..configs.ApiConnection import ApiConnection

class FlightService():
    def __init__(self):
        self.apiConnection = ApiConnection()


    def getFlights(self, outBound, inBound) -> List:
        nodes = []
        edges = []
        requestData = self.apiConnection.connect(outBound, inBound)

        nodes = self.getPlaces(requestData)
        edges = self.createEdges(requestData)

        return {
            "nodes": nodes,
            "edges": edges
        }

    def getPlaces(self, requestData):
        places = []

        for node in requestData['Places']:
            if node['Type'] == "Station":
                places.append({
                    "placeId": node['PlaceId'],
                    "cityName": node['CityName'],
                    "cityIdStr": node['CityId'],
                    "name": node['Name'],
                    "country": node['CountryName']
                })

        return places
    
    def findById(self, arr: list, id: int, foreignKey: str):
        query = ""
        for node in arr:
            if node['PlaceId'] == id:
                query = node['Name']
                return query 


    def createEdges(self, requestData):
        edges = []

        for quote in requestData['Quotes']:
            edge = (quote['OutboundLeg']['OriginId'], quote['OutboundLeg']['DestinationId'], quote['MinPrice'])
            edges.append({
                "from": edge[0],
                "to": edge[1],
                "cost": edge[2]
            })

        return edges
    