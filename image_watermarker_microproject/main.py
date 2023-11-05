import customtkinter as ctk
from tkinter.filedialog import askopenfile
from tkinter.filedialog import asksaveasfile
import shutil
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import os


def get_img_file(type_):
    file_path = askopenfile(mode='r', filetypes=[('Image Files', '*png')])
    if file_path is not None:
        pass
    else:
        return
    shutil.copyfile(file_path.name, f"./assets/{type_}.png")
    global target_img
    target_img = Image.open("./assets/image.png")
    img = resize_img(target_img)
    output_label.configure(image=ctk.CTkImage(
        light_image=img, size=(img.width, img.height)))
    upload_button.configure(state="disabled")
    text_watermark_entry.pack(pady=(20, 0))
    apply_button.pack(pady=(20, 0))


def resize_img(img: Image):
    base_width = 500
    wpercent = (base_width / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    img = img.resize((base_width, hsize), Image.Resampling.LANCZOS)
    return img


def enable_apply(*args):
    value = watermark_text.get()
    if len(value) == 0:
        apply_button.configure(state="disabled")
    else:
        apply_button.configure(state="enabled")


def add_text_watermark():
    watermark_image = target_img.copy()

    draw = ImageDraw.Draw(watermark_image)

    w, h = target_img.size
    x, y = int(w / 2), int(h / 2)
    if x > y:
        font_size = y
    elif y > x:
        font_size = x
    else:
        font_size = x

    font = ImageFont.truetype("arial.ttf", int(font_size/6))

    draw.text((x, y), watermark_text.get(), fill=(
        255, 255, 255), font=font, anchor='ms')

    text_watermark_entry.pack_forget()
    apply_button.pack_forget()
    img = resize_img(watermark_image)
    output_label.configure(image=ctk.CTkImage(
        light_image=img, size=(img.width, img.height)))
    save_button.pack(pady=(20, 0))
    watermark_image.save("./assets/image.png")


def save_img():
    image = Image.open("./assets/image.png")
    file = file = asksaveasfile(mode='wb', defaultextension=".png", filetypes=(
        ("PNG file", "*.png"), ("All Files", "*.*")))
    if file:
        image.save(file)

    save_button.pack_forget()
    success.pack(pady=20)


def clear_cache():
    os.remove("./assets/image.png")


app = ctk.CTk()
app.geometry("600x600")
app.title("Watermark Images")
app.resizable(False, False)

ctk.CTkLabel(app, text="Image Watermarker",
             fg_color="transparent", font=("Courier New", 25, "bold")).pack(pady=10)

output_label = ctk.CTkLabel(app, text="", width=500)
upload_button = ctk.CTkButton(
    master=app, text="Upload Image", command=lambda: get_img_file("image"))
watermark_text = ctk.StringVar()
watermark_text.trace("w", enable_apply)
text_watermark_entry = ctk.CTkEntry(
    app, placeholder_text="Enter watermark text", textvariable=watermark_text)
apply_button = ctk.CTkButton(
    app, text="Apply Watermark", state="disabled", command=add_text_watermark)
save_button = ctk.CTkButton(app, text="Save", command=save_img)
success = ctk.CTkLabel(app, text="Image Saved Successfully",
                       fg_color="transparent", font=("Courier New", 20, "bold"))

upload_button.pack(pady=(0, 20))
output_label.pack()

app.mainloop()
clear_cache()
