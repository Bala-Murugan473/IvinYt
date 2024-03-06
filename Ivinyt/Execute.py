import pandas as pd
import os
import datetime as dt

xl_path =os.path.abspath(os.path.dirname(__file__))+"/data/classic_data.xlsx"
class Execute:
    @staticmethod
    def MatchDetails():
        # df=pd.read_excel(xl_path, sheet_name='MatchDetails',engine='openpyxl')
        # date=df['MatchDate'][0]
        # time=df['MatchTime'][0]
        # price=df['Price'][0]
        # return date,time,price
        return "","",""

    @staticmethod
    def RemainingSlots():
        return 25 - pd.read_excel(xl_path, sheet_name='Classic',engine='openpyxl')['slot'].count()
    
    @staticmethod
    def Date():
        return dt.datetime.now()
    
    @staticmethod
    def VerifyGpayExists(gpay):
        df = pd.read_excel(xl_path, sheet_name='Classic',engine='openpyxl')
        if gpay in df["gpay"]:
            return False
        return True
    @staticmethod
    def Register(lt):
        lst = pd.Series(lt)

        df = pd.read_excel(xl_path, sheet_name='Classic',engine='openpyxl')
        added_slot = (df['slot'].count()+1)

        lst.iloc[0]=added_slot
        lst.iloc[-1]= Execute.Date()
        print("PLAYERS LIST ")
        print(lst)

        frame = {"slot":[lst[0]],"player1":[lst[1]],"player2":[lst[2]],"player3":[lst[3]],"player4":[lst[4]],"player5":[lst[5]],"gpay":[lst[6]],"regTime":[lst[7]]}
        x=pd.DataFrame(frame)
        update = pd.concat((df,x),)
        writer=pd.ExcelWriter(xl_path)
        update.to_excel(writer,sheet_name="Classic",index=False)
        writer.close()
        return 25-Execute.RemainingSlots()
    
    @staticmethod
    def ClassicRegistration():
        df = pd.read_excel(xl_path, sheet_name='Classic',engine='openpyxl')
        return df

    # @staticmethod
    # def ChangeMatchDetails(date,time,price):
    #     df = pd.read_excel(xl_path, sheet_name='MatchDetails',engine='openpyxl')
    #     df[''][0]=date
    #     df[''][0]=time
    #     df[''][0]=date



 