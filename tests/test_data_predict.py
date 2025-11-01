import pytest
import pandas as pd
import numpy as np
from process_data import data_predict, data_train_models


def test_data_predict_proba():
    """Test predict_proba functionality"""
    X_train = pd.DataFrame({"x1": [0, 1, 2, 3], "x2": [1, 1, 0, 0]})
    y_train = pd.Series([0, 0, 1, 1])
    
    model = data_train_models(X_train, y_train, model_type="logreg")
    
    X_test = pd.DataFrame({"x1": [0.5, 2.5], "x2": [1, 0]})
    predictions = data_predict(model, X_test, proba=True)
    
    assert len(predictions) == 2
    assert all(0 <= p <= 1 for p in predictions)


def test_data_predict_class():
    """Test class prediction (not proba)"""
    X_train = pd.DataFrame({"x1": [0, 1, 2, 3], "x2": [1, 1, 0, 0]})
    y_train = pd.Series([0, 0, 1, 1])
    
    model = data_train_models(X_train, y_train, model_type="logreg")
    
    X_test = pd.DataFrame({"x1": [0.5, 2.5], "x2": [1, 0]})
    predictions = data_predict(model, X_test, proba=False)
    
    assert len(predictions) == 2
    assert all(p in [0, 1] for p in predictions)


def test_data_predict_random_forest():
    """Test predictions with RandomForest model"""
    np.random.seed(42)
    X_train = pd.DataFrame({
        "x1": np.random.randn(50),
        "x2": np.random.randn(50)
    })
    y_train = pd.Series(np.random.randint(0, 2, 50))
    
    model = data_train_models(X_train, y_train, model_type="rf")
    
    X_test = pd.DataFrame({
        "x1": np.random.randn(10),
        "x2": np.random.randn(10)
    })
    
    predictions = data_predict(model, X_test, proba=True)
    
    assert len(predictions) == 10
    assert all(0 <= p <= 1 for p in predictions)


def test_data_predict_consistency():
    """Test that predictions are consistent"""
    X_train = pd.DataFrame({"x1": [0, 1, 2, 3], "x2": [1, 1, 0, 0]})
    y_train = pd.Series([0, 0, 1, 1])
    
    model = data_train_models(X_train, y_train, model_type="logreg")
    
    X_test = pd.DataFrame({"x1": [1.5], "x2": [0.5]})
    
    # Multiple calls should give same results
    pred1 = data_predict(model, X_test, proba=True)
    pred2 = data_predict(model, X_test, proba=True)
    
    np.testing.assert_array_almost_equal(pred1, pred2)