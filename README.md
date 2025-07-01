
## PETaL - Python Extract Transform and Load

A framework to compose custom ETLs on top of a logical floor.

Follow along in the `/examples` directory to build up arbitrary pipelines.

(This is modeled on Airflow's DAG Operator model for intuitive composition in Python.)

### 01. Trivial Case

```python
# The most trivial pipeline possible
with Pipeline("01_noop") as dag:  # Define the pipeline context manager, inner block gets scoped to this object
    source = EmptySource("empty_source")  # Define operators
    sink = NoOpSink("no_op_sink")

    source >> sink  # Compose the operators into a DAG

dag.run()
```

### 02. Simple Case - Single ETL Step

```python
# A single ETL step
with Pipeline("02_copy_file_to_file") as dag:
    read_logs = FileReader("read_logs", file_path="../data/example_input.txt")
    pattern_filter = RegexFilter("filter_info", pattern="^INFO")
    write_to_file = FileWriter("write_file", file_path="../data/example_output.txt")

    read_logs >> pattern_filter >> write_to_file

dag.run()
```

### 03. One Source, Multiple Sinks

```python
    with Pipeline("03_splitting_streams_to_multiple_destinations") as dag:
        read_logs = FileReader("read_logs", file_path="../data/example_input.txt")
        # Fan-out operator that can be used to split the stream into multiple threads
        splitter = Splitter("split")
        
        # One branch will be just a direct copy
        write_to_file_unfiltered = FileWriter("write_unfiltered", file_path="../data/example_output_unfiltered.txt")
        
        # The other branch will be nice and filtered
        pattern_filter = RegexFilter("filter_info", pattern="^INFO")
        write_to_file_filtered = FileWriter("write_filtered", file_path="../data/example_output_filtered.txt")
        

        # Read the logs into the splitter...
        read_logs >> splitter
        
        # ...then read as many branches from the splitter as you want
        splitter >> pattern_filter >> write_to_file_filtered
        splitter >> write_to_file_unfiltered

    dag.run()
```

### 04. Multiple Sources, One Sink

```python
    with Pipeline("example_04_joining_multiple_streams_into_one") as dag:
        source_1 = FileReader("source_1", file_path="../data/source_1.txt")
        source_2 = FileReader("source_2", file_path="../data/source_2.txt")
        source_3 = FileReader("source_3", file_path="../data/source_3.txt")
        
        joiner = StreamJoiner("joiner")

        write_to_file = FileWriter("write_to_file", file_path="../data/all_concatenated.txt")

        source_1 >> joiner
        source_2 >> joiner
        source_3 >> joiner
        joiner >> write_to_file

    dag.run()
```

### Development
After cloning this repo, make sure to run the following:
```bash
pip install -r requirements
pre-commit install
```

### Theory
There are 3 types of Operators - **Sources**, **Sinks**, and **Non-Terminal Operators.**
Pipelines in Petal are wrappers around arbitrary Directed Acyclic Graphs (DAGs). 
A Pipeline is constructed from a DAG and has the following invariants:
1. **It must have at least 1 Operator satisfying each of the terminal operator types (ie. at least 1 Source and 1 Sink).**
2. **Operators are directional (data flows in a particular direction within the Operator).**
3. **Each Operator has a unique ID and a reference to its upstream and downstream Operators.**
4. **There are no cycles in the graph.**

 

