# Spark Standalone Minio Setup

Setting Up Spark Standalone with MinIO Object Storage Using Docker Compose.

## Setup

This project uses [`uv`](https://github.com/astral-sh/uv) for dependency management and requires Python to be installed.

### Prerequisites

Ensure you have Python installed on your system. You can check by running:

```sh
python --version
```

Install `uv` if you haven't already:

```sh
pip install uv
```

### Installing Dependencies

To install dependencies from `uv.lock`:

```sh
uv venv --python 3.12
uv pip sync
```

Alternatively, to install dependencies from `pyproject.toml`:

```sh
uv pip install -r pyproject.toml
```

### Running the Project

Activate the virtual environment:

```sh
source .venv/bin/activate  # On macOS/Linux
.venv\Scripts\activate     # On Windows
```

Run your application:

```sh
python src/<script-name>.py  # Replace with the actual filename
```

### Run Spark Standalone and MinIO with Docker Compose

```sh
cd dockerfiles
docker compose up --scale spark-worker=3 -d
```

