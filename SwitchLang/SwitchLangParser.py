# Generated from SwitchLang.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,29,48,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,1,0,1,0,1,0,1,0,1,0,1,0,3,0,21,8,0,1,0,1,0,1,1,1,1,1,1,1,1,5,1,
        29,8,1,10,1,12,1,32,9,1,3,1,34,8,1,1,2,1,2,1,3,1,3,1,4,1,4,1,4,1,
        4,1,5,1,5,1,6,1,6,1,6,0,0,7,0,2,4,6,8,10,12,0,2,2,0,12,14,27,29,
        1,0,19,20,43,0,14,1,0,0,0,2,33,1,0,0,0,4,35,1,0,0,0,6,37,1,0,0,0,
        8,39,1,0,0,0,10,43,1,0,0,0,12,45,1,0,0,0,14,15,5,22,0,0,15,16,3,
        2,1,0,16,17,5,23,0,0,17,20,3,6,3,0,18,19,5,24,0,0,19,21,3,8,4,0,
        20,18,1,0,0,0,20,21,1,0,0,0,21,22,1,0,0,0,22,23,5,16,0,0,23,1,1,
        0,0,0,24,34,5,25,0,0,25,30,3,4,2,0,26,27,5,26,0,0,27,29,3,4,2,0,
        28,26,1,0,0,0,29,32,1,0,0,0,30,28,1,0,0,0,30,31,1,0,0,0,31,34,1,
        0,0,0,32,30,1,0,0,0,33,24,1,0,0,0,33,25,1,0,0,0,34,3,1,0,0,0,35,
        36,5,18,0,0,36,5,1,0,0,0,37,38,5,18,0,0,38,7,1,0,0,0,39,40,3,4,2,
        0,40,41,3,10,5,0,41,42,3,12,6,0,42,9,1,0,0,0,43,44,7,0,0,0,44,11,
        1,0,0,0,45,46,7,1,0,0,46,13,1,0,0,0,3,20,30,33
    ]

