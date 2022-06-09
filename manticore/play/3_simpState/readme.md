# state


* Each path executed has its state of the blockchain.

    * m.ready_states: the list of states that are ready (they did not execute a REVERT/INVALID)
    * m.killed_states: the list of states that are ready (they did not execute a REVERT/INVALID)
    * m.all_states: all the states

    ```
    for state in m.all_states:
    # do something with state
    ```


## state information


* state.platform.get_balance(account.address): the balance of the account
* state.platform.transactions: the list of transactions
* state.platform.transactions[-1].return_data: the data returned by the last transaction

## deserialize

* The data returned by the last transaction is an array, which can be converted to a value with ABI.deserialize

```
data = state.platform.transactions[0].return_data
data = ABI.deserialize("uint", data)
```

## generate testcase

* generate inputs for the state

```
m.generate_testcase(state, 'BugFound')

```


# run

```
> python 3_simp_throw.py 
Throw found /data/redef/research/manticore/play/3_simpState/mcore_0l0_e6me
2022-06-09 16:57:35,325: [208477] m.c.plugin:WARNING: Caught will_solve in state None, but failed to capture its initialization
```