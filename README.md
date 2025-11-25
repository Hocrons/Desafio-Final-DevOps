# 🚀 Desafio Final DevOps — API Flask com CI, Testes Automatizados e Deploy

Este projeto foi desenvolvido como parte do **Desafio Final de DevOps** e inclui:

- API Flask  
- Autenticação JWT  
- Documentação Swagger  
- Testes Automatizados  
- Pipeline CI com GitHub Actions  
- Deploy automático na Vercel  
- Docker para ambiente local  

---

## 📌 **Endpoints da API**

| Método | Rota         | Descrição                              |
|--------|--------------|------------------------------------------|
| GET    | `/`          | Status da API                           |
| GET    | `/items`     | Retorna lista de itens                  |
| POST   | `/login`     | Gera token JWT                          |
| GET    | `/protected` | Rota protegida por JWT                  |
| GET    | `/swagger`   | Interface Swagger UI                    |

---

# 🔐 Autenticação JWT

### ➤ **Login**
`POST /login`

Retorno esperado:

``json
{
  "access_token": "TOKEN_JWT_AQUI"
}
➤ Acesso à rota protegida
Envie o token no header:

makefile
Copiar código
Authorization: Bearer SEU_TOKEN_AQUI
📘 Documentação Swagger
A documentação completa está disponível em:

👉 /swagger

Arquivo JSON utilizado:

arduino
Copiar código
/static/swagger.json
🧪 Testes Automatizados
Testes desenvolvidos com unittest, cobrindo:

✔ Rota principal /
✔ Rota /items
✔ Login /login e retorno do token
✔ Acesso negado à rota /protected sem token
✔ Acesso permitido à rota /protected com token válido

Executar testes:
nginx
Copiar código
python -m unittest discover -v
⚙️ CI — GitHub Actions
Pipeline executa automaticamente:

Instalação das dependências

Execução dos testes automatizados

Validação do ambiente

Arquivo do workflow:
.github/workflows/ci.yml

☁️ Deploy na Vercel
O deploy é realizado automaticamente a cada push na branch main.

URL do deploy (substituir pela sua):

👉 https://seu-projeto.vercel.app

🐳 Executar com Docker
Para rodar usando Docker:

css
Copiar código
docker-compose up --build
Benefícios:

Ambiente isolado

Reprodutibilidade entre máquinas

Configuração consistente

📦 Dependências Principais
Flask

Flask-JWT-Extended

Flask-Swagger-UI

Gunicorn

Werkzeug 2.3.7

Arquivo: requirements.txt

💻 Como Rodar Localmente
1️⃣ Clonar o repositório
bash
Copiar código
git clone https://github.com/SEU-USUARIO/Desafio-Final-DevOps.git
2️⃣ Instalar dependências
nginx
Copiar código
pip install -r requirements.txt
3️⃣ Executar aplicação
nginx
Copiar código
python app.py
Acessar no navegador:

👉 http://localhost:5000

👤 Autor
Heitor dos Santos Oliveira
Estudante de Sistemas de Informação — DevOps Practitioner
