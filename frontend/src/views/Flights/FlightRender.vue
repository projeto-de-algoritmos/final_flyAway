<template>
    <section id="flight-render-section">
        <v-card id="network-card">
            <network
                ref="network"
                :nodes="nodes"
                :edges="edges"
                :options="options">
            </network>

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
import { Network } from "vue-vis-network";
import FlightService from "../../service/FlightService";
import { mapActions, mapState } from "vuex"

const flightService = new FlightService();

export default {
    components: {
        'network': Network
    },
    data() {
        return {
            loadingPage: false,
            options: {
                nodes: {
                    borderWidth: 2
                },
                edges: {
                    length: 400                    
                },
                physics: {
                    enabled: true,
                    solver: "repulsion",
                    repulsion: {
                        nodeDistance: 400
                    }
                }
            },
            messageError: undefined
        }
    },

    computed: {
        ...mapState(['nodes', 'edges'])
    },

    methods: {
        ...mapActions(['setNodes', 'setEdges']),
        
        async getFlights({outBound, inBound}) {
            this.loadingPage = true
            try {
                const response = await flightService.getFlights(outBound, inBound);
                this.setNodes(response.data.nodes);
                this.setEdges(response.data.edges);
                this.loadingPage = false;
            }
            catch (error) {
                this.messageError = error.message
                throw error;
            }
            this.loadingPage = false;
        }
    },
}
</script>

<style lang="scss">
#flight-render-section {
    width: 100%;
    flex-grow: 1;
    position: relative;
    #network-card {
        height: 100%;
        width: 100%;
        > div {
            height: 100%;
            width: 100%;
            canvas {
                max-height: calc(100vh - 110px) !important;
            }
        }
        .vis-network {
            min-height: 650px !important;
        }
    }
}
</style>