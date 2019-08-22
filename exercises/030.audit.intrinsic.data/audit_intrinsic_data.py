import json

user_inputs_file = open('./user_input_data.json')
user_inputs = json.load(user_inputs_file)

def element_empty(n):
    if n:
        return False
    return True

def element_length(n):
    if n:
        return len(str(n))
    return 0

def element_type(n):
    if n:
        return type(n).__name__
    return None

def put_audit(n):
    q = {}
    for key, value in n.items():
        q[key] = dict(value=value, empty=element_empty(value),
                     length=element_length(value), type=element_type(value))
    return json.JSONEncoder().encode(q)

def audit_input(n):
    return put_audit(user_inputs[n])

for i in range(1,11):
    print(audit_input(i))
