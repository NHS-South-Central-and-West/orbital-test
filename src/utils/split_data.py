import re
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
pd.options.future.infer_string = True

cols = ['NHS_Number', 'Organisation_Code_Provider',
       'Organisation_Code_Commissioner', 'Age_At_Arrival', 'LSOA_11',
       'Index_Of_Multiple_Deprivation',
       'Index_Of_Multiple_Deprivation_Description', 'Stated_Gender',
       'Ethnic_Category', 'LSOA_Site_Of_Treatment_Distance', 'Arrival_DateTime',
       'Arrival_Mode_Desc', 'Attendance_Category',
       'Departure_Time_Since_Arrival', 'Discharge_Status_Desc', 
       'Destination_Desc', 'Acuity_Desc','Acuity_Code_Approved', 
       'Long_Term_Condition_Asthma_Flag','Long_Term_Condition_Cancer_Flag',
       'Long_Term_Condition_Heart_Failure_Flag',
       'Long_Term_Condition_Diabetes_Flag', 'Long_Term_Condition_Renal_Flag',
       'Long_Term_Condition_COPD_Flag', 'Long_Term_Condition_Dementia_Flag',
       'Long_Term_Condition_Count_Number', 'GP_Practice_Code', 'GP_Practice',
       'Patient_Status', 'Care_Home_Status', 'Care_Home_Name', 'Living_Alone',
       'Palliative_Care_Flag', 'Acutely_Unwell_Flag', 'Disability_Speech_Flag',
       'Disability_Hearing_Flag', 'Disability_Sight_Flag',
       'Disability_Learning_Disability_Flag', 'Disability_Count_Number',
       'Segmentation_Bridges_To_Health',
       'segmentation_Bridges_To_Health_Description',
       'All_Long_Term_Condition_Count_Number', 'All_Long_Term_Condition_Count',
       'All_Long_Term_Conditions', 'Patient_Registration_Status', 'frequent_attender',
       'activity_within_12M_of_first_attend']

def to_snake_case_columns(df):
    df.columns = [re.sub(r'[^0-9a-zA-Z]+', '_', col).strip('_').lower() for col in df.columns]
    return df

def clean_attendance_category(df):
    df['attendance_category'] = df['attendance_category'].replace('X',np.nan).astype(float)
    return df

def create_frequent_attender(df):
    df["frequent_attender"] = df["activity_within_12M_of_first_attend"].map(lambda x: 1 if x >= 3 else 0)
    return df

def tt_split(df):
    processed_df = (
        # df.pipe(to_snake_case_columns)
        #.pipe(clean_attendance_category)
        df.pipe(create_frequent_attender)
    )

    train_df, test_df = train_test_split(
        processed_df[cols],
        test_size=0.3,
        stratify=processed_df['frequent_attender'],
        random_state=42
    )

    test_df = test_df.dropna()

    return train_df, test_df