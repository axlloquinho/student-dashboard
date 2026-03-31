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
        "INSERT INTO usuarios(id,nome, senha) VALUES (?, ?)",
        (id,nome, senha)
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



#parte das notas.... nao sei como vou fazer isso funcionar... tem só 2 meses que estudo
def criar_tabelas():
  conexao = sqlite3.connect("instance/database.db")
  cursor = conexao.cursor()

  cursor.execute("""CREATE TABLE IF NOT EXISTS bimestres(
  id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,  
  nome TEXT NOT NULL)""")  

  cursor.execute("""CREATE TABLE IF NOT EXISTS materias(
  id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
  nome TEXT NOT NULL)""")

  cursor.execute("""CREATE TABLE IF NOT EXISTS notas(
  id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
  usuario_id INTEGER,
  materia_id INTEGER,
  bimestre_id INTEGER,
  nota REAL,

  FOREIGN KEY (usuario_id) REFERENCES usuarios(id),
  FOREIGN KEY (materia_id) REFERENCES materias(id),
  FOREIGN KEY (bimestre_id) REFERENCES bimestres(id)
  )
  """)

  conexao.commit()
  conexao.close()



def pegar_notas(usuario_id):
  conexao = sqlite3.connect("instance/database.db")
  cursor = conexao.cursor()

  cursor.execute("""
    SELECT bimestres.nome, materias.nome, notas.nota
    FROM notas
    JOIN materias ON materias.id = notas.materia_id
    JOIN bimestres ON bimestres.id = notas.bimestre_id
    WHERE notas.usuario_id = ?
    """, (usuario_id,))

  dados = cursor.fetchall()
  conexao.close()
  
  return notas