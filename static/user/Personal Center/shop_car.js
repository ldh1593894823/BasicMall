const {
    createApp
} = Vue

createApp({
    data() {
        return {
            
            shop_list_data: [
                // { name: "", price: '', num: '', category: '', sales: '', myimage: [] },
            ],
            create_order_data: { courier_name: "", courier_phone: "", courier_place: "" ,harvest_type:"",}
        }
    },
    methods: {
        find_shop_list() {
            all_shop_car({ find_type: 'all' }, res => {
                if (res.result == 'ok') {
                    console.log('商品列表', res)
                    this.shop_list_data = res.shop_list
                }
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
        remove_shop(e) {
            console.log(e.target._value);
            del_shop_car({ car_id: e.target._value }, res => {
                if (res.result == 'ok') {
                    this.Wrring().show("删除成功");
                    this.find_shop_list()
                }
            })
        },
        click_create_order() {
            console.log(this.create_order_data.courier_name);
            if ((this.create_order_data.courier_name) == "") {
                this.Wrring().show("请输入收货人姓名")
            }
            else if ((this.create_order_data.courier_phone) == "") {
                this.Wrring().show("请输入收货人电话")
            } else if ((this.create_order_data.courier_place) == "") {
                this.Wrring().show("请输入收货人地址")
            } else if ((this.create_order_data.harvest_type) == "") {
                this.Wrring().show("请选择收获方式")
            }
            else {
                create_order(this.create_order_data, res => {
                    if (res.result == 'ok') {
                        $('#myModal').modal('toggle', 'center')
                        this.Wrring().show("下单成功")
                        window.open(html_host + '/user/Personal%20Center/order_detail.html?shop_id=' + res.order_id)
                        console.log(res.order_id);
                    }
                })
            }
        },
        click_harvest_type(e){
            console.log(e.target.id);
            this.create_order_data.harvest_type = e.target.id
        }
    },
    mounted: function () {
        this.host = host
        this.find_shop_list()
    }
}).mount('#app')