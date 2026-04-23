import streamlit as st

st.set_page_config(page_title="Disciplinas", page_icon="📚")

st.title("Gestão de Disciplinas")

# Abas para separar Listagem de Cadastro
tab_lista, tab_novo = st.tabs(["📋 Listar", "➕ Nova Disciplina"])

with tab_novo:
    st.subheader("Cadastrar Nova Matéria")
    with st.form("form_disciplina"):
        nome = st.text_input("Nome da Disciplina")
        professor = st.text_input("Nome do Professor")
        dia_semana = st.selectbox("Dia da Aula", ["Seg", "Ter", "Qua", "Qui", "Sex"])
        
        submitted = st.form_submit_button("Salvar")
        if submitted:
            st.success(f"Disciplina {nome} cadastrada! (Simulação)")

with tab_lista:
    st.info("A conexão com o Xano virá em breve.")
    # Exemplo de dados (Mockup)
    st.dataframe([
        {"Nome": "Software Engineering", "Professor": "Oriel", "Dia": "Seg"},
        {"Nome": "Database Management", "Professor": "Giuliano", "Dia": "Qui"},
    ], use_container_width=True)