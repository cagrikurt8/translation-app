FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN apt-get update && apt-get -y install libssl-dev libasound2

RUN apt-get update && apt-get install -y \
    vorbis-tools \
    sox \
    alsa-utils \
    libasound2 \
    libasound2-plugins \
    pulseaudio \
    pulseaudio-utils \
    --no-install-recommends \
    && rm -rf /var/lib/apt/lists/* 

RUN pip install -r requirements.txt 

COPY . .

EXPOSE 8000

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]