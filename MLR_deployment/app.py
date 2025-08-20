from flask import Flask, render_template, request
import numpy as np
import pickle
import matplotlib
matplotlib.use('Agg')  # For rendering without GUI
import matplotlib.pyplot as plt
import os

app = Flask(__name__)

# Load your trained model (make sure model.pkl is in the same folder)
model = pickle.load(open("MLR_Model.pkl", "rb"))

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    graph_url = None

    if request.method == "POST":
        try:
            age = float(request.form["age"])
            exp = float(request.form["experience"])

            # Reshape input for prediction
            input_data = np.array([[age, exp]])
            prediction = model.predict(input_data)[0]

            # Create a graph (Age vs Income with prediction point)
            ages = np.linspace(20, 60, 50)
            exps = np.linspace(1, 30, 50)
            # Just plotting w.r.t Age for visualization
            incomes = [model.predict([[a, exp]])[0] for a in ages]

            plt.figure(figsize=(6,4))
            plt.plot(ages, incomes, label=f"Prediction curve (exp={exp})")
            plt.scatter(age, prediction, color="red", s=80, label="Your Prediction")
            plt.xlabel("Age")
            plt.ylabel("Income")
            plt.title("Multiple Linear Regression Prediction")
            plt.legend()
            plt.grid(True)

            # Save the graph
            graph_path = "static/graph.png"
            if not os.path.exists("static"):
                os.makedirs("static")
            plt.savefig(graph_path)
            plt.close()

            graph_url = graph_path

        except Exception as e:
            prediction = f"Error: {str(e)}"

    return render_template("index.html", prediction=prediction, graph_url=graph_url)

if __name__ == "__main__":
    app.run(debug=True)
