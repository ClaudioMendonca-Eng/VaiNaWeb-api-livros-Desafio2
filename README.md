
# 📚 Desafio 2: API Livros - Vai Na Web

Este projeto é um desafio do módulo avançado de Back-end do curso **Vai Na Web**. O objetivo é criar uma API em Flask para cadastrar e listar livros, aplicando boas práticas no desenvolvimento de APIs e banco de dados.

## 🚀 Funcionalidades

- 📌 **Página inicial**: Acessar a rota `/` para verificar se a API está funcionando.
- 📌 **Cadastrar um livro**: Enviar uma requisição `POST` para `/doar` para adicionar um novo livro ao banco de dados.
- 📌 **Listar todos os livros**: Fazer uma requisição `GET` para `/livros` para obter todos os livros cadastrados.
- 📌 **Deletar um livro**: Enviar uma requisição `DELETE` para `/livros/<id>` para remover um livro existente.


## ⚙️ Tecnologias Utilizadas

- 🐍 **Flask** - Framework para construção da API.
- 🗄️ **SQLite** - Banco de dados para armazenar os livros.
- 📡 **JSON** - Formato de resposta da API.

## 📂 Estrutura do Projeto

```
📂 VaiNaWeb-api-livros-Desafio2
├── 📂templates
│   └── 📄 index.html       # Template da página inicial da API
├── 📄 app.py               # Código principal da API
├── 📄 database.db          # Banco de dados SQLite
├── 📄 requirements.txt     # Dependências do projeto
└── 📄 README.md            # Documentação do projeto
```

## 📥 Instalação e Execução

1️⃣ Clone este repositório:
```bash
git clone https://github.com/ClaudioMendonca-Eng/VaiNaWeb-api-livros-Desafio2
cd api-livros
```

2️⃣ Crie um ambiente virtual e ative-o:
```bash
python -m venv venv
# No Windows
venv\Scripts\activate
# No Linux/macOS
source venv/bin/activate
```

3️⃣ Instale as dependências:
```bash
pip install -r requirements.txt
```

4️⃣ Execute a API:
```bash
python app.py
```

A API estará rodando em `http://127.0.0.1:5000/`.

## 📤 Endpoints da API

| Método | Rota      | Descrição |
|--------|----------|-----------|
| GET    | `/`      | Página inicial da API |
| GET    | `/livros` | Listar todos os livros |
| POST   | `/doar`  | Cadastrar um novo livro |

### 📌 Exemplo de Requisição `POST /doar`
```json
{
  "titulo": "O Pequeno Príncipe",
  "categoria": "Ficção",
  "autor": "Antoine de Saint-Exupéry",
  "imagem_url": "https://exemplo.com/pequeno-principe.jpg"
}
```

### 📌 Exemplo de Resposta `GET /livros`
```json
[
  {
    "id": 1,
    "titulo": "O Pequeno Príncipe",
    "categoria": "Ficção",
    "autor": "Antoine de Saint-Exupéry",
    "imagem_url": "https://exemplo.com/pequeno-principe.jpg"
  }
]
```


### [![Postman](https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=postman&logoColor=white)](https://www.postman.com/) A documentação da API foi feita utilizando o Postman e está disponível no link abaixo:

- [Documentação da API](https://documenter.getpostman.com/view/19942731/2sAYkBs1ag)


---

## 📌 <a name="observações"> Observações </a>

> [!IMPORTANT]  
> Este projeto é voltado para fins educacionais e demonstração.

> [!TIP]
> Caso tenha alguma dúvida ou sugestão, entre em contato comigo pelo [LinkedIn](https://www.linkedin.com/in/claudio-mendonca/).


## <a name="licenca"> Licença </a>

<a href="https://www.buymeacoffee.com/claudiomendonca" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;" ></a>

Copyright © 2025 <a href="https://www.claudiomendonca.eng.br" target="_blank">ClaudioMendonca.eng.br</a>.
