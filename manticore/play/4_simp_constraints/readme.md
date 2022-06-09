# Constraints

* use constraints globally or for a specific state.


## Operators module 

import

```
from manticore.core.smtlib import Operators
```

support:


*    Operators.AND,
*    Operators.OR,
*    Operators.UGT (unsigned greater than),
*    Operators.UGE (unsigned greater than or equal to),
*    Operators.ULT (unsigned lower than),
*    Operators.ULE (unsigned lower than or equal to).

## CONCAT

* Operators.CONCAT is used to concatenate an array to a value.
* example : , the return_data of a transaction needs to be changed to a value to be checked against another value:

```
last_return = Operators.CONCAT(256, *last_return)

```


## global constraints

* Use m.constrain(constraint) to add a global cosntraint

example : call a contract from a symbolic address, and restraint this address to be specific values:

```
symbolic_address = m.make_symbolic_value()
m.constraint(Operators.OR(symbolic == 0x41, symbolic_address == 0x42))
m.transaction(caller=user_account,
              address=contract_account,
              data=m.make_symbolic_buffer(320),
              value=0)
```

## State constraint

* add a constraint to a specific state It can be used to constrain the state after its exploration to check some property on it.


```
state.constrain(constraint)
```

## Checking Constraint

* Use solver.check(state.constraints) to know if a constraint is still feasible.

```
// will constraint symbolic_value to be different from 65 and check if the state is still feasible:

state.constrain(symbolic_var != 65)
if solver.check(state.constraints):
    # state is feasible

```

## run

```
(manticore_native) (REDF)vlad@vladis:play/4_simp_constraints ‹main*›$ python 4_run.py                
2022-06-09 17:25:11,220: [286965] m.c.plugin:WARNING: Caught will_solve in state None, but failed to capture its initialization
No bug found

```