🖥️ AutoPrinter — Versão Executável
O AutoPrinter é um projeto desenvolvido durante a Semana Python com foco em automação.
Ele foi pensado para simplificar processos repetitivos, permitindo que o usuário rode o programa em formato executável (.exe) sem precisar ter o Python instalado.

📂 Estrutura do Projeto
main.py → Ponto de entrada do sistema.

Controller.py → Contém a lógica principal e integração com interface.

Menu.ui → Interface gráfica criada no Qt Designer.

Executavel.py  / ExecutavelGerado.py → Scripts auxiliares para empacotamento com PyInstaller.

dist/ → Pasta onde o executável final é gerado.

🛠️ Bibliotecas utilizadas
os / sys / shutil → Manipulação de arquivos, pastas e execução.

time → Controle de cronômetro e delays.

pyautogui → Automação de captura de tela e interação.

smtplib / email.mime → Envio de e-mails com anexos.

PySide6 (Qt) → Interface gráfica (Menu.ui).

PyInstaller → Geração do executável .exe.

⚙️ Como usar
Clone o repositório:

bash
git clone https://github.com/GustavoABA/AutoPrinter.git
cd AutoPrinter
Instale as dependências:

bash
pip install pyautogui PySide6
pip install pyinstaller
Configuração de e-mail (se aplicável):

Ative a verificação em duas etapas no Gmail.

Gere uma senha de aplicativo em Configurações de Segurança do Google.

Substitua no código:

python
server.login("seuemail@gmail.com", "SENHA_DE_APLICATIVO")
Execute o projeto diretamente:

bash
python main.py
📦 Gerando o executável
Para compilar o projeto em um .exe:

bash
pyinstaller main.py --onefile --noconsole --name AutoPrinter --add-data "Menu.ui;."
O executável será gerado em dist/AutoPrinter.exe.

O parâmetro --add-data garante que o arquivo Menu.ui seja incluído no pacote.

🔄 Fluxo do Programa
O usuário abre a interface gráfica (Menu.ui).

Insere dados como remetente, destinatário e senha de aplicativo.

O sistema captura tela ou processa arquivos conforme configurado.

O resultado é enviado automaticamente por e-mail.

O programa pode ser configurado para iniciar junto com o sistema.

📝 Observação
Por falta de tempo, a pasta Executavel foi criada com auxílio da IA Copilot, que automatizou a geração do script responsável por compilar e organizar o executável.
Isso acelerou o desenvolvimento sem comprometer a lógica principal.

👨‍💻 Autor
Projeto desenvolvido por GustavoABA durante a Semana Python.
Versão executável montada com apoio da IA Copilot para otimização de tempo.

👉 Gustavo, esse README já está pronto para você colar no GitHub. Quer que eu também monte um .gitignore básico para não versionar os arquivos da pasta dist e os .spec do PyInstaller?
