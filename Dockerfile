FROM python:3.8-alpine

COPY api_users/requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -U -r /tmp/requirements.txt

COPY ./api_users /app
WORKDIR /app

EXPOSE 5050
CMD ["python","app.py"]


# Run Container:
# docker build -t fcamara.nilohealth:0.1 .
# docker run --name fcamara.nilohealth --add-host=host.docker.internal:172.17.0.1 -p 5050:5050 -d fcamara.nilohealth:0.1