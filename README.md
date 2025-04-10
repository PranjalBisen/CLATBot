# CLATGuru Chatbot

**CLATGuru Chatbot** is a Streamlit-based application designed to assist law aspirants with CLAT (Common Law Admission Test) related queries. It leverages a hybrid approach by matching user queries against an internal knowledge base using TF-IDF and cosine similarity. This project demonstrates the application of NLP techniques to build an interactive mentorship/engagement tool.

---

## 📌 Table of Contents
- [Project Overview](#project-overview)  
- [Features](#features)  
- [Setup Instructions](#setup-instructions)  
- [Usage](#usage)  
- [Project Structure](#project-structure)  
- [Bonus: Scaling to a GPT-Based Model](#bonus-scaling-to-a-gpt-based-model)  
- [Dependencies](#dependencies)  
- [Contact](#contact)  

---

## 🚀 Project Overview

CLATGuru Chatbot is a lightweight tool that:

- Answers common CLAT-related questions (e.g., syllabus, exam pattern, cut-offs).
- Uses `spaCy` for text preprocessing (lemmatization, stopword and punctuation removal).
- Employs TF-IDF vectorization with cosine similarity to match user queries to known questions.
- Provides an interactive and responsive interface using Streamlit.

---

## ✨ Features

### 📚 Knowledge Base
- Pre-defined FAQs about CLAT: syllabus, eligibility, exam pattern, application fee, etc.

### 🧠 NLP Pipeline
- Text normalization using `spaCy`
- Vectorization using `TF-IDF`
- Semantic matching via `cosine similarity`

### 💬 User-Friendly Interface
- Real-time responses through a simple and modern Streamlit app

---

## 🛠️ Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/your_username/CLATBot.git
cd CLATGuruChatbot
```

### 2. Install Dependencies
Ensure Python 3.7+ is installed. Then run:
```bash
pip install streamlit spacy scikit-learn numpy
python -m spacy download en_core_web_sm
```

### 3. Run the App
```bash
streamlit run app.py
```

---

## 🧑‍💻 Usage

1. Launch the app using the above command. It will open in your default browser.
2. Enter your CLAT-related query in the text box.
3. The chatbot will respond based on the most relevant match from its knowledge base.
4. To improve performance or coverage, update the internal knowledge base with more Q&A.

---

## 📁 Project Structure

```
CLATGuruChatbot/
├── app.py            
├── clat_chatbot.py  
├── README.md         
```

---

## 📈 Bonus: Scaling to a GPT-Based Model

To enhance this chatbot using a transformer-based model:

### Step 1: Collect Data  
Gather NLTI mentorship content, FAQs, and resources.

### Step 2: Format as QA Pairs  
Clean and structure the data into prompts and responses.

### Step 3: Fine-Tune GPT  
Use Hugging Face Transformers to fine-tune a model like GPT-2.

### Step 4: Deploy  
Deploy the model via Hugging Face Spaces or a custom API.

### Step 5: Integrate  
Use the GPT model as a fallback or enhancement for open-ended questions.

---

## 📦 Dependencies

- Python 3.7+
- Streamlit  
- spaCy  
- scikit-learn  
- NumPy  
- (Optional) transformers, datasets

---

## 📬 Contact

**Name**: Pranjal D. Bisen  
**Email**: your.email@example.com

---
