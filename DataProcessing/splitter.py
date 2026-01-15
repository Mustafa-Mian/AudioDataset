# GOAL: Split multiple 20 second audio files into 5 second clips
import os
from pydub import AudioSegment
from pathlib import Path

# Splits all audio files in source_dir into 5 second chunks.
def split_audio_files(source_dir, chunk_duration_ms=5000):
    source_path = Path(source_dir)
    
    audio_extensions = {'.mp3', '.wav', '.ogg', '.flac', '.m4a'}
    
    audio_files = [f for f in source_path.iterdir() 
                   if f.is_file() and f.suffix.lower() in audio_extensions]
    
    if not audio_files:
        print(f"No audio files found in {source_dir}")
        return
    
    print(f"Found {len(audio_files)} audio file(s) to process")
    
    for audio_file in audio_files:
        try:
            print(f"\nProcessing: {audio_file.name}")
            
            audio = AudioSegment.from_file(str(audio_file))
            duration_ms = len(audio)
            
            num_chunks = (duration_ms + chunk_duration_ms - 1) // chunk_duration_ms
            
            print(f"  Duration: {duration_ms}ms → splitting into {num_chunks} chunks")
            
            for i in range(num_chunks):
                start_ms = i * chunk_duration_ms
                end_ms = min((i + 1) * chunk_duration_ms, duration_ms)
                
                chunk = audio[start_ms:end_ms]
                
                # Create output filename
                base_name = audio_file.stem
                chunk_filename = f"{base_name}_chunk_{i:03d}{audio_file.suffix}"
                chunk_path = audio_file.parent / chunk_filename
                
                # Export chunk
                chunk.export(str(chunk_path), format=audio_file.suffix[1:])
                print(f"    Saved: {chunk_filename}")
        
        except Exception as e:
            print(f"  Error processing {audio_file.name}: {e}")

# Run the splitter on ambientSounds directory
if __name__ == "__main__":
    ambient_sounds_dir = '../archive/mySounds'
    split_audio_files(ambient_sounds_dir)