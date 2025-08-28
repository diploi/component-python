<img alt="icon" src=".diploi/icon.svg" width="32">

# Python Component for Diploi

Uses the unofficial [arm64v8/python](https://hub.docker.com/r/arm64v8/python/) Docker image.

## Operation

### Development

Will activate a virtual environment in `.venv` and run `pip install -r requirements.txt` when component is first initialized, and `python src/main.py` when deployment is started.

### Production

Will build a production ready image. Image runs `pip install -r requirements.txt` when being created. Once the image runs, `python src/main.py` is called.
