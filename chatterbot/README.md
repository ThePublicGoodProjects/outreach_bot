# PGP Bot – Public Health Chatbot #

In this section, we will attempt two different ways to make our chatbot work. One, is through the [Chatterbot](https://chatterbot.readthedocs.io/en/stable/index.html) library, and the other is to attempt to train and test our own chatbot through seq2seq models.

**Most of the presented work is based on code listed below in 'Sources'**

## Sources ##
- [Practical Seq2Seq](http://suriyadeepan.github.io/2016-12-31-practical-seq2seq)
- [Tensorflow chatbot tutorial by Siraj Ravel](https://www.youtube.com/watch?v=SJDEOWLHYVo)
– [Stanford CS 20SI: Tensorflow chatbot](https://web.stanford.edu/class/cs20si/lectures/slides_13.pdf)
– [Code for scraping real time posts in Twitter](https://github.com/Marsan-Ma/twitter_scraper)
– [How I Used Deep Learning to Train a Chatbot to Talk Like Me](https://adeshpande3.github.io/How-I-Used-Deep-Learning-to-Train-a-Chatbot-to-Talk-Like-Me)
– [How to Build your own Chatbot](https://tutorials.botsfloor.com/how-to-build-your-first-chatbot-c84495d4622d)

## Datasets ##
Some common datasets are the [Cornell Movie Dialog Corpus](https://www.cs.cornell.edu/~cristian/Cornell_Movie-Dialogs_Corpus.html), the [Ubuntu corpus](http://dataset.cs.mcgill.ca/ubuntu-corpus-1.0/), and [Microsoft’s Social Media Conversation Corpus](https://www.microsoft.com/en-us/download/details.aspx?id=52375&from=http%3A%2F%2Fresearch.microsoft.com%2Fen-us%2Fdownloads%2F6096d3da-0c3b-42fa-a480-646929aa06f1%2F).

## Getting Started ##

### Pre-requisites ###

- Linux System (Ubuntu, etc)
- Python 2.7, 3.4 or 3.5
- Pandas, Numpy, Chatterbot libraries
– Tensorflow 1.0.0

### Using Chatterbot ###

Follow the steps in their [documentation](http://chatterbot.readthedocs.io/en/stable/tutorial.html) and train your bot with their corpus data. This may later be replaced with data gathered from Twitter.

```
# -*- coding: utf-8 -*-
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Uncomment the following lines to enable verbose logging
# import logging
# logging.basicConfig(level=logging.INFO)

# Create a new instance of a ChatBot
bot = ChatBot(
    "Terminal",
    storage_adapter="chatterbot.storage.SQLStorageAdapter",
    input_adapter="chatterbot.input.TerminalAdapter",
    output_adapter="chatterbot.output.TerminalAdapter",
    database="../database.db"
)

bot.set_trainer(ChatterBotCorpusTrainer)

bot.train(
    "chatterbot.corpus.english"
)
```

And use the following code to test the bot's reponse when you input something on the Terminal

```
print("Type something to begin...")

# The following loop will execute each time the user enters input
while True:
    try:
        # We pass None to this method because the parameter
        # is not used by the TerminalAdapter
        bot_input = bot.get_response(None)

    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break
```

Results are not really good. It may be because of insufficient training data

### Using Tensorflow and Seq2Seq models ###

There are some examples of Tensorflow chatbots that we can test. An interesting project is [Siraj's chatbot](https://github.com/llSourcell/tensorflow_chatbot). We tried it, but due to some dependency problems, we were not able to get it run.

Another great example is David Currie's project, where he uses the Cornell Movie Dialog Corpus to build a great chatbot. We will test his approach.

First clone his GitHub.

```
git clone https://github.com/Currie32/Chatbot-from-Movie-Dialogue
```

And make sure you are running tensorflow 1.0.0 as it won't work otherwise.

```
# in case you have a newer version, first uninstall
pip uninstall protobuf
pip uninstall tensorflow
# install for python 2.7
pip install tensorflow==1.0.0
# install for python 3.4
pip3 install tensorflow==1.0.0
```

Follow the steps on **`Chatbot_Attention.ipynb`** and start training your model with data from the [Cornell Movie Dialog Corpus][https://www.cs.cornell.edu/~cristian/Cornell_Movie-Dialogs_Corpus.html]. In our case, it's taking around 10 hours per epoch, which is too much.

Initial test are interesting, but training time needs to be considered.

## Credits ##

Developed by the [Public Good Projects](http://www.publicgoodprojects.org/).
