const {
    createApp
} = Vue

createApp({
    data() {
        return {
            admin_page: "shop_list.html",
            active_css: false,

            icon_logo: {
                "icon-circle": true,
                "icon-circle-blank": false
            },


            selector_data: [{
                    name: "商品管理",
                    class_css: "icon-time",
                    son_selector: [
                        { name: "所有商品", class_css: "icon-circle", is_selected: false, src: "shop_list.html" },
                        { name: "添加商品", class_css: "icon-circle", is_selected: false, src: "editor_shop.html" }
                    ]
                },
                {
                    name: "订单管理",
                    class_css: "icon-book",
                    son_selector: [
                        { name: "待付款", class_css: "icon-circle", is_selected: false ,src: "no_payment.html" },
                        { name: "待发货", class_css: "icon-circle", is_selected: false },
                        { name: "待收货", class_css: "icon-circle", is_selected: false }
                    ]
                },
                { name: "评价管理", class_css: "icon-comments", son_selector: [{ name: "评价管理", class_css: "icon-circle", is_selected: false }] },
                { name: "公告管理", class_css: "icon-comments", son_selector: [{ name: "公告管理", class_css: "icon-circle", is_selected: false ,src:"announcement.html"}] },
            ]
        }
    },
    methods: {

        clected(index, sondex) {
            for (let i = 0; i < this.selector_data.length; i++) {
                for (let j = 0; j < this.selector_data[i].son_selector.length; j++) {
                    this.selector_data[i].son_selector[j].is_selected = false
                }
            }
            this.selector_data[index].son_selector[sondex].is_selected = !this.selector_data[index].son_selector[sondex].is_selected
            this.admin_page = this.selector_data[index].son_selector[sondex].src
        }
    },
    mounted: function() {
        console.log("初始化成功")
    }
}).mount('#app')