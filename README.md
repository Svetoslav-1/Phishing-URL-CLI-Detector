

# 🛡️ Phishing URL Detector - (UNDER DEVELOPMENT - kinda broken)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.0.2+-orange.svg)](https://scikit-learn.org/)

A machine learning powered command-line tool to identify phishing URLs based on their characteristics.


## 🌟 Overview

This project is a command-line tool that uses machine learning to classify URLs as legitimate or phishing attempts. It leverages the PhiUSIIL Phishing URL Dataset from the UCI Machine Learning Repository to train a Random Forest classifier that analyzes URL characteristics.

## ✨ Features

- 🔍 Advanced URL feature extraction for phishing detection
- 🤖 Machine learning classification using Random Forest algorithm
- 💻 Simple command-line interface for easy URL checking
- 📊 Detailed output mode showing feature importance
- 🎯 High-accuracy detection of phishing URLs based on URL structure alone

## 🚀 Installation

### Prerequisites
- Python 3.9+
- pip package manager

### Setup
1. Clone the repository:
```bash
git clone https://github.com/Svetoslav-1/phishing-detector.git
cd phishing-detector
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## 📋 Usage

### Training the Model
The model needs to be trained before it can classify URLs:
```bash
python train_model.py
```

This will:
- Fetch the PhiUSIIL dataset from UCI repository
- Extract URL-based features
- Train a Random Forest classifier
- Save the model to `phishing_model.pkl`

### Analyzing URLs
To analyze a URL and determine if it's a phishing attempt:
```bash
python detect_phish.py https://example.com
```

For detailed information about the features and their importance:
```bash
python detect_phish.py https://example.com --verbose
```

## 📈 Performance

The model achieves high accuracy in detecting phishing URLs by analyzing patterns typical of malicious sites, including:

- Unusual domain name patterns
- Excessive subdomain usage
- Character distribution anomalies
- Suspicious URL patterns

## 📁 Project Structure

```
phishing-detector/
├── detect_phish.py        # CLI tool for analyzing URLs
├── train_model.py         # Fetches dataset and trains the classifier  
├── requirements.txt       # Project dependencies
├── LICENSE                # MIT License
├── README.md              # This file
├── src/
│   ├── __init__.py        # Package initialization
│   └── utils.py           # URL feature extraction utilities
└── models/                # Directory for trained models
    └── phishing_model.pkl # Trained model (generated after training)
```

## 📊 Dataset

The project uses the PhiUSIIL Phishing URL Dataset from the UCI Machine Learning Repository, containing:
- 134,850 legitimate URLs
- 100,945 phishing URLs 

The dataset features are extracted from both the URL structure and webpage characteristics.

## 🔍 Features Analyzed

The system analyzes multiple URL characteristics including:
- URL and domain length
- Presence of IP addresses in domain
- TLD legitimacy
- Character distribution (letters, digits, special characters)
- Subdomain properties
- SSL/HTTPS usage
- Character repetition patterns

## 📜 License

MIT License

Copyright (c) 2025 Svetoslasa-1

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## 🙏 Acknowledgments

- PhiUSIIL dataset creators: Arvind Prasad and Shalini Chandra
- UCI Machine Learning Repository
- The scikit-learn team

## 🔮 Future Improvements

- Web interface for easier access
- Integration with browser extensions
- Real-time analysis of webpage content
- Periodic model retraining with new phishing examples
- API for integration with other security tools
