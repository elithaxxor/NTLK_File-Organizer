import os, sys, re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

# Define cybersecurity categories and expanded training data
categories = [
    "Scanner", 
    "Exploitation", 
    "Web_Tools", 
    "Password_Cracking", 
    "Sniffing", 
    "Encryption", 
    "Network_Defense", 
    "Other"
]

training_data = {
    "Scanner": [
        "Nmap is a network scanning tool used for discovering hosts and services.",
        "Masscan performs fast port scanning across large networks.",
        "Shodan scans and indexes devices connected to the internet.",
        "TheHarvester gathers information about domains and emails."
    ],
    "Exploitation": [
        "Metasploit is a framework for developing and executing exploits.",
        "SQLMap automates SQL injection attacks.",
        "Cobalt Strike is used for post-exploitation activities.",
        "Empire specializes in exploitation and lateral movement."
    ],
    "Web_Tools": [
        "Burp Suite is used for web application security testing.",
        "Nikto scans web servers for vulnerabilities.",
        "OWASP ZAP helps identify security issues in web applications.",
        "WPScan scans WordPress sites for vulnerabilities."
    ],
    "Password_Cracking": [
        "Hydra is a tool for brute-force password cracking.",
        "John the Ripper cracks passwords using dictionary attacks.",
        "Hashcat is a high-performance password recovery tool.",
        "Cain & Abel recovers passwords using cryptanalysis."
    ],
    "Sniffing": [
        "Wireshark analyzes network traffic by capturing packets.",
        "Tcpdump is a command-line tool for packet analysis.",
        "Kismet detects wireless networks and captures packets.",
        "Aircrack-ng cracks WEP and WPA keys from captured packets."
    ],
    "Encryption": [
        "VeraCrypt encrypts files and drives securely.",
        "AxCrypt provides simple file encryption.",
        "Tor ensures anonymity through encrypted traffic routing.",
        "NordLocker encrypts files for secure storage."
    ],
    "Network_Defense": [
        "Snort detects intrusions in network traffic.",
        "Suricata provides real-time intrusion detection and prevention.",
        "pfSense secures networks with firewall capabilities.",
        "AlienVault OSSIM combines SIEM and network monitoring."
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
