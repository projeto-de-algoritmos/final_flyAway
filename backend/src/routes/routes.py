from ..controllers.FlightController import FlightController

class ApiRouter():
    def __init__(self):
        self.flightController = FlightController()

    def getRoutes(self, app):
        @app.get("/flights/")
        async def getFlights():
            return self.flightController.getFlights()

    
