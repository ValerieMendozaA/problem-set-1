'''
PART 5: Calibration-light
Use `calibration_plot` function to create a calibration curve for the logistic regression model. Set `n_bins` to 5. (The calibration plot may have less than 5 points, that's ok) 
Use `calibration_plot` function to create a calibration curve for the decision tree model. Set `n_bins` to 5. (The calibration plot may have less than 5 points, that's ok) 
Which model is more calibrated? Print this question and your answer. 

Extra Credit
Compute  PPV for the logistic regression model for arrestees ranked in the top 50 for predicted risk
Compute  PPV for the decision tree model for arrestees ranked in the top 50 for predicted risk
Compute AUC for the logistic regression model
Compute AUC for the decision tree model
Do both metrics agree that one model is more accurate than the other? Print this question and your answer. 
'''

# Import any further packages you may need for PART 5
from sklearn.calibration import calibration_curve
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import roc_auc_score
import pandas as pd

# Your code here
         def run_calibration_and_metrics():
    #  test data
    df = pd.read_csv('./data/df_arrests_test.csv')

    # make calibration plots
    calibration_plot(df['y'], df['pred_lr'], n_bins=5)  calibration_plot(df['y'], df['pred_dt'], n_bins=5)
    print("Which model is more calibrated? logistic regression usually is.")

    # check top 50 ppv
    ppv_lr = df.sort_values('pred_lr', ascending=False).head(50)['y'].mean()   ppv_dt = df.sort_values('pred_dt', ascending=False).head(50)['y'].mean()

  # auc scores 
 auc_lr = roc_auc_score(df['y'], df['pred_lr'])  auc_dt = roc_auc_score(df['y'], df['pred_dt'])

    print("PPV top 50 LR:", ppv_lr) print("PPV top 50 DT:", ppv_dt)
    print("AUC LR:", auc_lr) print("AUC DT:", auc_dt)

    # better check
    if (ppv_lr > ppv_dt) and (auc_lr > auc_dt):
        print("both say logistic regression is better")
    elif (ppv_lr < ppv_dt) and (auc_lr < auc_dt):
        print("both say decision tree is better")
    else:
        print("metrics give mixed results")
