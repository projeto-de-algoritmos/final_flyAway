from ..controllers.FlightController import FlightController
from fastapi import Request, Body

class ApiRouter():
    def __init__(self):
        self.flightController = FlightController()

    def getRoutes(self, app):
        @app.get("/flight/list/")
        def getFlights(inBound: str, outBound: str):
            return self.flightController.getFlights(inBound, outBound)

        @app.get("/flight/{flightId}")
        def getFlightById(flightId: int):
            return self.flightController.getFlightById(flightId)
        
        @app.get("/flight/info/{originId}")
        def getFlightsByOriginId(originId: int):
            return self.flightController.getFlightsByOriginId(originId)  
