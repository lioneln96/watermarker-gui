import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageDraw, ImageTk, ImageFont

image = None

def upload_image():
    global image
    file_path = filedialog.askopenfilename()
    if file_path:
        img = Image.open(file_path)
        img.thumbnail((500, 500))
        image = img  # Update the global image variable
        photo = ImageTk.PhotoImage(image)
        canvas.delete("all")
        canvas.create_image(0, 0, anchor="nw", image=photo)
        canvas.image = photo

def add_watermark():
    global image
    if not image:
        messagebox.showinfo("No Image", "Please upload an image first.")
        return

    watermark_text = "Lionel's Watermark"
    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default()
    text_bbox = draw.textbbox((0, 0), watermark_text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    x = image.width - text_width - 10
    y = image.height - text_height - 10
    draw.text((x, y), watermark_text, fill=(255, 255, 255), font=font)

    photo = ImageTk.PhotoImage(image)
    canvas.delete("all")
    canvas.create_image(0, 0, anchor="nw", image=photo)
    canvas.image = photo


window = tk.Tk()
window.title("Image Watermarker")
window.config(padx=15, pady=15, background="grey")

canvas = tk.Canvas(window, width=500, height=500, background="grey", highlightbackground="grey")
canvas.grid(row=0, column=0, columnspan=2)

upload_btn = tk.Button(window, text="Upload Image", command=upload_image, borderwidth=0, highlightbackground="grey")
upload_btn.grid(row=1, column=0, padx=5, pady=5)

watermark_btn = tk.Button(window, text="Add Watermark", command=add_watermark, borderwidth=0, highlightbackground="grey")
watermark_btn.grid(row=1, column=1, padx=5, pady=5)

window.mainloop()
