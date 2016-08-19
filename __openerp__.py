# coding: utf-8
{
    "name": "Account Asset Analytic by AbAKUS",
    "version": "9.0.1.0",
    "author": "AbAKUS it-solutions",
    "category": "Accounting",
    "website": "http://www.abakusitsolutions.eu",
    "license": "AGPL-3",
    "depends": [
        "account",
        "account_asset_management",
    ],
    "description": 
    """
Account Asset Analytic for NOVIAT Asset module

This module adds a field 'account analytic' on assets in order to generate depreciation an move lines that are linked to an analytic account.

This module is ispired by VAUXOO's one but transformed to work with NOVIAT's Assets Management module by Valentin THIRION at AbAKUS it-solutions.
    """,
    "data": [
        "view/view.xml",
    ],
}
