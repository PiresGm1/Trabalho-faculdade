import sqlite3
from tkinter import messagebox

class SistemaDeRegistro:
    def __init__(self):
        self.conn = sqlite3.connect('notas.db')
        self.c = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.c.execute('''CREATE TABLE IF NOT EXISTS notas(
                        id INTEGER PRIMARY KEY  AUTOINCREMENT,
                        nome TEXT NOT NULL,
                        email TEXT NOT NULL,
                        tel TEXT NOT NULL,
                        data_vencimento TEXT NOT NULL,
                        endereco TEXT NULL,
                        empresa TEXT NOT NULL,
                        pago TEXT NOT NULL,
                        nota TEXT NOT NULL,
                        logo TEXT NOT NULL)  ''')

    def register_notas(self, notas):
        self.c.execute("INSERT INTO notas(nome, email, tel, data_vencimento, endereco, empresa, pago,nota, logo) VALUES (?,?,?,?,?,?,?,?,?)",(notas))
        self.conn.commit()

        #mostrando mensagem de sucesso
        messagebox.showinfo('Sucesso', 'Registrado com sucesso!')

    def view_all_notas(self):
        self.c.execute("SELECT * FROM notas")
        dados = self.c.fetchall()
        return dados
    
    def search_notas(self, id):
        self.c.execute("SELECT * FROM notas WHERE id=?", (id,))
        dados = self.c.fetchone()

        return dados

        
    def update_notas(self, novo_valores):
        query = "UPDATE notas SET nome=?, email=?, tel=?, data_vencimento=?, endereco=?, empresa=?, pago=?,nota=?, logo=? WHERE id=?"
        self.c.execute(query,novo_valores)
        self.conn.commit()

        #mostrando mensagem de sucesso
        messagebox.showinfo('Sucesso', f'Nota com ID:{novo_valores[9]} foi atualizado!')

    def delete_notas(self, id):
        self.c.execute("DELETE FROM notas WHERE id=?", (id,))
        self.conn.commit()

         #mostrando mensagem de sucesso
        messagebox.showinfo('Sucesso', f'Nota com ID:{id} foi Deletado!')

# Criando um registro
sistema_de_registro = SistemaDeRegistro()

#Informacoes
#notas = ('Aline', 'aline@jls.com', '11973425904', '01/02/2026', 'Mogi', 'Mogi mobi', 'SIM', 'imagem1.png' )

#sistema_de_registro.register_notas(notas)

#ver notas
#todas_notas= sistema_de_registro.view_all_notas()

#procurar nota

#nota = sistema_de_registro.search_notas(3)

#atualizar nota
#notas = ('Aline', 'aline@jls.com', '444', '01/02/2026', 'Mogi', 'Mogi mobi', 'imagem1.png', 2)
#nota = sistema_de_registro.update_notas(notas)

#deleta nota
#sistema_de_registro.delete_notas(1)
