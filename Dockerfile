FROM openjdk:21-slim-bullseye
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        ca-certificates \
        curl \
        python3.9 \
        python3-pip \
        python3.9-dev \
        python3-setuptools \
        python3-wheel

WORKDIR /app
COPY scrape.py . 
RUN pip install pandas discord_webhook tabula-py
CMD ["python", "-u", "scrape.py"]
