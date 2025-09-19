import pandas as pd
import matplotlib.pyplot as plt
import psycopg2
from sqlalchemy import create_engine

# Conexão com PostgreSQL
# try:
#     conn = psycopg2.connect(
#         host="localhost",
#         database="LojaFicticia",
#         user="postgres",
#         password="Rafagb1980!"
#     )


#     cur = conn.cursor()
#     cur.execute("SELECT version();")
#     versao = cur.fetchone()
#     print("✅ Conexão bem-sucedida!")
#     print("Versão do PostgreSQL:", versao)

# except Exception as e:
#         print("❌ Erro ao conectar:", e)

# finally:
#         if 'cur' in locals():
#             cur.close()
#         if 'conn' in locals():
#             conn.close()



df = pd.read_csv('vendas_relatorio_300MB.csv')

caminho_csv = "vendas_relatorio_300MB.csv"

df = pd.read_csv(caminho_csv)

# Conexão com PostgreSQL
usuario = "postgres"
senha = "Rafagb1980!"
host = "localhost"
porta = "5432"
banco = "LojaFicticia"

engine = create_engine(f"postgresql+psycopg2://{usuario}:{senha}@{host}:{porta}/{banco}")

df = df.drop_duplicates()

# Enviar para PostgreSQL e criar tabela automaticamente
df.to_sql("vendas", engine, if_exists="replace", index=False)

# Remove duplicados no DataFrame antes de enviar




print("✅ CSV importado para PostgreSQL com sucesso!")




