var ec_left1=echarts.init(document.getElementById("left1"),"dark");
ec_left1_option = {
    backgroundColor:'#100C2A',
    title: {
        text: '全国累计趋势',
        left: 'left'
    },
    tooltip: {
        trigger: 'axis',
        axisPointer:{
            type:'line',
            lineStyle:{
                color:'#7171c6'
            },
        },
    },
    legend: {
        data: ['累计确诊', '现有疑似', '累计治愈', '累计死亡']
    },
    grid: {
        left: '3%',
        right: '4%',
        bottom: '3%',
        containLabel: true
    },
    xAxis: {
        type: 'category',
        boundaryGap: true,
        data: []
    },
    yAxis: {
        type: 'value'
    },
    series: [
        {
            name: '累计确诊',
            type: 'line',
            stack: '总量',
            smooth:true,
            data: []
        },
        {
            name: '现有疑似',
            type: 'line',
            stack: '总量',
            smooth:true,
            data: []
        },
        {
            name: '累计治愈',
            type: 'line',
            stack: '总量',
            smooth:true,
            data: []
        },
        {
            name: '累计死亡',
            type: 'line',
            stack: '总量',
            smooth:true,
            data: []
        }
    ]
};
