"""
This is a pyATS test file.

Concept:
- Connect to routers (via docker)
- Run BGP command
- Validate output
"""

from pyats import aetest
import subprocess
import re


class TestBGP(aetest.Testcase):

    @aetest.test
    def check_bgp_neighbors(self):
        """
        Test:
        Verify BGP session is established on r1
        """

        cmd = "docker exec clab-frr-lab-r1 vtysh -c 'show ip bgp summary'"
        output = subprocess.check_output(cmd, shell=True).decode()

        print(output)
        match = re.search(r"\s+\d+\s*$", output, re.MULTILINE)
        # Assertion 1: BGP must be up
        assert match, "BGP is NOT established"


    @aetest.test
    def check_prefix_learning(self):
        """
        Test:
        Verify routes are learned
        """

        cmd = "docker exec clab-frr-lab-r1 vtysh -c 'show ip bgp'"
        output = subprocess.check_output(cmd, shell=True).decode()

        print(output)

        # Assertion 2: Check for learned prefix
        assert "10.0.1.0/24" in output, "Prefix not learned"
