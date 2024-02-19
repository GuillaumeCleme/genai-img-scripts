import argparse
import os
import json
import glob
from pathlib import Path

def main(args):
    #List all images in the directory
    dir_path = Path(args.captions_dir)
    input_file = Path(args.input_file)

    i = 0
    with open(input_file, 'r') as f:
        for line in f:
            print(line)
            i += 1
    
    print(f"Total files processed: {i}")

def setup_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", type=str, help="JSONL input file containing captions")
    parser.add_argument("captions_dir", type=str, help="Directory where captions should be written")
    parser.add_argument(
        "--caption_extension",
        type=str,
        default="txt",
        help="Extension of caption files",
    )
    parser.add_argument(
        "--ref_prefix",
        type=bool,
        default=True,
        help="Extract the file name from the image-ref tags? (default: True)",
    )

    return parser


if __name__ == "__main__":
    parser = setup_parser()
    args = parser.parse_args()

    main(args)
