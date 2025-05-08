from analyzer.parser import parse_code
from analyzer.rules.unused_vars import check_unused_vars
from analyzer.rules.longMethod import longFunction
from analyzer.rules.longCondition import checkLongIfElse


def analyze(code: str):
    tree=parse_code(code)
    if not tree:
        return
    suggestions=[]

    suggestions+=check_unused_vars(tree) or []
    suggestions+=longFunction(tree) or []
    suggestions+=checkLongIfElse(tree) or []
    return suggestions
def analyze_code(filePath):
    with open(filePath, 'r') as f:
        code = f.read()
    suggestions = analyze(code)
    for s in suggestions:
        print('[Suggestions]', s)

if __name__=="__main__":
    analyze('test_samples/sample1.py')
    

    
