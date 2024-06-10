## User Manual: Running `make_config_file.py`

### Requirements
Before running the script, ensure you have Python installed on your system. The script also requires the `pandas` and `openpyxl` libraries. You can install these using pip:

```bash
pip install pandas openpyxl
```

### File Structure
Ensure that the `make_config_file.py` and `sample_excel.xlsx` files are in the same directory.

### Running the Script
1. **Open your command line interface (CLI):**
   - On Windows, you can use Command Prompt or PowerShell.
   - On macOS or Linux, open the Terminal.

2. **Navigate to the directory containing the script:**
   ```bash
   cd path_to_directory
   ```
   Replace `path_to_directory` with the path where the files are located.

3. **Execute the script:**
   ```bash
   python make_config_file.py sample_excel.xlsx
   ```
   This command runs the script with `sample_excel.xlsx` as the input file. The script reads the sheet names from the Excel file and saves them in a `config.json` file in the same directory.

### Expected Output
Upon successful execution, a `config.json` file will be created in the same directory. This file will contain the names of the sheets from the `sample_excel.xlsx` file, formatted as follows:

```json
{
  "filename": "sample_excel.xlsx",
  "sheetNames": ["Sheet1", "Sheet2"]
}
```

### Troubleshooting
- **ModuleNotFoundError**: If you encounter a `ModuleNotFoundError`, make sure you have installed the required `pandas` and `openpyxl` libraries using pip.
- **FileNotFoundError**: This error indicates that the script does not find the `sample_excel.xlsx` file. Ensure the file name is correct and located in the same directory as the script.

For any further issues, verify that your Python environment is set up correctly and all files are in the appropriate directory.
