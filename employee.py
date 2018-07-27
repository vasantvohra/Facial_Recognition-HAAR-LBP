import pickle
import sys
import os
import time
class employee:
    def __init__(self):
        self.__stu_empno=0
        self.__stu_name=""
        #self.__stu_phno=""
        #self.__stu_dob="dd/mm/yyyy"
        #self.__stu_address=""
        self.__stu_desig=""
        #self.__localtime=time.asctime( time.localtime(time.time()) )
    def get_detail(self):
        self.__stu_empno=int(input("Enter Employee no."))
        self.__stu_name=input("Enter Employee name")
        #self.__stu_phno=int(input("Enter Phone no."))
        #self.__stu_dob=input("Enter Date of Birth")
        #self.__stu_address=input("Enter Address")
        self.__stu_desig=input("Enter designation")
    def display(self):
        print ("Employee no.: ",self.__stu_empno)
        print ("Employee name:",self.__stu_name)
        #print ("Phone no.: ",self.__stu_phno)
        #print ("Date of birth: ",self.__stu_dob)
        #print ("Address: ",self.__stu_address)
        print ("Designation: ",self.__stu_desig)
        #print ("Local current time :",self.__localtime)
    def empno(self):
        return self.__stu_empno
    def modify(self):
        print ("enter '.' to retain old data")
        n=int(input("enter phno."))
        if n!='.':
            self.__stu_phno=n
        #a=input("enter address")
        #if a!='.':
            #self.__stu_address=a
#function to add arecord from database
def add_record(ob):
    t=employee()
    f=0
    try:
        #data cant be entered if customer already exists.
        fin=open("employee.log","rb")
        while True:
            t=pickle.load(fin)
            if t.empno()==ob.empno():
                print (" Employee number already exists")
                f=1
                break
    except EOFError:
        fin.close()
    except IOError:
        print("IOError")
    if f==0:
        fout=open("employee.log","ab")
        pickle.dump(ob,fout)
        print ("detail added")
        fout.close()
    return (f)
#function to remove a record from database
def remove_record(empno):
    t=employee()
    i=1
    try:
        fin=open("employee.log","rb")
        fout=open("temp.log","wb")
        while True:
            t=pickle.load(fin)
            if t.empno()!=empno:
                pickle.dump(t,fout)
                print ("rec",i,"copied")
                i=i+1
    except EOFError:
        fin.close()
        fout.close()
    except IOError:
        print ("no such file exists")
        fin.close()
    os.remove("employee.log")
    os.rename("temp.log","employee.log")
    print ("record deleted")
def modify_record(empno):
    t=employee()
    try:
        fin=open("employee.log","ab+")
        while True:
            t=pickle.load(fin)
            if t.empno()==empno:
                t.modify()
                fin.seek(-(sys.getsizeof(t)),1)
                pickle.dump(t,fin)
                print ("record Modified")
                break
    except EOFError:
        fin.close()
        print ("No such file exists")
    except IOError:
        print ("no such file exists")
        fin.close()
def search(empno):
    t=employee()
    try:
        fin=open("employee.log","rb")
        while True:
            t=pickle.load(fin)
            if t.empno()==empno:
                t.display()
                break
    except EOFError:
        fin.close()
        print ("no such employee no exists")
        fin.close()
# main

