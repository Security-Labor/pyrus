import sys
from lark import Lark, Transformer, v_args

# Gramática Pyrus v0.1 - Adicionado suporte a Números e Expressões
pyrus_grammar = """
?start: program
program: stmt*

?stmt: var_decl | print_stmt | comment

var_decl: "var" CNAME "=" expr ";"
print_stmt: "print" "(" expr ")" ";"
comment: "//" /.*/

?expr: term
     | expr "+" term   -> add
     | expr "-" term   -> sub
     | expr "*" term   -> mul
     | expr "/" term   -> div

?term: NUMBER          -> number
     | ESCAPED_STRING  -> string
     | CNAME           -> var_ref

%import common.CNAME
%import common.NUMBER
%import common.ESCAPED_STRING
%import common.WS
%ignore WS
"""

class PyrusEvaluator(Transformer):
    def __init__(self):
        self.env = {}

    def var_decl(self, args):
        name, value = args
        self.env[str(name)] = value
        return value

    def print_stmt(self, args):
        value = args[0]
        print(f"[Pyrus Out] -> {value}")

    def number(self, n):
        return float(n[0]) if '.' in n[0] else int(n[0])

    def string(self, s):
        return str(s[0])[1:-1]

    def var_ref(self, name):
        name = str(name[0])
        if name in self.env:
            return self.env[name]
        raise NameError(f"Variável '{name}' não definida.")

    # Operações Matemáticas
    def add(self, args): return args[0] + args[1]
    def sub(self, args): return args[0] - args[1]
    def mul(self, args): return args[0] * args[1]
    def div(self, args): return args[0] / args[1]
    
    def comment(self, args): pass

parser = Lark(pyrus_grammar, start='program', parser='lalr')

def executar_codigo(codigo_fonte):
    try:
        tree = parser.parse(codigo_fonte)
        PyrusEvaluator().transform(tree)
    except Exception as e:
        print(f"❌ Erro Pyrus:\n{e}")
