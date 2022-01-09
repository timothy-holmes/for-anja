from flask import Flask, escape, request, render_template
import random, emoji

app = Flask(__name__)

@app.route('/')
def hello():
    randnum1 = random.randint(1,3) # text or emoji
    if randnum1 == 1:
        randnum2 = random.randint(1,3)
        if randnum2 == 1:
            sentence = emoji.emojize(':kiss:')
        elif randnum2 == 2:
            sentence = emoji.emojize(':smiling_face_with_heart-eyes:')
        elif randnum2 == 3:
            sentence = emoji.emojize(':thumbs_up:')
    else:
        sentence = ''
        name = ['Anja']
        verb = ['is']
        amplifier = ['crazy','fucking','heaps','so crazy',' so fucking','heaps']
        quality = ['talented','smart','kind','awesome','sensible','sexy','great']
        words = [name,verb,amplifier,quality]
        for w in words:
            sentence += w[random.randint(0,len(w)-1)] + ' '
        sentence = sentence[:-1] + '!'
    return render_template('index.html', sentence=sentence)