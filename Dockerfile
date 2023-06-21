FROM python:3.11
EXPOSE 5000
WORKDIR /app
COPY .keys .
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY ./src/art-generator .
CMD ["flask", "run", "--host", "0.0.0.0"]
