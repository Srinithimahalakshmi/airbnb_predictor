
#  Airbnb Price & Demand Prediction System

##  Overview
A machine learning system designed to recommend optimal Airbnb listing prices and predict booking demand using **Lasso Regression**. The project includes data preprocessing, feature selection, model training, evaluation, plus market and seasonal analysis to deliver pricing insights and demand forecasts.

---

##  Table of Contents
- [⚙️ Installation](#-installation)  
- [🚀 Usage](#-usage)  
- [📁 Project Structure](#-project-structure)  
- [📊 Results](#-results)  
- [🤝 Contributing](#-contributing)  
- [📬 Contact](#-contact)  

---

##  Installation
```bash
git clone https://github.com/Srinithimahalakshmi/airbnb_predictor.git
cd airbnb_predictor

python3 -m venv venv
source venv/bin/activate             # Windows: venv\Scripts\activate
pip install -r requirements.txt

# (Optional) Add Google Maps API key
echo "GOOGLE_MAPS_API_KEY=your_key_here" > .env
````

---

## Usage

1. **Preprocess & Filter Data**

   ```bash
   python src/data_preprocessing.py --city "YourCity"
   ```

2. **Train Price Model**

   ```bash
   python src/models/train_price_model.py --data data/processed/yourcity_listings.csv --model models/price_predictor.pkl
   ```

3. **Predict Price in Code**

   ```python
   from src.predict import AirbnbPricePredictor

   predictor = AirbnbPricePredictor('models/price_predictor.pkl')
   listing_data = {
       'neighborhood': 'Downtown',
       'room_type': 'Entire home/apt',
       'accommodates': 2,
       'bedrooms': 1,
       'bathrooms': 1,
       'amenities': ['wifi', 'heating'],
       'review_scores_rating': 4.5
   }
   price = predictor.predict_optimal_price(listing_data)
   print(f"Recommended price: ${price:.2f}/night")
   ```

4. **Forecast Booking Probability**

   ```bash
   python src/forecasting/booking_probability.py --listing_id 12345 --model models/booking_model.pkl
   ```

5. **Launch Interactive Dashboard**

   ```bash
   streamlit run src/dashboard/app.py
   ```

   Then visit: `http://localhost:8501`

---

## Project Structure

```
airbnb_predictor/
├── data/                     
│   ├── raw/                
│   ├── processed/          
│   └── scraped/            
├── models/                 
│   ├── price_predictor.pkl
│   ├── booking_model.pkl
│   └── demand_forecaster.pkl
├── src/
│   ├── data_collection/
│   ├── preprocessing/
│   ├── models/
│   ├── forecasting/
│   ├── dashboard/
│   └── utils/
├── notebooks/
│   ├── 01_Market_Analysis.ipynb
│   ├── 02_Price_Optimization.ipynb
│   └── 03_Seasonality_Effects.ipynb
├── config/
│   ├── cities.yaml
│   └── model_config.yaml
├── results/
├── requirements.txt
└── README.md
```

---

## Results

* **Price Prediction**: MAE ≈ \$23.45, R² ≈ 0.892
* **Booking Probability**: ROC AUC ≈ 0.921, Precision ≈ 88.7%
* **Demand Forecasting**: SMAPE ≈ 12.3%
* Visualizations and key driver insights available in the `results/` folder and dashboard.

---

## Contributing

Your contributions are welcome! You could:

* Integrate local event data to improve seasonality modeling
* Experiment with advanced models like XGBoost or Time-Series
* Enhance data visualizations or UX of the Streamlit dashboard

**To contribute:**

1. Fork the repository
2. Create a branch: `git checkout -b feature/NewFeature`
3. Commit changes: `git commit -m "Add new feature"`
4. Push and open a Pull Request

---

## Contact

👤 **Maintainer**: Srinithi Mahalakshmi
📧 **Email**: [srinithiarumugam2003@gmail.com](mailto:srinithiarumugam2003@gmail.com)
🔗 **GitHub**: [Srinithimahalakshmi](https://github.com/Srinithimahalakshmi)

---

⭐ *If you find this project insightful, a star would be greatly appreciated!*

