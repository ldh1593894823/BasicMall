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
            api_find_shoping({find_type: 'all'}, res => {
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
            del_shop({id:e.target._value},res=>{
                if (res.result == 'ok') {
                    this.Wrring().show("发布成功");
                    this.find_shop_list()
                }
            })
        }
    },
    mounted: function() {
        console.log($.zui.store.get('user_info'))
        this.find_shop_list()
    }
}).mount('#app')