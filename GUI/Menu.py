from customtkinter import *


class Menu(CTkFrame):
    def __init__(self, master,  cmd_dashboard, cmd_inventory, cmd_addPackage):
        super().__init__(master, fg_color="#FF99FF")
        
        self.grid(row=1, column=0, sticky="nsew", padx=5, pady=10)


        self.columnconfigure(0, weight=1, uniform='a')
        self.rowconfigure(0, weight=1, uniform='a')
        self.rowconfigure((1,2,3,4), weight=2, uniform='a')
        self.rowconfigure(5, weight=8, uniform='a')
        self.rowconfigure((6,7), weight=2, uniform='a')

    
        self.create_widgets(cmd_dashboard, cmd_inventory, cmd_addPackage)
       


    def create_widgets(self, cmd_dashboard, cmd_inventory, cmd_addPackage):

        button_menu_dashboard = CTkButton(master=self,
                                    text_color = "#990099",
                                    font=("Arial",16, "bold"),
                                    anchor="w",
                                    text="Dashboard",
                                    fg_color="transparent",
                                    bg_color="transparent",
                                    hover_color="#FFB7FF",
                                    command= cmd_dashboard)
        button_menu_dashboard.grid(row=1, column=0, sticky="nsew", padx=5, pady= 5)

        button_menu_inventory = CTkButton(master=self,
                                    text_color = "#990099",
                                    font=("Arial",16, "bold"),
                                    anchor="w",
                                    text="Inventory",
                                    fg_color="transparent",
                                    hover_color="#FFB7FF",
                                    command=cmd_inventory)
        button_menu_inventory.grid(row=2, column=0, sticky="nsew", padx=5, pady= 5)

        # button_menu_order = CTkButton(master=self,
        #                             text_color = "#990099",
        #                             font=("Arial",16, "bold"),
        #                             anchor="w",
        #                             text="Order",
        #                             fg_color="transparent",
        #                             hover_color="#FFB7FF",
        #                             command=cmd_order)
        # button_menu_order.grid(row=3, column=0, sticky="nsew", padx=5, pady= 5)

        button_menu_addpackage = CTkButton(master=self,
                                    text_color = "#990099",
                                    font=("Arial",16,"bold"),
                                    anchor="w",
                                    text="Add Package",
                                    fg_color="transparent",
                                    hover_color="#FFB7FF",
                                    command=cmd_addPackage)
        button_menu_addpackage.grid(row=7, column=0, sticky="nsew", padx=5, pady= 5)

        # button_menu_deletepackage = CTkButton(master=self,
        #                             text_color = "#990099",
        #                             font=("Arial", 16, "bold"),
        #                             anchor="w",
        #                             text="Delete Package",
        #                             fg_color="transparent",
        #                             hover_color="#FFB7FF",
        #                             command=cmd_deletePackage)
        # button_menu_deletepackage.grid(row=7, column=0, sticky="nsew", padx=5, pady= 5)