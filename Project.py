from tkinter import *
def average(averagerating , numvotes , vote):
    averagerating1=float(averagerating)
    numvotes1=int(numvotes)
    vote1=int(vote)
    old_vote = averagerating1 * numvotes1
    vote1 += old_vote
    return float(vote1 / (numvotes1+1)) 


def Enter():
    #integers
    list_box_entry=list_box.get(ACTIVE)
    value_grade = entry_grade.get()
    key=0
    for film1 in menue:
        name_films1=film1.split('\t')[2]
        if name_films1 == list_box_entry:
            break
        else:
            key +=1
    print(key)

    ###############
    films_rate=open("C:\\Users\\Shahab\\Desktop\\uni-projects\\DS-00-Phase1\\title.ratings.txt" , 'r+')
    menue_rate= films_rate.readlines()
    name_films=[]
    
    for film in menue_rate:
        name_films+=(film.split('\t'))

    average_rate = name_films[1+3*key]

    numvote = name_films[2+3*key]
    name_films[1+3*key]= str(average(average_rate , numvote , value_grade )) ####
    name_films[2+3*key]=int(name_films[2+3*key])
    name_films[2+3*key] +=1
    name_films[2+3*key] = str(name_films[2+3*key])
    name_films[2+3*key] += '\n'


    print(name_films[1+3*key])
    edit=open("C:\\Users\\Shahab\\Desktop\\uni-projects\\DS-00-Phase1\\title.akas.txt" , 'w+')
    j=0
    for edits in name_films:
         j+=1
         if (j%3==0):
            edit.writelines(edits)
         else:
            edit.writelines(edits+'\t')

    ################
films=open("H:\\title.akas.txt" , 'r+')
menue = films.readlines()

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
for film in menue:
    name_films=film.split('\t')[2]
    if name_films != 'title':
        list_box.insert(END ,name_films )
#button
button = Button(window , text = 'Enter' , command = Enter)
button.grid(row=3 , column = 0 ,columnspan = 2 ,sticky = W+E , padx=5 , pady=5)

window.update_idletasks()
window.mainloop()
window.geometry(50+50+50+50)
