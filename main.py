import requests, os, sys, json, colorama
from PIL import Image as Img
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter import messagebox

class workers:
	def __init__(self, action):
		self.action = None

	def import_image(self, action):
		print(self.action)

class User:
	def __init__(self):
		print("INIT: Initialization the user properties..")
		self.root = Tk()
		self.button = Button(self.root, text="Choose Image..", command=self.image_choose)
		self.img_txt = StringVar()
		self.img_label = Label(self.root, textvariable=self.img_txt)
		self.cap_label = Label(self.root, text="Caption:")
		self.caption = Text(self.root, height=2, width=30)
		self.submit = Button(self.root, text="Submit...", command=self.submit)
		self.filename = None

	def runGui(self):
		print("RUNGUI: Rendering the page")
		self.root.title("Welcome to IG-Poster app")
		self.root.geometry("500x200")
		self.img_txt.set("...")
		self.button.grid(column=0, row=0)
		self.img_label.grid(column=1, row=0)
		self.cap_label.grid(column=1, row=1)
		self.caption.grid(column=1, row=3)
		self.submit.grid(column=1, row=4)

		self.root.mainloop()

	def image_choose(self):
		print("IMAGE_CHOOSE: Selecting...")
		ftypes = [
			('Image files', '*.img;*.png;*.jpeg'), 
			('Video files', '*.mp4;*.mov'),
		]

		self.filename = askopenfilename(filetypes=ftypes)
		print("IMAGE_CHOOSE: Selected: {}".format(self.filename ))
		self.img_txt.set(self.filename )

	def submit(self):
		print("SUBMIT: Making the image...")
		self.submit['state'] = 'disabled'
		img = Img.open(self.filename, 'r')
		img_w, img_h = img.size
		background = Img.new('RGBA', (img_w+50, img_h+50), (255, 255, 255, 255))
		bg_w, bg_h = background.size
		offset = (bg_w // 28, bg_h // 28)
		background.paste(img, offset)
		background.save('out.png')


		messagebox.showinfo("Output", "Are you ok with this ?")

		self.submit['state'] = 'normal'



def import_image(img):
	pass


def main():
	print("MAIN: Running IG-Poster")
	print("MAIN: Calling the User options")
	usr = User()
	usr.runGui()

try:
	main()
except e:
	pass