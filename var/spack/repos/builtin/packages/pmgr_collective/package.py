##############################################################################
# Copyright (c) 2013, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Written by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/llnl/spack
# Please also see the LICENSE file for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License (as published by
# the Free Software Foundation) version 2.1 dated February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################
from spack import *

class PmgrCollective(Package):
    """PMGR_COLLECTIVE provides a scalable network for bootstrapping
       MPI jobs."""
    homepage = "http://www.sourceforge.net/projects/pmgrcollective"
    url      = "http://downloads.sourceforge.net/project/pmgrcollective/pmgrcollective/PMGR_COLLECTIVE-1.0/pmgr_collective-1.0.tgz"

    version('1.0', '0384d008774274cc3fc7b4d810dfd07e')

    def install(self, spec, prefix):
        make('PREFIX="' + prefix + '"')
        make('PREFIX="' + prefix + '"', "install")
