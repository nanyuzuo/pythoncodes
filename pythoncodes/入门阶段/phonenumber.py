import random
def phoneNo(operator,chooseType):
    no1 = "1"
    no2 = random.choice(["3","5","7","8","9"])
    if no2 in ["3","8"]:
        no3 = str(random.randint(0,9))
    elif no2 == "5":
        no3 = random.choice(["0","1","2","3","5","6","7","8","9"])
    elif no2 == "7":
        no3 = random.choice(["0","1","2","3","5","6","7","8"])
    else: 
        no3 = random.choice(["8","9"])
    if operator == "四川移洞":
        no4 = random.choice(["5","7","8","9"])
    elif operator == "四川连通":
        no4 = random.choice(["0","2","5","6","9"])
    elif operator == "四川电兴":
        no4 = random.choice(["3","7","9"])
    else:
        print("没有该种运营商类型")
    if chooseType == "选取靓号":
        no5 = random.choice(["6666666","8888888","9999999"])
    elif chooseType == "普通选号":
        no5 = str(random.randint(1000000,9999999))
    else:
        print("没有该种选号类型")
    phoneNumber = no1 + no2 + no3 + no4 + no5
    return phoneNumber
phoneNumber = phoneNo("四川连通","选取靓号")
if phoneNumber == "19999999999":
    print("我要办理该手机号，号码为：19999999999")
else:
    print("该号码不是我想要的号码，我不办理")