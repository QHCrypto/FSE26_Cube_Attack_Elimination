# 845 Attack 

## Files

### `845_cubes`
Contains all the cubes used in attack

### `845_spolys`
Contains all the conditional superpolys used in attack

### `845_attack`
Implements equation solving using the Aggressive Testing Method.

#### `solve.py`
For example, the file `845_attack/spoly_k54k56k58` means the attack under weak key space k54=k56=k58=0. 

In solve.py, you can choose two kinds of modes, mode 1 is to check the used keys, mode 2 is to solve the equation for a randomly generated key

#### `group_files`
Contains the randomly generated keys that satisfy at least one weak key condition

### `845_logs`
Contains attack results for randomly sampled keys in different weak key space.

For example: 140_0ae3c45d1bdcb1183710.log means that we can get 33 = 173 - 140 equations. 

the first line [0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0]
means the correct values for $z_0$,$z_1$,...,$z_172$.

the third line denote the solution by the testing method, [[-54], [-56], [-58], [59], [-65], [-63], [-61], [-146], [111], [-96], [148], [135], [124], [-89], [-87], [-83], [-115], [-113], [100], [-98], [-94], [-130], [85], [39], [-80], [132], [102], [-109], [-128], [-13], [-11], [165], [134]]
where [-54] means $z_54 = 0$,[59] means $z_59 = 1$.

line 6-41: The equations obtained by using the aggressive method.

line 43-66: The output of the automated tool. This tool is available at https://github.com/hadipourh/autoguess

line 66: Number of determined variables calculated by the automated tool.

line 67: Results of the equation correctness verification

### `845_results`  

Take the file `0aa481802933c6a213f8.txt` as an example:  
```
[(33, 2942.48, 'Yes'), (31, 3389.03, 'Yes'), (31, 3819.42, 'Yes'), (31, 6598.41, 'Yes')]
Equation solving time is 2942.48
Enumeration complexity: 2^47.0
Whether success: 1
```  

#### Explanation of the content:  
1. **First line**: Indicates that this key belongs to 4 weak key spaces. Each tuple in the list corresponds to one weak key space, with the three elements representing:  
   - The number of determined variables in the equations obtained (e.g., `33` in the first tuple means 33 determined variables);  
   - Equation solving time (in seconds, e.g., `2942.48` means 2942.48 seconds);  
   - Equation correctness (e.g., `Yes` means all obtained equations are correct).  

2. **Second line**: Specifies the minimum equation solving time with `Yes`.  

3. **Third line**: Shows the enumeration complexity, which is \(2^{47.0}\).  

4. **Fourth line**: Marks the attack success status, where `1` represents a successful attack.

### `calculate_success_rate.py`
Calculate the success rate of the attack.


### `Output Information for solve.py (on-screen)`
"round 2": The index of the iteration.
"untested vars": The list of indices of the untested secret variables, sorted by the increasing order of the appearing times.
"to test var": The index of the variable to be tested.
"current_assigns": The list of the assignments determined in previous iterations. Specifically, ['k58=1', 'k61=0'] means k58=1 and k61=0, which obtains from previous tests.
"both_has_solutions": The list of indices of variables whose values cannot be determined.

"""
testing k61
Current assigns: ['k61=0']
Solution found in 0.29s
"""

which implies k61 == 0 maybe hold.

"""
Current assigns: ['k61=1']
Proven UNSAT in 1.16s
"""
which implies k61 == 1 is contradiciton, means k61 == 0 must hold

"Solution (first 173 vars)": It means we find a solution and the first phase of agressive teting method is done.
"Timeout after 142.48s": It means the equation is unsolved in 142.48s, we treat this situation the same with "Proven UNSAT"
"fix_k": Is contains the value of the untested variables.




The following are an output example of spoly_k54k56k58/solve.py.

845-Trivium (Extended 173 vars)
start
Choose processing mode:
1. Process keys from file
2. Generate and process random keys

