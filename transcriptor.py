import subprocess
from pathlib import Path

MODEL_PATH = Path("models/ggml-base.en.bin") #the path of the model you decide to use
WHISPER_EXE_PATH = Path("build/bin/Release/whisper-cli.exe") #the path of the executable 
FFMPEG = "ffmpeg"

#this method allows you to first extract the audio from the video and then transcribe it into a txt file
def transcribe_video(video_path_str, output_dir_str):
    video_path = Path(video_path_str)
    output_dir = Path(output_dir_str)
    base_name = video_path.stem
    audio_path = output_dir / f"{base_name}.wav"
    transcript_path = output_dir / f"{base_name}.txt"

    logs = []

    if not MODEL_PATH.exists():
        logs.append(f"Model not found in the folder: {MODEL_PATH}")
        return False, logs
    if not WHISPER_EXE_PATH.exists():
        logs.append(f"Executable whisper-cli.exe not found in the folder: {WHISPER_EXE_PATH}")
        return False, logs

    logs.append(f"🎬 Video: {video_path.name}")
    logs.append("🎧 Audio extraction...")

    ffmpeg_cmd = [
        FFMPEG,
        "-y",
        "-i", str(video_path),
        "-ar", "16000",
        "-ac", "1",
        "-c:a", "pcm_s16le",
        str(audio_path)
    ]

    try:
        subprocess.run(ffmpeg_cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except Exception as e:
        logs.append(f"❌ Error during the extraction of the audio: {e}")
        return False, logs

    logs.append("🧠 Transcribing...")

    whisper_cmd = [
        str(WHISPER_EXE_PATH),
        "-m", str(MODEL_PATH),
        "-f", str(audio_path),
        "--output-txt",
        "-of", str(transcript_path.with_suffix(""))  
    ]

    try:
        subprocess.run(whisper_cmd, check=True)
    except Exception as e:
        logs.append(f"❌ Error during the transcription: {e}")
        return False, logs

    logs.append(f"✅ Done! Trascription saved in the folder: {transcript_path}")
    return True, logs
