# Healthcare Assistant Chatbot

This is a **Streamlit-based AI chatbot** that provides **healthcare assistance** using **Google Gemini AI** for natural language processing.

## 🚀 Features
- **AI-Powered Responses**: Uses Gemini AI for intelligent healthcare-related answers.
- **User-Friendly UI**: Built with **Streamlit** for easy interaction.
- **Real-Time Query Processing**: Instant responses with a simple text input.

## 🛠️ Setup & Installation

### **1. Prerequisites**
Ensure you have the following installed:
- **Python 3.10+**
- **pip** (Python package manager)
- A **Google Gemini API Key** ([Get it here](https://ai.google.dev/))

### **2. Clone the Repository**
```sh
 git clone https://github.com/yourusername/healthcare-chatbot.git
 cd healthcare-chatbot
```

### **3. Install Dependencies**
Run the following command to install required Python packages:
```sh
pip install streamlit google-generativeai nltk
```

### **4. Set Up Google Gemini API Key**
Edit the `chatbothealth.py` file and replace `your_api_key_here` with your actual API key:
```python
import google.generativeai as genai

genai.configure(api_key="your_api_key_here")
```

Or, set it as an **environment variable**:
```sh
set GOOGLE_API_KEY=your_api_key_here  # Windows
export GOOGLE_API_KEY=your_api_key_here  # Mac/Linux
```

### **5. Run the Chatbot**
Start the chatbot with:
```sh
streamlit run chatbothealth.py
```

## 🏥 Usage
1. Open the Streamlit app in your browser.
2. Enter a healthcare-related question in the text box.
3. Click **Submit** and get an AI-generated response.

## 📝 File Structure
```
📂 healthcare-chatbot
 ├── chatbothealth.py  # Main Python script
 ├── requirements.txt  # Dependency list
 ├── README.md         # Documentation
```

## 🤝 Contributing
Feel free to fork this project and submit pull requests. If you have suggestions, open an issue.

## 📜 License
This project is licensed under the **MIT License**.

## 📧 Contact
For any queries, contact **your.email@example.com**.

