import argparse
import auto_upgrade_pip

parser = argparse.ArgumentParser(description="imgfit commands")
subparsers = parser.add_subparsers(dest="command", required=True)

subparsers.add_parser("auto", help="Auto mode.")
subparsers.add_parser("manual", help="Manual mode.")
subparsers.add_parser("version",help="get the version.")
custom = subparsers.add_parser("customize",help="customize mode,same as 'pip install --upgrade [customize]'")
custom.add_argument("options",help="Same as 'pip install --upgrade [customize]'",nargs="+")

args = parser.parse_args()

if args.command == "auto":
    auto_upgrade_pip.auto()
elif args.command == "manual":
    auto_upgrade_pip.select()
elif args.command == "customize":
    print(args)
    auto_upgrade_pip.customize(args.options)
elif args.command == "version":
    print("Version : auto-upgrade-pip",auto_upgrade_pip.__version__)