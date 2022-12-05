const {
    createApp
} = Vue

createApp({
    data() {
        return {
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
    methods: {},
    mounted: function() {
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