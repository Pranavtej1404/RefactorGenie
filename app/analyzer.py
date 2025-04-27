import ast

class RefactorSuggestor(ast.NodeVisitor):

    def __init__(self):
        self.suggestions = []
    def visit_For(self, node):
        if isinstance(node.body[0], ast.Expr) and isinstance(node.body[0].value, ast.Call):
            self.suggestions.append({
                "line": node.lineno,
                "type": "Refactor",
                "message": "Consider using a list comprehension if possible."
            })
        self.generic_visit(node)

def analyze_code(code):
    tree=ast.parse(code)
    sugester=RefactorSuggestor()
    sugester.visit(tree)
    return sugester.suggestions