const {
    createApp
} = Vue



createApp({
    data() {
        return {
            zui_uploader: {},
            willsend_data: {
                shop_name: "",
                shop_price: "",
                shop_category: "",
                shop_num: "",
                imageList: [],
            },
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
        submit_info() {
            let will_data = this.willsend_data
            if (will_data.shop_name == "") {
                this.Wrring().show("请输入商品名称")
            } else if (will_data.shop_price == "") {
                this.Wrring().show("请输入商品价格")
            } else if (will_data.shop_category == "") {
                this.Wrring().show("请选择商品分类")
            } else if (will_data.shop_num == "") {
                this.Wrring().show("请输入商品库存")
            } else if (will_data.imageList == "") {
                this.Wrring().show("请上传图片")
            } else {
                api_add_shop(this.willsend_data, res => {
                    console.log(res)
                    window.location.href = "shop_list.html";
                })
            }
        }
    },

    mounted: function() {
        let _this = this
        let uploader_options = {
            // 初始化选项
            chunk_size: 0, //关闭分片上传
            autoUpload: false, //自动上传关闭
            limitFilesCount: 5, //限制上传数量
            url: 'http://127.0.0.1:8080/upload/',
            renameByClick: true, //重命名图片名称
            unique_names: true, //开启随机名称

            responseHandler: (res) => {
                let response_img = (JSON.parse(res.response))
                if (response_img.result == 'ok') {
                    this.willsend_data.imageList.push(response_img.image_name)
                }
            }
        };
        var my_uploader = $('#myUploader').uploader(uploader_options);
        this.zui_uploader = my_uploader

        let picker_options = {
            multi: false,
            searchValueKey: false,
            defaultValue: null,

            onSelect: function(event) {
                _this.willsend_data.shop_category = String(event.value)
            }
        };
        var picker_ = $('#catgoary').picker(picker_options);
    }
}).mount('#app')