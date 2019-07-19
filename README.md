# cortextester

Inspired by [cortexutils](https://github.com/TheHive-Project/cortexutils) - a testing framework for Cortex-Analyzers (and maybe Responders at some point)

This set of Python tools can be used to create and validate the JSON-input passed to [Cortex-Analyzers](https://github.com/TheHive-Project/Cortex-Analyzers/) and their generated JSON-output. The goal is to make development and testing easier without depending on a full [Cortex](https://github.com/TheHive-Project/CortexDocs) installation.

## Requirements

* Python 3.6+
    * [jsonschema](https://github.com/Julian/jsonschema)

Special thanks to this great [json-schema.org](https://json-schema.org/) validation library!

## Usage

Validate JSON-config related to a Cortex-Analyzer:
```
cat <your-json-config-file> | analyzer-config
```

Validate JSON-input passed to a Cortex-Analyzer:
```
cat <your-json-input-file> | analyzer-input
```

Validate JSON-output created by a Cortex-Analyzer:
```
<your-cortex-analyzer> | analyzer-output
```

Create JSON-input for a Cortex-Analyzer via arguments:
```
analyzer-input -t "domain" -v "thehive-project.org"
```

Validate this JSON-input again if passed via piping:
```
analyzer-input -t "domain" -v "thehive-project.org" | analyzer-input
```

Pass this JSON-input to a Cortex-Analyzer for testing and development:
```
analyzer-input -t "domain" -v "thehive-project.org" | <your-cortex-analyzer>
```

Validate the whole process including a Cortex-Analyzer:
```
analyzer-input -t "domain" -v "thehive-project.org" | <your-cortex-analyzer> | analyzer-output
```

For more information about the usage of the tools, see:
```
analyzer-config --help
analyzer-input --help
analyzer-output --help
```

## Roadmap

Some ideas for the future development of cortextester:

* Create and validate JSON-input for Responders.
* Validate the JSON-output of Responders.
