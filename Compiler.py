class SimpleCompiler:
    def __init__(self):
        self.tokens = []
        self.current_token = None
        self.position = 0

    def tokenize(self, expression):
         self.tokens = []
         i = 0
        
         while i < len(expression):
            if expression[i].isdigit():
                num = ''
                while i < len(expression) and expression[i].isdigit():
                    num += expression[i]
                    i += 1
                self.tokens.append(('NUMBER', int(num)))
            elif expression[i] in "+-*/()":
                self.tokens.append(('OPERATOR', expression[i]))
                i += 1
            else:
                i += 1  
         self.tokens.append(('EOF', None))  
    
    def get_token(self):
        if self.position < len(self.tokens):
            self.current_token = self.tokens[self.position]
            self.position += 1
        return self.current_token

    def parse_expression(self):
        value = self.parse_term()
        while self.current_token[1] in ('+', '-'):
            op = self.current_token[1]
            self.get_token()
            if op == '+':
                value += self.parse_term()
            elif op == '-':
                value -= self.parse_term()
        return value
    
    def parse_term(self):
        value = self.parse_factor()
        while self.current_token[1] in ('*', '/'):
            op = self.current_token[1]
            self.get_token()
            if op == '*':
                value *= self.parse_factor()
            elif op == '/':
                divisor = self.parse_factor()
                if divisor == 0:
                    raise ValueError("Division by zero error!")
                value /= divisor
        return value

    def parse_factor(self):
    
        if self.current_token[1] == '(':
            self.get_token()
            value = self.parse_expression()
            if self.current_token[1] == ')':
                self.get_token()
            else:
                raise ValueError("Expected ')'")
            return value
        elif self.current_token[0] == 'NUMBER':
            value = self.current_token[1]
            self.get_token()
            return value
        else:
            raise ValueError("Unexpected token")

    def evaluate(self, expression):
         self.tokenize(expression)
         self.get_token()  
         result = self.parse_expression()
         return result

compiler = SimpleCompiler()
expression = "3 + 5 * (2 - 8)"
result = compiler.evaluate(expression)
print(f"Result of '{expression}' is {result}")
