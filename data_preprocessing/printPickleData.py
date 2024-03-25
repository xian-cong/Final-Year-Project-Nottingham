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

#########################################################################

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

#########################################################################

# # create 16-bit data
# import pickle
# import pandas as pd

# with open("data_preprocessing\\S2.pkl", "rb") as file:
#     obj = pickle.load(file, encoding="latin1")

# # Extract 'label' and 'ECG' arrays
# label_data = obj['label']
# ecg_data = obj['signal']['chest']['ECG']

# # Create a DataFrame with 'label' and 'ECG' columns
# df = pd.DataFrame({'label': label_data.flatten(), 'ECG': ecg_data.flatten()})

# # Filter out rows where the label is 1, 5, 6, or 7
# filtered_df = df[~df['label'].isin([0, 5, 6, 7])].copy()  # Make a copy to avoid SettingWithCopyWarning

# # Create a third column based on the modified formula using .loc
# filtered_df.loc[:, '16-bit'] = ((filtered_df['ECG'] / 3) + 0.5) * (2 ** 16)

# # Save the filtered DataFrame to CSV
# filtered_df.to_csv("data_preprocessing\\output_1.csv", index=False)

###########################################################################
# # make label on the right side of each row
# import pickle
# import pandas as pd
# import numpy as np

# # Load data from the pickle file
# with open("data_preprocessing\\S2.pkl", "rb") as file:
#     obj = pickle.load(file, encoding="latin1")

# # Extract 'label' and 'ECG' arrays
# label_data = obj['label']
# ecg_data = obj['signal']['chest']['ECG']

# # Create a DataFrame with 'label' and 'ECG' columns
# df = pd.DataFrame({'label': label_data.flatten(), 'ECG': ecg_data.flatten()})

# # Filter out rows where the label is 1, 5, 6, or 7
# filtered_df = df[~df['label'].isin([0, 5, 6, 7])].copy()  # Make a copy to avoid SettingWithCopyWarning

# # Create a '16-bit' column based on the modified formula using .loc
# filtered_df.loc[:, '16-bit'] = ((filtered_df['ECG'] / 3) + 0.5) * (2 ** 16)

# # Reshape 'label' and '16-bit' arrays to have the same number of rows
# num_rows = len(filtered_df) // 7000 * 7000
# label_data = filtered_df['label'][:num_rows].values.reshape((-1, 7000))
# bit16_data = filtered_df['16-bit'][:num_rows].values.reshape((-1, 7000))

# # Create a DataFrame with transposed '16-bit' data
# final_df = pd.DataFrame(np.hstack((bit16_data, label_data[:, 0].reshape(-1, 1))), columns=[f'data{i+1}' for i in range(7000)] + ['label'])

# # Save the final DataFrame to CSV
# final_df.to_csv("data_preprocessing\\output.csv", index=False)

###########################################################################
# # discard row with different label in a row data (WITH FIRST ROW LABEL) (4 classes)
# import pickle
# import pandas as pd
# import numpy as np

# # Load data from the pickle file
# with open("data_preprocessing\\pkl_data\\S17.pkl", "rb") as file:
#     obj = pickle.load(file, encoding="latin1")

# # Extract 'label' and 'ECG' arrays
# label_data = obj['label']
# ecg_data = obj['signal']['chest']['ECG']

# # Create a DataFrame with 'label' and 'ECG' columns
# df = pd.DataFrame({'label': label_data.flatten(), 'ECG': ecg_data.flatten()})

# # Filter out rows where the label is 1, 5, 6, or 7
# filtered_df = df[~df['label'].isin([0, 5, 6, 7])].copy()  # Make a copy to avoid SettingWithCopyWarning

# # Create a '16-bit' column based on the modified formula using .loc
# filtered_df.loc[:, '16-bit'] = ((filtered_df['ECG'] / 3) + 0.5) * (2 ** 16)

# # Reshape 'label' and '16-bit' arrays to have the same number of rows
# num_rows = len(filtered_df) // 7000 * 7000
# label_data = filtered_df['label'][:num_rows].values.reshape((-1, 7000))
# bit16_data = filtered_df['16-bit'][:num_rows].values.reshape((-1, 7000))

# # Identify rows where labels differ within the 7000 readings and discard those rows
# valid_rows_mask = (label_data == label_data[:, [0]]).all(axis=1)
# label_data = label_data[valid_rows_mask]
# bit16_data = bit16_data[valid_rows_mask]

# # Create a DataFrame with transposed '16-bit' data
# final_df = pd.DataFrame(np.hstack((bit16_data, label_data[:, 0].reshape(-1, 1))), columns=[f'data{i+1}' for i in range(7000)] + ['label'])

# # Save the final DataFrame to CSV
# final_df.to_csv("data_preprocessing\\output_filter_label\\output_S17.csv", index=False)

###########################################################################
# transpose csv file (for testing in STM Cube IDE)
# import pandas as pd

# def transpose_csv(input_file, output_file):
#     df = pd.read_csv(input_file)
#     df_transposed = df.transpose()
#     df_transposed.to_csv(output_file, header=False)

# # Example usage
# input_file_path = 'data_preprocessing\\output_filter_label\\test_output.csv'  # Replace with your input file path
# output_file_path = 'data_preprocessing\\output_filter_label\\test_output_transposed.csv'  # Replace with your desired output file path

# transpose_csv(input_file_path, output_file_path)

###########################################################################
# # # discard row with different label in a row data (WITH FIRST ROW LABEL) (2 classes) (stress/non-stress)
import pickle
import pandas as pd
import numpy as np

# Load data from the pickle file
with open("data_preprocessing\\pkl_data\\S2.pkl", "rb") as file:
    obj = pickle.load(file, encoding="latin1")

# Extract 'label' and 'ECG' arrays
label_data = obj['label']
ecg_data = obj['signal']['chest']['ECG']

# Create a DataFrame with 'label' and 'ECG' columns
df = pd.DataFrame({'label': label_data.flatten(), 'ECG': ecg_data.flatten()})

# Filter out rows where the label is 1, 5, 6, or 7
filtered_df = df[~df['label'].isin([0, 3, 4, 5, 6, 7])].copy()  # Make a copy to avoid SettingWithCopyWarning

# Create a '16-bit' column based on the modified formula using .loc
filtered_df.loc[:, '16-bit'] = ((filtered_df['ECG'] / 3) + 0.5) * (2 ** 16)

# Reshape 'label' and '16-bit' arrays to have the same number of rows
num_rows = len(filtered_df) // 500 * 500
label_data = filtered_df['label'][:num_rows].values.reshape((-1, 500))
bit16_data = filtered_df['16-bit'][:num_rows].values.reshape((-1, 500))

# Identify rows where labels differ within the 7000 readings and discard those rows
valid_rows_mask = (label_data == label_data[:, [0]]).all(axis=1)
label_data = label_data[valid_rows_mask]
bit16_data = bit16_data[valid_rows_mask]

# Create a DataFrame with transposed '16-bit' data
final_df = pd.DataFrame(np.hstack((bit16_data, label_data[:, 0].reshape(-1, 1))), columns=[f'data{i+1}' for i in range(500)] + ['label'])

# Save the final DataFrame to CSV
final_df.to_csv("data_preprocessing\\output_filter_label\\output_S2_2class_500in.csv", index=False)