import requests, os, sys, json, colorama
from colorama import Fore
from PIL import Image as Img
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter import messagebox

PROGRAM = 'Instagram Caption Poster'
VERSION = '1.0'
AUTHOR  = 'Abdullah Bashar & Ahmed'

class User:
	def __init__(self):
		self.root = Tk()
		self.import_image = Button(self.root, text="Import Image", command=self.image_choose)
		self.img_txt = StringVar()
		self.img_label = Label(self.root, textvariable=self.img_txt)
		self.cap_label = Label(self.root, text="Caption:")
		self.caption = Text(self.root, height=1.5, width=25)
		self.submit = Button(self.root, text="Submit", command=self.submit)
		self.filename = None

	def runGui(self):
		print("[{}] Initializing [{}]..".format(Fore.BLUE + "+" + Fore.RESET, "GUI"))
		self.root.title(PROGRAM)
		self.root.geometry("235x220")
		self.img_txt.set("")
		# self.root.config()
		self.import_image.grid(column=1, row=0, ipadx=60, padx=15, pady=(35, 0))
		self.img_label.grid(column=1, row=2)
		self.cap_label.grid(column=1, row=3)
		self.caption.grid(column=1, row=4)
		self.submit.grid(column=1, row=5, pady=15)
		# self.root

		self.root.resizable(0, 0)  
		self.root.mainloop()

	def image_choose(self):
		print("[{}] Selecting Image..".format(Fore.GREEN + "!" + Fore.RESET))
		ftypes = [
			('Image files', '*.img;*.png;*.jpeg'), 
			('Video files', '*.mp4;*.mov'),
		]

		self.filename = askopenfilename(filetypes=ftypes)
		if self.filename is not "":
			print("[{}] Image selected [{}]".format(Fore.BLUE + "+" + Fore.RESET, self.filename))
		else:
			print("[{}] Selection cancelled.".format(Fore.RED + "-" + Fore.RESET))
		self.img_txt.set(self.filename )

	def submit(self):
		print("SUBMIT: Making the image...")
		self.submit['state'] = 'disabled'
		img = Img.open(self.filename, 'r')
		img_w, img_h = img.size
		border = 50
		background = Img.new('RGBA', (img_w+border, int(img_h+border*1.5)), (255, 255, 255, 255))
		bg_w, bg_h = background.size
		offset = ((border//2) , int((border+10)))
		background.paste(img, offset)
		background.save('out.png')


		# messagebox.showinfo("Output", "Are you ok with this ?")

		self.submit['state'] = 'normal'

()

def import_image(img):
	pass


def main():
	print("[{}] Initializing [{} v{}]..".format(Fore.BLUE + "+" + Fore.RESET, PROGRAM,VERSION))
	usr = User()
	usr.runGui()

try:
	main()
except Exception as e:
	print(e)