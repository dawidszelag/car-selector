import {defineStore} from 'pinia';

export const useAppStore = defineStore('appStore', {
    state: () => {
        return {form: {},showResults: false }
    },

    actions: {
        setForm(form) {
            this.form = {...form}
        },
    },
})