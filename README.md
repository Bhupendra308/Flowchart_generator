# 🚀 Flowchart Generator

## 📌 Overview

The **Flowchart Generator** is a prototype web-based tool that allows users to generate flowcharts by simply entering a **single-line text prompt**. It uses **Flask (Python) for the backend** and **ChatGPT API from RapidAPI** to process user input and create flowcharts.

## ✨ Features

- 📝 **Enter a simple text prompt** (e.g., *"Flowchart for drone building"*)
- 🖥️ **Flask backend** processes the request
- 🌍 **ChatGPT API** generates the flowchart structure
- 📌 **Displays the flowchart on the web page**

## 🛠️ Installation

### Prerequisites:

- Python 3.x
- Flask
- API key from **RapidAPI** (Sign up at [RapidAPI](https://rapidapi.com))

### Steps:

1. Clone this repository:
   ```sh
   git clone https://github.com/your-username/flowchart-generator.git
   ```
2. Navigate to the project folder:
   ```sh
   cd flowchart-generator
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Set up API key:
   ```sh
   export RAPIDAPI_KEY="your_api_key_here"
   ```
5. Run the application:
   ```sh
   python app.py
   ```
6. Open the browser and visit:
   ```
   http://127.0.0.1:5000/
   ```

## 🚀 Usage

1. Enter a **single-line description** of what you need, such as:
   ```
   Flowchart for drone building
   ```
2. The Flask backend sends the input to **ChatGPT API (via RapidAPI)**.
3. The API returns a structured **flowchart format**.
4. The generated **flowchart is displayed** on the web interface.

## 📌 Example Input

```
Flowchart for building a car
```
## 📌 Example Output

![127 0 0 1_5000_](https://github.com/user-attachments/assets/1960776b-f551-4555-b062-7e77501905d1)


## 🛠️ Tech Stack

- **Backend:** Python, Flask
- **Frontend:** HTML, CSS
- **API:** ChatGPT via RapidAPI

---
