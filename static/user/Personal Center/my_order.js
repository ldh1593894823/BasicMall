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
        Wrring() {
            return new $.zui.Messager({
                type: 'success',
                icon: '',
                placement: 'top',
                time: 2000
            });
        },
        click_add_evaluation(e) {
            add_evaluation({ order_id: e.id, detail: this.shop_list_data[e.index].evaluation }, res => {
                if (res.result == "ok") {
                    this.Wrring().show("发布成功")
                } else {
                    this.Wrring().show("评论一旦发布禁止修改")
                }
            })
        },
        // 查询不同类型订单
        find_shop_list(type) {
            this.select_state = type
            find_order({ order_status: type }, res => {
                this.shop_list_data = res.order_list
                console.log(res)
            })
        },
        // 移除未付款订单
        remove_shop(e) {
            del_myorder({ order_id: e }, res => {
                this.Wrring().show(res.msg)
                this.find_shop_list()
            })
        },
        // 对订单进行收货
        set_order(e) {
            harvest_myorder({ order_id: e }, res => {
                this.Wrring().show(res.msg)
                this.find_shop_list(3)
            })
        },
        // 对订单进行付款
        pay_shop(e) {
            window.open(html_host + '/user/Personal%20Center/order_list.html?shop_id=' + e)
        },
        //退换货申请
        click_refunds_exchanges(e) {
            console.log(e);
            refunds_exchanges(e, res => {
                if (res.result == 'ok') {
                    this.Wrring().show("提交审核中")
                    this.find_shop_list(0)
                }
            })
        },
        //取消退货
        click_cancel_refunds(e) {
            cancel_refunds({order_id:e},res=>{
                if(res.result == 'ok'){
                    this.find_shop_list(4)
                    this.Wrring().show("取消退货成功")
                }
            })
        },
        //取消换货
        click_cancel_exchanges(e) {
            cancel_exchanges({order_id:e},res=>{
                if(res.result == 'ok'){
                    this.find_shop_list(6)
                    this.Wrring().show("取消换货成功")
                }
            })
        }
    },
    mounted: function () {
        this.host = host
        this.find_shop_list(1)
    }
}).mount('#app')