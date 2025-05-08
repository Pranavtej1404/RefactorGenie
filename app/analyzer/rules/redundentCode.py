import ast
import hashlib
from collections import defaultdict

class redundentCodeChecker(ast.NodeVisitor):
    def __init__(self):
        self.hash_map = defaultdict(list)
        self.suggestions = []

    def extract_sequences(self, statements):
        for i in range(len(statements) - 1):  # Use 2-statement window
            if isinstance(statements[i], ast.Expr) and isinstance(statements[i].value, ast.Str):
                continue
            seq = statements[i:i + 2]
            seq_str = ast.dump(ast.Module(body=seq, type_ignores=[]))
            seq_hash = hashlib.md5(seq_str.encode()).hexdigest()
            self.hash_map[seq_hash].append((self.current_func, statements[i].lineno))


    def visit_FunctionDef(self, node):
        self.current_func = node.name
        self.extract_sequences(node.body)
        for stmt in node.body:
            if hasattr(stmt, 'body') and isinstance(stmt.body, list):
                self.extract_sequences(stmt.body)
        self.generic_visit(node)


    def getRedundentSeq(self):
        return {
            h: locs for h, locs in self.hash_map.items()
            if len(locs) > 1
        }

    def report(self):
        redundent_blocks = self.getRedundentSeq()
        for hash_val, locations in redundent_blocks.items():
            self.suggestions.append((hash_val, locations))
        return self.suggestions

def redundentpattern(tree):
    checker = redundentCodeChecker()
    checker.visit(tree)
    return checker.report()
