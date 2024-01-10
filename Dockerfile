FROM python:3.11.7



WORKDIR /url_shortener

COPY . /url_shortener
COPY .env /url_shortener/.env
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080
#ENTRYPOINT ["/entrypoint.sh"]
CMD ["uvicorn", "asgi:api", "--host", "0.0.0.0", "--port", "8080"]