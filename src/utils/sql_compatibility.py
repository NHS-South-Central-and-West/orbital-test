# functions to make Orbital's SQL compatible with 2016 SQL Server
# that we have in-house.

# if something is missing, add a function for it and then add it to the pipe in adapt_sql()

from . import params

# set up a user-defined pipe-style chaining function.
def _pipe(sql, *funcs):
    for func in funcs:
        sql = func(sql)
    return sql

#------------------------------------------------------------#
# any functions required to make the Orbital SQL output
# compatible with 2016 SQL Server go here: 

def replace_greatest(sql):

    sql = sql.replace('GREATEST',params.REPLACE_GREATEST_UDF)

    return sql

def reinsert_full_table(sql):
    
    sql = sql.replace(params.JUST_THE_TABLE,params.TABLE_NAME_FOR_REINSERTION)

    return sql

#------------------------------------------------------------#

# the function that will apply the processing pipeline to the
# SQL output from Orbital:

def adapt_sql(sql):
    sql = _pipe(
        sql,
        replace_greatest,
        reinsert_full_table
    )
    return sql
