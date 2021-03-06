# Butterfly: A Plugin for CFD Analysis (GPL) started by Mostapha Sadeghipour Roudsari
# This file is part of Butterfly.
#
# You should have received a copy of the GNU General Public License
# along with Ladybug; If not, see <http://www.gnu.org/licenses/>.
# 
# @license GPL-3.0+ <http://spdx.org/licenses/GPL-3.0+>

"""
Distance refinement.

-

    Args:
        _levels: (d, l) values for level where d is distance of region and 
            l is level of refinement. 'levels' specifies per distance to the
            surface the wanted refinement level.
        
    Returns:
        distance_ref_mode: Refinement mode.
"""

ghenv.Component.Name = "Butterfly_DistanceRefinementMode"
ghenv.Component.NickName = "distRefMode"
ghenv.Component.Message = 'VER 0.0.05\nJAN_12_2019'
ghenv.Component.Category = "Butterfly"
ghenv.Component.SubCategory = "00::Create"
ghenv.Component.AdditionalHelpFromDocStrings = "5"

try:
    from butterfly.refinementRegion import Distance
except ImportError as e:
    msg = '\nFailed to import butterfly:'
    raise ImportError('{}\n{}'.format(msg, e))

_level = [(round(i[0], 4), int(i[1])) for i in _levels]

if _level:
    distance_ref_mode = Distance(_level)
