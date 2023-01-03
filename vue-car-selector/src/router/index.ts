import { createRouter, createWebHistory } from "vue-router";
import HomeView from "@/views/HomeView.vue";
import CarView from "@/views/CarView/index.vue";

const routes = [
    {
        path: "/",
        name: "home",
        component: HomeView,
    },
    {
        path: "/car/:carId",
        name: "carDetailsView",
        component: CarView,
    },
];


const index = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes,
});
export default index;