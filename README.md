# RAGAS Synthetic Test Data Generator For RAG Evaluation

A Python-based tool for generating synthetic test datasets to evaluate RAG (Retrieval Augmented Generation) systems using RAGAS and OpenAI. This generator creates diverse question-answer pairs with configurable distributions of simple, multi-context, and reasoning questions.

## Features

- 🤖 Automated test data generation using OpenAI's GPT-4
- 📊 Customizable question type distributions
- 📝 Markdown document support
- 📈 CSV export functionality
- 🔧 Easy-to-use implementation with LangChain

## Prerequisites

Before running the generator, make sure you have:
- Python 3.8 or higher
- OpenAI API key
- Your documents in Markdown format

## Installation

1. Clone the repository:

- git clone https://github.com/Croups/ragas-synthetic-data-generator.git
- cd ragas-synthetic-data-generator

2. Install required packages:

- pip install ragas langchain-openai langchain pandas

3. Set up your OpenAI API key:

- export OPENAI_API_KEY='your-api-key'

## Usage

Place your Markdown documents in the Sample_Docs_Markdown/ directory

Run the generator:

- python main.py

Find your generated test dataset in generated_testset.csv

## Contributing

- Contributions are welcome! Please feel free to submit a Pull Request.

## License

- This project is licensed under the MIT License - see the LICENSE file for details.


## Contact

- LinkedIn: www.linkedin.com/in/enes-koşar
- GitHub: https://github.com/Croups
