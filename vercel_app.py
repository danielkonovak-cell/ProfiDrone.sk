from app import app  # import your Flask app
from vercel_wsgi import handle

def handler(event, context):
    return handle(app, event, context)
