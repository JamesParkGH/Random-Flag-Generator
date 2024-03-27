# Title: GUI Module
# Author(s): Ganghoon Park

# Import necessary libraries
from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
import FlagGenerator
import webbrowser

root = tk.Tk() #create window object & indicates the beginning of interface

canvas = tk.Canvas(root, width=600, height=300) #600x300 pixels
canvas.grid(columnspan=3) #splits canvas to 2 identical columns to place elements 

#Flag generator logo (will need to change later)
logo = Image.open("./ImagesGUI/flag_logo.png") #load logo image
logo = ImageTk.PhotoImage(logo) #convert pillow image into tkinter image
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1, row=0)

#Instruction Text
instructions = tk.Label(root, text="Generate a random flag", font="Arial")
instructions.grid(columnspan=3, column=0, row=1)

instructions2 = tk.Label(root, text="Generated flag: ", font="Arial")
instructions2.grid(columnspan=3, column=0, row=12)

#Function to generate flag

def generateflag():
    FlagGenerator.generate_flag(str(e1.get()), "sha256")

def generate_pic():
    root = Tk()      
    canvas = Canvas(root, width = 300, height = 300)            
    pic1 = Image.open("./generated_flags/flag_"+str(e1.get())+".png")      
    photo1 = ImageTk.PhotoImage(pic1)
    resized_image= pic1.resize((300,205), Image.ANTIALIAS)
    new_image= ImageTk.PhotoImage(resized_image)
    label = Label(image=new_image)
    label.place(x=150, y=550)
    root.mainloop() 

#Generate button
generate_text = tk.StringVar()
generate_pictext = tk.StringVar()

tk.Label(root, text="Text input").grid(row=2, column=0)

e1 = tk.Entry(root)
e1.grid(row=2, column=1)

generate_btn = tk.Button(root, textvariable=generate_text, command=lambda:generateflag(), font="Raleway", bg="blue", fg="white", height=2, width=15)
generate_text.set("Generate Flag")
generate_btn.grid(column=1, row=5)

generate_picbtn = tk.Button(root, textvariable=generate_pictext, command=lambda:generate_pic(), font="Raleway", bg="red", fg="white", height=2, width=15)
generate_pictext.set("Display Flag")
generate_picbtn.grid(column=1, row=7)

canvas = tk.Canvas(root, width=600, height=250)
canvas.grid(columnspan=3)

root.mainloop() #end command 


'''
class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, GUI):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

class StartPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        self.image2 = Image.open("./ImagesGUI/generatebutton.png")
        self.image = Image.open("./ImagesGUI/flag_logo.png")
        self.photo = ImageTk.PhotoImage(self.image)
        self.photo2 = ImageTk.PhotoImage(self.image2)
        self.logo = Label(self, image=self.photo)
        self.button = Label(self, image=self.photo2)
        self.generate = Button(self, image=self.photo2, command=lambda: controller.show_frame("GUI"))
        self.button.bind("<Button 1>", lambda self: controller.show_frame("GUI"))
        self.init_window()

    def init_window(self):
        self.logo.place(x=0, y=0)
        self.button.place(x=0, y=200)

class GUI(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        self.image = Image.open("./ImagesGUI/text_input.png")
        #self.resizeimage = self.image.resize((15,4))
        self.image2 = Image.open("./ImagesGUI/generatebutton.png")

        self.photo = ImageTk.PhotoImage(self.image)
        self.photo2 = ImageTk.PhotoImage(self.image2)
        
        self.label = Label(self, image=self.photo)
        self.button = Label(self, image=self.photo2)
        
        self.button.bind("<Button 1>", self.generate)

        self.input_box = Entry(self)
        
        self.generate = Button(self, text="Generate", command=self.generate)


        self.graphics = FlagGenerator.generate_flag("helllloooo", "sha256")
        self.init_window()

    def init_window(self):

        self.label.place(x=0, y=0)
        self.input_box.place(x=100, y=150)
        self.button.place(x=0, y=200)


    def generate(self, event):
        string = self.input_box.get()

        self.graphics.generate_flag("helllloooo", "sha256")
        
if __name__.endswith('__main__'):
    app = SampleApp()
    app.geometry("310x400")
    app.title("Flag Generator")
    app.mainloop()
'''
    
