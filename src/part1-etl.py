'''
PART 1: ETL the two datasets and save each in `data/` as .csv's
'''
import pandas as pd

def run_etl():
    #  data
    pred_universe = pd.read_feather(
        "https://www.dropbox.com/scl/fi/69syqjo6pfrt9123rubio/universe_lab6.feather?dl=1"
    )
    arrest_events = pd.read_feather(
        "https://www.dropbox.com/scl/fi/wv9kthwbj4ahzli3edrd7/arrest_events_lab6.feather?dl=1"
    )
 # Clean up date 
    pred_universe['arrest_date_univ'] = pd.to_datetime(pred_universe.filing_date)
    arrest_events['arrest_date_event'] = pd.to_datetime(arrest_events.filing_date)
  # columns
    pred_universe.drop(columns='filing_date', inplace=True)
    arrest_events.drop(columns='filing_date', inplace=True)
  # results
    pred_universe.to_csv("./data/pred_universe_raw.csv", index=False)
    arrest_events.to_csv("./data/arrest_events_raw.csv", index=False)

    print("ETL complete: files saved in /data/")


# Save both data frames to `data/` -> 'pred_universe_raw.csv', 'arrest_events_raw.csv'
