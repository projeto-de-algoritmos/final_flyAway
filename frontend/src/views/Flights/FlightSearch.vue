<template>
    <section id="schedule-template">
        <div class="pa-6">
            <h5>De:</h5>
            <v-card class="mb-6">
                <select
                    id="from-card"
                    v-model="outBound">
                    <option
                        v-for="item, index in items"
                        :key="index"
                        :value="item.code">
                        {{ item.name }}
                    </option>
                </select>
            </v-card>
            <h5>Para:</h5>
            <v-card class="mb-6">
                <select
                    id="to-card"
                    v-model="inBound">
                    <option
                        v-for="item, index in items"
                        :key="index"
                        :value="item.code">
                        {{ item.name }}
                    </option>
                </select>
            </v-card>
            <v-btn
                class="mx-2"
                dark
                color="purple"
                @click="getFlights()">
                <h3>Procurar</h3>
                <v-icon>mdi-airplane-takeoff</v-icon>
            </v-btn>
            <v-overlay 
                absolute
                :value="loading">
                <div class="d-flex flex-column align-center">
                    <v-progress-circular v-if="loading" indeterminate size="64" />
                </div>
            </v-overlay>
        </div>
    </section>
</template>

<script>
import FlightService from "../../service/FlightService";

const flightService = new FlightService();
export default {
    data() {
        return {
            items: [],
            outBound: "",
            inBound: "",
            loading: false,
            messageError: undefined
        }
    },
    methods: {
        async getCountry() {
            this.loading = true;
            try {
                const result = await flightService.getCountry();
                this.items = result.data;
            }
            catch (error) {
                this.items = []
                this.messageError = error;
                throw error;
            }
            this.loading = false;
        },
        getFlights() {
            this.$emit('selectedFlights', {
                outBound: this.outBound,
                inBound: this.inBound
            })
        }
    },
    async created() {
        await this.getCountry();
    }
}
</script>

<style>
    .left-side {
        width: 20%;
        min-width: 250px;
    }
</style>