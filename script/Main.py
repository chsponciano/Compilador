from Lexico import Lexico
from Syntatic import Syntatic
from Semantic import Semantic
from LexicalError import LexicalError
from SemanticError import SemanticError
from SyntaticError import SyntaticError
import sys
sys.stdout.reconfigure(encoding='utf-8')

code = sys.argv[1]

try:
    lexico   = Lexico(code)
    syntatic = Syntatic()
    semantic = Semantic()
    
    syntatic.parse(lexico, semantic)

except (LexicalError, SyntaticError, SemanticError) as e:
    print(e)

sys.stdout.flush()