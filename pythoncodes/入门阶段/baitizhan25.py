# TODO 导入模块calendar
from calendar import isleap
# TODO 定义函数numLeapYear，传入参数year_start和year_end
def numLeapYear(year_start,year_end):
    num = 0
    for year in range(year_start,year_end + 1):
        if  isleap(year):
            num = num + 1
    return num
print(numLeapYear(1900,2022))