def match(ruleset, msg_string, curr_idx, rule_string):

    if rule_string[0].isdigit(): 
        for alternative in rule_string.split(' | '):
            # Subregelstack aufbauen            
            subrules = alternative.split(' ',1)

            if len(subrules)==1:
                # Rekursionsende, letzte Regel im Regelstack
                yield from match(ruleset, msg_string, curr_idx, ruleset[subrules[0]])
            else:
                # Regelstack abarbeiten
                for m in match(ruleset, msg_string, curr_idx, ruleset[subrules[0]]):
                    yield from match(ruleset, msg_string, m, subrules[1])
            
    elif curr_idx<len(msg_string) and msg_string[curr_idx] == rule_string[1]:   #rule_string = "x"
            yield curr_idx+1


with open('./19/input.txt') as file:
    rules, messages = file.read().split("\n\n")
    ruleset = {}
    ruleset= dict(rule.split(': ') for rule in rules.splitlines())

    ruleset["8"] = "42 | 42 8"
    ruleset["11"] = "42 31 | 42 11 31"
    
    matchlist = [1 if any(m==len(msg) for m in match(ruleset, msg, 0, '0')) else 0 for msg in messages.split('\n')]
    print(sum(matchlist))