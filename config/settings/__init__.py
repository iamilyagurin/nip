import environ
from pathlib import Path


env = environ.Env()

ROOT_DIR = Path(__file__).resolve(strict=True).parent.parent.parent
