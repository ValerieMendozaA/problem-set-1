'''
PART 2: Pre-processing
- Take the time to understand the data before proceeding
- Load `pred_universe_raw.csv` into a dataframe and `arrest_events_raw.csv` into a dataframe
- Perform a full outer join/merge on 'person_id' into a new dataframe called `df_arrests`
- Create a column in `df_arrests` called `y` which equals 1 if the person was arrested for a felony crime in the 365 days after their arrest date in `df_arrests`. 
- - So if a person was arrested on 2016-09-11, you would check to see if there was a felony arrest for that person between 2016-09-12 and 2017-09-11.
- - Use a print statment to print this question and its answer: What share of arrestees in the `df_arrests` table were rearrested for a felony crime in the next year?
- Create a predictive feature for `df_arrests` that is called `current_charge_felony` which will equal one if the current arrest was for a felony charge, and 0 otherwise. 
- - Use a print statment to print this question and its answer: What share of current charges are felonies?
- Create a predictive feature for `df_arrests` that is called `num_fel_arrests_last_year` which is the total number arrests in the one year prior to the current charge. 
- - So if someone was arrested on 2016-09-11, then you would check to see if there was a felony arrest for that person between 2015-09-11 and 2016-09-10.
- - Use a print statment to print this question and its answer: What is the average number of felony arrests in the last year?
- Print the mean of 'num_fel_arrests_last_year' -> pred_universe['num_fel_arrests_last_year'].mean()
- Print pred_universe.head()
- Return `df_arrests` for use in main.py for PART 3; if you can't figure this out, save as a .csv in `data/` and read into PART 3 in main.py
'''

# import the necessary packages

import pandas as pd

# Your code here
def run_preprocessing():
  pred_universe = pd.read_csv("./data/pred_universe_raw.csv")
  arrest_events = pd.read_csv("./data/arrest_events_raw.csv")
  pred_universe['arrest_date_univ'] = pd.to_datetime(pred_universe['arrest_date_univ'])
  arrest_events['arrest_date_event'] = pd.to_datetime(arrest_events['arrest_date_event'])
#merge
df_arrests = pd.merge(pred_universe, arrest_events, on='person_id', how='outer', suffixes=('_univ', '_event'))
 y = []   for _, row in df_arrests.iterrows():
        if pd.isna(row['arrest_date_univ']):
            y.append(0)
            continue cond = (arrest_events['person_id'] == row['person_id']) & \
               (arrest_events['arrest_date_event'] > row['arrest_date_univ']) & \
               (arrest_events['arrest_date_event'] <= row['arrest_date_univ'] + pd.Timedelta(365, unit='d')) & \
               (arrest_events['charge_type'] == 'felony')
  y.append(1 if arrest_events.loc[cond].any().any() else 0)   df_arrests['y'] = y


    print("What share of arrestees in the df_arrests table were rearrested for a felony crime in the next year?")
    print(df_arrests['y'].mean())  df_arrests['current_charge_felony'] = (df_arrests['charge_type_univ'] == 'felony').astype(int)
    print("What share of current charges are felonies?")
    print(df_arrests['current_charge_felony'].mean())

  num_fel = []  for _, row in df_arrests.iterrows():
        if pd.isna(row['arrest_date_univ']):
            num_fel.append(0)
            continue cond = (arrest_events['person_id'] == row['person_id']) & \
               (arrest_events['arrest_date_event'] < row['arrest_date_univ']) & \
               (arrest_events['arrest_date_event'] >= row['arrest_date_univ'] - pd.Timedelta(365, unit='d')) & \
               (arrest_events['charge_type'] == 'felony')
        num_fel.append(sum(cond))  df_arrests['num_fel_arrests_last_year'] = num_fel


# prints
    print("What is the average number of felony arrests in the last year?") 
    print(df_arrests['num_fel_arrests_last_year'].mean())
    if 'num_fel_arrests_last_year' in pred_universe.columns:
        print("Mean of num_fel_arrests_last_year in pred_universe:")
        print(pred_universe['num_fel_arrests_last_year'].mean())
    else:
        print("num_fel_arrests_last_year column not found in pred_universe")
    print("First 5 rows of pred_universe:")
    print(pred_universe.head())
  return df_arrests

