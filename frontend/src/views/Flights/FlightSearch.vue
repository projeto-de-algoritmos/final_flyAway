<template>
    <section id="schedule-template">
        <div class="pa-3 left-side">
            <v-text-field
                clearable
                v-model="local.origin"
                label="Local de origem" />
            <v-text-field
                clearable
                v-model="local.destination"
                label="Local de destino" />
        </div>
    </section>
</template>

<script>
export default {
    data() {
        return {
            local: {
                origin: undefined,
                destination: undefined
            },
        }
    },
    methods: {

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