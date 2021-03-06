#!/usr/bin/env python3

# (C) Copyright 2020 ECMWF.
#
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation
# nor does it submit to any jurisdiction.
#

import pytest

import climetlab as cml
from climetlab.core.bbox import BoundingBox
from Magics.Magics import MagicsError


def test_settings():

    bbox = BoundingBox(north=90, west=0, east=360, south=-90)

    with pytest.raises(MagicsError):
        cml.plot_map(bounding_box=bbox, projection="polar-north")
