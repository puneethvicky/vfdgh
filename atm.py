class Atm(object):
     """ blueprint for Atm
     """ 
     def __init__(self,CashWithdrawl, BalanceEnquiry ):
       self.CashWithdrawl = CashWithdrawl
       self.BalanceEnquiry = BalanceEnquiry
      
     def start(self): 
       print("started") 
     def stop(self): 
       print("stopped") 
     def accelarate(self): 
       print("accelarating...") 
       "accelarator functionality here" 
     def change_gear(self, gear_type): 
       print("gear changed") 
       " gear related functionality here" 
                 
ATM = payment(card, pin) 
print(atm.CashWithdrawl)








