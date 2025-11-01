from process_data import data_predict, data_train_models
import pandas as pd

def test_data_predict_with_logistic():
    X = pd.DataFrame({"x1": [0, 1, 2, 3], "x2": [1, 1, 0, 0]})
    y = [0, 0, 1, 1]
    model = data_train_models(X, y)
    preds = data_predict(model, X)
    assert len(preds) == len(y)