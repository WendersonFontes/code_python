import pandas as pd
import sqlite3

conn = sqlite3.connect(":memory:")

conn.execute('''CREATE TABLE clientes
                (id INT PRIMARY KEY,
                 nome TEXT,
                 idade INT)''')

conn.execute("INSERT INTO clientes (id, nome, idade) VALUES (1, 'Alice', 30)")
conn.execute("INSERT INTO clientes (id, nome, idade) VALUES (2, 'Bob', 25)")
conn.execute("INSERT INTO clientes (id, nome, idade) VALUES (3, 'Charlie', 35)")

oltp_data = pd.read_sql_query("SELECT * FROM clientes", conn)
print("Dados OLTP:")
print(oltp_data)
print("\n")

average_age = oltp_data['idade'].mean()
print(f"Média de Idade (Análise OLAP): {average_age}")

conn.close()
