import tkinter

def button_clicked():
    print("I got clicked")
    new_text=input.get()
    my_label.config(text=new_text)

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100,pady=200)

#TODO:Create a label
my_label = tkinter.Label(text="I Am a Label", font=("Arial", 24, "bold"))
#my_label["text"] = "new Text"
my_label.config(text="New text")
my_label.grid(column=0, row=0)
my_label.config(padx=50,pady=50)
#my_label.place(x=100, y=200)
#my_label.pack()

#TODO:Create a button
button=tkinter.Button(text="Click Me", command=button_clicked)
button.grid(column=1,row=1)
#button.pack()

#TODO:Create a new button
button=tkinter.Button(text="New Button", command=button_clicked)
button.grid(column=2,row=0)
#button.pack()

#TODO:Create an Entry

input = tkinter.Entry(width=10)
print(input.get())
input.grid(column=3, row=2)
#input.pack()

window.mainloop() # keep the window on screen