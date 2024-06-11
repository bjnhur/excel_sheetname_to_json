import os
import pandas as pd
import json
import argparse

def make_file_name(workbook_name):
    # 파일명과 확장자 분리
    base_name, extension = os.path.splitext(workbook_name)
    new_name = f"{base_name}_config.json"
    # if extension.lower() == '.xlsx':
    #     new_name = f'{base_name}.docx'
    # else:
    #     # # 확장자가 .xlsx가 아닐 경우에도 처리
    #     # new_name = f'{base_name}_sfr_doc_table{extension}'
    #     # 그냥 동일하게
    #     new_name = f'{base_name}.docx'
    
    return new_name

def save_sheet_names_to_json(filename):
    # 엑셀 파일을 열어 시트 이름들을 추출
    xls = pd.ExcelFile(filename)
    sheet_names = xls.sheet_names
    
    # 결과를 JSON 형식으로 변환
    config_data = {
        "workbookName": filename,
        "sheetName_List": sheet_names,
        "base_row_pos" : 5,
        "base_col_pos" : [2,3,4,5,6,7,8]
    }
    
    new_config_file_name = make_file_name(filename)
    # JSON 파일로 저장
    with open(new_config_file_name, 'w') as json_file:
        json.dump(config_data, json_file, indent=4)

def main():
    parser = argparse.ArgumentParser(description="Extract sheet names from an Excel file and save them to a JSON file.")
    parser.add_argument("filename", help="The Excel file to process.")
    args = parser.parse_args()
    
    # 함수 호출
    save_sheet_names_to_json(args.filename)

if __name__ == "__main__":
    main()
