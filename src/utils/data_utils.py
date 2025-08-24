def load_dataset(file_path):
    import pandas as pd
    
    # Load the dataset from a CSV file
    data = pd.read_csv(file_path)
    return data

def preprocess_data(data):
    # Perform any necessary preprocessing steps
    # For example, removing null values and normalizing text
    data = data.dropna()
    data['text'] = data['text'].str.lower()  # Example normalization
    return data

def split_data(data, train_size=0.8):
    from sklearn.model_selection import train_test_split
    
    # Split the dataset into training and validation sets
    train_data, val_data = train_test_split(data, train_size=train_size, random_state=42)
    return train_data, val_data

def save_preprocessed_data(train_data, val_data, output_dir):
    # Save the preprocessed datasets to the specified output directory
    train_data.to_csv(f"{output_dir}/train_data.csv", index=False)
    val_data.to_csv(f"{output_dir}/val_data.csv", index=False)