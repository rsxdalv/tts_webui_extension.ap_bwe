import setuptools

setuptools.setup(
    name="tts_webui_extension.ap_bwe",
    packages=setuptools.find_namespace_packages(),
    version="0.1.0",
    author="rsxdalv",
    description="AP-BWE: An audio bandwidth extension solution using Amplitude-Phase Bandwidth Extension models.",
    url="https://github.com/rsxdalv/tts_webui_extension.ap_bwe",
    project_urls={},
    scripts=[],
    install_requires=[
        "gradio",
        "huggingface_hub",
        "safetensors",
        "ap_bwe @ https://github.com/rsxdalv/AP-BWE/releases/download/v0.1.0/ap_bwe-0.1.0-py3-none-any.whl",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

