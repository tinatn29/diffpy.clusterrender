import argparse

from diffpy.clusterrender.version import __version__  # noqa


def main():
    parser = argparse.ArgumentParser(
        prog="diffpy.clusterrender",
        description=(
            "Package for high throughput 3D rendering of clusters of atoms for visualization and comparison\n\n"
            "For more information, visit: "
            "https://github.com/diffpy/diffpy.clusterrender/"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    parser.add_argument(
        "--version",
        action="store_true",
        help="Show the program's version number and exit",
    )

    args = parser.parse_args()

    if args.version:
        print(f"diffpy.clusterrender {__version__}")
    else:
        # Default behavior when no arguments are given
        parser.print_help()


if __name__ == "__main__":
    main()
