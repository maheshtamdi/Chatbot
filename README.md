
# 🤖 Chatbot Project – NLP | API Integration | Data Science

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-orange)
![pandas](https://img.shields.io/badge/pandas-Data%20Analysis-green)
![Contributions](https://img.shields.io/badge/Contributions-Welcome-brightgreen.svg)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

A **modular Python-based chatbot** that leverages **Natural Language Processing (NLP)**, **API integrations**, and **data analysis utilities**.  
It understands user intents, fetches real-time data (weather & jokes), and provides tools for analyzing chat history.  

---

## 📑 Table of Contents
- [✨ Features](#-features)
- [📂 Project Structure](#-project-structure)
- [⚙️ Requirements](#️-requirements)
- [📥 Installation](#-installation)
- [🔧 Configuration](#-configuration)
- [🚀 Usage](#-usage)
- [💻 Example Interaction](#-example-interaction)
- [📊 Data Analysis](#-data-analysis)
- [🤝 Contributing](#-contributing)
- [📜 License](#-license)
- [🙏 Acknowledgments](#-acknowledgments)

---

## ✨ Features
- 🧠 **NLP Model** – Train and predict user intents using `scikit-learn`.  
- 🌤️ **API Integration** – Fetch real-time **weather data** and **random jokes**.  
- 📊 **Data Analysis** – Use `pandas` to analyze and summarize chat logs.  
- ⚡ **Modular Design** – Clean separation of NLP, API, data utilities, and main logic.  
- 💡 **Extensible** – Easy to add new intents, APIs, or ML models.  

---

## 📂 Project Structure
```

chatbot\_project/
│── main.py              # Entry point for chatbot
│── nlp\_model.py         # NLP model (training + prediction)
│── api\_integration.py   # External API calls (weather, jokes, etc.)
│── data\_utils.py        # Data utilities (analysis with pandas)
│── requirements.txt     # Dependencies

````

---

## ⚙️ Requirements
- Python **3.8+**
- Install dependencies:
  ```bash
  pip install -r requirements.txt


---

## 📥 Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/maheshtamdi/chatbot_project.git
   cd chatbot_project
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

---

## 🔧 Configuration

* For weather API, update `api_integration.py` with your [OpenWeatherMap API Key](https://openweathermap.org/api):

  ```python
  api_key = "your_api_key_here"
  ```

---

## 🚀 Usage

Run the chatbot:

```bash
python main.py
```

Type your queries and interact with the bot.
Exit anytime with:

```bash
quit
exit
```

---

## 💻 Example Interaction

```
You: hello
Bot: Hello! How can I help you today?

You: tell me a joke
Bot: 😂 Why don't scientists trust atoms? Because they make up everything!

You: weather in London
Bot: 🌤️ The weather in London is clear sky.
```

---

## 📊 Data Analysis

You can analyze saved chat history using `data_utils.py`:

```python
from data_utils import analyze_chat_data
analyze_chat_data("chat_data.csv")
```

This provides insights like most common user messages, frequency of intents, etc.

---

## 🤝 Contributing

Contributions are welcome!

1. Fork this repository
2. Create your feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -m 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Open a Pull Request 🚀

---

## 📜 License

This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

* [scikit-learn](https://scikit-learn.org/) – for NLP model training
* [pandas](https://pandas.pydata.org/) – for data analysis
* [OpenWeatherMap API](https://openweathermap.org/api) – for weather data
* [JokeAPI](https://jokeapi.dev/) – for random jokes

---


