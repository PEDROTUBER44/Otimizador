from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont
import os
import platform

root = Tk()
#icon =


class Aplication():
	def __init__(self):
		self.root = root
		self.janela()
		self.frames_da_tela()
		self.conteudo()
		root.mainloop()
	
	def janela(self):
		self.root.title("Otimizador")
		self.root.configure(background='#5F9EA0')
		self.root.geometry("400x300")
		self.root.resizable(True, True)
		self.root.maxsize(width=450, height=350)
		self.root.minsize(width=350, height=250)
	

	def frames_da_tela(self):
		self.frame = Frame(self.root, height=15, width=100, background="#3B759B")
		self.frame.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.98)

	def conteudo(self):
		self.label = Label(self.root, text="Esse otimizador fará em seu pc:",background="#3B759B")
		self.label.place(relx=0.01, rely=0.01, relwidth=0.53, relheight=0.1)

		self.label = Label(self.root, text="-Limpará as pastas temporarias",background="#3B759B")
		self.label.place(relx=0.01, rely=0.1, relwidth=0.55, relheight=0.1)

		self.label = Label(self.root, text="-Limpara a cache da memoria ram",background="#3B759B")
		self.label.place(relx=0.01, rely=0.2, relwidth=0.59, relheight=0.1)

		self.label = Label(self.root, text="-E atualizará o seu sistema",background="#3B759B")
		self.label.place(relx=0.01, rely=0.3, relwidth=0.47, relheight=0.1)
		
		def Logs_bash():
			step()
			os.system("sudo apt update")
			step()
			os.system("sudo apt upgrade -y")
			step()
			os.system("sudo apt autoremove -y")
			step()
			os.system("sudo apt autoclean -y")
			step()
			os.system("history -c")
			step()
			os.system("su ; sudo echo 1 > /proc/sys/vm/drop_caches")
			step()
			os.system("sudo swapoff -a && sudo swapon -a")
			step()
			os.system("rm -rf /home/$USER/.cache/*")
			step()
			os.system("sudo rm -rf /home/$USER/.cache/*")
			step()
			
		fontStyle = tkFont.Font(family="Lucida Grande", size=20)
		self.bt_iniciar = Button(self.frame, text="Limpar", font=fontStyle, background="#3B759B",command=Logs_bash)
		self.bt_iniciar.place(relx=0.26, rely=0.5, relwidth=0.5, relheight=0.3)

Aplication()