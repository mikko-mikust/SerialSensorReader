from datetime import datetime
import sqlite3, serial,time

f = open("config.txt", "r")
b = dict(eval(f.read()))
#print(b['db_name'])
db = sqlite3.connect(b['db_name'])
cur = db.cursor()
cur.execute(
    """
    create table if not exists %s(
    time datetime primary key,
    temp double,
    humidity double
    )
    """ % (b["table_name"])
)

ser=serial.Serial(
    port=b['serial_name'],
    timeout=b['serial_timeout'],
    baudrate=b['serial_baudrate'])
##print(type(b['db_commit_interval']))
try:
    while 1:
        for t in range(b['db_commit_interval']):
            ser.write(b['temp_read_instruction'])
            temp_res = ser.read(size=7)
            temp_f = int.from_bytes(temp_res[3:5], byteorder="big") / 10
            print(datetime.utcnow(), end=' ')
            print(temp_res, end=' ')
            print(temp_f, end=' ')

            ser.write(b['humidity_read_instruction'])
            humidity_res = ser.read(size=7)
            humidity_f = int.from_bytes(humidity_res[3:5], byteorder="big") / 10

            print(humidity_res, end=' ')
            print(humidity_f)

            cur.execute(f"insert into %s (time,temp,humidity) values ('%s',%f,%f)"
                        % (b["table_name"], datetime.utcnow(), temp_f, humidity_f)
                        )
            time.sleep(b['serial_collection_interval'])
        db.commit()
except KeyboardInterrupt:
    db.commit()

cur.close()
db.close()

