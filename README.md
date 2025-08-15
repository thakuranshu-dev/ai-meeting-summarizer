# AI Meeting Summarizer + Action Item Extractor

## Overview
This project is an AI-powered tool that transcribes meeting audio, summarizes the discussion, and extracts actionable items. It provides a simple web interface for users to upload meeting recordings and download a structured report in DOCX format.

## Features
- **Audio Transcription:** Converts meeting audio to text using OpenAI Whisper.
- **Summarization:** Generates concise meeting summaries using a transformer-based model (T5).
- **Action Item Extraction:** Identifies and lists actionable tasks from the transcript using rule-based NLP.
- **Report Export:** Creates a downloadable DOCX report containing the summary and action items.
- **User Interface:** Simple Gradio web app for easy interaction.

## How It Works
1. **Upload Audio:** Users upload a meeting audio file (e.g., MP3).
2. **Transcription:** The audio is transcribed to text using Whisper.
3. **Summarization:** The transcript is summarized using a transformer model.
4. **Action Items:** Actionable sentences are extracted from the transcript.
5. **Report Generation:** A DOCX report is generated and made available for download.

## Installation
1. Clone the repository:
	```sh
	git clone https://github.com/thakuranshu-dev/ai-meeting-summarizer.git
	cd ai-meeting-summarizer
	```
2. Install dependencies:
	```sh
	pip install -r requirements.txt
	```
	Additional dependencies refrences:
	- [Whisper](https://github.com/openai/whisper)
	- [Transformers](https://huggingface.co/docs/transformers/index)
	- [python-docx](https://python-docx.readthedocs.io/en/latest/)
	- [Gradio](https://gradio.app/)

## Usage
Run the app with:
```sh
python app.py
```
Then open the provided local URL in your browser. Upload a meeting audio file and view/download the results.

## File Structure
- `app.py` — Main Gradio app
- `utils/` — Core logic modules:
  - `transcription.py` — Audio transcription
  - `summarization.py` — Text summarization
  - `action_items.py` — Action item extraction
  - `report_export.py` — DOCX report generation
- `assets/` — Sample audio files
- `requirements.txt` — Python dependencies

## Example
A sample meeting audio (`assets/sample_meeting.mp3`) is provided for testing.

## License
This project is for educational and hackathon use. See repository for details.
