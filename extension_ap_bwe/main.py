import gradio as gr


def extension__tts_generation_webui():
    ap_bwe_ui()
    return {
        "package_name": "extension_ap_bwe",
        "name": "AP-BWE Bandwidth Extension",
        "requirements": "git+https://github.com/rsxdalv/extension_ap_bwe@main",
        "description": "AP-BWE: An audio bandwidth extension solution using Amplitude-Phase Bandwidth Extension models.",
        "extension_type": "interface",
        "extension_class": "audio-conversion",
        "author": "rsxdalv",
        "extension_author": "rsxdalv",
        "license": "MIT",
        "website": "https://github.com/rsxdalv/AP-BWE",
        "extension_website": "https://github.com/rsxdalv/extension_ap_bwe",
        "extension_platform_version": "0.0.1",
    }


def ap_bwe_ui():
    from extension_ap_bwe.gradio_app import create_interface

    create_interface()


if __name__ == "__main__":
    if "demo" in locals():
        locals()["demo"].close()
    with gr.Blocks() as demo:
        extension__tts_generation_webui()
    demo.launch(
        server_port=7771,
    )
