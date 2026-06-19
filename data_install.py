import kagglehub
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

path = Path.cwd().resolve() / "data"
path.mkdir(parents=False,exist_ok=True)

if __name__=="__main__":
    print(path)
    kagglehub.competition_download('playground-series-s6e6')