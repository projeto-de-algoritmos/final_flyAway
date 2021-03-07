class ApiRouter():
    def __init__(self):
        self.api = None

    def getRoutes(self, app):

        @app.get("/flights/")
        async def getFlights():
            return { "message": "yeah!" }

    
