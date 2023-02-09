const {
    createApp
} = Vue

createApp({
    data() {
        return {
            user_info: {},
            // { username: "", user_qq: '', user_gender: '', contact_number: '', delivery_address: ""},
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
        modify_info(){
            modify_userinfo({user_info:this.user_info},res=>{
                if(res.result == "ok"){
                    this.Wrring().show("修改成功")
                    this.get_info()
                }
            })
        },
        get_info() {
            get_userinfo({},res=>{
                this.user_info = res.user_info
            })
        },
    },
    mounted: function () {
        this.get_info()
    }
}).mount('#app')