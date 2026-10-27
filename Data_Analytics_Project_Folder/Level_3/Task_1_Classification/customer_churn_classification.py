
import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.metrics import accuracy_score, classification_report
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

train_df = pd.read_csv("churn-bigml-80.csv")
test_df = pd.read_csv("churn-bigml-20.csv")

df = pd.concat([train_df, test_df], ignore_index=True)

label_cols = ["State", "International plan", "Voice mail plan"]

encoder = LabelEncoder()

for col in label_cols:
    df[col] = encoder.fit_transform(df[col])

df["Churn"] = df["Churn"].astype(int)

X = df.drop("Churn", axis=1)
y = df["Churn"]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42
)

log_model = LogisticRegression(max_iter=1000)
log_model.fit(X_train, y_train)

predictions = log_model.predict(X_test)

print("Logistic Regression Accuracy:")
print(accuracy_score(y_test, predictions))

print(classification_report(y_test, predictions))

param_grid = {
    "n_estimators": [50, 100],
    "max_depth": [5, 10]
}

grid = GridSearchCV(RandomForestClassifier(), param_grid, cv=3)

grid.fit(X_train, y_train)

print("Best Parameters:")
print(grid.best_params_)

best_model = grid.best_estimator_

rf_predictions = best_model.predict(X_test)

print("Random Forest Accuracy:")
print(accuracy_score(y_test, rf_predictions))
