FROM arm64v8/python:3.13-slim AS base

# This will be set by the GitHub action to the folder containing this component.
ARG FOLDER=/app

COPY . /app
WORKDIR ${FOLDER}

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000
ENV PORT=8000
ENV HOST="0.0.0.0"

CMD ["python", "src/main.py"]
