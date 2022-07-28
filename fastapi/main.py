from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles


app = FastAPI()


app.mount('/flutter_app', StaticFiles(directory='flutter_app'),
          name='Flutter App')
