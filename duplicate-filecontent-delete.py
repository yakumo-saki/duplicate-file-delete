from pprint import pprint
from base import main
from logging import getLogger, StreamHandler, DEBUG, basicConfig

fmt = "%(asctime)s %(levelname)s %(name)s %(message)s"
basicConfig(level=DEBUG, format=fmt)
logger = getLogger(__name__)

def get_hash(filepath):
    BUF_SIZE = 2048

    import hashlib
    hash = hashlib.sha256()

    # read file and get hash
    with open(filepath, 'rb') as f:
        while True:
            chunk = f.read(BUF_SIZE * hash.block_size)
            if len(chunk) != 0:
                hash.update(chunk)
            else:
                break    # end of file

    return hash.hexdigest()


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='重複ファイル削除プログラム')

    parser.add_argument('targets', nargs='+', help="target directory, not recurcive")
    parser.add_argument('--dry-run', action='store_true', dest="dryrun",
                        help='削除を実行せずに、メッセージのみ表示します。')

    args = parser.parse_args()

    logger.debug(args)

    main(args, get_hash)
