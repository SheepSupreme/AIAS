import customtkinter
import pyserial

root = customtkinter.CTk()

class App:
    def __init__(self,root):
        self.root = root
        self.root.title('GUI')
        self.root.geometry('400x150')
        self.root.columnconfigure(0,weight=1)

        self.button = customtkinter.CTkButton(self.root, text='press',command = self.button_press)
        self.button.grid(row=0,column=0,padx=10,pady=10)
    
    def button_press(self):
        print('button pressed')

App(root)

root.mainloop()

# customtkinter.set_appearance_mode('dark')
