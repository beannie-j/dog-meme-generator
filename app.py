import random
import os
import requests
from flask import Flask, render_template, abort, request

from meme.memeEngine import MemeEngine
from models.quoteModel import QuoteModel
from ingestors import Ingestor


app = Flask(__name__)

meme = MemeEngine('./static')


def setup():
    # @TODO: need to fix txt and pdf
    # quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
    #                './_data/DogQuotes/DogQuotesDOCX.docx',
    #                './_data/DogQuotes/DogQuotesPDF.pdf',
    #                './_data/DogQuotes/DogQuotesCSV.csv']

    quote_files = [
        './_data/DogQuotes/DogQuotesDOCX.docx',
        './_data/DogQuotes/DogQuotesCSV.csv']

    quotes = []
    for file in quote_files:
        try:
            quotes.extend(Ingestor.parse(file))
        except ValueError as error:
            print(f"ValueError: {error}")

    images_path = "./_data/photos/dog/"

    imgs = []
    for root, dir, files in os.walk(images_path):
        imgs = [os.path.join(root, name) for name in files]

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    img = random.choice(imgs)
    quote = random.choice(quotes)
    print("generated", quote.body, quote.author)
    path = meme.make_meme(img, quote.body, quote.author)
    print("path", path)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    # @TODO:
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """ Create a user defined meme """

    # @TODO:

    path = None

    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
