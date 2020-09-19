import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
    state: {
        dashboard: []
    },
    mutations: {
        addMachine(state, machine) {
            state.dashboard.push(machine)
        },
        deleteMachine(state, machine) {
            state.dashboard = state.dashboard.filter(x => x.id !== machine.id)
        }
    },
    actions: {
        addMachine(context, machine) {
            if (!context.state.dashboard.find(m => m.id === machine.id)) {
                context.commit('addMachine', machine)
                return true;
            } else
                return false;

        },
        deleteMachine(context, machine) {
            if (context.state.dashboard.find(m => m.id === machine.id)) {
                context.commit('deleteMachine', machine)
                return true;
            } else
                return false;
        }
    },
    getters: {}
})