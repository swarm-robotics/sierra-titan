# Copyright 2022 John Harwell, All rights reserved.
#
#  SPDX-License-Identifier: MIT
#
"""
Classes for the constant population density batch criteria for use in the TITAN
project.
"""

# Core packages

# 3rd party packages
import implements
from sierra.plugins.platform.argos.variables import population_constant_density as pcd
from sierra.plugins.platform.argos.variables import constant_density as cd
from sierra.core import types, utils

# Project packages
import titerra.variables.batch_criteria as bc


@implements.implements(bc.IPMQueryableBatchCriteria)
class PopulationConstantDensity(pcd.PopulationConstantDensity):
    """Extends :class:`~pcd.PopulationConstantDensity` with performance measure
    bits.

    """

    def __init__(self, *args, **kwargs) -> None:
        pcd.PopulationConstantDensity.__init__(self, *args, **kwargs)

    def pm_query(self, pm: str) -> bool:
        return pm in ['raw', 'scalability', 'self-org']


def factory(cli_arg: str,
            main_config: types.YAMLDict,
            cmdopts: types.Cmdopts,
            **kwargs) -> PopulationConstantDensity:
    """
    Factory to create :class:`PopulationConstantDensity` derived classes from
    the command line definition.

    """
    attr = cd.Parser()(cli_arg)
    kw = utils.gen_scenario_spec(cmdopts, **kwargs)
    dims = pcd.calc_dims(cmdopts, attr, **kwargs)

    def __init__(self) -> None:
        PopulationConstantDensity.__init__(self,
                                           cli_arg,
                                           main_config,
                                           cmdopts['batch_input_root'],
                                           attr["target_density"],
                                           dims,
                                           kw['scenario_tag'])

    return type(cli_arg,  # type: ignore
                (PopulationConstantDensity,),
                {"__init__": __init__})


__api__ = [
    'PopulationConstantDensity'
]