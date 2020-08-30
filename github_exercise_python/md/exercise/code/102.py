import datetime
import time

# 创建活动结束日期
activityDateTime = datetime.datetime(2019, 4, 13, 18, 0, 0)

"""命令行输出"""
while datetime.datetime.now() < activityDateTime:
    differDateTime = activityDateTime - datetime.datetime.now()
    print("倒计时：{}天 {}：{}：{}".format(
        differDateTime.days,
        differDateTime.seconds // 3600,
        differDateTime.seconds // 60 % 60,
        differDateTime.seconds % 3600 % 60
    ))
    time.sleep(1)

print("活动结束")
