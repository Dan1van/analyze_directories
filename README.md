# static_analysis
Консольная утилита для статического анализа проектов github написанных на языке Python.
## Использование

``` 
console_handler.py [-h] [--part-of-speech {verbs,nouns}] 
                        [--code-element {function,variable,class}] 
                        [--output-format {csv,json,stdout}] 
                        [--source {github}] [--language {python}]
                        [--limit LIMIT]
                        URL

positional arguments:
  URL                   Ссылка на git-репозиторий

optional arguments:
  -h, --help            Показывает это сообщение и заканчивает работу утилиты.
  --part-of-speech {verbs,nouns}, --pos {verbs,nouns}, -p {verbs,nouns}
                        Части речи, которые требуется искать.
  --code-element {function,variable,class}, -c {function,variable,class}
                        Элементы кода, в которых следует производить поиск.
  --output-format {csv,json,stdout}, -o {csv,json,stdout}
                        Формат вывода.
  --source {github}, -s {github}
                        Сервис с git-репозиториями.
  --language {python}, -l {python}
                        Язык программирования.
  --limit LIMIT         Предел вывода слов.
```
____
# English
Console utility for static analysis of python project from github.
## Usage
```
console_handler.py [-h] [--part-of-speech {verbs,nouns}] 
                        [--code-element {function,variable,class}] 
                        [--output-format {csv,json,stdout}] 
                        [--source {github}] [--language {python}]
                        [--limit LIMIT]
                        URL

positional arguments:
  URL                   URL path to repository.

optional arguments:
  -h, --help            show this help message and exit
  --part-of-speech {verbs,nouns}, --pos {verbs,nouns}, -p {verbs,nouns}
                        Parts of speech that will be searched.
  --code-element {function,variable,class}, -c {function,variable,class}
                        Elements of the code in which the search will be performed.
  --output-format {csv,json,stdout}, -o {csv,json,stdout}
                        Output format.
  --source {github}, -s {github}
                        Service with git repository.
  --language {python}, -l {python}
                        Programming language.
  --limit LIMIT         Word output limit.

```