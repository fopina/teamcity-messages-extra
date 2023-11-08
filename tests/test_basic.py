from unittest import TestCase
import io

from teamcity_extra import messages

class Test(TestCase):
    def test_constructor(self):
        messages.TeamcityServiceMessages()

    def test_metadata(self):
        out = io.BytesIO()
        tsm = messages.TeamcityServiceMessages(output=out)
        tsm.testMetadata('testName', 'link', value='https://github.com', type='link')
        self.assertEqual(
            out.getvalue(),
            b"##teamcity[testMetadata timestamp='2023[90 chars]']\n"
        )