
# Medical Disease Prediction using Machine Learning

## 📌 Project Overview
This project focuses on predicting the presence of a medical disease using supervised machine learning algorithms. Early disease prediction helps in preventive healthcare and decision support for doctors.

## 🧠 Type of Learning
Supervised Machine Learning

## 📊 Dataset
The dataset contains medical attributes such as age, glucose level, blood pressure, BMI, and other health-related features.  
Target variable indicates whether the patient has the disease (Yes / No).

## ⚙️ Algorithms Used
- Logistic Regression
- Decision Tree
- Random Forest
- K-Nearest Neighbors (KNN)
- Naïve Bayes

## 📈 Evaluation Metrics
- Confusion Matrix
- Precision
- Recall
- F1-Score

> Recall is given high importance as missing a diseased patient can be critical.

## 🛠️ Tools & Technologies
- Python
- NumPy
- Pandas
- Scikit-learn
- Matplotlib

## 🎯 Objective
To compare multiple classification algorithms and identify the best-performing model for medical disease prediction while addressing overfitting and bias-variance trade-off.

## Programming Language
- Python (implemented using Jupyter Notebook)

## 📌 What We Did in This Project

This project implements a complete **Machine Learning workflow** to predict the presence of a medical disease using patient health data.

The following steps were carried out:

### 1️⃣ Data Loading
- Loaded a real-world medical dataset (`diabetes.csv`) using Pandas.
- Displayed initial records to understand the structure of the data.

### 2️⃣ Data Understanding
- Used `data.info()` to check data types and missing values.
- Used `data.describe()` to analyze statistical properties such as mean, minimum, and maximum values.

### 3️⃣ Feature and Target Selection
- Separated the dataset into:
  - **Features (X):** Patient medical attributes such as glucose level, blood pressure, BMI, age, etc.
  - **Target (y):** Disease outcome (0 = No disease, 1 = Disease present).

### 4️⃣ Train–Test Split
- Split the dataset into training and testing sets.
- This ensures the model is evaluated on unseen data, simulating real-world usage.

### 5️⃣ Feature Scaling
- Applied **StandardScaler** to normalize feature values.
- This improves model performance, especially for Logistic Regression.

### 6️⃣ Model Training
The following supervised machine learning algorithms were implemented:
- **Logistic Regression** – used as the baseline classification model.
- **Random Forest Classifier** – used to improve performance and reduce overfitting.

### 7️⃣ Model Evaluation
- Evaluated models using:
  - Confusion Matrix
  - Precision
  - Recall
  - F1-Score
- Recall was given high importance since missing a diseased patient can be critical in medical applications.

### 8️⃣ Model Comparison
- Compared Logistic Regression and Random Forest using F1-score.
- Random Forest showed better performance due to ensemble learning and reduced variance.

### 9️⃣ Conclusion
- The project demonstrates how machine learning can assist in early medical disease prediction.
- Random Forest proved to be more reliable for this dataset compared to Logistic Regression.


## 🚀 Future Scope
- Use larger real-world medical datasets
- Deploy the model as a web application
- Add more advanced machine learning models

---

## 📂 Project Structure

