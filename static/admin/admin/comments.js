const {
    createApp
} = Vue

createApp({
    data() {
        return {
            todos:[
                {text:'公告&留言板',list:[{name:'温馨提示，您已进入监控区域'}]},
                {text:'公告&留言板',list:[{name:'温馨提示，您已进入监控区域'}]},
                {text:'公告&留言板',list:[{name:'温馨提示，您已进入监控区域'}]},
                {text:'公告&留言板',list:[{name:'温馨提示，您已进入监控区域'}]},
                {text:'公告&留言板',list:[{name:'温馨提示，您已进入监控区域'}]},
                {text:'公告&留言板',list:[{name:'温馨提示，您已进入监控区域'}]},
                {text:'公告&留言板',list:[{name:'温馨提示，您已进入监控区域'}]},
                {text:'公告&留言板',list:[{name:'温馨提示，您已进入监控区域'}]},
            ]
        }
    },
    methods: {},
    mounted: function() {
        console.log("初始化成功")
    }
}).mount('#app')