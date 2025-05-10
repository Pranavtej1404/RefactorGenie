


# 🧠 RefactorGenie – Python Code Refactoring Suggestion Tool

RefactorGenie is a lightweight, web-based Python code analysis tool that detects common code smells and suggests refactoring opportunities. It uses Python's `ast` module to parse source code and identify issues that affect code readability, maintainability, and design quality.

---

## 🔍 Features

- **Static Code Analysis** using AST
- Detects:
  - 🟡 Unused Variables
  - 🟠 Long Methods/Functions
  - 🔴 Long Conditional Chains (if-elif ladders or nested ifs)
  - 🟣 Redundant/Repetitive Code Blocks
- **Dual Input Support**:
  - File Upload (`.py`)
  - Direct Paste Input
- **Web Interface** built with Flask + HTML/CSS/JS
- Dynamic result display using Fetch API

---


### 🌐 Live Demo

You can try out RefactorGenie right now:

👉 **[https://refactorgenie.onrender.com](https://refactorgenie.onrender.com)**

No installation needed — just upload or paste your Python code to receive instant refactoring suggestions.

---




## 📁 Project Structure

```

RefactorGenie/
│
├── app/
│   ├── app.py                  # Flask routes and server setup
│   ├── main.py                 # Controller for code analysis
│   ├── analyzer/
│   │   ├── parser.py           # AST parsing logic
│   │   └── rules/
│   │       ├── unused\_vars.py
│   │       ├── longMethod.py
│   │       ├── longCondition.py
│   │       └── redundant\_code.py
│   ├── templates/
│   │   └── index.html          # Frontend HTML layout
│   └── static/
│       ├── styles.css          # Styling
│       └── script.js           # JS logic (drag-drop, paste, fetch)
│
└── test_samples/
      └── sample1.py            # Sample input for testing

````

---

## 🚀 How It Works

1. User uploads or pastes Python code.
2. The code is sent to the `/analyze` or `/analyze_paste` endpoint.
3. Code is parsed into an Abstract Syntax Tree (AST).
4. Rule modules evaluate the AST for code smells.
5. Suggestions are sent back and rendered dynamically on the frontend.

---

## 🔧 Installation & Usage

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/RefactorGenie.git
   cd RefactorGenie
````

2. **Create a virtual environment (optional but recommended)**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install flask
   ```

4. **Run the app**

   ```bash
   python app/app.py
   ```

5. **Open in browser**

   ```
   http://localhost:5000
   ```

---

## ✅ Test Cases

* Functional tests for detecting unused variables, long methods, long conditionals, and redundant logic.
* Test script available: `test_analyzer.py`

---

## 🌟 Future Enhancements

* Auto-refactoring for certain code smells
* Cyclomatic complexity analysis
* VS Code Extension integration
* Inline suggestions view with syntax highlighting

---



## 👨‍💻 Author

Made with  by N.Pranav Tej


