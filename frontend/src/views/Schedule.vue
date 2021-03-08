<template>
    <section id="home-section">
        <div class="d-flex pa-4">
            <flight-search />
            <flight-render />
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

    data() {
        return {
            
        }
    },
    computed: {

    },
}
</script>

<style>

</style>