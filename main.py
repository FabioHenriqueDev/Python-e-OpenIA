from legendador import legendar
import streamlit as st
import audioop


# legendar(arquivo_video='video.mp4', contexto='video de propaganda da hashtag')

def app():
    st.header('Legendador', divider=True)
    st.markdown("#### Gere a legenda de qualquer vídeo ou áudio automaticamente")

    contexto = st.text_input("Dê algum contexto do que o vídeo se trata para ajudar na legenda")
    arquivo = st.file_uploader("Selecione o vídeo (.mp4) ou áudio (.mp3) para legendar", type=['mp4', "mp3"])
    if arquivo:
        legenda = legendar(arquivo, contexto)
        st.write(f'Arquivo {arquivo.name} legendado com sucesso!')
        st.write(legenda)
   

    

if __name__ == '__main__':
    app()