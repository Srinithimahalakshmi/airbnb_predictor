from flask import Flask, render_template, request
import pandas as pd
import joblib

app = Flask(__name__)
model = joblib.load("model/lasso_model.pkl")  # Make sure the path is correct

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def predict():
    try:
        input_data = {
            'property_type': [request.form['property_type']],
            'cleaning_fee': [float(request.form['cleaning_fee'])],
            'review_scores_rating': [float(request.form['review_scores_rating'])],
            'accommodates': [int(request.form['accommodates'])],
            'beds': [int(request.form['beds'])],
            'number_of_reviews': [int(request.form['number_of_reviews'])],
            'room_type': [request.form['room_type']],
            'neighbourhood': [request.form['neighbourhood']],
            'bedrooms': [int(request.form['bedrooms'])],
            'bathrooms': [float(request.form['bathrooms'])]
        }

        input_df = pd.DataFrame(input_data)

        # Optional: check for missing columns
        missing_cols = set(model.feature_names_in_) - set(input_df.columns)
        if missing_cols:
            return f"Error: Missing columns in input: {missing_cols}"

        # Predict
        prediction = model.predict(input_df)[0]
        return render_template('index.html', prediction_text=f"Predicted Log Price: {round(prediction, 2)}")

    except Exception as e:
        return render_template('index.html', prediction_text=f"Error: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)
