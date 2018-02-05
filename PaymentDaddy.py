from abc import ABCMeta, abstractmethod
class PaymentDaddy:
    __metaclass__ = ABCMeta
    @abstractmethod
    def GetResult(self,money):pass
class discountPayment(PaymentDaddy):

    def GetResult(self,money):
        discountrate=float(input("打几折？ "))
        return discountrate*money/10

class manjianPayment(PaymentDaddy):

    def GetResult(self,money):
        manduoshao=float(input("满多少？"))
        minus=float(input("减多少?"))
        if(money>=manduoshao):
          s=money-minus
          return s
        else:
          return money

class normalPayment(PaymentDaddy):
    def GetResult(self,money):
        return money

class PaymentContext:
    pd= PaymentDaddy
    def getFinalResult(self,money):
      Type=input("选择付款活动方案号：1.不参加活动 2.满减活动 3.折扣活动:")
      if(Type=="1"):
          p=normalPayment()
          s=p.GetResult(money)
          return s
      if (Type=="2"):
          es=manjianPayment()
          s=es.GetResult(money)
          return s
      if(Type=="3"):
          r=discountPayment()
          s=r.GetResult(money)
          return s

if __name__=='__main__':
   for i in range(3):
    s=PaymentContext()
    money=float(input("请输入总金额:￥"))
    t=s.getFinalResult(money)
    #q=normalPayment()
    print('现在应付款:￥%d元'%t)

