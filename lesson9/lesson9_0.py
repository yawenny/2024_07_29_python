#自訂function(get_status_message)功能放在主程式
def get_status_message(bmi:float)->str:
    '''
    #param bmi:這是要傳入bmi(要寫在function內的第1行)
    #return:傳出bmi的狀態
    '''
    if bmi<18.5:
        return "體重過輕"
    elif bmi<24:
        return "正常範圍"
    elif bmi<27:
        return "過重"
    elif bmi<30:
        return "輕度肥胖"
    elif bmi<35:
        return "中度肥胖"
    elif bmi>=35:
        return "重度肥胖"

while True:
    try:
        name=str(input("請輸入姓名"))
        height=float(input('請輸入身高'))
        weight=float(input('請輸入體重'))
        bmi=round(weight/(((height*0.01))**2),ndigits=2)
        message = get_status_message(bmi)
        print(f"{name} 的 bmi 為 {bmi},為{message}")
    except ValueError:
        print("格式錯誤")
        continue
    stuff = input("請問是否繼續輸入資料 ('q':離開,任意鍵:繼續)?")

    if stuff == 'q':
        break
    

print("應用程式結束")