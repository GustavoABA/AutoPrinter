# 🖥️ AutoPrinter (AutoWeb) — GUI + Build de Executável

![Python](https://img.shields.io/badge/Python-3.x-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Qt](https://img.shields.io/badge/Qt-PySide6-217346?style=for-the-badge&logo=qt&logoColor=white)
![PyInstaller](https://img.shields.io/badge/PyInstaller-Build-yellow?style=for-the-badge)

O **AutoPrinter** é um app com interface (Qt/PySide6) que coleta dados na tela e dispara um processo de automação que:
- **gera um script Python “embutindo” e-mail/senha**
- **builda um executável (`.exe`) via PyInstaller**
- o executável gerado captura **screenshot** e envia por e-mail em loop

> ⚠️ **IMPORTANTE (Ética & Segurança):** este projeto envolve captura de tela e envio por e-mail. Use **somente em ambiente próprio**, com **consentimento explícito** e **nunca** em computadores de terceiros.

---

## ✅ O que tem neste repositório

- `Main.py` — ponto de entrada (abre a janela da aplicação)
- `Controller.py` — lógica da interface (carrega o `Menu.ui`, pega inputs e chama o sistema)
- `Executavel.py` — gera um novo script (`ExecutavelGerado.py`) e compila o executável com PyInstaller

> O `Menu.ui` precisa existir para a interface abrir.

---

## 📂 Estrutura recomendada do projeto

> **Do jeito que o código está hoje**, o `Menu.ui` é carregado a partir **da mesma pasta do `Controller.py`**.

Exemplo simples:

```
AutoPrinter/
├─ Main.py
├─ Controller.py
├─ Executavel.py
├─ Menu.ui
└─ (dist/)  ← gerado pelo PyInstaller
```

---

## 🛠️ Requisitos

- Python 3.x
- Windows (o build `.exe` e a parte de inicialização automática fazem mais sentido aqui)
- Dependências:
  - PySide6
  - pyautogui
  - pyinstaller

---

## ⚙️ Instalação

### 1) Clonar
```bash
git clone https://github.com/GustavoABA/AutoPrinter.git
cd AutoPrinter
```

### 2) (Opcional, mas recomendado) Criar ambiente virtual
```bash
python -m venv .venv
```

**Ativar no Windows (PowerShell):**
```bash
.\.venv\Scripts\Activate.ps1
```

### 3) Instalar dependências
```bash
pip install PySide6 pyautogui pyinstaller
```

> Se aparecer erro do PyAutoGUI no Windows, às vezes falta permissão de captura/controle. Rode como usuário normal e teste.

---

## ▶️ Como executar

```bash
python Main.py
```

O `Main.py` importa `Controller` e chama `Controller.abrir_janela()`, abrindo a interface.  
Quando o usuário clica no botão (e aceita o checkbox), a aplicação chama `Executavel.executar_system(remetente, destinatario, senha)`.

---

## 🧠 Como funciona (por baixo do capô)

### 1) Interface (Controller.py)
- Carrega `Menu.ui` via `QUiLoader`
- Lê três campos de texto:
  - **destinatário**
  - **remetente**
  - **senha**
- Valida se o **checkbox** está marcado
- Ao clicar no botão, dispara o processo de build chamando o módulo `Executavel`

---

### 2) Gerador de executável (Executavel.py)
Quando você chama `Executavel.executar_system(remetente, destinatario, senha)` ele:

1. Monta um **novo script** (string grande) com:
   - captura de tela via `pyautogui`
   - envio por e-mail via `smtplib` (Gmail: smtp.gmail.com:587)
   - loop com `sleep(120)` (a cada 2 minutos)
2. Salva esse script como:
   - `ExecutavelGerado.py`
3. Chama PyInstaller programaticamente (`PyInstaller.__main__.run`) para gerar:
   - `ExecutavelFinal.exe` (onefile, noconsole)

---

## 🔐 Configuração de e-mail (Gmail)

Para Gmail, normalmente você deve usar **Senha de App** (não a senha normal):

1. Ative **Verificação em duas etapas** na conta Google
2. Gere uma **Senha de Aplicativo**
3. Use essa senha no campo “senha” da interface

> Isso reduz risco e evita bloqueios do Google.

---

## 📦 Build do executável (manual)

Você pode buildar manualmente também.

### A) Build do app principal (GUI)
```bash
pyinstaller --onefile --noconsole --name AutoPrinter Main.py
```

> Se você quiser empacotar o `Menu.ui` junto, use `--add-data`, mas atenção: o código atual procura `Menu.ui` por caminho relativo ao `Controller.py`.  
> Uma abordagem comum é manter `Menu.ui` junto do `.exe` (ou adaptar o código para carregar de resources).

### B) Build do executável gerado (fluxo do projeto)
O fluxo “principal” do projeto é via GUI:
- abrir o app
- preencher remetente/destinatário/senha
- marcar checkbox
- clicar no botão

A partir disso, o próprio `Executavel.py` gera e builda o executável final automaticamente.

---

## ⚠️ Nota importante: inicialização automática no Windows

O script gerado possui lógica para **copiar o executável para a pasta de Inicializar do Windows** (Startup).  
Isso significa que ele pode começar junto com o Windows.

✅ Se sua intenção for **apenas demonstrar automação**, considere **remover/desativar** essa parte antes de publicar/usar em terceiros.

> Recomendação: deixe isso **desligado por padrão** e só habilite em ambiente de teste controlado.

---

## 🧯 Troubleshooting

### “A janela não abre / não acha Menu.ui”
- Garanta que o arquivo `Menu.ui` esteja no mesmo diretório do `Controller.py`.

### “PyInstaller não gera exe”
- Confira se você instalou o `pyinstaller` no mesmo ambiente Python que está executando.

### “Email falha (login)”
- Use Senha de Aplicativo no Gmail
- Verifique se o remetente/destinatário estão corretos

---

## 📌 Roadmap (ideias boas pra evoluir)
- [ ] Remover dependências não usadas (ex.: `helium` parece não ser utilizado)
- [ ] Guardar credenciais de forma segura (evitar embutir senha em script gerado)
- [ ] Criar modo de teste (sem loop infinito / sem startup)
- [ ] Logs na interface (QTextEdit) para o usuário ver o status do build/envio

---

## 👨‍💻 Autor

Desenvolvido por **GustavoABA** — foco em **produtividade** e **automação**.
