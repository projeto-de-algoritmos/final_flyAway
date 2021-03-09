from typing import List
from ..configs.ApiConnection import ApiConnection

class FlightService():
    def __init__(self):
        self.apiConnection = ApiConnection()


    def getFlights(self, inBound, outBound) -> List:
        flights = []
        requestData = self.apiConnection.connect(inBound, outBound)

        for flight in requestData.Quotes:
            flights.append({
                "QuoteId": flight['QuoteId'],
                "Cost": flight['MinPrice'],
                "Origin": self.findById(requestData.Places, flight.InboundLeg['OriginId'], 'PlaceId', 'Name'),
                "Destiny": self.findById(requestData.Places, flight.InboundLeg['DestinationId'], 'PlaceId', 'Name')
            })
        
        return flights
    
    def findById(arr: list, id: int, foreignKey: str, key: str):
        query = ""
        for id in arr:
            if id == arr[foreignKey]:
                query = arr[key]
        
        return query

    def createNodes(self, graph):
        nodes = [ node for node in graph ]

        return nodes

    def createEdges(self, graph):
        edgeList = []

        for node in graph:
            edgeList.append({
                "from": graph.get('OriginId'),
                "to": graph.get('DestinationId')
            })

        return edgeList
    