const {
    createApp
} = Vue

createApp({
    data() {
        return {
            announcement_list:"",
            now_id: 1,
            host: "",
            hot_shop_list: {},
            new_shop_list: {},
            son_shop_list: {},
            swiper_data: [{
                image: "/img/index1.jpg"
            }, {
                image: "/img/index2.jpg"
            }, {
                image: "/img/index3.jpg"
            }, {
                image: "/img/index4.jpg"
            }],
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
        click_tab(e) {
            this.now_id = e
            if (e == 2) { //查询彩妆
                api_new_hot_shop({ find_type: 'color' }, res => {
                    if (res.result == 'ok') {
                        console.log(res)
                        this.son_shop_list = res.shop_list
                    }
                })
            } else if (e == 3) { //查询底妆
                api_new_hot_shop({ find_type: 'b_makeup' }, res => {
                    if (res.result == 'ok') {
                        console.log(res)
                        this.son_shop_list = res.shop_list
                    }
                })
            } else if (e == 4) { //查询底妆
                api_new_hot_shop({ find_type: 'perfume' }, res => {
                    if (res.result == 'ok') {
                        console.log(res)
                        this.son_shop_list = res.shop_list
                    }
                })
            }

        },
        click_detail(e) {
            console.log(e);
            console.log(html_host + '/user/product_details/details.html?shop_id=' + e)
            window.open(html_host + '/user/product_details/details.html?shop_id=' + e)
        },
        clicked_shopcar(e) {
            console.log(e.target.id)
            add_shop_car({ shop_id: e.target.id, add_shop_num: 1 }, res => {
                if (res.result == 'ok') {
                    this.Wrring().show("购物车添加成功")
                }
            })
        }
    },
    mounted: function () {
        this.host = host
        api_new_hot_shop({ find_type: 'hot_shop' }, res => {
            if (res.result == 'ok') {
                console.log(res)
                this.hot_shop_list = res.shop_list
            }
        })
        api_new_hot_shop({ find_type: 'new_shop' }, res => {
            if (res.result == 'ok') {
                console.log(res)
                this.new_shop_list = res.shop_list
            }
        })
        get_a_announcement({},res=>{
            this.announcement_list = res.content
        })
    }
}).mount('#app')