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

## 🎯 Use Cases

- **Educators:** Create detailed lesson summaries and study guides  
- **Content Creators:** Analyze competitor videos and industry trends  
- **Researchers:** Extract key information and timestamps from lectures  
- **Students:** Generate comprehensive notes from educational content  
- **Product Reviewers:** Break down review videos into feature comparisons  

## 🛠️ Technical Architecture

### Core Components

- **Agent System:** Utilizes the agno framework for intelligent content analysis  
- **YouTube Tools:** Integrated YouTube API tools for video metadata extraction  
- **Streamlit UI:** Responsive and interactive user interface  
- **Template Engine:** Customizable analysis templates for different content types  

### Analysis Pipeline

#### Video Processing
- Metadata extraction  
- Content type identification  
- Structure analysis  

#### Content Analysis
- Automated timestamping  
- Topic segmentation  
- Key point extraction  

#### Output Generation
- Structured markdown output  
- Interactive expandable sections  
- Error handling and validation  

## 🎨 Analysis Templates

| Type          | Focus Use Case                         | Example                                      |
|---------------|----------------------------------------|----------------------------------------------|
| 💻 Tutorial   | Code examples & implementation steps   | Programming tutorials, how-to guides         |
| 📚 Educational| Learning material & key concepts        | Lectures, educational videos                 |
| 📱 Review     | Product features & comparisons          | Tech reviews, product demonstrations         |
| 🎨 Creative   | Techniques & methods                    | Art tutorials, design workflows              |

## 🔒 Security

- Secure API key handling through environment variables  
- Input validation and sanitization  
- Error handling and graceful failure modes

## 🚀 Deployment

🔗 Live Demo: [https://utubeagent.streamlit.app/]

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Built with Streamlit  
- Powered by Agno Framework  
- YouTube data analysis tools  

## 📧 Contact

For support or inquiries, please open an issue or contact [deepak164malik@gmail.com]



