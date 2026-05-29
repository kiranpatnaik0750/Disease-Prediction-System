import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from xgboost import XGBClassifier


print("\nLoading dataset...")

df = pd.read_csv("training_data_12symptoms.csv")

X = df.drop("prognosis", axis=1)
y = df["prognosis"]

# convert disease names to numbers
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(y)

joblib.dump(label_encoder, "label_encoder.pkl")

print("Dataset Loaded")


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

models = {

"Logistic Regression": LogisticRegression(max_iter=2000),

"Random Forest": RandomForestClassifier(
    n_estimators=300,
    max_depth=10
),

"Gradient Boosting": GradientBoostingClassifier(),

"XGBoost": XGBClassifier(
    n_estimators=300,
    learning_rate=0.05,
    max_depth=6,
    eval_metric="mlogloss"
)

}

best_model = None
best_accuracy = 0
best_name = ""

print("\n========== MODEL ACCURACY DASHBOARD ==========\n")

for name, model in models.items():

    print("Training:", name)

    model.fit(X_train, y_train)

    preds = model.predict(X_test)

    acc = accuracy_score(y_test, preds)

    print(f"{name:<20} {acc*100:.2f}%")

    if acc > best_accuracy:

        best_accuracy = acc
        best_model = model
        best_name = name


print("\n---------------------------------------------")
print("Best Model:", best_name)
print("Accuracy:", best_accuracy*100)

# SAVE BEST MODEL
joblib.dump(best_model, "best_model.pkl")

print("\nModel saved successfully as best_model.pkl")