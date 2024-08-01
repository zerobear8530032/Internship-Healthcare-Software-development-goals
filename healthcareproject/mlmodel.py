from flask import Flask, request, render_template
import pickle
import random
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import requests
#  for people who is using this first time you need to install this :
# nltk.download('stopwords')
# nltk.download('wordnet')

app = Flask(__name__)

# Load the model and vectorizer
with open('pickle/model.pkl', 'rb') as file:
    model = pickle.load(file)

with open('pickle/vectorizer.pkl', 'rb') as file:
    vectorizer = pickle.load(file)

def preprocess_text(text):
    text = text.lower()
    words = text.split()
    stop_words = set(stopwords.words('english'))
    lemmatizer = WordNetLemmatizer()
    words = [lemmatizer.lemmatize(word) for word in words if word not in stop_words]
    return ' '.join(words)

def google_search(query, api_key, cx):
    url = 'https://www.googleapis.com/customsearch/v1'
    params = {
        'key': api_key,
        'cx': cx,
        'q': query
    }
    response = requests.get(url, params=params)
    return response.json()


def  getresources(emotion):
    search_terms = {
    0: [
        "mental health support resources",
        "coping strategies for stress",
        "ways to improve mood",
        "emotional support resources",
        "self-care tips for tough times"
    ],
    1: [
        "positivity and motivation tips",
        "ways to stay positive",
        "inspirational stories",
        "positive affirmations",
        "motivational articles"
    ],
    2: [
        "general assistance resources",
        "customer service best practices",
        "helpful advice for users",
        "how to provide effective support",
        "guidance for user queries"
    ],
    3: [
        "anger management techniques",
        "ways to manage frustration",
        "resources for controlling anger",
        "strategies for anger relief",
        "help with managing anger"
    ],
    4: [
        "resources for managing sadness",
        "comforting activities for emotional well-being",
        "support for dealing with sadness",
        "ways to find comfort in tough times",
        "coping with feelings of sadness"
    ],
    5: [
        "health tips and resources",
        "latest health articles",
        "health and wellness updates",
        "valuable health information",
        "health tips for staying well"
    ]
    }
    api_key = 'AIzaSyC2sfEhQElHIjmGzd2P9Gq-aFbPnRigpNU'
    cx = 'e1786b722786945da'
    query = 'Artificial Intelligence'

    searchfor =random.choice(search_terms[emotion])
    searchresult=google_search(searchfor,api_key=api_key,cx=cx)
    return searchresult
    




