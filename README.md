# 🎥 UTube Video Analysis Agent

A powerful Streamlit-based application that leverages AI to provide in-depth analysis of YouTube videos, perfect for researchers, content creators, and educators.

## ✨ Key Features

- **Smart Content Analysis**: Automatically identifies video type, structure, and key moments
- **Intelligent Timestamping**: Creates precise, meaningful timestamps for easy navigation
- **Multiple Analysis Templates**: Specialized analysis modes for tutorials, educational content, reviews, and creative content
- **Customizable Analysis**: Flexibility to tailor analysis prompts to specific needs
- **User-Friendly Interface**: Clean, intuitive design with collapsible sections and clear prompts

---

## 🚀 Quick Start

### Prerequisites

```bash
python >= 3.7
streamlit
agno
python-dotenv
```

### Installation

#### 1. Clone the repository:
```bash
git clone https://github.com/deepakmalikk/UTube_Agent.git
cd UTube_Agent
```

#### 2. Install dependencies:
```bash
pip install -r requirements.txt
```

#### 3. Set up environment variables:
```bash
# Create .env file and add your OpenAI API key
echo "OPENAI_API_KEY=your_api_key_here" > .env
```

#### 4. Run the application:
```bash
streamlit run app.py
```
