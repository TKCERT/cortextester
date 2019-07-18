#!/usr/bin/env python
# encoding: utf-8

INPUT_SCHEMA = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "$id": "http://thehive-project.org/cortex/analyzer-input.schema.json",
    "title": "Cortex-Analyzer Input",
    "description": "Input to a Cortex analyzer.",
    "type": "object",
    "oneOf": [
        {
            "properties": {
                "dataType": {
                    "description": "Input data type",
                    "type": "string",
                    "not": { "const": "file" }
                },
                "data": {
                    "description": "Input data value",
                    "type": "string"
                },
            },
            "required": ["dataType", "data"]
        },
        {
            "properties": {
                "dataType": {
                    "description": "Input data type",
                    "type": "string",
                    "const": "file"
                },
                "file": {
                    "description": "Input file path",
                    "type": "string"
                },
                "filename": {
                    "description": "Input filename path",
                    "type": "string"
                },
            },
            "required": ["dataType", "file", "filename"]
        }
    ],
    "properties": {
        "tlp": {
            "description": "Input data TLP level",
            "type": "integer",
            "minimum": 0,
            "maximum": 3
        },
        "pap": {
            "description": "Input data PAP level",
            "type": "integer",
            "minimum": 0,
            "maximum": 3
        },
        "config": {
            "description": "Config key and value",
            "type": "object",
            "properties": {
                "check_tlp": {
                    "description": "Check allowed TLP level",
                    "type": "boolean"
                },
                "max_tlp": {
                    "description": "Max allowed TLP level",
                    "type": "integer",
                    "minimum": 0,
                    "maximum": 3
                },
                "check_pap": {
                    "description": "Check allowed PAP level",
                    "type": "boolean"
                },
                "max_pap": {
                    "description": "Max allowed PAP level",
                    "type": "integer",
                    "minimum": 0,
                    "maximum": 3
                },
                "proxy": {
                    "description": "Proxy key and value",
                    "type": "object",
                    "properties": {
                        "http": {"type": "string"},
                        "https": {"type": "string"},
                    }
                }
            }
        }
    },
    "required": ["dataType"]
}

OUTPUT_SCHEMA = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "$id": "http://thehive-project.org/cortex/analyzer-output.schema.json",
    "title": "Cortex-Analyzer Output",
    "description": "Output to a Cortex analyzer.",
    "type": "object",
    "properties": {
        "artifacts": {
            "description": "Extracted artifacts",
            "type": "array",
            "items": {
                "properties": {
                    "dataType": {
                        "description": "Extracted data type",
                        "type": "string",
                        "not": { "const": "file" }
                    },
                    "data": {
                        "description": "Extracted data value",
                        "type": "string"
                    },
                },
                "required": ["dataType", "data"]
            }
        },
        "full": {
            "description": "Full job report",
            "type": "object"
        },
        "success": {
            "description": "Job result",
            "type": "boolean"
        },
        "summary": {
            "description": "Job summary",
            "type": "object",
            "properties": {
                "taxonomies": {
                    "description": "Taxonomies",
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "level": {"type": "string", "enum": ["info", "safe", "suspicious", "malicious"]},
                            "namespace": {"type": "string"},
                            "predicate": {"type": "string"},
                            "value": {"type": "string"}
                        }
                    }
                }
            },
            "required": ["taxonomies"]
        }
    },
    "required": ["artifacts", "full", "success", "summary"]
}
