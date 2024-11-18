FROM python:3.10-slim

WORKDIR /app

COPY ./shared/ /app/shared
COPY ./batch/ /app/batch

RUN pip install --no-cache-dir -r ./batch/requirements.txt

ENV PYTHONPATH "${PYTHONPATH}:/app/shared/"

CMD ["python", "./batch/main.py"]
