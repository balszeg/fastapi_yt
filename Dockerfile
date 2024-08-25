FROM python:3.9.19

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install -r --no-cache-dir requirements.txt

COPY . .

CMD ["uvicorn", "app.main.:app", "--host", "0.0.0.0", "--port", "8000"]
