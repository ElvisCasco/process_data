import pandas as pd
from process_data import data_train_models

def test_data_train_models_logreg_and_rf():
    X = pd.DataFrame({"x1": [0, 1, 2, 3], "x2": [1, 1, 0, 0]})
    y = [0, 0, 1, 1]

    m_lr = data_train_models(X, y, model_type="logreg")
    m_rf = data_train_models(X, y, model_type="rf")

    assert hasattr(m_lr, "predict")
    assert hasattr(m_rf, "predict")

    preds_lr = m_lr.predict(X)
    preds_rf = m_rf.predict(X)
    assert len(preds_lr) == len(y)
    assert len(preds_rf) == len(y)