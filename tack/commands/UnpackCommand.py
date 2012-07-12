# Authors: 
#   Trevor Perrin
#   Moxie Marlinspike
#
# See the LICENSE file for legal information regarding use of this file.

import sys
from tack.commands.Command import Command
from tack.structures.TackActivation import TackActivation
from tack.structures.TackExtension import TackExtension
from tack.tls.TlsCertificate import TlsCertificate

class UnpackCommand(Command):

    def __init__(self, argv):
        Command.__init__(self, argv, "oE", "vx")
        self.outputFile, self.outputFileName = self.getOutputFile()
        self.tackExtension = self.getTackExtension(mandatory=True)

    def execute(self):
        if self.tackExtension.tack:
            self.outputFile.write(self.tackExtension.tack.serializeAsPem())
        for break_sig in self.tackExtension.break_sigs:
            self.outputFile.write(break_sig.serializeAsPem())
        self.printVerbose(str(self.tackExtension))

    @staticmethod
    def printHelp():
        print(
"""Takes the input TACK Extension, and writes out PEM encodings for its Tack 
and Break Signatures.

  unpack -e EXTENSION

Optional arguments:
  -v                 : Verbose
  -o FILE            : Write the output to this file (instead of stdout)
""")