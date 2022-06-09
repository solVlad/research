# Run a standalone exploration


```
2022-06-09 16:37:07,222: [150550] m.main:INFO: Registered plugins: IntrospectionAPIPlugin, <class 'manticore.ethereum.plugins.SkipRevertBasicBlocks'>, <class 'manticore.ethereum.plugins.FilterFunctions'>
2022-06-09 16:37:07,222: [150550] m.main:INFO: Beginning analysis
2022-06-09 16:37:07,223: [150550] m.e.manticore:INFO: Starting symbolic create contract
2022-06-09 16:37:07,423: [150550] m.e.manticore:INFO: Starting symbolic transaction: 0
2022-06-09 16:37:07,643: [150550] m.e.manticore:INFO: 1 alive states, 1 terminated states
2022-06-09 16:37:07,673: [150550] m.e.manticore:INFO: Starting symbolic transaction: 1
2022-06-09 16:37:08,036: [150550] m.e.manticore:INFO: 1 alive states, 1 terminated states
2022-06-09 16:37:08,128: [150652] m.c.manticore:INFO: Generated testcase No. 0 - STOP(3 txs)
2022-06-09 16:37:08,129: [150652] m.c.plugin:WARNING: Caught will_solve in state None, but failed to capture its initialization
2022-06-09 16:37:08,769: [150550] m.c.manticore:INFO: Results in /data/redef/research/manticore/play/1_simp_StandAlone/mcore_2t2smmqs
2022-06-09 16:37:08,769: [150550] m.c.manticore:INFO: Total time: 1.0945682525634766
```


```
├── command.sh
├── global.findings
├── global_Simple.init_asm
├── global_Simple.init_visited
├── global_Simple.runtime_asm
├── global_Simple.runtime_visited
├── global_Simple.sol
├── global.solver_stats
├── global.summary
├── manticore.yml
├── user_00000000.constraints
├── user_00000000.pkl
├── user_00000000.summary
├── user_00000000.trace
├── user_00000000.tx
└── user_00000000.tx.json


```
