# data_utils.py
import pandas as pd

def analyze_chat_data(file_path):
    """Analyze stored chat data for insights."""
    df = pd.read_csv(file_path)
    print("📊 Chat Data Overview:")
    print(df.head())
    print("\nConversation Stats:")
    print(df['message'].value_counts().head())
    return df
