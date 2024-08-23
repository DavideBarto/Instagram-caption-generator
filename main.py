from flask import Flask, request, render_template, jsonify
import openai

app = Flask(__name__)

# Set up your OpenAI API key
openai.api_key = 'YOUR_OPENAI_API_KEY'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_caption', methods=['POST'])
def generate_caption():
    description = request.form['description']
    
    if not description:
        return jsonify({'error': 'Description is required'}), 400
    
    # Generate a caption using GPT-4
    caption = generate_caption_from_description(description)
    
    return jsonify({'caption': caption})

def generate_caption_from_description(description):
    prompt = f"Generate an Instagram caption based on the following description: {description}"
    
    # Use the new `openai.ChatCompletion.create` method
    response = openai.ChatCompletion.create(
        model="gpt-4",  # or "gpt-3.5-turbo" if you are using GPT-3.5
        messages=[
            {"role": "system", "content": "You are a helpful assistant that generates Instagram captions."},
            {"role": "user", "content": prompt},
        ],
        max_tokens=50,
        temperature=0.7,
    )
    
    # Extract the generated caption
    caption = response.choices[0].message['content'].strip()
    return caption

if __name__ == '__main__':
    app.run(debug=True)
