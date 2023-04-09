from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
# from dotenv import load_dotenv
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
import os
import openai

# load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")



app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


base_prompt = '''
Here are the 4 houses:

spectreseek: - people who are ambitious and will get stuff done
alterok: - people who are clever and methodical about their thinking and work
gaudmire: - people who are very optimistic and cheerful
erevald: - people who patient and very easygoing

this is the questionnaire given to users
question 1:
When given a task, do you prefer to dive right in or carefully plan your approach?

question 2:
How do you handle setbacks or failures?

question 3:
Would you describe yourself as more of a leader or a team player?

question 4:
Which of the following qualities do you value most in others: ambition, intelligence, optimism, or patience?

question 5:
How do you typically handle stress or pressure?

Based on my answers decide the correct house. only return the house's name enclosed in square brackets.

'''

from pydantic import BaseModel
class Answers(BaseModel):
    question1: str
    question2: str
    question3: str
    question4: str
    question5: str

@app.post("/api/reccomendation")
def read_root(answers: Answers):
    answers = answers.dict()
    answer_text = ""
    for k,v in answers.items():
        answer_text += f"{k}: {v}"
    p = base_prompt + answer_text
    response = openai.Completion.create(
        model='text-davinci-003',
        prompt=p,
        temperature=0.9,
        max_tokens=20)
    print(response.choices[0].text)
    return response.choices[0].text

app.mount("/static", StaticFiles(directory="web"), name="static")

# @app.get('/')
# def index():
#     return FileResponse('web/index.html')
@app.get("/")
def index():
    # redirect to static
    return RedirectResponse(url="/static/index.html")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
    # return index.html from frotend


