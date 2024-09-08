#mportando dependencias do Tkinter
from tkinter.ttk import *
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog as fd

#importando pillow
from PIL import ImageTk, Image

#tk calendar
from tkcalendar import Calendar, DateEntry
from datetime import date

#importando o main
from main import *

#cores
co0 = "#2e2d2b"  # Preta
co1 = "#feffff"  # Branca   
co2 = "#e5e5e5"  # grey
co3 = "#00a095"  # Verde
co4 = "#403d3d"   # letra
co6 = "#003452"   # azul
co7 = "#ef5350"   # vermelha

co6 = "#FFFF00"   # amarelo
co8 = "#263238"   # + verde
co9 = "#e9edf5"   # + verde

# Criando janela
janela = Tk()
janela.title("")
janela.geometry('860x535')
janela.configure(background=co1)
janela.resizable(width=FALSE, height=FALSE)

style = Style(janela)
style.theme_use("clam")

#Criando Frames
# Criando Frames
frame_logo = Frame(janela, width=850, height=52, bg=co6)
frame_logo.grid(row=0, column=0, pady=0, padx=0, sticky=NSEW, columnspan=5)

frame_botoes = Frame(janela, width=100, height=200, bg=co1, relief=RAISED)
frame_botoes.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

frame_detalhes = Frame(janela, width=800, height=100, bg=co1, relief=SOLID)
frame_detalhes.grid(row=1, column=1, pady=1, padx=10, sticky=NSEW)

frame_tabela = Frame(janela, width=800, height=100, bg=co1, relief=SOLID)
frame_tabela.grid(row=3, column=0, pady=0, padx=10, sticky=NSEW, columnspan=5)

# Trabalhando no frame logo ------------------------------------
global imagem, imagem_string, l_imagem

app_lg = Image.open('imagens/logo.png')
app_lg = app_lg.resize((50,50))
app_lg = ImageTk.PhotoImage(app_lg)
app_logo = Label(frame_logo, image=app_lg, text="  Sistema de Registro de Notas", width=850, compound=LEFT, anchor=NW, font=('Verdana 25'), bg=co6, fg=co0)
app_logo.place(x=5, y=0)

#abrindo imagem

imagem = Image.open('imagens/logo.png')
imagem = imagem.resize((130,130))
imagem = ImageTk.PhotoImage(imagem)
l_imagem = Label(frame_detalhes, image=imagem,  bg=co1, fg=co4)
l_imagem.place(x=390, y=10)



#criando as funçoes para o CRUD

#funçao par poder adicionar
def adicionar ():
	global imagem, imagem_string, l_imagem

	#obtendo os valores
	nome=e_nome.get()
	email = e_email.get()
	tel = e_tel.get()
	pago = c_pago.get()
	data = data_vencimento.get()
	endereco = e_endereco.get()
	empresa = e_empresa.get()
	numero= e_numero.get()
	img = 'imagens/logo.png'

	lista = [nome, email, tel, pago, data, endereco, empresa, numero, img]

	# verificando se a lista tem algum valor vazio

	for i in lista:
		if i=='':
			messagebox.showerror('Erro','Preencha todos os campos')
			return

	# registrando os valores

	sistema_de_registro.register_notas(lista)

	#deletando os campos de entrada

	e_nome.delete(0,END)
	e_email.delete(0,END)
	e_tel.delete(0,END)
	c_pago.delete(0,END)
	data_vencimento.delete(0,END)
	e_endereco.delete(0,END)
	e_empresa.delete(0,END)
	e_numero.delete(0,END)

	#mostrando os valores na tabela
	
	mostrar_notas()

#função para poder procurar
def procurar():
	global imagem, imagem_string, l_imagem

	#pegando o id
	id_nota = int(e_procurar.get())

	#procurando a nota
	dados = sistema_de_registro.search_notas(id_nota)

	#deletando os campos de entrada

	e_nome.delete(0,END)
	e_email.delete(0,END)
	e_tel.delete(0,END)
	c_pago.delete(0,END)
	data_vencimento.delete(0,END)
	e_endereco.delete(0,END)
	e_empresa.delete(0,END)
	e_numero.delete(0,END)

	#inserindo valores nos campos de entrada

	e_nome.insert(END,dados[1])
	e_email.insert(END,dados[2])
	e_tel.insert(END,dados[3])
	c_pago.insert(END,dados[4])
	data_vencimento.insert(END,dados[5])
	e_endereco.insert(END,dados[6])
	e_empresa.insert(END,dados[7])
	e_numero.insert(END,dados[8])

