#!/usr/bin/env python3
import joblib
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
from ucimlrepo import fetch_ucirepo

def train_model():
    # Fetch dataset from UCI repository
    print("Fetching phishing URL dataset from UCI repository...")
    try:
        phishing_website = fetch_ucirepo(id=967)
        
        # Get features and target data
        X = phishing_website.data.features
        y = phishing_website.data.targets
        
        # Define URL-based features we can reliably extract
        url_features = [
            'URLLength', 'DomainLength', 'IsDomainIP', 'TLDLength', 'NoOfSubDomain', 
            'HasObfuscation', 'NoOfObfuscatedChar', 'ObfuscationRatio', 
            'NoOfLettersInURL', 'LetterRatioInURL', 'NoOfDegitsInURL', 'DegitRatioInURL',
            'NoOfEqualsInURL', 'NoOfQMarkInURL', 'NoOfAmpersandInURL',
            'NoOfOtherSpecialCharsInURL', 'SpacialCharRatioInURL', 'IsHTTPS',
            'CharContinuationRate'
        ]
        
        # Keep only URL-based features we can actually extract
        url_features_available = [col for col in url_features if col in X.columns]
        print(f"\nUsing these URL-based features: {url_features_available}")
        
        # Filter to keep only numeric columns from our list
        X_filtered = X[url_features_available].copy()
        
        # Convert any problematic columns to numeric
        for col in X_filtered.columns:
            if X_filtered[col].dtype == 'object':
                X_filtered[col] = pd.to_numeric(X_filtered[col], errors='coerce')
        
        # Drop any columns with NaN values
        X_filtered = X_filtered.dropna(axis=1)
        
        print(f"\nFinal features used for training: {list(X_filtered.columns)}")
        
        # Use this filtered feature set
        X = X_filtered
        
    except Exception as e:
        print(f"Error processing UCI dataset: {e}")
        print("Falling back to sample dataset...")
        # Create a sample dataset as fallback
        data = {
            'URLLength': [54, 75, 12, 18, 120, 20, 40],
            'DomainLength': [15, 20, 10, 8, 25, 12, 18],
            'IsHTTPS': [0, 0, 1, 1, 0, 1, 1],
            'NoOfSubDomain': [3, 2, 0, 0, 4, 1, 1],
            'HasObfuscation': [1, 1, 0, 0, 1, 0, 0],
            'NoOfDegitsInURL': [20, 15, 0, 2, 30, 4, 5],
            'DegitRatioInURL': [37, 20, 0, 11, 25, 20, 12],
            'SpacialCharRatioInURL': [0.2, 0.15, 0.05, 0.1, 0.3, 0.05, 0.07],
            'is_phishing': [1, 1, 0, 0, 1, 0, 0]
        }
        df = pd.DataFrame(data)
        X = df.drop('is_phishing', axis=1)
        y = df['is_phishing']
    
    # Print dataset information
    print(f"\nDataset shape: {X.shape}")
    print(f"Number of features: {X.shape[1]}")
    print(f"Number of samples: {X.shape[0]}")
    
    if isinstance(y, pd.DataFrame):
        y_values = y.values.ravel()  # Convert DataFrame to 1D array
    else:
        y_values = y
        
    print(f"Number of phishing websites: {sum(y_values)}")
    print(f"Number of legitimate websites: {len(y_values) - sum(y_values)}")
    
    # Take a sample of the data if it's too large
    if X.shape[0] > 20000:
        print(f"\nSampling 20,000 records from the dataset for balanced training...")
        # Get equal numbers of phishing and legitimate samples
        phish_indices = np.where(y_values == 1)[0]
        legit_indices = np.where(y_values == 0)[0]
        
        sample_size = min(10000, len(phish_indices), len(legit_indices))
        phish_sample = np.random.choice(phish_indices, sample_size, replace=False)
        legit_sample = np.random.choice(legit_indices, sample_size, replace=False)
        
        sample_indices = np.concatenate([phish_sample, legit_sample])
        X_sampled = X.iloc[sample_indices]
        y_sampled = y_values[sample_indices]
    else:
        X_sampled = X
        y_sampled = y_values
    
    # Split into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(
        X_sampled, y_sampled, test_size=0.2, random_state=42
    )
    
    # Train a Random Forest model with more trees and deeper
    print("\nTraining Random Forest classifier...")
    model = RandomForestClassifier(n_estimators=200, max_depth=20, random_state=42)
    model.fit(X_train, y_train)
    
    # Evaluate the model
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Model accuracy: {accuracy:.2%}")
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))
    
    # Save feature names with the model for later use
    model.feature_names = list(X.columns)
    
    # Find the most important features
    feature_importances = model.feature_importances_
    features_df = pd.DataFrame({
        'Feature': model.feature_names,
        'Importance': feature_importances
    }).sort_values('Importance', ascending=False)
    
    print("\nFeature importance:")
    print(features_df)
    
    # Save the model
    model_path = 'phishing_model.pkl'
    joblib.dump(model, model_path)
    print(f"\nModel saved to {model_path}")
    
    return model

if __name__ == "__main__":
    train_model()
