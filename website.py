# sum=0
# while(True):
#     userinput=input("enter the price or press q to get total")
#     if userinput!='q':
#         sum=sum+int(userinput)
#         print(f"you total is {sum}")
#     else:
#         print(f"your total bill is{sum}.thanks for shoping with us")
#         break
# # project no 2
# def factorial(number):
#     if (number==0 or number==1):
#         return 1
#     else:
#         return number * factorial(number-1)
#
#
# # print(factorial(7))
# def ftzero(number):
#     fac=factorial(number)
#     print(fac)
#     count=0
#     while (fac%10 ==0):
#       count=count+1
#       fac=fac/10
#     return count
# if __name__=='__main__':
#     # n= int(input("enter the number: \n"))
#     print(ftzero(8))
# project no 3 currency convertor

# with open("currency.txt.py") as f:
#     lines=f.readlines()
#     print(lines)
# currencyDIC = {}
# for line in lines:
#     parsed=line.split()  
#     currencyDIC[parsed[0]]=parsed[1]
# # print(currencyDIC)
# amount=int(input("Enter the amount"))
# print("enter the name of currency you want to convert avalable option")
# [print(item) for item in currencyDIC.keys()]
# currency= input("please enter one of these values")
# print(f"{amount} pakistani is equal to {amount} * {float(currencyDIC),[currency]} {currency}")
# project 4
# import time
# from plyer import notification
# while True:
#     notification.notify(
#         title="please drink water",
#         message="water is very important for us,other wise body will dehydrate and cause problmes",
#         app_icon="",
#         timeout=10
#     )
    # time.sleep(50)

# print("WELLCOME TO OUR HOTAL")
# menu={
#     'pizza':400,
#     'pasta':450,
#     'nuggets':400,
#     'shawarma':250,
#     'cold drink':60,
# }
#
# print("pizza: 400 \n pasta: 450 \n nuggets: 400 \n shawarma: 250 \n cold drink:60")
# order_total=0
# item_1=input("enter the thing you want to get")
# order_total+=menu[item_1]
# print(f"you item {item_1} has been  added to order")
# item_2=input("enter the 2nd thing you want to get")
# order_total+=menu[item_2]
# print("you order have been saved")
# print(f"your total amount  is {order_total}")
# form generation
# from tkinter import *
# root=Tk()
# root.geometry("500x300")
#
#
# Label(root,text="REGISRATION FORM",font="arial 15 bold").grid(row=0,column=2)
# name=Label(root,text="Name")
# gender=Label(root,text="Gender")
# phone no=Label(root,text="Phone no")
# blood group=Label(root,text="Blood Group")
# name.grid(row=,column=2)
#
# root.mainloop()
# from tkinter import *
# root=Tk()
# root.geometry("500x300")
#
#
# Label(root,text="REGISTARTION FORM").grid(row=0,column=3)
# name=Label(root,text="Name")
# gender=Label(root,text="Gender")
# phone=Label(root,text="Phone no")
# blood=Label(root,text="Blood Group")
# name.grid(row=1, column=2)
# gender.grid(row=2, column=2)
# phone.grid(row=3, column=2)
# blood.grid(row=4, column=2)
#
# namevalue= StringVar
# gendervalue=StringVar
# Phonevalue=StringVar
# bloodvalue=StringVar
# checkvalue=IntVar
#
# nameentry= Entry(root, textvariable=namevalue)
# genderentry= Entry(root, textvariable=gendervalue)
# phoneentry= Entry(root, textvariable=Phonevalue)
# bloodentry= Entry(root, textvariable=bloodvalue)
#
# nameentry.grid(row=1,column=3)
# genderentry.grid(row=2,column=3)
# phoneentry.grid(row=3,column=3)
# bloodentry.grid(row=4,column=3)
#
# checkbtn=Checkbutton(text="REMEMBER ME", variable=checkvalue)
# checkbtn.grid(row=6,column=3)
#
#
# root.mainloop()
# making color
# import turtle
# turtle.bgcolor("black")
#
# squary=turtle.Turtle()
# squary.speed(20)
# squary.pencolor("green")
# for i in range(400):
#     squary.forward(i)
#     squary.left(91)
# finding phone number location
# import phonenumbers
# from test import number
#
# from phonenumbers import geocoder
# ch_number=phonenumbers.parse(number, "CH")
# print(geocoder.description_for_number(ch_number,"en"))
#
#
# from phonenumbers import carrier
# service_number=phonenumbers.parse(number,"RO")
# print(carrier.na


import streamlit as st

with st.container():
   st.title("CHEMISTRY WORLD")
   st.header("WELLCOME TO WORLD OF CHEMISTRY")
   st.subheader("YOU CAN GET CHEMISTRY KNOWLDGE FROM HERE")
   st.markdown("i am iftikhar Mahmood")
   st.write("lecturer chemistry at punjab group of college")
   st.write("CONTACT:03007932606")
st.subheader("please provide your infromation")
name=st.text_input("please enter your Name")
fname=st.text_input("please enter your Father Name")
adr=st.text_input("please enter your Adress")
cno=st.text_input("please enter your contact no")
eadr=st.text_input("please enter your email adress")
button=st.button("Done")
if button:
   st.markdown(f"""
   Name : {name}
   Father Name : {fname}
   Adress : {adr}
   contact no : {cno}
   email adress : {eadr}
   
   """)


   
