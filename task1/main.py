from fastapi import FastAPI
app = FastAPI()

@app.get("/")
#async def json_response(slackUsername: str , backend: bool, age: int, bio: str):
async def json_response():
  slackUsername = 'chuchuN' 
  #backend = 'YES' 
  #age = 32 
  bio = 'ex-ronin, seeking ἄλφα'

  #return {print(slackUsername, backend, age, bio)}
  return {'slackUsername': slackUsername, "backend": bool('YES'), "age": int('32'), "bio": bio}

