df = pd.read_csv('vendas_relatorio_300MB.csv')

caminho_csv = "vendas_relatorio_300MB.csv"

df = pd.read_csv(caminho_csv)

# Conexão com PostgreSQL
usuario = "postgres"
senha = 
host = "localhost"
porta = "5432"
banco = "LojaFicticia"

engine = create_engine(f"postgresql+psycopg2://{usuario}:{senha}@{host}:{porta}/{banco}")

df = df.drop_duplicates()

# Enviar para PostgreSQL e criar tabela automaticamente
df.to_sql("vendas", engine, if_exists="replace", index=False)

# Remove duplicados no DataFrame antes de enviar




print("✅ CSV importado para PostgreSQL com sucesso!")

