from ..services.FlightService import FlightService
from fastapi import HTTPException

class FlightController():
    def __init__(self):
        self.flightService = FlightService()

    async def getFlights(self):
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
