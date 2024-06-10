# User Manual for the Automated SFR Table Generator

## Overview
This manual outlines the three-step process required to generate SFR tables from an Excel file. Each step is designed to be executed sequentially to ensure smooth operation and correct output.

## Step 1: Set Up Python Environment on Windows

### Download and Install Python
- **Download Python:** Visit the [official Python website](https://www.python.org/downloads/) and download the latest version of Python 3 for Windows. Choose the installer that corresponds to your system's architecture (32-bit or 64-bit).
- **Install Python:** During installation, check "Add Python 3.x to PATH" to enable running Python from the Command Prompt. Follow the prompts and click “Install Now”.

### Verify Python Installation
- **Check Installation:** Open Command Prompt and type `python --version` to see the Python version, confirming the installation.

### Install Required Libraries
- **Install Libraries:** In Command Prompt, run the following command to install libraries necessary for handling Excel files and creating Word documents:
  ```bash
  pip install pandas numpy openpyxl python-docx
  ```

## Step 2: Prepare Your Files and Workspace

### Set Up Working Directory
- **Create a Working Folder:** Create a dedicated folder to store the INFO Excel file and Python scripts.

### Download Necessary Files
- **Download Files:** Obtain the original INFO Excel file and the Python scripts required for generating the SFR tables.

### Configure Project Files
- **Create a `config.json` File:** Construct a JSON configuration file that specifies paths and settings. Here is a sample configuration:
  ```json
  {
    "filename": "sample_excel.xlsx",
    "sheetNames": ["Sheet1", "Sheet2"],
    "base_row_pos": 5,
    "base_col_pos": [2, 3, 4, 5, 6, 7, 8]
  }
  ```
- **Note:** You can manually create the config file based on the above sample or use a tool to generate it initially if dealing with many sheets.

### Step 2-1: Automatically Create Initial `config.json` File

#### Use `make_config_file.py` Script
1. **Ensure Scripts and Files are in the Same Directory:** Place `make_config_file.py` and `sample_excel.xlsx` in the same directory.
2. **Navigate to the Directory:**
   ```bash
   cd path_to_directory
   ```
3. **Execute the Script:**
   ```bash
   python make_config_file.py sample_excel.xlsx
   ```
   This command runs the script with `sample_excel.xlsx` as the input file. The script reads the sheet names from the Excel file and saves them in a `config.json` file in the same directory.

Upon successful execution, a `config.json` file will be created in the same directory. This file will contain the names of the sheets from the `sample_excel.xlsx` file, formatted as follows:
```json
{
  "filename": "sample_excel.xlsx",
  "sheetNames": ["Sheet1", "Sheet2"],
  "base_row_pos": 5,
  "base_col_pos": [2, 3, 4, 5, 6, 7, 8]
}
```

## Step 3: Execute the Scripts and Generate Outputs

### Navigate to the Script Directory
- **Change Directory:** Use Command Prompt to navigate to the directory containing the scripts:
  ```bash
  cd path_to_directory
  ```

### Run the Scripts
- **Execute Scripts:** Run `generate_sfr_excel.py` and `create_word_doc.py` using the following commands:
  ```bash
  python generate_sfr_excel.py
  python create_word_doc.py
  ```

### Check Outputs and Troubleshoot
- **Expected Output:** Check the specified output directory for newly created Excel and Word files.
- **Troubleshooting Tips:**
  - **ModuleNotFoundError:** Ensure all required libraries are installed.
  - **FileNotFoundError:** Verify that all files are correctly named and located as specified.

### Contact for Assistance
For further issues or questions, please contact [me](mailto:bongjun@bos-semi.com).
