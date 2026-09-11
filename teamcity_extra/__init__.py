import warnings

from packaging.version import Version
from teamcity import __version__ as _teamcity_version

__version__ = '1.2.0'

if Version(_teamcity_version) > Version('1.33'):
    warnings.warn(
        f'teamcity-messages {_teamcity_version} has not been tested with teamcity-messages-extra '
        '(tested through 1.33). Compatibility needs to be reviewed; please open a GitHub issue at '
        'https://github.com/fopina/teamcity-messages-extra/issues.',
        RuntimeWarning,
        stacklevel=2,
    )
