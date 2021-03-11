import Connection from './Connection';

class FlightService extends Connection {
    constructor() {
        super();
    }

    async getFlights(inBound = "", outBound = "") {
        const outBoundQuery = outBound ? `?outBound=${outBound}` : ""
        const inBoundQuery = inBound ? `&inBound=${inBound}` : ""
        
        return await this.client.get(`/flight/list/${outBoundQuery}${inBoundQuery}`)
    }

    async getCountry() {
        return await this.client.get(`/country/list/`)
    }

}

export default FlightService;