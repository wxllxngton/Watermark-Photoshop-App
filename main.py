# import all the libraries
from tkinter import *
from PIL import Image, ImageFont, ImageDraw

FONT_NAME = 'Courier'

# ------------------------- WATERMARK MECHANISM ---------------------------- #
def watermark_text():
    im = Image.open(img_path.get())
    watermark_image = im.copy()

    draw = ImageDraw.Draw(watermark_image)
    font = ImageFont.truetype("arial.ttf", 50)

    # Add watermark - (1st tuple = Position of WM) (2nd tuple = Color)
    draw.text((0, 0), wm_path.get(),
              (0, 0, 0), font=font)

    # Saves image - Opens with image viewer where you can save the image
    watermark_image.show()
    #     C:/Users/John Ombuya/Pictures/Send to the Mrs.PNG

def watermark_img():
    # image watermark
    im = Image.open(img_path.get())
    watermark_image = im.copy()

    # Crops the image to be used as the watermark
    size = (500, 100)
    crop_image = Image.open(wm_path.get())
    crop_image.thumbnail(size)

    # Add watermark
    watermark_image.paste(crop_image, (500, 200))
    watermark_image.show()




# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Watermarks')
window.config(padx=80, pady=80)

#Canvas widget - layer things on top of another
canvas = Canvas(width=120,height=104,highlightthickness=0)
tomato_img = PhotoImage(file="C:/Users/John Ombuya/Pictures/Send to the Mrs.PNG")
canvas.create_image(60,42,image=tomato_img)
logo_text = canvas.create_text(60,55,text='Watermarks', font=(FONT_NAME,15,"bold"))
canvas.grid(column=0, row=0)

# --------------- PATH SETUP -------------- #
img_label = Label(text='Enter Path: ',  font=(FONT_NAME,12,"bold"))
img_label.grid(column=0, row=1)

# Textbox to enter path of img
img_path = Entry(width=20)
img_path.grid(column=1, row=1, columnspan=2)

# --------------- WATERMARK SETUP -------------- #
wm_label = Label(text='Watermark Text/Img URL: ', font=(FONT_NAME,12,"bold"))
wm_label.grid(column=0, row=2)

# Textbox ro be used as watermark
wm_path = Entry(width=20)
wm_path.grid(column=1, row=2, columnspan=2)

# Button to submit path for text
submit = Button(text='Apply Txt', font=(FONT_NAME,10,"bold"), command=watermark_img)
submit.grid(column=1, row=3)

# Button to submit path for img
submit_img = Button(text='Apply Img', font=(FONT_NAME,10,"bold"), command=watermark_img)
submit_img.grid(column=2, row=3)

window.mainloop()
