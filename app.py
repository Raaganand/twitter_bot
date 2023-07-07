
from flask import Flask, render_template, request
import tweepy
import openai
import os


app = Flask(__name__)
# Your Twitter API configuration code here

consumer_key = "5mNygPAwvs5xu7EPuACotb4IJ"
consumer_secret = "XE5xv79P6KKh0FhzYcFFwivOxhWOADwqDEJdxnm1KYUL1yyB8W"
access_token = "1511705726770679814-pD81MYYiiTNBLNzvyarZEBlkNa60j0"
access_token_secret = "aBbuqSOJDuUO3whtyJicE95PuhJEMBUFeeO2uQj7VY1lf"
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_tweet', methods=['POST'])
def generate_tweet():
    prompt = request.form['prompt']

    # Generate a tweet using the OpenAI API
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.7
    )
    generated_tweet = response.choices[0].text.strip()

    # Post the generated tweet using the Twitter API
    api.update_status(generated_tweet)

    return "Tweet posted successfully!"

if __name__ == '__main__':
    app.run()