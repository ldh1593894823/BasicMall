const {
    createApp
} = Vue

createApp({
    data() {
        return {
            
            shop_list_data: [
                // { name: "", price: '', num: '', time: '', first_image: ""},
            ],
        }
    },
    methods: {
        Wrring() {
            return new $.zui.Messager({
                type: 'success',
                icon: '',
                placement: 'top',
                time: 2000
            });
        },
        find_shop_list(){
            find_order({order_status:1},res=>{
                console.log(res)
            })
        }

    },
    mounted: function () {
        this.host = host
        this.find_shop_list()
    }
}).mount('#app')