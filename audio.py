import tkinter as tk
from tkinter import OptionMenu, filedialog
import os
from pydub import AudioSegment

def run_audio_flix():
    # Create the Audio Flix window as a Toplevel window
    window = tk.Toplevel()

    # Set the window size
    window.geometry("500x250")

    # Set the window background color
    window.configure(bg="#f0f0f0")

    # Set the window title
    window.title("Audio Flix")

    # Define the available options
    options = ["AAC", "M4R", "MP3", "OGG", "WAV"]

    # Create a variable to hold the selected option for the first dropdown
    selected_option1 = tk.StringVar(window)
    selected_option1.set(options[0])  # Set the default option

    # Create the first dropdown box
    dropdown1 = OptionMenu(window, selected_option1, *options)
    dropdown1.configure(width=10)
    dropdown1.pack(pady=10)

    # Function to handle the upload button click event
    def upload_file():
        file_format = selected_option1.get()
        filetypes = [(f"{file_format.upper()} Files", f"*.{file_format.lower()}")]
        file_path = filedialog.askopenfilename(filetypes=filetypes)
        if file_path:
            file_label.config(text=f"Selected file: {file_path}")
            # Store the uploaded file path
            window.file_path = file_path

    # Create the upload button
    upload_button = tk.Button(window, text="Upload", command=upload_file, width=10)
    upload_button.pack()

    # Create the label to display the file path
    file_label = tk.Label(window, text="No file selected", bg="#f0f0f0", pady=10)
    file_label.pack()

    # Create a variable to hold the selected option for the second dropdown
    selected_option2 = tk.StringVar(window)
    selected_option2.set(options[0])  # Set the default option

    # Create the second dropdown box
    dropdown2 = OptionMenu(window, selected_option2, *options)
    dropdown2.configure(width=10)
    dropdown2.pack(pady=10)

    # Function to handle the convert button click event
    def convert_file():
        target_format = selected_option2.get()
        if hasattr(window, "file_path"):
            file_path = window.file_path
            file_name, file_ext = os.path.splitext(file_path)
            converted_file_path = os.path.join(os.path.dirname(file_path), f"{file_name}.{target_format.lower()}")
            try:
                audio = AudioSegment.from_file(file_path, format=file_ext[1:])  # Remove the leading dot from the file extension
                audio.export(converted_file_path, format=target_format.lower())
                file_label.config(text="Conversion successful!", fg="green")
            except Exception as e:
                file_label.config(text="Error converting file!", fg="red")
                print(f"Error converting file: {str(e)}")

    # Create the convert button
    convert_button = tk.Button(window, text="Convert", command=convert_file, width=10)
    convert_button.pack(pady=10)
