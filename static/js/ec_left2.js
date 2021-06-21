var ec_left2=echarts.init(document.getElementById("left2"),"dark");
ec_left2_option = {
    backgroundColor:'#100C2A',
    title: {
        text: '全国新增趋势',
        left: 'left'
    },
    tooltip: {
        trigger: 'axis',
        axisPointer:{
            type:'line',
            lineStyle:{
                color:'#7171c6'
            }

        }
    },
    legend: {
        data: ['新增确诊', '新增疑似', '新增治愈', '新增死亡']
    },
    grid: {
        left: '3%',
        right: '4%',
        bottom: '3%',
        containLabel: true
    },
    xAxis: {
        type: 'category',
        boundaryGap: false,
        data: []
    },
    yAxis: {
        type: 'value'
    },
    series: [
        {
            name: '新增确诊',
            type: 'line',
            stack: '总量',
            data: []
        },
        {
            name: '新增疑似',
            type: 'line',
            stack: '总量',
            data: []
        },
        {
            name: '新增治愈',
            type: 'line',
            stack: '总量',
            data: []
        },
        {
            name: '新增死亡',
            type: 'line',
            stack: '总量',
            data: []
        }
    ]
};
