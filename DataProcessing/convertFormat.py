# GOAL: Convert all .m4a files to .wav
import os
from pydub import AudioSegment
from pathlib import Path

def convert_m4a_to_wav(categories):
    base_path = Path('../Final Classifications')
    
    total_converted = 0
    
    for category in categories:
        category_path = base_path / category
        
        if not category_path.exists():
            print(f"Warning: Directory not found - {category_path}")
            continue
        
        print(f"\nProcessing category: {category}")
        
        # Find all .m4a files in the category
        m4a_files = list(category_path.glob('*.m4a'))
        
        if not m4a_files:
            print(f"  No .m4a files found")
            continue
        
        print(f"  Found {len(m4a_files)} .m4a file(s)")
        
        for m4a_file in m4a_files:
            try:
                print(f"  Converting: {m4a_file.name}")
                
                # Load the m4a file
                audio = AudioSegment.from_file(str(m4a_file), format='m4a')
                
                # Create output filename
                wav_filename = m4a_file.stem + '.wav'
                wav_path = m4a_file.parent / wav_filename
                
                # Export to wav
                audio.export(str(wav_path), format='wav')
                print(f"    Saved: {wav_filename}")
                
                # Remove the original m4a file
                m4a_file.unlink()
                print(f"    Removed: {m4a_file.name}")
                
                total_converted += 1
            
            except Exception as e:
                print(f"    Error converting {m4a_file.name}: {e}")
    
    print(f"\n✓ Conversion complete! {total_converted} file(s) converted.")

# Run the converter on specified categories
if __name__ == "__main__":
    categories = ['Music', 'Outdoors', 'Silent', 'Talking', 'Traffic']
    convert_m4a_to_wav(categories)
