# MagicPDF: Convert Excel Files to PDF

MagicPDF is a Python-based project that enables the conversion of single and multiple Excel files to PDF format. This utility simplifies the process of converting your Excel documents into portable and widely accessible PDF files.

## Features

- Convert single Excel files to PDF.
- Batch convert multiple Excel files to individual PDFs.

## Getting Started

### Installation

To begin using MagicPDF, follow these steps:

1. Clone the MagicPDF repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/MagicPDF.git
   ```

2. Navigate to the project directory:

   ```bash
   cd MagicPDF
   ```

3. Install the required dependencies using pip:

   ```bash
   pip install -r requirements.txt
   ```

### Usage

MagicPDF provides a straightforward command-line interface for converting Excel files to PDF.

#### Convert Single Excel File

To convert a single Excel file to PDF, use the following command:

```bash
python magicpdf.py convert --input input_file.xlsx --output output_file.pdf
```

Replace `input_file.xlsx` with the path to your input Excel file and `output_file.pdf` with the desired name of the output PDF file.

#### Batch Convert Multiple Excel Files

To batch convert multiple Excel files to individual PDFs, use the following command:

```bash
python magicpdf.py batch --input input_directory --output output_directory
```

Replace `input_directory` with the path to the directory containing your input Excel files and `output_directory` with the path to the directory where the output PDFs will be saved.

## Contribution

MagicPDF welcomes contributions from the open-source community. If you would like to contribute, fork the repository, make your changes, and submit a pull request. Contributions can include adding features, enhancing user experience, improving documentation, or fixing issues.

## License

MagicPDF is released under the [MIT License](LICENSE). You are free to use, modify, and distribute the project according to the terms of the license.
