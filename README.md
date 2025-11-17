# Projeto API Flask + Testes Unitários (DevOps)

Este repositório contém uma API simples desenvolvida em **Flask**, acompanhada de um ambiente configurado com **Docker** e **testes unitários** utilizando **unittest**, conforme solicitado no LAB e nos slides fornecidos.

---

## 📌 Objetivo do Projeto

O objetivo principal deste projeto é aplicar conceitos fundamentais de **DevOps**, incluindo:

* Criação de uma API web simples em Flask
* Criação de ambiente de execução com Docker
* Criação de testes unitários usando unittest
* Execução dos testes dentro de um container Docker
* Organização e padronização do projeto com README

---

## 🗂 Estrutura do Projeto

```
/Desafio-Final-DevOps
│
├── app.py                 # Código principal da API Flask
├── test_app.py            # Testes unitários dos endpoints
├── requirements.txt       # Dependências Python
├── Dockerfile             # Imagem Docker da API
└── docker-compose.yml     # Orquestração dos containers
```

---

## 🚀 API Flask

A API possui três endpoints principais:

### **GET /**

Retorna mensagem indicando que a API está online.

### **POST /login**

Gera um token JWT fictício apenas para fins de teste.

### **GET /protected**

Rota protegida que exige token. Sem token → retorna **401**.

---

## 🧪 Testes Unitários

Os testes validados no arquivo `test_app.py` verificam:

### ✔ test_home

* Verifica status 200
* Verifica resposta `{"message": "API is running"}`

### ✔ test_login

* Verifica status 200
* Verifica existência de `access_token` na resposta

### ✔ test_protected_no_token

* Acesso à rota protegida sem token
* Resultado esperado → **401 Unauthorized**

### ▶ Como executar os testes

No Docker Compose:

```
docker-compose run api python -m unittest discover
```

Sem Docker:

```
python -m unittest discover
```

---

## 🐳 Docker

### 📌 Dockerfile

O projeto possui um Dockerfile que:

* Define a imagem base Python
* Instala dependências
* Copia o código para o container
* Expõe porta 5000
* Executa o app Flask

### 📌 docker-compose.yml

O compose gerencia o serviço `api`, mapeando portas e volume do projeto.

### ▶ Como iniciar a API:

```
docker-compose up --build
```

API estará disponível em:

```
http://localhost:5000
```

---

## 📦 Dependências

As dependências do projeto estão no arquivo **requirements.txt**, incluindo:

* Flask
* Werkzeug>=2.3.3
* PyJWT (caso utilizado)

Instalação manual:

```
pip install -r requirements.txt
```

---

## 📚 Fonte / Base do Projeto

Este projeto segue como continuação das atividades do **LAB de API WEB + Testes Unitários + Docker**, conforme instruções dos slides fornecidos.

---

## ✅ Status do Projeto

✔ API funcionando<br>
✔ Testes unitários implementados<br>
✔ Ambiente Docker configurado<br>
✔ Pronto para entrega

---

## 👨‍💻 Autor

Heitor dos Santos

Projeto desenvolvido para disciplina de DevOps.
