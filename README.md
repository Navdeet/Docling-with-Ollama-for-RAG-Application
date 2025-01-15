## Introduction

Welcome to **Docling with Ollama**! This tool is combines the best of both Docling for document parsing and Ollama for local models. It enables you to use Docling and Ollama for RAG over PDF files (or any other supported file format) with LlamaIndex. It provides you a nice clean Streamlit GUI to chat with your own documents locally.

**Reason of this project**
Document conversion, particularly from PDF to machine-processable formats, has long presented significant challenges due to PDF files’ diverse and often complex nature. These documents, widely used across various industries, frequently need more standardization, resulting in a loss of structural features when optimized for printing. This structural loss complicates the recovery process, as important elements such as tables, figures, and reading order can be misinterpreted or completely lost. As businesses and researchers increasingly rely on digital documents, the need for efficient and accurate conversion tools has become crucial. The advent of advanced AI-driven tools has provided a promising solution to these challenges, enabling better understanding, processing, and extracting content from complex documents.
A critical issue in document conversion is the reliable extraction of content from PDFs while preserving the document’s structural integrity. Traditional methods often falter due to the wide variability in PDF formats, leading to problems such as inaccurate table reconstruction, misplaced text, and lost metadata. This problem is technical and practical, as document conversion accuracy directly impacts downstream tasks such as data analysis, search functionality, and information retrieval. Given the growing reliance on digital documents for academic and industrial purposes, ensuring the fidelity of converted content is essential. The problem lies in developing tools that can handle these tasks with the precision required by modern applications, particularly when dealing with large-scale document collections.

Current tools for PDF conversion, both commercial and open-source, often need to meet the necessary standards of performance and accuracy. Many existing solutions are limited by their dependence on proprietary algorithms and restrictive licenses, which hinder their adaptability and widespread use. Even popular methods struggle with specific tasks, such as accurate table recognition and layout analysis, critical components of high-quality document conversion. For instance, tools like PyPDFium and PyMuPDF have been noted for their shortcomings in processing complex document layouts, resulting in merged text cells or distorted table structures. The lack of an open-source, high-performance solution that can be easily extended and adapted has left a significant gap in the market, particularly for organizations that require reliable tools for large-scale document processing.
Docling has demonstrated impressive capabilities across various hardware configurations. Tests conducted on a dataset of 225 pages revealed that Docling could process documents with sub-second latency per page on a single CPU. Specifically, on a MacBook Pro M3 Max with 16 cores, Docling processed 92 pages in just 103 seconds using 16 threads, achieving a throughput of 2.45 pages per second. Even on older hardware, such as an Intel Xeon E5-2690, Docling maintained respectable performance, processing 143 pages in 239 seconds with 16 threads. These results highlight Docling’s ability to deliver fast and accurate document conversion, making it a practical choice for environments with varying resource constraints.
![image](https://github.com/user-attachments/assets/aa5a89d0-763a-4057-8774-0ab43f2071ed)

## Prerequisites

Before you begin, ensure you have met the following requirements:

- **Python**: Make sure you have Python version >3.10 installed. You can download it from [python.org](https://www.python.org/downloads/).
- **Pip**: Ensure pip is installed to manage Python packages. It usually comes with Python.
- **Virtual Environment**: It's recommended to use a virtual environment to manage dependencies. I prefer Conda.
- **Ollama**: Make sure Ollama is installed and llama3.2 model is downloaded with ollama pull llama3.2 command

## Installation

To install **Docling With Ollama**, follow these steps:

1. **Clone the repo**:

    ```bash
    git clone https://github.com/Navdeet/Docling-with-Ollama-for-RAG-Application
    ```

2. **Navigate to the project directory**:

    ```bash
    cd doclingwithollama
    ```

3. **Create a virtual environment** (recommended):

    Use Conda: (recommended)
    ```bash
      conda create -n ai python=3.11 -y && conda activate ai
    ```
    Or Use Python VENV:
    ```bash
    python3 -m venv myenv
    source myenv/bin/activate  # On Windows use `myenv\Scripts\activate`
    ```

5. **Install the dependencies**:

    ```bash
    pip install torch 
    pip install git+https://github.com/huggingface/transformers
    
    pip install llama-index-core llama-index-readers-docling llama-index-node-parser-docling llama-index-readers-file python-dotenv llama-index-llms-ollama llama-index-embeddings-huggingface llama-index-llms-huggingface-api
    
    pip install pdfplumber numpy streamlit 

    ```

## Running the Tool

To run **Docling with Ollama**, execute the following command:

```bash
streamlit run app.py
```

Open your browser and go to `http://localhost:8501` to see the tool in action, if it doesnt open automatically.


## Usage
From the left panel, upload your local PDF file, and start chatting with them. In my case, I uploaded a PDF related to docking documentation.

![image](https://github.com/user-attachments/assets/5ce7471d-9ebd-49d5-b47a-16ceafb4337e)



