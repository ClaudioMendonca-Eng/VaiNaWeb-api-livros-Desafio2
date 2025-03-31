from flask import Flask, request, jsonify, render_template
import sqlite3
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


def init_db():
    with sqlite3.connect('database.db') as conn:
        conn.execute("""CREATE TABLE IF NOT EXISTS livros (
                     id INTEGER PRIMARY KEY AUTOINCREMENT,
                     titulo TEXT NOT NULL,
                     categoria TEXT NOT NULL,
                     autor TEXT NOT NULL,
                     imagem_url TEXT NOT NULL
                     )""")
        print('Tabela criada com sucesso!')
        
        # Verifica se a tabela está vazia
        cursor = conn.execute("SELECT COUNT(*) FROM livros")
        count = cursor.fetchone()[0]
        if count == 0:
            exemplos = [
                {
                    "titulo": "O Pequeno Príncipe",
                    "categoria": "Ficção",
                    "autor": "Antoine de Saint-Exupéry",
                    "imagem_url": "https://m.media-amazon.com/images/I/81TmOZIXvzL._SY466_.jpg"
                },
                {
                    "titulo": "1984",
                    "categoria": "Distopia",
                    "autor": "George Orwell",
                    "imagem_url": "https://m.media-amazon.com/images/I/51VXYaKO-sL._SY445_SX342_.jpg"
                },
                {
                    "titulo": "Dom Casmurro",
                    "categoria": "Romance",
                    "autor": "Machado de Assis",
                    "imagem_url": "https://m.media-amazon.com/images/I/A1C0FSwUY8L._SY466_.jpg"
                },
                {
                    "titulo": "A Revolução dos Bichos",
                    "categoria": "Fábula",
                    "autor": "George Orwell",
                    "imagem_url": "https://m.media-amazon.com/images/I/61owA5ey3iL._SY445_SX342_.jpg"
                },
                {
                    "titulo": "Cem Anos de Solidão",
                    "categoria": "Realismo Mágico",
                    "autor": "Gabriel García Márquez",
                    "imagem_url": "https://m.media-amazon.com/images/I/511NRhFHZbL._SY445_SX342_.jpg"
                },
                {
                    "titulo": "O Alquimista",
                    "categoria": "Ficção",
                    "autor": "Paulo Coelho",
                    "imagem_url": "https://images-na.ssl-images-amazon.com/images/I/71aFt4+OTOL.jpg"
                },
                {
                    "titulo": "Moby Dick",
                    "categoria": "Aventura",
                    "autor": "Herman Melville",
                    "imagem_url": "https://m.media-amazon.com/images/I/A1xWjc50fmL._SL1500_.jpg"
                },
                {
                    "titulo": "O Hobbit",
                    "categoria": "Fantasia",
                    "autor": "J.R.R. Tolkien",
                    "imagem_url": "https://images-na.ssl-images-amazon.com/images/I/91b0C2YNSrL.jpg"
                },
                {
                    "titulo": "Hamlet",
                    "categoria": "Teatro",
                    "autor": "William Shakespeare",
                    "imagem_url": "https://m.media-amazon.com/images/I/41utozT3RWL._SY445_SX342_.jpg"
                },
                {
                    "titulo": "Ensaio sobre a Cegueira",
                    "categoria": "Distópico",
                    "autor": "José Saramago",
                    "imagem_url": "https://m.media-amazon.com/images/I/41iQySvQq0L._SY445_SX342_.jpg"
                }
            ]
            for livro in exemplos:
                conn.execute('INSERT INTO livros (titulo, categoria, autor, imagem_url) VALUES (?, ?, ?, ?)',
                             (livro["titulo"], livro["categoria"], livro["autor"], livro["imagem_url"]))
            conn.commit()
            print('Livros de exemplo adicionados com sucesso!')

init_db()

@app.route('/')

def home_page():  
    return render_template('index.html')

@app.route('/doar', methods=['POST'])
def doar_livro():
    dados = request.get_json()
    titulo = dados.get('titulo')
    categoria = dados.get('categoria')
    autor = dados.get('autor')
    imagem_url = dados.get('imagem_url')   
    
    if not all([titulo, categoria, autor, imagem_url]):
        return jsonify({"erro": "Todos os campos são obrigatórios"}), 400
    
    with sqlite3.connect('database.db') as conn:
        conn.execute('INSERT INTO livros (titulo, categoria, autor, imagem_url) VALUES (?, ?, ?, ?)',
                     (titulo, categoria, autor, imagem_url))
        conn.commit()
        return jsonify({"mensagem": "Livro cadastrado com sucesso!"}), 201

@app.route('/livros', methods=['GET'])
def listar_livros():
    with sqlite3.connect('database.db') as conn:
        livros = conn.execute('SELECT * FROM livros').fetchall()
    
    livros_formatados = []

    for livro in livros:
        dicionario_livro = {
            'id': livro[0],
            'titulo': livro[1],
            'categoria': livro[2],
            'autor': livro[3],
            'imagem_url': livro[4]
        }
        livros_formatados.append(dicionario_livro)
    return jsonify(livros_formatados)

@app.route('/livros/<int:livro_id>', methods=['DELETE'])
def deletar_livro(livro_id):
    with sqlite3.connect('database.db') as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM livros WHERE id = ?", (livro_id,))
        conn.commit()

    if cursor.rowcount == 0:
        return jsonify({"erro": "Livro não encontrado"}), 400
    return jsonify({"menssagem": "Livro excluído com sucesso"}), 200

if __name__ == '__main__':
    app.run(debug=True)