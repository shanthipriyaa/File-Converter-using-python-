import tkinter as tk
import os 
from PIL import ImageTk, Image
from tkinter import filedialog
from tkinter import ttk

def create_doc():
    dwin = tk.Toplevel()
    dwin.geometry("400x300")
    dwin.configure(bg="#E8F0F8")
    dwin.title("Document Flix")
# Create the "Upload" button
    def upload_file():

        format_mappings = {
        "DOCX": ["DOC", "HTML", "TXT"],
        "TXT": ["DOC", "DOCX", "HTML", "PDF"],
        "PDF": ["DOC", "DOCX", "TXT"],
        "HTML": ["DOC"],
        "DOC": ["HTML", "PDF", "TXT"]
}

        file_path = filedialog.askopenfilename()
        file_extension = file_path[file_path.rfind(".")+1:].upper()

        if file_extension in format_mappings:
            file_label.config(text="Uploaded file: " + file_path)
            format_dropdown["values"] = format_mappings[file_extension]
            format_dropdown.current(0)
        else:
            file_label.config(text="Unsupported file format!")

    upload_button = tk.Button(dwin, text="Upload", command=upload_file)
    upload_button.pack(pady=10)
# Create the label to display the uploaded file path
    file_label = tk.Label(dwin, text="Uploaded file: ")
    file_label.pack()
# Create the dropdown box for formats
    format_label = tk.Label(dwin, text="Select a format:")
    format_label.pack()
    selected_format = tk.StringVar()
    format_dropdown = ttk.Combobox(dwin, textvariable=selected_format, values=[], state="readonly")
    format_dropdown.pack()
# Create the "Convert" button
    convert_button = tk.Button(dwin, text="Convert")
    convert_button.pack(pady=10)
# Run the main event loop
    dwin.mainloop()
