import time
while True:
    print ("1. Employee details")
    print ("2. Recoganize Face")
    print ("3. Exit")
    ch=int(input("enter your choice"))
    if ch==1:
        import employee_detail
    elif ch==2:
        import face_recognition
        #if 0xFF == ord('q'):
            #break
    elif ch==3:  
        break

