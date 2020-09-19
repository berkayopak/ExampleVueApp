<template>
    <div>
        <v-alert class="my-16 mx-12" type="info" v-if="items.length<=0">
            There is no machines on dashboard. Please add machine to dashboard and check later!
        </v-alert>

        <v-list-item-group v-model="item" color="primary">

            <v-list-item
                    v-for="item in items"
                    :key="item.id"
            >
                <MachineBoard :item="item"/>
            </v-list-item>
        </v-list-item-group>
    </div>
</template>

<script>
    // @ is an alias to /src
    import MachineBoard from '@/components/MachineBoard.vue'

    export default {
        name: 'About',
        data: () => ({
            item: 1,
            items: []
        }),
        components: {
            MachineBoard
        },
        mounted() {
            this.items = this.$store.state.dashboard;
        },
        updated() {
            this.items = this.$store.state.dashboard;
        }
    }
</script>
