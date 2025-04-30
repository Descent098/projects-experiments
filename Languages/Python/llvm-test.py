import ast
import inspect

class CompileError(Exception):
    pass

class Compiler(ast.NodeTransformer):
    @classmethod
    def compile(cls, function):
        try:
            source = inspect.getsource(function)
            compiler = cls()
            function_ast = ast.parse(source)
            llvm_ir = compiler.visit(function_ast)

        except OSError:
            return function
        except CompileError:
            return function