#funçao par poder atualizar
def atualizar ():
	global imagem, imagem_string, l_imagem



	#pegando o id
	id_nota = int(e_procurar.get())

	#obtendo os valores
	nome=e_nome.get()
	email = e_email.get()
	tel = e_tel.get()
	pago = c_pago.get()
	data = data_vencimento.get()
	endereco = e_endereco.get()
	empresa = e_empresa.get()
	numero= e_numero.get()
	img = 'imagens/logo.png'

	lista = [nome, email, tel, pago, data, endereco, empresa,numero, img, id_nota]

	# verificando se a lista tem algum valor vazio

	for i in lista:
		if i=='':
			messagebox.showerror('Erro','Preencha todos os campos')
			return

	# registrando os valores


	sistema_de_registro.update_notas(lista)

	#deletando os campos de entrada

	e_nome.delete(0,END)
	e_email.delete(0,END)
	e_tel.delete(0,END)
	c_pago.delete(0,END)
	data_vencimento.delete(0,END)
	e_endereco.delete(0,END)
	e_empresa.delete(0,END)
	e_numero.delete(0,END)

	#mostrando os valores na tabela
	
	mostrar_notas()

#função que deleta
def deletar ():
	global imagem, imagem_string, l_imagem



	#pegando o id
	id_nota = int(e_procurar.get())

	#deletando o aluno

	sistema_de_registro.delete_notas(id_nota)

	#deletando os campos de entrada

	e_nome.delete(0,END)
	e_email.delete(0,END)
	e_tel.delete(0,END)
	c_pago.delete(0,END)
	data_vencimento.delete(0,END)
	e_endereco.delete(0,END)
	e_empresa.delete(0,END)
	e_numero.delete(0,END)

	e_procurar.delete(0,END)

	#mostrando os valores na tabela
	
	mostrar_notas()







#Criando os campos de entrada

l_nome = Label(frame_detalhes, text="Nome *", anchor=NW, font=('ivy 10'), bg=co1, fg=co4)
l_nome.place(x=4, y=10)
e_nome = Entry(frame_detalhes, width=30, justify='left', relief='solid')
e_nome.place(x=7, y=40)

l_email = Label(frame_detalhes, text="Email *", anchor=NW, font=('ivy 12'), bg=co1, fg=co4)
l_email.place(x=4, y=70)
e_email = Entry(frame_detalhes, width=30, justify='left', relief='solid')
e_email.place(x=7, y=100)

l_tel = Label(frame_detalhes, text="Telefone *", anchor=NW, font=('ivy 10'), bg=co1, fg=co4)
l_tel.place(x=4, y=130)
e_tel = Entry(frame_detalhes, width=15, justify='left', relief='solid')
e_tel.place(x=7, y=160)

l_pago = Label(frame_detalhes, text="Pagamento *", anchor=NW, font=('ivy 10'), bg=co1, fg=co4)
l_pago.place(x=127, y=130)
c_pago = ttk.Combobox(frame_detalhes, width=13, font=('Ivy 8 bold'), justify='center')
c_pago['values'] = ('Pago','A Receber')
c_pago.place(x=130, y=160)

l_data_vencimento = Label(frame_detalhes, text="Data de vencimento *", anchor=NW, font=('ivy 10'), bg=co1, fg=co4)
l_data_vencimento.place(x=220, y=10)
data_vencimento = DateEntry(frame_detalhes, width=18, justify='center', background='darkblue', foreground='white', borderwidth=2, year=2024)
data_vencimento.place(x=224, y=40)

