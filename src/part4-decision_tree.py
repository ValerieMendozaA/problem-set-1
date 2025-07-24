'''
PART 4: Decision Trees
- Read in the dataframe(s) from PART 3
- Create a parameter grid called `param_grid_dt` containing three values for tree depth. (Note C has to be greater than zero) 
- Initialize the Decision Tree model. Assign this to a variable called `dt_model`. 
- Initialize the GridSearchCV using the logistic regression model you initialized and parameter grid you created. Do 5 fold crossvalidation. Assign this to a variable called `gs_cv_dt`. 
- Run the model 
- What was the optimal value for max_depth?  Did it have the most or least regularization? Or in the middle? 
- Now predict for the test set. Name this column `pred_dt` 
- Return dataframe(s) for use in main.py for PART 5; if you can't figure this out, save as .csv('s) in `data/` and read into PART 5 in main.py
'''
# Import any further packages you may need for PART 4
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.model_selection import StratifiedKFold as KFold_strat
from sklearn.tree import DecisionTreeClassifier as DTC

# Your code here
def run_decision_tree():
# PART 3 output
    df_arrests_train = pd.read_csv('./data/df_arrests_train.csv')  df_arrests_test = pd.read_csv('./data/df_arrests_test.csv')
# target
    features = ['num_fel_arrests_last_year', 'current_charge_felony']
  X_train, y_train = df_arrests_train[features], df_arrests_train['y']  X_test, y_test = df_arrests_test[features], df_arrests_test['y']
    param_grid_dt = {'max_depth': [2, 4, 6]}
    dt_model = DTC(random_state=42)
 #CV
    gs_cv_dt = GridSearchCV(dt_model, param_grid_dt, cv=5)  gs_cv_dt.fit(X_train, y_train)
    # Bestdepth
    best_depth = gs_cv_dt.best_params_['max_depth']
    print("Best max_depth:", best_depth)
    if best_depth == min(param_grid_dt['max_depth']):
        print("Regularization: most")
    elif best_depth == max(param_grid_dt['max_depth']):
        print("Regularization: least")
    else:
        print("Regularization: middle")
 # Predict
    df_arrests_test = df_arrests_test.copy()  df_arrests_test['pred_dt'] = gs_cv_dt.predict_proba(X_test)[:, 1]  df_arrests_test.to_csv('./data/df_arrests_test.csv', index=False)
    return df_arrests_train, df_arrests_test
