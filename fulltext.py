import os.path
import re
from typing import Iterable

import more_itertools

letter_patten = re.compile("[\w]+")


class WordWithIndex:

    def __init__(self, word: str, pos: int):
        self.word = word
        self.pos = pos


class Article:
    def __init__(self, id: str, title: str, text: str):
        self.id = id
        self.title = title
        self.text = text

    def words(self) -> Iterable[WordWithIndex]:
        buffer = ''
        for (i, ch) in enumerate(self.text):
            if ch != ' ' and letter_patten.match(ch):
                buffer += ch
            elif buffer != '':
                yield WordWithIndex(buffer, i - len(buffer))
                buffer = ''

    def __str__(self):
        return self.id + ": " + self.title


class ArticleWithIndex:

    def __init__(self, article: Article, pos: int):
        self.article = article
        self.pos = pos


Index = dict[str, set[ArticleWithIndex]]


def create_index(articles: Iterable[Article]) -> Index:
    index: Index = {}
    for a in articles:
        for w in a.words():
            print(w)
            if w.word not in index:
                index[w.word] = set()

            index[w.word].add(ArticleWithIndex(a, w.pos))
    return index


def parse_chunk(chunk: [str, str, str]) -> Article:
    l = len(chunk)
    return Article(chunk[0], chunk[1] if l > 1 else "", chunk[2] if l > 2 else "")


def parse_articles(path: str) -> Iterable[Article]:
    with open(path, "r") as f:
        lines = f.readlines()
        lines_fixed = map(lambda line: line[:-1], lines)
        chunks = more_itertools.chunked(lines_fixed, 3)
        return map(parse_chunk, chunks)


def search(index: Index, *terms: str) -> dict[str, set[ArticleWithIndex]]:
    result: dict[str, set[ArticleWithIndex]] = {}
    for term in terms:
        result[term] = set()
        if term in index:
            for article in index[term]:
                result[term].add(article)
    return result


if __name__ == '__main__':
    chars = 20
    articles = parse_articles(os.path.join(os.path.dirname(__file__), "db.txt"))
    index = create_index(articles)
    for word, result in search(index, "kokos", "plastic", "start").items():
        if result:
            print(f"Results for {word}:")
            print("\t" + "\n\t".join(map(lambda
                                             a: f"{a.article} \n\t\t{a.article.text[a.pos:len(word) + a.pos + chars]}",
                                         result)))
        else:
            print(f"No results for {word}")
