#classmethod
from widget2.tools import MyClass
while True:
    try:
        name=str(input("請輸入姓名"))
        height=float(input('請輸入身高'))
        weight=float(input('請輸入體重'))
        bmi=round(weight/(((height*0.01))**2),ndigits=2)
        message =MyClass.get_status_message(bmi)
        print(f"{name} 的 bmi 為 {bmi},為{message}")
    except ValueError:
        print("格式錯誤")
        continue
    stuff = input("請問是否繼續輸入資料 ('q':離開,任意鍵:繼續)?")

    if stuff == 'q':
        break
    

print("應用程式結束")