FROM python:3.12-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN groupadd -r appuser && useradd -r -g appuser appuser

COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY src ./src

RUN chown -R appuser:appuser /app

USER appuser

EXPOSE ${{ values.servicePort }}

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "${{ values.servicePort }}"]
