import Connection from './Connection';

class FlightService extends Connection {
    constructor() {
        super();
    }

    async getFlights(inbound = "", outBound = "") {
        const outBoundQuery = outBound ? `?outBound=${outBound}` : ""
        const inBoundQuery = inbound ? `&inbound=${inbound}` : ""
        
        return await this.client.get(`/flight/list${outBoundQuery}${inBoundQuery}`)
    }

}

export default FlightService;