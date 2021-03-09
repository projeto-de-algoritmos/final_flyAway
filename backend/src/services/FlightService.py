from typing import List
from ..configs.ApiConnection import ApiConnection

class FlightService():
    def __init__(self):
        self.apiConnection = ApiConnection()


    def getFlights(self, inBound, outBound) -> List:
        """Função que gera os nodes

        Args:
            inBound (String): voo de retorno
            outBound ([type]): voo de ida

        Returns:
            List: callback da função
        """
        nodes = []
        edges = []
        requestData = self.apiConnection.connect(inBound, outBound)

        for flight in requestData['Quotes']:
            nodes.append({
                "QuoteId": flight['QuoteId'],
                "Cost": flight['MinPrice'],
                "Origin": self.findById(requestData['Places'], flight['OutboundLeg']['OriginId'], 'PlaceId'),
                "Destiny": self.findById(requestData['Places'], flight['OutboundLeg']['DestinationId'], 'PlaceId')
            })

        edges = self.createEdges(nodes)

        return {
            "nodes": nodes,
            "edges": edges
        }
    
    def findById(self, arr: list, id: int, foreignKey: str):
        query = ""
        for node in arr:
            if node['PlaceId'] == id:
                query = node['Name']
                return query 


    def createEdges(self, graph):
        edges = []

        for node in graph:
            edges.append({
                "from": node['Origin'],
                "to": node['Destiny'],
                "Cost": node['Cost']
            })

        return edges
    