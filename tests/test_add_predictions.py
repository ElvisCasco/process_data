import pytest
import pandas as pd
import numpy as np
from process_data import data_train_models
try:
    from process_data import add_predictions
except ImportError:
    from process_data.pred_auc_score import add_predictions


def test_add_predictions_basic():
    """Test adding predictions to train and test DataFrames"""
    # Create and train model
    X_train = pd.DataFrame({"x1": [0, 1, 2, 3], "x2": [1, 1, 0, 0]})
    y_train = pd.Series([0, 0, 1, 1])
    
    train_df = pd.DataFrame({"x1": [0, 1, 2, 3], "x2": [1, 1, 0, 0], "y": [0, 0, 1, 1]})
    test_df = pd.DataFrame({"x1": [0.5, 2.5], "x2": [1, 0], "y": [0, 1]})
    
    model = data_train_models(X_train, y_train, model_type="logreg")
    
    # Add predictions
    train_pred, test_pred = add_predictions(
        model, train_df, test_df, 
        features=["x1", "x2"], 
        pred_col="predictions",
        inplace=False
    )
    
    # Check predictions column exists
    assert "predictions" in train_pred.columns
    assert "predictions" in test_pred.columns
    
    # Check original columns preserved
    assert "y" in train_pred.columns
    assert "y" in test_pred.columns


def test_add_predictions_inplace_false():
    """Test that inplace=False doesn't modify original DataFrames"""
    X_train = pd.DataFrame({"x1": [0, 1, 2, 3], "x2": [1, 1, 0, 0]})
    y_train = pd.Series([0, 0, 1, 1])
    
    train_df = pd.DataFrame({"x1": [0, 1, 2, 3], "x2": [1, 1, 0, 0]})
    test_df = pd.DataFrame({"x1": [0.5, 2.5], "x2": [1, 0]})
    
    model = data_train_models(X_train, y_train, model_type="logreg")
    
    train_pred, test_pred = add_predictions(
        model, train_df, test_df,
        features=["x1", "x2"],
        pred_col="predictions",
        inplace=False
    )
    
    # Original DataFrames should not have predictions column
    assert "predictions" not in train_df.columns
    assert "predictions" not in test_df.columns


def test_add_predictions_inplace_true():
    """Test that inplace=True modifies original DataFrames"""
    X_train = pd.DataFrame({"x1": [0, 1, 2, 3], "x2": [1, 1, 0, 0]})
    y_train = pd.Series([0, 0, 1, 1])
    
    train_df = pd.DataFrame({"x1": [0, 1, 2, 3], "x2": [1, 1, 0, 0]})
    test_df = pd.DataFrame({"x1": [0.5, 2.5], "x2": [1, 0]})
    
    model = data_train_models(X_train, y_train, model_type="logreg")
    
    train_pred, test_pred = add_predictions(
        model, train_df, test_df,
        features=["x1", "x2"],
        pred_col="predictions",
        inplace=True
    )
    
    # Original DataFrames should have predictions column
    assert "predictions" in train_df.columns
    assert "predictions" in test_df.columns


def test_add_predictions_custom_column_name():
    """Test using custom prediction column name"""
    X_train = pd.DataFrame({"x1": [0, 1, 2, 3], "x2": [1, 1, 0, 0]})
    y_train = pd.Series([0, 0, 1, 1])
    
    train_df = pd.DataFrame({"x1": [0, 1, 2, 3], "x2": [1, 1, 0, 0]})
    test_df = pd.DataFrame({"x1": [0.5, 2.5], "x2": [1, 0]})
    
    model = data_train_models(X_train, y_train, model_type="logreg")
    
    train_pred, test_pred = add_predictions(
        model, train_df, test_df,
        features=["x1", "x2"],
        pred_col="my_predictions",
        inplace=False
    )
    
    assert "my_predictions" in train_pred.columns
    assert "my_predictions" in test_pred.columns


def test_add_predictions_probability_range():
    """Test that predictions are probabilities between 0 and 1"""
    np.random.seed(42)
    X_train = pd.DataFrame({
        "x1": np.random.randn(50),
        "x2": np.random.randn(50)
    })
    y_train = pd.Series(np.random.randint(0, 2, 50))
    
    train_df = X_train.copy()
    test_df = pd.DataFrame({
        "x1": np.random.randn(10),
        "x2": np.random.randn(10)
    })
    
    model = data_train_models(X_train, y_train, model_type="logreg")
    
    train_pred, test_pred = add_predictions(
        model, train_df, test_df,
        features=["x1", "x2"],
        pred_col="predictions",
        inplace=False
    )
    
    # Check all predictions are between 0 and 1
    assert all(0 <= p <= 1 for p in train_pred["predictions"])
    assert all(0 <= p <= 1 for p in test_pred["predictions"])