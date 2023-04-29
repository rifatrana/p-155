from tkinter import *
root=Tk()
root.title("Dictionary")
root.geometry("600x400")

label_of_mutable = Label(root)
label_of_inmutable = Label(root)
label_of_tkinter = Label(root)


dictionary = {'Mutable': 'Values can be changed just like a List',
              'Immutable': 'Values can not be changed just like a tuple',
              'Tkinter': 'It is the GUI library of python'}

def mutable():
    label_of_mutable["text"] = dictionary['Mutable']
    
def inmutable():
        label_of_inmutable["text"] = dictionary['Inmutable']
    
def tkinter():
    label_of_tkinter["text"] = dictionary['Tkinter']
    
button_mutable= Button(root , text = "Meaning of Mutable",command = mutable)
button_mutable.place(relx = 0.5, rely =0.2, anchor = CENTER)

label_of_mutable.place(relx = 0.5, rely =0.3 , anchor = CENTER)

button_inmutable = Button(root , text = "Meaning of Inmutable",command = inmutable)
button_inmutable.place(relx = 0.5, rely =0.2, anchor = CENTER)

label_of_inmutable.place(relx = 0.5, rely =0.3 , anchor = CENTER)

button_tkinter = Button(root , text = "Meaning of Tkinter",command = tkinter)
button_tkinter.place(relx = 0.5, rely =0.2, anchor = CENTER)

label_of_tkinter.place(relx = 0.5, rely =0.3 , anchor = CENTER)

root.mainloop()