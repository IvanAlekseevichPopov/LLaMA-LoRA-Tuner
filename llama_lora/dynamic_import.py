import importlib


def dynamic_import(module):
    return importlib.import_module(module, package='llama_lora')
