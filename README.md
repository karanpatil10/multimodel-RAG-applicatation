# Multimodal RAG Application

## Overview

This project is intended to build a multimodal Retrieval-Augmented Generation
(RAG) application. The goal is to let users ask questions about a collection of
content, retrieve relevant context from that collection, and use that context to
generate grounded responses. A multimodal version of this workflow can work with
text as well as other supported media, such as images or documents containing
visual content.

The repository is currently a starter workspace: application source code and
dependencies have not been added yet.

## Intended workflow

1. Add or select source documents and other supported media.
2. Extract useful text and information from the sources.
3. Split and index that information so relevant passages can be retrieved.
4. Retrieve context related to a user's question.
5. Generate a response using the retrieved context.

## Requirements

- Python 3.12
- [uv](https://docs.astral.sh/uv/) for Python and virtual-environment management

## Set up the Python environment

In Command Prompt (`cmd.exe`), list the Python versions uv can find:

```cmd
uv python list
```

If Python 3.12 is not available, install it with uv:

```cmd
uv python install 3.12
```

Create a virtual environment named `env` using Python 3.12:

```cmd
uv venv env --python 3.12
```

Activate the environment in Command Prompt:

```cmd
env\Scripts\activate.bat
```

When project dependencies have been added to `requirment.txt`, install them
with:

```cmd
uv pip install -r requirment.txt
```

To leave the virtual environment:

```cmd
deactivate
```

## Project status

The application implementation and its dependencies are not present yet.
Add the application code and list its required packages in `requirment.txt`
before running the project.