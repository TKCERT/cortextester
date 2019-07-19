#!/usr/bin/env python
# encoding: utf-8

INPUT_SCHEMA = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "$id": "https://github.com/TKCERT/cortextester/responder-input.schema.json",
    "title": "Cortex-Responder Input",
    "description": "Input to a Cortex responder.",
    "type": "object",
    "properties": {
        "dataType": {
            "description": "Input data type",
            "type": "string",
            "enum": ["thehive:case", "thehive:case_artifact", "thehive:alert",
                     "thehive:case_task", "thehive:case_task_log"]
        },
        "data": {
            "description": "Input data structure",
            "type": "object"
        },
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
    "required": ["dataType", "data"]
}

OUTPUT_SCHEMA = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "$id": "https://github.com/TKCERT/cortextester/responder-output.schema.json",
    "title": "Cortex-Responder Output",
    "description": "Output to a Cortex responder.",
    "type": "object",
    "oneOf": [
        {
            "properties": {
                "full": {
                    "description": "Full job report",
                    "type": "object"
                },
                "operations": {
                    "description": "Requested operations",
                    "type": "array",
                    "items": {
                        "type": "object",
                        "oneOf": [
                            {
                                "properties": {
                                    "type": {"type": "string", "enum": ["AddTagToArtifact", "AddTagToCase"]},
                                    "tag": {"type": "string"}
                                },
                                "required": ["type", "tag"]
                            },
                            {
                                "properties": {
                                    "type": {"type": "string", "const": "MarkAlertAsRead"}
                                },
                                "required": ["type"]
                            },
                            {
                                "properties": {
                                    "type": {"type": "string", "const": "AddCustomField"},
                                    "name": {"type": "string"},
                                    "value": {"description": "Value of any type"},
                                    "tpe": {"type": "string"}
                                },
                                "required": ["type", "name", "value", "tpe"]
                            },
                        ]
                    },
                },
                "success": {
                    "description": "Job result",
                    "type": "boolean",
                    "const": True
                }
            },
            "required": ["full", "operations", "success"]
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
    "$id": "https://github.com/TKCERT/cortextester/responder-config.schema.json",
    "title": "Cortex-Responder Config",
    "description": "Config to a Cortex responder.",
    "type": "object",
    "properties": {
        "name": {
            "description": "Name of the responder",
            "type": "string"
        },
        "version": {
            "description": "Version of the responder",
            "type": "string"
        },
        "author": {
            "description": "Author of the responder",
            "type": "string"
        },
        "url": {
            "description": "URL to find the responder",
            "type": "string"
        },
        "license": {
            "description": "License of the responder",
            "type": "string"
        },
        "description": {
            "description": "Description of the responder",
            "type": "string"
        },
        "dataTypeList": {
            "description": "List of dataTypes the responder can handle",
            "type": "array",
            "items": {
                "description": "Type of data the responder can handle",
                "type": "string",
                "enum": ["thehive:case", "thehive:case_artifact", "thehive:alert",
                         "thehive:case_task", "thehive:case_task_log"]
            }
        },
        "command": {
            "description": "Command to execute the responder",
            "type": "string"
        },
        "baseConfig": {
            "description": "Base configuration name of the responder",
            "type": "string"
        },
        "config": {
            "description": "Configuration of the responder",
            "type": "object"
        },
        "configurationItems": {
            "description": "Configuration items of the responder",
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
                        "type": "string",
                        "enum": ["text", "string", "number", "boolean"]
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
