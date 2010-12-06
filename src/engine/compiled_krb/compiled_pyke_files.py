# compiled_pyke_files.py

from pyke import target_pkg

pyke_version = '1.1.1'
compiler_version = 1
target_pkg_version = 1

try:
    loader = __loader__
except NameError:
    loader = None

def get_target_pkg():
    return target_pkg.target_pkg(__name__, __file__, pyke_version, loader, {
         ('engine', '', 'off_state_facts.kfb'):
           [1290250235.76504, 'off_state_facts.fbc'],
         ('engine', '', 'off_state_rules.krb'):
           [1290279294.531483, 'off_state_rules_fc.py'],
         ('engine', '', 'off_state_questions.kqb'):
           [1290252657.336259, 'off_state_questions.qbc'],
        },
        compiler_version)