Generating new random key...
Found valid random key:
Hex representation: 0cdb7396082c154c2fb0
Processing key: [0, 0, 0, 0, 1, 1, 0, 0, 1, 1]...
Initial key bits (80): [0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0]
Extended key bits 173: [0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1]
Hex key: 0cdb7396082c154c2fb0
now calculate dir: 845_organize_spoly_k54k56k58
[79, 162, 74, 75, 76, 77, 73, 71, 72, 69, 70, 78, 66, 67, 54, 56, 58, 153, 151, 23, 171, 140, 108, 21, 24, 8, 35, 17, 19, 138, 159, 125, 172, 149, 93, 9, 99, 152, 10, 110, 154, 97, 44, 127, 84, 142, 34, 45, 16, 49, 155, 123, 164, 60, 46, 112, 1, 114, 158, 160, 12, 163, 166, 48, 47, 129, 50, 14, 22, 7, 167, 106, 25, 33, 6, 156, 136, 95, 18, 20, 168, 36, 86, 121, 3, 82, 119, 144, 15, 42, 5, 53, 157, 43, 0, 51, 26, 101, 116, 62, 150, 170, 88, 107, 131, 27, 4, 147, 55, 31, 90, 143, 120, 68, 57, 52, 103, 29, 118, 28, 145, 32, 81, 117, 105, 126, 141, 139, 169, 40, 38, 104, 41, 2, 64, 122, 137, 30, 37, 91, 161, 133, 92, 134, 165, 11, 13, 128, 109, 102, 132, 80, 39, 85, 130, 94, 98, 100, 113, 115, 83, 87, 89, 124, 135, 148, 96, 111, 146, 61, 63, 65, 59]
[[-54], [-56], [-58]]
2025-07-16 17:00:16.006434
round 7
Current assigns: ['k61=0', 'k63=0', 'k65=0', 'k59=0', 'k54=0', 'k56=0', 'k58=0']

Timeout after 117.84s

.........


2025-07-16 17:17:11.148605
round 7
Current assigns: ['k61=1', 'k63=0', 'k65=0', 'k59=0', 'k54=0', 'k56=0', 'k58=0']

Solution found in 19.66s
Solution (first 173 vars): [False, False, False, False, True, True, False, False, True, False, False, True, True, False, True, True, False, True, True, True, False, False, True, True, True, False, False, True, False, True, True, False, False, False, False, False, False, False, False, False, False, False, True, False, True, True, False, False, False, False, False, True, False, True, False, True, False, True, False, False, True, True, False, False, False, False, True, False, True, True, True, True, True, False, True, True, False, False, True, False, True, False, True, False, False, False, True, True, True, True, True, True, False, False, True, False, True, False, False, False, True, True, True, False, False, False, True, True, True, True, False, False, True, True, False, False, False, False, False, False, False, True, False, True, True, False, False, True, False, False, True, False, True, True, False, True, True, False, False, True, True, False, True, True, False, True, True, False, True, False, True, False, True, False, False, True, False, False, True, False, True, True, False, False, False, True, False, False, True, True, False, False, True]
fix_k:  [125, 136, 149, 97, -112, 147, 62, -64, -66]
2025-07-16 17:17:33.141071
round 3
untested vars:  [124, 135, 148, 96, 111, 146, 61, 63, 65]
to test var: 59
current_assigns:  ['k54=0', 'k56=0', 'k58=0'] 3
both_has_solutions:  [] 0
Second phase, VARIFY
testing k59 == 0
Current assigns: ['k54=0', 'k56=0', 'k58=0', 'k59=1', 'k124=1', 'k135=1', 'k148=1', 'k96=1', 'k111=0', 'k146=1', 'k61=1', 'k63=0', 'k65=0']

Timeout after 134.57s
round is done

fix_k:  [125, 136, 149, 97, -112, 147, 62, -64]
2025-07-16 17:19:50.309229
round 4
untested vars:  [124, 135, 148, 96, 111, 146, 61, 63]
to test var: 65
current_assigns:  ['k54=0', 'k56=0', 'k58=0', 'k59=0'] 4
both_has_solutions:  [] 0
Second phase, VARIFY
testing k65 == 0
Current assigns: ['k54=0', 'k56=0', 'k58=0', 'k59=0', 'k65=1', 'k124=1', 'k135=1', 'k148=1', 'k96=1', 'k111=0', 'k146=1', 'k61=1', 'k63=0']

Timeout after 135.83s
round is done

