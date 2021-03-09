from ..services.FlightService import FlightService
from fastapi import HTTPException
from typing import List
from pydantic import BaseModel

class FlightController():
    def __init__(self):
        self.flightService = FlightService()

    def getFlights(self, inBound: str, outBound: str) -> List:
        try:
            return self.flightService.getFlights(inBound, outBound)
        except Exception:
            raise HTTPException(status_code=404, detail=Exception)