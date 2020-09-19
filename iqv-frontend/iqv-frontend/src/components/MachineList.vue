<template xmlns:v-slot="http://www.w3.org/1999/XSL/Transform">
    <v-card class="mx-12 my-12">
        <v-data-table
                :headers="headers"
                :items="machines"
                :items-per-page="5"
                class="elevation-1"
        >
            <template v-slot:item.monitor="{ item }">
                <div v-if="$store.state.dashboard.find(m => m.id === item.id)">
                <v-icon large color="primary" @click="deleteItem(item)" :disabled="snackbar" >
                    mdi-eye-check
                </v-icon>
                </div>
                <div v-if="!$store.state.dashboard.find(m => m.id === item.id)">
                    <v-icon large color="error" @click="addItem(item)" :disabled="snackbar">
                        mdi-eye-remove
                    </v-icon>
                </div>
            </template>
        </v-data-table>

        <v-snackbar
                v-model="snackbar"
                :timeout="snackbarTimeout"
                centered
                :color="snackbarColor"
        >
            <v-icon>{{snackbarIcon}}</v-icon>
            {{ snackbarText }}
        </v-snackbar>
    </v-card>
</template>

<script>
    import axios from 'axios';

    export default {
        name: 'MachineList',

        data: () => ({
            snackbar: false,
            snackbarIcon: '',
            snackbarText: '',
            snackbarColor: 'white',
            snackbarTimeout: 750,
            dialog: false,
            headers: [
                {text: 'Id', value: 'id'},
                {text: 'Name', value: 'name'},
                {text: 'Producer', value: 'producer'},
                {text: 'Model', value: 'model'},
                {text: 'Serial', value: 'serial'},
                {text: 'Monitor', value: 'monitor', sortable: false},
            ],
            machines: [],
        }),
        created() {
            axios.get('http://localhost:5000/machines/').then((res) => {
                this.machines = res.data;
            }).catch((err) => {
                console.log(err)
            })
        },
        methods: {
            async addItem(item) {
                if (!this.$store.state.dashboard.find(m => m.id === item.id)) {
                    const res = await this.$store.dispatch('addMachine', item);
                    console.log(res, "ADDED");
                    this.snackbarIcon = 'mdi-plus';
                    this.snackbarColor = 'green';
                    this.snackbarText = `${item.name} added to dashboard`;
                    this.snackbar = true;
                }
            },
            async deleteItem(item) {
                if (this.$store.state.dashboard.find(m => m.id === item.id)) {
                    const res = await this.$store.dispatch('deleteMachine', item);
                    console.log(res, "DELETED");
                    this.snackbarIcon = 'mdi-delete';
                    this.snackbarColor = 'red';
                    this.snackbarText = `${item.name} deleted from dashboard`;
                    this.snackbar = true;
                }
            }
        }
    }
</script>
