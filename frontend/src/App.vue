<template>
    <v-app>
        <v-app-bar
        app
        dense
        color="purple"
        dark>
        <div class="d-flex align-center">
            <v-icon class="mr-2">mdi-briefcase-search-outline</v-icon>
            <h2>Fly Away</h2>
        </div>
        <v-spacer></v-spacer>
        </v-app-bar>

        <v-main>
            <Schedule/>
        </v-main>
    </v-app>
</template>

<script>
import Schedule from './views/Schedule';
export default {
    name: 'App',
    components: {
        Schedule,
    },
};
</script>

<style lang="scss">
    .v-application {
        font-family: 'JetBrains Mono', monospace;
    }
</style>