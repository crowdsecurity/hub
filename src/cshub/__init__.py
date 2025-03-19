import argparse
import sys

from cshub import hublint, mkblockers, mkindex


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="cshub",
        description="cshub tool with subcommands: mkindex, mkblockers, and hublint.",
    )
    subparsers = parser.add_subparsers(dest="subcommand", required=True)

    hublint_parser = hublint.add_subparser(subparsers)
    _ = mkindex.add_subparser(subparsers)
    _ = mkblockers.add_subparser(subparsers)

    args = parser.parse_args()

    try:
        if args.subcommand == "mkindex":
            mkindex.main(args)
        elif args.subcommand == "mkblockers":
            mkblockers.main(args)
        elif args.subcommand == "hublint":
            hublint.main(args, hublint_parser)
    except KeyboardInterrupt:
        sys.exit(1)
