"""Gradio interface for audio bandwidth extension using AP-BWE models."""

import os
import gradio as gr
from ap_bwe.api import process_audio
from .download import get_default_checkpoint


def process_with_model_type(audio_path, model_type):
    if not audio_path:
        return None

    checkpoint_path = get_default_checkpoint(model_type)
    return process_audio(audio_path, checkpoint_path)


def create_interface():
    model_choices = [
        "16kHz (2kHz input)",
        "16kHz (4kHz input)",
        "16kHz (8kHz input)",
        "48kHz (8kHz input)",
        "48kHz (12kHz input)",
        "48kHz (16kHz input)",
        "48kHz (24kHz input)",
    ]

    gr.Markdown("### About")
    gr.Markdown(
        """
    This interface uses AP-BWE (Amplitude-Phase Bandwidth Extension) to enhance audio quality.
    
    - 16kHz BWE: Supports upsampling from 2kHz, 4kHz, or 8kHz to 16kHz
    - 48kHz BWE: Supports upsampling from 8kHz, 12kHz, 16kHz, or 24kHz to 48kHz
    
    Select the appropriate model based on your source audio and desired output.
    """
    )

    gr.Markdown("# AP-BWE: Audio Bandwidth Extension")
    gr.Markdown("Upload audio files and enhance their bandwidth using AP-BWE models.")

    with gr.Row():
        with gr.Column():
            audio_input = gr.Audio(label="Input Audio", type="filepath")
            model_type = gr.Dropdown(
                label="Model Type", choices=model_choices, value=model_choices[0]
            )
            process_btn = gr.Button("Process")

        with gr.Column():
            audio_output = gr.Audio(label="Enhanced Audio")

    process_btn.click(
        fn=process_with_model_type,
        inputs=[audio_input, model_type],
        outputs=audio_output,
    )
