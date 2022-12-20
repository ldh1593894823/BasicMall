const {
    createApp
} = Vue

createApp({
    data() {
        return {
            shop_list_data: [
                // { name: "", price: '', num: '', category: '', sales: '', myimage: [] },
            ],
        }
    },
    methods: {
        find_shop_list() {
            all_shop_car({find_type: 'all'}, res => {
                if (res.result == 'ok') {
                    console.log('商品列表', res)
                    this.shop_list_data = res.shop_list
                }
            })
        },
        Wrring() {
            return new $.zui.Messager({
                type: 'success',
                icon: 'check',
                placement: 'top',
                time: 2000
            });
        },
        remove_shop(e){
            console.log(e.target._value);
            del_shop_car({car_id:e.target._value},res=>{
                if (res.result == 'ok') {
                    this.Wrring().show("删除成功");
                    this.find_shop_list()
                }
            })
        }
    },
    mounted: function() {
        this.host = host
        this.find_shop_list()
    }
}).mount('#app')