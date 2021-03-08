import axios from 'axios';

class Connection {
    constructor() {
        this.client = axios.create({
            baseURL: process.env.API_URL
        })
    }
}

export default Connection;