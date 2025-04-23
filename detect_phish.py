#!/usr/bin/env python3
import argparse
import joblib
from src.utils import extract_website_features

def main():
    # Set up command line argument parsing
    parser = argparse.ArgumentParser(description='Detect phishing websites')
    parser.add_argument('url', help='URL to analyze')
    parser.add_argument('--model', default='phishing_model.pkl', 
                        help='Path to the trained model')
    parser.add_argument('--verbose', '-v', action='store_true',
                        help='Show detailed feature information')
    args = parser.parse_args()
    
    # Load the trained model
    try:
        model = joblib.load(args.model)
    except Exception as e:
        print(f"Error loading model: {e}")
        print("Please run train_model.py first to generate the model.")
        return 1
    
    # Extract features from the URL
    print(f"Analyzing URL: {args.url}")
    features = extract_website_features(args.url)
    
    # Ensure features match the expected format
    feature_vector = []
    for feature in model.feature_names:
        feature_vector.append(features.get(feature, 0))
    
    # Make prediction
    prediction = model.predict([feature_vector])[0]
    probability = model.predict_proba([feature_vector])[0][1]  # Probability of being phishing
    
    # Print result
    result = "Phishing" if prediction == 1 else "Legitimate"
    print(f"\nClassification: {result}")
    print(f"Confidence: {probability:.2%}")
    
    # Show feature details if verbose mode
    if args.verbose:
        print("\nFeature Details:")
        for name, value in zip(model.feature_names, feature_vector):
            print(f"  {name}: {value}")
        
        print("\nFeature Importance:")
        importance_dict = dict(zip(model.feature_names, model.feature_importances_))
        sorted_importance = sorted(importance_dict.items(), key=lambda x: x[1], reverse=True)
        for name, importance in sorted_importance:
            print(f"  {name}: {importance:.4f}")
    
    return 0

if __name__ == "__main__":
    exit(main())
