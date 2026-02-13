var contbox = document.querySelector('#contbox');
//img
var img_ul = document.querySelector('#img_list');
var img_li = document.querySelectorAll('#img_list>li');
var img_listlen = img_li.length;

//切换按钮
var left_arrow = document.querySelector('.left_arrow');
var right_arrow = document.querySelector('.right_arrow');

//指示点
var dot_list = document.querySelector('#dot_list');
var dot_a = document.querySelectorAll('.dot');

//other
var curidx = 0;
var timer = null;

// 隐藏函数----实现关键
function hide_Myself() {
    img_li[curidx].style.opacity = 0;
    img_li[curidx].style.zIndex = 0;
}
// 显示函数----实现关键
function show_Myself() {
    img_li[curidx].style.opacity = 1;
    img_li[curidx].style.zIndex = 1;
}
// 左滑按钮
left_arrow.onclick = function () {
    hide_Myself()
    curidx == 0 ? curidx = 4 : curidx--;//边界判断
    show_Myself()
    changdot()
};
// 右滑按钮
right_arrow.onclick = function () {
    hide_Myself()
    curidx == 4 ? curidx = 0 : curidx++;//边界判断
    show_Myself()
    changdot()
};
//自动轮播
function running() {
    timer = setInterval(function () {//timer用于清除定时器
        right_arrow.onclick()
        changdot()//同时改变指示点
    }, 2500)//每2.5秒自动轮播一次
}
running();
//细节处理
contbox.onmouseenter = function () {
    clearInterval(timer)//鼠标移动到容器上时，停止自动轮播
}
contbox.onmouseleave = function () {
    running()//鼠标移开容器之外，开始自动轮播
}
//指示点
function changdot() {
    for (let i = 0; i < dot_a.length; i++) {
        if (dot_a[i].classList.contains('cur')) {
            dot_a[i].classList.remove('cur')
            break;//如果找到cur类了，就删除cur类，并且立即退出循环
        }
    }
    dot_a[curidx].classList.add('cur');//所有的指示点都没有cur类了，那么给当前指示点添加cur
}
// 为dot自定义属性:data_order（自命名）
for (let i = 0; i < dot_a.length; i++) {
    dot_a[i].data_order = i;
    dot_a[i].onclick = function () {
        curidx = this.data_order;
        changdot()
        Jump()
        // console.log(this.data_order + ":" + curidx);
    }
}
// 底部原点跳转方法：
function Jump() {
    //当前curidx的li(既img_li[curidx]),设置到最顶层，其余的被覆盖
    show_Myself()
    for (let j = 0; j < img_li.length; j++) {
        if (curidx == j) {
            continue;
        }
        img_li[j].style.opacity = 0;
        img_li[j].style.zIndex = 0;
        // console.log(curidx);
        // hide_Myself();此处不能直接写函数,因为需要引用j的值作为curidx，循环结束会改变curidx的值
    }
}
