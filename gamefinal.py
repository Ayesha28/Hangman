
from tkinter import *
import tkinter
from PIL import ImageTk , Image
import os
import pygame
from functools import partial
my=tkinter.Tk()

# quit definetion

def qui():
    panel1.place(x=-6700,y=-5000)
    st.place(x=-100,y=-300)
    qu.place(x=-300,y=-300)
    panel6.place(x=0,y=0)
    labelexit.place(x=70,y=200)
    exitbutton1.place(x=200,y=300)
    exitbutton2.place(x=400,y=300)
    
def yes():
    my.destroy()
   
def no():
    panel6.place(x=-5000,y=-9000)
    panel1.place(x=0,y=0)
    exitbutton1.place(x=-700,y=-800)
    exitbutton2.place(x=-700,y=-800)
    labelexit.place(x=-700,y=-800)
    st.place(x=380,y=130)
    qu.place(x=600,y=130)
    
# start button calling instruction page
     
def instruction():
    panel1.place(x=-6700,y=-5000)
    panel2.place(x=0,y=0)
    st.place(x=-100,y=-300)
    qu.place(x=-300,y=-300)
    instruct.pack()
    instruct1.place(x=1,y=210)
    instruct2.place(x=1,y=270)
    instruct3.place(x=1,y=330)
    instruct4.place(x=20,y=361)
    instB.place(x=320,y=450)

# instruction page calling mode page
    
def modes():
    panel2.place(x=-5000,y=-6000)
    panel3.place(x=0,y=0)
    instruct.place(x=-300,y=-500)
    instruct1.place(x=-2000,y=-2100)
    instruct2.place(x=-1000,y=-2700)
    instruct3.place(x=-1000,y=-3300)
    instruct4.place(x=-203,y=-361)
    instB.place(x=-320,y=-450)
    label.pack()
    easy.place(x=270,y=300)
    mod.place(x=270,y=400)
    
# from mode page to easy levels

def easyness():
    easy.place(x=-270,y=-300)
    mod.place(x=-270,y=-400)
    panel3.place(x=-3000,y=-4000)
    label.place(x=-800,y=-800)
    panel4.place(x=0,y=0)
    label2=tkinter.Label(text="EASY MODE",fg="black",bg="snow",font=("Helvetica", 40 ,"bold italic"))
    label2.pack()
    q1a.place(x=150,y=200)
    q1b.place(x=240,y=200)
    q1c.place(x=330,y=200)
    q1d.place(x=420,y=200)
    q1e.place(x=510,y=200)
    e.place(x=280,y=350)
    submit.place(x=350,y=348)
    score.place(x=650,y=0)
    number1.place(x=720,y=0)
    
# from mode page to hard levels
    
def moderate():
    easy.place(x=-270,y=-300)
    mod.place(x=-270,y=-400)
    panel3.place(x=-3000,y=-4000)
    label.place(x=-800,y=-800)
    panel5.place(x=0,y=0)
    label3=tkinter.Label(text="HARD LEVEL",fg="black",bg="mediumaquamarine",font=("Helvetica", 40,"bold italic"))
    label3.pack()
    m1a.place(x=150,y=200)
    m1b.place(x=240,y=200)
    m1c.place(x=330,y=200)
    m1d.place(x=420,y=200)
    m1e.place(x=510,y=200)
    m1f.place(x=600,y=200)
    e1.place(x=280,y=350)
    login.place(x=350,y=348)
    m1hint.place(x=11,y=470)
    scor.place(x=650,y=0)
    num1.place(x=720,y=0)


#EASY MODE DEFINETIONS

def disappear5():
                global attempt5
                global s
                global total5
                e.place(x=280,y=350)
                
                next5.place(x=-200,y=-300)
                q5an.place(x=-100,y=-200)
                q5bn.place(x=-100,y=-200)
                q5cn.place(x=-100,y=-200)
                q5dn.place(x=-100,y=-200)
                q5en.place(x=-100,y=-200)
                q5a.place(x=-210,y=-200)
                q5b.place(x=-140,y=-200)
                q5c.place(x=-140,y=-200)
                q5d.place(x=-210,y=-200)
                q5e.place(x=-140,y=-200)
                
                e.place(x=-500,y=-500)
                submit5.place(x=-500,y=-500)
                win=Label(text="YOU WIN",fg="black",bg="LightBlue1",font=("Helvetica", 50))
                win.place(x=240,y=250)
                if attempt5 <= 5 and total5==attempt5:
                    s = s+10
                else:
                    s=s+0
                if s==50:
                        number5.place(x=-710,y=0)
                        number6.place(x=720,y=0)
                       
                if s==40:
                        number4.place(x=-460,y=0)
                        number5.place(x=720,y=0)
                if s==30:
                        number3.place(x=-460,y=0)
                        number4.place(x=720,y=0)
                if s==20:
                        number2.place(x=-460,y=0)
                        number3.place(x=720,y=0)
                if s==10:
                        number1.place(x=-460,y=0)
                        number2.place(x=720,y=0)
        
        
        
def update5(i):
        
                global stuck
                if stuck <= 4:
                    if i == 0:
                        q5a.place(x=-100,y=-200)
                        q5an.place(x=150,y=200)
                    if i == 1:
                        q5b.place(x=-140,y=-200)
                        q5bn.place(x=240,y=200)
                    if i == 2:
                        q5c.place(x=-210,y=-200)
                        q5cn.place(x=330,y=200)
                    if i == 3:
                        q5d.place(x=-260,y=-200)
                        q5dn.place(x=420,y=200)
                    if i == 4:
                        q5e.place(x=-310,y=-200)
                        q5en.place(x=510,y=200)
                if stuck==4:
                        e.place(x=-60,y=-300)
                        submit5.place(x=-350,y=-300)
                        next5.place(x=300,y=350)
                

def search5():
                global stuck
                global attempt5
                global total5
                global ra
                total5=total5+1
                ch = e.get()
                str="STUCK"
                
                for i in range(0,5):
                    if str[i] == ch  and str[i] !='U' and ra[i]==0:
                        stuck=stuck+1
                        ra[i]=1
                        attempt5 = attempt5+1
                        update5(i)


