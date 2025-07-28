FROM python:3.10-slim

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    build-essential \
    libgl1-mesa-glx \
    poppler-utils \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt && pip install huggingface_hub==0.14.1


COPY . .

CMD ["python", "test_runner.py", "--input_folder", "Collection_1/"]
