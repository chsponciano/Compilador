from Lexico import Lexico
from Syntatic import Syntatic
from Semantic import Semantic
from LexicalError import LexicalError
from SemanticError import SemanticError
from SyntaticError import SyntaticError
from pathlib import Path
import os
import sys
sys.stdout.reconfigure(encoding='utf-8')

code = sys.argv[1]
directory = sys.argv[2]
try:
    lexico   = Lexico(code)
    syntatic = Syntatic()
    semantic = Semantic()
    
    syntatic.parse(lexico, semantic)
    
    with open(os.path.dirname(directory) + '\\' + Path(directory).stem + '.il', 'w') as file_il:
        file_il.write(semantic.get_code_out())

except (LexicalError, SyntaticError, SemanticError) as e:
    print(e)

sys.stdout.flush()