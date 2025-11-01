# h. Predict the targets for both the train and test sets 
# and add the prediction as a new column 
# (use predict_proba from the model to get 
# the predicted probabilities) name the new column 
# something like predictions.

from typing import Union, Optional
import pandas as pd
from numpy.typing import ArrayLike

def data_predict(
    model, 
    X: Union[pd.DataFrame, ArrayLike], 
    proba: bool = False,
    add_to_df: Optional[pd.DataFrame] = None,
    pred_col: str = "predictions"
) -> Union[ArrayLike, pd.DataFrame]:
    """
    Predict with a fitted model.
    
    Parameters:
    -----------
    model : fitted sklearn estimator
        The trained model
    X : DataFrame or array-like
        Feature data for prediction
    proba : bool, default=False
        If True and model supports predict_proba, return positive class probabilities
    add_to_df : DataFrame, optional
        If provided, add predictions as a new column to this DataFrame
    pred_col : str, default="predictions"
        Name of the prediction column when add_to_df is used
    
    Returns:
    --------
    array or DataFrame
        If add_to_df is None: returns prediction array
        If add_to_df is provided: returns DataFrame with predictions column added
    """
    # Get predictions
    if proba and hasattr(model, "predict_proba"):
        predictions = model.predict_proba(X)[:, -1]
    else:
        predictions = model.predict(X)
    
    # If add_to_df provided, add predictions as a column
    if add_to_df is not None:
        result_df = add_to_df.copy()
        result_df[pred_col] = predictions
        return result_df
    
    return predictions