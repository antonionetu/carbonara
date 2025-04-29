import pandas as pd
from fastapi import UploadFile
from typing import Optional

def uploadFileToPandas(file: UploadFile) -> Optional[pd.DataFrame]:
    try:
        contents = file.file.read()
        df = pd.read_csv(pd.compat.StringIO(contents.decode('utf-8')))
        return df

    except Exception as e:
        print(f"Erro ao processar arquivo {file.filename}: {e}")
        return None
