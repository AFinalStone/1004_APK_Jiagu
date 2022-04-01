import time
from dateutil.parser import parse

start_time = time.localtime()
print("开始时间=================" + str(time.strftime("%Y-%m-%d %H:%M:%S", start_time)))
time.sleep(5)
end_time = time.localtime()
print("结束时间=================" + str(time.strftime("%Y-%m-%d %H:%M:%S", end_time)))
parse(start_time)
print(f"总用时================={str((end_time - start_time) / 1000)}秒")
