import pandas as pd
import numpy as np
import os
import shutil
from pathlib import Path

audio_classifications = pd.read_csv('esc50.csv')

def process_audio_classifications(df):
    df.dropna(inplace=True)
    
    # Base paths
    audio_base_path = '../archive/audio/audio'
    classifications_base_path = '../Original Classifications'
    
    for file in df.iterrows():
        filename = file[1]['filename']
        category = file[1]['category']
        
        # Construct source and destination paths
        source_file = os.path.join(audio_base_path, filename)
        dest_folder = os.path.join(classifications_base_path, category)
        dest_file = os.path.join(dest_folder, filename)
        
        # Check if source file exists
        if not os.path.exists(source_file):
            print(f"Warning: File not found - {source_file}")
            continue
        
        # Create destination folder if it doesn't exist
        os.makedirs(dest_folder, exist_ok=True)
        
        # Move the file
        try:
            shutil.move(source_file, dest_file)
            print(f"Moved {filename} to {category}/")
        except Exception as e:
            print(f"Error moving {filename}: {e}")

# Run the classification
process_audio_classifications(audio_classifications)

