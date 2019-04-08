from pprint import pprint

BUF_SIZE = 2048

args = None

def get_filelist(dir):
    from pathlib import Path
    path = Path(dir)

    list = []
    for file_or_dir in path.iterdir():
        if file_or_dir.is_file():
            list.append(file_or_dir.resolve())

    return list


def get_hash(filepath):
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


def main():
    list = []
    hash_dic = {}

    for dir in args.targets:
        list.extend(get_filelist(dir))

    for path in list:
        hash = get_hash(path)
        if hash in hash_dic:
            print("DELETE " + str(path) + " => " + hash + " cause " + hash_dic[hash])
            if args.dryrun == False:
                import os
                os.remove(str(path))
                print(str(path) + " deleted.")
        else:
            hash_dic[hash] = str(path)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='重複ファイル削除プログラム')

    parser.add_argument('targets', nargs='+', help="target directory, not recurcive")
    parser.add_argument('--dry-run', action='store_true', dest="dryrun",
                        help='削除を実行せずに、メッセージのみ表示します。')

    args = parser.parse_args()

    main()