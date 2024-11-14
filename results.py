import pandas as pd

# Load your CSV file
file_path = 'results.csv'  # Update with the path to your result.csv
df = pd.read_csv(file_path)

# Calculate the average of the relevant metrics
average_precision = df['metrics/precision(B)'].mean()
average_recall = df['metrics/recall(B)'].mean()
average_map50 = df['metrics/mAP50(B)'].mean()
average_map50_95 = df['metrics/mAP50-95(B)'].mean()

# Print out the results
print(f"Average Precision: {average_precision:.4f}")
print(f"Average Recall: {average_recall:.4f}")
print(f"Average mAP50: {average_map50:.4f}")
print(f"Average mAP50-95: {average_map50_95:.4f}")
