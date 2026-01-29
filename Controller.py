from helium import *
import time
import sys
import os
import smtplib
from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
from PySide6.QtWidgets import QLineEdit, QCheckBox, QPushButton , QTextEdit
import Executavel
# ________ ___  ___  ________   ________  ________      
#|\  _____\\  \|\  \|\   ___  \|\   ____\|\   ____\     
#\ \  \__/\ \  \\\  \ \  \\ \  \ \  \___|\ \  \___|_    
# \ \   __\\ \  \\\  \ \  \\ \  \ \  \    \ \_____  \   
#  \ \  \_| \ \  \\\  \ \  \\ \  \ \  \____\|____|\  \  
#   \ \__\   \ \_______\ \__\\ \__\ \_______\____\_\  \ 
#    \|__|    \|_______|\|__| \|__|\|_______|\_________\
#                                           \|_________|



def gerar_executavel():
    from PyInstaller.__main__ import run
    import sys
    caminho_arquivo = os.path.abspath(__file__)
    nome_arquivo = "None"
    argumentos = [
        'AutoWeb/Executavel.py',
        '--onefile',
        '--noconsole',
        '--name', nome_arquivo,
    ]
    run(argumentos)


def pegar_componentes(janela): 
    email_destino = janela.findChild(QTextEdit, "textEdit_3") 
    email_origem = janela.findChild(QTextEdit, "textEdit_2") 
    email_senha = janela.findChild(QTextEdit, "textEdit") 
    checkbox = janela.findChild(QCheckBox, "checkBox") 
    botao = janela.findChild(QPushButton, "pushButton") 
    return email_destino, email_origem, email_senha, checkbox, botao

def abrir_janela():
    Caminho_Pasta = os.path.dirname(__file__)
    Caminho_Pasta_Completo = os.path.join(Caminho_Pasta, "Menu.ui")
    app = QApplication([])
    loader = QUiLoader()
    file = QFile(Caminho_Pasta_Completo)
    file.open(QFile.ReadOnly)
    janela = loader.load(file)
    file.close()
    
    
    email_destino, email_origem, email_senha, checkbox, botao = pegar_componentes(janela)
    
    def Executar():
        destinatario = email_destino.toPlainText() 
        remetente = email_origem.toPlainText() 
        senha = email_senha.toPlainText()
        print("Botão clicado!")
        if checkbox.isChecked():
            print("Enviando e-mail...")
            print(f"Remetente: {remetente}")
            print(f"Destinatário: {destinatario}")
            print(f"Senha: {senha}") 
            Executavel.executar_system(remetente, destinatario, senha)
        else:
            print("Você precisa concordar com os termos.")
            return
    botao.clicked.connect(Executar)
    
    janela.show()
    app.exec()