import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import os
import shutil

def videoflix():
    def upload_file():
        selected_format = format_combobox1.get()
        filetypes = [(f"{selected_format} Files", f"*.{selected_format.lower()}")]
        file_path = filedialog.askopenfilename(filetypes=filetypes)
        file_label.config(text="File uploaded:\n" + file_path)  # Update the label with the selected file path

    def convert_file():
        selected_format = format_combobox2.get()
        uploaded_file = file_label.cget("text").split("\n")[1]
        file_name, file_ext = os.path.splitext(uploaded_file)
        new_file = file_name + '.' + selected_format.lower()

        try:
            shutil.copy2(uploaded_file, new_file)
            save_label.config(text="File saved:\n" + new_file)  # Update the label with the saved file path
        except shutil.Error as e:
            save_label.config(text="Error occurred during save.")

    window = tk.Tk()
    window.title("Video Flix")
    window.configure(background="#ADD8E6")
    window.geometry("500x500")

    style = ttk.Style()
    style.configure("TFrame", background="#ADD8E6")
    style.configure("TLabel", background="#ADD8E6", font=("Arial", 12))
    style.configure("TButton", background="#FFD700", font=("Arial", 12, "bold"))

    formats = ["FLV", "MP4", "MKV", "AVI"]
    format_combobox1 = ttk.Combobox(window, values=formats, state="readonly")
    format_combobox1.current(0)
    format_combobox1.pack(pady=10)

    upload_button = ttk.Button(window, text="Upload", command=upload_file)
    upload_button.pack()

    file_label = ttk.Label(window, text="File uploaded: ", font=("Arial", 10))
    file_label.pack(pady=10)

    format_combobox2 = ttk.Combobox(window, values=formats, state="readonly")
    format_combobox2.pack(pady=10)

    convert_button = ttk.Button(window, text="Convert", command=convert_file)
    convert_button.pack()

    save_label = ttk.Label(window, text="File saved: ", font=("Arial", 10))
    save_label.pack(pady=10)

    window.mainloop()

if __name__ == "__main__":
    videoflix()
