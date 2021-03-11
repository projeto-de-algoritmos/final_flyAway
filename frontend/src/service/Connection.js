import axios from 'axios';

class Connection {
    constructor() {
        this.client = axios.create({
            baseURL: process.env.VUE_APP_API_URL
        })
    }
}

export default Connection;