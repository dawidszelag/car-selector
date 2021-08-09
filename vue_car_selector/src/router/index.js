import {createRouter, createWebHistory} from "vue-router";
import Home from "@/views/Home.vue";
import Models from "@/views/Models";
import SubModels from "@/views/SubModels";
import Car from "@/views/Car";

const routeInfos = [
    {
        path: "/",
        component: Home,
        name: 'home'
    },
    {
        path: "/models",
        name: 'models',
        component: Models,
    },
    {
        path: "/sub-models/:modelId",
        name: 'sub-models',
        component: SubModels,
    },
    {
        path: "/car/:carId",
        name: 'car',
        component: Car,
    },
];

const router = createRouter({
    history: createWebHistory(),
    routes: routeInfos,
});

export default router;
