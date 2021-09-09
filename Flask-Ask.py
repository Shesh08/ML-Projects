import flask as Flask
app = Flask(__name__)
@app.route('/')
def homepage():
    return"Hi there, hi are you doing?"

if __name__ == '__main__':
    app.run(debug=True)

@ask.launch
def start_skill():
    welcome_message = 'Hello ther! Would you like the news?'
    return question(welcome_message)

@ask.intent("YesIntent")
def share_headlines():
    headlines = get_headlines()
    headline_msg = 'The current news headlines are {}'.format(headlines)
    return statement(headline_msg)

@ask.intent("NoIntent")
def no_intent():
    bye_text = 'I am not sure why you asked me to run then, but okay...bye'
    return statement(bye_text)
