const {
    createApp
} = Vue

createApp({
    data() {
        return {
            shop_list_data: [
                { name: "123" },
                { name: "456" },
                { name: "789" },
                { name: "102" },
                { name: "789" },
            ],
        }
    },
    methods: {},
    mounted: function() {
        console.log("初始化成功")
    }
}).mount('#app')