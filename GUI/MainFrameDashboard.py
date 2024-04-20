import time
from datetime import datetime
from tkinter import messagebox
from customtkinter import *
from Spinbox import *
import mysql.connector
from errno import errorcode
import serial

host = "127.0.0.1"
user = "userdb"
password = "userdb"
database = "aks" 

# serial_port = 'COM3'
# baud_rate = 9600
# ser = serial.Serial(serial_port, baud_rate, timeout=2)

try:
    conn = mysql.connector.connect(host=host,user=user,password=password)
    print("Connection established")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with the user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
else:
    cursor = conn.cursor()


class MainFrameDashboard(CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.grid(row=1, column=1, sticky="nsew", padx=5, pady=10)

        self.columnconfigure(0, weight=1, uniform='a')
        self.columnconfigure(1, weight=1, uniform='a')
        self.columnconfigure(2, weight=1, uniform='a')
        self.rowconfigure(0, weight=8, uniform='a')
        self.rowconfigure(1, weight=1, uniform='a')
        self.rowconfigure(2, weight=32, uniform='a')
        self.rowconfigure(3, weight=32, uniform='a')

        self.create_headline()
        self.kapazity()
        self.ausgabe()
        self.steuerung()
        self.issue_table()




    def create_headline(self):

        label_headline = CTkLabel(self, text="Dashboard", text_color = "#FF99FF", font=("Arial",24,"bold"))
        label_headline.grid(column=1, row=0, sticky="nsew", pady=5, padx=5)

        label_underline = CTkLabel(self, fg_color="#FF99FF", text="", )
        label_underline.grid(column=0, row=1, columnspan=3, sticky="nsew", padx=10)

    def kapazity(self):

        Kapazity_Box = CTkFrame(self, corner_radius=5 )
        Kapazity_Box.grid(column=0, row=2, sticky="nsew", pady=10, padx=10)

        Kapazity_Box.columnconfigure(0, weight=1, uniform='a')
        Kapazity_Box.columnconfigure(1, weight=1, uniform='a')
        Kapazity_Box.columnconfigure(2, weight=1, uniform='a')
        Kapazity_Box.rowconfigure(0, weight=1, uniform='a')
        Kapazity_Box.rowconfigure(1, weight=4, uniform='a')
        Kapazity_Box.rowconfigure(2, weight=1, uniform='a')

        headline = CTkLabel(Kapazity_Box, text="Utilization", text_color= "#FF99FF", font=("Arial",24,"bold"))
        headline.grid(column= 0, row=0, columnspan=3, pady=2, padx=2, sticky="nsew")
        
        box1 = CTkFrame(Kapazity_Box, border_color="#FF99FF", border_width=1)
        box1.grid(column=0, row=1, pady=2, padx=(10,5), sticky="nsew")

        box1.columnconfigure(0, weight=1)
        box1.rowconfigure((0,1,2),weight=1)

        box1_1 = CTkFrame(box1,fg_color="transparent", corner_radius=0)
        box1_1.grid(column=0, row=2)

        box1_2 = CTkFrame(box1,fg_color="transparent", corner_radius=0)
        box1_2.grid(column=0, row=1)

        box1_3 = CTkFrame(box1,fg_color="transparent", corner_radius=0)
        box1_3.grid(column=0, row=0)

        box2 = CTkFrame(Kapazity_Box, border_color="#FF99FF", border_width=1)
        box2.grid(column=1, row=1, pady=2, padx=5, sticky="nsew")

        box2.columnconfigure(0, weight=1)
        box2.rowconfigure((0,1,2),weight=1)

        box2_1 = CTkFrame(box2,fg_color="transparent", corner_radius=0)
        box2_1.grid(column=0, row=2)

        box2_2 = CTkFrame(box2,fg_color="transparent", corner_radius=0)
        box2_2.grid(column=0, row=1)

        box2_3 = CTkFrame(box2,fg_color="transparent", corner_radius=0)
        box2_3.grid(column=0, row=0)

        box3 = CTkFrame(Kapazity_Box, border_color="#FF99FF", border_width=1)
        box3.grid(column=2, row=1, pady=2, padx=(5,10), sticky="nsew")
 
        box3.columnconfigure(0, weight=1)
        box3.rowconfigure((0,1,2),weight=1)

        box3_1 = CTkFrame(box3,fg_color="transparent", corner_radius=0)
        box3_1.grid(column=0, row=2)

        box3_2 = CTkFrame(box3,fg_color="transparent", corner_radius=0)
        box3_2.grid(column=0, row=1)

        box3_3 = CTkFrame(box3,fg_color="transparent", corner_radius=0)
        box3_3.grid(column=0, row=0)

        box1text = CTkLabel(Kapazity_Box, text = "0%", text_color= "#FF99FF", font=("Arial",16,"bold"))
        box1text.grid(column=0, row=2, pady=2, padx=2, sticky="nsew")

        box2text = CTkLabel(Kapazity_Box, text = "0%", text_color= "#FF99FF", font=("Arial",16,"bold"))
        box2text.grid(column=1, row=2, pady=2, padx=2, sticky="nsew")

        box3text = CTkLabel(Kapazity_Box, text = "0%", text_color= "#FF99FF", font=("Arial",16,"bold"))
        box3text.grid(column=2, row=2, pady=2, padx=2, sticky="nsew")

        

        def update_utilization():
            query = "SELECT COUNT(*) FROM aks.tfact_issue_inventory WHERE position_x = %s"
            
            cursor.execute(query, (1,))
            count1 = cursor.fetchone()[0]
            cursor.execute(query, (2,))
            count2 = cursor.fetchone()[0]
            cursor.execute(query, (3,))
            count3 = cursor.fetchone()[0]
            
            box1text.configure(text=f"{count1} Packages")
            box2text.configure(text=f"{count2} Packages")
            box3text.configure(text=f"{count3} Packages")
            
            if count1 == 0:
                box1_1.configure(bg_color="transparent")
                box1_2.configure(bg_color="transparent")
                box1_3.configure(bg_color="transparent")
            elif count1 == 1:
                box1_1.configure(bg_color="#FF99FF")
                box1_2.configure(bg_color="transparent")
                box1_3.configure(bg_color="transparent")
            elif count1 == 2:
                box1_1.configure(bg_color="#FF99FF")
                box1_2.configure(bg_color="#FF99FF")
                box1_3.configure(bg_color="transparent")
            elif count1 == 3:
                box1_1.configure(bg_color="#FF99FF")
                box1_2.configure(bg_color="#FF99FF")
                box1_3.configure(bg_color="#FF99FF")
            
            
            if count2 == 0:
                box2_1.configure(bg_color="transparent")
                box2_2.configure(bg_color="transparent")
                box2_3.configure(bg_color="transparent")
            elif count2 == 1:
                box2_1.configure(bg_color="#FF99FF")
                box2_2.configure(bg_color="transparent")
                box2_3.configure(bg_color="transparent")
            elif count2 == 2:
                box2_1.configure(bg_color="#FF99FF")
                box2_2.configure(bg_color="#FF99FF")
                box2_3.configure(bg_color="transparent")
            elif count2 == 3:
                box2_1.configure(bg_color="#FF99FF")
                box2_2.configure(bg_color="#FF99FF")
                box2_3.configure(bg_color="#FF99FF")
            
            
            if count3 == 0:
                box3_1.configure(bg_color="transparent")
                box3_2.configure(bg_color="transparent")
                box3_3.configure(bg_color="transparent")
            elif count3 == 1:
                box3_1.configure(bg_color="#FF99FF")
                box3_2.configure(bg_color="transparent")
                box3_3.configure(bg_color="transparent")
            elif count3 == 2:
                box3_1.configure(bg_color="#FF99FF")
                box3_2.configure(bg_color="#FF99FF")
                box3_3.configure(bg_color="transparent")
            elif count3 == 3:
                box3_1.configure(bg_color="#FF99FF")
                box3_2.configure(bg_color="#FF99FF")
                box3_3.configure(bg_color="#FF99FF")

            # Timer erneut starten
            self.after(5000, update_utilization)

        update_utilization()

    def ausgabe(self):

        Ausgabe_Box = CTkFrame(self, corner_radius=5 )
        Ausgabe_Box.grid(column=0, row=3, sticky="nsew", pady=10, padx=10)

        Ausgabe_Box.columnconfigure(0, weight=1, uniform='a')
        Ausgabe_Box.rowconfigure(0, weight=2, uniform='a')
        Ausgabe_Box.rowconfigure(1, weight=4, uniform='a')
        Ausgabe_Box.rowconfigure(2, weight=4, uniform='a')

        headline = CTkLabel(Ausgabe_Box, text="Issue Packages", text_color= "#FF99FF", font=("Arial",24,"bold"))
        headline.grid(column= 0, row=0, columnspan=2, pady=2, padx=2, sticky="nsew")

        Spinbox = FloatSpinbox(Ausgabe_Box)
        Spinbox.grid(column=0, row= 1, sticky="ew")

        def package_issue():
            
            query = "SELECT COUNT(*) FROM aks.tfact_issue_inventory"
            cursor.execute(query)
            result = cursor.fetchall()

            for row in result:
                counter = row[0]

            for i in range(min(int(Spinbox.get()), counter)):

                query = "SELECT position_x FROM aks.tfact_issue_inventory WHERE position_y = 1 AND issue_datetime = (SELECT MIN(issue_datetime) FROM aks.tfact_issue_inventory)"
                cursor.execute(query)
                result = cursor.fetchall()
                
                if result and result[0][0] is not None:
                    x = result[0][0]

                    print(x)

                    # message = "Position"+str(x)
                    # print("message send:"+message)
                    # message_bytes = message.encode('ascii')
                    # ser.write(message_bytes)


                    query = "DELETE FROM aks.tfact_issue_inventory WHERE position_x = %s AND position_y = 1" %x
                    cursor.execute(query)
                    conn.commit()

                    query = "UPDATE aks.tfact_issue_inventory SET position_y = position_y - 1 WHERE position_x = %s" %x
                    cursor.execute(query)
                    conn.commit()
                

        Button = CTkButton(Ausgabe_Box,
                            text= "Issue!",
                            font=("Arial",24,"bold"),
                            fg_color = "#FF99FF",
                            text_color = "#990099",
                            hover_color="#FFB7FF",
                            command= package_issue)
        Button.grid(column=0, row=2, pady=(0,50), padx=20, sticky = "nsew")


    def steuerung(self):

        Steuerung_Box = CTkFrame(self, corner_radius=5 )
        Steuerung_Box.grid(column=1, row=2, rowspan=2, sticky="nsew", pady=10, padx=10)

        Steuerung_Box.columnconfigure(0, weight=1, uniform='a')
        Steuerung_Box.rowconfigure(0, weight=1,uniform='a')
        Steuerung_Box.rowconfigure(1, weight=1,uniform='a')
        Steuerung_Box.rowconfigure(2, weight=1,uniform='a')
        Steuerung_Box.rowconfigure(3, weight=1,uniform='a')
        Steuerung_Box.rowconfigure(4, weight=1,uniform='a')
        Steuerung_Box.rowconfigure(5, weight=1,uniform='a')
        Steuerung_Box.rowconfigure(6, weight=1,uniform='a')

        headline = CTkLabel(Steuerung_Box, text="Steering", text_color="#FF99FF", font=("Arial",24, "bold"))
        headline.grid(column=0, row=0, sticky="nsew")

        class Button:
            def __init__(self,root,name,cmd,_row,_column):
                self.root = root
                self.name = name
                self.cmd = cmd
                self.button = CTkButton(master=self.root,
                                        text = self.name,
                                        command=self.send_text,
                                        fg_color="#FF99FF",
                                        text_color = "#990099",
                                        hover_color="#FFB7FF",
                                        font=("Arial",16,"bold"))
                self.button.grid(row = _row, column = _column, padx=10,pady=10, sticky="nsew")
            
            def send_text(self):
                print('sent')
                # message = self.name
                # print("message send:"+message)
                # message_bytes = message.encode('ascii')
                # ser.write(message_bytes)
                # while True:
                #     text_mod = ser.readline()
                #     text = text_mod.decode().strip()
                #     print("message received:",text);
                #     if text == 'cmd_end': 
                #         break

        button_calibrate = Button(Steuerung_Box,'calibrate','calibration 50',1,0)
        button_blink = Button(Steuerung_Box,'blink','blink 0',2,0)
        button_pos1 = Button(Steuerung_Box,'move to pos_1', "pos_1 0",3,0)
        button_pos2 = Button(Steuerung_Box,'move to pos_2', "pos_2 0",4,0)
        button_pos3 = Button(Steuerung_Box,'move to pos_3', "pos_3 0",5,0)
        button_pos4 = Button(Steuerung_Box,'move to pos_4', "pos_4 0",6,0)


    def issue_table(self):

        issue_table_frame = CTkFrame(self, corner_radius=5 )
        issue_table_frame.grid(column=2, row=2, rowspan=2, sticky="nsew", pady=10, padx=10)

        issue_table_frame.columnconfigure(0, weight=1, uniform='a')
        issue_table_frame.rowconfigure(0, weight=1, uniform='a')
        issue_table_frame.rowconfigure(1, weight=10, uniform='a')

        headline = CTkLabel(issue_table_frame, text="Issue-System", text_color="#FF99FF", font=("Arial",24, "bold"))
        headline.grid(column=0, row=0, columnspan=2, sticky="nsew")

        table = CTkScrollableFrame(issue_table_frame, corner_radius=5)
        table.grid(column=0,row=1, pady=10, padx=10, sticky="nsew")
        table.columnconfigure(0,weight=1)

        class TimerEntry:
            def __init__(self, end_time, ID):
                self.container = CTkFrame(master=table, corner_radius=5, border_width=1)
                self.container.grid(row=0, column=0, sticky='nswe', pady=(5,0), padx=5)
                self.ID = ID
                self.end_time = end_time
                self.current_time = end_time - datetime.now()
                self.container.columnconfigure((0,1), weight=1)
                self.container.rowconfigure(0, weight=1)
                self.label1 = CTkLabel(self.container,font=('Arial', 20))
                self.label1.grid(column=0, row=0,padx=5, pady=5, sticky="nsew")
                self.label2 = CTkLabel(self.container, font=('Arial', 20))
                self.label2.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")
                self.update()

            def update(self):
                self.current_time = self.end_time - datetime.now()
                seconds = self.current_time.total_seconds()
                self.label2.configure(text=int(seconds))
                self.label1.configure(text=self.ID)
                if seconds < 0:
                    self.label2.configure(bg_color='red')
                self.container.after(1000, self.update)

        def get_endtimes_from_db():
            query = "SELECT issue_datetime FROM aks.tfact_issue_inventory"
            cursor.execute(query)
            results = cursor.fetchall()
            conn.commit()
            return [result[0] for result in results] if results else []
        
        def get_Id_from_db():
            query = "SELECT ID FROM aks.tfact_issue_inventory"
            cursor.execute(query)
            results = cursor.fetchall()
            conn.commit()
            return [result[0] for result in results] if results else []
        

        def add_timer_from_db():
            end_times = get_endtimes_from_db()
            Ids = get_Id_from_db()

            for i, (end_time, ID) in enumerate(zip(end_times, Ids), start=1):
                TimerEntry(end_time, ID).container.grid(row=i, column=0, sticky='nswe')
        
            self.after(5000, add_timer_from_db)
                                
            
        add_timer_from_db()