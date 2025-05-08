import ast

class longIfElseChecker(ast.NodeVisitor):
    def __init__(self):
        self.suggestions = []
        self.reported_starts = set()  # Track starting line numbers to avoid nested duplicates

    def visit_If(self, node):
        if node.lineno in self.reported_starts:
            return  # Already reported this chain

        chain = []
        current = node
        checked_vars = set()

        while isinstance(current, ast.If):
            condition = current.test
            if isinstance(condition, ast.Compare):
                left = condition.left
                if isinstance(left, ast.Name):
                    checked_vars.add(left.id)
                    chain.append(current.lineno)
            current = current.orelse[0] if current.orelse and isinstance(current.orelse[0], ast.If) else None

        if len(chain) >= 3 and len(checked_vars) == 1:
            var = next(iter(checked_vars))
            self.suggestions.append({
                "variable": var,
                "lines": chain,
                "message": f" Long if-elif chain on variable '{var}' at lines {chain}. Consider using polymorphism or strategy pattern."
            })
            self.reported_starts.update(chain)  # Mark these lines as already reported

        self.generic_visit(node)

    def report(self):
        if not self.suggestions:
            return ["No long if-else chains detected."]
        
        report_lines = ["Detected Long If-Else Chains:"]
        for i, s in enumerate(self.suggestions, start=1):
            lines_formatted = ', '.join(map(str, s['lines']))
            report_lines.append(
                f"  {i}. Variable: '{s['variable']}' | Lines: [{lines_formatted}]\n     Suggestion: Use polymorphism or strategy pattern."
            )
        return report_lines

def checkLongIfElse(tree):
    checker = longIfElseChecker()
    checker.visit(tree)
    return checker.report()
