BROKER_URL = "mongodb://127.0.0.1:27017/celerydb_teste"

CELERY_RESULT_BACKEND = "mongodb"

CELERY_MONGODB_BACKEND_SETTINGS = {
   "host": "127.0.0.1",
   "port": 27017,"database": "celerydb_resultados",
   "taskmeta_collection": "celerydb_resultados_meta",
}
CELERY_IMPORTS = ("computing.tasks", )
