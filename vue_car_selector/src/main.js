import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import { library } from '@fortawesome/fontawesome-svg-core'
import { faSquare, faCheckSquare, faCircle,faCheckCircle } from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import store from "./store";
import axios from 'axios'
import VueAxios from 'vue-axios'

const app = createApp(App);
app.component('font-awesome-icon', FontAwesomeIcon)
library.add(faSquare, faCheckSquare, faCircle,faCheckCircle)
axios.defaults.baseURL = process.env.VUE_APP_BACKEND_URL  + '/api/v1/';
store.state.base_media_url = process.env.VUE_APP_BACKEND_URL  +'/media/';
app.use(router);
app.use(store);
app.use(VueAxios, axios)
app.mount("#app");
