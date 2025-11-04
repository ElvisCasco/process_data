# Processing Data

a. Load the data.
b. Split the data between train and test. (you can use train_test_split from sklearn or any other way)
c. Remove those rows that contain NaN values in the columns: age, gender, ethnicity.
d. Fill NaN with the mean value of the column in the columns: height, weight.
e. Generate dummies for ethnicity column (One hot encoding).
f. Create a binary variable for gender M/F.
g. Train a model (for instance LogisticRegression or RandomForestClassifier from sklearn) in the train data. Use as features the columns: `age`, `height`, `weight`, `aids`, `cirrhosis`, `hepatic_failure`, `immunosuppression`, `leukemia`, `lymphoma`, `solid_tumor_with_metastasis`. Use as target the column: `diabetes_mellitus`
h. Predict the targets for both the train and test sets and add the prediction as a new column (use predict_proba from the model to get the predicted probabilities) name the new column something like predictions.
i. Compute the train and test roc_auc metric using roc_auc_score from sklearn.
7. Create a notebook that imports the functions and executes the previous steps in order to
