import streamlit as st
import snowflake.connector
import toml

# Função para conectar ao Snowflake
def get_snowflake_connection():
    "user" = st.secrets["user"],
    "password" = st.secrets["password"],
    "account" = st.secrets["account"],
    "warehouse" = st.secrets["warehouse"],
    "database" = st.secrets["database"],
    "schema" = st.secrets["schema"]
    
    conn = snowflake.connector.connect(
        user=user,
        password=password,
        account=account,
        warehouse=warehouse,
        database=database,
        schema=schema
    )
    return conn


# Função para executar consultas
def run_query(query, params=None):
    conn = get_snowflake_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(query, params)
        return cursor.fetchall()
    finally:
        cursor.close()
        conn.close()

st.title("Consultas no Snowflake")

consulta_selecionada = st.selectbox("Escolha a consulta:", [
    "1. Serviços solicitados por cliente", 
    "2. Empresa com mais serviços na cidade", 
    "3. Funcionários para cliente em mês/ano"
])

# 1. Serviços solicitados por cliente
if "1. Serviços solicitados por cliente" in consulta_selecionada:
    cliente_id = st.number_input("Insira o ID do cliente (X):", min_value=1, step=1)
    if st.button("Executar"):
        query = """
        SELECT s.nome_servico 
        FROM solicitacao s
        JOIN pedido p ON s.codigo_pedido = p.codigo
        WHERE p.id_cliente = %s
        AND s.data_fin >= DATE_TRUNC('MONTH', DATEADD(MONTH, -1, CURRENT_DATE()))
        AND s.data_fin < DATE_TRUNC('MONTH', CURRENT_DATE())
        AND YEAR(TO_DATE(s.data_fin, 'YYYY-MM-DD')) = YEAR(CURRENT_DATE());
        """



        
        result = run_query(query, (cliente_id,))
        st.write("Resultado:", result)


# 2. Empresa com mais serviços na cidade
if "2. Empresa com mais serviços na cidade" in consulta_selecionada:
    cidade = st.text_input("Insira o nome da cidade (Y):")
    estado = st.text_input("Insira o estado (Z):")
    if st.button("Executar"):
        query = """
        SELECT e.nome, COUNT(se.id) AS total_servicos
        FROM servico_empresa_cidade se
        JOIN empresa e ON se.id_empresa = e.id
        JOIN cidade c ON se.id_cidade = c.nome
        WHERE c.nome = %s AND c.estado = %s
        GROUP BY e.nome
        ORDER BY total_servicos DESC
        LIMIT 1;
        """
        result = run_query(query, (cidade, estado))
        st.write("Resultado:", result)

# 3. Funcionários para cliente em mês/ano
if "3. Funcionários para cliente em mês/ano" in consulta_selecionada:
    cliente_id = st.number_input("Insira o ID do cliente (X):", min_value=1, step=1)
    mes = st.number_input("Insira o mês (Y):", min_value=1, max_value=12, step=1)
    ano = st.number_input("Insira o ano (Z):", min_value=2000, max_value=2100, step=1)
    
    if st.button("Executar"):
        query = """
        SELECT f.nome, f.RG
        FROM func_solicitados fs
        JOIN solicitacao s ON fs.id_solicitacao = s.id
        JOIN pedido p ON s.codigo_pedido = p.codigo
        JOIN funcionarios f ON fs.cpf_func = f.CPF
        WHERE p.id_cliente = %s
          AND s.data_fin >= DATE_TRUNC('MONTH', TO_DATE(CONCAT(%s, '-', %s, '-01'), 'YYYY-MM-DD'))
          AND s.data_fin < DATEADD(MONTH, 1, DATE_TRUNC('MONTH', TO_DATE(CONCAT(%s, '-', %s, '-01'), 'YYYY-MM-DD')))
        """
        
        # Execute a consulta com os parâmetros passados (cliente_id, mes, ano)
        result = run_query(query, (cliente_id, ano, mes, ano, mes))
        
        # Exibe o resultado da consulta
        st.write("Resultado:", result)
