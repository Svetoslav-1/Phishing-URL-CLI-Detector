from urllib.parse import urlparse
import re
import tldextract
import numpy as np

def extract_website_features(url):
    """
    Extracts features from a website URL for phishing detection.
    Adapted to match the UCI PhiUSIIL dataset numeric features.
    """
    # Parse the URL
    parsed = urlparse(url)
    extracted = tldextract.extract(url)
    
    # Initialize features dictionary
    features = {}
    
    # Basic URL properties
    domain = extracted.domain + '.' + extracted.suffix if extracted.suffix else extracted.domain
    full_domain = '.'.join(part for part in [extracted.subdomain, extracted.domain, extracted.suffix] if part)
    
    # URLLength - Length of the URL
    features['URLLength'] = len(url)
    
    # DomainLength - Length of the domain
    features['DomainLength'] = len(domain)
    
    # IsDomainIP - If domain is an IP address
    features['IsDomainIP'] = 1 if re.match(r'^\d+\.\d+\.\d+\.\d+$', parsed.netloc) else 0
    
    # TLDLength - Length of the TLD
    features['TLDLength'] = len(extracted.suffix) if extracted.suffix else 0
    
    # NoOfSubDomain - Number of subdomains
    features['NoOfSubDomain'] = len(extracted.subdomain.split('.')) if extracted.subdomain else 0
    
    # HasObfuscation - Check for obfuscation in URL (simplified)
    suspicious_chars = ['@', '-', '_', '%', '=', '+']
    has_obfuscation = any(c in url for c in suspicious_chars)
    features['HasObfuscation'] = 1 if has_obfuscation else 0
    
    # NoOfObfuscatedChar - Count of potentially obfuscated characters
    features['NoOfObfuscatedChar'] = sum(url.count(c) for c in suspicious_chars)
    
    # ObfuscationRatio - Ratio of obfuscated characters
    features['ObfuscationRatio'] = int(features['NoOfObfuscatedChar'] * 100 / len(url)) if len(url) > 0 else 0
    
    # NoOfLettersInURL - Count of letters
    features['NoOfLettersInURL'] = sum(c.isalpha() for c in url)
    
    # LetterRatioInURL - Ratio of letters
    features['LetterRatioInURL'] = features['NoOfLettersInURL'] / len(url) if len(url) > 0 else 0
    
    # NoOfDegitsInURL - Count of digits
    features['NoOfDegitsInURL'] = sum(c.isdigit() for c in url)
    
    # DegitRatioInURL - Ratio of digits
    features['DegitRatioInURL'] = int(features['NoOfDegitsInURL'] * 100 / len(url)) if len(url) > 0 else 0
    
    # Special character counts
    features['NoOfEqualsInURL'] = url.count('=')
    features['NoOfQMarkInURL'] = url.count('?')
    features['NoOfAmpersandInURL'] = url.count('&')
    
    # NoOfOtherSpecialCharsInURL - Count of other special characters
    special_chars = '!@#$%^&*()_+-=[]{}|;:\'",.<>/?`~'
    features['NoOfOtherSpecialCharsInURL'] = sum(url.count(c) for c in special_chars)
    
    # SpacialCharRatioInURL - Ratio of special characters
    special_char_count = sum(c in special_chars for c in url)
    features['SpacialCharRatioInURL'] = special_char_count / len(url) if len(url) > 0 else 0
    
    # IsHTTPS - If URL uses HTTPS
    features['IsHTTPS'] = 1 if parsed.scheme == 'https' else 0
    
    # These features would normally require analyzing the webpage content
    # We provide default values here
    features['LineOfCode'] = 0
    features['LargestLineLength'] = 0
    features['HasTitle'] = 0
    features['DomainTitleMatchScore'] = 0
    features['URLTitleMatchScore'] = 0
    features['HasFavicon'] = 0
    features['Robots'] = 0
    features['IsResponsive'] = 0
    features['NoOfURLRedirect'] = 0
    features['NoOfSelfRedirect'] = 0
    features['HasDescription'] = 0
    features['NoOfPopup'] = 0
    features['NoOfiFrame'] = 0
    features['HasExternalFormSubmit'] = 0
    features['HasSocialNet'] = 0
    features['HasSubmitButton'] = 0
    features['HasHiddenFields'] = 0
    features['HasPasswordField'] = 0
    
    # Content type indicators
    features['Bank'] = 1 if any(word in url.lower() for word in ['bank', 'banking', 'account', 'secure']) else 0
    features['Pay'] = 1 if any(word in url.lower() for word in ['pay', 'payment', 'checkout', 'wallet']) else 0
    features['Crypto'] = 1 if any(word in url.lower() for word in ['crypto', 'bitcoin', 'wallet', 'token']) else 0
    
    # Page element counts (defaults)
    features['HasCopyrightInfo'] = 0
    features['NoOfImage'] = 0
    features['NoOfCSS'] = 0
    features['NoOfJS'] = 0
    features['NoOfSelfRef'] = 0
    features['NoOfEmptyRef'] = 0
    features['NoOfExternalRef'] = 0
    
    # URLSimilarityIndex - simplified
    features['URLSimilarityIndex'] = 0
    
    # CharContinuationRate - simplified check for repeated characters
    char_count = {}
    max_repeat = 0
    for c in url:
        if c in char_count:
            char_count[c] += 1
            max_repeat = max(max_repeat, char_count[c])
        else:
            char_count[c] = 1
    features['CharContinuationRate'] = max_repeat
    
    # TLDLegitimateProb - assign a probability based on common TLDs
    common_tlds = ['com', 'org', 'net', 'edu', 'gov', 'info']
    features['TLDLegitimateProb'] = 0.9 if extracted.suffix in common_tlds else 0.3
    
    # URLCharProb - simplified
    features['URLCharProb'] = 0.5  # Default value
    
    return features
