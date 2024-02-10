
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def load_data(file_path):
    """Load data from a CSV file."""
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}. Please provide a valid file path.")
        return None
    except Exception as e:
        print(f"Error: An error occurred during data loading: {e}")
        return None

def clean_text(text):
    """Clean the text data."""
    # For simplicity, we'll just convert text to lowercase
    text = text.lower()
    return text

def main():
    print("\n")
    print("Welcome to my Phishing Email Detection Program!")
    print("\n")
    print("--Importent Message From Author Bhanu--""\n(Before you using the programme make sure you have phishing email data set to prepare machine learning model.)")
    print("\n")
    print("Programme is running it will take time to load Please Wait")
    print("\n")

    # Load email data from the specified file
    file_path = "/home/bhanu/Desktop/email_data.csv"
    emails = load_data(file_path)
    if emails is None:
        return

    # Preprocess email text
    emails['text'] = emails['text'].apply(clean_text)

    # Split the data into features (email text) and labels
    X = emails['text']
    y = emails['label']

    # Vectorize the email text using Bag-of-Words representation
    vectorizer = CountVectorizer()
    X_vec = vectorizer.fit_transform(X)

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X_vec, y, test_size=0.2, random_state=42)

    # Train a Logistic Regression model
    model = LogisticRegression()
    model.fit(X_train, y_train)

    # Evaluate model
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Model Accuracy: {accuracy:.2f}")
    
    # User input to specify how many emails to check for phishing
    num_emails = input("Enter the number of email texts you want to check for phishing : ")
    try:
        num_emails = int(num_emails)
        if num_emails <= 0:
            raise ValueError("Number of emails must be a positive integer.")
    except ValueError as ve:
        print(f"Error: {ve}")
        return

    # Loop to check each email for phishing
    for i in range(num_emails):
        print("\nPlease copy suspisious email text and add below")
        user_input = input(f"Enter email text {i + 1}: ")
        # Clean and vectorize user input
        user_input_vec = vectorizer.transform([clean_text(user_input)])

        # Make prediction
        prediction = model.predict(user_input_vec)

        # Display prediction
        if prediction[0] == 1:
            print("Phishing Email Detected!")
        else:
            print("Normal Email")

if __name__ == "__main__":
    main()
