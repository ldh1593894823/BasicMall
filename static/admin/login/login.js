const {
    createApp
} = Vue

createApp({
    data() {
        return {
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
                    $.zui.store.pageSet('date', res.cookies); // 将一个对象存储到本地存储
                    console.log($.zui.store.pageGet('date')); // 从本地存储获取'name'的值
                    window.location.href = "../admin/admin.html";
                } else {
                    this.Wrring().show(res.msg);
                }
            })
        }

    },
    mounted: function() {}
}).mount('#app')