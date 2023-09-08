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
        try:
            res=0
            with open("filenames.txt","r") as filenames:
                for line in filenames:
                    if line.rstrip()==filename:
                        res+=1
        except FileNotFoundError:
            with open("filenames.txt","w"):
                pass
        if res==1:
            print("-----------------")
            print("This file exists!")
            print("------------------")
            break
        else:            
        
        
            with open(filename, "w") as x:
                pass
            with open("filenames.txt","a") as filenames:
                filenames.write(filename+"\n")
            print("--------------------------")
            print("File succesfully generated!")
            print("--------------------------")
            break
def editing_modes():
    print("-----------------------")
    print("1 for truncate the file")
    print("2 for append context")
    print("3 for overwriting")
    print("-----------------------")
def edit():
    while True:
        if not filenamesvarmı():
            print("/////There are no files!")
            break
        elif filenamesboşmu():
            print("/////There are no files!")
            break
        else:
            filenameslistesi()
            
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
                print("--------------------------------")
                print(f"{nameoftheeditingfile} doesnt exist")
                print("PLEASE WRITE AN EXISTING FILE")
                print("--------------------------------")
        
def delete():
    print("----------------")
    while True:
        if not filenamesvarmı():
            print("/////There are no files!")
            break
        elif filenamesboşmu():
            print("/////There are no files!")
            break
        else:
           
            filenameslistesi()
        
            print("----------------")

            try:
                fliline=int(input("Please type the line of the file: "))
                print("--------------------")
            except:
                print("-----------------------------------")
                print("////////////Please give acceptable line number!////////")
                print("-----------------------------------")
            else:
                
                if 0<fliline<=linenumber:
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
                    print("--------------------------")
                    
                    break
                else:
                    print("////////////Please give acceptable line number!////////")
                    print("-----------------------------------")
        


def filenamesboşmu():
    if os.path.getsize("filenames.txt") == 0:
        return True
    else:
        return False
    
def filenamesvarmı():
    if os.path.exists("filenames.txt"):
        return True
    else:
        return False


        

def filenameslistesi():
    global linenumber
    print("Here are the filenames:")
    linenumber=0
    with open("filenames.txt","r") as file:
        for line in file:
            linenumber+=1
            print(f"-{linenumber}- {line.rstrip()}")


def reading():
    filenameslistesi()
    whatthe=input("Please type the number of the file: ")
    


while True:
    main()
    x=input("Wha: ")
    if x=="4":
        break
    elif x=="3":
        delete()
        
    elif x=="2":
        edit()
        
    elif x=="1":
        create()
        
    else:
        print("1,2,3,4 gir"+"\n"+"-------------")
