class FeatureLogicParser:
    def __init__(self, expression):
        """初始化解析器，处理表达式"""
        self.expression = expression.replace(" ", "")  # 移除所有空格
        self.pos = 0  # 当前解析位置
        self.len = len(self.expression)
        self.current_char = self.expression[self.pos] if self.len > 0 else None

    def _advance(self):
        """移动到下一个字符"""
        self.pos += 1
        if self.pos < self.len:
            self.current_char = self.expression[self.pos]
        else:
            self.current_char = None

    def _parse_feature(self):
        """解析特征名（如featureA、featureB）"""
        feature = []
        # 特征名由字母和数字组成，必须以字母开头
        if not self.current_char.isalpha():
            raise SyntaxError(f"无效的特征名开头: {self.current_char} 在位置 {self.pos}")
            
        while self.current_char and (self.current_char.isalnum() or self.current_char == '_'):
            feature.append(self.current_char)
            self._advance()
            
        return ''.join(feature)

    def _parse_factor(self):
        """解析因子（特征或带括号的表达式）"""
        if self.current_char == '(':
            self._advance()  # 跳过 '('
            expr = self._parse_expression()
            if self.current_char != ')':
                raise SyntaxError(f"缺少右括号，在位置 {self.pos}")
            self._advance()  # 跳过 ')'
            return expr
        elif self.current_char.isalpha():
            # 解析特征名
            feature_name = self._parse_feature()
            return {'type': 'feature', 'name': feature_name}
        else:
            raise SyntaxError(f"意外字符: {self.current_char} 在位置 {self.pos}")

    def _parse_and_terms(self):
        """解析与运算（&），优先级高于或运算"""
        node = self._parse_factor()
        
        while self.current_char == '&':
            self._advance()  # 跳过 '&'
            right = self._parse_factor()
            node = {'type': 'and', 'left': node, 'right': right}
            
        return node

    def _parse_expression(self):
        """解析或运算（|），优先级最低"""
        node = self._parse_and_terms()
        
        while self.current_char == '|':
            self._advance()  # 跳过 '|'
            right = self._parse_and_terms()
            node = {'type': 'or', 'left': node, 'right': right}
            
        return node

    def parse(self):
        """解析表达式并返回抽象语法树(AST)"""
        ast = self._parse_expression()
        if self.current_char is not None:
            raise SyntaxError(f"表达式末尾有意外字符: {self.current_char}")
        return ast


def evaluate_feature_expression(ast, feature_values):
    """
    计算特征逻辑表达式的结果
    :param ast: 由FeatureLogicParser生成的抽象语法树
    :param feature_values: 字典，包含特征名到布尔值的映射
    :return: 表达式的布尔结果
    """
    if ast['type'] == 'feature':
        # 获取特征值，不存在的特征默认视为False
        return feature_values.get(ast['name'], False)
    elif ast['type'] == 'and':
        return (evaluate_feature_expression(ast['left'], feature_values) and 
                evaluate_feature_expression(ast['right'], feature_values))
    elif ast['type'] == 'or':
        return (evaluate_feature_expression(ast['left'], feature_values) or 
                evaluate_feature_expression(ast['right'], feature_values))
    else:
        raise ValueError(f"未知的节点类型: {ast['type']}")


def EvaluateFeatureDsl(expression, featureValues):
    parser = FeatureLogicParser(expression)
    ast = parser.parse()
    result = evaluate_feature_expression(ast, featureValues)
    return result

if __name__ == "__main__":
    # 测试表达式
    test_expressions = [
        "featureA&featureB",
        "featureA|featureB",
        "featureA&(featureB|featureC)",
        "(featureA|featureB)&featureC",
        "featureX|(featureY&featureZ)",
        "feature1&(feature2|(feature3&feature4))"
    ]
    
    # 特征值字典
    feature_states = {
        'featureA': True,
        'featureB': False,
        'featureC': True,
        'featureX': False,
        'featureY': True,
        'featureZ': True,
        'feature1': True,
        'feature2': False,
        'feature3': True,
        'feature4': True
    }
    
    # 解析并计算每个表达式
    for expr in test_expressions:
        try:
            parser = FeatureLogicParser(expr)
            ast = parser.parse()
            result = evaluate_feature_expression(ast, feature_states)
            print(f"表达式: {expr}")
            print(f"计算结果: {result}\n")
        except SyntaxError as e:
            print(f"解析错误 ({expr}): {e}\n")