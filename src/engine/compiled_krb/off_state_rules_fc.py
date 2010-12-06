# off_state_rules_fc.py

from __future__ import with_statement
from pyke import contexts, pattern, fc_rule, knowledge_base

pyke_version = '1.1.1'
compiler_version = 1

def init_rule(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('off_state_questions', 'beep_question', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        engine.assert_('off_state_facts', 'beep_answer',
                       (rule.pattern(0).as_data(context),)),
        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def ram_yes_rule(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('off_state_facts', 'beep_answer', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        import wx
        wx.MessageBox("Check the memory, you may have purchased the wrong memory, installed it incorrectly, or damaged the memory module by handling it improperly.", 'Solution')
        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def ram_no_rule(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('off_state_facts', 'beep_answer', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        engine.assert_('off_state_facts', 'problem_from',
                       (rule.pattern(0).as_data(context),)),
        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def speaker_rule(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('off_state_facts', 'problem_from', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('off_state_questions', 'speaker_question', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            engine.assert_('off_state_facts', 'speaker_answer',
                           (rule.pattern(0).as_data(context),)),
            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def speaker_yes_rule(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('off_state_facts', 'speaker_answer', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('off_state_questions', 'monitor_check_question', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            engine.assert_('off_state_facts', 'monitor_answer',
                           (rule.pattern(0).as_data(context),)),
            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def speaker_no_rule(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('off_state_facts', 'speaker_answer', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        import wx
        wx.MessageBox("Please make sure the speaker is there if not please install it in your case and rerun the program", 'Solution')
        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def monitor_yes_rule(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('off_state_facts', 'monitor_answer', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        import wx
        wx.MessageBox("Please check your monitor cable if it is connected to the case at the rear.", 'Solution')
        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def monitor_no_rule(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('off_state_facts', 'monitor_answer', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        import wx
        wx.MessageBox("Please switched on and see the results.", 'Solution')
        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def populate(engine):
  This_rule_base = engine.get_create('off_state_rules')
  
  fc_rule.fc_rule('init_rule', This_rule_base, init_rule,
    (('off_state_questions', 'beep_question',
      (contexts.variable('ans'),),
      False),),
    (contexts.variable('ans'),))
  
  fc_rule.fc_rule('ram_yes_rule', This_rule_base, ram_yes_rule,
    (('off_state_facts', 'beep_answer',
      (pattern.pattern_literal(True),),
      False),),
    ())
  
  fc_rule.fc_rule('ram_no_rule', This_rule_base, ram_no_rule,
    (('off_state_facts', 'beep_answer',
      (pattern.pattern_literal(False),),
      False),),
    (pattern.pattern_literal('speaker'),))
  
  fc_rule.fc_rule('speaker_rule', This_rule_base, speaker_rule,
    (('off_state_facts', 'problem_from',
      (pattern.pattern_literal('speaker'),),
      False),
     ('off_state_questions', 'speaker_question',
      (contexts.variable('ans'),),
      False),),
    (contexts.variable('ans'),))
  
  fc_rule.fc_rule('speaker_yes_rule', This_rule_base, speaker_yes_rule,
    (('off_state_facts', 'speaker_answer',
      (pattern.pattern_literal(True),),
      False),
     ('off_state_questions', 'monitor_check_question',
      (contexts.variable('ans'),),
      False),),
    (contexts.variable('ans'),))
  
  fc_rule.fc_rule('speaker_no_rule', This_rule_base, speaker_no_rule,
    (('off_state_facts', 'speaker_answer',
      (pattern.pattern_literal(False),),
      False),),
    ())
  
  fc_rule.fc_rule('monitor_yes_rule', This_rule_base, monitor_yes_rule,
    (('off_state_facts', 'monitor_answer',
      (pattern.pattern_literal(True),),
      False),),
    ())
  
  fc_rule.fc_rule('monitor_no_rule', This_rule_base, monitor_no_rule,
    (('off_state_facts', 'monitor_answer',
      (pattern.pattern_literal(False),),
      False),),
    ())


Krb_filename = '../off_state_rules.krb'
Krb_lineno_map = (
    ((13, 17), (3, 3)),
    ((18, 19), (5, 5)),
    ((28, 32), (9, 9)),
    ((33, 33), (11, 11)),
    ((34, 34), (12, 12)),
    ((43, 47), (16, 16)),
    ((48, 49), (18, 18)),
    ((58, 62), (22, 22)),
    ((63, 67), (23, 23)),
    ((68, 69), (25, 25)),
    ((78, 82), (29, 29)),
    ((83, 87), (30, 30)),
    ((88, 89), (32, 32)),
    ((98, 102), (36, 36)),
    ((103, 103), (38, 38)),
    ((104, 104), (39, 39)),
    ((113, 117), (43, 43)),
    ((118, 118), (45, 45)),
    ((119, 119), (46, 46)),
    ((128, 132), (50, 50)),
    ((133, 133), (52, 52)),
    ((134, 134), (53, 53)),
)
