export const DataTime = {
    convertToTime: (time_value: number) => {
        const hour = time_value ? parseInt(String(time_value / 60)) : 0
        const min = time_value ? parseInt(String(time_value % 60)) : 0
        return `${hour}h${min}min`
    }
}

export const Formatter = {
    formatPrice: (value: number) => {
        let val = (value / 1).toFixed(0).replace('.', ',')
        return val.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ".")
    }
}