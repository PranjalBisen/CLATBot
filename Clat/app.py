import streamlit as st
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

nlp = spacy.load("en_core_web_sm")

knowledge_base = {
    "What is CLAT?": (
        "CLAT stands for the Common Law Admission Test. "
        "It is a highly competitive entrance exam for admission to National Law Universities in India."
    ),
    "What is the syllabus for CLAT 2025?": (
        "The CLAT 2025 syllabus includes English Language, Current Affairs, "
        "Legal Reasoning, Logical Reasoning, and Quantitative Techniques."
    ),
    "How many questions are there in the English section?": (
        "The English section typically contains 28-32 questions."
    ),
    "What was last year’s cut-off for NLSIU Bangalore?": (
        "The 2024 CLAT cut-off for NLSIU Bangalore was approximately at 98.5 percentile."
    ),
    "Is there negative marking in CLAT?": (
        "Yes, there is negative marking in CLAT. For each incorrect answer, 0.25 marks are deducted."
    ),
    "What is the application fee for CLAT 2025?": (
        "The application fee for CLAT 2025 is expected to be around INR 4000 for general category applicants, "
        "with lower fees for reserved categories."
    ),
    "When will CLAT 2025 be conducted?": (
        "CLAT 2025 is anticipated to be conducted in early December 2024, though exact dates will be announced by the organizing body."
    ),
    "What is the exam pattern for CLAT?": (
        "CLAT is a pen-and-paper exam that comprises multiple sections including English, General Knowledge, "
        "Legal Reasoning, Logical Reasoning, and Quantitative Techniques."
    ),
    "Are there any reservations in CLAT?": (
        "Yes, reservations are applicable as per government norms for SC/ST/OBC/PwD candidates."
    ),
    "How many sections does the CLAT exam have?": (
        "The CLAT exam generally consists of 5 sections covering different subjects such as English, GK, "
        "Legal Reasoning, Logical Reasoning, and Quantitative Techniques."
    ),
    "What is the duration of the CLAT exam?": (
        "The exam typically lasts for 2 hours."
    )
}

def preprocess(text):
    """
    Preprocess the text by lowercasing, stripping whitespace,
    removing stopwords and punctuation, and lemmatizing.
    """
    doc = nlp(text.lower().strip())
    tokens = [token.lemma_ for token in doc if not token.is_stop and not token.is_punct]
    return " ".join(tokens)

questions = list(knowledge_base.keys())
processed_questions = [preprocess(q) for q in questions]
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(processed_questions)

def chatbot_response(user_input):
    """
    Generate a response based on the user input.
    Uses TF-IDF vectorization and cosine similarity for matching.
    """
    processed_input = preprocess(user_input)
    query_vec = vectorizer.transform([processed_input])
    similarity_scores = cosine_similarity(query_vec, tfidf_matrix).flatten()
    best_match_idx = np.argmax(similarity_scores)

    if similarity_scores[best_match_idx] > 0.5:
        return knowledge_base[questions[best_match_idx]]
    else:
        return "Sorry, I couldn't find an answer. Try rephrasing your question."

st.title("CLATGuru Chatbot")
st.write("Hi! Ask me anything about CLAT (syllabus, exam pattern, cut-offs, etc.).")

user_query = st.text_input("Your Query", "")

if user_query:
    answer = chatbot_response(user_query)
    st.markdown("**CLATGuru:**")
    st.write(answer)
