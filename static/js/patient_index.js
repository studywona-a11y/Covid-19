// 柱状图1模块
(function() {
  // 实例化对象
  var myChart = echarts.init(document.querySelector(".bar .chart"),);
  // 指定配置和数据
   var option={
    tooltip: {
    trigger: 'axis',
    axisPointer: {
      type: 'shadow'
    }
  },
    xAxis: {
      data: ['男性', '女性'],
      axisLabel: {
      align: "center",
    }
    },
    yAxis: {
      type:'value',
      min: 500,
      axisLabel: {
          margin: 6,
        fontSize:9,
    }
    },
    dataGroupId: '',
    animationDurationUpdate: 500,
    series: {
      type: 'bar',
      id: 'age',
      data: [
        {
          value: male,
          itemStyle:{color:'#69cce6'},
          groupId: 'male'
        },
        {
          value: female,
            itemStyle:{color:'#ff8282'},
          groupId: 'female'
        },
      ],
      universalTransition: {
        enabled: true,
        divideShape: 'clone'
      }
    }
  };
  const drilldownData = [
    {
      dataGroupId: 'male',
      data: [
        ['少年(0-17)', children],
        ['青年（18-45）', young],
        ['中年（46-69）', adults],
        ['老年（70及以上）', older],
      ]
    },
    {
      dataGroupId: 'female',
      data: [
        ['少年(0-17)', childrenN],
        ['青年（18-45）', youngN],
        ['中年（46-69）', adultsN],
        ['老年（70及以上）', olderN],
      ]
    },
  ];
  myChart.on('click', function (event) {
    if (event.data) {
      var subData = drilldownData.find(function (data) {
        return data.dataGroupId === event.data.groupId;
      });
      if (!subData) {
        return;
      }
      myChart.setOption({
        xAxis: {
          data: subData.data.map(function (item) {
            return item[0];
          })
        },
        series: {
          type: 'bar',
          id: 'age',
          dataGroupId: subData.dataGroupId,
          data: subData.data.map(function (item) {
            return item[1];
          }),
          universalTransition: {
            enabled: true,
            divideShape: 'clone'
          }
        },
        graphic: [
          {
            type: 'text',
            left: 50,
            top: 20,
            style: {
              text: 'Back',
              fontSize: 18
            },
            onclick: function () {
              myChart.setOption(option);
            }
          }
        ]
      });
    }
  });
  // // 把配置给实例对象
  myChart.setOption(option);
  // //图像自适应
  window.addEventListener("resize", function() {
    myChart.resize();
  });
  })();

(function(){
    var myChart = echarts.init(document.querySelector(".bar .chart1"),'macarons');
//     var option = {
//   legend: {
//     top: 'bottom'
//   },
//   toolbox: {
//     show: true,
//     feature: {
//       mark: { show: true },
//       dataView: { show: true, readOnly: false },
//       restore: { show: true },
//       saveAsImage: { show: true }
//     }
//   },
//   series: [
//     {
//       name: 'Nightingale Chart',
//       type: 'pie',
//       radius: [5, '75%'],
//       center: ['50%', '50%'],
//       roseType: 'area',
//       itemStyle: {
//         borderRadius: 15
//       },
//       legend: {
//     orient: 'vertical',
//     left: 'left'
//   },
//       data: [
//         { value: pfeiyan, name: '肺炎' },
//         { value: prenshen, name: '妊娠' },
//         { value: ptangniaobing, name: '糖尿病' },
//         { value: pfeiqizhong, name: '肺气肿' },
//         { value: pxiaochuan, name: '哮喘' },
//         { value: pgaoxueya, name: '高血压 ' },
//         { value: pxinxueguan, name: '心血管' },
//         { value: pfeipang, name: '肥胖' },
//         { value: pshenshuaijie, name: '肾衰竭' },
//         { value: psmoking, name: '吸烟' },
//         { value: pcontacts, name: '接触者' },
//         { value: pothers, name: '其他' }
//       ]
//     }
//   ]
// };
  var option = {
  title: {
    // text: 'Referer of a Website',
    // subtext: 'Fake Data',
    left: 'center'
  },
  tooltip: {
    trigger: 'item'
  },
  legend: {
    orient: 'vertical',
    left: 'left'
  },
  series: [
    {
      name: 'Access From',
      type: 'pie',
      radius: '50%',
      selectedMode: "true",
      left: "5%",
      data: [
        { value: pfeiyan, name: '肺炎' },
        { value: prenshen, name: '妊娠' },
        { value: ptangniaobing, name: '糖尿病' },
        { value: pfeiqizhong, name: '肺气肿' },
        { value: pxiaochuan, name: '哮喘' },
        { value: pgaoxueya, name: '高血压 ' },
        { value: pxinxueguan, name: '心血管' },
        { value: pfeipang, name: '肥胖' },
        { value: pshenshuaijie, name: '肾衰竭' },
        { value: psmoking, name: '吸烟' },
        { value: pcontacts, name: '接触者' },
        { value: pothers, name: '其他' }
      ],
      top:2,
      emphasis: {
        itemStyle: {
          shadowBlur: 10,
          shadowOffsetX: 0,
          shadowColor: 'rgba(0, 0, 0, 0.5)'
        }
      }
    }
  ]
};
    myChart.setOption(option);
  // //图像自适应
  window.addEventListener("resize", function() {
    myChart.resize();
  });
})();

