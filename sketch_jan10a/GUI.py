import customtkinter
import tkinterDnD
import time

customtkinter.set_ctk_parent_class(tkinterDnD.Tk)

customtkinter.set_appearance_mode('dark')

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.start_time = time.time()
        self.current_time = 0
        self.title("my app")
        self.geometry("400x150")
        self.grid_columnconfigure((0, 1), weight=1)

        self.timer_1 = customtkinter.CTkLabel(self.App, text = 'placeholder')
        self.timer_1.grid(row=0, column=0, padx=20, pady=20)
        self.update_time()

    def button_callback(self):
        return
    
    def update_time(self):
        # Get the current time
        current_time = time.strftime('%H:%M:%S')

        # Update the label text
        self.label.config(text=current_time)

        # Schedule the function to run again after 1000ms (1 second)
        self.after(1000, self.update_time)

app = App()
app.mainloop()
