# 🧐 Whisper.cpp GUI Transcriber

A lightweight Python-based GUI to transcribe video files using [`whisper.cpp`](https://github.com/ggerganov/whisper.cpp). The app extracts audio from videos, transcribes it to text using `whisper-cli.exe`.

---

## 📖 Why This Repo?

This project was created for people like me — a bit lazy, and definitely tired of rewatching long class recordings just to remember a few key points.
Instead of watching hours of lectures again, you can get everything transcribed and just **read the parts you need**.

**Important**: Be sure to download the right Whisper model depending on your machine’s power:

* `tiny` or `base` if you have a lower-end laptop
* `medium` or `large` for better accuracy (but needs more RAM and CPU power)

\n**Also be sure to copy the content of this repository in the whisper.cpp folder (If you have problem installing whisper.cpp then Follow the installation tutorial on the whisper.cpp repository at the top of this readme), in case the path of the whisper-cli.exe is different change it with your own path in the transcriptor.py file**
---

## 📦 Requirements

### 💻 System

* Windows 10 or later
* Python 3.8+
* `ffmpeg` (must be in your system PATH)

### 🧪 Python Libraries

* `tkinter` (usually pre-installed)
* `pathlib`
* `subprocess`

Install dependencies (if needed):

```bash
pip install --upgrade pip
pip install pathlib
```

---

## 🔧 Installing and Setting Up `whisper.cpp`

Follow these steps to compile `whisper.cpp` and download a model.

### ✅ Step 1: Clone the repository

```bash
git clone https://github.com/ggerganov/whisper.cpp
cd whisper.cpp
```

---

### ✅ Step 2: Download a Whisper model

Run this script (or download manually):

```bash
./models/download-ggml-model.sh base.en
```

If you're on Windows and can't run `.sh` files, manually download `ggml-base.en.bin` from:

📎 [https://huggingface.co/ggerganov/whisper.cpp/tree/main](https://huggingface.co/ggerganov/whisper.cpp/tree/main)

Place it into the folder:

```bash
whisper.cpp/models/
```

---

### ✅ Step 3: Compile whisper.cpp

You need CMake and a C++ compiler.


```bash
cd whisper.cpp
mkdir build
cd build
cmake .. -DCMAKE_BUILD_TYPE=Release
cmake --build . --config Release
```

You should now see:

```bash
build/bin/Release/whisper-cli.exe
```

Copy `whisper-cli.exe` into your Python project root.

---



## 🚀 How to Use

1. Place a video file (e.g. `.mp4`, `.mkv`) anywhere on your system.
2. Run the GUI:

```bash
python whisper_gui.py
```

3. In the GUI:

   * Click **“Select Video”** to choose a video file.
   * Click **“Select Folder”** to select an output folder.
   * Click **“Start Transcription”** to begin.

The GUI will:

* Extract audio to `.wav` using `ffmpeg`
* Transcribe using `whisper-cli.exe`
* Save the `.txt` transcript into your chosen folder

---

## 📌 Notes

* The transcription uses the `base.en` model (English only). You can use a larger model like `medium` or `large` if needed.

---

## 💡 Future Improvements

* Language auto-detection (`--detect-language`)
* Adding a NLP model to handle repetetive and out of context words
* Batch processing of videos

---

## 📄 License

MIT License. Free to use and modify.
