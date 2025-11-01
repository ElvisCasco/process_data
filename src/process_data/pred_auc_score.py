# h. Predict the targets for both the train and test sets 
# and add the prediction as a new column 
# (use predict_proba from the model to get 
# the predicted probabilities) name the new column 
# something like predictions.

from typing import Sequence, Tuple
import pandas as pd
from sklearn.metrics import roc_auc_score

def pred_auc_score(y_true: Sequence, y_score: Sequence) -> float:
    """Compute ROC AUC given true labels and predicted scores/probabilities."""
    return float(roc_auc_score(y_true, y_score))

def add_predictions(
    model,
    train_df: pd.DataFrame,
    test_df: pd.DataFrame,
    features: Sequence[str],
    pred_col: str = "predictions",
    inplace: bool = False,
) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """
    Add predicted probabilities to both train and test DataFrames as a new column.

    - model: fitted sklearn classifier with predict_proba
    - train_df, test_df: DataFrames containing the feature columns
    - features: list of feature column names to use for prediction
    - pred_col: name of the output column (default: "predictions")
    - inplace: if True, modify inputs in place; otherwise return copies

    Returns (train_df_with_predictions, test_df_with_predictions)
    """
    missing_train = [c for c in features if c not in train_df.columns]
    missing_test = [c for c in features if c not in test_df.columns]
    if missing_train or missing_test:
        raise KeyError(f"Missing feature columns. Train missing: {missing_train}, Test missing: {missing_test}")

    if not hasattr(model, "predict_proba"):
        raise AttributeError("Model does not support predict_proba; please use a classifier with predict_proba.")

    X_train = train_df[features]
    X_test = test_df[features]

    train_probs = model.predict_proba(X_train)[:, -1]
    test_probs = model.predict_proba(X_test)[:, -1]

    if inplace:
        train_df[pred_col] = train_probs
        test_df[pred_col] = test_probs
        return train_df, test_df

    train_out = train_df.copy()
    test_out = test_df.copy()
    train_out[pred_col] = train_probs
    test_out[pred_col] = test_probs
    return train_out, test_out