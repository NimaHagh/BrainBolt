from flask import Flask, render_template, request
from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
import os

# Load environment variables (OpenAI API key)
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# Set up OpenAI model
model = ChatOpenAI(model="gpt-3.5-turbo")

@app.route('/')
def landing_page():
    # Render the new landing page
    return render_template('landing.html')

@app.route('/form')
def form_page():
    # Render the form page when "Get Started" is clicked
    return render_template('form.html')

@app.route('/generate', methods=['POST'])
def generate_ideas():
    # Get data from the form
    topic = request.form['topic']
    members = request.form['members']
    goal = request.form['goal']
    method = request.form['method']

    # Define brainstorming methods
    if method == "mind_map":
        messages = [
            ("system", "You are a brainstorming assistant who helps create mind maps."),
            ("human", f"We are brainstorming about '{topic}' with {members} members. Our goal is: {goal}. Create a mind map with ideas around this topic.")
        ]
    elif method == "word_association":
        messages = [
            ("system", "You are a brainstorming assistant who uses random word association to generate ideas."),
            ("human", f"We are brainstorming about '{topic}' with {members} members. Our goal is: {goal}. Use random word association to generate creative ideas around this topic.")
        ]

    # Create the LangChain prompt
    prompt_template = ChatPromptTemplate.from_messages(messages)
    prompt = prompt_template.invoke({
        "topic": topic,
        "members": members,
        "goal": goal
    })

    # Call the OpenAI model
    result = model.invoke(prompt)

    # Separate the replacement of newlines from the f-string
    brainstormed_ideas = result.content.replace('\n', '<br>')

    # Return the formatted HTML with brainstormed ideas
    return f"<h1>Brainstormed Ideas</h1><p>{brainstormed_ideas}</p>"


if __name__ == '__main__':
    app.run(debug=True)
