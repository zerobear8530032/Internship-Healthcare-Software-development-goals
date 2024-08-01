from flask import Flask, request, render_template
import pickle
import random
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

nltk.download('stopwords')
nltk.download('wordnet')

app = Flask(__name__)

# Load the model and vectorizer
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

with open('vectorizer.pkl', 'rb') as file:
    vectorizer = pickle.load(file)

def preprocess_text(text):
    text = text.lower()
    words = text.split()
    stop_words = set(stopwords.words('english'))
    lemmatizer = WordNetLemmatizer()
    words = [lemmatizer.lemmatize(word) for word in words if word not in stop_words]
    return ' '.join(words)

def predict_sentiment(text):
    processed_text = preprocess_text(text)
    text_vec = vectorizer.transform([processed_text])
    prediction = model.predict(text_vec)
    replies = {
        0: ["I'm sorry to hear that. Here are some resources that might help.",
            "It seems like you're having a tough time. How about taking a break and doing something you enjoy?",
            "Remember, it's okay to feel down sometimes. Here are some tips to lift your mood."],
        1: ["That's great to hear! Keep up the positive vibes.",
            "Awesome! It sounds like you're doing well. Keep it up!",
            "It's wonderful to see you in high spirits. Stay positive!"],
        2: ["Thanks for sharing. How can I assist you further?",
            "Got it. Is there anything specific you'd like to talk about?",
            "I understand. Let me know if there's anything you need."],
        3: ["It seems like you're upset. Here are some techniques to calm down.",
            "I'm sorry you're feeling this way. Let's try to find a solution.",
            "Anger can be tough to manage. Here are some resources that might help."],
        4: ["I'm sorry to hear that you're feeling sad. Here are some comforting thoughts.",
            "It's okay to feel sad sometimes. Here are some ways to cope.",
            "I'm here for you. Here are some resources that might help."],
        5: ["Stay informed with our health tips.",
            "Explore our health resources for more information.",
            "Check out these articles to learn more."]
    }
    return replies[prediction[0]][random.randint(0, 2)]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get data from form
        text = request.form['text']
        
        # Get reply based on prediction
        reply = predict_sentiment(text)
        
        # Render template with reply
        return render_template('index.html', reply=reply, text=text)
    
    return render_template('index.html', reply=None)

if __name__ == '__main__':
    app.run(debug=True)
