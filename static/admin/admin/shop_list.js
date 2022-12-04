const {
    createApp
} = Vue

createApp({
    data() {
        return {
            will_send_data: {
                find_type: 'all'
            },
            shop_list_data: [
                // { name: "", price: '', num: '', category: '', sales: '', myimage: [] },
            ],
        }
    },
    methods: {

    },
    mounted: function() {
        api_find_shoping(this.will_send_data, res => {
            if (res.result == 'ok') {
                console.log(res)
                this.shop_list_data = res.shop_list
            }
        })
    }
}).mount('#app')