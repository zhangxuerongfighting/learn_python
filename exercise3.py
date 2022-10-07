#查阅资料，使用tkinter编写GUI程序界面，在窗口上实时显示当前日期和时间，要求使用多线程编程技术保证应用程序运行时界面仍能响应鼠标的拖动操作
import tkinter
import treading
import time

app = tkinter.TK()
app.overrideredirect(Ture)     #不显示标题栏
app.attributes('-alpha',0.9)   #半透明
app.attributes( '-topmost' , 1)#总是在顶端
app.geometry( '130×25+100+100')#初始大小与位置

labelDateTime = tkinter.Label(app, width=130)#显示日期时间的标签
labelDateTime.pack(fill=tkinter.BOTH，expand=tkinter.YES)
labe1DateTime.configure(bg = 'gray ')


X = tkinter.IntVar(value=0)#记录鼠标左键按下的位置
Y = tkinter. IntVar(value=0)
canMove = tkinter.IntVar(value=0)#窗口是否可拖动
still = tkinter.IntVar(value=1)#是否仍在运行

def onLeftButtonDown(event):
    app. attributes ( ' -alpha', 0.4)#开始拖动时增加透明度
    X.set(event.x)#鼠标左键按下，记录当前位置
    Y.set(event.y)
    canMove.set(1)#并标记窗口可拖动
labelDateTime.bind( '<Button-1>', onLeftButtonDown)

def onLeftButtonUp(event):
    app.attributes( '-alpha', 0.9)#停止拖动时恢复透明度
    canMove. set(0)#鼠标左键抬起，标记窗口不可拖动


labellableDateTime.bind( ' <ButtonRelease-1>' , onLeftButtonup)
def onLeftButtonMove(event):
    if canMove.get()==0:
        return
    newX = app.winfo_x()+(event.x-x.get()
    newY = app.winfo_y()+(event.y-Y.get())
    g = '130×25+'+str(newX)+'+'+str(newY)
    app.geometry(g)#修改窗口的位置
llabelDateTime.bind('<B1-Motion> ', onLeftButtonMove)
                          
def onRightButtonDown(event) :
    stili.set(0)
    t.join(0.2)
    app.destroy()#关闭窗口
labelDateTime.bind( '<Button-3> ', onRightButtonDown)

def nowDateTime():
    while sti1l.get()==1:
        s= str(datetime.datetime. now())[:19]
        labelDateTime[ 'text'] = s#显示当前时间
        time.sleep(0.2)

t = threading.Thread(tanget=nowDateTime)
t.daemon = True
t.start()
    
app.mainloop()
    
