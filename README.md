# 🧙‍♂️ TextWizard

**Elevate your text game with powerful text transformation tools!**

TextWizard is a modern web application built with Django that provides various text processing operations through an intuitive and responsive interface. Transform your text with just a few clicks!

![TextWizard Screenshot](https://img.shields.io/badge/Django-5.0.6-green?style=flat&logo=django)
![Bootstrap](https://img.shields.io/badge/Bootstrap-4.6.2-purple?style=flat&logo=bootstrap)
![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat&logo=python)

## ✨ Features

### 🔧 Text Operations

- **Remove Punctuations** - Clean punctuation marks from your text
- **UPPERCASE Conversion** - Transform text to ALL CAPS
- **lowercase conversion** - Transform text to all lowercase
- **Title Case** - Capitalize Each Word Beautifully
- **New Line Remover** - Remove line breaks and make text continuous
- **Extra Space Remover** - Clean up unnecessary spaces between words
- **Remove Numbers** - Strip all numeric digits (0-9) from text

### 🎨 User Interface

- **Responsive Design** - Works perfectly on desktop, tablet, and mobile
- **Real-time Typing Animation** - Dynamic heading with Typed.js
- **Live Statistics** - Character, word, and line count on results
- **Copy to Clipboard** - One-click copying of processed text
- **Download Results** - Save your processed text as a .txt file
- **Mutual Exclusivity** - Smart toggle behavior (prevents UPPERCASE + lowercase)

### 🚀 Technical Features

- **Django 5.0.6** - Modern Python web framework
- **Bootstrap 4.6.2** - Responsive CSS framework
- **SQLite Database** - Lightweight database for development
- **Fixed Footer** - Professional layout with consistent branding
- **Form Validation** - Prevents conflicting operations

## 🛠️ Installation & Setup

### Prerequisites

- Python 3.x
- Git

### Quick Start

1. **Clone the repository**

   ```bash
   git clone https://github.com/joshiGaurav-2712/TextWizard.git
   cd TextWizard
   ```

2. **Set up virtual environment**

   ```bash
   # Windows
   python -m venv env
   env\Scripts\activate

   # macOS/Linux
   python3 -m venv env
   source env/bin/activate
   ```

3. **Install dependencies**

   ```bash
   pip install django==5.0.6
   ```

4. **Run the development server**

   ```bash
   cd mysite
   python manage.py runserver
   ```

5. **Open in browser**
   Navigate to `http://127.0.0.1:8000/` and start transforming text!

## 📖 Usage

### Basic Workflow

1. **Enter Text** - Type or paste your text in the main textarea (up to 10,000 characters)
2. **Select Operations** - Toggle one or more text transformation options
3. **Analyze** - Click the "Analyze text" button to process your text
4. **View Results** - See your transformed text with statistics
5. **Copy/Download** - Use the action buttons to copy or save results

### Operation Examples

| Operation           | Input                | Output         |
| ------------------- | -------------------- | -------------- |
| Remove Punctuations | `Hello, World!`      | `Hello World`  |
| UPPERCASE           | `hello world`        | `HELLO WORLD`  |
| Title Case          | `hello world`        | `Hello World`  |
| Remove Numbers      | `Call me at 123-456` | `Call me at -` |
| Remove Extra Spaces | `hello    world`     | `hello world`  |

### Pro Tips

- ✅ Combine multiple operations for complex text transformations
- ✅ Operations are applied sequentially in the order they appear
- ✅ Use "Clear" button to quickly reset the input field
- ✅ UPPERCASE and lowercase toggles are mutually exclusive

## 🏗️ Project Structure

```
TextWizard/
├── env/                          # Virtual environment
├── mysite/                       # Django project
│   ├── manage.py                 # Django management script
│   ├── db.sqlite3               # SQLite database
│   ├── mysite/                  # Main application
│   │   ├── __init__.py
│   │   ├── settings.py          # Django configuration
│   │   ├── urls.py              # URL routing
│   │   ├── views.py             # Business logic
│   │   ├── wsgi.py              # WSGI configuration
│   │   └── asgi.py              # ASGI configuration
│   └── templates/               # HTML templates
│       ├── index.html           # Homepage
│       └── analyze.html         # Results page
└── README.md                    # This file
```

## 🔧 Technical Details

### Backend (Django)

- **Framework**: Django 5.0.6
- **Database**: SQLite3 (development)
- **Views**: Function-based views for simplicity
- **Templates**: Django template engine with Bootstrap

### Frontend

- **CSS Framework**: Bootstrap 4.6.2
- **JavaScript**: Vanilla JS + Typed.js for animations
- **Responsive**: Mobile-first design
- **Accessibility**: ARIA labels and screen reader support

### Text Processing Pipeline

1. Form data validation
2. Sequential operation application
3. Result generation with statistics
4. Template rendering with processed data

## 🌐 API Endpoints

| Endpoint   | Method | Description                     |
| ---------- | ------ | ------------------------------- |
| `/`        | GET    | Homepage with text input form   |
| `/analyze` | POST   | Process text and return results |


### Development Setup

```bash
# Install development dependencies
pip install django==5.0.6

# Run tests (when available)
python manage.py test

# Check for issues
python manage.py check
```


## 📊 Project Stats

- **Language**: Python
- **Framework**: Django 5.0.6
- **Frontend**: Bootstrap 4.6.2 + Vanilla JavaScript
- **Database**: SQLite3
- **Text Operations**: 7 unique transformations


---

