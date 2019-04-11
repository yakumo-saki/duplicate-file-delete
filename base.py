from logging import getLogger
logger = getLogger(__name__)

def main(args, get_hash):
    list = []
    hash_dic = {}

    logger.debug("getting file list.")

    for dir in args.targets:
        list.extend(get_filelist(dir))

    logger.debug("total files = " + str(len(list)))
    logger.debug("processing...")

    del_count = 0
    for path in list:
        hash = get_hash(path)
        if hash in hash_dic:
            del_count = del_count + 1
            msg = str(path) + " => " + hash + " cause " + hash_dic[hash]
            if args.dryrun:
                logger.debug("(dry-run) DELETE " + msg)
            else:
                import os
                os.remove(str(path))
                logger.debug("DELETE " + msg)
        else:
            hash_dic[hash] = str(path)
            
    logger.info("DELETE count = " + str(del_count))


def get_filelist(dir):
    from pathlib import Path
    path = Path(dir)

    list = []
    for file_or_dir in path.iterdir():
        if file_or_dir.is_file():
            list.append(file_or_dir.resolve())

    logger.info("file count " + dir + " => " + str(len(list)) )
    return list
