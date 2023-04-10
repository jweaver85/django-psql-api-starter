FROM python:3.11
ENV PYTHONUNBUFFERED=1
ENV PORT=8000
WORKDIR /app

COPY . .
RUN pip install --upgrade pip && pip install -r requirements.txt

EXPOSE $PORT
CMD python manage.py runserver 0.0.0.0:$PORT
