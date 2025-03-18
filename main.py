from collections import Counter
import re


class TextAnlayzer:
    def __init__(self,file_name):
        self.file_name=file_name
        self.content=self._read_file()

    def _read_file(self):
        try:
            with open(self.file_name,'r',encoding='utf8') as file:
                return file.read()
        except FileNotFoundError:
            print(f"Файл '{self.file_name}' не найден!")
            return ""
    def search_by_length(self):
        text = self._read_file()
        words = text.split()
        counter = Counter(words)
        _max = max(counter,key=len)
        _min = min(counter,key=len)
        print(f'Самое длинное слово: {_max}')
        print(f'Самое короткое слово: {_min}')

    def string_and_word_counter(self):
        text=self._read_file()
        strings=text.split('\n')
        string_counter=len(strings)
        print(f'Число строк: {string_counter}')
        words = re.findall(r'\b\w+\b', text)
        word_count = len(words)
        print(f'Число слов: {word_count}')

    def symbols_counter(self):
        text=self._read_file()
        symbols_counter=len(text)
        print(f'Количество символов: {symbols_counter}')

    def frequent_words_counter(self):
        text=self._read_file()
        words=text.split()
        counter=Counter(words)
        if counter >1:
            frequent_words = counter.most_common()
            for word in frequent_words:
                print(f'Часто встречаемые слова: {word}')




file_name=input("Введите имя файла(.txt): ")
analyzer=TextAnlayzer(file_name)
print(analyzer.content)
analyzer.search_by_length()
analyzer.string_and_word_counter()
analyzer.symbols_counter()
analyzer.frequent_words_counter()
