import ast
import os
import re

def split_words(text: str) -> list:
    if not text or text == "null": return []
    clean = re.sub('([A-Z])', r' \1', text).replace('_', ' ')
    return [p.lower() for p in clean.split() if len(p) > 2]

def file_analyze(path: str) -> list:
    try:
        with open(path, 'r', encoding='utf-8') as f:
            tree = ast.parse(f.read())
        
        word = []
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                word.extend(split_words(node.name))
        return word
    except:
        return []

def process_directory(dir_path: str) -> list:
    words = []
    for root, _, files in os.walk(dir_path):
        for file in files:
            if file.endswith('.py') or file.endswith('.java'):
                full_path = os.path.join(root, file)
                words.extend(file_analyze(full_path))
    return words
    