# SerialSensorReader
从串口读取温湿度并写入sqlite3数据库
# config.txt配置
|配置名|python数据类型|默认值|描述|
|-------|---|---|---|
|db_name|str|1.db|打开或创建的数据库文件名称|
|table_name|str|"temperature"|从数据库打开或创建的表名称|
|db_commit_interval|int|5|每隔几次将结果数据提交进数据库|
|serial_collection_interval|int|2|每隔几秒读取串口数据|
|serial_name|str|""|串口号|
|serial_baudrate|int|9600|波特率|
|serial_timeout|int|2|串口超时时间|
|temp_read_instruction|bytes|b"\x01\x03\x00\x00\x00\x01\x84\x0A"|发送的读取温度的指令|
|humidity_read_instruction|bytes|b"\x01\x03\x00\x01\x00\x01\xD5\xCA"|发送的读取湿度的指令|
# 表结构
|字段名|sqlite3内部数据类型|单位|栗子|
|---|---|---|---|
|时间|datetime|以UTC时间计算的日期|1919-08-10 11:45:14.114514|
|温度|double|摄氏度|11.4|
|湿度|double|百分比|51.4|
