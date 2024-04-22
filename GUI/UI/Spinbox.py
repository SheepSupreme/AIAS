from typing import Union
from typing import Callable
from customtkinter import *


class FloatSpinbox(CTkFrame):
    def __init__(self, *args,
                 width: int = 100,
                 height: int = 50,
                 step_size: Union[int] = 1,
                 command: Callable = None,
                 **kwargs):
        super().__init__(*args, width=width, height=height, **kwargs)

        self.grid(pady=10, padx=10)

        self.step_size = step_size
        self.command = command

        self.configure(fg_color=("gray78", "gray28"))  # set frame color

        self.grid_columnconfigure((0, 2), weight=1)  # buttons don't expand
        self.grid_columnconfigure(1, weight=4)  # entry expands
        self.grid_rowconfigure(1, weight=1)

        self.subtract_button = CTkButton(self,
                                            text="-",
                                            width=height-6,
                                            height=height-6,
                                            fg_color = "#FF99FF",
                                            text_color = "#990099",
                                            hover_color="#FFB7FF",
                                            font=("Arial",24, "bold"),
                                            command=self.subtract_button_callback)
        self.subtract_button.grid(row=0, column=0, padx=(3, 0), pady=3, sticky="nsew")

        self.entry = CTkEntry(self, width=width-(2*height), height=height-6, border_width=0, font=("Arial",24, "bold"), justify='center' )
        self.entry.grid(row=0, column=1, columnspan=1, padx=3, pady=3, sticky="nsew")

        self.add_button = CTkButton(self, 
                                    text="+",
                                    width=height-6,
                                    height=height-6,
                                    fg_color = "#FF99FF",
                                    text_color = "#990099",
                                    hover_color="#FFB7FF",
                                    font=("Arial",24, "bold"),
                                    command=self.add_button_callback)
        self.add_button.grid(row=0, column=2, padx=(0, 3), pady=3, sticky="nsew")

        # default value
        self.entry.insert(0, "0")

    def add_button_callback(self):
        if self.command is not None:
            self.command()
        try:
            value = int(self.entry.get()) + self.step_size
            self.entry.delete(0, "end")
            self.entry.insert(0, value)
        except ValueError:
            return

    def subtract_button_callback(self):
        if self.command is not None:
            self.command()
        try:
            if int(self.entry.get()) <= 0:
                return
            else:
                value = int(self.entry.get()) - self.step_size
                self.entry.delete(0, "end")
                self.entry.insert(0, value)
        except ValueError:
            return

    def get(self) -> Union[int, None]:
        try:
            return int(self.entry.get())
        except ValueError:
            return None

    def set(self, value: int):
        self.entry.delete(0, "end")
        self.entry.insert(0, str(int(value)))