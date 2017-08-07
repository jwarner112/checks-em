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
/path/to/repos/checksem $ `# If you want a non-global install, use this script as a base but don't use it.`
/path/to/repos/checksem $ sudo ./install.sh
[sudo] password for user: 
========================================
Installing...
The directory '/home/jwarner/.cache/pip/http' or its parent directory is not owned by the current user and the cache has been disabled. Please check the permissions and owner of that directory. If executing pip with sudo, you may want sudo's -H flag.
The directory '/home/jwarner/.cache/pip' or its parent directory is not owned by the current user and caching wheels has been disabled. check the permissions and owner of that directory. If executing pip with sudo, you may want sudo's -H flag.
Processing /home/jwarner/repos/checksem
/usr/local/lib/python2.7/dist-packages/pip/_vendor/requests/packages/urllib3/util/ssl_.py:318: SNIMissingWarning: An HTTPS request has been made, but the SNI (Subject Name Indication) extension to TLS is not available on this platform. This may cause the server to present an incorrect TLS certificate, which can cause validation failures. You can upgrade to a newer version of Python to solve this. For more information, see https://urllib3.readthedocs.io/en/latest/security.html#snimissingwarning.
  SNIMissingWarning
/usr/local/lib/python2.7/dist-packages/pip/_vendor/requests/packages/urllib3/util/ssl_.py:122: InsecurePlatformWarning: A true SSLContext object is not available. This prevents urllib3 from configuring SSL appropriately and may cause certain SSL connections to fail. You can upgrade to a newer version of Python to solve this. For more information, see https://urllib3.readthedocs.io/en/latest/security.html#insecureplatformwarning.
  InsecurePlatformWarning
Requirement already up-to-date: click in /usr/local/lib/python2.7/dist-packages (from checksem==0.3.2)
Installing collected packages: checksem
  Found existing installation: checksem 0.3.2
    Uninstalling checksem-0.3.2:
      Successfully uninstalled checksem-0.3.2
  Running setup.py install for checksem ... done
Successfully installed checksem-0.3.2
Verifying...
Binary:   test.txt
Checksums:
    Generated: a7966bf58e23583c9a5a4059383ff850
    Provided:  a7966bf58e23583c9a5a4059383ff850
OK!
If above reads 'MISMATCH!' instead of 'OK!', an error has occurred.
========================================
/path/to/repos/checksem $
```
