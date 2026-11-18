import re
PERMISSIONS={'reader':{'search'},'operator':{'search','health'}}
def authorized(role,tool):
    return tool in PERMISSIONS.get(role,set())
def redact(text):
    return re.sub(r'[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}','[REDACTED_EMAIL]',text)
