#!/usr/bin/env python
# encoding: utf-8

def schema_from_configuration_items(configurationItems):
    configRequired = list()
    configProperties = dict()
    for configItem in configurationItems:
        configItemName = configItem.get("name")
        configItemProperties = {
            "description": configItem.get("description"),
            "type": configItem.get("type"),
        }
        if configItem.get("multi", True):
            configProperties[configItemName] = {
                "type": "array",
                "items": configItemProperties,
            }
        else:
            configProperties[configItemName] = configItemProperties
        if configItem.get("required", False):
            configRequired.append(configItemName)

    configSchema = {
        "type": "object",
        "properties": configProperties,
        "required": configRequired,
    }
    return configSchema
