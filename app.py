import streamlit as st

st.title('Добро пожаловать на главную страницу проекта, мастер 🧙‍♂️')

st.markdown(
    '<h3 style="text-align: center;">Логотип нашей команды! (поменяй)</h3>',
    unsafe_allow_html=True
)
# st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
# st.image('/home/Rena/bootcamp_ds/phase_2/ds-phase-2/nn_project/images/test_logo.png', width=100)
# st.markdown("</div>", unsafe_allow_html=True)

st.markdown(
    """
    <style>
        .logo-container {
            display: flex;
            justify-content: center;
        }
    </style>
    <div class='logo-container'>
        <img src='/home/Rena/bootcamp_ds/phase_2/ds-phase-2/nn_project/images/ffile.jpg' width='100'>
    </div>
""",
unsafe_allow_html=True
)

st.markdown("""
## Данный проект был создан для демонстрации того, чему мы научились за эту неделю!

**Авторы:** [Илья Крючков](https://github.com/xefr762), [Алина Зарницына](https://github.com/RenaTheDv), [Анатолий Яковлев](https://github.com/cdxxi)

**Описание:**
- **Главная страница**: Общая информация и навигация 🌠
- **Первая страница**: Модель, которая принимает от пользователя картинку и выдает предсказанный класс 🎰
- **Вторая страница**: Модель, которая тоже принимает от пользователя картинку и выдает предсказанный класс (удивительно, да?) 🤔
- **Третья страница**: Метрики моделей, время их обучения, описание проблем 🥂


Переключайтесь между страницами через левый сайдбар! 
""")