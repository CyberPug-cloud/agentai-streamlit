import streamlit as st
import openai
import os
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

st.title("Generator Postów Marketingowych")

# Formularz do wprowadzenia tematów na każdy dzień tygodnia
st.header("Wprowadź tematy postów na najbliższy tydzień")
days = ["Poniedziałek", "Wtorek", "Środa", "Czwartek", "Piątek", "Sobota", "Niedziela"]
topics = {}
for day in days:
    topics[day] = st.text_input(f"Temat na {day}:", "")

# Przycisk do generowania treści
if st.button("Generuj treści na cały tydzień"):
    generated_posts = {}
    for day, topic in topics.items():
        if topic:  # Jeśli temat został wpisany
            # Przygotowanie promptu dla ChatGPT
            prompt = (f"Przygotuj post na Instagram zgodny z poniższym Brand Brief:\n"
                      "Brand Brief: [Tutaj wpisz swój Brand Brief, np. ton, styl, wartości]\n"
                      f"Temat: {topic}\n"
                      "Wygeneruj treść posta, która jest zgodna z tymi wymaganiami.")
            # Wywołanie OpenAI API
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=150,
                temperature=0.7
            )
            post_text = response['choices'][0]['message']['content'].strip()
            generated_posts[day] = post_text
        else:
            generated_posts[day] = "Brak tematu."
    
    # Wyświetlenie wygenerowanych postów
    st.header("Wygenerowane posty:")
    for day in days:
        st.subheader(day)
        st.write(generated_posts[day])
