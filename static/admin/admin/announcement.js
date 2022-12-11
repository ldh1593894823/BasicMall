const {
    createApp
} = Vue

createApp({
    data() {
        return {
            will_send_data: {
                title: "1",
                content: "",
            },
            todos: [
            ]
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
        // 发布公告
        click_submit() {
            console.log("发布公告")
            if (this.will_send_data.content == "") {
                this.Wrring().show("请输入公告内容");
            }
            else {
                add_announcement(this.will_send_data, res => {
                    if (res.result == 'ok') {
                        this.Wrring().show("发布成功");
                        this.will_send_data.content = ""
                        this.get_announcement()
                    }
                })
            }
        },
        // 获取所有公告
        get_announcement(){
            all_announcement(null,res=>{
                this.todos = res.comment_list
                console.log(res)
            })
        },
        remove_announcement(e){
            console.log(e.srcElement._value)
            del_announcement({id:e.srcElement._value},res=>{
                console.log(res)
                if (res.result == 'ok') {
                    this.Wrring().show("删除成功");
                    this.get_announcement()
                }
            })
        }
    },
    mounted: function () {
        this.get_announcement()
        console.log("初始化成功")
    }
}).mount('#app')