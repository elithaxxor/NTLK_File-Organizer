import os
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline



"""  script tailored to categorize files based on cybersecurity tools into the specified categori """

# Define cybersecurity categories and example training data
categories = ["Scanner", "Exploitation", "Web_Tools", "Password_Cracking", "Sniffing", "Other"]

training_data = {
    "Scanner": [
        "Nmap is a network scanning tool used for discovering hosts and services.",
        "Masscan performs fast port scanning across large networks."
    ],
    "Exploitation": [
        "Metasploit is a framework for developing and executing exploits.",
        "Various exploits target vulnerabilities in systems and applications."
    ],
    "Web_Tools": [
        "Burp Suite is used for web application security testing.",
        "DirBuster helps find hidden directories and files on web servers."
    ],
    "Password_Cracking": [
        "Hydra is a tool for brute-force password cracking.",
        "John the Ripper cracks passwords using dictionary attacks."
    ],
    "Sniffing": [
        "Wireshark analyzes network traffic by capturing packets.",
        "Tcpdump is a command-line tool for packet analysis."
    ],
    "Other": [
        "This file does not match any specific category of cybersecurity tools."
    ]
}

# Function to preprocess text (basic cleaning)
def preprocess_text(text):
    text = re.sub(r'\W+', ' ', text)  # Remove non-alphanumeric characters
    text = text.lower()  # Convert to lowercase
    return text

# Prepare training data for machine learning
X_train = []
y_train = []
for category, texts in training_data.items():
    for text in texts:
        X_train.append(preprocess_text(text))
        y_train.append(category)

# Train a simple classifier (TF-IDF + Naive Bayes)
model = make_pipeline(TfidfVectorizer(), MultinomialNB())
model.fit(X_train, y_train)

# Directory containing files to categorize
input_directory = "./files_to_categorize"  # Replace with your directory path

# Function to load files from a directory
def load_files_from_directory(directory):
    file_contents = {}
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r', encoding='utf-8') as file:
                file_contents[filename] = file.read()
    return file_contents

# Load and preprocess files from the directory
files = load_files_from_directory(input_directory)
file_names = list(files.keys())
file_contents = [preprocess_text(content) for content in files.values()]

# Predict categories for the files
predicted_categories = model.predict(file_contents)

# Display results
print("File Categorization Results:")
for i, filename in enumerate(file_names):
    print(f"{filename}: {predicted_categories[i]}")

# Save results to a text file
output_file = "categorized_files.txt"
with open(output_file, 'w') as file:
    for i, filename in enumerate(file_names):
        file.write(f"{filename}: {predicted_categories[i]}\n")

print(f"\nResults saved to '{output_file}'")