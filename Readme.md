# Influenza Outbreak Event Prediction via Twitter

## 👨‍💻 Team Members
- Raunit Arya (2401560078)
- Sahil  (2401560079)
- Rahul Sharma  (2401560062)

## 📄 Project Description
This project aims to forecast influenza outbreaks by combining CDC-reported flu activity data with sentiment signals extracted from Twitter. Using Natural Language Processing (NLP) and machine learning/deep learning models, we analyze tweets containing flu-related keywords and predict outbreak trends. The project demonstrates the feasibility of using real-time social media data for public health surveillance and early outbreak warnings.

## 🎥 Video Presentation

[Click here to watch the project presentation](https://github.com/RaunitArya/Inlfuenza-Outbreak-Prediction-via-Twitter/raw/main/Y1-2024-25-G299.mp4)


## 🛠️ Technologies Used
- Python  
- Tweepy (Twitter API)  
- Pandas, NumPy  
- NLTK, VADER Sentiment Analysis  
- Scikit-learn (Logistic Regression, Random Forest)  
- TensorFlow/Keras (RNN, LSTM)  
- Matplotlib, Seaborn  
- Jupyter Notebook

## 🌐 **Steps to Access the Twitter API**

### ✅ **1. Create a Twitter Developer Account**

- Go to the [Twitter Developer Portal](https://developer.twitter.com/en).
- Log in using your Twitter credentials.
- Click on **“Developer Portal”** or “Apply” under “Get started”.
- Choose the appropriate use case (e.g., **Student/Academic** or **Hobbyist**).
- Fill in your application form honestly and explain your project.

> 
> Example: *“I am building a machine learning model to analyze tweets and predict influenza outbreaks using NLP and sentiment analysis techniques for academic purposes.”*
- Agree to the Developer Agreement and submit.

* * *

### ✅ **2. Create a Project and App**

- Once approved, go to the [Developer Dashboard](https://developer.twitter.com/en/portal/dashboard).
- Click **“+ Create Project”**.
- Name the project (e.g., “Flu Outbreak Prediction”).
- Describe what your project will do (same as above).
- After creating the project, you’ll be prompted to create an **App**.

* * *

### ✅ **3. Generate Your API Keys and Tokens**

After the app is created:

- Go to the “Keys and Tokens” tab.
- You will find:

    - **API Key and Secret**
    - **Bearer Token**
- Generate:

     **Bearer Token**
   

## 🚀 How to Run the Project

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/influenza-prediction-twitter.git
cd influenza-prediction-twitter
```

### 2. Install Required Libraries
```bash
pip install -r requirements.txt
```

### 3. Set Up Twitter API Keys
- Create a `.env` file or directly insert your API keys in the script.
- Required keys: `API_KEY`, `API_SECRET`, `ACCESS_TOKEN`, `ACCESS_SECRET`

### 4. Run the Notebooks
- `main.ipynb` – Contains CDC data processing and model training  
- `TweetsCleaning.ipynb` – Preprocessing, sentiment analysis, and integration of Twitter data  

### 5. Watch the Output
- Outputs include graphs showing flu sentiment trends, model performance, and prediction accuracy.

