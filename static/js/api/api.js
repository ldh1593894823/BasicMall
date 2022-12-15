var host = "http://192.168.31.127:8080";

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
 * 注册接口
 * @param username 用户昵称
 * @param password 用户密码
 * @param phone 用户手机号码
 * @returns msg:返回信息,result：状态 ok\error
 */
async function api_register(send, callback) {
    let settings = {
        "url": host + "/register/",
        "method": "POST",
        "data": send
    }
    let return_data = { msg, result } = await request(settings)
    callback(return_data)
}

/**
 * 登录接口
 * @param password 用户密码
 * @param phone 手机号
 * @returns msg:返回信息,result：状态 ok\error
 */
async function api_login(send, callback) {
    let settings = {
        "url": host + "/login/",
        "method": "POST",
        "data": send
    }
    let return_data = { msg, result, user_type, login_user } = await request(settings)
    callback(return_data)
}

/**
 * 超级管理员登录
 * @param password 用户密码
 * @param phone 手机号
 * @returns msg:返回信息,result：状态 ok\error
 */
async function api_login(send, callback) {
    let settings = {
        "url": host + "/login/",
        "method": "POST",
        "data": send
    }
    let return_data = { msg, result } = await request(settings)
    callback(return_data)
}

/**
 * 获取商品接口
 * @param hot_shop 热销商品
 * @returns msg:返回信息,result：状态 ok\error
 */
async function api_new_hot_shop(send, callback) {
    let settings = {
        "url": host + "/find_shoping/",
        "method": "POST",
        "data": send
    }
    let return_data = { msg, result } = await request(settings)
    callback(return_data)
}