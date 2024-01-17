#  Shift availability PROGRAM


from tkinter import *
from tkcalendar import *
from datetime import datetime


window = Tk()
window.title('Shift Availability Compiler')
window.geometry('+350+100')
#  logo = PhotoImage(file = 'logo.gif')


#  functions
def add_button():
    selected_date = cal.get_date() # gets the selected date

    #  append and go to a new line
    log_append = open("Sign Up.txt", mode='a')
    log_append.write(f'{selected_date}\n')

    log_append.close()

    #  Display logged selections
    log = open('Sign up.txt', mode='r')
    txt_content = log.read()
    log.close()
    del_output()
    output.insert(END, txt_content)


def del_output():
    output.delete(0.0, END)


def clear_file():
    clear_content = open('Sign Up.txt', mode='r+')
    clear_content.seek(0)
    clear_content.truncate()
    txt_content = clear_content.read()
    clear_content.close()
    del_output()
    output.insert(END, txt_content)


def exit_program():
    entered_name = textentry.get().capitalize() #  gets the name
    selected_date = cal.get_date() # gets the selected date

    #  clear_file()

    window.destroy()
    exit()


#  Enter name:
#  name entry label
name_label = Label(window, text='Enter Name and Last Name', font='none 12 bold')
name_label.pack(side=TOP)

#  name entry box
textentry = Entry(window, width=50, bg='white')
textentry.pack(side = TOP)

#  Calendar picker:
#  Set today's date as default
currentDay = datetime.now().day
currentMonth = datetime.now().month
currentYear = datetime.now().year

#  create a calendar from tkcalendar
cal = Calendar(window, selectmode='day', year =currentYear, month=currentMonth, day=currentDay)
cal.pack()

#  Shift log output box:
#  create a text output box
output = Text(window, width=55, height=6, wrap=WORD, background='white')
output.pack(side=BOTTOM)

#  add button
add_butn = Button(window, text='Add', width=20, command=add_button)
add_butn.pack()

#  clear button
clear_butn = Button(window, text='Clear', width=20, command=clear_file)
clear_butn.pack()

#  send and exit button
exit_butn = Button(window, text='Save & Close', width=20, command=exit_program)
exit_butn.pack()

window.mainloop()
