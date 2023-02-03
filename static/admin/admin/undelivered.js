const { createApp } = Vue;

createApp({
    data() {
        return {
            express_id: "",
            shop_order_data: [
                // { user_id: "123" ,price:"",image:""},
            ],
        };
    },
    methods: {
        Wrring() {
            return new $.zui.Messager({
                type: "success",
                icon: "check",
                placement: "top",
                time: 2000,
            });
        },
        find_order_list() {
            all_orders({ order_status: 2 }, (res) => {
                if (res.result == "ok") {
                    this.shop_order_data = res.order_list;
                    console.log("商品列表", res);
                }
            });
        },
        click_deliver(e) {
            console.log(e);
            console.log(this.shop_order_data[e.index].express_id);
            if (this.shop_order_data[e.index].express_id == "") {
                this.Wrring().show("订单号不能为空");
            } else {
                deliver_goods(
                    {
                        order_id: e.id,
                        express_id: this.shop_order_data[e.index].express_id,
                    },
                    (res) => {
                        if (res.result == "ok") {
                            this.Wrring().show("发货成功");
                            this.find_order_list();
                        }
                    }
                );
            }
        },
    },
    mounted: function () {
        this.host = host;
        this.find_order_list();
    },
}).mount("#app");
