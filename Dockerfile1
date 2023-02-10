FROM python:3.8-slim-buster

WORKDIR /app1

RUN pip install Flask requests

COPY city_name_to_zip_code.py .

ENV FLASK_APP=city_name_to_zip_code.py

EXPOSE 5050

CMD ["flask", "run", "--host=0.0.0.0"]
