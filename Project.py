from tkinter import *

window = Tk()
#labels
label_username = Label(window , text =  'User_name')
label_username.grid(row = 0 , column = 0)
label_username = Label(window , text =  'grade')
label_username.grid(row = 0 , column = 1 , padx=5 , pady=5)
#entrys
entry_username = Entry(window , fg = 'blue')
entry_username.grid(row=1 , column = 0, padx=5 , pady=5)
entry_grade = Entry(window, fg='red')
entry_grade.grid(row=1 , column = 1, padx=5 , pady=5 )
#list_boxes
list_box= Listbox(window)
list_box.grid(row=2,columnspan = 2 ,sticky = W+E )
#button
button = Button(window , text = 'Enter' )
button.grid(row=3 , column = 0 ,columnspan = 2 ,sticky = W+E , padx=5 , pady=5)
window.mainloop()