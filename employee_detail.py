import pickle
import sys
import os
import time
class employee:
    def __init__(self):
        self.__emp_empno=0
        self.__emp_name=""
        #self.__emp_phno=""
        #self.__emp_dob="dd/mm/yyyy"
        #self.__emp_address=""
        self.__emp_desig=""
        #self.__localtime=time.asctime( time.localtime(time.time()) )
    def get_detail(self):
        self.__emp_empno=int(input("Enter Employee no.: "))
        self.__emp_name=input("Enter Employee name: ")
        #self.__emp_phno=int(input("Enter Phone no.: "))
        #self.__emp_dob=input("Enter Date of Birth: ")
        #self.__emp_address=input("Enter Address: ")
        self.__emp_desig=input("Enter designation: ")
        import newface
    def display(self):
        print ("Employee no.: ",self.__emp_empno)
        print ("Employee name:",self.__emp_name)
        #print ("Phone no.: ",self.__emp_phno)
        #print ("Date of birth: ",self.__emp_dob)
        #print ("Address: ",self.__emp_address)
        print ("Designation: ",self.__emp_desig)
        #print ("Local current time :",self.__localtime)
    def empno(self):
        return self.__emp_empno
    def modify(self):
        print ("enter '.' to retain old data")
        n=int(input("enter phno."))
        if n!='.':
            self.__emp_phno=n
        #a=input("enter address")
        #if a!='.':
            #self.__emp_address=a
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
        print ("no such emp id exists")
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
while True:
    print ("1. Add a Employee detail ")
    print ("2. Delete a Employee detail ")
    print ("3. Modify a Employee detail ")
    print ("4. To display detail")
    print ("5. Go back to main menu")
    ch=int(input("enter your choice: "))
    if ch==1:
        f=1
        t=employee()
        while f==1:
            t.get_detail()
            f=add_record(t)
    elif ch==2:
        empo=int(input("enter the Employee number whose record is to be deleted: "))
        remove_record(empo)
    elif ch==3:
        empo=int(input("enter the Employee number whose record is to be Modified: "))
        modify_record(empo)
    elif ch==4:
        empo=int(input("enter Employee number: "))
        search(empo)
        
    elif ch==5:
        import menu
        break
