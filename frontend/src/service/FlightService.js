import Connection from './Connection';

class FlightService extends Connection {
    constructor() {
        super();
    }

    async getFlightById(id) {
        return await this.client.get(`/flight/${id}`);
    }

    async getFlights() {
        return await this.client.get("/flight/list/")
    }

    async getFlightsByOriginId(originId) {
        return await this.client.get(`/flight/info/${originId}`);
    }
}

export default FlightService;