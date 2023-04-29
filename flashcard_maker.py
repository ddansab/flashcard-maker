#!/usr/bin/env python3

import os
from sys import platform
import tkinter
import tkinter.messagebox
import customtkinter
import time

from functions import get_the_werdz, intro_stuff, zheng_long_shuo, new_line_split, make_xls_worksheet

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("green")


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("又o又o Flashcard Maker")
        self.geometry(f"{1100}x{650}")
        self.update_idletasks()
        if platform == 'Darwin':
            self.iconbitmap('yoyoyo.ico')

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(
            self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(
            self.sidebar_frame, text="又o又o", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.appearance_mode_label = customtkinter.CTkLabel(
            self.sidebar_frame, text="UI Preference:", anchor="w")
        self.appearance_mode_label.grid(row=1, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(
            row=2, column=0, padx=20, pady=(10, 10))

        # create category name field
        self.entry = customtkinter.CTkEntry(
            self, placeholder_text="Enter Category Name")
        self.entry.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")

        # create textbox
        self.textbox = customtkinter.CTkTextbox(
            self, height=530, undo=True, font=('Calibri', 18))
        self.textbox.grid(row=1, column=1, padx=20, pady=0, sticky="nsew")

        # create checkbox and switch frame
        self.checkbox_slider_frame = customtkinter.CTkFrame(
            self, width=200, corner_radius=0)
        self.checkbox_slider_frame.grid(
            row=0, column=2, rowspan=4, sticky="nsew")
        self.checkbox_label = customtkinter.CTkLabel(
            self.checkbox_slider_frame, text="File Type", font=customtkinter.CTkFont(size=16, weight="bold"))
        self.checkbox_label.grid(
            row=0, column=0, pady=(20, 0), padx=10, sticky="n")
        self.pleco_checkbox = customtkinter.CTkCheckBox(
            master=self.checkbox_slider_frame, text="Pleco")
        self.pleco_checkbox.grid(row=1, column=0, pady=20, padx=10, sticky="n")
        self.excel_checkbox = customtkinter.CTkCheckBox(
            master=self.checkbox_slider_frame, text="Excel")
        self.excel_checkbox.grid(
            row=2, column=0, pady=(0, 20), padx=10, sticky="n")
        self.create_file_button = customtkinter.CTkButton(
            self.checkbox_slider_frame, command=self.sidebar_button_event, text="Create File")
        self.create_file_button.grid(row=3, column=0, padx=20, pady=10)
        self.see_files_button = customtkinter.CTkButton(
            self.checkbox_slider_frame, command=self.see_file_event, text="Open Files")
        self.see_files_button.grid(row=4, column=0, padx=20, pady=10)
        self.clear_button = customtkinter.CTkButton(
            self.sidebar_frame, command=self.clear_text_event, text="Clear Text", fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"))
        self.clear_button.grid(
            row=10, column=0, pady=(10, 20), padx=(30, 20), sticky="w")

        # set default values
        self.appearance_mode_optionemenu.set("System")

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def open_checkbox_error_event(self):
        tkinter.messagebox.showerror(
            "ERROR", "Please pick at least one file type")

    def open_textbox_error_event(self):
        tkinter.messagebox.showerror(
            "ERROR", "Either your file is empty, or you need a category name.")

    def clear_text_event(self):
        self.textbox.delete('1.0', 'end-1c')
        self.entry.delete(0, 'end')

    file_name = ""

    def open_input_filename_event(self):
        filename = customtkinter.CTkInputDialog(
            text="Type your filename:", title="Filename")
        global file_name
        file_name = filename.get_input()
        intro_stuff(file_name, self.entry.get())
        self.progressbar = customtkinter.CTkProgressBar(
            self.checkbox_slider_frame, width=100)
        self.progressbar.grid(row=5, column=0, padx=10,
                              pady=30, sticky="ew")
        self.progressbar.set(0)
        for x in range(60):
            self.progressbar.update_idletasks()
            self.progressbar.set(x/60)
            time.sleep(0.025)
        self.progressbar.grid_forget()
        self.see_files_button.configure(text="See New Files")

    def sidebar_button_event(self):
        input = self.textbox.get("1.0", 'end-1c')
        cat = self.entry.get()
        hazCom = input.find(', ')
        if not self.pleco_checkbox.get() and not self.excel_checkbox.get():
            self.open_checkbox_error_event()
        elif input == "" or cat == "":
            self.open_textbox_error_event()
        else:
            if self.pleco_checkbox.get():
                self.open_input_filename_event()
            if hazCom == -1:
                if self.pleco_checkbox.get() and self.excel_checkbox.get():
                    get_the_werdz(new_line_split(input), file_name)
                    make_xls_worksheet(new_line_split(input), cat)
                elif self.pleco_checkbox.get():
                    get_the_werdz(new_line_split(input), file_name)
                elif self.excel_checkbox.get():
                    self.progressbar = customtkinter.CTkProgressBar(
                        self.checkbox_slider_frame, width=100)
                    self.progressbar.grid(row=5, column=0, padx=10,
                                          pady=30, sticky="ew")
                    self.progressbar.set(0)
                    for x in range(60):
                        self.progressbar.update_idletasks()
                        self.progressbar.set(x/60)
                        time.sleep(0.025)
                    self.progressbar.grid_forget()
                    self.see_files_button.configure(text="See New Files")
                    make_xls_worksheet(new_line_split(input), cat)
            else:
                get_the_werdz(zheng_long_shuo(input), file_name)

    def see_file_event(self):
        if platform == 'linux' or platform == 'linux2':
            os.system('xdg-open new_files')
        elif platform == 'darwin':
            os.system('open new_files')
        elif platform == 'win32':
            os.system('start new_files')


if __name__ == "__main__":
    app = App()
    app.mainloop()
