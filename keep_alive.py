from flask import Flask
from threading import Thread
from random import randint


app = Flask('')

@app.route('/')
def home():
  return '<code>Bot is ready to rock and roll</code>'

  def run():
    app.run(
      host='0.0.0.0',
      port=randint=(2000,9000)
    )

def keep_alive():
  '''
  Creates and starts a new thread that run the function `run`
  '''
  t = Thread(target=run)
  t.start()