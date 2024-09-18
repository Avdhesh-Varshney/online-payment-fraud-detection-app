# <font color="gold">Online Payments Fraud Detection ML Model</font>

![Fraud Detection](https://img.shields.io/badge/Fraud-Detection-brightgreen?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.8+-blue.svg?style=for-the-badge)
![XGBoost](https://img.shields.io/badge/-XGBoost-important?style=for-the-badge)
![AUC ROC](https://img.shields.io/badge/AUC--ROC-0.9556-blue?style=for-the-badge)
![License](https://img.shields.io/github/license/Avdhesh-Varshney/online-payment-fraud-detection-app?style=for-the-badge)

---

## <font color="lavendar">Project Overview</font>

The **Online Payments Fraud Detection** application is designed to predict fraudulent transactions in online payment systems using advanced machine learning techniques. With the growing risk of online payment fraud, this model helps financial institutions and e-commerce platforms identify suspicious transactions in real-time.

Our solution leverages machine learning models, such as **XGBoost**, to detect fraudulent transactions based on a set of features that describe the transaction details. This project focuses on:
- **Real-time fraud detection** by integrating machine learning models into the payment processing system.
- **Interactive interface** for users to input transaction details and receive immediate feedback on transaction validity.
- **Comprehensive feature engineering** and data reduction techniques to optimize model performance.

---

## <font color="lavendar">Features</font>

- **Fraud Detection Model**: Built with XGBoost and tuned using hyperparameter optimization to achieve an <font color="khaki">AUC ROC score of 0.9556</font>.
- **Feature Reduction**: <font color="khaki">Dimensionality reduction from 394 to 53 features</font> for optimized performance.
- **Interactive Web Application**: A user-friendly interface built with <font color="lightgreen">Streamlit</font> for real-time fraud prediction.
- **Scalable**: Suitable for integration into <font color="plum">large-scale</font> online payment platforms.
- **Visualization Tools**: Displays transaction analysis and prediction results in an intuitive format.
- **Comprehensive Documentation**: Access detailed documentation about <font color="khaki">what has been done</font> through the links provided below.

---

## <font color="lavendar">Usage</font>

1. Open the web app by running the command below.
   > <font color="red">https://online-payment-fraud-detector.streamlit.app/</font>

2. Enter transaction details like:
   - Transaction amount
   - Transaction ID
   - Device Type
   - Card Type (Visa/ discover/ american express/ mastercard)
   - Transaction type (debit/credit)
3. Click the **Predict** button to determine if the transaction is fraudulent.
4. View the prediction result (fraudulent or genuine).

---

## <font color="lavendar">Model Pipeline</font>

The machine learning pipeline for this project consists of the following steps:

1. **Data Preprocessing**: Handling missing values, scaling, and encoding categorical features.
2. **Feature Engineering**: Reducing the dataset from 394 features to 53 using techniques like PCA and feature importance.
3. **Model Training**: Using **XGBoost** with hyperparameter tuning for optimal performance.
4. **Model Evaluation**: Evaluating the model based on metrics such as AUC ROC and accuracy.
5. **Prediction**: Real-time predictions using the trained model.

> <font color="purple">**NOTE:**</font> To dive deeper into the technical details, model architecture, or other functionalities, visit the following sections:
> > <font color="seagreen">**NOTEBOOK LINK:**</font> https://www.kaggle.com/code/avdhesh15/fraud-detection-model <br />
> > <font color="seagreen">**WEBSITE LINK:**</font> https://avdhesh-varshney.github.io/online-payment-fraud-detection-app/

---

## <font color="lavendar">Evaluation Metrics</font>

The model was evaluated on the **IEEE-CIS Fraud Detection Dataset** using the following metrics:
- <font color="plum">**1 CV Score**</font>: 0.9562
- <font color="plum">**2 CV Score**</font>: 0.952
- <font color="plum">**3 CV Score**</font>: 0.9586
- <font color="lavendar">**Mean AUC ROC**</font>: 0.9556

These metrics ensure a reliable detection of fraudulent transactions, minimizing both false positives and false negatives.

---

## <font color="lavendar">Dataset</font>

This project uses the <font color="gold">**IEEE-CIS Fraud Detection Dataset**</font>, which contains anonymized transaction data. The dataset includes a wide range of features that describe each transaction, such as transaction amount, device information, and transaction type.

- **Training Data**: Used for model training and validation.
- **Testing Data**: Used to evaluate the final model.

---

## <font color="lavendar">Technologies Used</font>

- <font color="yellow">**Python 3.8+**</font>
- <font color="skyblue">**XGBoost**</font>: The primary machine learning model used for prediction.
- <font color="lightgreen">**Streamlit**</font>: For building the web interface and API.
- <font color="coral">**Pandas, NumPy**</font>: For data manipulation and preprocessing.
- <font color="salmon">**Scikit-learn**</font>: For preprocessing and model evaluation.
- <font color="violet">**Matplotlib, Seaborn**</font>: For visualizations and feature analysis.

<div align="center">
  <h3>Show some &nbsp;❤️&nbsp; by &nbsp;🌟&nbsp; this repository!</h3>
</div>

<a href="#top"><img src="https://img.shields.io/badge/-Back%20to%20Top-red?style=for-the-badge" align="right"/></a>
