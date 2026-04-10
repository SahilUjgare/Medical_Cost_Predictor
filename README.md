# Medical_Cost_Predictor :

```markdown

This is a simple **Streamlit web application** that predicts medical insurance charges based on user inputs such as age, gender, BMI, smoking habits, and region.  
The prediction is powered by a pre-trained machine learning model.

---

## 📁 Project Structure

```

├── app.py                 # Streamlit application file
├── best_model (1).pkl     # Trained ML model
├── insurance.csv          # Dataset used for training/testing
├── requirements.txt       # Dependencies for the app
└── README.md              # Project documentation

````

---

## 🚀 How to Run the App

1. **Clone this repository** or download the project folder.

2. **Install the dependencies**:
   ```bash
   pip install -r requirements.txt
````

3. **Run the Streamlit app**:

   ```bash
   streamlit run app.py
   ```

4. **Enter the input details** in the sidebar and click **Predict Charges**.

---

## ⚙️ Features

* Interactive UI built with Streamlit
* Accepts user input for:

  * Age
  * Sex
  * BMI
  * Number of children
  * Smoking status
  * Region
* Displays predicted insurance charge instantly

---

## 📦 Requirements

* Python 3.8+
* Streamlit
* Pandas
* Scikit-learn

---

## ❤️ Acknowledgements

* Dataset: `insurance.csv`
* Built with [Streamlit](https://streamlit.io/)
* Model trained using Scikit-learn

---

**Author:** *Sahil Ujgare*
**Made with ❤️ using Python and Streamlit*

```
