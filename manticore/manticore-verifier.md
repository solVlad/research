# manticore-verifier

* https://manticore.readthedocs.io/en/latest/verifier.html

* Manticore installs a separated CLI tool to do property based symbolic execution of smart contracts.
* manticore-verifier initializes an emulated blockchain environment with a configurable set of accounts and then send sarious symbolic transactions to the target contract containing property methods.
* A configurable stopping condition bounds the exploration, properties not failing are considered to pass.

* manticore-verifier will detect and test property methods written in the original contract language

## usage

* use methods names starting with `crytic_`
* select your own way to name property methods using the --propre 
```
--propre PROPRE       A regular expression for selecting properties
```
* manticore-verifier needs to be pointed to a the target contract containing any number of property methods.

```
--contract_name CONTRACT_NAME The target contract name defined in the source code
```

