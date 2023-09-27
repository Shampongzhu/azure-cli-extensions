# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: disable=too-many-lines
# pylint: disable=too-many-statements

# from azure.cli.core.commands import CliCommandType
from .custom import MoveResourceAdd


def load_command_table(self, _):  # pylint: disable=unused-argument
    self.command_table["resource-mover move-resource add"] = MoveResourceAdd(loader=self)