const {
    createApp
} = Vue

createApp({
    data() {
        return {
            active_css: false,

            icon_logo: {
                "icon-circle": true,
                "icon-circle-blank": false
            },


            selector_data: [
                { name: "主页", class_css: "icon-th", son_selector: [{ name: "主页", class_css: "icon-circle", is_selected: false }] },
                {
                    name: "商品管理",
                    class_css: "icon-time",
                    son_selector: [{ name: "所有商品", class_css: "icon-circle", is_selected: false }, { name: "添加商品", class_css: "icon-circle", is_selected: false }]
                },
                { name: "订单管理", class_css: "icon-book", son_selector: [{ name: "所有订单", class_css: "icon-circle", is_selected: false }, { name: "待付款", class_css: "icon-circle", is_selected: false }, { name: "待发货", class_css: "icon-circle", is_selected: false }, { name: "待收货", class_css: "icon-circle", is_selected: false }] },
                { name: "评价管理", class_css: "icon-comments", son_selector: [{ name: "评价管理", class_css: "icon-circle", is_selected: false }] },
                { name: "公告管理", class_css: "icon-comments", son_selector: [{ name: "公告管理", class_css: "icon-circle", is_selected: false }] },
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
        }
    },
    mounted: function() {
        console.log("初始化成功")
    }
}).mount('#app')