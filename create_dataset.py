import pandas as pd

data = {
    'having_IP_Address': [1, 1, 0, 0, 1],
    'URL_Length': [1, 1, 0, 0, 1],
    'Shortining_Service': [0, 1, 0, 0, 1],
    'having_At_Symbol': [1, 0, 0, 0, 1],
    'double_slash_redirecting': [1, 0, 0, 0, 1],
    'Prefix_Suffix': [1, 0, 0, 0, 1],
    'having_Sub_Domain': [1, 1, 0, 0, 1],
    'SSLfinal_State': [0, 0, 1, 1, 0],
    'Domain_registeration_length': [0, 0, 1, 1, 0],
    'HTTPS_token': [1, 1, 0, 0, 1],
    'is_phishing': [1, 1, 0, 0, 1]
}

df = pd.DataFrame(data)
df.to_csv('phishing_dataset.csv', index=False)
print("Dataset created successfully!")
