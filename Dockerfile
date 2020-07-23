FROM python:3

WORKDIR /app

COPY ./ .

RUN pip install -r requirements.txt

EXPOSE 5000

ENV FLASK_APP run.py
ENV FLASK_ENV production

ENV DB_NAME space 
ENV DB_USER ''
ENV DB_HOST mongo
ENV DB_PASSWORD ''

CMD flask run --host=0.0.0.0