FROM python:3.6
    
RUN mkdir /quasar_flask_api
WORKDIR /quasar_flask_api

ADD quasar_flask_api/requirements.txt requirements.txt

RUN pip install -r requirements.txt

ADD ./quasar_flask_api .

ENTRYPOINT ["python", "app.py"]
