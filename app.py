from re import sub
import gradio as gr
from utils.transcription import transcribe_audio
from utils.summarization import summarize_text
from utils.action_items import extract_action_items
from utils.report_export import export_to_docx
import config

def process_meeting(audio_file):
    if not audio_file:
        print("No audio file provided.")
        return 
    else:
        print(f"Processing audio file: {audio_file}")
        transcript = transcribe_audio(audio_file)
    
        summary = summarize_text(transcript)

        action_items = extract_action_items(transcript)

        report_path = export_to_docx(summary, action_items)

        return transcript, summary, "\n".join(action_items), report_path

with gr.Blocks() as demo:
    gr.Markdown("## 📋 AI Meeting Summarizer + Action Item Extractor")
    with gr.Row():
        audio_input = gr.Audio(type="filepath", label="Upload Meeting Audio")
        
    with gr.Row():
        submit_button = gr.Button("Submit", variant="primary")

    with gr.Row():
        transcript_output = gr.Textbox(label="Full Transcript")
        summary_output = gr.Textbox(label="Summary")
        actions_output = gr.Textbox(label="Action Items")
    report_output = gr.File(label="Download Report")

    submit_button.click(
        fn=process_meeting,
        inputs=[audio_input],
        outputs=[transcript_output, summary_output, actions_output, report_output]
    )

if __name__ == "__main__":
    demo.launch()
