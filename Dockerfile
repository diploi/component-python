FROM python:3.12-slim AS base

# This will be set by the GitHub action to the folder containing this component.
ARG FOLDER=/app

# Install dependencies only when needed
FROM base AS deps

COPY . /app
WORKDIR ${FOLDER}

# Install dependencies
RUN pip install --no-cache-dir --prefer-binary -r requirements.txt

# Production image, copy all the files and run "npm start"
FROM base AS runner

COPY --from=deps /app /app
WORKDIR ${FOLDER}

EXPOSE 8000
ENV PORT=8000
ENV HOST="0.0.0.0"

CMD ["python", "src/main.py"]
