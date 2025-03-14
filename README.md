# **Image Converter**  

A simple Python script to convert and compress images (including AVIF support). Supports format conversion and optional compression to a target size.  

## **Features**  
✅ Convert images between formats (AVIF, JPG, PNG, etc.)  
✅ Compress images to reduce file size  
✅ Works as a standalone script or a global command  

## **Setup**  

### **1. Create a Project Directory**  
First, create a dedicated folder to store the script and images:  
```bash
mkdir -p ~/ConvertedImages
cd ~/ConvertedImages
```

### **2. Clone the Repository**  
```bash
git clone git@github.com:yourusername/img-converter.git  
cd img-converter
```

### **3. Create and Activate a Virtual Environment**  
```bash
python3 -m venv .venv  
source .venv/bin/activate  # macOS/Linux
```

### **4. Install Dependencies**  
```bash
pip install -r requirements.txt
```

---

## **Usage**  

### **Convert an Image**  
```bash
python img_converter.py input.avif output.jpg
```

### **Convert & Compress (Target Size in KB)**  
```bash
python img_converter.py input.jpg output.webp 500
```

---

## **Running the Script Globally**  

Want to run `img_converter` from anywhere in your terminal? Follow these steps:  

### **1. Move the `run_converter` Script**  
```bash
mkdir -p ~/bin  
mv run_converter.sh ~/bin/run_converter  
chmod +x ~/bin/run_converter
```

### **2. Add `bin` to Your PATH**  
```bash
echo 'export PATH="$HOME/bin:$PATH"' >> ~/.zshrc  # macOS (zsh)
source ~/.zshrc
```

### **3. Convert Images Globally**  
Now, you can place images inside `~/ConvertedImages/` and convert them from anywhere:  
```bash
run_converter input.avif output.jpg 1000
```
This automatically runs the script while keeping all images inside `~/ConvertedImages/`.

---
