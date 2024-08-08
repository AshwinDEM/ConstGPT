from datasets import load_dataset
import pandas as pd

# Load the SciQ dataset
dataset = load_dataset("SciQ")

# Explore the 'train' split
print(dataset['train'][0])

# Convert the dataset to a pandas DataFrame, excluding the distractors
train_df = pd.DataFrame(dataset['train'])
validation_df = pd.DataFrame(dataset['validation'])
test_df = pd.DataFrame(dataset['test'])

# Select only the relevant columns
train_df = train_df[['question', 'correct_answer', 'support']]
validation_df = validation_df[['question', 'correct_answer', 'support']]
test_df = test_df[['question', 'correct_answer', 'support']]

# Save the preprocessed data to CSV files (optional)
train_df.to_csv('sciq_train.csv', index=False)
validation_df.to_csv('sciq_validation.csv', index=False)
test_df.to_csv('sciq_test.csv', index=False)

print("Train data example:\n", train_df.head())
print("Validation data example:\n", validation_df.head())
print("Test data example:\n", test_df.head())
