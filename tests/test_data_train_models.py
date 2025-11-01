import pytest
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from process_data import data_train_models


def test_data_train_models_logreg():
    """Test training LogisticRegression model"""
    X = pd.DataFrame({
        "age": [25, 30, 35, 40, 45],
        "height": [170, 175, 180, 165, 172]
    })
    y = pd.Series([0, 0, 1, 1, 0])
    
    model = data_train_models(X, y, model_type="logreg")
    
    assert isinstance(model, LogisticRegression)
    assert hasattr(model, "predict")
    assert hasattr(model, "predict_proba")


def test_data_train_models_random_forest():
    """Test training RandomForestClassifier model"""
    X = pd.DataFrame({
        "age": [25, 30, 35, 40, 45, 50],
        "height": [170, 175, 180, 165, 172, 168]
    })
    y = pd.Series([0, 0, 1, 1, 0, 1])
    
    model = data_train_models(X, y, model_type="rf")
    
    assert isinstance(model, RandomForestClassifier)
    assert hasattr(model, "predict")
    assert hasattr(model, "predict_proba")


def test_data_train_models_invalid_type():
    """Test error handling for invalid model type"""
    X = pd.DataFrame({"col1": [1, 2, 3]})
    y = pd.Series([0, 1, 0])
    
    with pytest.raises((ValueError, KeyError)):
        data_train_models(X, y, model_type="invalid")


def test_data_train_models_prediction():
    """Test that trained model can make predictions"""
    X_train = pd.DataFrame({
        "feature1": [1, 2, 3, 4, 5],
        "feature2": [5, 4, 3, 2, 1]
    })
    y_train = pd.Series([0, 0, 1, 1, 1])
    
    model = data_train_models(X_train, y_train, model_type="logreg")
    
    # Test prediction
    X_test = pd.DataFrame({"feature1": [2.5], "feature2": [3.5]})
    prediction = model.predict(X_test)
    
    assert len(prediction) == 1
    assert prediction[0] in [0, 1]


def test_data_train_models_with_more_features():
    """Test training with multiple features (like diabetes dataset)"""
    np.random.seed(42)
    X = pd.DataFrame({
        "age": np.random.randint(18, 85, 100),
        "height": np.random.normal(170, 10, 100),
        "weight": np.random.normal(75, 15, 100),
        "feature1": np.random.randint(0, 2, 100),
        "feature2": np.random.randint(0, 2, 100),
    })
    y = pd.Series(np.random.randint(0, 2, 100))
    
    model_lr = data_train_models(X, y, model_type="logreg")
    model_rf = data_train_models(X, y, model_type="rf")
    
    assert isinstance(model_lr, LogisticRegression)
    assert isinstance(model_rf, RandomForestClassifier)
    
    # Test predictions
    predictions_lr = model_lr.predict(X)
    predictions_rf = model_rf.predict(X)
    
    assert len(predictions_lr) == 100
    assert len(predictions_rf) == 100