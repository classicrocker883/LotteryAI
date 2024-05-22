import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier

# Load the data
#filename = 'powerball.csv'
filename = 'megamillions.csv'
data = pd.read_csv(filename)

# Assume 'Num1', 'Num2', 'Num3', 'Num4', 'Num5', 'NumS' are columns in the CSV file.
columns = ['Num1', 'Num2', 'Num3', 'Num4', 'Num5', 'NumS']

# MegaMillions
max_white = 70
max_red = 25
# Powerball
#max_white = 69
#max_red = 26

# Initialize weights for numbers 1-69/70 for Num1-Num5 and 1-26/25 for NumS
weights = np.ones(max_white+1)  # Initialize all weights to 1
weights_s = np.ones(max_red+1)

def update_weights(row):
    for col in columns[:-1]:  # Update weights for Num1-Num5
        num = row[col]
        if 1 <= num <= max_white:  # Check if the number is within the expected range
            weights[num] += 1
    num_s = row['NumS']
    if 1 <= num_s <= max_red:  # Update weight for NumS
        weights_s[num_s] += 1

# Number of rows in data
set_rows = 200

# Apply weights based on recent draws
for index, row in data.iloc[-set_rows:].iterrows():
    update_weights(row)

probabilities = 1 / weights
probabilities_s = 1 / weights_s

# Normalize probabilities
total_prob = probabilities.sum()
total_prob_s = probabilities_s.sum()
probabilities /= total_prob
probabilities_s /= total_prob_s

# Create feature set and target variable
X = data[columns].iloc[:-1]  # All rows except the last one
y = data[columns].iloc[1:]   # All rows shifted up by one (next draw)

# Train a simple RandomForestClassifier (this is just an example, you might need a different approach)
clf = RandomForestClassifier(n_estimators=100)
clf.fit(X, y)

# Predict the next draw
next_draw_probabilities = []
for i in range(5):
    next_draw_probabilities.append(np.argmax(probabilities[1:]) + 1)  # Add 1 to index to account for 1-based numbering
    probabilities[next_draw_probabilities[-1]] = 0  # Remove the selected number from probabilities

next_draw_s = np.argmax(probabilities_s[1:]) + 1  # Add 1 to index to account for 1-based numbering

print("Predicted next draw numbers:", next_draw_probabilities, "Special number:", next_draw_s)
