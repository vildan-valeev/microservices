FROM python:3.8

#RUN apt install wkhtmltopdf

ENV PYTHONUNBUFFERED 1
COPY /pb /pb

WORKDIR /app

COPY requirements.txt .
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
