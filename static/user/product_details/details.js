const {
    createApp
} = Vue

createApp({
    data() {
        return {
            _host: "",
            shop_info: {},
            add_shop_number: 1
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
        num_add() {
            console.log(this.add_shop_number);
            this.add_shop_number++;
        },
        numred() {
            if (this.add_shop_number > 1) {
                this.add_shop_number--;
            }
        },
        click_add_cart() {
            add_shop_car({shop_id:this.shop_info.id,add_shop_num:this.add_shop_number},res=>{
                console.log(res);
                if(res.result == "ok"){
                    this.Wrring().show("购物车添加成功")
                }
            })
        }
    },
    mounted: function () {
        this._host = host
        let url = decodeURI(location.search); //获取url中"?"符后的字串 ?
        let userid;
        if (url.indexOf("?") != -1) {
            str = url.substr(1);
            strs = str.split("=");
            userid = strs[1];
        }
        console.log(userid)
        api_new_hot_shop({ find_type: 'one_shop', shop_id: userid }, res => {
            if (res.result == 'ok') {
                console.log(res.shop_list[0]);
                this.shop_info = res.shop_list[0]
                console.log();
            }
        })
    }
}).mount('#app')