import re

"""
Retriving the code blocks from the response.
"""
def extract_python_code(text):
    # 正则表达式模式，匹配 ```python[code]``` 框起来的代码
    pattern = r'```python(.*?)```'
    
    # 使用 re.findall 查找所有匹配的代码块
    matches = re.findall(pattern, text, re.DOTALL)
    
    code = '\n'.join(x for x in matches)

    return code

if __name__ == "__main__":
    response = """
who are you
```python
def a():
    return 1
```
wadasda
```python
def b():
    return 2
```
"""
    code = extract_python_code(response)
    print(code)