from customtkinter import *

class TopLeiste(CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color="#FF99FF", height=50, width=2000)

        self.grid(row=0, column=0, columnspan=2, sticky="nsew", padx=5, pady=1)
        
        #TopLeiste Grid
        self.columnconfigure(0, weight=1, uniform='a')
        self.columnconfigure(1, weight=6, uniform='a')
        #self.columnconfigure(2, weight=1, uniform='a')
        self.rowconfigure(0, weight=1, uniform='a')

        label_text = CTkLabel(self, text="Package-System", text_color = "#990099", font=("Arial",16,"bold"))
        label_text.grid(column=0, row=0, sticky="nsew", pady=5, padx=5)

       # self.create_widgets()

    #def create_widgets(self):
        
        #frame_text = CTkFrame(self)
        #frame_text.grid(column=0, row=0, sticky="nsew", pady=5, padx=5)

        #label_text = CTkLabel(self, text="Package-System", text_color = "#990099", font=("Arial",16,"bold"))
        #label_text.grid(column=0, row=0, sticky="nsew", pady=5, padx=5)

        


        # button_konto = CTkButton(master=self,
        #                             text_color = "#990099",
        #                             font=("Arial", 16, "bold"),
        #                             anchor="e",
        #                             text="Konto",
        #                             fg_color="transparent",
        #                             hover_color="#FFB7FF",
        #                             width= 40)
        # button_konto.grid(column=2, row=0, sticky="e", pady=5, padx=5)

