FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /Survey
COPY requirements.txt /Survey/
RUN pip install -r requirements.txt
COPY . /Survey/