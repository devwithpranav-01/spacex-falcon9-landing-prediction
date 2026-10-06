# SpaceX Falcon 9 First-Stage Landing Prediction
IBM Applied Data Science Capstone

**Author:** Pranav Vyankatesh Jagdale

Predicts whether a Falcon 9 first stage will land successfully, using launch data from the SpaceX API and Wikipedia.

## Contents
| File | Purpose |
|---|---|
| `01_Data_Collection_API.ipynb` | Collect launch data from the SpaceX REST API |
| `02_Data_Collection_Web_Scraping.ipynb` | Scrape Falcon 9 launch tables from Wikipedia |
| `03_Data_Wrangling.ipynb` | Clean data and create the landing `Class` target |
| `04_EDA_with_SQL.ipynb` | SQL exploration with SQLite |
| `05_EDA_with_Data_Visualization.ipynb` | Plots and feature engineering |
| `06_Interactive_Visual_Analytics_Folium.ipynb` | Launch-site map and distance analysis |
| `07_spacex_dash_app.py` | Plotly Dash dashboard |
| `08_Machine_Learning_Prediction.ipynb` | Four tuned classifiers and evaluation |

## Run
Open each notebook in Google Colab or Jupyter and run the cells top to bottom.
Dashboard: `pip install dash pandas plotly` then `python 07_spacex_dash_app.py`.
