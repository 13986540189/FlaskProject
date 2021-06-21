function get_time() {
    $.ajax({
        //请求的url地址
            url: "/time",
        //若请求成功将响应的数据显示在页面上
            success: function (data) {
                $("#time").html(data)
            },
        }
    );
}

function get_c1_data() {
    $.ajax({
        url: "/center1",
        success: function (data) {
            //总感染人数
            $(".num h1").eq(0).text(data.confirm)
            //总疑似案例
            $(".num h1").eq(1).text(data.suspect)
            //总康复人数
            $(".num h1").eq(2).text(data.heal)
            //总死亡人数
            $(".num h1").eq(3).text(data.dead)
        }
    })
}

function get_c2_data() {
    $.ajax({
        url: "/center2",
        success: function (data) {
            //将服务器响应给客户端的数据作为echarts的option参数
            en_center_option.series[0].data = data.data;
            //设置疫情地图的option
            ec_center.setOption(en_center_option);
        }
    });
}

function get_l1_data() {
    $.ajax({
        url: "/left1",
        success: function (data) {
            ec_left1_option.xAxis.data=data.day;
            ec_left1_option.series[0].data=data.confirm;
            ec_left1_option.series[1].data=data.suspect;
            ec_left1_option.series[2].data=data.heal;
            ec_left1_option.series[3].data=data.dead;
            //设置疫情地图的option参数
            ec_left1.setOption(ec_left1_option);
        }
    });
}

function get_l2_data() {
    $.ajax({
        url: "/left2",
        success: function (data) {
            ec_left2_option.xAxis.data=data.day;
            ec_left2_option.series[0].data=data.confirm_add;
            ec_left2_option.series[1].data=data.suspect_add;
            ec_left2_option.series[2].data=data.heal_add;
            ec_left2_option.series[3].data=data.dead_add;
            //设置疫情地图的option参数
            ec_left2.setOption(ec_left2_option);
        }
    });
}

function get_r1_data() {
    $.ajax({
        url: "/right1",
        success: function (data) {
            ec_right1_option.xAxis.data=data.province_name;
            ec_right1_option.series[0].data=data.confirm;
            //设置疫情地图的option参数
            ec_right1.setOption(ec_right1_option);
        }
    });
}

function get_r2_data() {
    $.ajax({
        url: "/right2",
        success: function (data) {
            ec_right2_option.series[0].data=data.keyword;
            //设置疫情地图的option参数
            ec_right2.setOption(ec_right2_option);
        }
    });
}


get_time();
get_c1_data();
get_c2_data();
get_l1_data();
get_l2_data();
get_r1_data();
get_r2_data();
setInterval(get_time,1000);
setInterval(get_c1_data,10000);
setInterval(get_c2_data,10000*10);
setInterval(get_l1_data,10000);
setInterval(get_l2_data,10000*10);
setInterval(get_r1_data,10000*10);
setInterval(get_r2_data,2000);


