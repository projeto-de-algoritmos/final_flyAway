<template>
    <section id="home-section">
        <div class="d-flex graph-container pa-4">
            <flight-search
                @selectedFlights="updateData"/>
            <flight-render ref="render" />
        </div>
    </section>
</template>

<script>
import FlightSearch from "./Flights/FlightSearch";
import FlightRender from "./Flights/FlightRender";

export default {
    components: {
        'flight-search' : FlightSearch,
        'flight-render' : FlightRender
    },
    methods: {
        async updateData({outBound, inBound}) {
            await this.$refs.render.getFlights({outBound, inBound})
        }
    },

    data() {
        return {}
    },
}
</script>

<style lang="scss">
body {
    overflow: hidden;
}
#home-section {
    height: 100%;
    display: flex;

    .graph-container {
        overflow: hidden;
        flex-grow: 1;
    }
}
</style>