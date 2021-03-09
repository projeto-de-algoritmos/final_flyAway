from ..services.FlightService import FlightService
from fastapi import HTTPException
from typing import List
from pydantic import BaseModel

class FlightController():
    def __init__(self):
        self.flightService = FlightService()

    def getFlights(self, inBound, outBound) -> List:
        try:
            return self.flightService.getFlights(inBound, outBound)
        except Exception:
            raise HTTPException(status_code=404, detail=Exception)

    def getFlightById(self, flightId: int):
        try:
            return self.flightService.getFlightById(flightId)
        except Exception:
            raise HTTPException(status_code=404, detail=Exception)

    def getFlightsByOriginId(self, originId: int) -> List:
        try:
            return self.flightService.getFlightsByOriginId(originId)
        except Exception:
            raise HTTPException(status_code=404, detail=Exception)