def disappear4():
                global attempt4
                global s
                global total4
                e.place(x=280,y=350)
               
                next4.place(x=-200,y=-300)
                q4an.place(x=-100,y=-200)
                q4bn.place(x=-100,y=-200)
                q4cn.place(x=-100,y=-200)
                q4dn.place(x=-100,y=-200)
                q4en.place(x=-100,y=-200)
                q4a.place(x=-100,y=-200)
                q4b.place(x=-140,y=-200)
                q4c.place(x=-210,y=-200)
                q4d.place(x=-260,y=-200)
                q4e.place(x=-310,y=-200)
                q5a.place(x=150,y=200)
                q5b.place(x=240,y=200)
                q5c.place(x=330,y=200)
                q5d.place(x=420,y=200)
                q5e.place(x=510,y=200)
                submit4.place(x=-450,y=-800)
                submit5.place(x=350,y=348)
                if attempt4 <= 5 and attempt4==total4:
                    s = s+10
                else:
                    s=s+0
                if s==40:
                       number4.place(x=-460,y=0)
                       number5.place(x=720,y=0)
                if s==30:
                        number3.place(x=-460,y=0)
                        number4.place(x=720,y=0)
                if s==20:
                        number2.place(x=-460,y=0)
                        number3.place(x=720,y=0)
                if s==10:
                        number1.place(x=-460,y=0)
                        number2.place(x=720,y=0)

def update4(i):
        
        global youth
        if youth <= 3:
            if i == 0:
                q4a.place(x=-100,y=-200)
                q4an.place(x=150,y=200)
            if i == 1:
                q4b.place(x=-140,y=-200)
                q4bn.place(x=240,y=200)
            if i == 2:
                q4c.place(x=-210,y=-200)
                q4cn.place(x=330,y=200)
            if i == 3:
                q4d.place(x=-260,y=-200)
                q4dn.place(x=420,y=200)
            if i == 4:
                q4e.place(x=-310,y=-200)
                q4en.place(x=510,y=200)
        if youth==3:
                e.place(x=-60,y=-300)
                submit4.place(x=-350,y=-300)
                next4.place(x=300,y=350)
            
def search4():
    
    global youth
    global attempt4
    global r
    global total4
    total4 = total4+1
    ch = e.get()
    str="YOUTH"
    for i in range(0,5):
        if str[i] == ch and str[i] !='O' and str[i] !='U' and r[i]==0 :
            youth=youth+1
            r[i]=1
            attempt4 = attempt4+1
            update4(i)            




def disappear3():
                global attempt3
                global s
                global total3
                e.place(x=280,y=350)
                
                next3.place(x=-200,y=-300)
                q3an.place(x=-100,y=-200)
                q3bn.place(x=-100,y=-200)
                q3cn.place(x=-100,y=-200)
                q3dn.place(x=-100,y=-200)
                q3en.place(x=-100,y=-200)
                q3a.place(x=-100,y=-200)
                q3b.place(x=-140,y=-200)
                q3c.place(x=-210,y=-200)
                q3d.place(x=-260,y=-200)
                q3e.place(x=-310,y=-200)
                q4a.place(x=150,y=200)
                q4b.place(x=240,y=200)
                q4c.place(x=330,y=200)
                q4d.place(x=420,y=200)
                q4e.place(x=510,y=200)
                submit3.place(x=-450,y=-800)
                submit4.place(x=350,y=348)
                if attempt3 <= 5 and attempt3==total3:
                    s = s+10
                else:
                    s=s+0
                if s==30:
                    number3.place(x=-460,y=0)
                    number4.place(x=720,y=0)
                if s==20:
                    number2.place(x=-460,y=0)
                    number3.place(x=720,y=0)
                if s==10:
                    number1.place(x=-460,y=0)
                    number2.place(x=720,y=0)

def update3(i):
        global vital
        if vital <= 3:
            if i == 0:
                q3a.place(x=-100,y=-200)
                q3an.place(x=150,y=200)
            if i == 1:
                q3b.place(x=-140,y=-200)
                q3bn.place(x=240,y=200)
            if i == 2:
                q3c.place(x=-210,y=-200)
                q3cn.place(x=330,y=200)
            if i == 3:
                q3d.place(x=-260,y=-200)
                q3dn.place(x=420,y=200)
            if i == 4:
                q3e.place(x=-310,y=-200)
                q3en.place(x=510,y=200)
        if vital==3:
                e.place(x=-60,y=-300)
                submit3.place(x=-350,y=-300)
                next3.place(x=300,y=350)
                
        

def search3():
    global vital
    global attempt3
    global total3
    global ar
    total3=total3+1
    ch = e.get()
    str="VITAL"
    
    for i in range(0,5):
        if str[i] == ch and str[i] !='I' and str[i] !='A' and ar[i]==0 :
            vital=vital+1
            ar[i]=1
            attempt3 = attempt3+1
            update3(i)


def disappear2():
                global attempt2
                global s
                global total2
                e.place(x=280,y=350)
                
                next2.place(x=-200,y=-300)
                q2an.place(x=-100,y=-200)
                q2bn.place(x=-100,y=-200)
                q2cn.place(x=-100,y=-200)
                q2dn.place(x=-100,y=-200)
                q2en.place(x=-100,y=-200)
                q2a.place(x=-100,y=-200)
                q2b.place(x=-140,y=-200)
                q2c.place(x=-210,y=-200)
                q2d.place(x=-260,y=-200)
                q2e.place(x=-310,y=-200)
                q3a.place(x=150,y=200)
                q3b.place(x=240,y=200)
                q3c.place(x=330,y=200)
                q3d.place(x=420,y=200)
                q3e.place(x=510,y=200)
                submit2.place(x=-450,y=-800)
                submit3.place(x=350,y=348)
                if attempt2 <= 5 and attempt2==total2:
                    s = s+10
                else:
                    s=s+0
                if s == 20:
                    number2.place(x=-460,y=0)
                    number3.place(x=720,y=0)
                if s == 10:
                    number1.place(x=-460,y=0)
                    number2.place(x=720,y=0)


def update2(i):
        global adopt
        if adopt <= 3:
            if i == 0:
                q2a.place(x=-100,y=-200)
                q2an.place(x=150,y=200)
            if i == 1:
                q2b.place(x=-140,y=-200)
                q2bn.place(x=240,y=200)
            if i == 2:
                q2c.place(x=-210,y=-200)
                q2cn.place(x=330,y=200)
            if i == 3:
                q2d.place(x=-260,y=-200)
                q2dn.place(x=420,y=200)
            if i == 4:
                q2e.place(x=-310,y=-200)
                q2en.place(x=510,y=200)
        if adopt==3:
                e.place(x=-60,y=-300)
                submit2.place(x=-350,y=-300)
                next2.place(x=300,y=350)
               
        

def search2():
    global adopt
    global attempt2
    global a
    global total2
    total2=total2+1
    ch = e.get()
    str="ADOPT"
    
    for i in range(0,5):
        if str[i] == ch and str[i] !='O' and a[i]==0:
            adopt=adopt+1
            a[i]=1
            attempt2 = attempt2+1
            update2(i)

