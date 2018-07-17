# Experimenting with Python imports

## Experiment 1

### Purpose

To check if it's possible to capture all imported modules in one
process/runtime/machine and import exactly the same modules in another.

### Commands 

```bash
$ python dump_modules_to_json.py
$ python import_modules_from_json.py
```

## Experiment 2

### Purpose

To check if it is possible to capture the globals of caller.

### Commands

```bash
$ python obj_caller.py
$ python func_caller.py
```

## Experiment 3

### Purpose

To play around with context manager.

### Commands

```bash
$ python context_manager.py
```
