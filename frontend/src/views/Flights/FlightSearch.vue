<template>
    <section id="schedule-template">
        <div class="pa-3 left-side">
            <v-text-field
                clearable
                v-model="outBound"
                label="Local de origem" />
            
            <v-text-field
                clearable
                v-model="inBound"
                label="Local de destino" />

            <v-btn
                class="mx-2"
                dark
                color="purple"
                @click="getFlights()">
                <h3>Procurar</h3>
                <v-icon>mdi-airplane-takeoff</v-icon>
            </v-btn>
        </div>
    </section>
</template>

<script>
export default {
    data() {
        return {
            outBound: "",
            inBound: ""
        }
    },
    methods: {
        getFlights() {
            this.$emit('selectedFlights', {
                outBound: this.outBound,
                inbound: this.inbound
            })
        }
    },
    computed: {
    },
}
</script>

<style>
    .left-side {
        width: 20%;
        min-width: 250px;
    }
</style>