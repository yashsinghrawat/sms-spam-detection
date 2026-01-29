# 📩 SMS Spam Detection Web App

A complete **end-to-end NLP-based SMS Spam Detection system** that classifies messages as **Spam** or **Not Spam** using Machine Learning.  
The project covers the full ML lifecycle — from data preprocessing and model training to **deployment as a live web application**.

🚀 **Live Demo:**  
👉 https://dft79rykjimsh2hrxrfxoe.streamlit.app/

---

## 📌 Project Overview

Spam messages are a common problem in digital communication. This project aims to automatically detect spam SMS messages using **Natural Language Processing (NLP)** and **Supervised Machine Learning** techniques.

The trained model is deployed using **Streamlit Cloud**, allowing users to input any SMS text and instantly receive a prediction.

---

## 🧠 Machine Learning Approach

### 🔹 Problem Type
- Binary Classification  
  - **Spam**
  - **Not Spam (Ham)**

### 🔹 Data Preprocessing
- Lowercasing text
- Tokenization
- Removal of punctuation and stopwords
- Stemming using **Porter Stemmer**

### 🔹 Feature Extraction
- **TF-IDF Vectorization**

### 🔹 Models Trained & Evaluated
- Multinomial Naive Bayes
- Logistic Regression
- Support Vector Machine (SVM)

👉 **Multinomial Naive Bayes** was selected for deployment based on its strong precision–recall balance for imbalanced text data.

---

## 📊 Model Performance
- Accuracy: **~97%**
- Focused on **precision & recall** to minimize false positives in spam detection
- Evaluated using classification metrics and confusion matrix

---

## 🌐 Web App Deployment

- Frontend & inference powered by **Streamlit**
- Model and vectorizer serialized using **pickle**
- Deployed on **Streamlit Cloud**
- Public, shareable URL for real-time predictions

---

## 🛠️ Tech Stack

**Programming Language**
- Python

**Libraries & Frameworks**
- scikit-learn
- NLTK
- Pandas
- NumPy
- Streamlit

**Tools**
- Git & GitHub
- Jupyter Notebook
- Streamlit Cloud
- Linux

---

## 📂 Project Structure

