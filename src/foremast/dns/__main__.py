"""Create DNS record."""
import argparse
import logging

from ..args import add_app, add_debug, add_env, add_region
from ..consts import LOGGING_FORMAT
from .create_dns import SpinnakerDns


def main():
    """Run newer stuffs."""
    logging.basicConfig(format=LOGGING_FORMAT)
    log = logging.getLogger(__name__)

    parser = argparse.ArgumentParser()
    add_debug(parser)
    add_app(parser)
    add_env(parser)
    add_region(parser)
    parser.add_argument("--elb-subnet",
                        help="Subnetnet type, e.g. external, internal",
                        required=True)
    args = parser.parse_args()

    logging.getLogger(__package__.split('.')[0]).setLevel(args.debug)

    log.debug('Parsed arguments: %s', args)

    # Dictionary containing application info. This is passed to the class for processing
    appinfo = {
        'app': args.app,
        'region': args.region,
        'env': args.env,
        'elb_subnet': args.elb_subnet
    }

    spinnakerapps = SpinnakerDns(app_info=appinfo)
    spinnakerapps.create_elb_dns()


if __name__ == "__main__":
    main()
