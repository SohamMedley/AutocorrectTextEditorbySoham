from flask import Flask, render_template, request, jsonify
from autocorrect import Speller
import re

app = Flask(__name__)

# Initialize the Speller from autocorrect
spell = Speller(lang='en')

# Whitelist of common Indian names and places (extend this dictionary as needed)
whitelist = {
    "raj": "Raj",
    "soham": "Soham",
    "amey": "Amey",
    "durvesh": "Durvesh",
    "shravani": "Shravani",
    "ayush": "Ayush",
    "vikas": "Vikas",
    "priya": "Priya",
    "ravi": "Ravi",
    "amit": "Amit",
    "sanjay": "Sanjay",
    "neha": "Neha",
    "maharashtra": "Maharashtra",
    "mumbai": "Mumbai",
    "navi": "Navi",
    "pune": "Pune",
    "dombivali": "Dombivali",
    "thane": "Thane",
    "ghatkopar": "Ghatkopar",
    "dadar": "Dadar",
    # ... add additional names/places as desired up to 100 entries ...
}

def smart_autocorrect_text(text):
    """
    Tokenize the input text (words and punctuation), then apply autocorrection 
    to words not in the whitelist. This approach uses regex to preserve punctuation.
    """
    # Split text into tokens (words and punctuation)
    tokens = re.findall(r'\w+|[^\w\s]', text, re.UNICODE)
    corrected_tokens = []
    for token in tokens:
        if re.match(r'\w+', token):
            lower = token.lower()
            if lower in whitelist:
                corrected_tokens.append(whitelist[lower])
            else:
                # Use autocorrect's Speller for correction
                corrected_tokens.append(spell(token))
        else:
            corrected_tokens.append(token)
    corrected_text = " ".join(corrected_tokens)
    # Clean up spaces before punctuation
    corrected_text = re.sub(r'\s([,.!?])', r'\1', corrected_text)
    return corrected_text

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/autocorrect', methods=['POST'])
def autocorrect():
    data = request.get_json()
    text = data.get("text", "")
    corrected_text = smart_autocorrect_text(text)
    # Capitalize the first character if needed
    if corrected_text:
        corrected_text = corrected_text[0].upper() + corrected_text[1:]
    # Preserve trailing space if it exists
    if text.endswith(" "):
        corrected_text += " "
    return jsonify({"correctedText": corrected_text})

if __name__ == '__main__':
    app.run(debug=True)
