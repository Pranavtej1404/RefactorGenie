import ast

class UnusedVariableChecker(ast.NodeVisitor):
    def __init__(self):
        self.assigned=set()
        self.used=set()
        self.suggestions=[]
    
    def visit_Assign(self, node):
        for target in node.targets:
            if isinstance(target,ast.Name):
                self.assigned.add(target.id)
        self.generic_visit(node)
    def visit_Name(self, node):
        if isinstance(node.ctx,ast.Load):
            self.used.add(node.id)
    def report(self):
        unused=self.assigned-self.used
        for var in unused:
            self.suggestions.append(f"Variable '{var}' is never used" )
        return self.suggestions
def check_unused_vars(tree):
    checker=UnusedVariableChecker()
    checker.visit(tree)
    return checker.report()
