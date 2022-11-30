var host = "http://pu2crp.natappfree.cc"

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