<template>
    <v-card width="100%" class="my-12">
        {{item.name}}
        <v-btn icon color="#FE5B4D" @click="deleteMachine(item)">
            <v-icon>mdi-delete</v-icon>
        </v-btn>

        <line-chart :key="item.name + xCount" :chartdata="chartData" :options="options"/>
    </v-card>
</template>

<script>
    import LineChart from '@/components/LineChart.vue'

    const endpoint = 'ws://localhost:5000';
    const route = '/consumption/';
    //let ws;

    export default {
        name: 'MachineBoard',
        components: {
            LineChart
        },
        props: {
            item: {
                type: Object,
                required: true
            }
        },
        data: () => ({
            ws: null,
            enabled: true,
            xCount: 0,
            chartData: {
                labels: [],
                datasets: [
                    {
                        label: 'Usage',
                        backgroundColor: '#6DBFA2',
                        data: [],
                    }
                ]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                animation: {
                    duration: 0
                }
            }
        }),
        created() {
            this.connect();
        },
        destroyed() {
            this.disconnect();
        },
        methods: {
            connect() {
                this.ws = new WebSocket(endpoint + route);
                const jsonReq = JSON.stringify({"machine_id": this.item.id});

                this.ws.onopen = e => {
                    this.ws.send(jsonReq);
                    console.log(e);
                    this.ws.onmessage = e => {
                        if (e && e.data) {
                            const data = JSON.parse(e.data);
                            if (data.usage || data.usage === 0) {
                                this.updateChartData(data.usage)
                            }
                        }
                    }
                }
            },
            disconnect() {
                if (1 === this.ws.readyState) {
                    this.ws.close();
                    this.ws = null; // prevent memory leak
                }
            },
            updateChartData(usageData) {
                const formattedData = {
                    x: this.xCount++,
                    y: usageData
                };

                const chartData = {
                    labels: [...this.chartData.labels, formattedData.x],
                    datasets: [
                        {
                            label: 'Usage',
                            backgroundColor: '#6DBFA2',
                            data: [...this.chartData.datasets[0].data, formattedData]
                        }
                    ]
                };
                this.chartData = chartData;
            },
            async deleteMachine(machine) {
                    const res = await this.$store.dispatch('deleteMachine', machine);
                    console.log(res,"DELETED");
            }
        }
    }
</script>
