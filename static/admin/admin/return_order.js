const {
    createApp
} = Vue

createApp({
    data() {
        return {
            select_state: "1",
            shop_list_data: [
                // { name: "", price: '', num: '', time: '', first_image: ""},
            ],
        }
    },

    methods: {
        click_modify_order(e) {
            modify_order(e, res => {
                if (res.resluat == 'ok') {
                    this.Wrring().show("审核成功")
                    this.find_order_list(e.type - 1)
                }
            })
            console.log(e);
        },
        find_order_list(type) {
            all_orders({ order_status: type }, res => {
                console.log(res);
                this.shop_list_data = res.order_list
            })
        },
        Wrring() {
            return new $.zui.Messager({
                type: 'success',
                icon: '',
                placement: 'top',
                time: 2000
            });
        },

    },
    mounted: function () {
        this.host = host
        this.find_order_list(10)
    }
}).mount('#app')