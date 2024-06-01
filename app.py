import streamlit as st
import pickle
from nltk.corpus import stopwords
import string
import os
import nltk
from nltk.stem.porter import PorterStemmer
ps = PorterStemmer()

nltk.data.path.append(os.path.join(os.path.dirname(__file__), 'nltk_data'))

def transformText(text):
    text = text.lower()
    text = nltk.word_tokenize(text)
    newText = []
    for i in text:
        if i.isalnum():
            newText.append(i)

    text = newText[:]
    newText.clear()
    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            newText.append(ps.stem(i))
    return " ".join(newText)

td = pickle.load(open('vectorizer.pkl','rb'))
mnb = pickle.load(open('model.pkl','rb'))

st.title("Email/SMS Spam Classifier")

#Preprocess
inputText = st.text_area("Enter the Message")
if st.button("Predict"):
    transText = transformText(inputText)

    #Vectorization
    vector = td.transform([transText])

    #Prediction
    ans = mnb.predict(vector)[0]

    if ans==1:
        st.header("SPAM")
    else:
        st.header("NOT SPAM")
