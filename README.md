# for_anja
Anja was having a bad day, and I was experimenting with flask. I thought this random compliment generator might cheer her up, albeit briefly. Yeah, I'm a dork...

When the index page is requested, Flask serves up this function. The index page contains an instruction to refresh every 3 seconds.

Hosted here: https://timothyholmes.com.au/for_anja

```python
def hello():
    randnum1 = random.randint(1,3) # text or emoji
    if randnum1 == 1:
        emojis = [':kiss:',':smiling_face_with_heart-eyes:,':thumbs_up:']
        randnum2 = random.randint(0,2)
        sentence = emoji.emojize(randnum2)
    else:
        name = ['Anja']
        verb = ['is']
        amplifier = ['crazy','fucking','heaps','so crazy',' so fucking','heaps']
        quality = ['talented','smart','kind','awesome','sensible','sexy','great']
        words = [name,verb,amplifier,quality]
        sentence = ''
        for w in words:
            sentence += w[random.randint(0,len(w)-1)] + ' '
        sentence = sentence[:-1] + '!'
    return render_template('index.html', sentence=sentence)
```

The next step in experiementation would have been to refactor the app into a compliment generator microservice and a page that repeats a single GET request.
