<template>
    <section id="flight-render-section">
        <v-card id="network-card">
            <Network
                ref="network"
                :nodes="nodes"
                :edges="edges"
                :options="options">
            </Network>

            <v-overlay 
                absolute
                :value="loadingPage">
                <div class="d-flex flex-column align-center">
                    <v-progress-circular v-if="loadingPage" indeterminate size="64" />
                </div>
            </v-overlay>
        </v-card>
    </section>
</template>

<script>
// import { Network } from "vue-vis-network";

export default {
    data() {
        return {
            loadingPage: false,
            message: undefined,
            options: {
            nodes: {
                borderWidth: 2
            },
            edges: {
                arrows: 'to'
            }
        },
        }
    }
}
</script>

<style lang="scss">
    
    .network-card {
        height: 100%;
        width: 100%;
        > div {
            height: 100%;
            width: 100%;
            canvas {
                max-height: calc(100vh - 110px) !important;
            }
        }
    }
    .vis-network {
        min-height: 650px !important;
    }
</style>