def disappear1():
            global s
            global attempt1
            global total1
            q1an.place(x=-100,y=-200)
            q1bn.place(x=-100,y=-200)
            q1cn.place(x=-100,y=-200)
            q1dn.place(x=-100,y=-200)
            q1en.place(x=-100,y=-200)
            q1a.place(x=-100,y=-200)
            q1b.place(x=-140,y=-200)
            q1c.place(x=-210,y=-200)
            q1d.place(x=-260,y=-200)
            q1e.place(x=-310,y=-200)
            q2a.place(x=150,y=200)
            q2b.place(x=240,y=200)
            q2c.place(x=330,y=200)
            q2d.place(x=420,y=200)
            q2e.place(x=510,y=200)
            submit.place(x=-450,y=-800)
            submit2.place(x=350,y=348)
            e.place(x=280,y=350)
            
            next1.place(x=-200,y=-300)
            if attempt1 <=5 and total1 == attempt1:
                 s=s+10
                 number1.place(x=-460,y=0)
                 number2.place(x=720,y=0)
            else:
                 s=s+0
 
def update(i):
    
    global slurr
    if slurr <= 3:
            if i == 0:
                q1a.place(x=-100,y=-200)
                q1an.place(x=150,y=200)
            if i == 1:
                q1b.place(x=-140,y=-200)
                q1bn.place(x=240,y=200)
            if i == 2:
                q1c.place(x=-210,y=-200)
                q1cn.place(x=330,y=200)
            if i == 3:
                q1d.place(x=-260,y=-200)
                q1dn.place(x=420,y=200)
                q1e.place(x=-310,y=-200)
                q1en.place(x=510,y=200)
    if slurr==3:
            e.place(x=-60,y=-300)
            submit.place(x=-350,y=-300)
            next1.place(x=300,y=350)
            



     
def search():
    global slurr
    global attempt1
    global arr
    global total1
    total1=total1+1
    ch = e.get()
    str="SLURR"
    for i in range(0,5):
        if str[i] == ch and str[i] != 'U' and arr[i] == 0:
            slurr=slurr+1
            arr[i]=1
            attempt1 = attempt1+1
            update(i)




   
   

    
    
   
#Moderate level defenitions
def dis5():
            global sc
            global tt5
            global att5
            m5an.place(x=-100,y=-200)
            m5bn.place(x=-100,y=-200)
            m5cn.place(x=-100,y=-200)
            m5dn.place(x=-100,y=-200)
            m5en.place(x=-100,y=-200)
            m5fn.place(x=-100,y=-200)
            m5a.place(x=-210,y=-200)
            m5b.place(x=-210,y=-200)
            m5c.place(x=-140,y=-200)
            m5d.place(x=-140,y=-200)
            m5e.place(x=-210,y=-200)
            m5f.place(x=-210,y=-200)
            nex5.place(x=-200,y=-300)
            e1.place(x=-500,y=-500)
            login5.place(x=-500,y=-500)
            win=Label(text="YOU WIN",fg="black",bg="aquamarine",font=("Helvetica", 50))
            win.place(x=240,y=250)
            if att5<=8 and tt5==att5:
                sc=sc+10
            if sc==50:
                num5.place(x=-460,y=0)
                num6.place(x=720,y=0)
            if sc==40:
                num4.place(x=-460,y=0)
                num5.place(x=720,y=0)
            if sc==30:
                num3.place(x=-460,y=0)
                num4.place(x=720,y=0)
            if sc==20:
                num2.place(x=-460,y=0)
                num3.place(x=720,y=0)
            if sc==10:
                num1.place(x=-460,y=0)
                num2.place(x=720,y=0)
    
def change5(i):
        global cringe
        if cringe <= 4:
            if i == 0:
                m5a.place(x=-100,y=-200)
                m5an.place(x=150,y=200)
            if i == 1:
                m5b.place(x=-140,y=-200)
                m5bn.place(x=240,y=200)
            if i == 2:
                m5c.place(x=-210,y=-200)
                m5cn.place(x=330,y=200)
            if i == 3:
                m5d.place(x=-260,y=-200)
                m5dn.place(x=420,y=200)
            if i == 4:
                m5e.place(x=-310,y=-200)
                m5en.place(x=510,y=200)
            if i == 5:
                m5f.place(x=-360,y=-200)
                m5fn.place(x=600,y=200)
        if cringe==4:
            e1.place(x=-60,y=-300)
            login5.place(x=-350,y=-300)
            nex5.place(x=300,y=350)
            
            
        

def check5():
        global cringe
        global att5
        global tt5
        global m5
        tt5=tt5+1
        ch = e1.get()
        str="CRINGE"
        for i in range(0,6):
            if str[i] == ch  and str[i] !='E' and str[i] != 'I' and m5[i]==0:
                cringe=cringe+1
                att5=att5+1
                m5[i]=1
                change5(i)

def dis4():
            global att4
            global sc
            global tt4
            e1.place(x=280,y=350)
            
            nex4.place(x=-200,y=-300)
            m4an.place(x=-100,y=-200)
            m4bn.place(x=-100,y=-200)
            m4cn.place(x=-100,y=-200)
            m4dn.place(x=-100,y=-200)
            m4en.place(x=-100,y=-200)
            m4fn.place(x=-100,y=-200)
            m4hint.place(x=-789,y=-9876)
            m4a.place(x=-100,y=-200)
            m4b.place(x=-140,y=-200)
            m4c.place(x=-210,y=-200)
            m4d.place(x=-260,y=-200)
            m4e.place(x=-310,y=-200)
            m4f.place(x=-360,y=-200)
            m5a.place(x=150,y=200)
            m5b.place(x=240,y=200)
            m5c.place(x=330,y=200)
            m5d.place(x=420,y=200)
            m5e.place(x=510,y=200)
            m5f.place(x=600,y=200)
            m5hint.place(x=11,y=470)
            login4.place(x=-450,y=-800)
            login5.place(x=350,y=348)
            if att4<=8 and att4==tt4:
                sc=sc+10
            if sc==40:
                num4.place(x=-460,y=0)
                num5.place(x=720,y=0)
            if sc==30:
                num3.place(x=-460,y=0)
                num4.place(x=720,y=0)
            if sc==20:
                num2.place(x=-460,y=0)
                num3.place(x=720,y=0)
            if sc==10:
                num1.place(x=-460,y=0)
                num2.place(x=720,y=0)



