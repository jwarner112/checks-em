# Checks Em

A small Python utility that compares a generated checksum against a provided one.

Get it? It checks 'em.

# Installation and Usage

TLDR;

1. Clone this repo
2. Install via `pip`
3. Run `checksem --help` for more information

In a terminal window, issue the following:

```bash
$ cd /path/to/repos
/path/to/repos $ `# If you don't have SSH configured, use HTTPS and GitHub credentials instead.`
/path/to/repos $ git clone git@github.com:jwarner112/checksem.git
Cloning into 'checksem'...
remote: Counting objects: 9, done.
remote: Compressing objects: 100% (9/9), done.
remote: Total 9 (delta 1), reused 4 (delta 0), pack-reused 0
Receiving objects: 100% (9/9), 13.84 KiB | 0 bytes/s, done.
Resolving deltas: 100% (1/1), done.
/path/to/repos $ cd checksem
/path/to/repos/checksem $ `# If you want a non-global install, see pip's advanced options`
/path/to/repos/checksem $ pip install .
Processing /path/to/repos/checksem
Requirement already satisfied: click in /usr/local/lib/python2.7/site-packages (from checksem==0.1.2)
Installing collected packages: checksem
  Running setup.py install for checksem ... done
Successfully installed checksem-0.1.2
/path/to/repos/checksem $ `# Verify proper installation...`
/path/to/repos/checksem $ echo "Hello, world" > test.txt
/path/to/repos/checksem $ openssl md5 test.txt > test.txt.md5
/path/to/repos/checksem $ checksem md5 test.txt test.txt.md5
Generating checksum using md5...
Binary:   test.txt
Checksums:
    Generated: a7966bf58e23583c9a5a4059383ff850
    Provided:  a7966bf58e23583c9a5a4059383ff850
OK!
/path/to/repos/checksem $
```
