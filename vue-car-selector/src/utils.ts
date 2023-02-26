export const DataTime = {
    convertToTime: (time_value: number | undefined) => {
        const hour = time_value ? parseInt(String(time_value / 60)) : 0
        const min = time_value ? parseInt(String(time_value % 60)) : 0
        if (hour === 0  && min ===0){
            return '-- h'
        }
        return `${hour}h${min}min`
    }
}

export const Formatter = {
    formatPrice: (value: number) => {
        let val = (value / 1).toFixed(0).replace('.', ',')
        return val.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ".")
    }
}