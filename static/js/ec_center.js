var ec_center=echarts.init(document.getElementById("center2"),"dark");

en_center_option = {
    backgroundColor:'#100C2A',
    title: {
        text: '',
        subtext: '',
        x: 'left'
    },
    tooltip: {
        trigger: 'item'
    },
    legend: {
        orient: 'vertical',
        left: 'left',
        data: ['订单量']
    },
    visualMap: {
        type: 'piecewise',
        pieces: [
            {min: 50000},
            {min: 1000, max: 4999},
            {min: 500, max: 999},
            {min: 100, max: 499},
            {min: 10, max: 99},
            {min:1,max: 5}
        ],
        color: ['#960404', '#DF013A', '#FE2E64','#F78181','#F5A9A9','#FBEFEF']
    },
       roamController: {
        show: true,
        left: 'right',
        mapTypeControl: {
            'china': true
        }
    },

    series: [
        {
            name: '累计确诊人数',
            type: 'map',
            mapType: 'china',
            roam: false,
            label: {
                show: true,
                fontSize: 8
            },
            emphasis: {
                show:true,
                fontSize:8
            },
            itemStyle:{
              normal:{
                  borderWidth:0,
                  borderColor:"#009fe8",
                  areaColor:"#ffefd5"
              },
              emphasis:{
                  borderWidth:0,
                  borderColor:"#4b0082",
                  areaColor:"#fff"
              }
            },
            data:[]
        }
    ]
};

