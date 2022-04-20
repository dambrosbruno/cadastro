from PyQt5 import uic, QtWidgets
import sqlite3

app = QtWidgets.QApplication([])
sc_cadastro = uic.loadUi("gui_cadastro.ui")

def cadastrar():
    nome = sc_cadastro.lineEdit_1.text()
    cpf = sc_cadastro.lineEdit_2.text()
    email = sc_cadastro.lineEdit_3.text()
    rua = sc_cadastro.lineEdit_4.text()
    nascimento = sc_cadastro.dateEdit_5.text()
    whatsapp = sc_cadastro.lineEdit_6.text()
    senha = sc_cadastro.lineEdit_7.text()
    c_senha = sc_cadastro.lineEdit_8.text()

    print('Nome: ', nome)
    print('CPF: ', cpf)
    print('Email: ', email)
    print('Rua: ', rua)
    print('Nascimento: ', nascimento)
    print('Whatsapp: ', whatsapp)
    print('Senha: ', senha)

    banco = sqlite3.connect('db_cadastro.db')
    cursor = banco.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS tb_cadastro (nome text, cpf text, email text, rua text, nascimento datetime, whatsapp integer, senha text)")

    if (senha == c_senha):
        cursor.execute("INSERT INTO tb_cadastro VALUES ('"+nome+"', '"+cpf+"', '"+email+"', '"+rua+"', '"+nascimento+"', '"+whatsapp+"', '"+senha+"')")
        banco.commit()
        banco.close()
        sc_cadastro.label_12.setText("Cadastro feito com sucesso")
    else:
        sc_cadastro.label_12.setText("As senhas digitadas são diferentes")

sc_cadastro.pushButton.clicked.connect(cadastrar)

sc_cadastro.show()
app.exec()