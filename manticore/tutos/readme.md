# Tutorial

* ref: https://github.com/trailofbits/manticore/wiki/Tutorial
* workshop: https://github.com/trailofbits/publications/tree/master/workshops/Automated%20Smart%20Contracts%20Audit%20-%20TruffleCon%202018/manticore
* run in docker:

```
 docker pull trailofbits/eth-security-toolbox
 docker run -it trailofbits/eth-security-toolbox

ethsec@db0d14f62320:~/rattle$ cd /home/ethsec/
ethsec@db0d14f62320:~$ git clone https://github.com/trailofbits/publications

```

## 01.eth-security-toolbox train  - workshop01

* https://github.com/crytic/building-secure-contracts/tree/master/program-analysis/manticore

```
/home/ethsec/building-secure-contracts/program-analysis/manticore
=================================================================
├── adding-constraints.md
├── examples
│   ├── example_constraint.py
│   ├── example_run.py
│   ├── example.sol
│   ├── example_throw.py
│   └── suicidal.sol
├── exercises
│   ├── example
│   │   ├── my_token.py
│   │   └── my_token.sol
│   ├── example.md
│   ├── exercise1
│   │   ├── solution.py
│   │   ├── template.py
│   │   └── token.sol
│   ├── exercise1.md
│   ├── exercise2
│   │   ├── overflow.sol
│   │   ├── solution.py
│   │   └── template.py
│   ├── exercise2.md
│   └── README.md
├── getting-throwing-paths.md
├── README.md
├── running-under-manticore.md
├── scripts
│   └── gh_action_test.sh
└── symbolic-execution-introduction.md
```

## 02.   workshop01

```
~/publications/workshops/Automated Smart Contracts Audit - TruffleCon 2019/manticore
=====================================================================================
├── examples
│   ├── example_2.sol
│   ├── example_constraint.py
│   ├── example_run.py
│   ├── example.sol
│   ├── example_throw.py
│   ├── my_token
│   │   ├── my_token.py
│   │   └── my_token.sol
│   └── suicidal.sol
├── exercises
│   ├── exercise1
│   │   ├── solution.py
│   │   ├── template.py
│   │   └── token.sol
│   └── exercise2
│       ├── overflow.sol
│       ├── solution.py
│       └── template.py
└── manticore.pdf
```