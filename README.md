# 🚀 Object Detection with YOLO and Hugging Face 🤗

This project implements **real-time object detection** using **YOLOS (You Only Look One-Series)**, a transformer-based model available via **Hugging Face**. The app is built with **Streamlit**, allowing users to upload images and detect objects using a pre-trained YOLOS model.

---

## 🔥 **Features**
✅ Upload an image and detect multiple objects  
✅ Uses **YOLOS-Tiny** from Hugging Face for inference  
✅ **Bounding boxes & labels** drawn on detected objects  
✅ Displays **detection summary** with object labels and confidence scores  
✅ Streamlit-powered **web interface** for easy use  

---

## 📌 **Tech Stack**
- **Python** ![Python](python_18894.ico)
- **Hugging Face Transformers** 🤗  
- **YOLOS (You Only Look One-Series)** 🖼️  
- **Streamlit (UI Framework)** 🎨  
- **PIL (Image Processing)** 🖼️  
- **PyTorch (Deep Learning Framework)** 🔥  

---

## 🎯 **Installation & Setup**
### **Clone the repo**
```bash
git clone https://github.com/Atharva01/Object-Detection-using-YOLO-and-Hugging-Face.git \
```
### **Create a virtual environment
### 1. Windows 
```bash
python -m venv yolos
\yolos\bin\activate.bat
```
### 2. Linux (please ensure virtualenv is installed)

```bash
python3 -m venv yolos
source yolos/bin/activate
```

### **Install the dependencies**
```bash
pip install -r requirements.txt
```

### **Launch the StreamLit UI**
```bash
streamlit run app.py
```


