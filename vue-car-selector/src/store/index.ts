import {defineStore} from 'pinia';

export const useAppStore = defineStore('appStore', {
    state: () => {
        return {
            form: {},
            showResults: false,
            showFeedBack: true,
        }
    },

    actions: {
        setForm(form: {}) {
            this.form = {...form}
        },
        resetFeedback(){
            this.showFeedBack = false;
        },
        setFeedback(){
            this.showFeedBack = true;
        }
    },
})