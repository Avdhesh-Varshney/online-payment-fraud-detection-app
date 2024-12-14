# About the Application 

The **Online Payments Fraud Detection** application predicts fraudulent transactions in online payment systems using advanced machine learning techniques. With the growing risk of online payment fraud, this model helps financial institutions and e-commerce platforms identify suspicious transactions in real-time.  

---

## Features  

1. **Real-Time Fraud Detection**  
   - Detects fraud during transaction processing by analyzing transaction features like amount, origin, and time.  
   - Provides immediate feedback to help prevent fraudulent activities.  

2. **Interactive Interface**  
   - Powered by **Streamlit**, users can easily input transaction details to get predictions.  
   - Designed for accessibility and user-friendliness, ensuring a seamless experience.  

3. **Comprehensive Feature Engineering**  
   - Implements advanced preprocessing steps to clean and optimize transaction data.  
   - Uses dimensionality reduction techniques like **Principal Component Analysis (PCA)** to improve model performance.  

---

## How It Works  

The application leverages the **XGBoost** machine learning model to detect fraudulent transactions based on transaction attributes. Here’s how it operates:  

- **Data Preprocessing**: Transaction data undergoes cleaning and feature scaling to ensure consistency.  
- **Feature Selection**: PCA reduces input dimensions, retaining only the most critical features.  
- **Prediction**: The trained **XGBoost** model evaluates transaction details to classify them as genuine or fraudulent.  

This approach ensures accurate predictions while maintaining computational efficiency.  

---

## Key Highlights  

- **Machine Learning Backbone**: Powered by **XGBoost**, renowned for its accuracy and efficiency in handling imbalanced datasets.  
- **AUC-ROC Performance**: Achieves a score of **0.9556**, demonstrating its reliability in fraud detection.  
- **Seamless Integration**: Can be embedded into existing payment systems for real-time fraud analysis.  
