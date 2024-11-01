from setuptools import setup, find_packages

setup(
    name="mistral_interpreter",
    version="0.1.0",
    packages=find_packages(),
    install_requires=["mistralai"],
    author="Jules Bousrez",
    author_email="contact@julesbousrez.fr",
    description="A simple interpreter to create with Mistral AI.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/julesbsz/mistral-interpreter",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        "console_scripts": [
            "mistral-interpreter=mistral_interpreter.chatbot:run_main",
        ],
    },
)
