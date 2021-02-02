import streamlit as st
import pandas as pd



def main():
    
    st.title("Minha primeira aplicação")
    
    
    obitos_2019 = carrega_dados('../Dados/obitos-2019.csv')
    st.text("Dados Brutos")
    st.dataframe(obitos_2019)

def carrega_dados(caminho):
    dados = pd.read_csv(caminho)
    return dados     

               
if __name__ == "__main__":
    main()                                               