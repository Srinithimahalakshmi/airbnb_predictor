# Airbnb Price & Demand Prediction System 🏡📊

![Airbnb Analytics](https://img.shields.io/badge/domain-short_term_rentals-blue) ![Machine Learning](https://img.shields.io/badge/ML-Regression_&_Classification-green) ![Python](https://img.shields.io/badge/Python-3.8%2B-yellow)

Machine learning system for predicting optimal Airbnb listing prices and booking probability. Includes market analysis, competitive pricing, and occupancy forecasting.

## Features ✨
- Optimal price recommendation engine
- Booking probability prediction
- Seasonal demand forecasting
- Neighborhood value analysis
- Amenity impact scoring
- Competitive positioning insights

## Installation 💻

### Prerequisites
- Python 3.8+
- pip package manager
- Google Maps API key (for geocoding)

### Setup
```bash
# Clone repository
git clone https://github.com/Srinithimahalakshmi/airbnb_predictor.git
cd airbnb_predictor

# Create virtual environment
python -m venv airbnb_env
source airbnb_env/bin/activate  # Linux/Mac
airbnb_env\Scripts\activate    # Windows

# Install dependencies
pip install -r requirements.txt

# Set API key (get from https://developers.google.com/maps)
echo "GOOGLE_MAPS_API_KEY=your_key_here" > .env
Dataset 📊
Airbnb Market Data (included in data/)

Contains:

Listing details (location, room type, amenities)

Historical price data

Booking calendars

Review scores

Sources:

InsideAirbnb.com datasets

Scraped market data (see data_collection/)

Key features:

Neighborhood desirability score

Seasonality factors

Amenity flags (pool, wifi, etc.)

Review sentiment score

Usage 🚀
1. Data Preparation
bash
python src/data_preprocessing.py --city "New York"
2. Train Price Prediction Model
bash
python src/models/train_price_model.py --data data/processed/ny_listings.csv --model models/price_predictor.pkl
3. Predict Optimal Price
python
from src.predict import AirbnbPricePredictor

predictor = AirbnbPricePredictor('models/price_predictor.pkl')

listing_data = {
    'neighborhood': 'Brooklyn',
    'room_type': 'Entire home/apt',
    'accommodates': 4,
    'bedrooms': 2,
    'bathrooms': 1.5,
    'amenities': ['wifi', 'kitchen', 'washer'],
    'review_scores_rating': 4.8
}

optimal_price = predictor.predict_optimal_price(listing_data)
print(f"Recommended price: ${optimal_price:.2f}/night")
4. Booking Probability Forecast
bash
python src/forecasting/booking_probability.py --listing_id 12345 --model models/booking_model.pkl
5. Launch Dashboard
bash
streamlit run src/dashboard/app.py  # Access at http://localhost:8501
Model Performance 📈
Model/Task	Metric	Performance
Price Prediction	MAE	$23.45
R²	0.892
Booking Probability	ROC AUC	0.921
Precision	88.7%
Demand Forecasting	SMAPE	12.3%
https://results/neighborhood_prices.png <!-- Add actual path -->

Key Price Drivers 🔑
Location (walk score, transit access)

Property type and size

Seasonality and local events

Review scores and ratings

Amenities quality

Host reputation

Repository Structure 📂
text
├── data/                   # Raw and processed datasets
│   ├── raw/                # Original datasets
│   ├── processed/          # Cleaned data
│   └── scraped/            # Market data collection
│
├── models/                 # Trained models
│   ├── price_predictor.pkl
│   ├── booking_model.pkl
│   └── demand_forecaster.pkl
│
├── src/                    # Source code
│   ├── data_collection/    # Web scraping tools
│   ├── data_preprocessing/ 
│   ├── geospatial/         # Location analysis
│   ├── models/             # ML models
│   │   ├── train_price_model.py
│   │   ├── train_booking_model.py
│   │   └── evaluate_models.py
│   ├── forecasting/        # Time series analysis
│   ├── dashboard/          # Streamlit dashboard
│   └── utils/              # Helper functions
│
├── notebooks/              # Jupyter notebooks
│   ├── 01_Market_Analysis.ipynb
│   ├── 02_Price_Optimization.ipynb
│   └── 03_Seasonality_Effects.ipynb
│
├── config/                 # Configuration files
│   ├── cities.yaml         # City-specific parameters
│   └── model_config.yaml
│
├── results/                # Output visualizations
├── requirements.txt        # Python dependencies
└── LICENSE
Business Applications 💼
New Hosts: Determine competitive pricing

Existing Hosts: Optimize prices for seasons/events

Property Managers: Portfolio performance analysis

Investors: Identify high-potential neighborhoods

Guests: Find best value listings

Sample Dashboard View
https://src/dashboard/static/dashboard_screenshot.png <!-- Add actual path -->
Interactive dashboard showing price recommendations and occupancy forecasts

Contributors 👥
Srinithi Mahalakshmi
https://img.shields.io/badge/LinkedIn-Connect-blue
https://img.shields.io/badge/GitHub-Follow-lightgrey

