# Data Analytics and Machine Learning Project Suite

Hi, I'm **Ramkrishna Majumder**. In this repository, I have organized a collection of data analytics and machine learning tasks into three levels. The projects cover data cleaning, exploratory data analysis, visualization, regression, time-series analysis, clustering, classification, dashboard planning, and sentiment analysis.

## Project Overview

I divided the work into three levels so that each level focuses on different data analysis and machine learning techniques.

### Level 1: Data Analysis Fundamentals

- **Data Cleaning:** I inspect the Iris dataset, check missing values, remove duplicate rows, standardize column names, and save a cleaned CSV file.
- **Exploratory Data Analysis (EDA):** I generate descriptive statistics, examine numeric correlations, and create histograms and a scatter plot.
- **Data Visualization:** I visualize Iris species counts and explore sepal and petal measurements using bar, line, and scatter plots.

### Level 2: Intermediate Analysis and Machine Learning

- **Regression Analysis:** I train a Linear Regression model on a house-price dataset and evaluate it using Mean Squared Error (MSE) and the R² score.
- **Time-Series Analysis:** I analyze AAPL stock closing prices, calculate a 30-day moving average, and perform seasonal decomposition.
- **Clustering Analysis:** I standardize Iris features, use the elbow method to explore the number of clusters, and apply K-Means clustering.

### Level 3: Advanced Analytics Tasks

- **Classification:** I use a customer churn dataset to train Logistic Regression and Random Forest models. I also use GridSearchCV to tune Random Forest parameters and evaluate the models with accuracy and a classification report.
- **Dashboard Guide:** I document steps for building an interactive dashboard in Power BI or Tableau with charts, KPI cards, filters, and slicers.
- **Sentiment Analysis:** I use TextBlob to classify text as positive, negative, or neutral, then visualize sentiment counts and generate a word cloud.

## Technologies and Libraries

- Python
- Pandas
- Matplotlib
- Scikit-learn
- Statsmodels
- TextBlob
- WordCloud
- Power BI or Tableau (dashboard task)

## Repository Structure

```text
Data_Analytics_Project_Folder/
├── README.md
├── Level_1/
│   ├── Task_1_Data_Cleaning/
│   │   └── iris_cleaning.py
│   ├── Task_2_EDA/
│   │   └── iris_eda.py
│   └── Task_3_Visualization/
│       └── iris_visualization.py
├── Level_2/
│   ├── Task_1_Regression/
│   │   └── house_regression.py
│   ├── Task_2_Time_Series/
│   │   └── stock_time_series.py
│   └── Task_3_Clustering/
│       └── iris_clustering.py
└── Level_3/
    ├── Task_1_Classification/
    │   └── customer_churn_classification.py
    ├── Task_2_Dashboard_Guide/
    │   └── powerbi_tableau_steps.txt
    └── Task_3_Sentiment_Analysis/
        └── sentiment_analysis.py
```

## Datasets

The scripts refer to these datasets:

- Iris dataset: `1) iris.csv`
- Stock prices dataset: `2) Stock Prices Data Set.csv`
- Sentiment dataset: `3) Sentiment dataset.csv`
- House prediction dataset: `4) house Prediction Data Set.csv`
- Customer churn datasets: `churn-bigml-80.csv` and `churn-bigml-20.csv`

**Note:** These dataset files are referenced by the scripts, but they are not included in the ZIP archive I reviewed. Before running a script, place its required dataset in the expected working directory or update the file path in the script.

## Installation

I recommend using a Python virtual environment.

### Linux/macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Windows

```bash
python -m venv .venv
.venv\\Scripts\\activate
```

Install the libraries used across the projects:

```bash
pip install pandas matplotlib scikit-learn statsmodels textblob wordcloud
```

## How to Run

1. Download or clone this repository.
2. Install the required libraries.
3. Add the dataset needed for the task to the appropriate working directory.
4. Open a terminal in the relevant task folder.
5. Run the corresponding Python script. For example:

```bash
python iris_cleaning.py
```

Use the matching script name for the task you want to run. Some scripts save charts or processed data files in the current working directory.

## What I Practiced

By working through these tasks, I practiced cleaning and exploring datasets, visualizing data, building regression and classification models, evaluating model performance, analyzing time-series data, clustering observations, working with text sentiment, and planning interactive dashboards.

## Author

**Ramkrishna Majumder**
