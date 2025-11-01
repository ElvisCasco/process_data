import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from process_data import data_predict

def test_data_predict_with_dataframe():
    # Create sample data
    X_train = pd.DataFrame({"x1": [0, 1, 2, 3], "x2": [1, 1, 0, 0]})
    y_train = [0, 0, 1, 1]
    
    # Train model
    model = LogisticRegression(max_iter=1000, random_state=42)
    model.fit(X_train, y_train)
    
    # Test DataFrame with additional columns
    test_df = pd.DataFrame({
        "x1": [0.5, 1.5, 2.5],
        "x2": [1, 0.5, 0],
        "id": [1, 2, 3],
        "other_col": ["a", "b", "c"]
    })
    
    # Get predictions as array
    preds_array = data_predict(model, test_df[["x1", "x2"]], proba=True)
    assert len(preds_array) == 3
    assert all(0 <= p <= 1 for p in preds_array)
    
    # Add predictions to DataFrame
    result_df = data_predict(
        model, 
        test_df[["x1", "x2"]], 
        proba=True, 
        add_to_df=test_df,
        pred_col="predictions"
    )
    
    assert "predictions" in result_df.columns
    assert len(result_df) == len(test_df)
    assert list(result_df.columns) == ["x1", "x2", "id", "other_col", "predictions"]
    assert all(result_df["predictions"] == preds_array)
    
    # Original DataFrame should be unchanged
    assert "predictions" not in test_df.columns

def test_data_predict_both_train_and_test():
    """Test adding predictions to both train and test sets"""
    X_train = pd.DataFrame({"x1": [0, 1, 2, 3], "x2": [1, 1, 0, 0]})
    y_train = [0, 0, 1, 1]
    X_test = pd.DataFrame({"x1": [0.5, 2.5], "x2": [1, 0]})
    
    train_df = pd.DataFrame({"x1": [0, 1, 2, 3], "x2": [1, 1, 0, 0], "y": y_train})
    test_df = pd.DataFrame({"x1": [0.5, 2.5], "x2": [1, 0], "y": [0, 1]})
    
    model = LogisticRegression(max_iter=1000, random_state=42)
    model.fit(X_train, y_train)
    
    # Add predictions to both train and test
    train_with_pred = data_predict(
        model, train_df[["x1", "x2"]], proba=True, 
        add_to_df=train_df, pred_col="predictions"
    )
    test_with_pred = data_predict(
        model, test_df[["x1", "x2"]], proba=True, 
        add_to_df=test_df, pred_col="predictions"
    )
    
    assert "predictions" in train_with_pred.columns
    assert "predictions" in test_with_pred.columns
    assert len(train_with_pred) == len(train_df)
    assert len(test_with_pred) == len(test_df)