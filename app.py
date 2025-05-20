from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

questions = [
    "How do I contact HR?",
    "What is the leave policy?",
    "Tell me about the office hours.",
    "I want to apply for leave.",
    "What are the holidays this year?",
    "Exit the chat"
]

responses = {
    "1": "You can contact HR at hr@example.com.",
    "2": "Employees are entitled to 18 days of paid leave per year.",
    "3": "Office hours are 9 AM to 6 PM, Monday to Friday.",
    "4": "To apply for leave, use the HR portal or email HR directly.",
    "5": "Check the HR portal for the latest list of holidays.",
    "6": "Thank you! Have a great day 😊 You can refresh the page to restart the chat.",
    "contact": "You can contact HR at hr@example.com.",
    "leave": "Employees are entitled to 18 days of paid leave per year.",
    "office": "Office hours are 9 AM to 6 PM, Monday to Friday.",
    "apply": "To apply for leave, use the HR portal or email HR directly.",
    "holiday": "Check the HR portal for the latest list of holidays.",
    "exit": "Thank you! Have a great day 😊 You can refresh the page to restart the chat."
}

@app.route('/')
def index():
    return render_template('index.html', questions=questions)

@app.route('/chatbot', methods=['POST'])
def chatbot():
    data = request.get_json()
    message = data.get('message', '').lower().strip()

    response = responses.get(message, "Sorry, I didn't understand that. Please contact HR at hr@example.com.")
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
