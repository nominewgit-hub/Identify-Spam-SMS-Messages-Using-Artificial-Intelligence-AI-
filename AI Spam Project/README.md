# 📩 Identify spam SMS messages using AI
Below is a free classifier to identify spam SMS messages. Just input your text, and our AI will predict if it's spam - in just seconds.

A **production‑ready Machine Learning project** that detects whether an SMS message is **Spam** or **Ham (Not Spam)**. This repository is designed to be **beginner‑friendly**, **academically sound**, and **industry‑oriented**, with a clear workflow from dataset loading to model training and deployment.

---

## 🚀 Project Overview

Spam messages waste time, cause fraud, and create security risks. This project applies **Natural Language Processing (NLP)** and **Machine Learning** techniques to automatically classify SMS messages.

✔ Clean & structured dataset handling
✔ Text preprocessing and feature extraction
✔ Model training and evaluation
✔ Notebook‑based experimentation
✔ Python application for prediction

This repository is suitable for:

* Data Science & AI students
* Mini / Final Year Projects
* Machine Learning practice
* GitHub portfolio showcase

---

## 🧠 Technologies Used

| Category      | Tools                             |
| ------------- | --------------------------------- |
| Programming   | Python 3.x                        |
| Data Handling | Pandas, NumPy                     |
| NLP           | NLTK / Scikit‑learn               |
| ML Models     | Naive Bayes / Logistic Regression |
| Visualization | Matplotlib, Seaborn               |
| Environment   | Jupyter Notebook                  |
| Deployment    | Python Script / App               |

---

## 📂 Project Structure

```bash
SMS-Spam-Detection/
│
├── dataset/
│   └── spam.csv                  # Raw SMS dataset
│
├── notebooks/
│   └── sms-spam-detection.ipynb   # EDA + Model Training
│
├── app.py                         # Prediction application
├── train_model.py                 # Model training script
├── requirements.txt               # Dependencies
├── README.md                      # Project documentation
└── model.pkl                      # Trained ML model
```

---

## 📊 Dataset Information

* **Source:** Public SMS Spam Dataset
* **Total Records:** ~5,500 SMS messages
* **Classes:**

  * `Ham` – Legitimate messages
  * `Spam` – Promotional / Fraud messages

### Sample Data

| Label | Message                                |
| ----- | -------------------------------------- |
| Ham   | Hey, are we meeting today?             |
| Spam  | Congratulations! You won a free prize! |

---

## 🔁 Machine Learning Workflow

1️⃣ Data Loading

2️⃣ Data Cleaning

3️⃣ Text Preprocessing

4️⃣ Feature Extraction (Bag of Words / TF‑IDF)

5️⃣ Model Training

6️⃣ Model Evaluation

7️⃣ Model Saving

8️⃣ Prediction on New Messages

---

## 🛠 Installation & Setup (For New Users)

Follow **each step carefully** after downloading the repository.

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/SMS-Spam-Detection.git
cd Identify spam SMS messages using AI
```

### Step 2: Create Virtual Environment (Recommended)

```bash
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate # Linux/Mac
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 📘 Running the Project

### 🔹 Option 1: Run Jupyter Notebook (Learning Mode)

```bash
jupyter notebook
```

Open:

```
notebooks/sms-spam-detection.ipynb
```

✔ Understand dataset
✔ Explore visualizations
✔ Train and test models

---

### 🔹 Option 2: Train Model via Script

```bash
python train_model.py
```

This will:

* Preprocess the data
* Train the ML model
* Save the trained model (`model.pkl`)

---

### 🔹 Option 3: Run Prediction App

```bash
python app.py
```

Enter an SMS message and get prediction:


```text
Input: "You have won a free lottery"
Output: Spam ❌
```

---

## 📈 Model Performance

| Metric    | Score |
| --------- | ----- |
| Accuracy  | ~97%  |
| Precision | High  |
| Recall    | High  |

> Exact scores may vary depending on preprocessing and model selection.

---

## 🔐 Key Features

✔ High accuracy spam detection

✔ Clean & modular code

✔ Beginner‑friendly documentation

✔ Ready for extension (Web / API / Mobile)


---

## 🧩 Future Improvements

* Deploy using Flask / FastAPI
* Add deep learning (LSTM / BERT)
* Web‑based UI
* Multi‑language spam detection

---

## 👨‍💻 Author

**Muhamamd Noman**

AI & Machine learning Project

📌 GitHub: * https://github.com/nominewgit-hub *

---

## 📜 License


Feel free to use, modify, and share for educational purposes.

---

## ⭐ Support

If you find this project useful:

* ⭐ Star the repository
* 🧠 Learn & build more ML projects

---

> "Learning Machine Learning is not about models — it’s about **process, practice, and patience**." 
