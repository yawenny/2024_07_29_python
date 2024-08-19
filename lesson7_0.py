
while True:
    try:
        name=input("請輸入姓名:")
        height=float(input('請輸入身高:'))
        weight=float(input('請輸入體重:'))
        bmi=round(weight/(((height*0.01))**2),ndigits=2)
        if bmi<18.5:
            grade="過輕"
        elif bmi<24:
            grade="正常"
        elif bmi<27:
            grade="過重"
        elif bmi<30:
            grade="輕度肥胖"
        elif bmi<35:
            grade="中度肥胖"
        elif bmi>=35:
            grade="重度肥胖"
        print(f"{name}您好,您的的BMI值為{bmi},體重:{grade}")
    except ValueError:
        print("格式錯誤")
        continue
    answer=input("是否再進行計算?按q會離開,enter繼續")
    if answer == 'q':
        break 
       
print("應用程式結束")
