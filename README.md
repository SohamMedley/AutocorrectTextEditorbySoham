```md
# Smart Text Editor

Smart Text Editor is a modern, premium text editor with live autocorrect, spell-check, and grammar suggestions built with HTML, CSS, JavaScript, and Python (Flask). This project features a sleek dark theme with red, blue, and black accents.

## Overview

Smart Text Editor offers a rich text editing experience with:
- **Live Autocorrect:** Automatically corrects words as you type. Corrections trigger after each space (with a debounce) using the Python `autocorrect` package while preserving common Indian names and places via a custom whitelist.
- **Rich Text Formatting:** Format your text easily with Bold, Italic, and Underline commands.
- **Custom File Saving:** Save your work as a text file with a custom file name (if no name is provided, the download is cancelled).
- **Premium Dark UI:** Enjoy a sophisticated design with animated backgrounds and a dynamic dark color scheme.

## Features

- **Autocorrect:** Smart correction of common typos with minimal interference on proper names.
- **Text Formatting:** Use an intuitive toolbar for Bold, Italic, and Underline formatting.
- **Dynamic UI:** Responsive interface built with modern design principles.
- **File Download:** Prompt-based file saving that prevents accidental downloads when no name is entered.

## Installation & Running

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/smart-text-editor.git
   ```
2. **Navigate to the Project Directory:**
   ```bash
   cd smart-text-editor
   ```
3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Run the Flask Server:**
   ```bash
   python server.py
   ```
5. **Open Your Browser:**
   Visit [http://127.0.0.1:5000](http://127.0.0.1:5000) to access the editor.

## Project Structure

```
text-editor/
├── static/
│   ├── css/
│   │   └── styles.css
│   └── js/
│       └── script.js
├── templates/
│   └── index.html
├── server.py
├── requirements.txt
└── README.md
```

## Technologies Used

- **HTML5 & CSS3**
- **JavaScript (ES6)**
- **Python (Flask)**
- **Autocorrect Package**

## About the Developer

This project was developed by **Soham**, a Computer Engineering student at **DY Patil College**, for his friend **Raj**. It represents a blend of modern design and smart functionality aimed at creating a seamless text editing experience.

## License

This project is licensed under the [MIT License](LICENSE).

---

Thank you for checking out my project!
```
