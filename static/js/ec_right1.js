var ec_right1 = echarts.init(document.getElementById("right1"), "dark")
ec_right1_option = {
    backgroundColor:'#100C2A',
    title: {
        text: '非湖北地区确诊TOP5',
        left: 'left'
    },
    color: '#3398DB',
    grid: {
        left: '3%',
        right: '4%',
        bottom: '3%',
        containLabel: true
    },
    xAxis: {
        type: 'category',
        data: []
    },
    tooltip: {
        trigger: 'axis',
        axisPointer: {
            type: 'shadow',
        },
    },
    yAxis: {
        type: 'value'
    },
    series: [{
        data: [],
        type: 'bar',
        barMaxWidth: "50%"
    }]
};
