# Phishing URL Detector
Overview
This project is a command-line tool that uses machine learning to classify URLs as legitimate or phishing attempts. It leverages the PhiUSIIL Phishing URL Dataset from the UCI Machine Learning Repository to train a Random Forest classifier that analyzes URL characteristics.
Features

URL feature extraction for phishing detection
Machine learning classification using Random Forest algorithm
Command-line interface for easy URL checking
Detailed output mode showing feature importance
High-accuracy detection of phishing URLs based on URL structure alone

Installation
Prerequisites

Python 3.9+
pip package manager

Setup

Clone the repository:

bashgit clone https://github.com/yourusername/phishing-detector.git
cd phishing-detector

Create and activate a virtual environment:

bashpython -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

Install dependencies:

bashpip install -r requirements.txt
Usage
Training the Model
The model needs to be trained before it can classify URLs:
bashpython train_model.py
This will:

Fetch the PhiUSIIL dataset from UCI repository
Extract URL-based features
Train a Random Forest classifier
Save the model to phishing_model.pkl

Analyzing URLs
To analyze a URL and determine if it's a phishing attempt:
bashpython detect_phish.py https://example.com
For detailed information about the features and their importance:
bashpython detect_phish.py https://example.com --verbose
Project Structure

train_model.py: Fetches dataset and trains the classifier
detect_phish.py: CLI tool for analyzing URLs
src/utils.py: URL feature extraction utilities
src/__init__.py: Package initialization file
requirements.txt: Project dependencies
phishing_model.pkl: Trained model (generated after training)

Dataset
The project uses the PhiUSIIL Phishing URL Dataset from UCI, containing 134,850 legitimate and 100,945 phishing URLs. The dataset features are extracted from both the URL structure and webpage characteristics.
Features Analyzed
The system analyzes multiple URL characteristics including:

URL and domain length
Presence of IP addresses
TLD legitimacy
Character distribution (letters, digits, special characters)
Subdomain properties
SSL/HTTPS usage
Character repetition patterns

License
[Add your license here]
Acknowledgments

PhiUSIIL dataset creators: Arvind Prasad and Shalini Chandra
UCI Machine Learning Repository

Future Improvements

Web interface for easier access
Integration with browser extensions
Real-time analysis of webpage content
Periodic model retraining with new phishing examples

