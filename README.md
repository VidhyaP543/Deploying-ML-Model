# Deploying-ML-Model
# Deploying a Machine Learning Model

## Iris Flower Classification API

##  Project Overview

This project demonstrates the deployment of a machine learning model using a Flask web application. A Random Forest classifier is trained on the Iris dataset to classify Iris flowers into three species: Setosa, Versicolor, and Virginica. The trained model is saved as a serialized file (`model.pkl`) and loaded into a Flask API, allowing users to send flower measurements and receive predictions through HTTP requests.

---

##  Problem Statement

Develop and deploy a machine learning model that predicts the species of an Iris flower based on its sepal and petal measurements.

---

##  Objectives

* Train a machine learning classification model.
* Save the trained model for future use.
* Build a Flask API to serve predictions.
* Test the prediction endpoint using sample input.
* Demonstrate a simple machine learning deployment workflow.

---

##  Dataset

**Dataset Name:** Iris Dataset

**Number of Samples:** 150

**Number of Features:** 4

### Features

* Sepal Length
* Sepal Width
* Petal Length
* Petal Width

### Target Classes

* Setosa
* Versicolor
* Virginica

---

## 🛠 Technologies Used

* Python
* Jupyter Notebook
* Flask
* Scikit-learn
* NumPy
* Pickle

---

##  Project Workflow

1. Load the Iris dataset.
2. Train a Random Forest classifier.
3. Evaluate the model performance.
4. Save the trained model as `model.pkl`.
5. Develop a Flask API (`app.py`).
6. Load the trained model into the API.
7. Accept user input and return predictions.

---

##  Machine Learning Model

**Algorithm Used:** Random Forest Classifier

The model is trained using the Iris dataset and serialized using Python's Pickle library for deployment.

---

## 📁 Repository Structure

```text
Deploying-ML-Model/
│
├── model/
│   └── model.pkl
│
├── app.py
│
├── report/
│   └── Deploying_ML_Model_Project_Report.pdf
│
└── README.md
```

---

## ▶️ How to Run the Project

1. Install the required Python libraries.
2. Run the Jupyter Notebook to train the model and generate `model.pkl`.
3. Place `model.pkl` in the `model` folder.
4. Run the Flask application:

```bash
python app.py
```

5. Open your browser or API testing tool and access the application.

---

##  Expected Output

The API accepts flower measurements and returns the predicted Iris species in JSON format.

---

##  Future Enhancements

* Containerize the application using Docker.
* Deploy the API to AWS, Google Cloud, or Azure.
* Add a web-based user interface.
* Improve the model using hyperparameter tuning.
* Implement authentication and monitoring.

---

##  Conclusion

This project demonstrates the complete workflow of deploying a machine learning model as a web API. It shows how a trained model can be integrated into an application to provide real-time predictions and forms a strong foundation for deploying larger machine learning solutions.
