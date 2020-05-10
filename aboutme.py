from tkinter import messagebox as tmsg

class Mydetails:
	def __init__(self):
		self.info = "My name is Sritiman Adak and I am currently pursuing Btech degree in Computer Science Engineering Techno Main Salt Lake ,Kolkata. My home town is Kolkata.\nThis project is not a part of my course curriculum.The tools that are used to make this project, I have learnt them from Youtube , and some some popular internet websites."
	def show(self, label):
		tmsg.showinfo(label,self.info)	