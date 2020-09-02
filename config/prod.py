from .default import *
import urllib

SECRET_KEY = '7110c8ae51a4b5af97be6534caef90e4bb9bdcb3380af008f90b23a5d1616bf319bc298105da20fe'

APP_ENV = APP_ENV_PRODUCTION

SQLALCHEMY_DATABASE_URI = "mssql+pyodbc:///?odbc_connect=%s" % urllib.parse.quote_plus('DRIVER={SQL Server};SERVER=DESKTOP-DUHA34C;DATABASE=miniblog;Trusted_Connection=yes;')
