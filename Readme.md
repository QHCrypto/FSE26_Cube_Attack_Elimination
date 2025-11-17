# Cube Attack Toolkit

A repository for the paper *Cube Attacks with Elimination Strategy: Key Recovery Attacks on Trivium*.

> **Note**: All experiments were conducted on **Ubuntu 22.04.3** system.

## Requirements
- For superpoly recovery: **Gurobi** optimizer
- For equation solving: **python-sat** package
  ```bash
  pip3 install python-sat
  pip3 install pycryptosat==5.11.21

## Superpoly Recovery

1. **`initial_cube_with_numeric_mapping`**  
   Provides implementation for initial cube search using numeric mapping 
2. **`cube_search_with_monomial_prediction`**  
   Contains code for: 
   • Cube expansion using monomial prediction  
   • Subcube search algorithms
3. **`conditional_superpoly_recovery`**  
   Implements:  
   • Superpoly recovery  
   • Conditional superpoly recovery  
   • Codes of selecting eliminable variables

> 💡 In `main()`, uncomment the corresponding line to enable the desired feature.
To compile the code:
$ make

To run the program:
$ ./a.out
## Experimental Data

- **`840_data`**  
  Demonstrates equation solving using:  
  • 58-dimensional mother cube  
  • 54-dimensional mother cube

- **`845_data`**  
  Contains equation solving codes and results for all 9 weak key spaces

- **`855_con_spoly`**  
  Stores a conditional superpoly at 855-round. Here, the polynomial we present are in terms of z_{83}. We employed variable substitution to express it as a polynomial in terms of k, their expressions excessively complex, requiring a storage space of 69 GB. Therefore, we did not upload them. However, we have uploaded the code for performing variable substitution operations, which can be found in the folder 'conditional_superpoly_recovery'.
 
  To verify the balance:
  $ g++ -o a.out calculate_balance.cpp
  $ ./a.out

- **`comparison`** 
  Stores superpolys recoverd by 3 different superpoly recovery methods. 