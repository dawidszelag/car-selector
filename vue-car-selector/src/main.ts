import {createApp} from 'vue'
import './style.css'
import App from './App.vue'
import router from "./router";
import { createPinia } from 'pinia'
import {OpenAPI} from "./api";

OpenAPI.BASE = import.meta.env.VITE_BACKEND_URL || "http://144.91.87.153:9000";
const pinia = createPinia()
const app = createApp(App);
app.use(router);
app.use(pinia)
app.mount('#app')
