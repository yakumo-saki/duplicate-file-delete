from pprint import pprint
from base import main
from logging import getLogger, StreamHandler, DEBUG, basicConfig

fmt = "%(asctime)s %(levelname)s %(name)s %(message)s"
basicConfig(level=DEBUG, format=fmt)
logger = getLogger(__name__)

def get_hash(filepath):
    from os import path
    import hashlib
    basename = path.basename(filepath)
    logger.debug(filepath + " => " + basename)

    hash = hashlib.sha256()
    hash.update(basename)

    return hash.hexdigest()  # hashする必要はないけれども...


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='重複ファイル削除プログラム')

    parser.add_argument('targets', nargs='+', help="target directory, not recurcive")
    parser.add_argument('--dry-run', action='store_true', dest="dryrun",
                        help='削除を実行せずに、メッセージのみ表示します。')

    args = parser.parse_args()

    logger.debug(args)

    main(args, get_hash)
