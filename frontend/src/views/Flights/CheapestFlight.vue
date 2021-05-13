<template>
    <section
        id="cheapest-flight">
        <v-card>
            <v-card-title>
                Passagem mais barata:
            </v-card-title>
            <v-card-text
            v-model="cheapest">
                R$ {{ cheapest.label }}
            </v-card-text>
        </v-card>
    </section>
</template>

<script>
export default {
    props: {
        cheapest: {
            default: undefined,
        },
    },
    data() {
        return {}
    },
}
</script>

<style lang="scss">
#cheapest-flight {
    width: 25%;
    flex-grow: 1;
    position: relative;
    margin-bottom: 5px;
}
</style>