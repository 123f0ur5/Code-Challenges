from tkinter import *
from pessoa import Pessoa
import tkinter.messagebox

root = Tk()

class application():
    def __init__(self):
        self.root = root
        self.my_menu = Menu(self.root)
        self.root.config(menu=self.my_menu)
        self.window()
        self.cadastro_menu()
        self.pesquisa_menu()
        root.mainloop()
    def window(self):
        self.root.title("Teste")
        self.root.geometry("400x400")
        self.root.resizable(True, True)
        self.root.maxsize(width = 700, height = 400)
        self.root.minsize(width = 400, height = 400)
    def cadastro_menu(self):
        self.cadastro_menu = Menu(self.my_menu)
        self.my_menu.add_cascade(label="Cadastro", menu=self.cadastro_menu)
        self.cadastro_menu.add_command(label="Cadastro de Usuário", command=self.cadastro_usuario)
    def cadastro_usuario(self):
        self.bt_salvar = Button(self.tela_cadastro, text="Salvar", command=self.salvar_usuario)
        self.bt_salvar.place(relx=0.8, rely=0.9, relwidth=0.2, relheight=0.1)
        self.user = Label(self.tela_cadastro, text="Nome: ")
        self.user.place(relx=0.1, rely=0.1)
        self.user_entry = Entry(self.tela_cadastro)
        self.user_entry.place(relx=0.22, rely=0.1, relwidth=0.4)
        self.age = Label(self.tela_cadastro, text="Idade: ")
        self.age.place(relx=0.1, rely=0.3)
        self.age_entry = Entry(self.tela_cadastro)
        self.age_entry.place(relx=0.22, rely=0.3, relwidth=0.4)
        self.salario = Label(self.tela_cadastro, text="Salário: ")
        self.salario.place(relx=0.1, rely=0.4)
        self.salario_entry = Entry(self.tela_cadastro)
        self.salario_entry.place(relx=0.22, rely=0.4, relwidth=0.4)
    def salvar_usuario(self):
        self.nome_cadastro = self.user_entry.get()
        self.idade_cadastro = self.age_entry.get()
        self.salario_cadastro = self.salario_entry.get()
        self.ppl = Pessoa(self.nome_cadastro, self.idade_cadastro, self.salario_cadastro)
        self.user_entry.delete(0,END)
        self.age_entry.delete(0,END)
        self.salario_entry.delete(0,END)
        tkinter.messagebox.showinfo("Usuário Cadastrado", "O usuário foi cadastrado com sucesso!")
    def pesquisa_menu(self):
        self.pesq_menu = Menu(self.my_menu)
        self.my_menu.add_cascade(label="Pesquisa", menu=self.pesq_menu)
        self.pesq_menu.add_command(label="Pesquisa de Usuário", command=self.pesquisa_usuario)
    def pesquisa_usuario(self):
        self.userq = Label(self.tela_pesquisa, text="Nome: ")
        self.userq.place(relx=0.1, rely=0.1)
        self.userq_entry = Label(self.tela_pesquisa, text= self.ppl.get_nome())
        self.userq_entry.place(relx=0.22, rely=0.1, relwidth=0.4)
        self.ageq = Label(self.tela_pesquisa, text="Idade: ")
        self.ageq.place(relx=0.1, rely=0.3)
        self.ageq_entry = Label(self.tela_pesquisa, text=self.ppl.get_idade())
        self.ageq_entry.place(relx=0.22, rely=0.3, relwidth=0.4)
        self.salarioq = Label(self.tela_pesquisa, text="Salário: ")
        self.salarioq.place(relx=0.1, rely=0.4)
        self.salarioq_entry = Label(self.tela_pesquisa, text=self.ppl.get_salario())
        self.salarioq_entry.place(relx=0.22, rely=0.4, relwidth=0.4)
    def create_menu(nome : str, title: str):
        nome = Toplevel()
        nome.title(title)
        nome.geometry("400x400")
        nome.resizable(True, True)
        nome.maxsize(width = 700, height = 400)
        nome.minsize(width = 400, height = 400)



application()