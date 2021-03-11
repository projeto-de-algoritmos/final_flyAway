from ..controllers.FlightController import FlightController
from fastapi import Request, Body

class ApiRouter():
    def __init__(self):
        self.flightController = FlightController()

    def getRoutes(self, app):
        @app.get("/flight/list/")
        def getFlights(outBound: str, inBound: str):
            return self.flightController.getFlights(outBound, inBound)

        @app.get("/country/list/")
        def getCountry():
            return self.flightController.getCountry()