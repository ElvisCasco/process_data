from typing import Union
import pandas as pd
from numpy.typing import ArrayLike

def data_predict(model, X: Union[pd.DataFrame, ArrayLike], proba: bool = False):
    """Predict with a fitted model. If proba=True and model supports predict_proba, return positive class prob."""
    if proba and hasattr(model, "predict_proba"):
        proba_vals = model.predict_proba(X)
        return proba_vals[:, -1]
    return model.predict(X)