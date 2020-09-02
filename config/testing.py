from .default import *
import urllib

# Parámetros para activar el modo debug
TESTING = True
DEBUG = True

APP_ENV = APP_ENV_TESTING

SQLALCHEMY_DATABASE_URI = "mssql+pyodbc:///?odbc_connect=%s" % urllib.parse.quote_plus('DRIVER={SQL Server};SERVER=DESKTOP-DUHA34C;DATABASE=miniblog;Trusted_Connection=yes;')
