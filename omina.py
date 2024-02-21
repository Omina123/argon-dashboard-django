# train_model.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
import joblib

# Load your dataset
df = pd.read_csv('recom_data.csv')

# Split the dataset into training and testing sets
train_data, test_data, train_labels, test_labels = train_test_split(df[['symptoms', 'diagnosis']], df['recommendation'], test_size=0.2, random_state=42)

# Create a text classification pipeline
model = make_pipeline(TfidfVectorizer(min_df=1, stop_words='english'), MultinomialNB(alpha=0.1))  # Fine-tune parameters

# Train the model
model.fit(train_data['symptoms'], train_labels)  # Use 'symptoms' as the input feature

# Save the trained model to a file
joblib.dump(model, 'omina_model.joblib')

# Evaluate the Confusion Matrix
from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

# Make predictions on the test set
predictions = model.predict(test_data['symptoms'])  # Use 'symptoms' as the input feature

# Create a confusion matrix
conf_matrix = confusion_matrix(test_labels, predictions)

# Plot the confusion matrix
plt.figure(figsize=(8, 6))
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', xticklabels=['0', '1'], yticklabels=['0', '1'])
plt.xlabel('Predicted')
plt.ylabel('True')
plt.title('Confusion Matrix')
plt.show()
