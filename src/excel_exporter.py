import pandas as pd

def export_to_excel(data: list, filename: str):
    if not data :
        print ('no data to export')
    df = pd.DataFrame(data)
    with pd.ExcelWriter(filename,engine='openpyxl') as writer:
        df.to_excel(writer,index=False,sheet_name='Products')
        
        worksheet = writer.sheets['Products']
        worksheet.freeze_panes = 'A2'
        
        for column_cells in worksheet.columns:
            max_length = 0
            column_letter = column_cells[0].column_letter

            for cell in column_cells:
                if cell.value:
                    max_length = max(max_length, len(str(cell.value)))

            worksheet.column_dimensions[column_letter].width = max_length + 2
    # df.to_excel(filename, index=False)
