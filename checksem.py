import hashlib
import re

import click


def get_md5(filepath):
    with open(filepath, 'rb') as fd:
        return hashlib.md5(fd.read()).hexdigest()


def get_sha1(filepath):
    with open(filepath, 'rb') as fd:
        return hashlib.sha1(fd.read()).hexdigest()


def get_sha256(filepath):
    with open(filepath, 'rb') as fd:
        return hashlib.sha256(fd.read()).hexdigest()


@click.command()
@click.argument("algorithm", type=click.Choice(["md5", "sha1", "sha256"]))
@click.argument("binary", type=click.Path(exists=True))
@click.argument("checksum", type=click.Path(exists=True))
@click.version_option()
def main(algorithm, binary, checksum):
    """Validates a binary file with its corresponding checksum

        ALGORITHM       Use one of [md5, sha1, sha256] to generate a new checksum
        BINARY          The file from which the checksum will be generated
        CHECKSUM        The file wherein the source checksum is contained
    """

    with open(checksum, 'r') as fd:
        contents = fd.read()
        if algorithm == "sha1":
            gen_checksum = get_sha1(binary)
            src_checksum = re.search(r"[0-9a-fA-F]{40}", contents).group(0)
        elif algorithm == "sha256":
            gen_checksum = get_sha256(binary)
            src_checksum = re.search(r"[0-9a-fA-F]{64}", contents).group(0)
        else:
            gen_checksum = get_md5(binary)
            src_checksum = re.search(r"[0-9a-fA-F]{32}", contents).group(0)

    print "Binary:   {b}".format(b=binary)
    print "Checksums:"
    print "    Generated: {g}".format(g=gen_checksum)
    print "    Provided:  {p}".format(p=src_checksum)
    if gen_checksum == src_checksum:
        print "OK!"
    else:
        print "MISMATCH!"
