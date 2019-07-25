# author : ARYAN MITTAL

from tkinter import *
import parser
import math


root = Tk()
root.title('Calculator')

# write func to get input and place in textfield
i = 0
def get_variables(num):
    global i
    # i for index position on textfield
    display.insert(i,num)
    i+=1

def clear_all():
    display.delete(0,END)

def undo():
    entire_string = display.get()
    if len(entire_string):
        new_string = entire_string[:-1]
        clear_all()

        display.insert(0,new_string)
    else:
        clear_all()
        display.insert(0,"Error")

def get_operation(operator):
    global i
    length = len(operator)
    display.insert(i,operator)
    i+=length

def fact():
    global i
    display.insert(i,"!")
    i+=1

def calculate():
    entire_string = display.get()
    try:
        if entire_string[-1] == "!":
            clear_all()
            result = math.factorial(int(entire_string[0:len(entire_string)-1]))
            display.insert(0,result)
        else:
            result = eval(entire_string)
            clear_all()
            display.insert(0,result)
    except:
        clear_all()
        display.insert(0,"Error")

def cal_fact():
    entire_number = int(display.get())
    result = math.factorial(entire_number)
    clear_all()
    display.insert(0,result)

# adding the input fields
# Entry to inputfields
display = Entry(root)

# adding this to main window and form grid layout
# sticky W+E for layout to spread from West to East
display.grid(row = 1,columnspan=6,sticky=W+E)

# adding buttons to calc
Button(root,text="1",command = lambda :get_variables(1)).grid(row=2,column=0)
Button(root,text="2",command = lambda :get_variables(2)).grid(row=2,column=1)
Button(root,text="3",command = lambda :get_variables(3)).grid(row=2,column=2)

Button(root,text="4",command = lambda :get_variables(4)).grid(row=3,column=0)
Button(root,text="5",command = lambda :get_variables(5)).grid(row=3,column=1)
Button(root,text="6",command = lambda :get_variables(6)).grid(row=3,column=2)

Button(root,text="7",command = lambda :get_variables(7)).grid(row=4,column=0)
Button(root,text="8",command = lambda :get_variables(8)).grid(row=4,column=1)
Button(root,text="9",command = lambda :get_variables(9)).grid(row=4,column=2)

#adding other buttons to calc
Button(root,text="AC",command= lambda :clear_all()).grid(row=5,column=0)
Button(root,text="0",command = lambda :get_variables(0)).grid(row=5,column=1)
Button(root,text="=",command=lambda :calculate()).grid(row=5,column=2)

Button(root,text="+",command= lambda :get_operation("+")).grid(row=2,column=3)
Button(root,text="-",command= lambda :get_operation("-")).grid(row=3,column=3)
Button(root,text="*",command= lambda :get_operation("*")).grid(row=4,column=3)
Button(root,text="/",command= lambda :get_operation("/")).grid(row=5,column=3)

#adding new operations
Button(root,text="pi",command= lambda :get_operation("3.14")).grid(row=2,column=4)
Button(root,text="%",command= lambda :get_operation("%")).grid(row=3,column=4)
Button(root,text="(",command= lambda :get_operation("(")).grid(row=4,column=4)
Button(root,text="exp",command= lambda :get_operation("**")).grid(row=5,column=4)

Button(root,text="<-",command= lambda :undo()).grid(row=2,column=5)
Button(root,text="!",command= lambda :fact()).grid(row=3,column=5)
Button(root,text=")",command= lambda :get_operation(")")).grid(row=4,column=5)
Button(root,text="sq",command= lambda :get_operation("**2")).grid(row=5,column=5)

root.mainloop()