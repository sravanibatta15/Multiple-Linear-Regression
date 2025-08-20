# 📊 Multiple Linear Regression with Flask

This repository contains an **end-to-end implementation of Multiple Linear Regression (MLR)** using Python.  
The project demonstrates how to train an MLR model, save it using **pickle**, and deploy it with **Flask** so users can interact with it through a **web interface (HTML/CSS)**.  

---

## 🚀 What is Multiple Linear Regression (MLR)?
**Multiple Linear Regression (MLR)** is a supervised machine learning algorithm that predicts the value of a **dependent variable** based on two or more **independent variables**.  

📌 General Equation:  
\[
Y = β_0 + β_1X_1 + β_2X_2 + … + β_nX_n + ε
\]  

- **Y** → Dependent variable (e.g., Income)  
- **X1, X2, …, Xn** → Independent variables (e.g., Age, Experience)  
- **β** → Coefficients (impact of each variable)  
- **ε** → Error term  

Example: Predicting **Income** based on **Age** and **Experience**.  

---
- This project includes:
  - Training the model with sample data  
  - Saving the model using `pickle`  
  - Building a Flask app for deployment  
  - Creating a simple frontend with HTML/CSS  
  - Displaying predictions and dynamic graphs  

---
## 📂 Dataset Used

For this project, we use a **small custom dataset** containing employee records with the following columns:  

| Age | Experience (Years) | Income ($) |
|-----|---------------------|------------|
| 25  | 2                   | 25000      |
| 30  | 5                   | 40000      |
| 35  | 7                   | 50000      |
| 40  | 10                  | 65000      |
| 45  | 12                  | 70000      |
| 50  | 15                  | 85000      |

- **Age** → Employee’s age in years  
- **Experience** → Total work experience in years  
- **Income** → Annual income in USD  

This dataset is used to train the Multiple Linear Regression model, which then predicts income for unseen data points.  

---

## 🛠️ Libraries Used

### 1. **NumPy**
NumPy is the core numerical computing library in Python.  
It provides efficient array operations, mathematical functions, and linear algebra tools.  
Here, it is used to **reshape data arrays** and pass structured inputs to the regression model.  

### 2. **Pandas**
Pandas is a powerful library for data analysis and manipulation.  
It makes working with **tabular datasets** easy using DataFrames.  
In this project, Pandas is used to **prepare datasets, manage input data, and preprocess training data**.  

### 3. **Matplotlib**
Matplotlib is a visualization library for Python.  
It allows us to create static and dynamic plots for better understanding of data.  
Here, Matplotlib is used to **plot regression graphs and visualize predicted points** in the web app.  

### 4. **Pickle**
Pickle is a Python module for object serialization.  
It allows saving trained machine learning models as `.pkl` files and loading them later.  
In this project, Pickle is used to **save the trained MLR model** and **load it into the Flask app for predictions**.  

