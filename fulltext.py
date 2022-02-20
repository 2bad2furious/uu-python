import os.path
from typing import Iterable

import more_itertools


class Article:
    def __init__(self, id: str, title: str, text: str):
        self.id = id
        self.title = title
        self.text = text

    def words(self) -> Iterable[str]:
        for words in [self.id, self.title, self.text]:
            for word in words.split(" "):
                yield word

    def __str__(self):
        return self.id + ":" + self.title


Index = dict[str, set[Article]]


def create_index(articles: Iterable[Article]) -> Index:
    index: Index = {}
    for a in articles:
        for word in a.words():
            if word not in index:
                index[word] = set()

            index[word].add(a)
    return index


def parse_chunk(chunk: [str, str, str]) -> Article:
    return Article(chunk[0], chunk[1] if 1 in chunk else "", chunk[2] if 2 in chunk else "")


def parse_articles(path: str) -> Iterable[Article]:
    with open(path, "r") as f:
        lines = f.readlines()
        lines_fixed = map(lambda line: line[:-1], lines)
        chunks = more_itertools.chunked(lines_fixed, 3)
        return map(parse_chunk, chunks)


def search(index: Index, *terms: str) -> set[Article]:
    result: set[Article] = set()
    for term in terms:
        if term in index:
            for article in index[term]:
                result.add(article)
    return result


if __name__ == '__main__':
    articles = parse_articles(os.path.join(os.path.dirname(__file__), "db.txt"))
    index = create_index(articles)
    print("\n".join(map(str, search(index, "plastic"))))