class SwitchLangParser ( Parser ):

    grammarFileName = "SwitchLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'if'", "'else'", "'('", "')'", "'{'", 
                     "'}'", "'='", "'+'", "'-'", "'*'", "'/'", "'>'", "'<'", 
                     "'=='", "'!='", "';'", "':'" ]

    symbolicNames = [ "<INVALID>", "IF", "ELSE", "LPAREN", "RPAREN", "LBRACE", 
                      "RBRACE", "ASSIGN", "PLUS", "MINUS", "MUL", "DIV", 
                      "GT", "LT", "EQ", "NEQ", "SEMI", "SEMA", "IDENTIFIER", 
                      "NUMBER", "STRING", "WS", "SELECT", "FROM", "WHERE", 
                      "STAR", "COMMA", "GE", "LE", "NE" ]

    RULE_query = 0
    RULE_column_list = 1
    RULE_column = 2
    RULE_table = 3
    RULE_condition = 4
    RULE_operator = 5
    RULE_value = 6

    ruleNames =  [ "query", "column_list", "column", "table", "condition", 
                   "operator", "value" ]

    EOF = Token.EOF
    IF=1
    ELSE=2
    LPAREN=3
    RPAREN=4
    LBRACE=5
    RBRACE=6
    ASSIGN=7
    PLUS=8
    MINUS=9
    MUL=10
    DIV=11
    GT=12
    LT=13
    EQ=14
    NEQ=15
    SEMI=16
    SEMA=17
    IDENTIFIER=18
    NUMBER=19
    STRING=20
    WS=21
    SELECT=22
    FROM=23
    WHERE=24
    STAR=25
    COMMA=26
    GE=27
    LE=28
    NE=29

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class QueryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SELECT(self):
            return self.getToken(SwitchLangParser.SELECT, 0)

        def column_list(self):
            return self.getTypedRuleContext(SwitchLangParser.Column_listContext,0)


        def FROM(self):
            return self.getToken(SwitchLangParser.FROM, 0)

        def table(self):
            return self.getTypedRuleContext(SwitchLangParser.TableContext,0)


        def SEMI(self):
            return self.getToken(SwitchLangParser.SEMI, 0)

        def WHERE(self):
            return self.getToken(SwitchLangParser.WHERE, 0)

        def condition(self):
            return self.getTypedRuleContext(SwitchLangParser.ConditionContext,0)


        def getRuleIndex(self):
            return SwitchLangParser.RULE_query

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQuery" ):
                listener.enterQuery(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQuery" ):
                listener.exitQuery(self)




    def query(self):

        localctx = SwitchLangParser.QueryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_query)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 14
            self.match(SwitchLangParser.SELECT)
            self.state = 15
            self.column_list()
            self.state = 16
            self.match(SwitchLangParser.FROM)
            self.state = 17
            self.table()
            self.state = 20
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==24:
                self.state = 18
                self.match(SwitchLangParser.WHERE)
                self.state = 19
                self.condition()


            self.state = 22
            self.match(SwitchLangParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Column_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STAR(self):
            return self.getToken(SwitchLangParser.STAR, 0)

        def column(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SwitchLangParser.ColumnContext)
            else:
                return self.getTypedRuleContext(SwitchLangParser.ColumnContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(SwitchLangParser.COMMA)
            else:
                return self.getToken(SwitchLangParser.COMMA, i)

        def getRuleIndex(self):
            return SwitchLangParser.RULE_column_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterColumn_list" ):
                listener.enterColumn_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitColumn_list" ):
                listener.exitColumn_list(self)




    def column_list(self):

        localctx = SwitchLangParser.Column_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_column_list)
        self._la = 0 # Token type
        try:
            self.state = 33
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [25]:
                self.enterOuterAlt(localctx, 1)
                self.state = 24
                self.match(SwitchLangParser.STAR)
                pass
            elif token in [18]:
                self.enterOuterAlt(localctx, 2)
                self.state = 25
                self.column()
                self.state = 30
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==26:
                    self.state = 26
                    self.match(SwitchLangParser.COMMA)
                    self.state = 27
                    self.column()
                    self.state = 32
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ColumnContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(SwitchLangParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return SwitchLangParser.RULE_column

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterColumn" ):
                listener.enterColumn(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitColumn" ):
                listener.exitColumn(self)




    def column(self):

        localctx = SwitchLangParser.ColumnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_column)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self.match(SwitchLangParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(SwitchLangParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return SwitchLangParser.RULE_table

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTable" ):
                listener.enterTable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTable" ):
                listener.exitTable(self)




    def table(self):

        localctx = SwitchLangParser.TableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_table)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self.match(SwitchLangParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def column(self):
            return self.getTypedRuleContext(SwitchLangParser.ColumnContext,0)


        def operator(self):
            return self.getTypedRuleContext(SwitchLangParser.OperatorContext,0)


        def value(self):
            return self.getTypedRuleContext(SwitchLangParser.ValueContext,0)


        def getRuleIndex(self):
            return SwitchLangParser.RULE_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition" ):
                listener.enterCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition" ):
                listener.exitCondition(self)




    def condition(self):

        localctx = SwitchLangParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self.column()
            self.state = 40
            self.operator()
            self.state = 41
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GT(self):
            return self.getToken(SwitchLangParser.GT, 0)

        def LT(self):
            return self.getToken(SwitchLangParser.LT, 0)

        def EQ(self):
            return self.getToken(SwitchLangParser.EQ, 0)

        def GE(self):
            return self.getToken(SwitchLangParser.GE, 0)

        def LE(self):
            return self.getToken(SwitchLangParser.LE, 0)

        def NE(self):
            return self.getToken(SwitchLangParser.NE, 0)

        def getRuleIndex(self):
            return SwitchLangParser.RULE_operator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperator" ):
                listener.enterOperator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperator" ):
                listener.exitOperator(self)




    def operator(self):

        localctx = SwitchLangParser.OperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 939552768) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(SwitchLangParser.NUMBER, 0)

        def STRING(self):
            return self.getToken(SwitchLangParser.STRING, 0)

        def getRuleIndex(self):
            return SwitchLangParser.RULE_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue" ):
                listener.enterValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue" ):
                listener.exitValue(self)




    def value(self):

        localctx = SwitchLangParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            _la = self._input.LA(1)
            if not(_la==19 or _la==20):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





