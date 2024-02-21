import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.metrics import accuracy_score
import joblib

# Load your dataset
df = pd.read_csv('anthr.csv')

# Split the dataset into training and testing sets
train_data, test_data, train_labels, test_labels = train_test_split(df['symptoms'], df['recommendation'], test_size=0.2, random_state=42)

# Create a text classification pipeline
model = make_pipeline(TfidfVectorizer(), MultinomialNB())

# Train the model
model.fit(train_data, train_labels)

# Make predictions on the test set
predictions = model.predict(test_data)

# Evaluate and check  the accuracy of the model
accuracy = accuracy_score(test_labels, predictions)
print(f'Model Accuracy: {accuracy}')

# Save the trained model to a file(recomendation_model.joblib)
joblib.dump(model, 'recommendation_model.joblib')
