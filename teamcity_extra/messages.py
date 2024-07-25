from teamcity.messages import TeamcityServiceMessages as _TSM


class TeamcityServiceMessages(_TSM):
    def testMetadata(self, testName, name, value='', type='', flowId=None):
        # https://www.jetbrains.com/help/teamcity/reporting-test-metadata.html#Reporting+Additional+Test+Data
        self.message('testMetadata', name=name, testName=testName, value=value, type=type, flowId=flowId)

    def buildStatisticValue(self, key, value):
        # https://www.jetbrains.com/help/teamcity/service-messages.html#Reporting+Build+Statistics
        self.message('buildStatisticValue', key=key, value=str(value))

    def addBuildTag(self, tag):
        # https://www.jetbrains.com/help/teamcity/service-messages.html#Adding+and+Removing+Build+Tags
        self._single_value_message('addBuildTag', tag)

    def removeBuildTag(self, tag):
        # https://www.jetbrains.com/help/teamcity/service-messages.html#Adding+and+Removing+Build+Tags
        self._single_value_message('removeBuildTag', tag)
