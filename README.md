# AI Blog Content Generator

An AI-powered modular Python application that generates complete blog content based on a user-provided topic. The system uses separate modules for intent detection, title generation, content generation, summary creation, SEO keyword extraction, and meta description generation.

## 🚀 Features

* User-friendly topic input
* Intent detection
* AI-generated blog title
* AI-generated blog content
* Automatic summary generation
* SEO keyword generation
* Meta description generation
* Saves generated blog content
* Modular Python architecture
* Demo execution support
* Screenshot-based demonstration

## 🛠️ Technologies Used

* Python
* Natural Language Processing (NLP)
* Artificial Intelligence
* Generative AI
* Modular Python Programming

## 📁 Project Structure

```text
Blog-Content-Generator/
│
├── screenshots/
│   ├── HomeScreen.png
│   ├── Userinput_Intent_Detection.png
│   ├── blog_title.png
│   ├── BlogGeneration.png
│   ├── BlogGenerationpartII.png
│   ├── Summary_Generation .png
│   ├── SEO_Keywords.png
│   ├── Meta_Description .png
│   └── Blog Saved_Successfully.png
│
├── blog_module.py
├── demo_run.py
├── input_module.py
├── intent_module.py
├── keyword_module.py
├── main.py
├── meta_module.py
├── summary_module.py
├── title_module.py
├── utils.py
├── requirements.txt
├── .gitignore
└── README.md
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/Devanandasunil/Blog-Content-Generator.git
```

### 2. Navigate to the project folder

```bash
cd Blog-Content-Generator
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

**Windows:**

```bash
venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

## ▶️ Running the Application

Run the main application using:

```bash
python main.py
```

Enter a blog topic when prompted:

```text
=== AI Blog Generator ===
Enter the blog topic:
```

For example:

```text
The Future of Artificial Intelligence in Education
```

The application then processes the topic and generates the required blog content.

## 🧩 Modules

| Module              | Purpose                        |
| ------------------- | ------------------------------ |
| `main.py`           | Main application workflow      |
| `input_module.py`   | Handles user input             |
| `intent_module.py`  | Detects the user's intent      |
| `title_module.py`   | Generates the blog title       |
| `blog_module.py`    | Generates blog content         |
| `summary_module.py` | Generates the blog summary     |
| `keyword_module.py` | Generates SEO keywords         |
| `meta_module.py`    | Generates the meta description |
| `utils.py`          | Utility functions              |
| `demo_run.py`       | Demonstration/testing script   |

## 🔄 Workflow

```text
User Topic
    ↓
Input Processing
    ↓
Intent Detection
    ↓
Title Generation
    ↓
Blog Content Generation
    ↓
Summary Generation
    ↓
SEO Keyword Generation
    ↓
Meta Description Generation
    ↓
Blog Output
```

## 📸 Screenshots

### Home Screen

![Home Screen](screenshots/HomeScreen.png)

### User Input & Intent Detection

![Intent Detection](screenshots/Userinput_Intent_Detection.png)

### Blog Title Generation

![Blog Title](screenshots/blog_title.png)

### Blog Generation

![Blog Generation](screenshots/BlogGeneration.png)

### Summary Generation

![Summary](screenshots/Summary_Generation%20.png)

### SEO Keywords

![SEO Keywords](screenshots/SEO_Keywords.png)

### Meta Description

![Meta Description](screenshots/Meta_Description%20.png)

### Blog Saved Successfully

![Blog Saved](screenshots/Blog%20Saved_Successfully.png)

## 🎯 Purpose

This project demonstrates how AI and NLP techniques can be combined with a modular Python architecture to automate the process of creating structured and SEO-friendly blog content.

## 🔮 Future Enhancements

* Web-based user interface
* Multiple language support
* Advanced SEO optimization
* Blog tone and style selection
* Word-count customization
* Cloud deployment
* Database integration
* Automated publishing to blogging platforms

## 👩‍💻 Author

**Devananda Sunil**

---

