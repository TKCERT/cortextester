#!/usr/bin/env python
# encoding: utf-8

INPUT_SCHEMA = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "$id": "https://github.com/TKCERT/cortextester/analyzer-input.schema.json",
    "title": "Cortex-Analyzer Input",
    "description": "Input to a Cortex analyzer.",
    "type": "object",
    "oneOf": [
        {
            "properties": {
                "dataType": {
                    "description": "Input data type",
                    "type": "string",
                    "enum": ["domain", "file", "filename", "fqdn", "hash", "ip", "mail", "mail_subject",
                             "other", "regexp", "registry", "uri_path", "url", "user-agent"],
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
                    "enum": ["domain", "file", "filename", "fqdn", "hash", "ip", "mail", "mail_subject",
                             "other", "regexp", "registry", "uri_path", "url", "user-agent"],
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
                    "minimum": -1,
                    "maximum": 3
                },
                "check_pap": {
                    "description": "Check allowed PAP level",
                    "type": "boolean"
                },
                "max_pap": {
                    "description": "Max allowed PAP level",
                    "type": "integer",
                    "minimum": -1,
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
    "$id": "https://github.com/TKCERT/cortextester/analyzer-output.schema.json",
    "title": "Cortex-Analyzer Output",
    "description": "Output to a Cortex analyzer.",
    "type": "object",
    "oneOf": [
        {
            "properties": {
                "artifacts": {
                    "description": "Extracted artifacts",
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "dataType": {
                                "description": "Extracted data type",
                                "type": "string",
                                "enum": ["domain", "file", "filename", "fqdn", "hash", "ip", "mail", "mail_subject",
                                         "other", "regexp", "registry", "uri_path", "url", "user-agent"],
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
                                },
                                "required": ["level", "namespace", "predicate", "value"]
                            }
                        }
                    },
                    "required": ["taxonomies"]
                },
                "success": {
                    "description": "Job result",
                    "type": "boolean",
                    "const": True
                }
            },
            "required": ["artifacts", "full", "summary", "success"]
        },
        {
            "properties": {
                "input": {
                    "description": "Original job input",
                    "type": "object"
                },
                "errorMessage": {
                    "description": "Error message",
                    "type": "string"
                },
                "success": {
                    "description": "Job result",
                    "type": "boolean",
                    "const": False
                }
            },
            "required": ["errorMessage", "success"]
        }
    ],
    "properties": {
        "success": {
            "description": "Job result",
            "type": "boolean"
        }
    },
    "required": ["success"]
}

CONFIG_SCHEMA = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "$id": "https://github.com/TKCERT/cortextester/analyzer-config.schema.json",
    "title": "Cortex-Analyzer Config",
    "description": "Config to a Cortex analyzer.",
    "type": "object",
    "properties": {
        "name": {
            "description": "Name of the analyzer",
            "type": "string"
        },
        "version": {
            "description": "Version of the analyzer",
            "type": "string"
        },
        "author": {
            "description": "Author of the analyzer",
            "type": "string"
        },
        "url": {
            "description": "URL to find the analyzer",
            "type": "string"
        },
        "license": {
            "description": "License of the analyzer",
            "type": "string"
        },
        "description": {
            "description": "Description of the analyzer",
            "type": "string"
        },
        "dataTypeList": {
            "description": "List of dataTypes the analyzer can handle",
            "type": "array",
            "items": {
                "description": "Type of data the analyzer can handle",
                "type": "string"
            }
        },
        "command": {
            "description": "Command to execute the analyzer",
            "type": "string"
        },
        "baseConfig": {
            "description": "Base configuration name of the analyzer",
            "type": "string"
        },
        "config": {
            "description": "Configuration of the analyzer",
            "type": "object"
        },
        "configurationItems": {
            "description": "Configuration items of the analyzer",
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "name": {
                        "description": "Name of the configuration item",
                        "type": "string"
                    },
                    "description": {
                        "description": "Description of the configuration item",
                        "type": "string"
                    },
                    "type": {
                        "description": "Type of the configuration item value",
                        "type": "string"
                    },
                    "multi": {
                        "description": "Flag if the configuration item can have multiple values",
                        "type": "boolean"
                    },
                    "required": {
                        "description": "Flag if the configuration item is required",
                        "type": "boolean"
                    },
                    "defaultValue": {
                        "description": "Default value of the configuration item"
                    },
                },
                "required": ["name", "description", "type", "multi", "required"]
            }
        }
    },
    "required": ["name", "version", "author", "url", "license", "description",
                 "dataTypeList", "command", "baseConfig"]
}
