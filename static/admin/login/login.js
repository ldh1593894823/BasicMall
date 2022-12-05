const {
    createApp
} = Vue

createApp({
    data() {
        return {
            user_info: {
                type: "",
                login_name: "",
                cookies: ""
            },
            will_send_data: {
                "username": "admin",
                "password": "123456"
            }
        }
    },
    methods: {

        Wrring() {
            return new $.zui.Messager({
                type: 'warning',
                icon: 'exclamation-sign',
                placement: 'top',
                time: 2000
            });
        },

        Scuuess() {
            return new $.zui.Messager({
                type: 'success',
                icon: 'check-circle-o',
                placement: 'top',
                time: 2000
            });
        },


        login() {
            api_login_admin(this.will_send_data, res => {
                if (res.result == "ok") {
                    this.Scuuess().show(res.msg)
                    $.zui.store.remove('user_info'); //清空参数再存储
                    $.zui.store.set('user_info', res); // 将一个对象存储到本地存储
                    window.location.href = "../admin/admin.html";
                } else {
                    this.Wrring().show(res.msg);
                }
            })
        }

    },
    mounted: function() {}
}).mount('#app')