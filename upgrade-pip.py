import argparse
import auto_upgrade_pip

class VersionAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        self.handle_output(parser, namespace, values)

    @staticmethod
    def handle_output(parser, namespace, values):
        setattr(namespace, "v", values) 

parser = argparse.ArgumentParser(description="imgfit commands")
subparsers = parser.add_subparsers(dest="command", required=False)

subparsers.add_parser("auto", help="Auto mode.")

subparsers.add_parser("select", help="Not auto mode.")

parser.add_argument("-v","--version",nargs="?",action=VersionAction,type=str,help="get the imgfit version.")

args = parser.parse_args()

try:
    if args.command == "auto":
        auto_upgrade_pip.auto()
    elif args.command == "select":
        auto_upgrade_pip.select()
    elif args.v is None:
        pass
except AttributeError:
    print("Version : auto-upgrade-pip:",auto_upgrade_pip.__version__)
else:
    print("done!")