from .default import *
import urllib

APP_ENV = APP_ENV_STAGING

SQLALCHEMY_DATABASE_URI = "mssql+pyodbc:///?odbc_connect=%s" % urllib.parse.quote_plus('DRIVER={SQL Server};SERVER=DESKTOP-DUHA34C;DATABASE=miniblog;Trusted_Connection=yes;')
