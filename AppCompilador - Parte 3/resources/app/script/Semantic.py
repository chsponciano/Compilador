from SemanticError import SemanticError
from Constants import Constants

class Semantic(Constants):

    def executeAction(self, action, token):
        try:
            print(f"Action #{action}, Token: {token}")
        except SemanticError as e:
            print(e)
