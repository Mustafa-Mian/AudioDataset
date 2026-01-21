import argparse
from downloadSpeech import download

# Create arguments object
args = argparse.Namespace(
    csv_dataset='../data/balanced_train_segments.csv',
    destination_dir='../output',
    label_file='../data/class_labels_indices.csv',
    strict=False,
    blacklist=['Music', 'Noise', 'Dog']
)

# Download speech files
download('speech', args)