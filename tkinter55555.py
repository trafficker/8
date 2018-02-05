import tkinter
from tkinter import*

def center_window(root,width,height):
    screenwidth=root.winfo_screenwidth()
    screenheight=root.winfo_screenheight()
    size='%dx%d+%d+%d'%(width,height,(screenwidth-width)/2,(screenheight-height)/2)
    print(size)
    root.geometry(size)
ytm=tkinter.Tk()#创建Tk对象  
ytm["bg"]='#87CEEB'
ytm.attributes("-alpha",0.90)
ytm.title("github文档推荐~~~~") #窗口标题  
ytm.geometry("300x300")

center_window(ytm,300,240)
ytm.minsize(300,240)
l1=tkinter.Label(ytm, text="请在下方输入github用户名",fg='purple',bg='#87CEEB',width=20,height=3)
l1.pack()
user_text=tkinter.Entry()
user_text.pack()

l2=tkinter.Label(ytm, text="请在下方输入github密码",fg='purple',bg='#87CEEB',width=20,height=3)
l2.pack()
user_text2=tkinter.Entry()#创建文本框  
user_text2.pack()
textshuchu=tkinter.Text(ytm,width=10,height=35)
textshuchu.pack(fill=tkinter.X,side=tkinter.BOTTOM )

def getuser():
    user=user_text.get()  #获取输入的用户名
    return user

def getpassword():
    password=user_text2.get()   #获取输入的密码  
    return password

def printout():  # 画板结果输出函数
  textshuchu.insert(tkinter.END,"您可能感兴趣的文档为:")#此处插入运行结果文本
  q=resultget(getuser(),getpassword())

  textshuchu.insert(tkinter.END,'\n') #### 画板上插入显示的推荐的文档的文本
  textshuchu.insert(tkinter.END, "oooooo")
def resultget(user,password):  #获得训练预测数据集
    result=" " ###待定

    #  此处预测函数！！
    return result

#定义触发按钮
tkinter.Button(ytm,text='查看您的推荐文档',command=printout).pack(side=BOTTOM)
#定义结果显示的文本画板
t1=tkinter.Text(width = 10,height = 1)
ytm.mainloop()#进入主循环  
