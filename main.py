import requests, os, sys, json, colorama, PIL
from tkinter import *
from tkinter.filedialog import askopenfilename

class workers:
	def __init__(self, action):
		self.action = None

	def import_image(self, action):
		print(self.action)

class User:
	def __init__(self):
		self.root = Tk()
		self.button = Button(self.root, text="Choose Image..", command=self.image_choose)
		self.img_txt = StringVar()
		self.img_txt.set("...")
		self.img_label = Label(self.root, textvariable=self.img_txt)
		self.cap_label = Label(self.root, text="Caption:")
		self.caption = Text(self.root, height=2, width=30)

	def runGui(self):
		self.root.title("Welcome to IG-Poster app")
		self.root.geometry("500x200")
		self.button.grid(column=0, row=0)
		self.img_label.grid(column=1, row=0)
		self.cap_label.grid(column=1, row=1)
		self.caption.grid(column=1, row=3)

		self.root.mainloop()

	def image_choose(self):
		ftypes = [
			('Image files', '*.img;*.png;*.jpeg'), 
			('Video files', '*.mp4;*.mov'),
		]

		filename = askopenfilename(filetypes=ftypes)
		self.img_txt.set(filename)


def import_image(img):
	pass


def main():
	print("Running IG-Poster")
	usr = User()
	usr.runGui()

try:
	main()
except e:
	pass