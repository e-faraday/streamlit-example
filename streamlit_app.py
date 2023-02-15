import streamlit as st
import psycopg2


@st.experimental_singleton
def init_connection():
    return psycopg2.connect(**st.secrets["postgres"])

conn = init_connection()

@st.experimental_memo(ttl=15)
def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()
    
 rows = run_query("SELECT * from testschema15.test_table15;")   

for row in rows:
    st.write(f"{row[0]} has a :{row[1]}:")


