import importlib
import warnings
from unittest import TestCase, mock

import teamcity_extra


class CompatibilityTest(TestCase):
    def tearDown(self):
        importlib.reload(teamcity_extra)
        super().tearDown()

    def test_tested_versions_do_not_warn(self):
        for version in ('1.32', '1.33', '1.33.0'):
            with self.subTest(version=version), mock.patch('teamcity.__version__', version):
                with warnings.catch_warnings(record=True) as caught:
                    warnings.simplefilter('always')
                    importlib.reload(teamcity_extra)
                self.assertEqual(caught, [])

    def test_newer_versions_warn_without_blocking_import(self):
        for version in ('1.33.1', '1.34rc1', '1.34', '1.100', '2.0'):
            with self.subTest(version=version), mock.patch('teamcity.__version__', version):
                with self.assertWarns(RuntimeWarning) as caught:
                    importlib.reload(teamcity_extra)
                message = str(caught.warning)
                self.assertIn(version, message)
                self.assertIn('has not been tested', message)
                self.assertIn('tested through 1.33', message)
                self.assertIn('https://github.com/fopina/teamcity-messages-extra/issues', message)
