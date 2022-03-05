import argparse
import logging


def export_log():
    logging.basicConfig(
        filename="files/log.txt",
        format="%(asctime)s:%(levelname)s:%(message)s",
        level=logging.INFO,
    )


def arg_parse():
    """parse command arguments"""
    parser = argparse.ArgumentParser(
        description="Drone photographing in assigh area using different strategy."
    )
    parser.add_argument(
        "-l",
        "--length",
        type=int,
        help="The length of area, int is required, such as 7",
        required=True,
    )
    parser.add_argument(
        "-s",
        "--strategy",
        default="snake shape",
        help="different move strategy for drone, such as 'snake shape'.",
    )

    args = parser.parse_args()
    area = (args.length, args.length)
    strategy = args.strategy
    return area, strategy
