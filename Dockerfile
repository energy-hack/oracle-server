FROM python:3.6
    
RUN mkdir /quasar_flask_api
WORKDIR /quasar_flask_api
RUN pip install flask 
RUN pip install pytz

ADD ./quasar_flask_api .

ENTRYPOINT ["python", "app.py"]