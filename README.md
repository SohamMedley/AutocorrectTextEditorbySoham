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
