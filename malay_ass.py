# -*- coding: utf-8 -*-
"""
Created on Tue May 19 04:49:31 2020

@author: Ajayi Raymond T
"""

import sys
class Transportation:
    def __init__(self):
        print("WELCOME TO SATHYS TRANSPORTATION SYSTEM")
        print("1.REgister New Vehicle Ownership\n2.Transfer Vehicle Ownership\n3.Search Vehicle Ownership\n4.Exit system")
        self.dict()
        
    def dict(self):
        try:
            
            self.empty_dict={}
            self.a=0
            while self.a<5:
                self.a+=1
                self.choice=int(input("Enter your choice:"))
                if self.choice==1:
                    print("WELCOME TO REGISTRATION")
                    print("1.Owners Details\n2.Vehicle Details\n3.Registration Number")
                    self.option=int(input("Enter Option:"))
                    if self.option==1:
                        print("Provide Owners Details Below:")
                        try:
                            self.name=input("Enter your Name:")
                            self.empty_dict["NAME"]=self.name
                            print(self.empty_dict)
                            print(self.empty_dict["NAME"])
                        
                        except:
                            print(self.empty_dict.keys()[-1])
                        
                        try:
                            self.num=int(input("Enter your IC/Passport Number:"))
                            self.empty_dict["NUMBER"]=self.num
                            print(self.empty_dict)
                            print(self.empty_dict["NUMBER"])
                        
                        except:
                            print(self.empty_dict.keys()[-2])
                      
                        try:
                            self.add=(input("Enter your Address:"))
                            self.empty_dict["Address"]=self.add
                            print(self.empty_dict)
                            print(self.empty_dict["Address"])
                        except:
                            print(self.empty_dict.keys()[-3])
                    elif self.option==2:
                        print("Provide Vehicle Details Below:")
                        try:
                            self.model=input("Enter Model:")
                            self.empty_dict["MODEL"]=self.model
                            print(self.empty_dict)
                        except:
                            print(self.empty_dict.keys()[-4])
                        print("Provide Vehicle Details Below:")
                        try:
                            self.color=input("Enter Color:")
                            self.empty_dict["COLOR"]=self.color
                            print(self.empty_dict)
                        except:
                            print(self.empty_dict.keys()[-5])
                        print("Provide Vehicle Details Below:")
                        try:
                            self.engcap=input("Enter Engine Capacity:")
                            self.empty_dict["ENGINE CAPACITY"]=self.engcap
                            print(self.empty_dict)
                        except:
                            print(self.empty_dict.keys()[-6])
                    elif self.option==3:
                        print("Provide Vehicle Detail Below:")
                        try:
                            self.regnum=input("Enter Number Plate:")
                            self.empty_dict["REGISTRATION NUMBER"]=self.regnum
                            print(self.empty_dict)
                        except:
                            print(self.empty_dict.keys()[-7])
                            
                            
                elif self.choice==2:
                    print("WELCOME TO TRANSFER")
                    print("Want to transfer ownership?")
                    self.ans=input(":")
                    if self.ans=="yes":
                        self.owner=input("Enter owners name:")
                        self.reciepient=input("Enter Reciepients Address:")
                        if self.owner== self.empty_dict["NAME"] and self.owner== self.empty_dict["Address"]:
                            print(" successfully Transferred from {} to {}".format(self.owner,self.reciepient))
                        else:
                            print("Name not found")
                            
                            
                elif self.choice==3:
                    print("WELCOME TO SEARCH")
                    self.regnum=int(input("Enter Registration number to search for:"))
                    if self.regnum== self.empty_dict["NUMBER"]:
                            print(" {} Found!!!".format(self.regnum))
                    else:
                            print("Number not found")
                    
                elif self.choice==4:
                    sys.exit()
                else:
                    print(' ')
        except:
            print("Entered Value is nor Recognised!!!")
CALL=Transportation()