import tkinter
from tkinter import ttk


class UI:
    def __init__(self,screen_name, height, width):
        self.screen =  tkinter.Tk()
        self.screen.title(screen_name)
        self.screen.geometry(f"{height}x{width}") 

    def pack (self, element):
        element.pack()   


    @staticmethod
    def loop(obj):
        obj['screen'].mainloop()

class Input:
    def __init__(self):
        self.entry = tkinter.Entry()

    def get_input_component(self):
        return self.entry
    
    def get_data(self):
        return self.entry.get()
    
    def to_int(self):
        return int(self.entry.get())

class Button:
    def __init__(self, text, bg="purple", fg="black", command=""):
        self.text = text
        self.fg = fg
        self.bg = bg
        self.button = tkinter.Button(
            command=command if command else "",
            text=self.text, bg=self.bg, fg=self.fg) 

    def get_button_component(self):
        return self.button                 

class Label:
    def __init__(self, text, fg= "white", bg= "black"):
        self.text = text
        self.fg = fg
        self.bg = bg
        self.label = tkinter.Label(text=self.text, bg=self.bg, fg=self.fg)
                   
    def get_label_component(self):
        return self.label