import streamlit as st
from src.services.text_summary_service import TextSummaryService


@st.cache_data
def get_handler():
    handler = TextSummaryService()
    return handler


def show():
    if 'start_btn' in st.session_state and st.session_state.start_btn is True:
        st.session_state.running = True
    else:
        st.session_state.running = False

    # Выводим заголовок страницы
    st.title('Выделение основных тезисов из вашего текста')
    # Выводим форму для ввода текста
    text = st.text_area(
        label='',
        placeholder='Введите текст',
        key='target_text',
        height=320)
    # Выводим кнопку на запуск саммаризации
    btn = st.button(
        'Сформировать конспект',
        type='primary',
        key='start_btn',
        disabled=st.session_state.running)

    if btn and text:
        summary = get_handler().handle(text, useV2=True)
        st.session_state.output = summary
        st.experimental_rerun()

    if 'output' in st.session_state:
        st.write('## Итоговый конспект:')
        st.write(st.session_state.output)
