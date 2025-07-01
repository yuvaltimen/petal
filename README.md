
## PETaL - Python Extract Transform and Load

A framework to compose custom ETLs on top of a logical floor.

Follow along in the `/examples` directory to build up arbitrary pipelines.

(This is modeled on Airflow's DAG Operator model for intuitive composition in Python.)

### 01 - Trivial Case

```python
# 

```

### 01 - Simple Case

```python

```

### Theory
There are 3 types of Operators - **Sources**, **Sinks**, and **Non-Terminal Operators.**
Pipelines in Petal are wrappers around arbitrary Directed Acyclic Graphs (DAGs). 
A Pipeline is constructed from a DAG and has the following invariants:
1. **It must have at least 1 Operator satisfying each of the terminal operator types (ie. at least 1 Source and 1 Sink).**
2. **Operators are directional (data flows in a particular direction within the Operator).**
3. **Each Operator has a unique ID and a reference to its upstream and downstream Operators.**
4. **There are no cycles in the graph.**

 

