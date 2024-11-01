# Mistral Interpreter

An interactive Python interpreter to communicate with Mistral AI. This tool allows users to send messages to Mistral AI models and receive responses in real-time.

## Table of Contents

-   [Installation](#installation)
-   [Setup](#setup)
-   [Usage](#usage)
-   [Features](#features)
-   [Upcoming features](#upcoming)
-   [Support](#support)

## Installation

Clone this repository and navigate to the project directory:

```bash
git clone https://github.com/julesbsz/mistral-interpreter.git
cd mistral-interpreter
```

Install the package using `pip`:

```bash
pip install .
```

## Setup

The interpreter requires an API key for Mistral AI, which can be obtained by signing up at [Mistral AI](https://www.mistralai.com).

Set up the API key as an environment variable:

```bash
    echo 'export MISTRAL_API_KEY=[your_key_here]' >> ~/.zshenv
    source ~/.zshenv
```

## Usage

After installation, you can start the interpreter by running in your terminal:

```bash
mistral-interpreter
```

You can now chat with Mistral!

## Features

-   **Asynchronous Interaction**: Uses Python's asyncio for smooth, non-blocking message exchanges.
-   **Conversation History**: Maintains a session history for easy tracking and debugging.
-   **Command-line Friendly**: Initiate sessions and receive responses directly in the terminal.

## Upcoming features

1. Use Mistral to interact with local files
2. Allow Mistral to interact directly with your system (write and execute code, open apps...)
3. Use Mistral as a developer assistant with knowledge of your local codebase
4. And more!

## Support

The best way to support this project is by giving it a star on GitHub and sharing it as widely as possible. Your support helps bring more visibility to the project and contributes to its growth. Thank you for your help!