def change4(i):
        global legacy
        if legacy <= 4:
            if i == 0:
                m4a.place(x=-100,y=-200)
                m4an.place(x=150,y=200)
            if i == 1:
                m4b.place(x=-140,y=-200)
                m4bn.place(x=240,y=200)
            if i == 2:
                m4c.place(x=-210,y=-200)
                m4cn.place(x=330,y=200)
            if i == 3:
                m4d.place(x=-260,y=-200)
                m4dn.place(x=420,y=200)
            if i == 4:
                m4e.place(x=-310,y=-200)
                m4en.place(x=510,y=200)
            if i == 5:
                m4f.place(x=-310,y=-200)
                m4fn.place(x=600,y=200)
        if legacy==4:
            e1.place(x=-60,y=-300)
            login4.place(x=-350,y=-300)
            nex4.place(x=300,y=350)
            
        

def check4():
            global legacy
            global att4
            global tt4
            global m4
            tt4=tt4+1
            ch = e1.get()
            str="LEGACY"
            for i in range(0,6):
                if str[i] == ch and str[i] !='E' and str[i] !='A' and m4[i]==0:
                    legacy=legacy+1
                    m4[i]=1
                    att4=att4+1
                    change4(i)

def dis3():
            global att3
            global sc
            global tt3
            e1.place(x=280,y=350)
            
            nex3.place(x=-200,y=-300)
            m3an.place(x=-100,y=-200)
            m3bn.place(x=-100,y=-200)
            m3cn.place(x=-100,y=-200)
            m3dn.place(x=-100,y=-200)
            m3en.place(x=-100,y=-200)
            m3fn.place(x=-100,y=-200)
            m3hint.place(x=-987,y=-678)
            m3a.place(x=-100,y=-200)
            m3b.place(x=-140,y=-200)
            m3c.place(x=-210,y=-200)
            m3d.place(x=-260,y=-200)
            m3e.place(x=-310,y=-200)
            m3f.place(x=-360,y=-200)
            m4a.place(x=150,y=200)
            m4b.place(x=240,y=200)
            m4c.place(x=330,y=200)
            m4d.place(x=420,y=200)
            m4e.place(x=510,y=200)
            m4f.place(x=600,y=200)
            m4hint.place(x=11,y=470)
            login3.place(x=-450,y=-800)
            login4.place(x=350,y=348)
            if att3<=8 and att3==tt3:
                sc=sc+10
            if sc==30:
                num3.place(x=-460,y=0)
                num4.place(x=720,y=0)
            if sc==20:
                num2.place(x=-460,y=0)
                num3.place(x=720,y=0)
            if sc==10:
                num1.place(x=-460,y=0)
                num2.place(x=720,y=0)



def change3(i):
        global squint
        if squint<= 4:
            if i == 0:
                m3a.place(x=-100,y=-200)
                m3an.place(x=150,y=200)
            if i == 1:
                m3b.place(x=-140,y=-200)
                m3bn.place(x=240,y=200)
            if i==2:
                m3c.place(x=-210,y=-200)
                m3cn.place(x=330,y=200)
            if i == 3:
                m3d.place(x=-210,y=-200)
                m3dn.place(x=420,y=200)
            if i == 4:
                m3e.place(x=-260,y=-200)
                m3en.place(x=510,y=200)
            if i == 5:
                m3f.place(x=-310,y=-200)
                m3fn.place(x=600,y=200)
        if squint==4:
            e1.place(x=-60,y=-300)
            login3.place(x=-350,y=-300)
            nex3.place(x=300,y=350)
            
        

def check3():
    global squint
    global att3
    global tt3
    global m3
    tt3=tt3+1
    ch = e1.get()
    str="SQUINT"
    for i in range(0,6):
        if str[i] == ch and str[i] !='I' and str[i] !='U' and m3[i]==0:
            squint=squint+1
            m3[i]=1
            att3=att3+1
            change3(i)
def dis2():
            global sc
            global att2
            global tt2
            e1.place(x=280,y=350)
            
            nex2.place(x=-200,y=-300)
            m2an.place(x=-100,y=-200)
            m2bn.place(x=-100,y=-200)
            m2cn.place(x=-100,y=-200)
            m2dn.place(x=-100,y=-200)
            m2en.place(x=-100,y=-200)
            m2fn.place(x=-100,y=-200)
            m2hint.place(x=-567,y=-987)
            m2a.place(x=-100,y=-200)
            m2b.place(x=-140,y=-200)
            m2c.place(x=-210,y=-200)
            m2d.place(x=-260,y=-200)
            m2e.place(x=-310,y=-200)
            m2f.place(x=-360,y=-200)
            m3a.place(x=150,y=200)
            m3b.place(x=240,y=200)
            m3c.place(x=330,y=200)
            m3d.place(x=420,y=200)
            m3e.place(x=510,y=200)
            m3f.place(x=600,y=200)
            m3hint.place(x=11,y=470)
            
            login2.place(x=-450,y=-800)
            login3.place(x=350,y=348)
            if att2<=8 and att2==tt2:
                sc=sc+10
            else:
                sc=sc+0
            if sc==20:
                num2.place(x=-460,y=0)
                num3.place(x=720,y=0)
            if sc==10:
                num1.place(x=-460,y=0)
                num2.place(x=720,y=0)

def change2(i):
        global att2
        global sc
        global tt2
        global trudge
        if trudge <= 4:
            if i == 0:
                m2a.place(x=-100,y=-200)
                m2an.place(x=150,y=200)
            if i == 1:
                m2b.place(x=-140,y=-200)
                m2bn.place(x=240,y=200)
            if i == 2:
                m2c.place(x=-210,y=-200)
                m2cn.place(x=330,y=200)
              
            if i == 3:
                m2d.place(x=-260,y=-200)
                m2dn.place(x=420,y=200)
            if i == 4:
                m2e.place(x=-310,y=-200)
                m2en.place(x=510,y=200)
            if i==5:
                m2f.place(x=-600,y=-200)
                m2fn.place(x=600,y=200)
                
        if trudge==4:
            e1.place(x=-60,y=-300)
            login2.place(x=-350,y=-300)
            nex2.place(x=300,y=350)
            
        

def check2():
    global trudge
    global att2
    global tt2
    global m2
    tt2=tt2+1
    ch = e1.get()
    str="TRUDGE"
    for i in range(0,6):
        if str[i] == ch and str[i] !='U' and str[i] !='E' and m2[i]==0:
            trudge=trudge+1
            m2[i]=1
            att2=att2+1
            change2(i)
