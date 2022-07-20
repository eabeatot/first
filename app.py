import streamlit as st

menu = st.sidebar.selectbox('MENU', options=['로그인', '회원가입', '회원목록'])

if menu == '로그인':
    st.subheader('로그인')
    st.sidebar.subheader('로그인')

    login_id = st.sidebar.text_input('아이디', placeholder='아이디를 입력하세요')
    login_pw = st.sidebar.text_input('패스워드',
                                     placeholder='패스워드를 입력하세요',
                                     type='password')

    login_btn = st.sidebar.button('로그인')

    if login_btn:
        st.sidebar.write(login_id)
        st.sidebar.write(login_pw)

if menu == '회원가입':
    st.subheader('회원가입')
    st.sidebar.write('회원가입')
if menu == '회원목록':
    st.subheader('회원목록')
    st.sidebar.write('회원목록')