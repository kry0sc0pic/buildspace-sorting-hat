<img src="demo/buildspace-logo.png">

# buildspace house sorter
### (unofficial) house sorter for [buildspace](https://buildspace.so) powered by gpt3


![](https://img.shields.io/static/v1?label=DEPLOYED%20ON&message=RAILWAY&color=blueviolet&style=for-the-badge&logo=railway)
![](https://img.shields.io/static/v1?label=python&message=3.11&color=blue&style=for-the-badge&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Flutter](https://img.shields.io/badge/Flutter-%2302569B.svg?style=for-the-badge&logo=Flutter&logoColor=white)

---
## Demo
[![house sorter demo](https://cdn.loom.com/sessions/thumbnails/e54af3169bdd42a2b7b2ebe27fc0df6e-with-play.gif)](https://www.loom.com/share/e54af3169bdd42a2b7b2ebe27fc0df6e "house sorter demo")


## future
- better questions & more detailed house descriptions for gpt3



## setup
### 1) setup virtual environment
```bash
virtualenv venv
```

### 2) install dependencies
```bash
pip install -r requirements.txt
```



### 3) configure openai api key
- create `.env` file
- add a new variable `OPENAI_API_KEY` and add in your api key
```env
OPENAI_API_KEY="sk-Ac....G0U"
```
### 4) uncomment line `4` and line `10` in `main.py` 

### 5) start server
```bash
python main.py
```
### open `http://localhost:8000/` in your browser

## frontend source
### available at [kry0s0cpic/buildspace-sorting-hat-frontend](https://github.com/kry0sc0pic/buildspace-sorting-hat-frontend)
## license
### GNU AGPLv3