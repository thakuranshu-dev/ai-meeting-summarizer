import whisper
import os

# Set ffmpeg path manually (adjust if different on your system)
os.environ["PATH"] += os.pathsep + r"C:\ffmpeg\bin"

# def transcribe_audio(file_path, model_size="small"):
#     model = whisper.load_model(model_size)
#     result = model.transcribe(file_path)
#     return result["text"]

# preferred modal for cpu
def transcribe_audio(file_path, model_size="tiny"):
    """
    Transcribe audio file using Whisper tiny model (lightweight).
    Options: tiny, base, small, medium, large
    """
    model = whisper.load_model(model_size)
    result = model.transcribe(file_path)
    return result["text"]
