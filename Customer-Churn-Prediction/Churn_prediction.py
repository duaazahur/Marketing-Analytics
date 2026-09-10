from typing import Tuple, List
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    confusion_matrix
)
#
from sklearn.linear_model import *
from sklearn.ensemble import *

# =========================================================
# STEP 1 - LOAD DATASETS
# =========================================================
def load_datasets(
    dataset_path: str
) -> Tuple[pd.DataFrame, pd.DataFrame]:

    """
    Load training and test datasets.
    """

    train_df = pd.read_csv(dataset_path)

    train_df, test_df = train_test_split(
        train_df,
        test_size=0.20,
        random_state=42,
        stratify=train_df["churn"]
    )

    return (
        train_df.reset_index(drop=True),
        test_df.reset_index(drop=True)
    )

# =========================================================
# STEP 2 - DATASET OVERVIEW
# =========================================================

def dataset_overview(
    train_df: pd.DataFrame,
    test_df: pd.DataFrame
) -> None:

    print("=" * 50)
    print("TRAINING DATASET")
    print("=" * 50)

    print("Shape:", train_df.shape)

    print("\nMissing Values:")
    print(train_df.isnull().sum())

    print("\nStatistics:")
    print(train_df.describe(include="all"))

    print("\n")

    print("=" * 50)
    print("TEST DATASET")
    print("=" * 50)

    print("Shape:", test_df.shape)

    print("\nMissing Values:")
    print(test_df.isnull().sum())

    print("\nStatistics:")
    print(test_df.describe(include="all"))

# =========================================================
# STEP 3 - DEFINE FEATURES AND TARGET
# =========================================================

def split_features_target(
    train_df: pd.DataFrame,
    test_df: pd.DataFrame,
    target_column: str
) -> Tuple[
    pd.DataFrame,
    pd.Series,
    pd.DataFrame,
    pd.Series
]:
    """
    Separate features and target variable.
    """

    X_train = train_df.drop(columns=[target_column])
    y_train = train_df[target_column]

    X_test = test_df.drop(columns=[target_column])
    y_test = test_df[target_column]

    return X_train, y_train, X_test, y_test

# =========================================================
# STEP 4 - IDENTIFY COLUMN TYPES
# =========================================================

def identify_column_types(
    X_train: pd.DataFrame
) -> Tuple[List[str], List[str]]:

    categorical_cols = X_train.select_dtypes(
        include=["object"]
    ).columns.tolist()

    numeric_cols = X_train.select_dtypes(
        exclude=["object"]
    ).columns.tolist()

    return categorical_cols, numeric_cols


# =========================================================
# STEP 5 - BUILD PREPROCESSOR
# =========================================================

def build_preprocessor(
    numeric_cols: List[str],
    categorical_cols: List[str]
) -> ColumnTransformer:
    """
    Create preprocessing pipeline.
    """

    numeric_transformer = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="median")),
            ("scaler", StandardScaler())
        ]
    )

    categorical_transformer = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="most_frequent")),
            ("onehot", OneHotEncoder(handle_unknown="ignore"))
        ]
    )

    preprocessor = ColumnTransformer(
        transformers=[
            ("num", numeric_transformer, numeric_cols),
            ("cat", categorical_transformer, categorical_cols)
        ]
    )

    return preprocessor


# =========================================================
# STEP 6 - BUILD MODEL PIPELINE
# =========================================================

def build_model(
    preprocessor: ColumnTransformer
) -> Pipeline:
    """
    Create machine learning pipeline.
    """

    model = RandomForestClassifier(
        n_estimators=200,
        random_state=42
    )

    pipeline = Pipeline(
        steps=[
            ("preprocessor", preprocessor),
            ("classifier", model)
        ]
    )

    return pipeline

# =========================================================
# STEP 7 - TRAIN MODEL
# =========================================================

def train_model(
    model: Pipeline,
    X_train: pd.DataFrame,
    y_train: pd.Series
) -> Pipeline:
    """
    Train machine learning model.
    """

    model.fit(X_train, y_train)

    return model
# =========================================================
# STEP 8 - MAKE PREDICTIONS
# =========================================================

