
# TODO 定义函数weeklyWage，传入3个参数 hourlyWage , hour , standardHours
def weeklyWage(hourlyWage,hour,standardHours): 
    if  hour <= standardHours: 
         total = hourlyWage * hour
    else: 
         total = hourlyWage * standardHours + 1.5 * hourlyWage * (hour - standardHours)
    return total
print(weeklyWage(10,40,35))
print(weeklyWage(20,35,35))

