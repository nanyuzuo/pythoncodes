# TODO 定义函数weeklyWage，传入3个参数 hourly_wage , hours_worked , standard_hours
def weeklyWage(hourly_wage: float, hours_worked: float, standard_hours: float) -> float:
    """计算员工的周工资。

    Args:
        hourly_wage: 每小时基本工资
        hours_worked: 实际工作小时数
        standard_hours: 标准工作小时数（超出部分按1.5倍计算）

    Returns:
        float: 员工的周工资总额
    """
    if hours_worked <= standard_hours:
        total_wage = hourly_wage * hours_worked
    else:
        overtime_hours = hours_worked - standard_hours
        total_wage = (hourly_wage * standard_hours) + (1.5 * hourly_wage * overtime_hours)
    
    return total_wage

print(weeklyWage(10,40,35))
print(weeklyWage(20,35,35))

