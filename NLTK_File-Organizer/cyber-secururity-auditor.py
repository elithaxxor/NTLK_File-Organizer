import os
import sys
import re
import csv
import shutil
from datetime import datetime
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from fpdf import FPDF
import magic  # For file type detection
import json


class CybersecurityFileCategorizer:
    """
    A class to categorize files based on their content using machine learning,
    analyze file metadata, and generate reports.
    """

    def __init__(self, categories, training_data, input_directory="./files_to_categorize"):
        """
        Initializes the CybersecurityFileCategorizer with categories, training data, and input directory.

        Args:
            categories (list): List of cybersecurity categories.
            training_data (dict): Dictionary of training data with categories as keys and lists of texts as values.
            input_directory (str): Path to the directory containing files to categorize.
        """
        self.categories = categories
        self.training_data = training_data
        self.input_directory = input_directory
        self.model = self._train_model()
        self.file_metadata = {}  # Dictionary to store file metadata

    def _preprocess_text(self, text):
        """
        Preprocesses text by removing non-alphanumeric characters and converting to lowercase.

        Args:
            text (str): The text to preprocess.

        Returns:
            str: The preprocessed text.
        """
        text = re.sub(r'\W+', ' ', text)  # Remove non-alphanumeric characters
        text = text.lower()  # Convert to lowercase
        return text

    def _train_model(self):
        """
        Trains a machine learning model (TF-IDF + Naive Bayes) on the training data.

        Returns:
            sklearn.pipeline.Pipeline: The trained machine learning model.
        """
        X_train = []
        y_train = []
        for category, texts in self.training_data.items():
            for text in texts:
                X_train.append(self._preprocess_text(text))
                y_train.append(category)

        model = make_pipeline(TfidfVectorizer(), MultinomialNB())
        model.fit(X_train, y_train)
        return model

    def _load_files_from_directory(self):
        """
        Loads text files from the input directory.

        Returns:
            dict: A dictionary where keys are filenames and values are file contents.
        """
        file_contents = {}
        for filename in os.listdir(self.input_directory):
            if filename.endswith(".txt"):
                filepath = os.path.join(self.input_directory, filename)
                with open(filepath, 'r', encoding='utf-8') as file:
                    file_contents[filename] = file.read()
        return file_contents

    def categorize_files(self):
        """
        Categorizes files in the input directory using the trained model.

        Returns:
            dict: A dictionary where keys are filenames and values are predicted categories.
        """
        files = self._load_files_from_directory()
        file_names = list(files.keys())
        file_contents = [self._preprocess_text(content) for content in files.values()]
        predicted_categories = self.model.predict(file_contents)

        results = {}
        for i, filename in enumerate(file_names):
            results[filename] = predicted_categories[i]
        return results

    def save_results_to_csv(self, results, filename="results.csv"):
        """
        Saves the categorization results to a CSV file.

        Args:
            results (dict): Dictionary of filename: category pairs.
            filename (str): Name of the CSV file to save to.
        """
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["File Name", "Category"])
            for filename, category in results.items():
                writer.writerow([filename, category])

    def save_results_to_pdf(self, results, filename=None):
        """
        Saves the categorization results to a PDF file.

        Args:
            results (dict): Dictionary of filename: category pairs.
            filename (str, optional): Name of the PDF file to save to. Defaults to a timestamped filename.
        """
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=15)
        pdf.cell(200, 10, txt="File Categorization Results", ln=True, align='C')
        pdf.ln(10)
        for filename, category in results.items():
            pdf.cell(200, 10, txt=f"{filename}: {category}", ln=True, align='L')

        if filename is None:
            filename = f"results_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.pdf"

        try:
            pdf.output(filename)
        except Exception as e:
            print("Error saving PDF:", e)
            print("Attempting to save PDF again...")
            pdf.output(filename)

    def move_or_copy_files(self, results, action="copy"):
        """
        Moves or copies categorized files to subdirectories based on their predicted categories.

        Args:
            results (dict): Dictionary of filename: category pairs.
            action (str): Either "copy" or "move" to specify the action to perform.
        """
        if action not in ["copy", "move"]:
            raise ValueError("Action must be either 'copy' or 'move'")

        for filename, category in results.items():
            source_path = os.path.join(self.input_directory, filename)
            destination_directory = os.path.join(self.input_directory, category)

            # Create the destination directory if it doesn't exist
            os.makedirs(destination_directory, exist_ok=True)

            destination_path = os.path.join(destination_directory, filename)

            try:
                if action == "copy":
                    shutil.copy2(source_path, destination_path)  # copy2 preserves metadata
                    print(f"Copied '{filename}' to '{category}' directory.")
                elif action == "move":
                    shutil.move(source_path, destination_path)
                    print(f"Moved '{filename}' to '{category}' directory.")
            except Exception as e:
                print(f"Error {action}ing '{filename}': {e}")

    def _extract_metadata(self, filepath):
        """
        Extracts metadata from a file.

        Args:
            filepath (str): Path to the file.

        Returns:
            dict: A dictionary containing file metadata.
        """
        try:
            file_type = magic.from_file(filepath)
            file_size = os.path.getsize(filepath)
            creation_time = os.path.getctime(filepath)
            modification_time = os.path.getmtime(filepath)
            return {
                "file_type": file_type,
                "file_size": file_size,
                "creation_time": datetime.fromtimestamp(creation_time).strftime('%Y-%m-%d %H:%M:%S'),
                "modification_time": datetime.fromtimestamp(modification_time).strftime('%Y-%m-%d %H:%M:%S'),
            }
        except Exception as e:
            print(f"Error extracting metadata from '{filepath}': {e}")
            return {}

    def analyze_files(self):
        """
        Analyzes files in the input directory, extracts metadata, and generates a report.

        Returns:
            dict: A dictionary containing analysis results, including metadata and categorization.
        """
        analysis_results = {}
        categorization_results = self.categorize_files()

        for filename in os.listdir(self.input_directory):
            filepath = os.path.join(self.input_directory, filename)
            if os.path.isfile(filepath):
                metadata = self._extract_metadata(filepath)
                self.file_metadata[filename] = metadata
                analysis_results[filename] = {
                    "metadata": metadata,
                    "category": categorization_results.get(filename, "Unknown"),
                }

        return analysis_results

    def generate_analysis_report(self, analysis_results, report_filename="analysis_report.json"):
        """
        Generates a report of the file analysis and saves it to a JSON file.

        Args:
            analysis_results (dict): The results of the file analysis.
            report_filename (str): The name of the JSON file to save the report to.
        """
        try:
            with open(report_filename, 'w') as f:
                json.dump(analysis_results, f, indent=4)
            print(f"Analysis report saved to '{report_filename}'.")
        except Exception as e:
            print(f"Error generating analysis report: {e}")


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


def main():
    categorizer = CybersecurityFileCategorizer(categories, training_data)

    while True:
        print("\nCybersecurity File Organizer Menu:")
        print("1. Categorize Files")
        print("2. Analyze Files")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            results = categorizer.categorize_files()
            print("\nFile Categorization Results:")
            for filename, category in results.items():
                print(f"{filename}: {category}")

            categorizer.save_results_to_csv(results)
            categorizer.save_results_to_pdf(results)

            # Ask the user if they want to copy or move the files
            while True:
                action = input(
                    "Do you want to (copy) or (move) the files to their respective category folders? (copy/move/no): ").lower()
                if action in ["copy", "move", "no"]:
                    break
                else:
                    print("Invalid input. Please enter 'copy', 'move', or 'no'.")

            if action != "no":
                categorizer.move_or_copy_files(results, action)

        elif choice == '2':
            analysis_results = categorizer.analyze_files()
            print("\nFile Analysis Results:")
            for filename, data in analysis_results.items():
                print(f"\nFilename: {filename}")
                print(f"  Category: {data['category']}")
                print("  Metadata:")
                for key, value in data['metadata'].items():
                    print(f"    {key}: {value}")
            categorizer.generate_analysis_report(analysis_results)

        elif choice == '3':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
