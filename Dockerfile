FROM python:3.9-slim
WORKDIR /app
COPY scrape.py . 
RUN pip install pandas discord_webhook tabula-py
CMD ["python", "-u", "scrape.py"]
