import ast
from . import redundentCode  # This must be in the same folder or on the PYTHONPATH

class longfuntionChecker(ast.NodeVisitor):
    def __init__(self):
        self.longFunctions = []
        self.suggestion = []

    def visit_FunctionDef(self, node):
        start_line = node.lineno
        end_line = self.endLineNo(node)
        function_length = end_line - start_line + 1

        if function_length > 20:
            self.longFunctions.append((node.name, function_length, start_line, node))

    def endLineNo(self, node):
        end_line = node.lineno
        for child in ast.walk(node):
            if hasattr(child, 'lineno'):
                end_line = max(end_line, child.lineno)
        return end_line

    def report(self):
        rCode = []
        for i, f in enumerate(self.longFunctions):
            redundant = redundentCode.redundentpattern(f[3])
            rCode.append((f[0], redundant))  # Use function name instead of index

        messages = []
        if self.longFunctions:
            long_fn_names = [f[0] for f in self.longFunctions]
            messages.append(f"[Long Functions] {', '.join(long_fn_names)}")

        for func_name, redundants in rCode:
            if redundants:
                messages.append(f"[Redundancy] In '{func_name}':")
                for hash_val, locs in redundants:
                    lines = [f"{fname} @ line {lineno}" for fname, lineno in locs]
                    messages.append(f"  → Repeated block at: {', '.join(lines)}")

        return messages


def longFunction(tree):
    checker = longfuntionChecker()
    checker.visit(tree)
    return checker.report()
