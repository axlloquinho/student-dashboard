import sqlite3


def cadastrar(nome, senha):
    conexao = sqlite3.connect("instance/database.db")
    cursor = conexao.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS usuarios(
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    nome TEXT UNIQUE NOT NULL,
    senha TEXT NOT NULL)""")

    try:
      cursor.execute(
        "INSERT INTO usuarios(nome, senha) VALUES (?, ?)",
        (nome, senha)
    )

      conexao.commit()
      conexao.close()
      return "ok"

    except sqlite3.IntegrityError:
        conexao.rollback()
        conexao.close()
        return "existe"
    
    except Exception as e:
       conexao.rollback()
       conexao.close()
       print("ERRO REAL:", e)
       return "erro"

def login_funcao(nome,senha):
  conexao = sqlite3.connect("instance/database.db")
  cursor = conexao.cursor()

  cursor.execute("""CREATE TABLE IF NOT EXISTS usuarios(
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    nome TEXT UNIQUE NOT NULL,
    senha TEXT NOT NULL)""")

  cursor.execute("SELECT * FROM usuarios WHERE nome=? AND senha=?", (nome,senha))
  login=cursor.fetchone()


  if login:
    return "permitido"

  else:
    return "negado" 

  conexao.close()   
      