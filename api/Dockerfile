# Usar una imagen base de Python
FROM python:3.10-slim

WORKDIR /app

COPY ./shared/ /app/shared
COPY ./api/ /app/api

RUN pip install --no-cache-dir -r /app/api/requirements.txt

ENV PYTHONPATH="${PYTHONPATH}:/app/shared/"

EXPOSE 8000

CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]
