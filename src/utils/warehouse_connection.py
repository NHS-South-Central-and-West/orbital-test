import sqlalchemy as sa
import pandas as pd
from . import params # use . for relative import when using sibling modules

def warehouse_connection(query):

   server = params.SERVER
   database = params.DATABASE
   connection_string = ('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+
                     ';DATABASE='+database+
                     ';ENCRYPT=no;TRUSTED_CONNECTION=yes;'
      )
   connection_url = sa.engine.URL.create(
      "mssql+pyodbc",
      query=dict(odbc_connect=connection_string)
      )
   engine = sa.create_engine(connection_url, fast_executemany= True)
   query = query
   df = pd.read_sql(query, engine)

   return df