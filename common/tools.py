
def once(func):
    """装饰器：确保函数只执行一次"""
    executed = False
    result = None
    
    def wrapper(*args, **kwargs):
        nonlocal executed, result
        if not executed:
            result = func(*args, **kwargs)
            executed = True
        return result
    return wrapper

