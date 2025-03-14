import argparse
import sys

from cshub import mkblockers, mkindex, hublint


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="cshub",
        description="cshub tool with subcommands: mkindex, mkblockers, and hublint."
    )
    subparsers = parser.add_subparsers(dest="subcommand", required=True)

    hublint_parser = hublint.add_subparser(subparsers)
    mkindex.add_subparser(subparsers)
    mkblockers.add_subparser(subparsers)

    args = parser.parse_args()

    try:
        if args.subcommand == "mkindex":
            mkindex.main()
        elif args.subcommand == "mkblockers":
            mkblockers.main()
        elif args.subcommand == "hublint":
            hublint.main(args, hublint_parser)
    except KeyboardInterrupt:
        sys.exit(1)
