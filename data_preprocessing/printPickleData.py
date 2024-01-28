# Raw data normalised
# import pickle
# import csv

# with open("S2.pkl", "rb") as file:
#     obj = pickle.load(file, encoding="latin1")

# # Extract 'label' and 'ECG' arrays
# label_data = obj['label']
# ecg_data = obj['signal']['chest']['ECG']

# # Combine 'label' and 'ECG' arrays
# combined_data = list(zip(label_data, ecg_data))

# # Save combined data to CSV
# with open("output.csv", "w", newline='') as csvfile:
#     csv.writer(csvfile).writerow(['label', 'ECG'])  # Write header
#     csv.writer(csvfile).writerows(combined_data)

# # Processed data normalised
# import pickle
# import pandas as pd

# with open("S2.pkl", "rb") as file:
#     obj = pickle.load(file, encoding="latin1")

# # Extract 'label' and 'ECG' arrays
# label_data = obj['label']
# ecg_data = obj['signal']['chest']['ECG']

# # Create a DataFrame with 'label' and 'ECG' columns
# df = pd.DataFrame({'label': label_data.flatten(), 'ECG': ecg_data.flatten()})

# # Filter out rows where the label is 1, 5, 6, or 7
# filtered_df = df[~df['label'].isin([0, 5, 6, 7])]

# # Save the filtered DataFrame to CSV
# filtered_df.to_csv("output.csv", index=False)


import pickle
import pandas as pd

with open("S2.pkl", "rb") as file:
    obj = pickle.load(file, encoding="latin1")

# Extract 'label' and 'ECG' arrays
label_data = obj['label']
ecg_data = obj['signal']['chest']['ECG']

# Create a DataFrame with 'label' and 'ECG' columns
df = pd.DataFrame({'label': label_data.flatten(), 'ECG': ecg_data.flatten()})

# Filter out rows where the label is 1, 5, 6, or 7
filtered_df = df[~df['label'].isin([0, 5, 6, 7])].copy()  # Make a copy to avoid SettingWithCopyWarning

# Create a third column based on the modified formula using .loc
filtered_df.loc[:, '16-bit'] = ((filtered_df['ECG'] / 3) + 0.5) * (2 ** 16)

# Save the filtered DataFrame to CSV
filtered_df.to_csv("output.csv", index=False)