fix_k:  [125, 136, 149, 97, -112, 147, 62]
2025-07-16 17:22:08.909776
round 5
untested vars:  [124, 135, 148, 96, 111, 146, 61]
to test var: 63
current_assigns:  ['k54=0', 'k56=0', 'k58=0', 'k59=0', 'k65=0'] 5
both_has_solutions:  [] 0
Second phase, VARIFY
testing k63 == 0
Current assigns: ['k54=0', 'k56=0', 'k58=0', 'k59=0', 'k65=0', 'k63=1', 'k124=1', 'k135=1', 'k148=1', 'k96=1', 'k111=0', 'k146=1', 'k61=1']

Timeout after 137.13s
round is done

fix_k:  [125, 136, 149, 97, -112, 147]
2025-07-16 17:24:28.561675
round 6
untested vars:  [124, 135, 148, 96, 111, 146]
to test var: 61
current_assigns:  ['k54=0', 'k56=0', 'k58=0', 'k59=0', 'k65=0', 'k63=0'] 6
both_has_solutions:  [] 0
Second phase, VARIFY
testing k61 == 0
Current assigns: ['k54=0', 'k56=0', 'k58=0', 'k59=0', 'k65=0', 'k63=0', 'k61=0', 'k124=1', 'k135=1', 'k148=1', 'k96=1', 'k111=0', 'k146=1']

Proven UNSAT in 24.45s
round is done

fix_k:  [125, 136, 149, 97, -112]
2025-07-16 17:24:55.325279
round 7
untested vars:  [124, 135, 148, 96, 111]
to test var: 146
current_assigns:  ['k54=0', 'k56=0', 'k58=0', 'k59=0', 'k65=0', 'k63=0', 'k61=1'] 7
both_has_solutions:  [] 0
Second phase, VARIFY
testing k146 == 0
Current assigns: ['k54=0', 'k56=0', 'k58=0', 'k59=0', 'k65=0', 'k63=0', 'k61=1', 'k146=0', 'k124=1', 'k135=1', 'k148=1', 'k96=1', 'k111=0']

Proven UNSAT in 14.94s
round is done

fix_k:  [125, 136, 149, 97]
2025-07-16 17:25:12.686138
round 8
untested vars:  [124, 135, 148, 96]
to test var: 111
current_assigns:  ['k54=0', 'k56=0', 'k58=0', 'k59=0', 'k65=0', 'k63=0', 'k61=1', 'k146=1'] 8
both_has_solutions:  [] 0
Second phase, VARIFY
testing k111 == 0
Current assigns: ['k54=0', 'k56=0', 'k58=0', 'k59=0', 'k65=0', 'k63=0', 'k61=1', 'k146=1', 'k111=1', 'k124=1', 'k135=1', 'k148=1', 'k96=1']

Timeout after 142.48s
round is done

fix_k:  [125, 136, 149]
2025-07-16 17:27:37.756555
round 9
untested vars:  [124, 135, 148]
to test var: 96
current_assigns:  ['k54=0', 'k56=0', 'k58=0', 'k59=0', 'k65=0', 'k63=0', 'k61=1', 'k146=1', 'k111=0'] 9
both_has_solutions:  [] 0
Second phase, VARIFY
testing k96 == 0
Current assigns: ['k54=0', 'k56=0', 'k58=0', 'k59=0', 'k65=0', 'k63=0', 'k61=1', 'k146=1', 'k111=0', 'k96=0', 'k124=1', 'k135=1', 'k148=1']

Proven UNSAT in 7.96s
round is done

fix_k:  [125, 136]
2025-07-16 17:27:48.097597
round 10
untested vars:  [124, 135]
to test var: 148
current_assigns:  ['k54=0', 'k56=0', 'k58=0', 'k59=0', 'k65=0', 'k63=0', 'k61=1', 'k146=1', 'k111=0', 'k96=1'] 10
both_has_solutions:  [] 0
Second phase, VARIFY
testing k148 == 0
Current assigns: ['k54=0', 'k56=0', 'k58=0', 'k59=0', 'k65=0', 'k63=0', 'k61=1', 'k146=1', 'k111=0', 'k96=1', 'k148=0', 'k124=1', 'k135=1']

Proven UNSAT in 12.38s
round is done

