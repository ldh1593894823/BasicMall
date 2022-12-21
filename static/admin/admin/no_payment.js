const {
    createApp
} = Vue

createApp({
    data() {
        return {
            shop_order_data: [
                // { user_id: "123" ,price:"",image:""},
            ],
        }
    },
    methods: {
        find_order_list() {
            all_orders({}, res => {
                if (res.result == 'ok') {
                    this.shop_order_data = res.order_list
                    console.log('商品列表', res)
                }
            })
        },
    },
    mounted: function () {
        this.host = host
        this.find_order_list()
        console.log("初始化成功")
    }
}).mount('#app')