import os
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv

# Import modern LangChain classes
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

@app.route('/')
def index():
    """Serves the main application page."""
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_article():
    """Generates an article based on the provided topic using LangChain and OpenAI-compatible API."""
    try:
        # Get JSON data from the frontend request
        data = request.get_json() or {}
        topic = data.get('topic', '').strip()

        # 1. Validate that the topic is not empty
        if not topic:
            return jsonify({"error": "Please enter an article topic."}), 400

        # 2. Retrieve and validate AI API configuration
        api_key = os.getenv("OPENAI_API_KEY")
        base_url = os.getenv("OPENAI_BASE_URL")
        model_name = os.getenv("OPENAI_MODEL")

        # Check if the API key is missing or set to placeholder
        if not api_key or api_key == "your_api_key_here":
            return jsonify({"error": "AI API configuration is missing. Please check your .env file."}), 400

        # 3. Setup the LangChain LLM using the configured environment variables
        # If base_url is a placeholder or not provided, we pass None to let langchain use default OpenAI endpoint
        llm_base_url = None
        if base_url and base_url != "your_base_url_here":
            llm_base_url = base_url

        # Check if model_name is configured, otherwise fallback to a default
        llm_model = "gpt-3.5-turbo"
        if model_name and model_name != "your_model_here":
            llm_model = model_name

        llm = ChatOpenAI(
            api_key=api_key,
            base_url=llm_base_url,
            model=llm_model,
            temperature=0.7
        )

        # 4. Create the prompt template
        # We instruct the model to return the title on the first line, then the body in Markdown format.
        prompt = ChatPromptTemplate.from_messages([
            ("system", (
                "You are a professional article writer. Write a well-structured, easy-to-read article "
                "about the given topic. The article must contain: an introduction, clear headings, "
                "useful paragraphs, and a conclusion. Avoid unnecessary repetition.\n\n"
                "CRITICAL FORMATTING INSTRUCTION: The very first line of your response must be the article's title "
                "(without any markdown formatting like '#' or '**', and without 'Title:' prefix). "
                "After the title, add exactly one blank line, and then write the rest of the article in Markdown format."
            )),
            ("user", "Topic: {topic}")
        ])

        # 5. Chain the prompt, model, and output parser together (Modern LangChain Runnable syntax)
        chain = prompt | llm | StrOutputParser()

        # Invoke the LangChain chain to generate the article text
        response_text = chain.invoke({"topic": topic})

        # 6. Parse the response text to separate the title from the article body
        lines = response_text.strip().split('\n')
        title = "Untitled Article"
        body_lines = []

        if lines:
            # Find the first non-empty line as the title
            title_index = 0
            for i, line in enumerate(lines):
                if line.strip():
                    title = line.strip().lstrip('#').replace('**', '').replace('*', '').strip()
                    title_index = i
                    break
            # Everything after the title (plus a blank line) is the body of the article
            body_lines = lines[title_index + 1:]

        article_body = '\n'.join(body_lines).strip()

        # Return the title and article body to the frontend
        return jsonify({
            "title": title,
            "article": article_body
        })

    except Exception as e:
        # Log the actual exception in the console for debugging
        print(f"[ERROR] Article generation failed: {e}")
        # Return a user-friendly error message to the client
        return jsonify({"error": "An error occurred while generating the article. Please check your API configuration or connection."}), 500

if __name__ == '__main__':
    # Run the Flask app on localhost (127.0.0.1) and port 5000
    app.run(host='127.0.0.1', port=5000, debug=True)
