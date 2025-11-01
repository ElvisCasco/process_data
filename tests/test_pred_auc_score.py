import pytest
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from process_data import pred_auc_score, data_train_models


def test_pred_auc_score_perfect_predictions():
    """Test AUC score with perfect predictions"""
    y_true = [0, 0, 1, 1]
    y_score = [0.1, 0.2, 0.9, 0.95]
    
    auc = pred_auc_score(y_true, y_score)
    
    assert auc == 1.0


def test_pred_auc_score_random_predictions():
    """Test AUC score with random predictions (should be around 0.5)"""
    np.random.seed(42)
    y_true = np.random.randint(0, 2, 100)
    y_score = np.random.random(100)
    
    auc = pred_auc_score(y_true, y_score)
    
    # Random predictions should give AUC around 0.5
    assert 0.3 < auc < 0.7


def test_pred_auc_score_with_trained_model():
    """Test AUC score with predictions from a trained model"""
    # Create training data
    np.random.seed(42)
    X_train = pd.DataFrame({
        "feature1": np.random.randn(100),
        "feature2": np.random.randn(100)
    })
    y_train = (X_train["feature1"] + X_train["feature2"] > 0).astype(int)
    
    # Train model
    model = data_train_models(X_train, y_train, model_type="logreg")
    
    # Get predictions
    y_proba = model.predict_proba(X_train)[:, 1]
    
    # Calculate AUC
    auc = pred_auc_score(y_train, y_proba)
    
    # Should be quite high for this simple linearly separable problem
    assert auc > 0.8


def test_pred_auc_score_returns_float():
    """Test that function returns a float"""
    y_true = [0, 1, 0, 1]
    y_score = [0.2, 0.8, 0.3, 0.7]
    
    auc = pred_auc_score(y_true, y_score)
    
    assert isinstance(auc, float)


def test_pred_auc_score_invalid_input():
    """Test error handling with mismatched lengths"""
    y_true = [0, 1, 0]
    y_score = [0.2, 0.8]  # Different length
    
    with pytest.raises(ValueError):
        pred_auc_score(y_true, y_score)