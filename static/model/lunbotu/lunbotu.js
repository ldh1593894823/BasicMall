$(function() {
    /*保存当前图片的索引*/
    let index = 0;
    let btn = false;
    /*去除a标签自带的刷新*/
    $('a[href=""]').prop('href', 'javascript:;');
    /*开始先把图片隐藏，默认显示第一张图*/
    $('.content>ul>li').hide();
    $('.content>ul>li:eq(0)').show();
    // 设置方向箭头图标的淡入、淡出
    $('.carousel').hover(function() {
            $('.pos').stop().fadeIn()
        }, function() {
            $('.pos').stop().fadeOut()
        })
        // 为左方向图标绑定点击事件
    $('.left').on('click', function() {
            btn = true;
            clean();
            if (index == 0) {
                index = 2;
            } else {
                --index;
            }
            show();
        })
        // 为右方向图标绑定点击事件
    $('.right').on('click', function() {
            btn = true;
            clean();
            if (index == 2) {
                index = 0;
            } else {
                ++index;
            }
            show();
        })
        //指示器指示功能（为指示器绑定点击事件）
    $('.dot li').on('click', function() {
            btn = true;
            let now = $(this).index()
            if (now != index) {
                clean();
                index = now;
                show();
            }
        })
        //自动播放功能（定时器）
    setInterval(function() {
            if (!btn) {
                clean();
                if (index == 2) {
                    index = 0;
                } else {
                    ++index;
                }
                show();
            } else {
                btn = false;
            }
        }, 2000)
        //清除上一张图片和指示器上的指示
    function clean() {
        $(`.content>ul>li:eq(${index})`).stop().fadeOut();
        $(`.dot>ul>li:eq(${index})`).removeClass('active');
    }
    //添加新的图片和指示器上的指示
    function show() {
        // console.log(index);
        $(`.content>ul>li:eq(${index})`).stop().fadeIn();
        // console.log($(`.content>ul>li:eq(${index})`))
        $(`.dot>ul>li:eq(${index})`).addClass('active');
    }
})