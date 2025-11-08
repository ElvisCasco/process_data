# g. Train a model 
# (for instance LogisticRegression or RandomForestClassifier from sklearn) 
# in the train data. 
# Use as features the columns: 
# ‘age’, ‘height’, ‘weight’, ‘aids’, ‘cirrhosis’, 
# ‘hepatic_failure’, ‘immunosuppression’, 
# ‘leukemia’, ‘lymphoma’, ‘solid_tumor_with_metastasis’. 
# Use as target the column: ‘diabetes_mellitus’

# g. Train a model 
# (for instance LogisticRegression or RandomForestClassifier from sklearn) 
# in the train data. 

from typing import Optional, Literal
from numpy.typing import ArrayLike
from sklearn.base import BaseEstimator
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

def model_train_models(
    X: ArrayLike,
    y: ArrayLike,
    model: Optional[BaseEstimator] = None,
    model_type: Literal["logreg", "rf"] = "logreg",
    random_state: int = 42,
) -> BaseEstimator:
    """
    Fit and return a classifier.
    - If model is None, create it based on model_type:
      * "logreg" -> LogisticRegression(max_iter=1000, random_state=random_state)
      * "rf"     -> RandomForestClassifier(n_estimators=200, random_state=random_state)
    - If model is provided, model_type is ignored.
    """
    if model is None:
        if model_type == "rf":
            model = RandomForestClassifier(n_estimators=200, random_state=random_state)
        else:
            model = LogisticRegression(max_iter=1000, random_state=random_state)

    model.fit(X, y)
    return model