def dis1():
           global sc
           global att1
           global tt1
           m1an.place(x=-100,y=-200)
           nex1.place(x=-200,y=-300)
           m1bn.place(x=-100,y=-200)
           m1cn.place(x=-100,y=-200)
           m1dn.place(x=-100,y=-200)
           m1en.place(x=-100,y=-200)
           m1fn.place(x=-100,y=-200)
           m1hint.place(x=-6789,y=-9876)
           m1a.place(x=-100,y=-200)
           m1b.place(x=-140,y=-200)
           m1c.place(x=-210,y=-200)
           m1d.place(x=-260,y=-200)
           m1e.place(x=-310,y=-200)
           m1f.place(x=-360,y=-200)
           m2a.place(x=150,y=200)
           m2b.place(x=240,y=200)
           m2c.place(x=330,y=200)
           m2d.place(x=420,y=200)
           m2e.place(x=510,y=200)
           m2f.place(x=600,y=200)
           e1.place(x=280,y=350)
           login2.place(x=350,y=348)
           m2hint.place(x=11,y=470)
           if att1<=8 and tt1==att1:
               sc=sc+10
               num1.place(x=-460,y=0)
               num2.place(x=720,y=0)
           else:
               sc=sc+0
    
 
def change(i):
    global sc
    global att1
    global tt1
    global martyr
    if martyr <=3:
            if i == 0:
                m1a.place(x=-100,y=-200)
                m1an.place(x=150,y=200)
            if i == 1:
                m1b.place(x=-140,y=-200)
                m1bn.place(x=240,y=200)
            if i == 2:
                m1c.place(x=-210,y=-200)
                m1cn.place(x=330,y=200)
                m1f.place(x=-360,y=-200)
                m1fn.place(x=600,y=200)
             
            if i == 3:
                m1d.place(x=-260,y=-200)
                m1dn.place(x=420,y=200)
                
            if i ==4:
                m1e.place(x=-310,y=-200)
                m1en.place(x=510,y=200)
           
    if martyr==3:
           e1.place(x=-60,y=-300)
           login.place(x=-350,y=-300)
           nex1.place(x=300,y=350)
           


     
def check():
    global martyr
    global att1
    global tt1
    global m1
    tt1=tt1+1
    ch = e1.get()
    str="MARTYR"
    for i in range(0,6):
        if str[i] == ch and str[i] !='A' and m1[i]==0:
            martyr=martyr+1
            att1=att1+1
            m1[i]=1
            change(i)
     
































#Window declaration and size

my.title("new window")
my.geometry("750x650")
my.resizable(0,0)

# image for main page

path1="F:\\hangmanfinal\mainpage.jpg"
mainpage = ImageTk.PhotoImage(Image.open(path1))
panel1 = Label(my,image=mainpage)
panel1.place(x=0,y=0)

# image for instruction page

path2="F:\\hangmanfinal\instruct.jpg"
inst = ImageTk.PhotoImage(Image.open(path2))
panel2 = Label(my,image=inst)

# image for mode page

path3="F:\\hangmanfinal\modes.jpg"
mode = ImageTk.PhotoImage(Image.open(path3))
panel3 = Label(my,image=mode)

# image for easy page

path4="F:\\hangmanfinal\easy.jpg"
soft = ImageTk.PhotoImage(Image.open(path4))
panel4 = Label(my,image=soft)

# image for easy page

path5="F:\\hangmanfinal\hard.jpg"
hard = ImageTk.PhotoImage(Image.open(path5))
panel5 = Label(my,image=hard)

# image for QUIT page

path6="F:\\hangmanfinal\quit.jpg"
q = ImageTk.PhotoImage(Image.open(path6))
panel6 = Label(my,image=q)

#path2="C:\\Users\Aditi khandelwal\Desktop\hangman\hang\images\yel.jpg"
#img2 = ImageTk.PhotoImage(Image.open(path2))
#panel2 = Label(my,image=img2)
#my.configure(background="yellow")

# label hangman for mode page

label=Button(my,text="HANGMAN",fg="black",width="10",height=1,bg="SlateGray3",font=("Helvetica", 60,"bold italic"))

#start quit button

st=Button(my,text="start",bg="black",fg="white",height=1,width=5,font=("Helvetica", 22,"bold italic"),command=instruction)
st.place(x=380,y=130)
qu=Button(text="quit",bg="black",fg="white",height=1,width=5,font=("Helvetica", 22,"bold italic"),command=qui)
qu.place(x=600,y=130)

#instruction page 

instruct=Label(text="INSTRUCTIONS",fg="white",bg="black",font=("Helvetica", 60,"bold italic"))
instruct1=Label(text="1. You have to fill the blanks with CONSONANTS only.",fg="white",bg="black",font=("Helvetica", 16,"bold"))
instruct2=Label(text="2. You will be given 5 attempts for easy level and 8 attempts for hard level.",fg="white",bg="black",font=("Helvetica", 16,"bold"))
instruct3=Label(text="3. If you completed the challenge within the given attempts then you will",fg="white",bg="black",font=("Helvetica", 16,"bold"))
instruct4=Label(text="be awarded 10 points otherwise 5 points.",fg="white",bg="black",font=("Helvetica", 16,"bold"))
instB=Button(text="next",bg="white",fg="black",height=1,width=5,font=("Helvetica", 20,"bold italic"),command=modes)

# easy moderate difficult button

easy=Button(my,text="EASY",bg="SlateGray3",fg="black",height=1,width=10,font=("Helvetica", 20,"bold"),command=easyness)
mod=Button(my,text="HARD",bg="SlateGray3",fg="black",height=1,width=10,font=("Helvetica", 20,"bold"),command=moderate)

#next button for easy levels

next1=Button(my,text="next",bg="black",fg="white",height=1,width=10,font=("Helvetica", 20),command=disappear1)
next2=Button(my,text="next",bg="black",fg="white",height=1,width=10,font=("Helvetica", 20),command=disappear2)
next3=Button(my,text="next",bg="black",fg="white",height=1,width=10,font=("Helvetica", 20),command=disappear3)
next4=Button(my,text="next",bg="black",fg="white",height=1,width=10,font=("Helvetica", 20),command=disappear4)
next5=Button(my,text="next",bg="black",fg="white",height=1,width=10,font=("Helvetica", 20),command=disappear5)

# next buttons for hard levels

nex1=Button(my,text="next",bg="black",fg="white",height=1,width=10,font=("Helvetica", 20),command=dis1)
nex2=Button(my,text="next",bg="black",fg="white",height=1,width=10,font=("Helvetica", 20),command=dis2)
nex3=Button(my,text="next",bg="black",fg="white",height=1,width=10,font=("Helvetica", 20),command=dis3)
nex4=Button(my,text="next",bg="black",fg="white",height=1,width=10,font=("Helvetica", 20),command=dis4)
nex5=Button(my,text="next",bg="black",fg="white",height=1,width=10,font=("Helvetica", 20),command=dis5)

#SCORE LABEL for easy levels

