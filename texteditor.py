#18.29-6.09.2023-Eren Veli Acar 
import os

def main():
    print("1 for creating file")
    print("2 for editing an existing file")
    print("3 for deleting a file")
    print("4 for quiting")

def create():
    while 1==1:
        
        filename=input("name of the file: ")
        res=0
        with open("filenames.txt","r") as filenames:
            for line in filenames:
                if line.rstrip()==filename:
                    res+=1
        if res==1:
            
            print("this file exists")
            break
        else:            
        
        
            with open(filename, "w") as x:
                pass
            with open("filenames.txt","a") as filenames:
                filenames.write(filename+"\n")
            print("file succesfully generated")
            break
def editing_modes():
    print("-----------------------")
    print("1 for truncate the file")
    print("2 for append context")
    print("3 for overwriting")
def edit():
    while True:
        nameoftheeditingfile=input("file name: ")
        result=0
        with open("filenames.txt","r") as file:
            for line in file:
                if line.rstrip()==nameoftheeditingfile:
                    result+=1
        if result==1:                
            editing_modes()
            
            y=input("Wha: ")
            if y=="3":
                insk=input("What u wanna write: ")
                with open(nameoftheeditingfile,"w") as file:
                    file.write(insk)
                break
            elif y=="2":
                insk=input("What u wanna append: ")
                with open(nameoftheeditingfile,"a") as file:
                    file.write(insk)
                break
            elif y=="1":
                with open(nameoftheeditingfile,"w") as file:
                    file.truncate()
                break
            else:
                print("1,2,3 gir"+"\n"+"-----------")
        else:
            print(f"{nameoftheeditingfile} doesnt exist")
            print("PLEASE WRITE AN EXISTING FILE")
    

def delete():
    print("----------------")
    while True:
        
        a=0
        with open("filenames.txt","r") as file:
            for line in file:
                a+=1
                print(f"-{a}- {line.rstrip()}")

        try:
            fliline=int(input("please select the line of the file"))
        except:
            print("please give appropriate line number")
        else:
            
            if 0<fliline<=a:
                a=0
                with open("filenames.txt","r") as file:
                    for line in file:
                        a+=1
                        if a==fliline:
                            lineson=line.rstrip()
                os.remove(lineson)
                
                with open("filenames.txt","r") as file:
                    filenames= file.read().splitlines()
                filenames.remove(lineson)
                
                with open("filenames.txt","w") as file:
                    file.write("\n".join(filenames))
                    
                
                print(f"{lineson} is succesfully deleted!")
                
                break
            else:
                print("please give appropriate line number")
                
while True:
    main()
    x=input("Wha: ")
    if x=="4":
        break
    elif x=="3":
        delete()
        break
    elif x=="2":
        edit()
        break
    elif x=="1":
        create()
        break
    else:
        print("1,2,3,4 gir"+"\n"+"-------------")