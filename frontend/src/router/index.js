import Vue from 'vue';
import VueRouter from 'vue-router';
import Schedule from '@/views/Schedule.vue';

Vue.use(VueRouter)

const routes = [
    {
        path: '/',
        name: 'Schedule',
        component: Schedule
    }
]

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
})

export default router