l_endereco = Label(frame_detalhes, text= "Endereço *", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_endereco.place(x=220, y=70)
e_endereco = Entry(frame_detalhes, width=15, justify='left', relief='solid')
e_endereco.place(x=224, y=100)

l_empresa = Label(frame_detalhes, text= "Empresa *", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_empresa.place(x=250, y=130)
e_empresa = Entry(frame_detalhes, width=17, justify='left', relief='solid')
e_empresa.place(x=250, y=160)

l_numero = Label(frame_detalhes, text= "Nota *", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_numero.place(x=400, y=150)
e_numero = Entry(frame_detalhes, width=13, justify='left', relief='solid')
e_numero.place(x=400, y=180)




#função para escolher a logo

def escolher_logo():
    global imagem, imagem_string, l_imagem

    imagem = fd.askopenfilename()
    imagem_string=imagem

    imagem = Image.open(imagem)
    imagem = imagem.resize((130,130))
    imagem = ImageTk.PhotoImage(imagem)
    l_imagem = Label(frame_detalhes, image=imagem,  bg=co1, fg=co4)
    l_imagem.place(x=390, y=10)

    
# Tabela notas
def mostrar_notas():

	
	list_header = ['id','Nome','email',  'Telefone','Pagamento','Vencimento', 'Endereço','Empresa','Numero da nota']

	# ver todas as notas
	df_list = sistema_de_registro.view_all_notas()

	tree_notas = ttk.Treeview(frame_tabela, selectmode="extended",columns=list_header, show="headings")

	# barra de rolagem vertival
	vsb = ttk.Scrollbar(frame_tabela, orient="vertical", command=tree_notas.yview)
	# barra de rolavem horizontal
	hsb = ttk.Scrollbar(frame_tabela, orient="horizontal", command=tree_notas.xview)

	tree_notas.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
	tree_notas.grid(column=0, row=1, sticky='nsew')
	vsb.grid(column=1, row=1, sticky='ns')
	hsb.grid(column=0, row=2, sticky='ew')
	frame_tabela.grid_rowconfigure(0, weight=12)

	hd=["nw","nw","nw","center","center","center","center","center","center", "center"]
	h=[40,120,150,70,80,80,90,100,100,100]
	n=0

	for col in list_header:
		tree_notas.heading(col, text=col.title(), anchor=NW)
		# adjust the column's width to the header string
		tree_notas.column(col, width=h[n],anchor=hd[n])

		n+=1

	for item in df_list:
		tree_notas.insert('', 'end', values=item)

# Procurar nota -----------

frame_procurar = Frame(frame_botoes, width=40, height=50, bg=co1, relief=RAISED)
frame_procurar.grid(row=0, column=0, pady=10, padx=10, sticky=NSEW)

l_nome = Label(frame_procurar, text="Procurar Nota [ Coloque o ID ]", height=1,anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_nome.grid(row=0, column=0, pady=10, padx=0, sticky=NSEW)
e_procurar = Entry(frame_procurar, width=5, justify='center',relief="solid",font=('Ivy 10'))
e_procurar.grid(row=1, column=0, pady=10, padx=0, sticky=NSEW)

botao_procurar = Button(frame_procurar,command=procurar, anchor=CENTER, text="Procurar", width=9, overrelief=RIDGE,  font=('ivy 7 bold'),bg=co1, fg=co0 )
botao_procurar.grid(row=1, column=1, pady=10, padx=0, sticky=NSEW)

# Botoes --------------------

app_img_adicionar = Image.open('imagens/add.png')
app_img_adicionar = app_img_adicionar.resize((25,25))
app_img_adicionar = ImageTk.PhotoImage(app_img_adicionar)
app_adicionar = Button(frame_botoes,command=adicionar, image=app_img_adicionar, text=" Adicionar", width=100, compound=LEFT, relief=GROOVE, overrelief=RIDGE, font=('Ivy 11'), bg=co1, fg=co0)
app_adicionar.grid(row=1, column=0, pady=5, padx=10, sticky=NSEW)

app_img_atualizar = Image.open('imagens/atualizar.png')
app_img_atualizar = app_img_atualizar.resize((25,25))
app_img_atualizar = ImageTk.PhotoImage(app_img_atualizar)
app_atualizar = Button(frame_botoes,command=atualizar, image=app_img_atualizar, text=" Atualizar", width=100, compound=LEFT, relief=GROOVE, overrelief=RIDGE, font=('Ivy 11'), bg=co1, fg=co0)
app_atualizar.grid(row=2, column=0, pady=5, padx=10, sticky=NSEW)

app_img_deletar = Image.open('imagens/deleta.png')
app_img_deletar = app_img_deletar.resize((25,25))
app_img_deletar = ImageTk.PhotoImage(app_img_deletar)
app_deletar = Button(frame_botoes,command=deletar, image=app_img_deletar, text=" Deletar", width=100, compound=LEFT, relief=GROOVE, overrelief=RIDGE, font=('Ivy 11'), bg=co1, fg=co0)
app_deletar.grid(row=3, column=0, pady=5, padx=10, sticky=NSEW)

# linha separatoria ---------------------------------------------------

l_linha = Label(frame_botoes, relief=GROOVE, text='h', width=1, height=123, anchor=NW, font=('Ivy 1'), bg=co1, fg=co0)
l_linha.place(x=260, y=15)



#chamar tabela

mostrar_notas()

janela.mainloop()