def make_predictions(
    model: Pipeline,
    X_test: pd.DataFrame
) -> Tuple[pd.Series, pd.Series]:
    """
    Generate predictions and probabilities.
    """

    y_pred = model.predict(X_test)

    y_prob = model.predict_proba(X_test)[:, 1]

    return y_pred, y_prob


# =========================================================
# STEP 9 - EVALUATE MODEL
# =========================================================

def evaluate_model(
    y_test: pd.Series,
    y_pred: pd.Series,
    y_prob: pd.Series
) -> None:
    """
    Evaluate classification performance.
    """

    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    roc_auc = roc_auc_score(y_test, y_prob)

    print("\n===== MODEL PERFORMANCE =====")
    print(f"Accuracy : {accuracy:.4f}")
    print(f"Precision: {precision:.4f}")
    print(f"Recall   : {recall:.4f}")
    print(f"F1 Score : {f1:.4f}")
    print(f"ROC-AUC  : {roc_auc:.4f}")


# =========================================================
# STEP 10 - CONFUSION MATRIX
# =========================================================

def display_confusion_matrix(
    y_test: pd.Series,
    y_pred: pd.Series
) -> None:
    """
    Display confusion matrix.
    """

    cm = confusion_matrix(y_test, y_pred)

    print("\nConfusion Matrix")
    print(cm)

# =========================================================
# STEP 11 - FEATURE IMPORTANCE
# =========================================================

def feature_importance_analysis(
    model: Pipeline,
    numeric_cols: List[str],
    categorical_cols: List[str]
) -> pd.DataFrame:
    """
    Analyze feature importance.
    """

    preprocessor = model.named_steps["preprocessor"]

    feature_names = (
        numeric_cols +
        list(
            preprocessor
            .named_transformers_["cat"]
            .named_steps["onehot"]
            .get_feature_names_out(categorical_cols)
        )
    )

    importances = model.named_steps["classifier"].feature_importances_

    importance_df = pd.DataFrame({
        "Feature": feature_names,
        "Importance": importances
    })

    importance_df = importance_df.sort_values(
        by="Importance",
        ascending=False
    )

    plt.figure(figsize=(10,6))

    plt.barh(
        importance_df["Feature"].head(10),
        importance_df["Importance"].head(10)
    )

    plt.gca().invert_yaxis()

    plt.title("Top 10 Feature Importances")

    plt.tight_layout()

    plt.savefig("feature_importance.png")

    plt.show()

    return importance_df

# =========================================================
# STEP 12 - SAVE PREDICTIONS
# =========================================================

def save_predictions(
    test_df: pd.DataFrame,
    y_pred: pd.Series,
    y_prob: pd.Series,
    output_file: str
) -> None:
    """
    Save prediction results.
    """

    output = test_df.copy()

    output["Predicted_Churn"] = y_pred

    output["Probability"] = y_prob

    output.to_csv(output_file, index=False)

    print(f"Saved {output_file}")

def save_predictions(
    test_df: pd.DataFrame,
    y_pred: pd.Series,
    y_prob: pd.Series,
    output_file: str
) -> None:

    output = test_df.copy()

    output["Predicted_Churn"] = y_pred
    output["Probability"] = y_prob

    output.to_csv(output_file, index=False)

    print(f"Saved {output_file}")


if __name__ == "__main__":

    for dataset in ["dataset1_HW1.csv", "dataset2_HW1.csv"]:

        print(f"\nProcessing {dataset}")

        train_df, test_df = load_datasets(dataset)

        dataset_overview(train_df, test_df)

        X_train, y_train, X_test, y_test = split_features_target(
            train_df,
            test_df,
            "churn"
        )

        categorical_cols, numeric_cols = identify_column_types(X_train)

        preprocessor = build_preprocessor(
            numeric_cols,
            categorical_cols
        )

        model = build_model(preprocessor)

        model = train_model(
            model,
            X_train,
            y_train
        )

        y_pred, y_prob = make_predictions(
            model,
            X_test
        )

        evaluate_model(
            y_test,
            y_pred,
            y_prob
        )

        display_confusion_matrix(
            y_test,
            y_pred
        )

        feature_importance_analysis(
            model,
            numeric_cols,
            categorical_cols
        )

        output_file = dataset.replace(".csv", "_predictions.csv")

        save_predictions(
            test_df,
            y_pred,
            y_prob,
            output_file
        )