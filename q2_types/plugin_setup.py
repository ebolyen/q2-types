# ----------------------------------------------------------------------------
# Copyright (c) 2016-2018, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

import importlib

import qiime2.plugin
import qiime2.sdk

from q2_types import __version__


plugin = qiime2.plugin.Plugin(
    name='types',
    version=__version__,
    website='https://github.com/qiime2/q2-types',
    package='q2_types',
    description=('This QIIME 2 plugin defines semantic types and '
                 'transformers supporting microbiome analysis.'),
    short_description='Plugin defining types for microbiome analysis.'
)

importlib.import_module('q2_types.feature_table')
importlib.import_module('q2_types.distance_matrix')
importlib.import_module('q2_types.tree')
importlib.import_module('q2_types.ordination')
importlib.import_module('q2_types.sample_data')
importlib.import_module('q2_types.feature_data')
importlib.import_module('q2_types.per_sample_sequences')
importlib.import_module('q2_types.multiplexed_sequences')
