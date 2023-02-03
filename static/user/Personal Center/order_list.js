const {
    createApp
} = Vue

createApp({
    data() {
        return {
            order_id:'',
            order_list: [],
            timer:{},
            diplay_Messager:{}
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
        error() {
            return new $.zui.Messager({
                type: 'danger',
                icon: '',
                placement: 'top',
                time: 2000
            });
        },
        click_buy_now() {
            this.timer = setTimeout(() => {
                pay_myorder({order_id:this.order_id},res=>{
                    if(res.result=="ok"){
                        this.Wrring().show("支付成功")
                        this.diplay_Messager.modal('hide')
                        setTimeout(() => {
                            window.location.href="/index.html"
                        }, 1000);
                    }
                })
            }, 3000)
        },
        cancel_buy(){
            this.error().show("支付失败")
            clearTimeout(this.timer)
        }
    },
    mounted: function () {
        this.diplay_Messager = $('#myModal').modal({
            keyboard : false,
            show     : false,
            backdrop : false,
        })
        let url = decodeURI(location.search); //获取url中"?"符后的字串 ?
        let order_id;
        if (url.indexOf("?") != -1) {
            str = url.substr(1);
            strs = str.split("=");
            order_id = strs[1];
        }
        console.log(order_id)
        this.order_id = order_id
        order_list({ order_id: order_id }, res => {
            this.order_list = res.order_list
        })
        this.host = host
    }
}).mount('#app')