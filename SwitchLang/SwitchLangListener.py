# Generated from SwitchLang.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .SwitchLangParser import SwitchLangParser
else:
    from SwitchLangParser import SwitchLangParser

# This class defines a complete listener for a parse tree produced by SwitchLangParser.
class SwitchLangListener(ParseTreeListener):

    # Enter a parse tree produced by SwitchLangParser#query.
    def enterQuery(self, ctx:SwitchLangParser.QueryContext):
        pass

    # Exit a parse tree produced by SwitchLangParser#query.
    def exitQuery(self, ctx:SwitchLangParser.QueryContext):
        pass


    # Enter a parse tree produced by SwitchLangParser#column_list.
    def enterColumn_list(self, ctx:SwitchLangParser.Column_listContext):
        pass

    # Exit a parse tree produced by SwitchLangParser#column_list.
    def exitColumn_list(self, ctx:SwitchLangParser.Column_listContext):
        pass


    # Enter a parse tree produced by SwitchLangParser#column.
    def enterColumn(self, ctx:SwitchLangParser.ColumnContext):
        pass

    # Exit a parse tree produced by SwitchLangParser#column.
    def exitColumn(self, ctx:SwitchLangParser.ColumnContext):
        pass


    # Enter a parse tree produced by SwitchLangParser#table.
    def enterTable(self, ctx:SwitchLangParser.TableContext):
        pass

    # Exit a parse tree produced by SwitchLangParser#table.
    def exitTable(self, ctx:SwitchLangParser.TableContext):
        pass


    # Enter a parse tree produced by SwitchLangParser#condition.
    def enterCondition(self, ctx:SwitchLangParser.ConditionContext):
        pass

    # Exit a parse tree produced by SwitchLangParser#condition.
    def exitCondition(self, ctx:SwitchLangParser.ConditionContext):
        pass


    # Enter a parse tree produced by SwitchLangParser#operator.
    def enterOperator(self, ctx:SwitchLangParser.OperatorContext):
        pass

    # Exit a parse tree produced by SwitchLangParser#operator.
    def exitOperator(self, ctx:SwitchLangParser.OperatorContext):
        pass


    # Enter a parse tree produced by SwitchLangParser#value.
    def enterValue(self, ctx:SwitchLangParser.ValueContext):
        pass

    # Exit a parse tree produced by SwitchLangParser#value.
    def exitValue(self, ctx:SwitchLangParser.ValueContext):
        pass



del SwitchLangParser