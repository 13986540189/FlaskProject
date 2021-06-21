ec_right2 = echarts.init(document.getElementById("right2"), "dark")
var keywords = []
ec_right2_option = {
    backgroundColor: '#100C2A',
     title: {
        text: '今日疫情热搜',
        left: 'left'
    },
    series: [{
        type: 'wordCloud',
        shape: 'circle', //circle cardioid diamond triangle-forward triangle
        left: 0,
        right: 0,
        top: 0,
        width: '100%',
        height: '100%',
        gridSize: 0, //值越大，word间的距离越大，单位像素
        sizeRange: [10, 32], //word的字体大小区间，单位像素
        rotationRange: [-45, 0, 45, 90], //word的可旋转角度区间
        textStyle: {
            normal: {
                color: function () {
                    return 'rgb(' + [
                        Math.round(Math.random() * 160),
                        Math.round(Math.random() * 160),
                        Math.round(Math.random() * 160)
                    ].join(',') + ')';
                }
            },
            emphasis: {
                shadowBlur: 2,
                shadowColor: '#000'
            }
        },
        data: keywords,
    }]
};