# def predict_sentiment(text):
#     processed_text = preprocess_text(text)
#     text_vec = vectorizer.transform([processed_text])
#     prediction = model.predict(text_vec)
#     replies = {
#         0: ["I'm sorry to hear that. Here are some resources that might help.",
#             "It seems like you're having a tough time. How about taking a break and doing something you enjoy?",
#             "Remember, it's okay to feel down sometimes. Here are some tips to lift your mood.",
#             "I understand that things might be challenging right now. You are not alone.",
#             "It's important to acknowledge how you feel. Here are some ways to cope.",
#             "Sometimes it helps to talk to someone. Consider reaching out to a friend or counselor.",
#             "I’m here for you. Here are some resources to support you.",
#             "Feeling down is okay. Here are some strategies that might help improve your mood.",
#             "It’s tough when things aren’t going well. Here are a few ideas to help you get through it.",
#             "Your feelings are valid. Here are some suggestions to help manage them.",
#             "Take some time for yourself. Here are some activities that could boost your mood.",
#             "It’s okay to take a step back and breathe. Here are some resources to support you.",
#             "Remember, every day is a new opportunity. Here are some ways to find comfort.",
#             "It’s okay to seek help when you need it. Here are some support options.",
#             "You’re not alone in this. Here are some ways to find comfort and support.",
#             "Sometimes just talking about it can help. Here are some resources you might find useful.",
#             "It’s important to care for yourself. Here are some suggestions for self-care.",
#             "Hang in there. Here are some resources and tips to help you through this time.",
#             "Remember to be kind to yourself. Here are some ways to practice self-compassion.",
#             "It's okay to ask for help. Here are some resources that could be beneficial.",
#             "Sometimes it’s the small things that can make a difference. Here are some suggestions.",
#             "It’s important to reach out when you need support. Here are some options for help.",
#             "Here are some tips that might help lift your spirits. Remember, it’s okay to take things one day at a time.",
#             "Take a moment for yourself. Here are some calming techniques you might find helpful.",
#             "It’s okay to have tough days. Here are some resources to help you navigate through them."
#         ],
#         1: ["That's great to hear! Keep up the positive vibes.",
#             "Awesome! It sounds like you're doing well. Keep it up!",
#             "It's wonderful to see you in high spirits. Stay positive!",
#             "You’re on the right track! Keep the positive energy going.",
#             "Fantastic! Your positivity is inspiring. Keep it up!",
#             "Great to hear! Let’s maintain this positive momentum.",
#             "Wonderful news! It’s great to see you feeling good.",
#             "I’m glad to hear you’re feeling positive. Keep shining!",
#             "It’s awesome to see you in a good place. Keep spreading those good vibes!",
#             "Amazing! Your positivity is truly uplifting.",
#             "It’s great that you’re feeling well. Here’s to more positive days ahead!",
#             "Your positive outlook is refreshing. Keep up the great work!",
#             "So glad to hear you’re feeling good. Let’s keep this positivity going!",
#             "It’s fantastic to see you happy. Keep enjoying the good moments!",
#             "Awesome to hear! Your positive attitude is truly commendable.",
#             "Wonderful news! Keep embracing the positivity.",
#             "It’s great to see you in high spirits. Here’s to more of this!",
#             "Your positive energy is great. Keep enjoying these good feelings!",
#             "Fantastic to hear you’re feeling upbeat. Let’s maintain this positivity!",
#             "So glad to hear you’re doing well. Keep up the positive attitude!",
#             "Your positive vibes are contagious. Keep spreading them!",
#             "Great to hear! Your happiness is truly inspiring.",
#             "Wonderful to hear you’re feeling good. Keep that positivity flowing!",
#             "It’s amazing to see you in a positive space. Keep it up!"
#         ],
#         2: ["Thanks for sharing. How can I assist you further?",
#             "Got it. Is there anything specific you'd like to talk about?",
#             "I understand. Let me know if there's anything you need.",
#             "Thank you for your input. How can I help you today?",
#             "I appreciate you sharing that. What would you like to do next?",
#             "Got your message. Is there something specific you need assistance with?",
#             "Thank you for letting me know. How can I be of help?",
#             "I’m here to help. What would you like to discuss further?",
#             "I appreciate the information. How can I support you?",
#             "Thanks for the update. What can I assist you with next?",
#             "Thank you for sharing. How can I help you move forward?",
#             "I see. Let me know how I can assist you.",
#             "Got it. Please let me know if there’s anything specific you need.",
#             "Thank you for providing this information. What would you like to do next?",
#             "Thanks for sharing. How can I assist you with this?",
#             "I understand. How can I help you further?",
#             "Got it. If you need any further assistance, just let me know.",
#             "Thanks for your input. What can I help you with?",
#             "I appreciate you sharing. How can I assist you going forward?",
#             "Thank you for the information. Is there anything specific you need?",
#             "Got your message. What can I do to help you today?",
#             "Thanks for providing that information. How can I support you?",
#             "I see. How can I be of assistance?",
#             "Thank you for sharing. Let me know how I can assist you further.",
#             "Got it. If you have any specific needs, just let me know."
#         ],
#         3: ["It seems like you're upset. Here are some techniques to calm down.",
#             "I'm sorry you're feeling this way. Let's try to find a solution.",
#             "Anger can be tough to manage. Here are some resources that might help.",
#             "I understand you’re feeling frustrated. Here are some strategies to help you cope.",
#             "It’s important to address anger in a healthy way. Here are some techniques to consider.",
#             "Managing anger can be challenging. Here are some resources to help you navigate through it.",
#             "It’s okay to feel angry. Here are some tips to help you calm down.",
#             "Anger is a natural emotion. Here are some ways to help you manage it.",
#             "I’m sorry you’re feeling this way. Here are some methods to help with anger management.",
#             "Sometimes it helps to talk about it. Here are some techniques to help you process your feelings.",
#             "It’s important to find healthy ways to deal with anger. Here are some suggestions.",
#             "I understand that anger can be overwhelming. Here are some resources to support you.",
#             "Anger can be difficult to handle. Here are some techniques to help you manage it.",
#             "It’s okay to feel angry, but it’s important to find ways to manage it. Here are some tips.",
#             "I’m here to help. Here are some strategies to manage anger effectively.",
#             "Sometimes it helps to take a step back. Here are some techniques for managing anger.",
#             "Managing anger can be tough. Here are some resources and tips to help you through it.",
#             "It’s important to address anger in a constructive way. Here are some suggestions.",
#             "I understand you’re upset. Here are some ways to cope with anger.",
#             "Anger management techniques can be helpful. Here are some you might find useful.",
#             "It’s important to find healthy outlets for anger. Here are some resources to consider.",
#             "Managing your emotions is key. Here are some strategies for handling anger.",
#             "It’s okay to seek help when dealing with anger. Here are some resources to assist you.",
#             "Sometimes taking a break can help. Here are some anger management techniques you might find helpful.",
#             "It’s important to take care of your emotional well-being. Here are some ways to manage anger."
#         ],
#         4: ["I'm sorry to hear that you're feeling sad. Here are some comforting thoughts.",
#             "It's okay to feel sad sometimes. Here are some ways to cope.",
#             "I'm here for you. Here are some resources that might help.",
#             "Feeling sad is a normal part of life. Here are some tips to help you feel better.",
#             "It’s important to acknowledge your feelings. Here are some ways to find comfort.",
#             "Sometimes it helps to talk about it. Here are some resources for support.",
#             "I’m sorry you’re feeling this way. Here are some suggestions to help lift your spirits.",
#             "It’s okay to take time for yourself. Here are some activities that might help you feel better.",
#             "Your feelings are valid. Here are some comforting thoughts to consider.",
#             "Sometimes it’s the small things that can help. Here are some suggestions to improve your mood.",
#             "It’s important to care for your emotional well-being. Here are some resources for comfort.",
#             "I understand that you’re feeling down. Here are some ways to cope with sadness.",
#             "It’s okay to seek support when you’re feeling sad. Here are some options for help.",
#             "Feeling sad is a part of life, and it’s okay. Here are some resources to help you through it.",
#             "I’m here to help. Here are some comforting resources for when you’re feeling low.",
#             "Sometimes it helps to reach out to others. Here are some suggestions for support.",
#             "It’s important to acknowledge how you’re feeling. Here are some ways to find comfort.",
#             "I’m sorry you’re going through this. Here are some resources to help you manage sadness.",
#             "It’s okay to feel sad. Here are some comforting thoughts and tips to help you feel better.",
#             "Sometimes talking to someone can help. Here are some resources that might provide comfort.",
#             "It’s important to take care of yourself emotionally. Here are some ways to cope with sadness.",
#             "I understand that you’re feeling down. Here are some comforting ideas to help you feel better.",
#             "It’s okay to have moments of sadness. Here are some resources to help you through it.",
#             "I’m here for you. Here are some comforting tips to help with sadness.",
#             "Sometimes a change of pace can help. Here are some suggestions to lift your mood."
#         ],
#         5: ["Stay informed with our health tips.",
#             "Explore our health resources for more information.",
#             "Check out these articles to learn more.",
#             "We have a variety of health tips available. Here’s something that might interest you.",
#             "Stay updated with our latest health resources.",
#             "Here are some articles to help you stay informed about health.",
#             "Explore our collection of health tips and resources.",
#             "Check out these health-related articles for more information.",
#             "We offer a range of health resources. Here’s something you might find useful.",
#             "Discover our latest health tips and articles.",
#             "Here are some valuable health resources you might find interesting.",
#             "Stay tuned for more health tips and updates.",
#             "We have a selection of health articles that you might enjoy.",
#             "Explore our health resources to stay informed and healthy.",
#             "Check out our latest health tips and updates.",
#             "Here are some helpful health articles for you to read.",
#             "Stay informed with our range of health resources.",
#             "Here’s a collection of articles to keep you updated on health topics.",
#             "Discover our health tips and stay on top of your wellness.",
#             "We have new health resources available. Here’s something for you.",
#             "Stay healthy with our curated health tips.",
#             "Explore our latest articles for more health information.",
#             "Check out our health resources to stay informed.",
#             "Here’s some valuable information to help with your health."]
#     }
#     emotion = prediction[0]
#     if emotion in replies:
#         return random.choice(replies[emotion]), emotion
#     else:
#         return "I'm not sure how to respond. Please try again.", emotion
    
# @app.route('/model', methods=['GET', 'POST'])
# def model():
#     if request.method == 'POST':
#         # Get data from form
#         text = request.form['text']
        
#         # Get reply based on prediction
#         reply, emotion = predict_sentiment(text)
#         resource=  getresources(emotion)
#         # Render template with reply
#         return render_template('model.html', reply=reply, text=text,resource=resource)
    
#     return render_template('model.html', reply=None)

if __name__ == '__main__':
    app.run(debug=True)