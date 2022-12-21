var host = "http://127.0.0.1:8080";
var html_host = "http://127.0.0.1:5500"

/**
 * 封装数据包接口
 * @param data_settings 接口url以及数据
 * @param  method  方法  post | get
 * @returns 返回后端数据
 */
async function request(data_settings) {
    //将本地存储用户信息增加到发送数据包，用于后台需要取用cookies时使用
    data_settings.data = Object.assign({}, data_settings.data, { user_data: $.zui.store.get('user_info') })
    let data = await $.ajax(data_settings)
    console.log('响应数据', data)
    if (data.result == "not_permission") { //如果没权限弹出登录
        window.parent.postMessage({ type: 'check', data: ["自定义需要发送的数据"] }, '*')
    }
    return data
}

/**
 * 超级管理员登录
 * @param username 用户密码
 * @param password 手机号
 * @returns msg:返回信息,result：状态 ok\error,cookies,login_user
 */
async function api_login_admin(send, callback) {
    let settings = {
        "url": host + "/login_admin/",
        "method": "POST",
        "data": send
    }
    let return_data = { msg, result, cookies, user_type, login_user } = await request(settings)
    callback(return_data)
}

/**
 * 上传商品
 * @param shop_name     商品名称
 * @param shop_price    商品价格
 * @param shop_category 商品分类
 * @param shop_num      商品数量
 * @param imageList     图片数组类型
 * @returns msg:返回信息,result：状态 ok\无权限
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
 * 删除商品
 * @returns msg:返回信息,result：状态 ok\无权限
 * @param id 商品id
 */
async function del_shop(send, callback) {
    send.imageList = '1' + JSON.stringify(send.imageList)
    let settings = {
        "url": host + "/del_shop/",
        "method": "POST",
        "data": send
    }
    let return_data = { msg, result, cookies } = await request(settings)
    callback(return_data)
}

/**
 * 查询所有商品
 * @param type 查询类型 三种/所有(需验证cookies)\热销\上新
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

/**
 * 添加公告
 * @param title: 公告标题
 * @param content:公告内容
 * @returns msg:返回信息,result：状态 ok\error
 */
async function add_announcement(send, callback) {
    let settings = {
        "url": host + "/add_announcement/",
        "method": "POST",
        "data": send
    }
    let return_data = { msg, result, cookies } = await request(settings)
    callback(return_data)
}

/**
 * 获取公告列表
 * @returns msg:返回信息,result：状态 ok\error
 */
async function all_announcement(send, callback) {
    let settings = {
        "url": host + "/all_announcement/",
        "method": "POST",
        "data": send
    }
    let return_data = { msg, result, cookies } = await request(settings)
    callback(return_data)
}

/**
 * 获取公告列表
 * @param id:公告的id
 * @returns msg:返回信息,result：状态 ok\error
 */
async function del_announcement(send, callback) {
    let settings = {
        "url": host + "/del_announcement/",
        "method": "POST",
        "data": send
    }
    let return_data = { msg, result, cookies } = await request(settings)
    callback(return_data)
}

/**
 * 所有订单列表
 * @param null:
 * @returns msg:返回信息,result：状态 ok\error
 */
async function all_orders(send, callback) {
    let settings = {
        "url": host + "/all_orders/",
        "method": "POST",
        "data": send
    }
    let return_data = { msg, result, cookies } = await request(settings)
    callback(return_data)
}