# cortextester

Inspired by [cortexutils](https://github.com/TheHive-Project/cortexutils) - a testing framework for Cortex-Analyzers (and maybe Responders at some point)

This little tool can be used to create and validate the JSON-input passed to [Cortex-Analyzers](https://github.com/TheHive-Project/Cortex-Analyzers/) and their generated JSON-output. The goal is to make development and testing easier without depending on a full [Cortex](https://github.com/TheHive-Project/CortexDocs) installation.

## Requirements

* Python 3.6+
    * [jsonschema](https://github.com/Julian/jsonschema)

Special thanks to this great [json-schema.org](https://json-schema.org/) validation library!

## Usage

Validate JSON-input passed to a Cortex-Analyzer:
```
cat <your-json-input-file> | python analyzer-input.py
```

Validate JSON-output created by a Cortex-Analyzer:
```
<your-cortex-analyzer> | python analyzer-output.py
```

Create JSON-input for a Cortex-Analyzer via arguments:
```
python analyzer-input.py -t "domain" -v "thehive-project.org"
```

Validate this JSON-input again if passed via piping:
```
python analyzer-input.py -t "domain" -v "thehive-project.org" | python analyzer-input.py
```

Pass this JSON-input to a Cortex-Analyzer for testing and development:
```
python analyzer-input.py -t "domain" -v "thehive-project.org" | <your-cortex-analyzer>
```

Validate the whole process including a Cortex-Analyzer:
```
python analyzer-input.py -t "domain" -v "thehive-project.org" | <your-cortex-analyzer> | python analyzer-output.py
```

For more information about the usage of `analyzer-input.py`, see:
```
python analyzer-input.py --help
```

## Roadmap

Some ideas for the future development of cortextester:

* Make the main programs of this tool installable to `PATH` or usable via `python -m`.
* Create and validate JSON-input for Responders.
* Validate the JSON-output of Responders.
