FROM python:3 AS base

# This will be set by the GitHub action to the folder containing this component.
ARG FOLDER=/app

# Install dependencies only when needed
FROM base AS deps

COPY . /app
WORKDIR ${FOLDER}

USER 1000:1000

# Install dependencies
RUN DISPLAY= pip install --no-cache-dir -r requirements.txt

# Production image, copy all the files and run "npm start"
FROM base AS runner

COPY --from=deps --chown=1000:1000 /app /app
WORKDIR ${FOLDER}

USER 1000:1000

EXPOSE 8000
ENV PORT=8000
ENV HOST="0.0.0.0"

CMD ["python", "src/main.py"]
