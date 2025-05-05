import pandas as pd
from fastapi import UploadFile
from typing import Optional
from io import StringIO, BytesIO

def uploadFileToPandas(file: UploadFile) -> Optional[pd.DataFrame]:
    try:
        filename = file.filename.lower()

        contents = file.file.read()

        if filename.endswith('.csv'):
            try:
                decoded = contents.decode('utf-8')
            except UnicodeDecodeError:
                decoded = contents.decode('latin1')
            df = pd.read_csv(StringIO(decoded))

        elif filename.endswith(('.xls', '.xlsx')):
            df = pd.read_excel(BytesIO(contents))

        else:
            print(f"Tipo de arquivo não suportado: {filename}")
            return None

        return df

    except Exception as e:
        print(f"Erro ao processar arquivo {file.filename}: {e}")
        return None
