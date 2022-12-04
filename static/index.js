const {
    createApp
} = Vue

createApp({
    data() {
        return {
            will_send_data: {
                find_type: 'hot_shop'
            },
            hot_shop_list: {},
            swiper_data: [{
                image: "https://www.luncode.com/usr/uploads/2022/10/3621845037.jpg "
            }, {
                image: "https://www.luncode.com/usr/uploads/2022/10/3621845037.jpg "
            }, {
                image: "https://www.luncode.com/usr/uploads/2022/10/3621845037.jpg "
            }, {
                image: "https://www.luncode.com/usr/uploads/2022/10/3621845037.jpg "
            }],
        }
    },
    methods: {},
    mounted: function() {
        api_new_hot_shop(this.will_send_data, res => {
            if (res.result == 'ok') {
                console.log(res)
                this.hot_shop_list = res.shop_list
            }
        })
    }
}).mount('#app')