from Constants import Constants
from Stack import Stack
from Lexico import Lexico
from Token import Token
from Semantic import Semantic
from LexicalError import LexicalError
from SemanticError import SemanticError
from SyntaticError import SyntaticError

class Syntatic(Constants):

    def __init__(self):
        super(Syntatic, self).__init__()
        self.stack = Stack()
        self.currentToken = None
        self.previousToken = None
        self.scanner = None
        self.semanticAnalyser = None

    def isTerminal(self, x):
        return x < self.FIRST_NON_TERMINAL

    def validationLexeme(self, lexeme):
        if lexeme == '$':
            return 'fim de arquivo'
        
        return lexeme

    def isNonTerminal(self, x):
        return x >= self.FIRST_NON_TERMINAL and x < self.FIRST_SEMANTIC_ACTION

    def isSemanticAction(self, x):
        return x >= self.FIRST_SEMANTIC_ACTION

    def parse(self, scanner, semanticAnalyser):
        self.scanner = scanner
        self.semanticAnalyser = semanticAnalyser

        self.stack.clear()
        self.stack.push(self.DOLLAR)
        self.stack.push(self.START_SYMBOL)

        self.currentToken = scanner.nextToken()

        while not self.step():
            continue 

    def pushProduction(self, topStack, tokenInput):
        p = self.PARSER_TABLE[topStack - self.FIRST_NON_TERMINAL][tokenInput - 1]

        if p >= 0:
            production = self.PRODUCTIONS[p]
            for i in range(len(production) - 1, -1, -1):
                self.stack.push(production[i])
            return True
        
        return False

    def step(self):
        if self.currentToken is None:
            pos = 0
            if self.previousToken is not None:
                pos = self.previousToken.position + len(self.previousToken.lexeme)
            
            self.currentToken = Token(self.DOLLAR, "$", pos)
            
        x = self.stack.pop()
        a = self.currentToken.identification

        if x == self.EPSILON:
            return False
            
        elif self.isTerminal(x):
            if x == a:
                if self.stack.empty():
                    return True
                else:
                    self.previousToken = self.currentToken
                    self.currentToken = self.scanner.nextToken()
                    return False
            else:
                raise SyntaticError(self.PARSER_ERROR[x], self.scanner.lineToken(self.currentToken.position), self.validationLexeme(self.currentToken.lexeme))
        
        elif self.isNonTerminal(x):
            if self.pushProduction(x, a):
                return False
            else:
                raise SyntaticError(self.PARSER_ERROR[x], self.scanner.lineToken(self.currentToken.position), self.validationLexeme(self.currentToken.lexeme))
        
        else:
            self.semanticAnalyser.executeAction(x - self.FIRST_SEMANTIC_ACTION, self.previousToken)
            return False