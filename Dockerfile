FROM python:3.10-alpine
COPY ./ /app
RUN pip install -r /app/requirements.txt --no-cache-dir
EXPOSE 8080
CMD python /app/app.py
