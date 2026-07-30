from pyats import aetest
import subprocess


class TestBGPGenie(aetest.Testcase):

    @aetest.test
    def test_bgp_with_fallback(self):

        print("\n--- Attempting Genie (expected to fail for FRR) ---")

        # ALWAYS define output first (important fix)
        cmd = "docker exec clab-frr-lab-r1 vtysh -c 'show ip bgp summary'"
        output = subprocess.check_output(cmd, shell=True).decode()

        try:
            from genie.conf import Genie

            # Minimal valid structure (still not useful for FRR)
            testbed = Genie.init({
                "devices": {
                    "r1": {
                        "os": "iosxe",
                        "type": "router",
                        "connections": {
                            "cli": {
                                "protocol": "ssh",
                                "ip": "127.0.0.1"
                            }
                        }
                    }
                }
            })

            device = testbed.devices["r1"]

            parsed = device.parse("show ip bgp summary", output=output)

            print("\n✅ Genie Parsing SUCCESS")
            print(parsed)

        except Exception as e:
            print("\n❌ Genie Parsing FAILED → Using fallback")
            print("Error:", str(e))

            # SAFE fallback (now output exists)
            for line in output.splitlines():
                if "10.0.0.2" in line:
                    parts = line.split()
                    state = parts[-2]

                    assert state.isdigit(), "BGP NOT established"