s=0
score=Label(text="SCORE:",fg="black",width=8,bg="azure",font=("Helvetica", 13, "bold"))
number1=Label(text="0",fg="black",width=2,bg="azure",font=("Helvetica", 13, "bold"))
number2=Label(text="10",fg="black",width=2,bg="azure",font=("Helvetica", 13, "bold"))
number3=Label(text="20",fg="black",width=2,bg="azure",font=("Helvetica", 13, "bold"))
number4=Label(text="30",fg="black",width=2,bg="azure",font=("Helvetica", 13, "bold"))
number5=Label(text="40",fg="black",width=2,bg="azure",font=("Helvetica", 13, "bold"))
number6=Label(text="50",fg="black",width=2,bg="azure",font=("Helvetica", 13, "bold"))

#variables for easy level

slurr=0
adopt=0
youth=0
stuck=0
vital=0
attempt1=0
attempt2=0
attempt3=0
attempt4=0
attempt5=0
total1=0
total2=0
total3=0
total4=0
total5=0
arr=[0,0,1,0,0]
a=[1,0,1,0,0]
ar=[0,1,0,1,0]
r=[0,1,1,0,0]
ra=[0,0,1,0,0]

# variables for hard level

martyr=0
trudge=0
legacy=0
squint=0
cringe=0
tt1=0
tt2=0
tt3=0
tt4=0
tt5=0
att1=0
att2=0
att3=0
att4=0
att5=0
m1=[0,1,0,0,0,0]
m2=[0,0,1,0,0,1]
m3=[0,0,1,1,0,0]
m4=[0,1,0,1,0,0]
m5=[0,0,1,0,0,1]

#SCORE LABEL FOR HARD LEVEL

sc=0
scor=Label(text="SCORE:",fg="black",width=8,bg="mediumaquamarine",font=("Helvetica", 13, "bold"))
num1=Label(text="0",fg="black",width=2,bg="mediumaquamarine",font=("Helvetica", 13, "bold"))
num2=Label(text="10",fg="black",width=2,bg="mediumaquamarine",font=("Helvetica", 13, "bold"))
num3=Label(text="20",fg="black",width=2,bg="mediumaquamarine",font=("Helvetica", 13, "bold"))
num4=Label(text="30",fg="black",width=2,bg="mediumaquamarine",font=("Helvetica", 13, "bold"))
num5=Label(text="40",fg="black",width=2,bg="mediumaquamarine",font=("Helvetica", 13, "bold"))
num6=Label(text="50",fg="black",width=2,bg="mediumaquamarine",font=("Helvetica", 13, "bold"))

# labels for easy level ques 1

q1a=Label(text="_",fg="black",height=1,width=2,bg="LightBlue1",font=("Helvetica", 50))
q1b=Label(text="_",fg="black",bg="LightBlue1",height=1,width=2,font=("Helvetica", 50))
q1c=Label(text="U",fg="black",bg="LightBlue1",height=1,width=2,font=("Helvetica", 50,"underline"))
q1d=Label(text="_",fg="black",bg="LightBlue1",height=1,width=2,font=("Helvetica", 50))
q1e=Label(text="_",fg="black",bg="LightBlue1",height=1,width=2,font=("Helvetica", 50))

# labels with text of ques 1

q1an=Label(text="S",fg="black",height=1,width=2,bg="LightBlue1",font=("Helvetica", 50,"underline"))
q1bn=Label(text="L",fg="black",height=1,width=2,bg="LightBlue1",font=("Helvetica", 50,"underline"))
q1cn=Label(text="U",fg="black",height=1,width=2,bg="LightBlue1",font=("Helvetica", 50,"underline"))
q1dn=Label(text="R",fg="black",height=1,width=2,bg="LightBlue1",font=("Helvetica", 50,"underline"))
q1en=Label(text="R",fg="black",height=1,width=2,bg="LightBlue1",font=("Helvetica", 50,"underline"))

#labels for easy level ques 2

q2a=Label(text="A",fg="black",bg="LightBlue1",height=1,width=2,font=("Helvetica", 50,"underline"))
q2b=Label(text="_",fg="black",bg="LightBlue1",height=1,width=2,font=("Helvetica", 50))
q2c=Label(text="O",fg="black",bg="LightBlue1",height=1,width=2,font=("Helvetica", 50,"underline"))
q2d=Label(text="_",fg="black",bg="LightBlue1",height=1,width=2,font=("Helvetica", 50))
q2e=Label(text="_",fg="black",bg="LightBlue1",height=1,width=2,font=("Helvetica", 50))

# labels with text of ques 2

q2an=Label(text="A",fg="black",height=1,width=2,bg="lightBlue1",font=("Helvetica", 50,"underline"))
q2bn=Label(text="D",fg="black",height=1,width=2,bg="LightBlue1",font=("Helvetica", 50,"underline"))
q2cn=Label(text="O",fg="black",height=1,width=2,bg="LightBlue1",font=("Helvetica", 50,"underline"))
q2dn=Label(text="P",fg="black",height=1,width=2,bg="LightBlue1",font=("Helvetica", 50,"underline"))
q2en=Label(text="T",fg="black",height=1,width=2,bg="LightBlue1",font=("Helvetica", 50,"underline"))

# label for easy level ques 3

q3a=Label(text="_",fg="black",bg="LightBlue1",height=1,width=2,font=("Helvetica", 50))
q3b=Label(text="I",fg="black",bg="LightBlue1",height=1,width=2,font=("Helvetica", 50,"underline"))
q3c=Label(text="_",fg="black",bg="LightBlue1",height=1,width=2,font=("Helvetica", 50))
q3d=Label(text="A",fg="black",bg="LightBlue1",height=1,width=2,font=("Helvetica", 50,"underline"))
q3e=Label(text="_",fg="black",bg="LightBlue1",height=1,width=2,font=("Helvetica", 50))

# labels with text of ques 3

q3an=Label(text="V",fg="black",height=1,width=2,bg="LightBlue1",font=("Helvetica", 50,"underline"))
q3bn=Label(text="I",fg="black",height=1,width=2,bg="LightBlue1",font=("Helvetica", 50,"underline"))
q3cn=Label(text="T",fg="black",height=1,width=2,bg="LightBlue1",font=("Helvetica", 50,"underline"))
q3dn=Label(text="A",fg="black",height=1,width=2,bg="LightBlue1",font=("Helvetica", 50,"underline"))
q3en=Label(text="L",fg="black",height=1,width=2,bg="LightBlue1",font=("Helvetica", 50,"underline"))

# label for easy level ques 4

q4a=Label(text="_",fg="black",bg="LightBlue1",height=1,width=2,font=("Helvetica", 50))
q4b=Label(text="O",fg="black",bg="LightBlue1",height=1,width=2,font=("Helvetica", 50,"underline"))
q4c=Label(text="U",fg="black",bg="LightBlue1",height=1,width=2,font=("Helvetica", 50,"underline"))
q4d=Label(text="_",fg="black",bg="LightBlue1",height=1,width=2,font=("Helvetica", 50))
q4e=Label(text="_",fg="black",bg="LightBlue1",height=1,width=2,font=("Helvetica", 50))

