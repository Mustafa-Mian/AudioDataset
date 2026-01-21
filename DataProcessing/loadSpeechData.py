from datasets import load_dataset, Audio
import os
import soundfile as sf

# Load microset
ds = load_dataset("MLCommons/peoples_speech", "microset", split="train")

# Disable automatic decoding (we'll handle it manually)
ds = ds.cast_column("audio", Audio(decode=False))

out_dir = "microset_wav"
os.makedirs(out_dir, exist_ok=True)

for i, ex in enumerate(ds):
    # Download the FLAC file to cache if not present
    flac_path = ex["audio"]["path"]

    # Read audio manually
    data, sr = sf.read(flac_path)

    # Convert to WAV
    wav_path = os.path.join(out_dir, f"sample_{i}.wav")
    sf.write(wav_path, data, sr)

print(f"✅ Done! {len(ds)} WAV files saved to {out_dir}")
