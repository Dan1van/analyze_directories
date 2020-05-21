import ast
import os
import collections

from nltk import pos_tag


def flat_the_list(_list):
    # [(1,2), (3,4)] -> [1, 2, 3, 4]
    return sum([list(item) for item in _list], [])


def is_verb(word):
    if not word:
        return False
    pos_info = pos_tag([word])
    return pos_info[0][1] == 'VB'


def get_files(path):
    filenames = []
    for dirname, dirs, files in os.walk(path, topdown=True):
        for file in files:
            if file.endswith('.py'):
                filenames.append(os.path.join(dirname, file))
                if len(filenames) == 100:
                    break
    print(f'total {len(filenames)} files')
    return filenames


def get_trees(path):
    filenames = get_files(path)
    trees = []
    for filename in filenames:
        with open(filename, 'r', encoding='utf-8') as attempt_handler:
            main_file_content = attempt_handler.read()
        try:
            tree = ast.parse(main_file_content)
        except SyntaxError as e:
            print(e)
            tree = None
    print('trees generated')
    return trees


def get_verbs_from_function_name(function_name):
    return [word for word in function_name.split('_') if is_verb(word)]


def get_words(path, word_type='get_verbs_from_funcs'):
    trees = get_trees(path)
    function_list = [[node.name.lower() for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)]
                     for tree in trees]
    func_names = [func for func in flat_the_list(function_list)]
    if word_type == 'get_verbs_from_funcs':
        verbs = flat_the_list([get_verbs_from_function_name(function_name) for function_name in func_names])
        return verbs
    elif word_type == 'functions_names':
        return func_names
    else:
        raise Exception('Wrong word_type!')


def main():
    top_size = 10
    projects = [
        'django',
        'flask',
        'pyramid',
        'sqlalchemy'
    ]
    words = []

    for project in projects:
        print(f'{project} directory')
        path = os.path.join('.', project)
        words += get_words(path)  # you can choose word_type | можно выбрать word_type
        print('\n')

    print('total %s words, %s unique' % (len(words), len(set(words))))

    for word, entry_count in collections.Counter(words).most_common(top_size):
        print(word, entry_count)


if __name__ == '__main__':
    main()
