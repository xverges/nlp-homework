# The Making-Of a language detection test

## Goals

My goal is to have some tests driving the Watson language detection API
and another not as-a-Service API. A side effect should be to start
bringing back some of my long-forgotten Python fluency.

## TDD + Data Driven Tests

I am a believer on TDD/BDD. And the problem at hand calls for some kind of
data driven tests. Some googling on Python Data Driven Tests 
(<http://defragdev.com/blog/?p=660>) reminds me that I used to like nose,
even if I know nothing about it nowadays.  Looks like nose is too old, and
that I should be using
[nose2](https://nose2.readthedocs.io/en/latest/getting_started.html).
But, wait, <https://github.com/wolever/nose-parameterized>, does not rely
on nose.

## Dependencies?

Coming from the comfort of node.js `package.json` and `npm install` I NEED
to specify my project dependencies! How is this done nowadays in Python? 

[pip FTW!](http://stackoverflow.com/a/31753111/239408)

## Project structure + interface

I don't want to look messy, so some googling again.
[What is the best project structure for a Python application?](http://stackoverflow.com/a/3419951/239408)

Also worth a quick look at the two interfaces I want to be using, so
I know what is a sensible interface for library that relies on them.

### Watson

<https://www.ibm.com/watson/developercloud/alchemy-language/api/v1/?python#language>
`alchemy_language.language(text='blah blah blah')` returns a JSON object. The response
does not involve any confidence/probability index.

### Other APIs

From stackoverflow's [NLTK and language detection](http://stackoverflow.com/questions/3182268/nltk-and-language-detection), some candidates

* nltk.detect. Although I should be looking into this, I under the impression
  that getting started with ntlk will involve some yack shaving.
* <https://pypi.python.org/pypi/langdetect>. Apache License. `detect('blah')` returns
  a language-id while `detect_languages('blah')` returns ids+probabilities.
* <https://github.com/saffsd/langid.py>. BSD License. `langid.classify("blah")` returns
  id+probability. Has training capabilities and you can limit the number of
  languages it considers. I am going to go for this one.

## At last, ready for a commit!

Some dummy tests, and my first commit!

## Let's bring in `langid`

```
>pip install langid
>pip freeze > requirements.txt
>less requirements.txt
colorama==0.3.3
decorator==4.0.9
httpie==0.9.2
ipython==4.1.1
ipython-genutils==0.1.0
keyring==5.3
langid==1.1.6
numpy==1.11.3
path.py==8.1.2
pickleshare==0.6
PyAudio==0.2.9
Pygments==2.0.2
pyreadline==2.1
requests==2.9.1
simplegeneric==0.8.1
SpeechRecognition==3.3.0
traitlets==4.1.0
```

Wow! PyAudio? SpeechRecognition?

But I can write actual code!

## Argh! 

* My first Spanish sentence has been identified as Italian. Not nice.
* When I try to add a 'ñ', so that it is super obvious that this is Spanish,
  Python gets upset.

## Two working tests!

After adding a comment in the first lines specifying UTF-8 encoding,
I have two working tests. Time for my second happy commit.

## Let's try data-driven-tests

Just a taste of how `nose_parameterized` works.

Watson is missing, my googling about project structure and thinking about
a facade to hide the different APIs was probably YAGNI, but it looks like
my third commit will be of a "minimum viable homework"!

