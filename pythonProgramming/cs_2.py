# Task 1: Change the names of numeric variables in car_crashes data to upper case and add NUM at the beginning.
import seaborn as sns
df = sns.load_dataset("car_crashes")
df.columns
comp = new_columns = ["NUM_" + column.upper() if df[column].dtype.kind in 'fi' else column.upper() for column in df.columns]
# 'i': Tam sayı (integer), 'f': Ondalık sayı (float)
print(comp) # ['NUM_TOTAL', 'NUM_SPEEDING', 'NUM_ALCOHOL', 'NUM_NOT_DISTRACTED', 'NUM_NO_PREVIOUS', 'NUM_INS_PREMIUM', 'NUM_INS_LOSSES', 'ABBREV']


# Task 2: In car_crashes data, write "FLAG" at the end of the names of variables that do not contain "no" in their names.
import seaborn as sns
df = sns.load_dataset("car_crashes")
df.columns
comp = new_columns = [column.upper() + "_FLAG" if not "no" in column else column.upper() for column in df.columns]
print(comp) # ['TOTAL_FLAG', 'SPEEDING_FLAG', 'ALCOHOL_FLAG', 'NOT_DISTRACTED', 'NO_PREVIOUS', 'INS_PREMIUM_FLAG', 'INS_LOSSES_FLAG', 'ABBREV_FLAG']


# Task 3: Select the names of the variables that are DIFFERENT from the variable names in the "org_list" list and create a new dataframe.
import seaborn as sns
df = sns.load_dataset("car_crashes")
df.columns

og_list = ["abbrev", "no_previous"]
new_cols = [column for column in df.columns if not column in og_list]

new_df = df[new_cols]
print(new_cols)
print(new_df)