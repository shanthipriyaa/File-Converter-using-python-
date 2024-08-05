import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import os

def open_img():
    root = tk.Toplevel()
    root.title("Image Formatter")
    root.geometry("500x500")
    root.configure(bg="#ADD8E6")

    def open_image():
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.gif;*.jpg;*.jpeg;*.png;*.webp")])
        if file_path:
            _, file_extension = os.path.splitext(file_path)
            allowed_extensions = ['.gif', '.jpg', '.jpeg', '.png', '.webp']
            if file_extension.lower() in allowed_extensions:
                image = Image.open(file_path)
                image.thumbnail((400, 400))
                photo = ImageTk.PhotoImage(image)
                image_label.configure(image=photo)
                image_label.image = photo  # Store the reference to the image
                path_label.configure(text="Image Path: " + file_path)

                format_variable.set(file_extension[1:].upper())
                format_dropdown['menu'].delete(0, tk.END)
                for extension in allowed_extensions:
                    if extension.lower() != file_extension.lower():
                        format_dropdown['menu'].add_command(
                            label=extension[1:].upper(),
                            command=tk._setit(format_variable, extension[1:].upper())
                        )
            else:
                path_label.configure(text="Invalid file format!")
                format_variable.set("")

    upload_button = tk.Button(root, text="Upload Image", command=open_image, bg="white", fg="black", padx=10, pady=5)
    upload_button.pack(pady=10)

    
    image_label = tk.Label(root)
    image_label.pack()

    path_label = tk.Label(root, text="Image Path: ", bg="#ADD8E6", fg="black", font=("Arial", 12))
    path_label.pack(pady=5)

    format_label = tk.Label(root, text="Image Format:", bg="#ADD8E6", fg="black", font=("Arial", 12))
    format_label.pack()

    format_variable = tk.StringVar(root)
    format_dropdown = tk.OptionMenu(root, format_variable, "GIF", "JPG", "PNG", "WEBP")
    format_dropdown.configure(bg="white", fg="black", padx=10, pady=5)
    format_dropdown.pack()

    

    def convert_image():
        file_path = path_label.cget("text")[12:]
        _, file_extension = os.path.splitext(file_path)
        selected_format = format_variable.get()

        save_path = filedialog.asksaveasfilename(
            defaultextension=selected_format.lower(),
            filetypes=[("Image files", f"*.{selected_format.lower()}")]
        )

        if save_path:
            try:
                image = Image.open(file_path)

                if selected_format == "GIF":
                    converted_image = image.convert("P", dither=Image.NONE, palette=Image.WEB)
                elif selected_format == "JPG" or selected_format == "JPEG":
                    converted_image = image.convert("RGB")
                elif selected_format == "PNG":
                    converted_image = image.convert("RGBA")
                elif selected_format == "WEBP":
                    converted_image = image

                converted_image.save(save_path, format=selected_format.lower())

                path_label.configure(text="Image Path: " + save_path)
                open_image()
            except Exception as e:
                path_label.configure(text="Conversion Failed!")
                print(f"Error converting image: {e}")

    
    convert_button = tk.Button(root, text="Convert", command=convert_image, bg="white", fg="black", padx=10, pady=5)
    convert_button.pack(pady=10)

    root.mainloop()

