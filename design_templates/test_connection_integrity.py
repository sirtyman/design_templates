from unittest import TestCase, main

from design_templates.common.utils import check_connection


class TestIntegrity(TestCase):
    @classmethod
    def setupClass(cls):
        """**Test script pre-conditions**

        - Setup the channel to DUT
        """
        pass

    @classmethod
    def tearDownClass(cls):
        """**Test script post-conditions**

        - Close the channel to DUT
        """
        pass

    def setUp(self):
        """**TestCase pre-conditions**

        - DUT is in the X state
        - Application X downloaded to DUT
        - Task A is inhibited
        - All connections with external devices are set
        - All connections are not flickering over 20 s
        """
        pass

    def tearDown(self):
        """**TestCase post-conditions**

        - Blanc the DUT
        """

    def scenario_1(self):
        """**Scenario**

        - *Given*:
            - DUT connected to the Ethernet
            - And connection rate set to the highest rate

        - *When*:
            - Un-inhibiting task
            - And when waiting TEST_WAIT time [s]

        - *Then*:
            - All connections are preserved during the TEST_WAIT time
            - And data integrity is preserved during the TEST_WAIT time
        """
        pass


if __name__ == "__main__":
    main()