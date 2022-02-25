import sqlite3
from tkinter import *
#from tkinter import filedialog
import tkinter.filedialog

root = Tk()

def filedialogs():
    global get_image
    get_image = tkinter.filedialog.askopenfilenames(title="SELECT IMAGE", filetypes=(("png","*.png"),("jpg","*.jpg"),("ALLfile","*.*")))

def cover_image_into_binary(filename):
    with open(filename, 'rb') as file:
        photo_image = file.read()
    return photo_image

def inser_image():
    image_database = sqlite3.connect("Image_data.db")
    data = image_database.cursor()

    for image in get_image:
        insert_photo = cover_image_into_binary(image)
        data.execute("INSERT INTO Image Values(:image)",
                 {'image': insert_photo})

    image_database.commit()
    image_database.close()

def create_database():
    image_database = sqlite3.connect("Image_data.db")
    data = image_database.cursor()

    data.execute("CREATE TABLE IF NOT EXISTS Image(Image BLOB)")

    image_database.commit()
    image_database.close()



select_image = Button(root, text="Select Image", command=filedialogs)
select_image.grid(row=0, column=0, pady=(100,0), padx= 10)

save_image = Button(root, text="Save",command=inser_image)
save_image.grid(row=1, column=0)

root.mainloop()