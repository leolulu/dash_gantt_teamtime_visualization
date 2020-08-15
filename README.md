# dash_gantt_teamtime_visualization

## 数据表

|中文|英文|必填与否|备注|
|-|-|-|-|
|目前状态|current_status||		
|责任人|liable_person|必填|	
|数据分类|category|必填|[客源，房源，小B，VR，新房]
|数据表|data_table|必填||	
|使用对象|user|必填|	
|星期|weekdays||默认值0|
|预计花费时间（分钟）|time_consuming|必填|	“已设置”或其他
|是否能设置看板|board_feasibility|		
|是否建立with as模块化|with_as_modulable|		
|看板链接|board_url||		
|开始时间|btime|必填|	类似9.5  ->  9:30这种
|结束时间|etime|必填|	类似18  ->  18:00这种

## 参考文献
https://dash.plotly.com/interactive-graphing
https://plotly.com/python/line-and-scatter/
https://plotly.com/python/bar-charts/
https://plotly.com/python/gantt/
https://plotly.com/python/time-series/
https://dash.plotly.com/dash-core-components/graph