# labels with text of ques 4

q4an=Label(text="Y",fg="black",height=1,width=2,bg="LightBlue1",font=("Helvetica", 50,"underline"))
q4bn=Label(text="O",fg="black",height=1,width=2,bg="LightBlue1",font=("Helvetica", 50,"underline"))
q4cn=Label(text="U",fg="black",height=1,width=2,bg="LightBlue1",font=("Helvetica", 50,"underline"))
q4dn=Label(text="T",fg="black",height=1,width=2,bg="LightBlue1",font=("Helvetica", 50,"underline"))
q4en=Label(text="H",fg="black",height=1,width=2,bg="LightBlue1",font=("Helvetica", 50,"underline"))


# label for easy level ques 5

q5a=Label(text="_",fg="black",bg="LightBlue1",height=1,width=2,font=("Helvetica", 50))
q5b=Label(text="_",fg="black",bg="LightBlue1",height=1,width=2,font=("Helvetica", 50))
q5c=Label(text="U",fg="black",bg="LightBlue1",height=1,width=2,font=("Helvetica", 50,"underline"))
q5d=Label(text="_",fg="black",bg="LightBlue1",height=1,width=2,font=("Helvetica", 50))
q5e=Label(text="_",fg="black",bg="LightBlue1",height=1,width=2,font=("Helvetica", 50))

# labels with text of ques 5

q5an=Label(text="S",fg="black",height=1,width=2,bg="LightBlue1",font=("Helvetica", 50,"underline"))
q5bn=Label(text="T",fg="black",height=1,width=2,bg="LightBlue1",font=("Helvetica", 50,"underline"))
q5cn=Label(text="U",fg="black",height=1,width=2,bg="LightBlue1",font=("Helvetica", 50,"underline"))
q5dn=Label(text="C",fg="black",height=1,width=2,bg="LightBlue1",font=("Helvetica", 50,"underline"))
q5en=Label(text="K",fg="black",height=1,width=2,bg="LightBlue1",font=("Helvetica", 50,"underline"))

#MODERATE LEVEL

# labels for moderate level ques 1

m1a=Label(text="_",fg="black",height=1,width=2,bg="aquamarine",font=("Helvetica", 50))
m1b=Label(text="A",fg="black",bg="aquamarine",height=1,width=2,font=("Helvetica", 50,"underline"))
m1c=Label(text="_",fg="black",bg="aquamarine",height=1,width=2,font=("Helvetica", 50))
m1d=Label(text="_",fg="black",bg="aquamarine",height=1,width=2,font=("Helvetica", 50))
m1e=Label(text="_",fg="black",bg="aquamarine",height=1,width=2,font=("Helvetica", 50))
m1f=Label(text="_",fg="black",bg="aquamarine",height=1,width=2,font=("Helvetica", 50))
m1hint=Label(text="HINT : a person who is killed because of their religious or other beliefs.",fg="black",bg="light sea green",height=1,width=56,font=("Helvetica", 16,"bold italic"))
# labels with text of ques 1

m1an=Label(text="M",fg="black",height=1,width=2,bg="aquamarine",font=("Helvetica", 50,"underline"))
m1bn=Label(text="A",fg="black",height=1,width=2,bg="aquamarine",font=("Helvetica", 50,"underline"))
m1cn=Label(text="R",fg="black",height=1,width=2,bg="aquamarine",font=("Helvetica", 50,"underline"))
m1dn=Label(text="T",fg="black",height=1,width=2,bg="aquamarine",font=("Helvetica", 50,"underline"))
m1en=Label(text="Y",fg="black",height=1,width=2,bg="aquamarine",font=("Helvetica", 50,"underline"))
m1fn=Label(text="R",fg="black",height=1,width=2,bg="aquamarine",font=("Helvetica", 50,"underline"))

#labels for easy level ques 2

m2a=Label(text="_",fg="black",bg="aquamarine",height=1,width=2,font=("Helvetica", 50))
m2b=Label(text="_",fg="black",bg="aquamarine",height=1,width=2,font=("Helvetica", 50))
m2c=Label(text="U",fg="black",bg="aquamarine",height=1,width=2,font=("Helvetica", 50,"underline"))
m2d=Label(text="_",fg="black",bg="aquamarine",height=1,width=2,font=("Helvetica", 50))
m2e=Label(text="_",fg="black",bg="aquamarine",height=1,width=2,font=("Helvetica", 50))
m2f=Label(text="E",fg="black",bg="aquamarine",height=1,width=2,font=("Helvetica", 50,"underline"))
m2hint=Label(text="HINT : walk slowly and with heavy steps,typically because of exhaustion.",fg="black",bg="light sea green",height=1,width=56,font=("Helvetica", 16,"bold italic"))
# labels with text of ques 2

m2an=Label(text="T",fg="black",height=1,width=2,bg="aquamarine",font=("Helvetica", 50,"underline"))
m2bn=Label(text="R",fg="black",height=1,width=2,bg="aquamarine",font=("Helvetica", 50,"underline"))
m2cn=Label(text="U",fg="black",height=1,width=2,bg="aquamarine",font=("Helvetica", 50,"underline"))
m2dn=Label(text="D",fg="black",height=1,width=2,bg="aquamarine",font=("Helvetica", 50,"underline"))
m2en=Label(text="G",fg="black",height=1,width=2,bg="aquamarine",font=("Helvetica", 50,"underline"))
m2fn=Label(text="E",fg="black",height=1,width=2,bg="aquamarine",font=("Helvetica", 50,"underline"))

# label for easy level ques 3

m3a=Label(text="_",fg="black",bg="aquamarine",height=1,width=2,font=("Helvetica", 50))
m3b=Label(text="_",fg="black",bg="aquamarine",height=1,width=2,font=("Helvetica", 50))
m3c=Label(text="U",fg="black",bg="aquamarine",height=1,width=2,font=("Helvetica", 50,"underline"))
m3d=Label(text="I",fg="black",bg="aquamarine",height=1,width=2,font=("Helvetica", 50,"underline"))
m3e=Label(text="_",fg="black",bg="aquamarine",height=1,width=2,font=("Helvetica", 50))
m3f=Label(text="_",fg="black",bg="aquamarine",height=1,width=2,font=("Helvetica", 50))
m3hint=Label(text="HINT : have eyes that look in different directions.",fg="black",bg="light sea green",height=1,width=56,font=("Helvetica", 16,"bold italic"))
# labels with text of ques 3

