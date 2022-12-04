var host = "http://127.0.0.1:8080";

/**
 * 封装数据包接口
 * @param data_settings 接口url以及数据
 * @param  method  方法  post | get
 * @returns 返回后端数据
 */
async function request(data_settings) {
    let data = await $.ajax(data_settings)
    console.log(data)
    return data
}

/**
 * 超级管理员登录
 * @param username 用户密码
 * @param password 手机号
 * @returns msg:返回信息,result：状态 ok\error,cookies
 */
async function api_login_admin(send, callback) {
    let settings = {
        "url": host + "/login_admin/",
        "method": "POST",
        "data": send
    }
    let return_data = { msg, result, cookies } = await request(settings)
    callback(return_data)
}

/**
 * 上传商品
 * @param shop_name     商品名称
 * @param shop_price    商品价格
 * @param shop_category 商品分类
 * @param shop_num      商品数量
 * @param imageList     图片数组类型
 * @returns msg:返回信息,result：状态 ok\error,cookies
 */
async function api_add_shop(send, callback) {
    send.imageList = '1' + JSON.stringify(send.imageList)
    let settings = {
        "url": host + "/add_shop/",
        "method": "POST",
        "data": send
    }
    let return_data = { msg, result, cookies } = await request(settings)
    callback(return_data)
}

/**
 * 查询所有商品
 * @param type 查询类型
 * @returns msg:返回信息,result：状态 ok\error,cookies
 */
async function api_find_shoping(send, callback) {
    let settings = {
        "url": host + "/find_shoping/",
        "method": "POST",
        "data": send
    }
    let return_data = { msg, result, cookies } = await request(settings)
    callback(return_data)
}