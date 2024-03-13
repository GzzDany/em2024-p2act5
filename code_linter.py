def count_comparisons(func):
    tree = ast.parse(inspect.getsource(func))
    boolean_count = sum([1 for node in ast.walk(tree) if isinstance(node, ast.Compare)])
    return boolean_count
