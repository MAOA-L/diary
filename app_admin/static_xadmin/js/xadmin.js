$(function () {
    //加载弹出层
    layui.use(['form','element'],
    function() {
        layer = layui.layer;
        element = layui.element();
    });

    //判断是否显示左侧菜单
    $(window).resize(function(){
        width=$(this).width();
        if(width>1024){
            $('#side-nav').show();
        }
    });

    //背景初始化
    $('.reset').click(function  () {
        localStorage.clear();
        layer.msg('初如化成功',function(){});
    });

    //窄屏下的左侧菜单隐藏效果
    $('.container .open-nav svg').click(function(event) {
        $('#side-nav').toggle(400);
        // $('.wrapper .left-nav').toggle(400)
    });

    //左侧菜单效果
    $('.left-nav #nav li.list').click(function () {
        console.log("看一下到底是什么",$(this));
        if($(this).hasClass('open')){
            $(this).removeClass('open');
            $(this).find('a i.icon_i').removeClass("icon_rotate");
            $(this).children('.sub-menu').slideUp();
            // $(this).siblings().children('.sub-menu').slideUp();
        }else{
            $(this).addClass('open');
            $(this).find('a i.icon_i').addClass("icon_rotate");
            $(this).children('.sub-menu').slideDown();
            $(this).siblings().children('.sub-menu').slideUp();
            $(this).siblings().find('a i.icon_i').removeClass("icon_rotate");
            $(this).siblings().removeClass('open');
        }
    });
    $("ul.sub-menu li a").click(function (e) {
        console.log($(this).html());
        e.stopPropagation();
    });

});

/**
 * 初始化菜单，将相应的栏目置为打开状态和赋值背景
 * @param obj
 * @param children_a_id
 */
function need_open_li(obj, children_a_id) {
    $(obj).addClass('current open');
    $(obj).find('a i.icon_i').addClass("icon_rotate");
    $(obj).children('.sub-menu').slideDown();

    $(obj).find("a").eq(children_a_id).css("background", "#00BCD4").css("color", "white");

}


/*弹出层*/
/*
    参数解释：
    title   标题
    url     请求的url
    id      需要操作的数据id
    w       弹出层宽度（缺省调默认值）
    h       弹出层高度（缺省调默认值）
*/
function x_admin_show(title,url,w,h){
    if (title == null || title == '') {
        title=false;
    };
    if (url == null || url == '') {
        url="404.html";
    };
    if (w == null || w == '') {
        w=800;
    };
    if (h == null || h == '') {
        h=($(window).height() - 50);
    };
    layer.open({
        type: 2,
        area: [w+'px', h +'px'],
        fix: false, //不固定
        maxmin: true,
        shadeClose: true,
        shade:0.4,
        title: title,
        content: url
    });
}

/*关闭弹出框口*/
function x_admin_close(){
    var index = parent.layer.getFrameIndex(window.name);
    parent.layer.close(index);
}
