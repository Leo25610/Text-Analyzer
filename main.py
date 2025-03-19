from collections import Counter
import re


class TextAnalyzer:
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
        if counter :
            max_count = counter.most_common(1)[0][1]
            frequent_words = [word for word,count in counter.items() if count==max_count]
            print(f'Часто встречаемые слова: {','.join(frequent_words)}')

    def unique_word(self):
        text=self._read_file()
        words=text.split()
        counter=Counter(words)
        unique_words=[word for word,count in counter.items() if count == 1]
        print(f'Слово встречающаеся один раз: {', '.join(unique_words)}')


class NumbersAnalyzer:
    def __init__(self,file_name):
        self.file_name = file_name
        self.content = self._read_file()

    def _read_file(self):
        try:
            with open(self.file_name,'r',encoding='utf8') as file:
                return file.read()
        except FileNotFoundError:
            print(f"Файл '{self.file_name}' не найден!")
            return ""


    def is_number_file(self):
        return all(word.isdigit() for word in self.content.split())


    def max_min_numbers(self):
        text=self._read_file()
        numbers=text.split()
        counter=Counter(numbers)
        _max=max(map(int,counter.keys()))
        _min=min(map(int,counter.keys()))
        print(f'Максимальное число: {_max}')
        print(f'Минимальное число: {_min}')


    def sum_numbers_counter(self):
        text=self._read_file()
        numbers=text.split()
        counter=Counter(numbers)
        num_sum = sum(int(num) * count for num,count in counter.items() if num.isdigit())
        print(f'Сумма чисел в файле: {num_sum}')

    def custom_number_search(self, position):
        text = self._read_file()
        numbers = list(map(int, text.split()))
        unique_numbers = sorted(set(numbers), reverse=True)

        if 0 < position <= len(unique_numbers):
            print(f"{position}-е по величине число: {unique_numbers[position - 1]}")
        else:
            print("Ошибка: заданный параметр выходит за границы доступных чисел.")
    def average_num(self):
        text=self._read_file()
        numbers=[int(num) for num in text.split() if num.isdigit()]
        if numbers:
            average_num=sum(numbers)/len(numbers)
            print(f'Средне арифмитическое: {average_num}')
        else:
            print("В файле нет чисел!")



file_name=input("Введите имя файла(.txt): ")
content = open(file_name, 'r', encoding='utf8').read()

if all(word.isdigit() for word in content.split()):
    analyzer = NumbersAnalyzer(file_name)
    analyzer.max_min_numbers()
    analyzer.sum_numbers_counter()
    position = int(input("Введите порядковый номер величины который вы хотите найти(2-ое по величине число): "))
    analyzer.custom_number_search(position)
    analyzer.average_num()

else:
    analyzer = TextAnalyzer(file_name)
    analyzer.search_by_length()
    analyzer.string_and_word_counter()
    analyzer.symbols_counter()
    analyzer.frequent_words_counter()
    analyzer.unique_word()