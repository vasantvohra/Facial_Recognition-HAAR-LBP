import pickle
import sys
import os
import time
import datetime
now=datetime.datetime.now()
time=now.strftime("%H:%M:%S")

dn=now.strftime('%H')
dn1=int(dn)
class attendance1:
    def __init__(self):
        self.__emp_id=0
        self.__emp_time=""
    def get_detail(self,id2=0,time=0):
        self.__emp_id=id2
        self.__emp_time=time
    def display(self):
        print("Employee no",self.__emp_id)
        print("Time",self.__emp_time)
    def empno(self):
        return self.__emp_id
def add_record(ob):
    a=attendance1()
    f=0
    try:
        fin=open("attendance1.log","rb")
        while True:
            t=pickle.load(fin)
            #if dn1<16:
            if a.empno()==ob.empno():
                print("Employee no. Already exist")
                f=1
                break
    except EOFError:
        fin.close()
    except IOError:
        print("IO Error")
    if f==0:
        fout=open("attendance1.log","ab")
        pickle.dump(ob,fout)
        print("Attendance Marked")
        fout.close()
    return (f)
def search(empno):
    a=attendance1()
    try:
        fin=open("attendance1.log","rb")
        while True:
            a=pickle.load(fin)
            if a.empno()==empno:
                a.display()
                break
    except EOFError:
        fin.close()
        print ("no such employee no exists")
        fin.close()
def add():
    f=1
    a=attendance1()
    while f==1:
        id2=3
        t=time
        a.get_detail(id2,t)
        f=add_record(a)
add()
def disp():
    empno=3
    search(empno)
disp()    
