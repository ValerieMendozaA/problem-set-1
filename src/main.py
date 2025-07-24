'''
You will run this problem set from main.py, so set things up accordingly
'''

import pandas as pd
import etl
import preprocessing
import logistic_regression
import decision_tree
import calibration_plot


# Call functions / instanciate objects from the .py files
def main():
    # PART 1: ETL - download and save raw datasets
    etl.run_etl()
    # PART 2: Preprocessing - load, merge, create features, save processed data
    preprocessing_df = preprocessing.run_preprocessing()
    # PART 3: Logistic Regression - train model, save train/test splits and preds
    train_df, test_df = logistic_regression.run_logistic_regression(preprocessing_df)
    # PART 4: Decision Tree - train and predict
    train_df_dt, test_df_dt = decision_tree.run_decision_tree()
    # PART 5: Calibration plot and metrics - analyze models
    calibration_plot.run_calibration_and_metrics()

if __name__ == "__main__":
    main()
