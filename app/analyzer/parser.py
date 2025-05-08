import ast

def parse_code(source_code: str):
    try:
        return ast.parse(source_code)
    except SyntaxError as e:
        print(f"Syntax error in  code:{e}")
        return None
