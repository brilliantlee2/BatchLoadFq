from collections import namedtuple
import gzip

# a light class for a read in fastq file
read_tuple = namedtuple('read_tuple', ['id', 'seq', 'q_letter'])
def fastq_parser(file_handle):
    while True:
        id = next(file_handle, None)
        if id is None:
            break
        seq = next(file_handle)
        next(file_handle) # skip  '+'
        q_letter = next(file_handle)
        yield read_tuple(id[1:].split()[0], seq.strip(), q_letter.strip()) #每次yield一条read的信息

# split any iterator in to batches  
def batch_iterator(iterator, batch_size):
    """generateor of batches of items in a iterator with batch_size.
    """
    batch = []
    i=0
    for entry in iterator:
        i += 1
        batch.append(entry)
        
        if i == batch_size:
            yield batch
            batch = []
            i = 0
    if len(batch):  #保证批次处理的时候，最后一批不满足batch_size的那些数据，也可以被yield
        yield batch

def read_batch_generator(fastq_fns, batch_size):   #输出batch size read info
    """Generator of barches of reads from list of fastq files

    Args:
        fastq_fns (list): fastq filenames
        batch_size (int, optional):  Defaults to 100.
    """
    for fn in fastq_fns:
        if str(fn).endswith('.gz'):
            with gzip.open(fn, "rt") as handle:
                fastq = fastq_parser(handle)
                read_batch = batch_iterator(fastq, batch_size=batch_size)
                for batch in read_batch:
                    yield batch
        else:
            with open(fn, "r") as handle:
                fastq = fastq_parser(handle)
                read_batch = batch_iterator(fastq, batch_size=batch_size)
                for batch in read_batch:
                    yield batch

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Batch-read FASTQ files.")
    parser.add_argument(
        "-f", "--fq", nargs="+", required=True,
        help="FASTQ/FASTQ.GZ files (space-separated)."
    )
    parser.add_argument(
        "-b", "--batch-size", type=int, default=2,
        help="Batch size (default: 2)."
    )
    args = parser.parse_args()

    test_res = read_batch_generator(args.fq, args.batch_size)

    for batch in test_res:
        if batch:
            print(batch[0].id)
            #print("breakpoint")
