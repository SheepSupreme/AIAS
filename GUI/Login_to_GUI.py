import time
from customtkinter import *
from PIL import Image
import mysql.connector
import subprocess

db = mysql.connector.connect(
    host="127.0.0.1",
    user="userdb",
    password="userdb",
)
cursor = db.cursor()

class LoginApp(CTk):
    def __init__(self):

        #main setup
        super().__init__()
        self.title('Login to Database')
        self.geometry("600x480")
        self.resizable(0, 0)

        self.Login = Login(self)

                
        self.mainloop()

    

class Login(CTkLabel):
    def __init__(self, master):
        super().__init__(master)

        self.grid(sticky = "nsew")

        self.columnconfigure((0,1), weight=1, uniform='a')
        self.rowconfigure(0, weight=1, uniform='a')

        side_img_data = Image.open("Hintergrund_Menu.jpg")
        email_icon_data = Image.open("email-icon.png")
        password_icon_data = Image.open("password-icon.png") 

        side_img = CTkImage(dark_image=side_img_data, light_image=side_img_data, size=(300, 480))
        email_icon = CTkImage(dark_image=email_icon_data, light_image=email_icon_data, size=(20, 20))
        password_icon = CTkImage(dark_image=password_icon_data, light_image=password_icon_data, size=(17, 17))

        CTkLabel(master=self, text="", image=side_img).grid(column=0, row=0, sticky='nsew')

        frame = CTkFrame(master=self, width=300, height=480, fg_color="#ffffff")
        frame.grid(column=1, row=0, sticky="nsew",)
        

        CTkLabel(master=frame, text="Welcome!", text_color="#990099", anchor="w", justify="left",
                font=("Arial Bold", 24)).pack(anchor="w", pady=(50, 5), padx=(25, 0))
        CTkLabel(master=frame, text="Login to Inventory-Manager!", text_color="#990099", anchor="w", justify="left",
                font=("Arial Bold", 12)).pack(anchor="w", padx=(25, 0))

        CTkLabel(master=frame, text="  Email:", text_color="#990099", anchor="w", justify="left",
                font=("Arial Bold", 14), image=email_icon, compound="left").pack(anchor="w", pady=(38, 0), padx=(25, 0))
        email_entry = CTkEntry(master=frame, width=225, fg_color="#EEEEEE", border_color="#990099", border_width=1,
                            text_color="#000000")
        email_entry.pack(anchor="w", padx=(25, 0))

        CTkLabel(master=frame, text="  Password:", text_color="#990099", anchor="w", justify="left",
                font=("Arial Bold", 14), image=password_icon, compound="left").pack(anchor="w", pady=(21, 0), padx=(25, 0))
        password_entry = CTkEntry(master=frame, width=225, fg_color="#EEEEEE", border_color="#990099", border_width=1,
                                text_color="#000000", show="*")
        password_entry.pack(anchor="w", padx=(25, 0))

        status_label = CTkLabel(master=frame, text="", text_color="#990099", anchor="w", justify="left",
                                font=("Arial Bold", 12))
        status_label.pack(anchor="w", padx=(25, 0))


        def login():

            email = 0
            password = 0
            user = 0

            # Retrieve login credentials
            email = email_entry.get()
            password = password_entry.get()

            # Construct SQL query to fetch user record
            query = """SELECT password FROM login.user_password WHERE email = '%s'""" %email
            cursor.execute(query)
            
            for row in cursor:
                stored_password = row[0]

            
            if user is not None:
                # Compare passwords  
                if password == stored_password:
                    # Login successful
                    status_label.configure(text="Login successful!", text_color="#00FF00")
                    time.sleep(2)
                    self.destroy()
                    subprocess.run(["python", "GUI_Classes.py"])  
                else:
                    # Invalid password
                    status_label.configure(text="Invalid password!", text_color="#FF0000")
            else:
                # User not found
                status_label.configure(text="User not found!", text_color="#FF0000")
                
        CTkButton(master=frame, text="Login", fg_color="#990099", hover_color="#FFB7FF", font=("Arial Bold", 12),
                text_color="#ffffff", width=225, command=login).pack(anchor="w", pady=(40, 0), padx=(25, 0))


LoginApp()