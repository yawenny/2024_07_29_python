class MyClass():
    @classmethod
    def get_status_message(cls,bmi:float)->str:
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