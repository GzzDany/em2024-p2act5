import ast
import inspect

def count_comparisons(func):
    tree = ast.parse(inspect.getsource(func))
    boolean_count = sum([1 for node in ast.walk(tree) if isinstance(node, ast.Compare)])
    assert boolean_count <= 2, "Your function uses more than two comparison statements! In order to get full points, you should ensure you're properly using dictionaries!" 
    return 
