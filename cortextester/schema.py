#!/usr/bin/env python
# encoding: utf-8

from distutils.util import strtobool
from jsonschema.validators import _DEPRECATED_DEFAULT_TYPES

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

def defaults_from_configuration_items(configurationItems):
    defaults = dict()
    for configItem in configurationItems:
        if "defaultValue" in configItem:
            configItemName = configItem.get("name")
            configItemDefaultValue = configItem.get("defaultValue")
            defaults[configItemName] = configItemDefaultValue

    return defaults

def try_cast_configuration_items(config, configSchema):
    for configItemName, configItemProperty in configSchema.get("properties", {}).items():
        if configItemName in config:
            configItemType = configItemProperty.get("type")
            configItemValue = config[configItemName]
            if isinstance(configItemValue, str) and configItemType == "boolean":
                config[configItemName] = bool(strtobool(configItemValue))
                continue

            cast = _DEPRECATED_DEFAULT_TYPES.get(configItemType, type(configItemValue))
            if not isinstance(configItemValue, cast):
                config[configItemName] = cast(configItemValue)

    return config
