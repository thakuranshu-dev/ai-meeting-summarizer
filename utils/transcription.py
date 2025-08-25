"""
Transcription utilities using OpenAI's Whisper model.
"""
import whisper
import os
import config

# Set ffmpeg path manually (adjust if different on your system)
os.environ["PATH"] += os.pathsep + r"C:\ffmpeg\bin"

_loaded_models = {}

def load_model(model_size):
    """
    Load and cache Whisper model by size.
    Options: tiny, base, small, medium, large
    """
    if model_size not in _loaded_models:
        _loaded_models[model_size] = whisper.load_model(model_size)
    return _loaded_models[model_size]


# def transcribe_audio(file_path, model_size="small"):
#     model = whisper.load_model(model_size)
#     result = model.transcribe(file_path)
#     return result["text"]

# preferred modal for cpu
def transcribe_audio(file_path, model_size=config.WHISPER_MODEL_SIZE):
    """
    Transcribe audio file using Whisper tiny model (lightweight).
    Options: tiny, base, small, medium, large
    """
    model = load_model(model_size)
    result = model.transcribe(file_path)
    return result["text"]
