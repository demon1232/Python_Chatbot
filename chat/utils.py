import re
import json
from difflib import get_close_matches
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

with open(os.path.join(BASE_DIR, "chat", "qa_data.json")) as f:
    QA_DATA = json.load(f)

# 🔥 PYTHON TOPICS (EXPANDED 🔥)
PYTHON_TOPICS = {

    # 🔹 BASICS
    "python_intro": {
        "keywords": ["what is python", "python"],
        "response": "Python is a high-level programming language used for web, AI, and automation."
    },

    "django": {
        "keywords": ["django"],
        "response": """Django is a Python web framework.

Features:
- Fast development
- Admin panel
- Secure
"""
    },

    "flask": {
        "keywords": ["flask"],
        "response": "Flask is a lightweight Python web framework."
    },

    "api": {
        "keywords": ["api", "rest api"],
        "response": "API allows communication between systems."
    },

    # 🔹 DATA STRUCTURES
    "list": {
        "keywords": ["list", "lists"],
        "response": "List stores multiple items. Example: [1,2,3]"
    },

    "tuple": {
        "keywords": ["tuple"],
        "response": "Tuple is immutable."
    },

    "dictionary": {
        "keywords": ["dictionary", "dict"],
        "response": "Dictionary stores key-value pairs."
    },

    "set": {
        "keywords": ["set"],
        "response": "Set stores unique values."
    },

    # 🔹 LOOPS
    "for_loop": {
        "keywords": ["for loop", "for"],
        "response": """For loop example:
for i in range(5):
    print(i)
"""
    },

    "while_loop": {
        "keywords": ["while loop", "while"],
        "response": """While loop example:
i = 0
while i < 5:
    i += 1
"""
    },

    "loop": {
        "keywords": ["loop"],
        "response": "Loops repeat tasks using for and while."
    },

    # 🔹 FUNCTIONS
    "function": {
        "keywords": ["function", "def"],
        "response": """Function example:
def add(a,b):
    return a+b
"""
    },

    "lambda": {
        "keywords": ["lambda"],
        "response": "Lambda is a one-line anonymous function."
    },

    # 🔹 OOP
    "class": {
        "keywords": ["class"],
        "response": "Class is a blueprint for objects."
    },

    "object": {
        "keywords": ["object"],
        "response": "Object is instance of class."
    },

    "inheritance": {
        "keywords": ["inheritance"],
        "response": "Child class inherits parent."
    },

    # 🔹 ERRORS
    "error": {
        "keywords": ["error", "bug", "exception"],
        "response": """Common errors:
- SyntaxError
- NameError
- TypeError
"""
    },

    "history": {
        "keywords": ["creator", "history"],
        "response": "Python was created by Guido van Rossum."
    },

    # 🔹 DJANGO ADVANCED
    "django_model": {
        "keywords": ["model"],
        "response": "Model defines database structure in Django."
    },

    "django_view": {
        "keywords": ["view"],
        "response": "View handles request and response."
    },

    "django_template": {
        "keywords": ["template"],
        "response": "Template renders HTML."
    },

    "django_url": {
        "keywords": ["url"],
        "response": "URL routes requests to views."
    },

    "django_admin": {
        "keywords": ["admin"],
        "response": "Django admin is built-in dashboard."
    },

    # 🔹 DATA SCIENCE
    "numpy": {
        "keywords": ["numpy"],
        "response": "NumPy is used for numerical operations."
    },

    "pandas": {
        "keywords": ["pandas"],
        "response": "Pandas is used for data analysis."
    },

    "matplotlib": {
        "keywords": ["matplotlib"],
        "response": "Used for graphs."
    }
}

# ❌ BLOCK OTHER LANGUAGES
NON_PYTHON_KEYWORDS = [
    "javascript", "js", "java", "c++", "cpp", "c#", "php",
    "html", "css", "react", "node", "angular"
]

# 🧠 ERROR SOLUTIONS
ERROR_SOLUTIONS = {
    "indentationerror": "Fix indentation properly.",
    "syntaxerror": "Missing colon or syntax issue.",
    "nameerror": "Variable not defined.",
    "typeerror": "Wrong data types.",
    "indexerror": "List index out of range."
}

# ✅ GREETING
def is_greeting(query):
    return any(word in query.lower() for word in ["hi", "hello", "salam"])


# 🎯 INTENT DETECTION
def detect_intent(query):
    query = query.lower()

    for topic, data in PYTHON_TOPICS.items():
        for keyword in data["keywords"]:
            if keyword in query:
                return topic

    return None


# 🧠 ERROR DETECTION
def detect_error(query):
    query = query.lower()
    for err in ERROR_SOLUTIONS:
        if err in query:
            return ERROR_SOLUTIONS[err]
    return None


# 🧠 CODE CHECK
def is_code(query):
    return "\n" in query or "print(" in query or "def " in query


# 🧠 DEBUG
def debug_code(code):
    if "print " in code:
        return "Use print() with parentheses."
    return None


# 🚀 MAIN
def generate_python_answer(query):
    q = query.lower()

    # ❌ BLOCK OTHER LANGUAGES FIRST
    if any(lang in q for lang in NON_PYTHON_KEYWORDS):
        return "❌ Only Python-related questions are allowed."

    # Greeting
    if is_greeting(query):
        return "W/Salam 😊 Ask Python-related question."

    # Code debugging
    if is_code(query):
        debug = debug_code(query)
        if debug:
            return debug

    # Error detection
    error = detect_error(query)
    if error:
        return error

    # ✅ NOW match from dataset
    answer = find_best_match(query)
    if answer:
        return answer

    # Intent detection fallback
    intent = detect_intent(query)
    if intent:
        return PYTHON_TOPICS[intent]["response"]

    return "⚠️ Please ask a Python-related question."

def find_best_match(user_query):
    questions = list(QA_DATA.keys())

    match = get_close_matches(user_query.lower(), questions, n=1, cutoff=0.6)

    if match:
        return QA_DATA[match[0]]

    return None