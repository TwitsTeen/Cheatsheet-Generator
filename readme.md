# Cheatsheet Generator with Ollama

## Description

This Python program uses Ollama to generate cheatsheets in Markdown (.md) format and then converts them into PDF (.pdf). It utilizes the following libraries:

    requests – For making API calls to Ollama
    json – For handling JSON responses
    markdown – For processing Markdown content
    pdfkit – For converting Markdown to PDF

## Features

    Generates cheatsheets for various topics using AI.
    Saves the cheatsheet in Markdown format (.md).
    Converts the Markdown file to a PDF (.pdf).

## Requirements

Ensure you have the following installed:

    Python 3.x
    wkhtmltopdf (required by pdfkit)

## Install dependencies using:

pip install requests markdown pdfkit

## Installation

Clone the repository:

git clone https://github.com/TwitsTeen/Cheatsheet-Generator.git
cd cheatsheet-generator

## Usage

Run the script and specify the topic for the cheatsheet:

python main.py "Python Basics"

Example Output

    Python_Basics.md – Contains the generated cheatsheet in Markdown format.
    Python_Basics.pdf – The final converted PDF file.

## Configuration

Modify generate_cheatsheet.py to customize:

    The Ollama API endpoint
    Formatting options for Markdown and PDF
