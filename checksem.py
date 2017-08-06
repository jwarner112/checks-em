import subprocess

import click


def gen_md5(filepath):
   return subprocess.check_output(["openssl", "md5", filepath]).strip().split(" ")[1]


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

    if algorithm == "sha1":
        raise NotImplementedError("To be added in version 0.2")
    elif algorithm == "sha256":
        raise NotImplementedError("To be added in version 0.3")
    else:
        print "Generating checksum using md5..."
        gen_checksum = gen_md5(binary)

    with open(checksum, 'r') as fd:
        src_checksum = fd.read().strip().split(" ")[1]

    print "Binary:   {b}".format(b=binary)
    print "Checksums:"
    print "    Generated: {g}".format(g=gen_checksum)
    print "    Provided:  {p}".format(p=src_checksum)
    if gen_checksum == src_checksum:
        print "OK!"
    else:
        print "MISMATCH!"
