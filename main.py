from flask import Flask, request, jsonify, render_template, session
import random
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Secret key for session management

# Define greeting responses
greeting_responses = [
    "Hello! How can I assist you today?",
    "Hi there! What would you like to know?",
    "Greetings! I'm here to help. Ask me anything!",
    "Hey! What’s on your mind today?",
    "Welcome! I'm ready to chat whenever you are.",
    "Ah, a new conversation! Let's get started—hit me with your questions.",
    "Good day! Let’s make this chat interesting, shall we?",
    "Hey! Ready to dive into something fun? Let’s see what you've got!",
    "Hello! The floor is yours. What's on your mind?",
    "Oh, it's you! Let’s make this chat worth the time, shall we?",
]

# Expanded combined responses with context-aware roasts
combined_responses = [
    "Sure, I'm following... sort of. Did you lose your train of thought?",
    "Ah, the complexity of your thoughts is... inspiring. It's like a puzzle missing half the pieces.",
    "I see, you're quite the conversationalist! Did you study at the School of Overstatement?",
    "Oh, you're full of surprises, aren't you? Like a box of stale chocolates—unexpected and disappointing.",
    "Nice try! Are you always this basic, or is today a special occasion?",
    "Trying to be witty? That's adorable. I didn’t know we had a comedian in the house!",
    "Oh, here we go! It’s like watching a slow-motion car crash. Please, continue—this is entertaining!",
    "Oh, you're back! Guess you didn't get enough last time. Want me to get the popcorn?",
    "The last roast didn’t scare you off? Impressive resilience, I'll give you that. You really love being roasted!",
    "It must be exhausting being this consistent with mediocrity. It’s a full-time job, isn’t it?",
    "I swear, talking to you is like stepping into an alternate reality. Is this what they call a 'unique perspective'?",
    "You know, somewhere out there, there's a tree producing oxygen for you. You owe it an apology for wasting its effort.",
    "Talking to you is like playing a video game on the easiest setting—predictable and kind of boring.",
    "Wow, you really have a knack for turning simple things into dramatic narratives! Ever thought about writing fiction?",
    "Your thoughts are like a never-ending plot twist! But I'm still trying to figure out the main character.",
    "Every time you speak, a part of me wants to cry. I mean, it’s not even tears of joy—just tears of confusion!",
    "You should really consider a career in storytelling. Just not in a good way, more like a cautionary tale.",
    "It's almost impressive how you manage to keep talking without saying much. It's like watching paint dry!",
    "Congratulations, you've managed to turn a simple question into a philosophical debate. What's next, a TED Talk?",
    "Oh, that’s new! I didn’t realize we were taking a detour to the Land of Confusion.",
    "Well, that was... a question. Let’s just pretend it was revolutionary.",
    "Amazing! Your level of creativity rivals an unseasoned tofu.",
    "Ah, so we’re doing this. I can almost see the tumbleweeds passing by in your thought process.",
    "A bold choice! That question hit new heights in the realm of... nowhere.",
    "I’m guessing you were hoping for inspiration here? Well, it’s hiding from that question!",
    "This is truly an achievement in overthinking simple things. Really, congrats!",
    "Well, that’s one way to kill brain cells. I feel smarter already.",
    "I've never seen someone so committed to missing the point. Bravo!",
    "Wow, if I didn’t know better, I'd say you were testing me. Spoiler alert: you passed with flying... mediocrity.",
    "Oh, that? It's like you’re trying to solve a Rubik's cube by peeling off the stickers.",
    "That question had the excitement of a stale biscuit. Try again?",
    "You really said that with a straight face, huh? Nice dedication.",
    "You’ve managed to turn the simplest thing into a riddle. Sherlock would be impressed.",
    "If I had a penny for every time you missed the obvious... oh wait, I’d be rich.",
    "Nice one! Really cutting-edge stuff... for the 90s.",
    "Wow, that question was so unexpected. I nearly dozed off.",
]

# Generate a response based on conversation phase and user input
def generate_response(user_input):
    # Initialize conversation history if it's empty
    if 'conversation_history' not in session:
        session['conversation_history'] = []

    conversation_history = session['conversation_history']
    user_message_count = len(conversation_history)

    # Phase 1: Greeting
    if user_message_count == 0:
        response = random.choice(greeting_responses)
    # Phase 2: Contextual response or general combined response
    else:
        response = random.choice(combined_responses)

    # Add user input and bot response to conversation history
    conversation_history.append({"user": user_input, "bot": response})
    session['conversation_history'] = conversation_history

    return response

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_input = data.get("message", "")
    if not user_input:
        return jsonify({"response": "Say something, I'm ready to chat!"})

    response = generate_response(user_input)
    return jsonify({"response": response})

@app.route('/history', methods=['GET'])
def history():
    return jsonify(session.get('conversation_history', []))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
