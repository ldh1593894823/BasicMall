const {
    createApp
} = Vue

createApp({
    data() {
        return {
            host:"",
            hot_shop_list: {},
            new_shop_list: {},
            swiper_data: [{
                image: "https://res.lancome.com.cn/resources/activityReleased/06751bcd-7769-4ef2-ad53-79f95ee8783b/images/pc_img_01-1.jpg?20221202160006"
            }, {
                image: "https://res.lancome.com.cn/resources/activityReleased/06751bcd-7769-4ef2-ad53-79f95ee8783b/images/pc_img_01-3.jpg?20221202160006"
            }, {
                image: "https://res.lancome.com.cn/resources/activityReleased/06751bcd-7769-4ef2-ad53-79f95ee8783b/images/pc_img_01-6.jpg?20221202160006"
            }, {
                image: "https://res.lancome.com.cn/resources/activityReleased/06751bcd-7769-4ef2-ad53-79f95ee8783b/images/pc_img_01-5.jpg?20221202160006"
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
        click_detail(e){
            console.log(html_host+'/user/product_details/details.html?shop_id='+e.path[2].id)
            window.open (html_host+'/user/product_details/details.html?shop_id='+e.path[2].id)
        },
        clicked_shopcar(e){
            console.log(e.target.id)
            add_shop_car({shop_id:e.target.id,add_shop_num:1},res=>{
                if (res.result == 'ok') {
                    this.Wrring().show("购物车添加成功")
                }
            })
        }
    },
    mounted: function() {
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
    }
}).mount('#app')