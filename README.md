# Processing Data Library

This exercise was developed by:
- María Victoria Suriel
- Mariajosé Argote
- Elvis Casco

We created tests for the functions in `hw4.py`.

The functions, in the folder `src/process_data` let the user to:

1. `data_loader.py`: Load the data.
2. `data_split.py`: Split the data between train and test.
3. `data_remove_nans.py`: Remove those rows that contain NaN values in the columns: age, gender, ethnicity (using a list to select those columns).
4. `data_fill_nans.py`: Fill NaN with the mean value of the column in the columns: height, weight (using a list to select those columns).
5. `data_encoding.py`: Generate dummies for ethnicity column (One hot encoding); also using a list to select the column, in case the user wanted to choose another column to apply this methodology.
6. `data_binary.py`: Create a binary variable for gender M/F (using a list to select the column).
7. `data_train_models.py`: Train a model in the train data (options: `logreg` for LogisticRegression and `rf` for RandomForestClassifier), using as features the columns: `age`, `height`, `weight`, `aids`, `cirrhosis`, `hepatic_failure`, `immunosuppression`, `leukemia`, `lymphoma`, `solid_tumor_with_metastasis`. The target is the column: `diabetes_mellitus`
8. `data_predict.py`: Predict the targets for both the train and test sets and add the prediction as a new column (use predict_proba from the model to get the predicted probabilities) name the new column something like predictions.
9. `pred_auc_score.py`: Compute the train and test roc_auc metric using roc_auc_score from sklearn.

For each of the functions, a `test_` file was created in the folder `tests`.

 A notebook that imports the functions and executes the previous steps was created: `process_data_demo.ipynb`. For its use, you must change the folder that contains the file `sample_diabetes_mellitus_data.csv` in the variable `wd` at the beginning of the code.
