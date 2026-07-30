"""
Job file = entry point for pyATS

This tells pyATS which test script to execute
"""

from pyats.easypy import run

def main():
    # Run your test script
    run(testscript="tests/test_bgp.py")
    run(testscript="tests/test_bgp_with_genie.py")
