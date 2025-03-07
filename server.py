from flask import Flask, render_template, request, jsonify
from autocorrect import Speller
import re

app = Flask(__name__)
spell = Speller(lang='en')

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
    "dadar": "Dadar"
}

def smart_autocorrect_text(text):
    tokens = re.findall(r'\s+|\S+', text)
    corrected_tokens = []
    for token in tokens:
        if token.isspace():
            corrected_tokens.append(token)
        else:
            stripped = re.sub(r'[^\w]', '', token).lower()
            if stripped in whitelist:
                prefix = re.match(r'^\W*', token).group(0)
                suffix = re.search(r'\W*$', token).group(0)
                corrected_tokens.append(prefix + whitelist[stripped] + suffix)
            else:
                try:
                    corrected_tokens.append(spell(token))
                except Exception:
                    corrected_tokens.append(token)
    corrected_text = "".join(corrected_tokens)
    if corrected_text:
        corrected_text = corrected_text[0].upper() + corrected_text[1:]
    return corrected_text

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/autocorrect', methods=['POST'])
def autocorrect_route():
    data = request.get_json()
    text = data.get("text", "")
    corrected_text = smart_autocorrect_text(text)
    if text.endswith(" ") and not corrected_text.endswith(" "):
        corrected_text += " "
    return jsonify({"correctedText": corrected_text})

if __name__ == '__main__':
    app.run(debug=True)
