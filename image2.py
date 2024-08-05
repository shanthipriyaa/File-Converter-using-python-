import tkinter as tk
from tkinter import OptionMenu, filedialog
import os 
from PIL import Image



def run_image_flix():
    # Create the main window
    window = tk.Toplevel()
    window.title("Image Flix")
    window.geometry("500x500")  # Set the size of the window

    # Set the background color and font
    window.configure(bg="#ADD8E6")
    window.option_add("*Font", "Helvetica 12")

    # Custom colors
    bg_color = "#ADD8E6"
    button_bg_color = "white"
    button_border_color = "gold"

    # Dropdown menu options
    image_formats = ["gif", "jpeg", "jpg", "png", "webp"]
    selected_format_1 = tk.StringVar()
    selected_format_1.set(image_formats[0])  # Set the default value for the first dropdown

    selected_format_2 = tk.StringVar()
    selected_format_2.set(image_formats[0])  # Set the default value for the second dropdown

    # First dropdown menu widget
    dropdown_1 = OptionMenu(window, selected_format_1, *image_formats)
    dropdown_1.config(bg=bg_color)
    dropdown_1.pack(pady=10)

    # Button to upload the selected file
    def upload_file():
        filetypes = [(f"{selected_format_1.get().upper()} files", f"*.{selected_format_1.get()}")]
        file_path = filedialog.askopenfilename(filetypes=filetypes)
        if file_path:
            uploaded_file_label.configure(text=f"Uploaded File:\n{file_path}")

    upload_button = tk.Button(window, text="Upload File", command=upload_file, bg=button_bg_color, fg="black", highlightbackground=button_border_color, highlightcolor=button_border_color, highlightthickness=2)
    upload_button.pack(pady=10)

    # Label to display the uploaded file name and path
    uploaded_file_label = tk.Label(window, text="No file uploaded", bg=bg_color)
    uploaded_file_label.pack(pady=10)

    # Second dropdown menu widget
    dropdown_2 = OptionMenu(window, selected_format_2, *image_formats)
    dropdown_2.config(bg=bg_color)
    dropdown_2.pack(pady=10)

    
    # Function to convert the uploaded image
    def convert_image():
        file_path = uploaded_file_label.cget("text").split("\n")[1]
        output_format = selected_format_2.get()

        if file_path and output_format != selected_format_1.get():
            try:
                # Open the uploaded image
                image = Image.open(file_path)

                # Convert the image format
                converted_image = image.convert("RGB")  # Convert to RGB format

                # Save the converted image in the same directory as the uploaded file
                file_directory, file_name = os.path.split(file_path)
                converted_file_path = os.path.join(file_directory, f"converted_image.{output_format}")
                converted_image.save(converted_file_path)

                print("Image converted and saved successfully.")
            except Exception as e:
                print("Error converting the image:", str(e))
        else:
            print("Invalid conversion parameters.")

    convert_button = tk.Button(window, text="Convert", command=convert_image, bg=button_bg_color, fg="black", highlightbackground=button_border_color, highlightcolor=button_border_color, highlightthickness=2)
    convert_button.pack(pady=10)

    # Run the main loop
    window.mainloop()
