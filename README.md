# 🚀 Desafio Final DevOps — API Flask com CI, Testes Automatizados e Deploy na Vercel

Este projeto foi desenvolvido como parte do desafio final do módulo de **DevOps**, aplicando:
- Desenvolvimento de API em Flask  
- Autenticação JWT  
- Documentação com Swagger  
- Testes automatizados  
- CI usando GitHub Actions  
- Deploy automatizado utilizando a Vercel  

O resultado é uma aplicação completa, profissional e seguindo boas práticas modernas de desenvolvimento e automação.

---

# 📂 Estrutura do Projeto

Desafio-Final-DevOps/
├── app.py
├── test_app.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── static/
│ └── swagger.json
└── .github/
└── workflows/
└── ci.yml

yaml
Copiar código

---

# 🧩 Funcionalidades da API

### **Endpoints principais**

| Método | Rota         | Descrição                              |
|--------|--------------|------------------------------------------|
| GET    | `/`          | Verifica se a API está no ar            |
| GET    | `/items`     | Retorna uma lista de itens              |
| POST   | `/login`     | Gera um token JWT                       |
| GET    | `/protected` | Endpoint protegido que exige JWT        |
| GET    | `/swagger`   | Interface Swagger UI com documentação   |

---

# 🔐 Autenticação (JWT)

A rota `/login` gera um token JWT:

```json
{
  "access_token": "xxxx.yyyy.zzzz"
}
Para acessar /protected, envie o token no cabeçalho:

makefile
Copiar código
Authorization: Bearer SEU_TOKEN_AQUI
📘 Documentação Swagger
A API possui documentação Swagger UI disponível em:

👉 /swagger

Arquivos JSON da documentação ficam em:

arduino
Copiar código
/static/swagger.json
🧪 Testes Automatizados
Os testes foram criados utilizando o módulo unittest.

Os seguintes cenários são validados:

✔ Teste da rota principal (/)

✔ Teste da lista de itens (/items)

✔ Teste de login e retorno do token JWT (/login)

✔ Teste da rota protegida sem token (deve falhar)

✔ Teste da rota protegida com token válido (deve passar)

Executar testes localmente:
nginx
Copiar código
python -m unittest discover -v
⚙️ CI — Integração Contínua com GitHub Actions
O pipeline CI executa automaticamente:

Instalação de dependências

Execução dos testes automatizados

Validação da qualidade do código

Arquivo do pipeline:

bash
Copiar código
.github/workflows/ci.yml
Workflow utilizado:

yaml
Copiar código
name: CI - Testes Automatizados

on:
  push:
    branches: ["main"]
  pull_request:
    branches: ["main"]

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: Run tests
        run: python -m unittest discover -v
☁️ Deploy — Plataforma Vercel
O deploy da aplicação é realizado automaticamente pela Vercel a cada push na branch main.

✔ Deploy automático
✔ Logs e previews gerenciados pela Vercel
✔ Ambiente estável e escalável
A URL do deploy deve ser adicionada aqui:

👉 https://seu-projeto.vercel.app

🐳 Docker (Ambiente Local)
O projeto também conta com configuração Docker para execução local.

Build e execução:
css
Copiar código
docker-compose up --build
Isso permite:

Ambiente isolado

Mesma configuração entre dev e produção

Execução rápida e consistente

📦 Dependências principais
Flask

Flask-JWT-Extended

Flask-Swagger-UI

Werkzeug 2.3.7

Gunicorn

Arquivo: requirements.txt

💡 Como Rodar Localmente
Clone o repositório

bash
Copiar código
git clone https://github.com/SEU-USUARIO/Desafio-Final-DevOps.git
Instale dependências

nginx
Copiar código
pip install -r requirements.txt
Inicie o servidor

nginx
Copiar código
python app.py
Acesse no navegador:

arduino
Copiar código
http://localhost:5000
📝 Autor
Heitor dos Santos
Estudante de Sistemas de Informação | Desenvolvedor | DevOps
