# Generated from C:/Users/Frrn/PycharmProjects/CompilerChomin_py\MiLenguaje.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MiLenguajeParser import MiLenguajeParser
else:
    from MiLenguajeParser import MiLenguajeParser

# This class defines a complete generic visitor for a parse tree produced by MiLenguajeParser.

class MiLenguajeVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MiLenguajeParser#start.
    def visitStart(self, ctx:MiLenguajeParser.StartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiLenguajeParser#statement.
    def visitStatement(self, ctx:MiLenguajeParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiLenguajeParser#condition.
    def visitCondition(self, ctx:MiLenguajeParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiLenguajeParser#action.
    def visitAction(self, ctx:MiLenguajeParser.ActionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiLenguajeParser#expression.
    def visitExpression(self, ctx:MiLenguajeParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiLenguajeParser#expression_print.
    def visitExpression_print(self, ctx:MiLenguajeParser.Expression_printContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiLenguajeParser#arithmeticExpression.
    def visitArithmeticExpression(self, ctx:MiLenguajeParser.ArithmeticExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiLenguajeParser#additiveExpression.
    def visitAdditiveExpression(self, ctx:MiLenguajeParser.AdditiveExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiLenguajeParser#multiplicativeExpression.
    def visitMultiplicativeExpression(self, ctx:MiLenguajeParser.MultiplicativeExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiLenguajeParser#assignmentExpression.
    def visitAssignmentExpression(self, ctx:MiLenguajeParser.AssignmentExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiLenguajeParser#primaryExpression.
    def visitPrimaryExpression(self, ctx:MiLenguajeParser.PrimaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiLenguajeParser#variableDeclaration.
    def visitVariableDeclaration(self, ctx:MiLenguajeParser.VariableDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiLenguajeParser#assignment.
    def visitAssignment(self, ctx:MiLenguajeParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiLenguajeParser#variable.
    def visitVariable(self, ctx:MiLenguajeParser.VariableContext):
        return self.visitChildren(ctx)



del MiLenguajeParser