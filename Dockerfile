FROM python:3.10.8-alpine3.15

WORKDIR /src

COPY ./src /src

RUN pip install --no-chache-dir --upgrade pip && pip install --no-cache-dir -r requirements.txt

CMD ["python", "./src/web.py"]