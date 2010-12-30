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
         ('engine', '', 'on_state/on_state_rules_sound.krb'):
           [1293729565.955581, 'on_state_rules_sound_fc.py'],
         ('engine', '', 'on_state/on_state_fact_network.kfb'):
           [1293729565.958706, 'on_state_fact_network.fbc'],
         ('engine', '', 'off_state_facts.kfb'):
           [1293727489.825137, 'off_state_facts.fbc'],
         ('engine', '', 'on_state/on_state_fact_screen.kfb'):
           [1293729565.959432, 'on_state_fact_screen.fbc'],
         ('engine', '', 'on_state/on_state_questions_sound.kqb'):
           [1293729565.981629, 'on_state_questions_sound.qbc'],
         ('engine', '', 'off_state_rules.krb'):
           [1293727489.939237, 'off_state_rules_fc.py'],
         ('engine', '', 'on_state/on_state_rules_screen.krb'):
           [1293729565.990631, 'on_state_rules_screen_fc.py'],
         ('engine', '', 'on_state/on_state_rules_network.krb'):
           [1293729565.999601, 'on_state_rules_network_fc.py'],
         ('engine', '', 'on_state/on_state_fact_sound.kfb'):
           [1293729566.000341, 'on_state_fact_sound.fbc'],
         ('engine', '', 'off_state_questions.kqb'):
           [1293727489.975198, 'off_state_questions.qbc'],
         ('engine', '', 'on_state/on_state_questions_screen.kqb'):
           [1293729566.000966, 'on_state_questions_screen.qbc'],
         ('engine', '', 'on_state/on_state_questions_network.kqb'):
           [1293729566.001518, 'on_state_questions_network.qbc'],
        },
        compiler_version)