m3an=Label(text="S",fg="black",height=1,width=2,bg="aquamarine",font=("Helvetica", 50))
m3bn=Label(text="Q",fg="black",height=1,width=2,bg="aquamarine",font=("Helvetica", 50))
m3cn=Label(text="U",fg="black",height=1,width=2,bg="aquamarine",font=("Helvetica", 50))
m3dn=Label(text="I",fg="black",height=1,width=2,bg="aquamarine",font=("Helvetica", 50))
m3en=Label(text="N",fg="black",height=1,width=2,bg="aquamarine",font=("Helvetica", 50))
m3fn=Label(text="T",fg="black",height=1,width=2,bg="aquamarine",font=("Helvetica", 50))

# label for easy level ques 4

m4a=Label(text="_",fg="black",bg="aquamarine",height=1,width=2,font=("Helvetica", 50))
m4b=Label(text="E",fg="black",bg="aquamarine",height=1,width=2,font=("Helvetica", 50))
m4c=Label(text="_",fg="black",bg="aquamarine",height=1,width=2,font=("Helvetica", 50))
m4d=Label(text="A",fg="black",bg="aquamarine",height=1,width=2,font=("Helvetica", 50))
m4e=Label(text="_",fg="black",bg="aquamarine",height=1,width=2,font=("Helvetica", 50))
m4f=Label(text="_",fg="black",bg="aquamarine",height=1,width=2,font=("Helvetica", 50))
m4hint=Label(text="HINT : a amount of money or property left to someone in a will",fg="black",bg="light sea green",height=1,width=56,font=("Helvetica", 16,"bold italic"))
# labels with text of ques 4

m4an=Label(text="L",fg="black",height=1,width=2,bg="aquamarine",font=("Helvetica", 50))
m4bn=Label(text="E",fg="black",height=1,width=2,bg="aquamarine",font=("Helvetica", 50))
m4cn=Label(text="G",fg="black",height=1,width=2,bg="aquamarine",font=("Helvetica", 50))
m4dn=Label(text="A",fg="black",height=1,width=2,bg="aquamarine",font=("Helvetica", 50))
m4en=Label(text="C",fg="black",height=1,width=2,bg="aquamarine",font=("Helvetica", 50))
m4fn=Label(text="Y",fg="black",height=1,width=2,bg="aquamarine",font=("Helvetica", 50))


# label for easy level ques 5

m5a=Label(text="_",fg="black",bg="aquamarine",height=1,width=2,font=("Helvetica", 50))
m5b=Label(text="_",fg="black",bg="aquamarine",height=1,width=2,font=("Helvetica", 50))
m5c=Label(text="I",fg="black",bg="aquamarine",height=1,width=2,font=("Helvetica", 50,"underline"))
m5d=Label(text="_",fg="black",bg="aquamarine",height=1,width=2,font=("Helvetica", 50))
m5e=Label(text="_",fg="black",bg="aquamarine",height=1,width=2,font=("Helvetica", 50))
m5f=Label(text="E",fg="black",bg="aquamarine",height=1,width=2,font=("Helvetica", 50,"underline"))

# labels with text of ques 5

m5an=Label(text="C",fg="black",height=1,width=2,bg="aquamarine",font=("Helvetica", 50,"underline"))
m5bn=Label(text="R",fg="black",height=1,width=2,bg="aquamarine",font=("Helvetica", 50,"underline"))
m5cn=Label(text="I",fg="black",height=1,width=2,bg="aquamarine",font=("Helvetica", 50,"underline"))
m5dn=Label(text="N",fg="black",height=1,width=2,bg="aquamarine",font=("Helvetica", 50,"underline"))
m5en=Label(text="G",fg="black",height=1,width=2,bg="aquamarine",font=("Helvetica", 50,"underline"))
m5fn=Label(text="E",fg="black",height=1,width=2,bg="aquamarine",font=("Helvetica", 50,"underline"))
m5hint=Label(text="HINT :bend one's head or body in fear.",fg="black",bg="light sea green",height=1,width=56,font=("Helvetica", 16,"bold italic"))



# text input and submit
e = Entry(my,width=6,font=("Calibri",15,"bold"),justify="center",bg="LightSkyBlue1")
e1 = Entry(my,width=6,font=("Calibri",13,"bold"),justify="center",bg="light sea green")

submit=Button(my,text="SUBMIT",bg="LightSkyBlue1",fg="black",height=1,width=8,font=("Helvetica", 13,"bold"),command=search)
submit.place(x=-500,y=-400)
#submit button for ques 2
submit2=Button(my,text="SUBMIT",bg="LightSkyBlue1",fg="black",height=1,width=8,font=("Helvetica",13,"bold"),command=search2)
#submit button for ques 3
submit3=Button(my,text="SUBMIT",bg="LightSkyBlue1",fg="black",height=1,width=8,font=("Helvetica", 13,"bold"),command=search3)
#submit button for ques 4
submit4=Button(my,text="SUBMIT",bg="LightSkyBlue1",fg="black",height=1,width=8,font=("Helvetica", 13,"bold"),command=search4)
#submit button for ques 5
submit5=Button(my,text="SUBMIT",bg="LightSkyBlue1",fg="black",height=1,width=8,font=("Helvetica", 13,"bold"),command=search5)

#submit buttons for hard level

login=Button(my,text="SUBMIT",bg="light sea green",fg="white",height=1,width=8,font=("Helvetica", 13,"bold"),command=check)
login.place(x=-500,y=-400)
#submit button for ques 2
login2=Button(my,text="SUBMIT",bg="light sea green",fg="white",height=1,width=8,font=("Helvetica", 13,"bold"),command=check2)
#submit button for ques 3
login3=Button(my,text="SUBMIT",bg="light sea green",fg="white",height=1,width=8,font=("Helvetica", 13,"bold"),command=check3)
#submit button for ques 4
login4=Button(my,text="SUBMIT",bg="light sea green",fg="white",height=1,width=8,font=("Helvetica", 13,"bold"),command=check4)
#submit button for ques 5
login5=Button(my,text="SUBMIT",bg="light sea green",fg="white",height=1,width=8,font=("Helvetica", 13,"bold"),command=check5)

# label for exit 

labelexit=Label(text="Do You Really Want To Quit?",fg="black",height=1,width=25,bg="aquamarine4",font=("Helvetica", 30))
exitbutton1=Button(my,text="YES",bg="white",fg="black",height=1,width=5,font=("Helvetica", 20,"bold"),command=yes)

exitbutton2=Button(my,text="NO",bg="white",fg="black",height=1,width=5,font=("Helvetica", 20,"bold"),command=no)


my.mainloop()
  - by ayesha



