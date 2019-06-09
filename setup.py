#! /usr/bin/env python
# -*- coding: utf-8 -*-
import odooClient
from setuptools import setup, find_packages

setup(
    name='odoo_jsonrpc_client',
    version=odooClient.__version__,
    description="Another python json-rpc client",
    author="Pyhunterpig",
    license='LGPL v3',
    author_email="hunterpig75@qq.com",
    packages=['odooClient'],
    platforms = 'any',
    install_requires = [
       'requests>=2.0',
    ],
    url = "https://github.com/pyhunterpig/odoo_jsonrpc_client",
)