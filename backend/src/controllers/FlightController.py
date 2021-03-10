from ..services.FlightService import FlightService
from fastapi import HTTPException
from typing import List
from pydantic import BaseModel

class FlightController():
    def __init__(self):
        self.flightService = FlightService()

    def getFlights(self,  outBound: str, inBound: str) -> List:
        try:
            return self.flightService.getFlights(outBound, inBound)
        except Exception:
            raise HTTPException(status_code=404, detail=Exception)