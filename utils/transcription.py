import whisper

def transcribe_audio(file_path, model_size="small"):
    model = whisper.load_model(model_size)
    result = model.transcribe(file_path)
    return result["text"]
