from tkinter import *
from tkinter import ttk #theme of tk
from tkinter import messagebox

#################csv######################

import csv

def writecsv(datalist):
     with open('data.csv','a',encoding='utf-8',newline='') as file:
         fw = csv.writeer(file) #fw = file writer
         fw.writerow(datalist) # datalist = ['Bakery','Material','Price']
 
def readcsv():
    with open('data.csv',encoding='utf-8',newline='') as file:
         fr = csv.reader(file) #fr = file reader
         data = list(fr)
    return data 

############################################


GUI = Tk() # นี่คือหน้าจอหลักโปรแกรม
GUI.title('โปรแกรมบันทึกข้อมูล') #นี่คือชื่อโปรแกรม
GUI.geometry('1200x400') #นี่คือขนาดโปรแกรม

L1 = Label(GUI,text='โปรแกรมบันทึกข้อมูลการสั่งซื้อ',font=('Angsana New',30),fg='blue')
L1.place(x=100,y=50)
######################

def Button2():
    text = 'รายการสั่งซื้อสินค้า 1 รายการ'
    messagebox.showinfo('รายการสั่งซื้้อสิินค้า 1 รายการ',text)

FB1 = Frame(GUI) #คล้ายกระดาน
FB1.place(x=180,y=90)
B2 = ttk.Button(FB1,text='บันทึกรายการสั่่งซื้อ',command=Button2)
B2.pack(ipadx=50,ipady=30)
###############

def Button3():
    text = 'รายการสินค้าที่ยกเลิก'
    massagebox.showinfo('รายการสินค้าที่ยกเลิก',text)

FB2 = Frame(GUI) #คล้ายกระดาน
FB2.place(x=180,y=90)
B3 = ttk.Button(FB1,text='ยกเลิกรายการสั่่งซื้อ',command=Button3)
B3.pack(ipadx=50,ipady=30)

###############

def Button4():
    text = 'รายการสินค้าที่แก้ไข'
    massagebox.showinfo('รายการสินค้าที่แก้ไข',text)

FB3 = Frame(GUI) #คล้ายกระดาน
FB3.place(x=180,y=90)
B4 = ttk.Button(FB1,text='แก้ไขรายการสั่่งซื้อ',command=Button4)
B4.pack(ipadx=50,ipady=30)

################Section Right#################################
LF1 = ttk.LabelFrame(GUI,text='กรุณากรอกข้อมูลรายการสินค้า')
LF1.place(x=500,y=250)

v_data = StringVar() #ตัวแปรพิเศษที่ใช้กับข้อความใน gui
E1 = ttk.Entry(LF1,textvariable=v_data,font=('Angsana New',25))
E1.pack(pady=10,padx=10)

from datetime import datetime

def SaveData():
    t = datetime.now().strftime('%Y%m%d %H%M%S')
    data = v_data.get() #ดึงข้อมูลจากตัวแปร v_data มาใช้งาน
    Text = [t,data] # [เวลา,ข้อมูลที่ได้จากการสั่งซื้อสินค้า]
    writecsv(Text) #บันทึกลง CSV
    v_data.set('') #ล้างข้อมูลที่อยู่ในรายการสั่งซื้อ

B5 = ttk.Button(LF1,text='บันทึกข้อมูลรายการสั่่งซื้อ',command=Button4)
B5.pack(ipadx=50,ipady=30)

GUI.mainloop()
