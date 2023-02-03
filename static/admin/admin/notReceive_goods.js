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
        Wrring() {
            return new $.zui.Messager({
                type: 'success',
                icon: 'check',
                placement: 'top',
                time: 2000
            });
        },
        find_order_list() {
            all_orders({order_status:3}, res => {
                if (res.result == 'ok') {
                    this.shop_order_data = res.order_list
                    console.log('商品列表', res)
                }
            })
        },
        del_order(e){
            admin_del_order({"order_id":e},res=>{
                if(res.result == "ok"){
                    this.Wrring().show("删除成功")
                    this.find_order_list()
                }
            })
        }
    },
    mounted: function () {
        this.host = host
        this.find_order_list()
    }
}).mount('#app')