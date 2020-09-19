<template>
    <v-app id="app">
        <v-app-bar dense fixed>
            <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
        </v-app-bar>

        <v-navigation-drawer
                v-model="drawer"
                :color="color"
                dense
                fixed
                temporary
        >
            <v-list
                    dense
                    nav
                    class="py-0"
            >
                <v-list-item two-line>
                    <v-list-item-avatar>
                        <img src="https://randomuser.me/api/portraits/men/81.jpg">
                    </v-list-item-avatar>

                    <v-list-item-content>
                        <v-list-item-title>IQV Frontend</v-list-item-title>
                        <v-list-item-subtitle>Menu</v-list-item-subtitle>
                    </v-list-item-content>
                </v-list-item>

                <v-divider></v-divider>

                <v-list-item
                        v-for="item in items"
                        :key="item.title"
                        link
                        :to="item.route"
                >
                    <v-list-item-icon>
                        <v-icon>{{ item.icon }}</v-icon>
                    </v-list-item-icon>

                    <v-list-item-content>
                        <v-list-item-title>{{ item.title }}</v-list-item-title>
                    </v-list-item-content>
                </v-list-item>
            </v-list>
        </v-navigation-drawer>

        <v-main class="my-12">
            <router-view/>
        </v-main>
    </v-app>
</template>

<style lang="scss">
    #app {
        font-family: Avenir, Helvetica, Arial, sans-serif;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        text-align: center;
        color: #2c3e50;
    }

    #nav {
        padding: 30px;

        a {
            font-weight: bold;
            color: #2c3e50;

            &.router-link-exact-active {
                color: #42b983;
            }
        }
    }
</style>

<script>
    export default {
        data() {
            return {
                drawer: null,
                items: [
                    {title: 'Home', icon: 'mdi-home', route: '/'},
                    {title: 'Dashboard', icon: 'mdi-view-dashboard', route: '/dashboard'},
                ],
                color: 'white',
            }
        },
    }
</script>