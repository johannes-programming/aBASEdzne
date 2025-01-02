import unittest
import tempfile
import os

# Import your package or main function
from aBASEdzne.core import main

class TestABASEdzne(unittest.TestCase):
    def test_creates_output_file(self):
        # Create a temporary directory that will be cleaned up automatically
        with tempfile.TemporaryDirectory() as tmpdir:
            # Construct the output filename within this temp directory
            outfile = os.path.join(tmpdir, "aBASE-output.xlsm")

            # Call your main function with the desired arguments
            main([
                "--hchain", "G4:G300",
                "--heavykeys", "H3:W3",
                "--kchain", "Y4:Y300",
                "--kappakeys", "Z3:AM3",
                "--lchain", "AO4:AO300",
                "--lambdakeys", "AP3:BC3",
                "--dataprefix=/data/SeqData/",
                "/data/aBASE-113-input.xlsx",
                outfile
            ])

            # Assert that the output file now exists
            self.assertTrue(
                os.path.exists(outfile),
                msg=f"Expected output file '{outfile}' not found."
            )

if __name__ == "__main__":
    unittest.main()
