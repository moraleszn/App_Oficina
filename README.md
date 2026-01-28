# 🚗 App Oficina

> Sistema web para gerenciamento de clientes e veículos de uma oficina mecânica. Projeto de portfólio.

---

## ✨ Funcionalidades

🔹 Cadastro de clientes com dados pessoais (nome, sobrenome, e-mail, CPF)  
🔹 Cadastro de múltiplos carros por cliente (modelo, placa, ano)  
🔹 Listagem e visualização de clientes  
🔹 Interface amigável e responsiva  

---

## 🛠️ Tecnologias Utilizadas

🐍 **Python 3**  
🌐 **Django** (framework web principal)  
🗄️ **SQLite** (banco de dados local)  
💻 **HTML5** & **CSS3** (com Bootstrap 4)  
⚡ **JavaScript** (dinamismo nos formulários)  
🎨 **Boxicons** (ícones visuais)  

---

## 📁 Estrutura do Projeto

```
App_Oficina/
├── appjato/           # Configurações do projeto Django
├── clientes/          # App Django para clientes e carros
│   ├── migrations/    # Migrações do banco de dados
│   ├── templates/     # Templates HTML
│   ├── static/        # Arquivos estáticos (JS, CSS)
├── static/            # Arquivos estáticos globais
├── templates/         # Templates globais
├── db.sqlite3         # Banco de dados local (ignorado no git)
├── manage.py          # Gerenciador Django
└── README.md          # Este arquivo
```

---

## 🚀 Como rodar o projeto

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/moraleszn/App_Oficina.git
   cd App_Oficina
   ```
2. **Instale as dependências** (recomenda-se uso de ambiente virtual):
   ```bash
   pip install django
   ```
3. **Aplique as migrações:**
   ```bash
   python manage.py migrate
   ```
4. **Inicie o servidor de desenvolvimento:**
   ```bash
   python manage.py runserver
   ```
5. **Acesse:** [http://127.0.0.1:8000/clientes/](http://127.0.0.1:8000/clientes/)

---

## ℹ️ Observações

🗃️ O arquivo `db.sqlite3` não é versionado; use as migrações para criar o banco.  
📦 Migrações e arquivos essenciais estão versionados para facilitar a reprodução do projeto.  

