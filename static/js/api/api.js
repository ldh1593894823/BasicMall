var host = "http://127.0.0.1:8080";
var html_host = "http://127.0.0.1:5500"

// var host = "http://mickeycat.luncode.com:8080";
// var html_host = "http://mickeycat.luncode.com:5500"

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
    if (data.result == "not_permission") { //如果没权限弹出登录
        window.location.href = "/user/login.html";
    }
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
/***********************************************购物车管理接口 *****************************************/
/**
 * 添加购物车接口
 * @param shop_id 商品对应id
 * @returns msg:返回信息,result：状态 ok\error
 */
async function add_shop_car(send, callback) {
    let settings = {
        "url": host + "/add_shop_car/",
        "method": "POST",
        "data": send
    }
    let return_data = { msg, result } = await request(settings)
    callback(return_data)
}

/**
 * 查询当前用户所有购物车内容
 * @returns msg:返回信息,result：状态 ok\error
 */
async function all_shop_car(send, callback) {
    let settings = {
        "url": host + "/all_shop_car/",
        "method": "POST",
        "data": send
    }
    let return_data = { msg, result } = await request(settings)
    callback(return_data)
}

/**
 * 删除购物车中的一件商品
 * @param car_id 商品对应id
 * @returns msg:返回信息,result：状态 ok\error
 */
async function del_shop_car(send, callback) {
    let settings = {
        "url": host + "/del_shop_car/",
        "method": "POST",
        "data": send
    }
    let return_data = { msg, result } = await request(settings)
    callback(return_data)
}

/***********************************************用户订单管理接口 *****************************************/

/**
 * 新建订单
 * @param courier_name,courier_phone,courier_place 收货人信息
 * @returns msg:返回信息,result：状态 ok\error
 */
async function create_order(send, callback) {
    let settings = {
        "url": host + "/create_order/",
        "method": "POST",
        "data": send
    }
    let return_data = { msg, result } = await request(settings)
    callback(return_data)
}

/**
 * 查询未支付订单详情 订单还未支付的情况下 返回订单内商品列表
 * @param order_id 订单编号
 * @returns msg:返回信息,result：状态 ok\error
 */
async function order_list(send, callback) {
    let settings = {
        "url": host + "/order_list/",
        "method": "POST",
        "data": send
    }
    let return_data = { msg, result } = await request(settings)
    callback(return_data)
}

/**
 * 查询不同类型订单 1待付款 2待发货 3待收货 4已完成
 * @param order_id 订单编号
 * @returns msg:返回信息,result：状态 ok\error
 */
async function find_order(send, callback) {
    let settings = {
        "url": host + "/find_order/",
        "method": "POST",
        "data": send
    }
    let return_data = { msg, result } = await request(settings)
    callback(return_data)
}

/**
 * 删除订单接口
 * @param order_id 订单编号
 * @returns msg:返回信息,result：状态 ok\error
 */
async function del_myorder(send, callback) {
    let settings = {
        "url": host + "/del_myorder/",
        "method": "POST",
        "data": send
    }
    let return_data = { msg, result } = await request(settings)
    callback(return_data)
}

/**
 * 支付订单
 * @param order_id 订单编号
 * @returns msg:返回信息,result：状态 ok\error
 */
async function pay_myorder(send, callback) {
    let settings = {
        "url": host + "/pay_myorder/",
        "method": "POST",
        "data": send
    }
    let return_data = { msg, result } = await request(settings)
    callback(return_data)
}

/**
 * 对订单进行收货处理
 * @param order_id 订单编号 快递单号
 * @returns msg:返回信息,result：状态 ok\error
 */
async function harvest_myorder(send, callback) {
    let settings = {
        "url": host + "/harvest_myorder/",
        "method": "POST",
        "data": send
    }
    let return_data = { msg, result } = await request(settings)
    callback(return_data)
}

/**
 * 获取一条公告
 * @param order_id 订单编号 快递单号
 * @returns msg:返回信息,result：状态 ok\error
 */
async function get_a_announcement(send, callback) {
    let settings = {
        "url": host + "/get_a_announcement/",
        "method": "POST",
        "data": send
    }
    let return_data = { msg, result } = await request(settings)
    callback(return_data)
}

/**
 * 对订单进行退换货申请
 * @param order_id 订单编号
 * @returns msg:返回信息,result：状态 ok\error
 */
async function refunds_exchanges(send, callback) {
    let settings = {
        "url": host + "/refunds_exchanges/",
        "method": "POST",
        "data": send
    }
    let return_data = { msg, result } = await request(settings)
    callback(return_data)
}

/**
 * 普通用户发布评论
 * @param order_id 订单编号
 * @returns msg:返回信息,result：状态 ok\error
 */
async function add_evaluation(send, callback) {
    let settings = {
        "url": host + "/add_evaluation/",
        "method": "POST",
        "data": send
    }
    let return_data = { msg, result } = await request(settings)
    callback(return_data)
}
