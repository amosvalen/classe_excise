def bmi_value(weight, height):
    return weight/(height/100)**2


def suggestion(bmi):
    message = ""
    if bmi < 18.5:
        message = "體重過輕"
    elif bmi < 24:
        message = "體重正常"
    elif bmi < 27:
        message = "體重過重"
    elif bmi < 30:
        message = "輕度肥胖"
    elif bmi < 35:
        message = "中度肥胖"
    else:
        message = "重度肥胖"
    return message


def user_bmi():
    name = input("請輸入姓名:")
    height = int(input("請輸入身高(公分):"))
    weight = int(input("請輸入體重(公斤):"))
    bmi = bmi_value(weight, height)
    info = suggestion(bmi)
    print(f"{name}您好:")
    print(f"您的BMI數值是{bmi}")
    print(f"給您的建議是{info}")
