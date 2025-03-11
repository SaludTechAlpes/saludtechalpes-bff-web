FROM python:3.9

EXPOSE 8003

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

WORKDIR /src

CMD [ "uvicorn", "bff_web.main:app", "--host", "0.0.0.0", "--port", "8003", "--reload"]
