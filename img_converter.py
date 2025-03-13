import sys
import subprocess
import os
from PIL import Image
from tqdm import tqdm  # Progress bar library

#Ensure AVIF support by dynamically loading the pillow_avif plugin if necessary
def ensure_avif_plugin():
    try:
        import pillow_avif  # Try to import the AVIF plugin
        print("✅ AVIF plugin loaded.")
    except ImportError:
        print("⚠️ AVIF support missing. Installing pillow-avif-plugin...")
        subprocess.run([sys.executable, "-m", "pip", "install", "pillow-avif-plugin"], check=True)
        import pillow_avif  # Try importing again after installation
        print("✅ AVIF plugin installed and loaded.")

#Compress and convert the image
def compress_image(input_path, output_path, max_size_kb=None):
    try:
        img = Image.open(input_path)

        # Convert image mode if needed (e.g., RGBA to RGB)
        if img.mode in ("RGBA", "P"):
            img = img.convert("RGB")

        # Default quality
        quality = 95
        img.save(output_path, quality=quality, optimize=True)  # Save with initial quality

        # 🟢 If compression is requested
        if max_size_kb:
            max_size_bytes = max_size_kb * 1024
            print(f"Starting compression to meet size ~{max_size_kb}KB")
            with tqdm(total=max_size_kb, desc="Compressing", unit="KB") as pbar:
                # While the file is larger than the max size, reduce quality
                while os.path.getsize(output_path) > max_size_bytes and quality > 10:
                    quality -= 5  # Reduce quality in steps of 5
                    img.save(output_path, quality=quality, optimize=True)  # Save again with lower quality
                    pbar.update(1)  # Update the progress bar

        print(f"✅ Converted: {input_path} → {output_path}")
        if max_size_kb:
            print(f"📉 Compressed to ~{max_size_kb}KB")

    except Exception as e:
        print(f"❌ Error processing {input_path}: {e}")



# 🟢 Step 4: Command-line arguments
if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: img_converter.py input.jpg output.png [max_size_kb]")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    max_size_kb = int(sys.argv[3]) if len(sys.argv) > 3 and sys.argv[3].isdigit() else None

    if not os.path.exists(input_file):
        print(f"❌ Error: Input file '{input_file}' does not exist.")
        sys.exit(1)

    # Ensure AVIF plugin is loaded
    ensure_avif_plugin()

    compress_image(input_file, output_file, max_size_kb)
