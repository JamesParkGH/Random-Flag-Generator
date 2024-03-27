from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
import FlagGenerator
import webbrowser


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
        self.image2 = Image.open("./ImagesGUI/startbutton.png")
        self.image = Image.open("./ImagesGUI/flag_logo.png")
        self.photo = ImageTk.PhotoImage(self.image)

        self.resize_image2 = self.image2.resize((100, 50))

        self.photo2 = ImageTk.PhotoImage(self.resize_image2)
        self.logo = Label(self, image=self.photo)
        self.button = Label(self, image=self.photo2)
        self.generate = Button(self, image=self.photo2, command=lambda: controller.show_frame("GUI"))
        self.button.bind("<Button 1>", lambda self: controller.show_frame("GUI"))
        self.init_window()

    def init_window(self):
        self.logo.place(x=25, y=0)
        self.button.place(x=100, y=300)

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