fix_k:  [125]
2025-07-16 17:28:02.707548
round 11
untested vars:  [124]
to test var: 135
current_assigns:  ['k54=0', 'k56=0', 'k58=0', 'k59=0', 'k65=0', 'k63=0', 'k61=1', 'k146=1', 'k111=0', 'k96=1', 'k148=1'] 11
both_has_solutions:  [] 0
Second phase, VARIFY
testing k135 == 0
Current assigns: ['k54=0', 'k56=0', 'k58=0', 'k59=0', 'k65=0', 'k63=0', 'k61=1', 'k146=1', 'k111=0', 'k96=1', 'k148=1', 'k135=0', 'k124=1']

Proven UNSAT in 69.13s
round is done


fix_k:  [-80, -163, 75, 76, -77, -78, -74, 72, 73, 70, 71, 79, 67, -68, -55, -57, -59, -154, -152, 24, -172, 141, 109, -22, 25, 9, -36, 18, 20, -139, -160, -126, 173, -150, -94, -10, -100, 153, -11, -111, -155, -98, 45, 128, -85, 143, -35, 46, -17, -50, 156, 124, -165, 61, -47, 113, -2, -115, 159, 161, 13, -164, -167, -49, -48, -130, -51, 15, 23, -8, -168, 107, -26, -34, -7, -157, 137, -96, 19, -21, 169, -37, 87, 122, -4, 83, -120, -145, 16, 43, 6, 54, -158, -44, -1, 52, -27, 102, -117, -63, 151, -171, 89, 108, -132, 28, 5, -148, 56, -32, 91, 144, -121, 69, 58, -53, -104, 30, -119, -29, 146, -33, -82, -118, -106, -127, -142, 140, 170, -41, -39, -105, -42, -3, -65, -123, -138, 31, -38, 92, 162, 134, -93, -135, 166, 12, -14]
2025-07-16 17:32:41.045449
round 28
untested vars:  [79, 162, 74, 75, 76, 77, 73, 71, 72, 69, 70, 78, 66, 67, 54, 56, 58, 153, 151, 23, 171, 140, 108, 21, 24, 8, 35, 17, 19, 138, 159, 125, 172, 149, 93, 9, 99, 152, 10, 110, 154, 97, 44, 127, 84, 142, 34, 45, 16, 49, 155, 123, 164, 60, 46, 112, 1, 114, 158, 160, 12, 163, 166, 48, 47, 129, 50, 14, 22, 7, 167, 106, 25, 33, 6, 156, 136, 95, 18, 20, 168, 36, 86, 121, 3, 82, 119, 144, 15, 42, 5, 53, 157, 43, 0, 51, 26, 101, 116, 62, 150, 170, 88, 107, 131, 27, 4, 147, 55, 31, 90, 143, 120, 68, 57, 52, 103, 29, 118, 28, 145, 32, 81, 117, 105, 126, 141, 139, 169, 40, 38, 104, 41, 2, 64, 122, 137, 30, 37, 91, 161, 133, 92, 134, 165, 11, 13]
to test var: 128
current_assigns:  ['k54=0', 'k56=0', 'k58=0', 'k59=0', 'k65=0', 'k63=0', 'k61=1', 'k146=1', 'k111=0', 'k96=1', 'k148=1', 'k135=1', 'k124=1', 'k89=1', 'k87=1', 'k83=0', 'k115=0', 'k113=1', 'k100=1', 'k98=0', 'k94=1', 'k130=1', 'k85=0', 'k39=0', 'k80=1', 'k132=1', 'k102=1', 'k109=1'] 28
both_has_solutions:  [] 0
Second phase, VARIFY
testing k128 == 0
Current assigns: ['k54=0', 'k56=0', 'k58=0', 'k59=0', 'k65=0', 'k63=0', 'k61=1', 'k146=1', 'k111=0', 'k96=1', 'k148=1', 'k135=1', 'k124=1', 'k89=1', 'k87=1', 'k83=0', 'k115=0', 'k113=1', 'k100=1', 'k98=0', 'k94=1', 'k130=1', 'k85=0', 'k39=0', 'k80=1', 'k132=1', 'k102=1', 'k109=1', 'k128=1']

Proven UNSAT in 2.55s
round is done

0cdb7396082c154c2fb0_144.log
Time cost: 1965.40s.