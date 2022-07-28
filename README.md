# flutter_web_on_fastapi

A Flutter Web application hosted served by FastAPI

This project is inspired by [this](https://betterprogramming.pub/serving-flutter-web-applications-with-python-flask-c60ab5fc3fc1) article.

## how to run
1. Install python dependencies
```
$ cd fastapi
$ pip install -r requirements.txt
```
2. Run the server
```
$ uvicorn main:app --reload
```
3. The Flutter App should now be running in your machine at [localhost:8000/flutter_ap/index.html](http://localhost:8000/flutter_app/index.html).

## how to serve a Flutter app in FastAPI
1. Copy the flutter build folder into the FastAPI project
2. Then in your FastAPI code, mount the build folder as a [StaticFile](https://fastapi.tiangolo.com/tutorial/static-files/). 
3. You might need to change the base href value of index.html
