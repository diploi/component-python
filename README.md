<img alt="icon" src=".diploi/icon.svg" width="32">

# Python Component for Diploi

Uses [uv](https://docs.astral.sh/uv/) to manage Python versions & packages.

## Operation

### Development

Will activate a virtual environment in `.venv` and run `uv sync` when component is first initialized, and `python src/main.py` when deployment is started.

### Production

Will build a production ready image. Image runs `uv sync` when being created. Once the image runs, `python src/main.py` is called.
