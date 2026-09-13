# For App image Scanning:
```
barq-assessment-app-01:latest (debian 12.15)
  ============================================
  Total: 62 (HIGH: 57, CRITICAL: 5)
  
  ┌──────────────────┬────────────────┬──────────┬──────────────┬────────────────────┬─────────────────┬──────────────────────────────────────────────────────────────┐
  │     Library      │ Vulnerability  │ Severity │    Status    │ Installed Version  │  Fixed Version  │                            Title                             │
  ├──────────────────┼────────────────┼──────────┼──────────────┼────────────────────┼─────────────────┼──────────────────────────────────────────────────────────────┤
  │ bsdutils         │ CVE-2026-53613 │ HIGH     │ affected     │ 1:2.38.1-5+deb12u3 │                 │ util-linux: util-linux: TOCTOU in the mount program via      │
  │                  │                │          │              │                    │                 │ ancestor directory swap on...                                │
  │                  │                │          │              │                    │                 │ https://avd.aquasec.com/nvd/cve-2026-53613                   │
  │                  ├────────────────┤          │              │                    ├─────────────────┼──────────────────────────────────────────────────────────────┤
  │                  │ CVE-2026-76642 │          │              │                    │                 │ util-linux: util-linux: failed external mount helper still   │
  │                  │                │          │              │                    │                 │ runs privileged X-mount post-hooks                           │
  │                  │                │          │              │                    │                 │ https://avd.aquasec.com/nvd/cve-2026-76642                   │
  │                  ├────────────────┤          │              │                    ├─────────────────┼──────────────────────────────────────────────────────────────┤
  │                  │ CVE-2026-78408 │          │              │                    │                 │ util-linux: util-linux: nsenter --join-cgroup leaks root     │
  │                  │                │          │              │                    │                 │ cgroup migration authority                                   │
  │                  │                │          │              │                    │                 │ https://avd.aquasec.com/nvd/cve-2026-78408                   │
  │                  ├────────────────┤          │              │                    ├─────────────────┼──────────────────────────────────────────────────────────────┤
  │                  │ CVE-2026-78409 │          │              │                    │                 │ util-linux: util-linux: X-mount.subdir detached-tree         │
  │                  │                │          │              │                    │                 │ resolution can escape via intermediate symlinks              │
  │                  │                │          │              │                    │                 │ https://avd.aquasec.com/nvd/cve-2026-78409                   │
  │                  ├────────────────┤          │              │                    ├─────────────────┼──────────────────────────────────────────────────────────────┤
  │                  │ CVE-2026-78410 │          │              │                    │                 │ util-linux: util-linux: restricted bind mounts do not pin    │
  │                  │                │          │              │                    │                 │ the source, allowing X-mount.owner/group/mode...             │
  │                  │                │          │              │                    │                 │ https://avd.aquasec.com/nvd/cve-2026-78410                   │
  ├──────────────────┼────────────────┤          ├──────────────┼────────────────────┼─────────────────┼──────────────────────────────────────────────────────────────┤
  │ gzip             │ CVE-2026-41992 │          │ fix_deferred │ 1.12-1             │                 │ gzip: gzip: Information disclosure via global buffer         │
  │                  │                │          │              │                    │                 │ overflow in LZH decompression                                │
  │                  │                │          │              │                    │                 │ https://avd.aquasec.com/nvd/cve-2026-41992                   │
  ├──────────────────┼────────────────┤          │              ├────────────────────┼─────────────────┼──────────────────────────────────────────────────────────────┤
  │ libacl1          │ CVE-2026-54369 │          │              │ 2.3.1-3            │                 │ acl: Symlink traversal privilege escalation via libacl       │
  │                  │                │          │              │                    │                 │ functions                                                    │
  │                  │                │          │              │                    │                 │ https://avd.aquasec.com/nvd/cve-2026-54369                   │
  ├──────────────────┼────────────────┤          ├──────────────┼────────────────────┼─────────────────┼──────────────────────────────────────────────────────────────┤
  │ libblkid1        │ CVE-2026-53613 │          │ affected     │ 2.38.1-5+deb12u3   │                 │ util-linux: util-linux: TOCTOU in the mount program via      │
  │                  │                │          │              │                    │                 │ ancestor directory swap on...                                │
  │                  │                │          │              │                    │                 │ https://avd.aquasec.com/nvd/cve-2026-53613                   │
  │                  ├────────────────┤          │              │                    ├─────────────────┼──────────────────────────────────────────────────────────────┤
  │                  │ CVE-2026-76642 │          │              │                    │                 │ util-linux: util-linux: failed external mount helper still   │
  │                  │                │          │              │                    │                 │ runs privileged X-mount post-hooks                           │
  │                  │                │          │              │                    │                 │ https://avd.aquasec.com/nvd/cve-2026-76642                   │
  │                  ├────────────────┤          │              │                    ├─────────────────┼──────────────────────────────────────────────────────────────┤
  │                  │ CVE-2026-78408 │          │              │                    │                 │ util-linux: util-linux: nsenter --join-cgroup leaks root     │
  │                  │                │          │              │                    │                 │ cgroup migration authority                                   │
  │                  │                │          │              │                    │                 │ https://avd.aquasec.com/nvd/cve-2026-78408                   │
  │                  ├────────────────┤          │              │                    ├─────────────────┼──────────────────────────────────────────────────────────────┤
  │                  │ CVE-2026-78409 │          │              │                    │                 │ util-linux: util-linux: X-mount.subdir detached-tree         │
  │                  │                │          │              │                    │                 │ resolution can escape via intermediate symlinks              │
  │                  │                │          │              │                    │                 │ https://avd.aquasec.com/nvd/cve-2026-78409                   │
  │                  ├────────────────┤          │              │                    ├─────────────────┼──────────────────────────────────────────────────────────────┤
  │                  │ CVE-2026-78410 │          │              │                    │                 │ util-linux: util-linux: restricted bind mounts do not pin    │
  │                  │                │          │              │                    │                 │ the source, allowing X-mount.owner/group/mode...             │
  │                  │                │          │              │                    │                 │ https://avd.aquasec.com/nvd/cve-2026-78410                   │
  ├──────────────────┼────────────────┤          │              │                    ├─────────────────┼──────────────────────────────────────────────────────────────┤
  │ libmount1        │ CVE-2026-53613 │          │              │                    │                 │ util-linux: util-linux: TOCTOU in the mount program via      │
  │                  │                │          │              │                    │                 │ ancestor directory swap on...                                │
  │                  │                │          │              │                    │                 │ https://avd.aquasec.com/nvd/cve-2026-53613                   │
  │                  ├────────────────┤          │              │                    ├─────────────────┼──────────────────────────────────────────────────────────────┤
  │                  │ CVE-2026-76642 │          │              │                    │                 │ util-linux: util-linux: failed external mount helper still   │
  │                  │                │          │              │                    │                 │ runs privileged X-mount post-hooks                           │
  │                  │                │          │              │                    │                 │ https://avd.aquasec.com/nvd/cve-2026-76642                   │
  │                  ├────────────────┤          │              │                    ├─────────────────┼──────────────────────────────────────────────────────────────┤
  │                  │ CVE-2026-78408 │          │              │                    │                 │ util-linux: util-linux: nsenter --join-cgroup leaks root     │
  │                  │                │          │              │                    │                 │ cgroup migration authority                                   │
  │                  │                │          │              │                    │                 │ https://avd.aquasec.com/nvd/cve-2026-78408                   │
  │                  ├────────────────┤          │              │                    ├─────────────────┼──────────────────────────────────────────────────────────────┤
  │                  │ CVE-2026-78409 │          │              │                    │                 │ util-linux: util-linux: X-mount.subdir detached-tree         │
  │                  │                │          │              │                    │                 │ resolution can escape via intermediate symlinks              │
  │                  │                │          │              │                    │                 │ https://avd.aquasec.com/nvd/cve-2026-78409                   │
  │                  ├────────────────┤          │              │                    ├─────────────────┼──────────────────────────────────────────────────────────────┤
  │                  │ CVE-2026-78410 │          │              │                    │                 │ util-linux: util-linux: restricted bind mounts do not pin    │
  │                  │                │          │              │                    │                 │ the source, allowing X-mount.owner/group/mode...             │
  │                  │                │          │              │                    │                 │ https://avd.aquasec.com/nvd/cve-2026-78410                   │
  ├──────────────────┼────────────────┤          │              ├────────────────────┼─────────────────┼──────────────────────────────────────────────────────────────┤
  │ libncursesw6     │ CVE-2025-69720 │          │              │ 6.4-4              │                 │ ncurses: ncurses: Buffer overflow vulnerability may lead to  │
  │                  │                │          │              │                    │                 │ arbitrary code execution.                                    │
  │                  │                │          │              │                    │                 │ https://avd.aquasec.com/nvd/cve-2025-69720                   │
  ├──────────────────┼────────────────┤          ├──────────────┼────────────────────┼─────────────────┼──────────────────────────────────────────────────────────────┤
  │ libpcre2-8-0     │ CVE-2026-86145 │          │ fixed        │ 10.42-1            │ 10.42-1+deb12u1 │ pcre2: PCRE2: Out-of-bounds write allows arbitrary code      │
  │                  │                │          │              │                    │                 │ execution via crafted regular expressions...                 │
  │                  │                │          │              │                    │                 │ https://avd.aquasec.com/nvd/cve-2026-86145                   │
  │                  ├────────────────┤          │              │                    │                 ├──────────────────────────────────────────────────────────────┤
  │                  │ CVE-2026-89161 │          │              │                    │                 │ pcre2: PCRE2: Memory corruption vulnerability in             │
  │                  │                │          │              │                    │                 │ pcre2_jit_match                                              │
  │                  │                │          │              │                    │                 │ https://avd.aquasec.com/nvd/cve-2026-89161                   │
  ├──────────────────┼────────────────┤          ├──────────────┼────────────────────┼─────────────────┼──────────────────────────────────────────────────────────────┤
  │ libsmartcols1    │ CVE-2026-53613 │          │ affected     │ 2.38.1-5+deb12u3   │                 │ util-linux: util-linux: TOCTOU in the mount program via      │
  │                  │                │          │              │                    │                 │ ancestor directory swap on...                                │
  │                  │                │          │              │                    │                 │ https://avd.aquasec.com/nvd/cve-2026-53613                   │
  │                  ├────────────────┤          │              │                    ├─────────────────┼──────────────────────────────────────────────────────────────┤
  │                  │ CVE-2026-76642 │          │              │                    │                 │ util-linux: util-linux: failed external mount helper still   │
  │                  │                │          │              │                    │                 │ runs privileged X-mount post-hooks                           │
  │                  │                │          │              │                    │                 │ https://avd.aquasec.com/nvd/cve-2026-76642                   │
  │                  ├────────────────┤          │              │                    ├─────────────────┼──────────────────────────────────────────────────────────────┤
  │                  │ CVE-2026-78408 │          │              │                    │                 │ util-linux: util-linux: nsenter --join-cgroup leaks root     │
  │                  │                │          │              │                    │                 │ cgroup migration authority                                   │
  │                  │                │          │              │                    │                 │ https://avd.aquasec.com/nvd/cve-2026-78408                   │
  │                  ├────────────────┤          │              │                    ├─────────────────┼──────────────────────────────────────────────────────────────┤
  │                  │ CVE-2026-78409 │          │              │                    │                 │ util-linux: util-linux: X-mount.subdir detached-tree         │
  │                  │                │          │              │                    │                 │ resolution can escape via intermediate symlinks              │
  │                  │                │          │              │                    │                 │ https://avd.aquasec.com/nvd/cve-2026-78409                   │
  │                  ├────────────────┤          │              │                    ├─────────────────┼──────────────────────────────────────────────────────────────┤
  │                  │ CVE-2026-78410 │          │              │                    │                 │ util-linux: util-linux: restricted bind mounts do not pin    │
  │                  │                │          │              │                    │                 │ the source, allowing X-mount.owner/group/mode...             │
  │                  │                │          │              │                    │                 │ https://avd.aquasec.com/nvd/cve-2026-78410                   │
  ├──────────────────┼────────────────┼──────────┤              ├────────────────────┼─────────────────┼──────────────────────────────────────────────────────────────┤
  │ libsqlite3-0     │ CVE-2025-7458  │ CRITICAL │              │ 3.40.1-2+deb12u2   │                 │ sqlite: SQLite integer overflow                              │
  │                  │                │          │              │                    │                 │ https://avd.aquasec.com/nvd/cve-2025-7458                    │
  │                  ├────────────────┼──────────┼──────────────┤                    ├─────────────────┼──────────────────────────────────────────────────────────────┤
  │                  │ CVE-2026-11822 │ HIGH     │ fix_deferred │                    │                 │ sqlite: SQLite: Arbitrary code execution via crafted FTS5    │
  │                  │                │          │              │                    │                 │ full-text search data                                        │
  │                  │                │          │              │                    │                 │ https://avd.aquasec.com/nvd/cve-2026-11822                   │
  │                  ├────────────────┤          │              │                    ├─────────────────┼──────────────────────────────────────────────────────────────┤
  │                  │ CVE-2026-11824 │          │              │                    │                 │ sqlite: SQLite: Arbitrary code execution and crash via       │
  │                  │                │          │              │                    │                 │ heap-based buffer overflow in...                             │
  │                  │                │          │              │                    │                 │ https://avd.aquasec.com/nvd/cve-2026-11824                   │
  ├──────────────────┼────────────────┤          │              ├────────────────────┼─────────────────┼──────────────────────────────────────────────────────────────┤
  │ libsystemd0      │ CVE-2026-16742 │          │              │ 252.39-1~deb12u2   │                 │ systemd: systemd-homed: Local privilege escalation via       │
  │                  │                │          │              │                    │                 │ missing home-record signature verification                   │
  │                  │                │          │              │                    │                 │ https://avd.aquasec.com/nvd/cve-2026-16742                   │
  ├──────────────────┼────────────────┤          ├──────────────┼────────────────────┼─────────────────┼──────────────────────────────────────────────────────────────┤
  │ libtinfo6        │ CVE-2025-69720 │          │ affected     │ 6.4-4              │                 │ ncurses: ncurses: Buffer overflow vulnerability may lead to  │
  │                  │                │          │              │                    │                 │ arbitrary code execution.                                    │
  │                  │                │          │              │                    │                 │ https://avd.aquasec.com/nvd/cve-2025-69720                   │
  ├──────────────────┼────────────────┤          ├──────────────┼────────────────────┼─────────────────┼──────────────────────────────────────────────────────────────┤
  │ libudev1         │ CVE-2026-16742 │          │ fix_deferred │ 252.39-1~deb12u2   │                 │ systemd: systemd-homed: Local privilege escalation via       │
  │                  │                │          │              │                    │                 │ missing home-record signature verification                   │
  │                  │                │          │              │                    │                 │ https://avd.aquasec.com/nvd/cve-2026-16742                   │
  ├──────────────────┼────────────────┤          ├──────────────┼────────────────────┼─────────────────┼──────────────────────────────────────────────────────────────┤
  │ libuuid1         │ CVE-2026-53613 │          │ affected     │ 2.38.1-5+deb12u3   │                 │ util-linux: util-linux: TOCTOU in the mount program via      │
  │                  │                │          │              │                    │                 │ ancestor directory swap on...                                │
  │                  │                │          │              │                    │                 │ https://avd.aquasec.com/nvd/cve-2026-53613                   │
  │                  ├────────────────┤          │              │                    ├─────────────────┼──────────────────────────────────────────────────────────────┤
  │                  │ CVE-2026-76642 │          │              │                    │                 │ util-linux: util-linux: failed external mount helper still   │
  │                  │                │          │              │                    │                 │ runs privileged X-mount post-hooks                           │
  │                  │                │          │              │                    │                 │ https://avd.aquasec.com/nvd/cve-2026-76642                   │
  │                  ├────────────────┤          │              │                    ├─────────────────┼──────────────────────────────────────────────────────────────┤
  │                  │ CVE-2026-78408 │          │              │                    │                 │ util-linux: util-linux: nsenter --join-cgroup leaks root     │
  │                  │                │          │              │                    │                 │ cgroup migration authority                                   │
  │                  │                │          │              │                    │                 │ https://avd.aquasec.com/nvd/cve-2026-78408                   │
  │                  ├────────────────┤          │              │                    ├─────────────────┼──────────────────────────────────────────────────────────────┤
  │                  │ CVE-2026-78409 │          │              │                    │                 │ util-linux: util-linux: X-mount.subdir detached-tree         │
  │                  │                │          │              │                    │                 │ resolution can escape via intermediate symlinks              │
  │                  │                │          │              │                    │                 │ https://avd.aquasec.com/nvd/cve-2026-78409                   │
  │                  ├────────────────┤          │              │                    ├─────────────────┼──────────────────────────────────────────────────────────────┤
  │                  │ CVE-2026-78410 │          │              │                    │                 │ util-linux: util-linux: restricted bind mounts do not pin    │
  │                  │                │          │              │                    │                 │ the source, allowing X-mount.owner/group/mode...             │
  │                  │                │          │              │                    │                 │ https://avd.aquasec.com/nvd/cve-2026-78410                   │
  ├──────────────────┼────────────────┤          │              │                    ├─────────────────┼──────────────────────────────────────────────────────────────┤
  │ mount            │ CVE-2026-53613 │          │              │                    │                 │ util-linux: util-linux: TOCTOU in the mount program via      │
  │                  │                │          │              │                    │                 │ ancestor directory swap on...                                │
  │                  │                │          │              │                    │                 │ https://avd.aquasec.com/nvd/cve-2026-53613                   │
  │                  ├────────────────┤          │              │                    ├─────────────────┼──────────────────────────────────────────────────────────────┤
  │                  │ CVE-2026-76642 │          │              │                    │                 │ util-linux: util-linux: failed external mount helper still   │
  │                  │                │          │              │                    │                 │ runs privileged X-mount post-hooks                           │
  │                  │                │          │              │                    │                 │ https://avd.aquasec.com/nvd/cve-2026-76642                   │
  │                  ├────────────────┤          │              │                    ├─────────────────┼──────────────────────────────────────────────────────────────┤
  │                  │ CVE-2026-78408 │          │              │                    │                 │ util-linux: util-linux: nsenter --join-cgroup leaks root     │
  │                  │                │          │              │                    │                 │ cgroup migration authority                                   │
  │                  │                │          │              │                    │                 │ https://avd.aquasec.com/nvd/cve-2026-78408                   │
  │                  ├────────────────┤          │              │                    ├─────────────────┼──────────────────────────────────────────────────────────────┤
  │                  │ CVE-2026-78409 │          │              │                    │                 │ util-linux: util-linux: X-mount.subdir detached-tree         │
  │                  │                │          │              │                    │                 │ resolution can escape via intermediate symlinks              │
  │                  │                │          │              │                    │                 │ https://avd.aquasec.com/nvd/cve-2026-78409                   │
  │                  ├────────────────┤          │              │                    ├─────────────────┼──────────────────────────────────────────────────────────────┤
  │                  │ CVE-2026-78410 │          │              │                    │                 │ util-linux: util-linux: restricted bind mounts do not pin    │
  │                  │                │          │              │                    │                 │ the source, allowing X-mount.owner/group/mode...             │
  │                  │                │          │              │                    │                 │ https://avd.aquasec.com/nvd/cve-2026-78410                   │
  ├──────────────────┼────────────────┤          │              ├────────────────────┼─────────────────┼──────────────────────────────────────────────────────────────┤
  │ ncurses-base     │ CVE-2025-69720 │          │              │ 6.4-4              │                 │ ncurses: ncurses: Buffer overflow vulnerability may lead to  │
  │                  │                │          │              │                    │                 │ arbitrary code execution.                                    │
  │                  │                │          │              │                    │                 │ https://avd.aquasec.com/nvd/cve-2025-69720                   │
  ├──────────────────┤                │          │              │                    ├─────────────────┤                                                              │
  │ ncurses-bin      │                │          │              │                    │                 │                                                              │
  │                  │                │          │              │                    │                 │                                                              │
  │                  │                │          │              │                    │                 │                                                              │
  ├──────────────────┼────────────────┼──────────┤              ├────────────────────┼─────────────────┼──────────────────────────────────────────────────────────────┤
  │ perl-base        │ CVE-2026-13221 │ CRITICAL │              │ 5.36.0-7+deb12u3   │                 │ perl: Perl: Incorrect regular expression processing via      │
  │                  │                │          │              │                    │                 │ large regular expressions                                    │
  │                  │                │          │              │                    │                 │ https://avd.aquasec.com/nvd/cve-2026-13221                   │
  │                  ├────────────────┤          ├──────────────┤                    ├─────────────────┼──────────────────────────────────────────────────────────────┤
  │                  │ CVE-2026-42496 │          │ fix_deferred │                    │                 │ perl-archive-tar: perl-archive-tar: Path traversal via       │
  │                  │                │          │              │                    │                 │ crafted symlinks allows arbitrary file access                │
  │                  │                │          │              │                    │                 │ https://avd.aquasec.com/nvd/cve-2026-42496                   │
  │                  ├────────────────┤          ├──────────────┤                    ├─────────────────┼──────────────────────────────────────────────────────────────┤
  │                  │ CVE-2026-8376  │          │ affected     │                    │                 │ perl: Perl: Heap buffer overflow when compiling regular      │
  │                  │                │          │              │                    │                 │ expressions on 32-bit builds...                              │
  │                  │                │          │              │                    │                 │ https://avd.aquasec.com/nvd/cve-2026-8376                    │
  │                  ├────────────────┼──────────┼──────────────┤                    ├─────────────────┼──────────────────────────────────────────────────────────────┤
  │                  │ CVE-2026-42497 │ HIGH     │ fix_deferred │                    │                 │ perl-Archive-Tar: perl-Archive-Tar: Arbitrary file           │
  │                  │                │          │              │                    │                 │ modification via crafted hardlinks during archive extraction │
  │                  │                │          │              │                    │                 │ https://avd.aquasec.com/nvd/cve-2026-42497                   │
  │                  ├────────────────┤          ├──────────────┤                    ├─────────────────┼──────────────────────────────────────────────────────────────┤
  │                  │ CVE-2026-48962 │          │ affected     │                    │                 │ perl-IO-Compress: perl-IO-Compress: Arbitrary code execution │
  │                  │                │          │              │                    │                 │ via attacker-controlled output glob                          │
  │                  │                │          │              │                    │                 │ https://avd.aquasec.com/nvd/cve-2026-48962                   │
  │                  ├────────────────┤          │              │                    ├─────────────────┼──────────────────────────────────────────────────────────────┤
  │                  │ CVE-2026-57432 │          │              │                    │                 │ perl: Perl: Information disclosure via integer overflow in   │
  │                  │                │          │              │                    │                 │ pack/unpack operations                                       │
  │                  │                │          │              │                    │                 │ https://avd.aquasec.com/nvd/cve-2026-57432                   │
  │                  ├────────────────┤          │              │                    ├─────────────────┼──────────────────────────────────────────────────────────────┤
  │                  │ CVE-2026-57433 │          │              │                    │                 │ Storable: Storable: Denial of Service via signed integer     │
  │                  │                │          │              │                    │                 │ overflow in deserialization                                  │
  │                  │                │          │              │                    │                 │ https://avd.aquasec.com/nvd/cve-2026-57433                   │
  │                  ├────────────────┤          ├──────────────┤                    ├─────────────────┼──────────────────────────────────────────────────────────────┤
  │                  │ CVE-2026-9538  │          │ fix_deferred │                    │                 │ perl-Archive-Tar: perl-Archive-Tar: Denial of Service via    │
  │                  │                │          │              │                    │                 │ crafted tar header with large entry...                       │
  │                  │                │          │              │                    │                 │ https://avd.aquasec.com/nvd/cve-2026-9538                    │
  ├──────────────────┼────────────────┤          ├──────────────┼────────────────────┼─────────────────┼──────────────────────────────────────────────────────────────┤
  │ util-linux       │ CVE-2026-53613 │          │ affected     │ 2.38.1-5+deb12u3   │                 │ util-linux: util-linux: TOCTOU in the mount program via      │
  │                  │                │          │              │                    │                 │ ancestor directory swap on...                                │
  │                  │                │          │              │                    │                 │ https://avd.aquasec.com/nvd/cve-2026-53613                   │
  │                  ├────────────────┤          │              │                    ├─────────────────┼──────────────────────────────────────────────────────────────┤
  │                  │ CVE-2026-76642 │          │              │                    │                 │ util-linux: util-linux: failed external mount helper still   │
  │                  │                │          │              │                    │                 │ runs privileged X-mount post-hooks                           │
  │                  │                │          │              │                    │                 │ https://avd.aquasec.com/nvd/cve-2026-76642                   │
  │                  ├────────────────┤          │              │                    ├─────────────────┼──────────────────────────────────────────────────────────────┤
  │                  │ CVE-2026-78408 │          │              │                    │                 │ util-linux: util-linux: nsenter --join-cgroup leaks root     │
  │                  │                │          │              │                    │                 │ cgroup migration authority                                   │
  │                  │                │          │              │                    │                 │ https://avd.aquasec.com/nvd/cve-2026-78408                   │
  │                  ├────────────────┤          │              │                    ├─────────────────┼──────────────────────────────────────────────────────────────┤
  │                  │ CVE-2026-78409 │          │              │                    │                 │ util-linux: util-linux: X-mount.subdir detached-tree         │
  │                  │                │          │              │                    │                 │ resolution can escape via intermediate symlinks              │
  │                  │                │          │              │                    │                 │ https://avd.aquasec.com/nvd/cve-2026-78409                   │
  │                  ├────────────────┤          │              │                    ├─────────────────┼──────────────────────────────────────────────────────────────┤
  │                  │ CVE-2026-78410 │          │              │                    │                 │ util-linux: util-linux: restricted bind mounts do not pin    │
  │                  │                │          │              │                    │                 │ the source, allowing X-mount.owner/group/mode...             │
  │                  │                │          │              │                    │                 │ https://avd.aquasec.com/nvd/cve-2026-78410                   │
  ├──────────────────┼────────────────┤          │              │                    ├─────────────────┼──────────────────────────────────────────────────────────────┤
  │ util-linux-extra │ CVE-2026-53613 │          │              │                    │                 │ util-linux: util-linux: TOCTOU in the mount program via      │
  │                  │                │          │              │                    │                 │ ancestor directory swap on...                                │
  │                  │                │          │              │                    │                 │ https://avd.aquasec.com/nvd/cve-2026-53613                   │
  │                  ├────────────────┤          │              │                    ├─────────────────┼──────────────────────────────────────────────────────────────┤
  │                  │ CVE-2026-76642 │          │              │                    │                 │ util-linux: util-linux: failed external mount helper still   │
  │                  │                │          │              │                    │                 │ runs privileged X-mount post-hooks                           │
  │                  │                │          │              │                    │                 │ https://avd.aquasec.com/nvd/cve-2026-76642                   │
  │                  ├────────────────┤          │              │                    ├─────────────────┼──────────────────────────────────────────────────────────────┤
  │                  │ CVE-2026-78408 │          │              │                    │                 │ util-linux: util-linux: nsenter --join-cgroup leaks root     │
  │                  │                │          │              │                    │                 │ cgroup migration authority                                   │
  │                  │                │          │              │                    │                 │ https://avd.aquasec.com/nvd/cve-2026-78408                   │
  │                  ├────────────────┤          │              │                    ├─────────────────┼──────────────────────────────────────────────────────────────┤
  │                  │ CVE-2026-78409 │          │              │                    │                 │ util-linux: util-linux: X-mount.subdir detached-tree         │
  │                  │                │          │              │                    │                 │ resolution can escape via intermediate symlinks              │
  │                  │                │          │              │                    │                 │ https://avd.aquasec.com/nvd/cve-2026-78409                   │
  │                  ├────────────────┤          │              │                    ├─────────────────┼──────────────────────────────────────────────────────────────┤
  │                  │ CVE-2026-78410 │          │              │                    │                 │ util-linux: util-linux: restricted bind mounts do not pin    │
  │                  │                │          │              │                    │                 │ the source, allowing X-mount.owner/group/mode...             │
  │                  │                │          │              │                    │                 │ https://avd.aquasec.com/nvd/cve-2026-78410                   │
  ├──────────────────┼────────────────┼──────────┼──────────────┼────────────────────┼─────────────────┼──────────────────────────────────────────────────────────────┤
  │ zlib1g           │ CVE-2023-45853 │ CRITICAL │ will_not_fix │ 1:1.2.13.dfsg-1    │                 │ zlib: integer overflow and resultant heap-based buffer       │
  │                  │                │          │              │                    │                 │ overflow in zipOpenNewFileInZip4_6                           │
  │                  │                │          │              │                    │                 │ https://avd.aquasec.com/nvd/cve-2023-45853                   │
  └──────────────────┴────────────────┴──────────┴──────────────┴────────────────────┴─────────────────┴──────────────────────────────────────────────────────────────┘

```
# For nginx image:
```
Report Summary
  
  ┌───────────────────────────────────┬────────┬─────────────────┬─────────┐
  │              Target               │  Type  │ Vulnerabilities │ Secrets │
  ├───────────────────────────────────┼────────┼─────────────────┼─────────┤
  │ nginx:1.28-alpine (alpine 3.23.3) │ alpine │       54        │    -    │
  └───────────────────────────────────┴────────┴─────────────────┴─────────┘
  Legend:
  - '-': Not scanned
  - '0': Clean (no security findings detected)
  
  
  For OSS Maintainers: VEX Notice
  --------------------------------
  If you're an OSS maintainer and Trivy has detected vulnerabilities in your project that you believe are not actually exploitable, consider issuing a VEX (Vulnerability Exploitability eXchange) statement.
  VEX allows you to communicate the actual status of vulnerabilities in your project, improving security transparency and reducing false positives for your users.
  Learn more and start using VEX: https://trivy.dev/docs/v0.74/guide/supply-chain/vex/repo#publishing-vex-documents
  
  To disable this notice, set the TRIVY_DISABLE_VEX_NOTICE environment variable.
  
  
  nginx:1.28-alpine (alpine 3.23.3)
  =================================
  Total: 54 (HIGH: 52, CRITICAL: 2)
  
  ┌──────────────┬────────────────┬──────────┬────────┬───────────────────┬───────────────┬──────────────────────────────────────────────────────────────┐
  │   Library    │ Vulnerability  │ Severity │ Status │ Installed Version │ Fixed Version │                            Title                             │
  ├──────────────┼────────────────┼──────────┼────────┼───────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
  │ c-ares       │ CVE-2026-33630 │ HIGH     │ fixed  │ 1.34.6-r0         │ 1.34.8-r0     │ c-ares: c-ares: Use-after-free / double-free in              │
  │              │                │          │        │                   │               │ query-completion handling                                    │
  │              │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-33630                   │
  ├──────────────┼────────────────┤          │        ├───────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
  │ curl         │ CVE-2026-11352 │          │        │ 8.17.0-r1         │ 8.22.0-r0     │ curl: libcurl: curl/libcurl: Remote denial of service via    │
  │              │                │          │        │                   │               │ QUIC UDP receive function...                                 │
  │              │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-11352                   │
  │              ├────────────────┤          │        │                   │               ├──────────────────────────────────────────────────────────────┤
  │              │ CVE-2026-11586 │          │        │                   │               │ curl: curl: Denial of Service via WebSocket PING flood       │
  │              │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-11586                   │
  │              ├────────────────┤          │        │                   │               ├──────────────────────────────────────────────────────────────┤
  │              │ CVE-2026-12064 │          │        │                   │               │ curl: curl: SSH host verification bypass when using          │
  │              │                │          │        │                   │               │ schemeless URLs with SFTP/SCP...                             │
  │              │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-12064                   │
  │              ├────────────────┤          │        │                   ├───────────────┼──────────────────────────────────────────────────────────────┤
  │              │ CVE-2026-5773  │          │        │                   │ 8.20.0-r0     │ curl: libcurl: Wrong file transfer due to incorrect SMB      │
  │              │                │          │        │                   │               │ connection reuse                                             │
  │              │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-5773                    │
  │              ├────────────────┤          │        │                   │               ├──────────────────────────────────────────────────────────────┤
  │              │ CVE-2026-6276  │          │        │                   │               │ curl: libcurl: Information disclosure due to cookie leak     │
  │              │                │          │        │                   │               │ when reusing connections with...                             │
  │              │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-6276                    │
  │              ├────────────────┤          │        │                   ├───────────────┼──────────────────────────────────────────────────────────────┤
  │              │ CVE-2026-8286  │          │        │                   │ 8.22.0-r0     │ curl: curl: Insecure connection establishment due to TLS     │
  │              │                │          │        │                   │               │ configuration mismatch                                       │
  │              │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-8286                    │
  │              ├────────────────┤          │        │                   │               ├──────────────────────────────────────────────────────────────┤
  │              │ CVE-2026-8458  │          │        │                   │               │ curl: libcurl: Unauthorized connection reuse due to a        │
  │              │                │          │        │                   │               │ logical error                                                │
  │              │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-8458                    │
  │              ├────────────────┤          │        │                   │               ├──────────────────────────────────────────────────────────────┤
  │              │ CVE-2026-8925  │          │        │                   │               │ curl: curl: Double-free vulnerability in SASL authentication │
  │              │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-8925                    │
  │              ├────────────────┤          │        │                   │               ├──────────────────────────────────────────────────────────────┤
  │              │ CVE-2026-8927  │          │        │                   │               │ curl: Information disclosure due to uncleared proxy          │
  │              │                │          │        │                   │               │ authentication state                                         │
  │              │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-8927                    │
  │              ├────────────────┤          │        │                   │               ├──────────────────────────────────────────────────────────────┤
  │              │ CVE-2026-9547  │          │        │                   │               │ curl: curl: Man-in-the-middle attack via SSH host key bypass │
  │              │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-9547                    │
  ├──────────────┼────────────────┼──────────┤        ├───────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
  │ libcrypto3   │ CVE-2026-31789 │ CRITICAL │        │ 3.5.5-r0          │ 3.5.6-r0      │ openssl: OpenSSL: Heap buffer overflow on 32-bit systems     │
  │              │                │          │        │                   │               │ from large X.509 certificate...                              │
  │              │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-31789                   │
  │              ├────────────────┼──────────┤        │                   ├───────────────┼──────────────────────────────────────────────────────────────┤
  │              │ CVE-2026-14456 │ HIGH     │        │                   │ 3.5.8-r0      │ openssl: OpenSSL: Denial of Service via unbounded memory     │
  │              │                │          │        │                   │               │ growth in QUIC server...                                     │
  │              │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-14456                   │
  │              ├────────────────┤          │        │                   ├───────────────┼──────────────────────────────────────────────────────────────┤
  │              │ CVE-2026-28387 │          │        │                   │ 3.5.6-r0      │ openssl: OpenSSL: Arbitrary code execution due to            │
  │              │                │          │        │                   │               │ use-after-free in DANE TLSA authentication...                │
  │              │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-28387                   │
  │              ├────────────────┤          │        │                   │               ├──────────────────────────────────────────────────────────────┤
  │              │ CVE-2026-28388 │          │        │                   │               │ openssl: OpenSSL: Denial of Service due to NULL pointer      │
  │              │                │          │        │                   │               │ dereference in delta...                                      │
  │              │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-28388                   │
  │              ├────────────────┤          │        │                   │               ├──────────────────────────────────────────────────────────────┤
  │              │ CVE-2026-28389 │          │        │                   │               │ openssl: OpenSSL: Denial of Service vulnerability in CMS     │
  │              │                │          │        │                   │               │ processing                                                   │
  │              │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-28389                   │
  │              ├────────────────┤          │        │                   │               ├──────────────────────────────────────────────────────────────┤
  │              │ CVE-2026-28390 │          │        │                   │               │ openssl: OpenSSL: Denial of Service due to NULL pointer      │
  │              │                │          │        │                   │               │ dereference in CMS...                                        │
  │              │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-28390                   │
  │              ├────────────────┤          │        │                   ├───────────────┼──────────────────────────────────────────────────────────────┤
  │              │ CVE-2026-45447 │          │        │                   │ 3.5.7-r0      │ openssl: Heap Use-After-Free in OpenSSL PKCS7_verify()       │
  │              │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-45447                   │
  ├──────────────┼────────────────┤          │        ├───────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
  │ libcurl      │ CVE-2026-11352 │          │        │ 8.17.0-r1         │ 8.22.0-r0     │ curl: libcurl: curl/libcurl: Remote denial of service via    │
  │              │                │          │        │                   │               │ QUIC UDP receive function...                                 │
  │              │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-11352                   │
  │              ├────────────────┤          │        │                   │               ├──────────────────────────────────────────────────────────────┤
  │              │ CVE-2026-11586 │          │        │                   │               │ curl: curl: Denial of Service via WebSocket PING flood       │
  │              │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-11586                   │
  │              ├────────────────┤          │        │                   │               ├──────────────────────────────────────────────────────────────┤
  │              │ CVE-2026-12064 │          │        │                   │               │ curl: curl: SSH host verification bypass when using          │
  │              │                │          │        │                   │               │ schemeless URLs with SFTP/SCP...                             │
  │              │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-12064                   │
  │              ├────────────────┤          │        │                   ├───────────────┼──────────────────────────────────────────────────────────────┤
  │              │ CVE-2026-5773  │          │        │                   │ 8.20.0-r0     │ curl: libcurl: Wrong file transfer due to incorrect SMB      │
  │              │                │          │        │                   │               │ connection reuse                                             │
  │              │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-5773                    │
  │              ├────────────────┤          │        │                   │               ├──────────────────────────────────────────────────────────────┤
  │              │ CVE-2026-6276  │          │        │                   │               │ curl: libcurl: Information disclosure due to cookie leak     │
  │              │                │          │        │                   │               │ when reusing connections with...                             │
  │              │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-6276                    │
  │              ├────────────────┤          │        │                   ├───────────────┼──────────────────────────────────────────────────────────────┤
  │              │ CVE-2026-8286  │          │        │                   │ 8.22.0-r0     │ curl: curl: Insecure connection establishment due to TLS     │
  │              │                │          │        │                   │               │ configuration mismatch                                       │
  │              │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-8286                    │
  │              ├────────────────┤          │        │                   │               ├──────────────────────────────────────────────────────────────┤
  │              │ CVE-2026-8458  │          │        │                   │               │ curl: libcurl: Unauthorized connection reuse due to a        │
  │              │                │          │        │                   │               │ logical error                                                │
  │              │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-8458                    │
  │              ├────────────────┤          │        │                   │               ├──────────────────────────────────────────────────────────────┤
  │              │ CVE-2026-8925  │          │        │                   │               │ curl: curl: Double-free vulnerability in SASL authentication │
  │              │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-8925                    │
  │              ├────────────────┤          │        │                   │               ├──────────────────────────────────────────────────────────────┤
  │              │ CVE-2026-8927  │          │        │                   │               │ curl: Information disclosure due to uncleared proxy          │
  │              │                │          │        │                   │               │ authentication state                                         │
  │              │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-8927                    │
  │              ├────────────────┤          │        │                   │               ├──────────────────────────────────────────────────────────────┤
  │              │ CVE-2026-9547  │          │        │                   │               │ curl: curl: Man-in-the-middle attack via SSH host key bypass │
  │              │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-9547                    │
  ├──────────────┼────────────────┤          │        ├───────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
  │ libexpat     │ CVE-2026-45186 │          │        │ 2.7.5-r0          │ 2.8.1-r0      │ libexpat: denial of service via crafted XML input            │
  │              │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-45186                   │
  │              ├────────────────┤          │        │                   ├───────────────┼──────────────────────────────────────────────────────────────┤
  │              │ CVE-2026-76956 │          │        │                   │ 2.8.4-r0      │ libexpat: libexpat: Denial of Service via hash flooding      │
  │              │                │          │        │                   │               │ attack with crafted XML...                                   │
  │              │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-76956                   │
  │              ├────────────────┤          │        │                   │               ├──────────────────────────────────────────────────────────────┤
  │              │ CVE-2026-76957 │          │        │                   │               │ libexpat: libexpat: Memory corruption vulnerability allows   │
  │              │                │          │        │                   │               │ arbitrary code execution or denial of...                     │
  │              │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-76957                   │
  ├──────────────┼────────────────┼──────────┤        ├───────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
  │ libssl3      │ CVE-2026-31789 │ CRITICAL │        │ 3.5.5-r0          │ 3.5.6-r0      │ openssl: OpenSSL: Heap buffer overflow on 32-bit systems     │
  │              │                │          │        │                   │               │ from large X.509 certificate...                              │
  │              │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-31789                   │
  │              ├────────────────┼──────────┤        │                   ├───────────────┼──────────────────────────────────────────────────────────────┤
  │              │ CVE-2026-14456 │ HIGH     │        │                   │ 3.5.8-r0      │ openssl: OpenSSL: Denial of Service via unbounded memory     │
  │              │                │          │        │                   │               │ growth in QUIC server...                                     │
  │              │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-14456                   │
  │              ├────────────────┤          │        │                   ├───────────────┼──────────────────────────────────────────────────────────────┤
  │              │ CVE-2026-28387 │          │        │                   │ 3.5.6-r0      │ openssl: OpenSSL: Arbitrary code execution due to            │
  │              │                │          │        │                   │               │ use-after-free in DANE TLSA authentication...                │
  │              │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-28387                   │
  │              ├────────────────┤          │        │                   │               ├──────────────────────────────────────────────────────────────┤
  │              │ CVE-2026-28388 │          │        │                   │               │ openssl: OpenSSL: Denial of Service due to NULL pointer      │
  │              │                │          │        │                   │               │ dereference in delta...                                      │
  │              │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-28388                   │
  │              ├────────────────┤          │        │                   │               ├──────────────────────────────────────────────────────────────┤
  │              │ CVE-2026-28389 │          │        │                   │               │ openssl: OpenSSL: Denial of Service vulnerability in CMS     │
  │              │                │          │        │                   │               │ processing                                                   │
  │              │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-28389                   │
  │              ├────────────────┤          │        │                   │               ├──────────────────────────────────────────────────────────────┤
  │              │ CVE-2026-28390 │          │        │                   │               │ openssl: OpenSSL: Denial of Service due to NULL pointer      │
  │              │                │          │        │                   │               │ dereference in CMS...                                        │
  │              │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-28390                   │
  │              ├────────────────┤          │        │                   ├───────────────┼──────────────────────────────────────────────────────────────┤
  │              │ CVE-2026-45447 │          │        │                   │ 3.5.7-r0      │ openssl: Heap Use-After-Free in OpenSSL PKCS7_verify()       │
  │              │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-45447                   │
  ├──────────────┼────────────────┤          │        ├───────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
  │ libuuid      │ CVE-2026-53612 │          │        │ 2.41.2-r0         │ 2.41.6-r0     │ util-linux: util-linux: TOCTOU in the mount program when     │
  │              │                │          │        │                   │               │ applying post-mount ownership/mode changes...                │
  │              │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-53612                   │
  │              ├────────────────┤          │        │                   │               ├──────────────────────────────────────────────────────────────┤
  │              │ CVE-2026-53613 │          │        │                   │               │ util-linux: util-linux: TOCTOU in the mount program via      │
  │              │                │          │        │                   │               │ ancestor directory swap on...                                │
  │              │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-53613                   │
  │              ├────────────────┤          │        │                   │               ├──────────────────────────────────────────────────────────────┤
  │              │ CVE-2026-53614 │          │        │                   │               │ util-linux: util-linux: SUID mount(8) allows nosuid/noexec   │
  │              │                │          │        │                   │               │ bypass via LIBMOUNT_FORCE_MOUNT2                             │
  │              │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-53614                   │
  │              ├────────────────┤          │        │                   │               ├──────────────────────────────────────────────────────────────┤
  │              │ CVE-2026-76642 │          │        │                   │               │ util-linux: util-linux: failed external mount helper still   │
  │              │                │          │        │                   │               │ runs privileged X-mount post-hooks                           │
  │              │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-76642                   │
  │              ├────────────────┤          │        │                   ├───────────────┼──────────────────────────────────────────────────────────────┤
  │              │ CVE-2026-78408 │          │        │                   │ 2.41.6-r1     │ util-linux: util-linux: nsenter --join-cgroup leaks root     │
  │              │                │          │        │                   │               │ cgroup migration authority                                   │
  │              │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-78408                   │
  │              ├────────────────┤          │        │                   ├───────────────┼──────────────────────────────────────────────────────────────┤
  │              │ CVE-2026-78410 │          │        │                   │ 2.41.6-r0     │ util-linux: util-linux: restricted bind mounts do not pin    │
  │              │                │          │        │                   │               │ the source, allowing X-mount.owner/group/mode...             │
  │              │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-78410                   │
  ├──────────────┼────────────────┤          │        ├───────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
  │ libxml2      │ CVE-2026-6732  │          │        │ 2.13.9-r0         │ 2.13.9-r1     │ libxml2: libxml2: Denial of Service via crafted              │
  │              │                │          │        │                   │               │ XSD-validated document                                       │
  │              │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-6732                    │
  ├──────────────┼────────────────┤          │        ├───────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
  │ musl         │ CVE-2026-40200 │          │        │ 1.2.5-r21         │ 1.2.5-r23     │ musl: musl libc: Arbitrary code execution and denial of      │
  │              │                │          │        │                   │               │ service via stack-based...                                   │
  │              │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-40200                   │
  ├──────────────┤                │          │        │                   │               │                                                              │
  │ musl-utils   │                │          │        │                   │               │                                                              │
  │              │                │          │        │                   │               │                                                              │
  │              │                │          │        │                   │               │                                                              │
  ├──────────────┼────────────────┤          │        ├───────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
  │ nghttp2-libs │ CVE-2026-27135 │          │        │ 1.68.0-r0         │ 1.68.1        │ nghttp2: nghttp2: Denial of Service via malformed HTTP/2     │
  │              │                │          │        │                   │               │ frames after session termination...                          │
  │              │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-27135                   │
  ├──────────────┼────────────────┤          │        ├───────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
  │ nginx        │ CVE-2026-42055 │          │        │ 1.28.3-r1         │ 1.28.3-r4     │ nginx: NGINX: Arbitrary code execution or Denial of Service  │
  │              │                │          │        │                   │               │ via heap-based buffer...                                     │
  │              │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-42055                   │
  │              ├────────────────┤          │        │                   ├───────────────┼──────────────────────────────────────────────────────────────┤
  │              │ CVE-2026-42533 │          │        │                   │ 1.28.3-r6     │ nginx: NGINX: Arbitrary code execution via crafted HTTP      │
  │              │                │          │        │                   │               │ requests                                                     │
  │              │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-42533                   │
  │              ├────────────────┤          │        │                   ├───────────────┼──────────────────────────────────────────────────────────────┤
  │              │ CVE-2026-49975 │          │        │                   │ 1.28.3-r3     │ httpd: httpd: HTTP/2 Remote Denial of Service via            │
  │              │                │          │        │                   │               │ compression bomb and Slowloris-style...                      │
  │              │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-49975                   │
  │              ├────────────────┤          │        │                   ├───────────────┼──────────────────────────────────────────────────────────────┤
  │              │ CVE-2026-60005 │          │        │                   │ 1.28.3-r6     │ nginx: NGINX: Memory disclosure and denial of service in     │
  │              │                │          │        │                   │               │ ngx_http_slice_module                                        │
  │              │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-60005                   │
  │              ├────────────────┤          │        │                   ├───────────────┼──────────────────────────────────────────────────────────────┤
  │              │ CVE-2026-9256  │          │        │                   │ 1.28.3-r2     │ nginx: ngx_http_rewrite_module: code execution and denial of │
  │              │                │          │        │                   │               │ service                                                      │
  │              │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-9256                    │
  ├──────────────┼────────────────┤          │        ├───────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
  │ zlib         │ CVE-2026-22184 │          │        │ 1.3.1-r2          │ 1.3.2-r0      │ zlib: zlib: Arbitrary code execution via buffer overflow in  │
  │              │                │          │        │                   │               │ untgz utility                                                │
  │              │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-22184                   │
  └──────────────┴────────────────┴──────────┴────────┴───────────────────┴───────────────┴──────────────────────────────────────────────────────────────┘
```

# For postgres image:
```
Report Summary
  
  ┌────────────────────────────────────┬──────────┬─────────────────┬─────────┐
  │               Target               │   Type   │ Vulnerabilities │ Secrets │
  ├────────────────────────────────────┼──────────┼─────────────────┼─────────┤
  │ postgres:16-alpine (alpine 3.24.1) │  alpine  │        9        │    -    │
  ├────────────────────────────────────┼──────────┼─────────────────┼─────────┤
  │ usr/local/bin/gosu                 │ gobinary │       22        │    -    │
  └────────────────────────────────────┴──────────┴─────────────────┴─────────┘
  Legend:
  - '-': Not scanned
  - '0': Clean (no security findings detected)
  
  
  For OSS Maintainers: VEX Notice
  --------------------------------
  If you're an OSS maintainer and Trivy has detected vulnerabilities in your project that you believe are not actually exploitable, consider issuing a VEX (Vulnerability Exploitability eXchange) statement.
  VEX allows you to communicate the actual status of vulnerabilities in your project, improving security transparency and reducing false positives for your users.
  Learn more and start using VEX: https://trivy.dev/docs/v0.74/guide/supply-chain/vex/repo#publishing-vex-documents
  
  To disable this notice, set the TRIVY_DISABLE_VEX_NOTICE environment variable.
  
  
  postgres:16-alpine (alpine 3.24.1)
  ==================================
  Total: 9 (HIGH: 9, CRITICAL: 0)
  
  ┌────────────┬────────────────┬──────────┬────────┬───────────────────┬───────────────┬────────────────────────────────────────────────────────────┐
  │  Library   │ Vulnerability  │ Severity │ Status │ Installed Version │ Fixed Version │                           Title                            │
  ├────────────┼────────────────┼──────────┼────────┼───────────────────┼───────────────┼────────────────────────────────────────────────────────────┤
  │ libcrypto3 │ CVE-2026-14456 │ HIGH     │ fixed  │ 3.5.7-r0          │ 3.5.8-r0      │ openssl: OpenSSL: Denial of Service via unbounded memory   │
  │            │                │          │        │                   │               │ growth in QUIC server...                                   │
  │            │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-14456                 │
  ├────────────┤                │          │        │                   │               │                                                            │
  │ libssl3    │                │          │        │                   │               │                                                            │
  │            │                │          │        │                   │               │                                                            │
  │            │                │          │        │                   │               │                                                            │
  ├────────────┼────────────────┤          │        ├───────────────────┼───────────────┼────────────────────────────────────────────────────────────┤
  │ libuuid    │ CVE-2026-53612 │          │        │ 2.42.1-r0         │ 2.42.3-r0     │ util-linux: util-linux: TOCTOU in the mount program when   │
  │            │                │          │        │                   │               │ applying post-mount ownership/mode changes...              │
  │            │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-53612                 │
  │            ├────────────────┤          │        │                   │               ├────────────────────────────────────────────────────────────┤
  │            │ CVE-2026-53613 │          │        │                   │               │ util-linux: util-linux: TOCTOU in the mount program via    │
  │            │                │          │        │                   │               │ ancestor directory swap on...                              │
  │            │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-53613                 │
  │            ├────────────────┤          │        │                   │               ├────────────────────────────────────────────────────────────┤
  │            │ CVE-2026-53614 │          │        │                   │               │ util-linux: util-linux: SUID mount(8) allows nosuid/noexec │
  │            │                │          │        │                   │               │ bypass via LIBMOUNT_FORCE_MOUNT2                           │
  │            │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-53614                 │
  │            ├────────────────┤          │        │                   │               ├────────────────────────────────────────────────────────────┤
  │            │ CVE-2026-76642 │          │        │                   │               │ util-linux: util-linux: failed external mount helper still │
  │            │                │          │        │                   │               │ runs privileged X-mount post-hooks                         │
  │            │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-76642                 │
  │            ├────────────────┤          │        │                   ├───────────────┼────────────────────────────────────────────────────────────┤
  │            │ CVE-2026-78408 │          │        │                   │ 2.42.3-r1     │ util-linux: util-linux: nsenter --join-cgroup leaks root   │
  │            │                │          │        │                   │               │ cgroup migration authority                                 │
  │            │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-78408                 │
  │            ├────────────────┤          │        │                   ├───────────────┼────────────────────────────────────────────────────────────┤
  │            │ CVE-2026-78409 │          │        │                   │ 2.42.3-r0     │ util-linux: util-linux: X-mount.subdir detached-tree       │
  │            │                │          │        │                   │               │ resolution can escape via intermediate symlinks            │
  │            │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-78409                 │
  │            ├────────────────┤          │        │                   │               ├────────────────────────────────────────────────────────────┤
  │            │ CVE-2026-78410 │          │        │                   │               │ util-linux: util-linux: restricted bind mounts do not pin  │
  │            │                │          │        │                   │               │ the source, allowing X-mount.owner/group/mode...           │
  │            │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-78410                 │
  └────────────┴────────────────┴──────────┴────────┴───────────────────┴───────────────┴────────────────────────────────────────────────────────────┘
  
  usr/local/bin/gosu (gobinary)
  =============================
  Total: 22 (HIGH: 21, CRITICAL: 1)
  
  ┌─────────┬────────────────┬──────────┬────────┬───────────────────┬──────────────────────────────┬──────────────────────────────────────────────────────────────┐
  │ Library │ Vulnerability  │ Severity │ Status │ Installed Version │        Fixed Version         │                            Title                             │
  ├─────────┼────────────────┼──────────┼────────┼───────────────────┼──────────────────────────────┼──────────────────────────────────────────────────────────────┤
  │ stdlib  │ CVE-2025-68121 │ CRITICAL │ fixed  │ v1.24.6           │ 1.24.13, 1.25.7, 1.26.0-rc.3 │ crypto/tls: crypto/tls: Incorrect certificate validation     │
  │         │                │          │        │                   │                              │ during TLS session resumption                                │
  │         │                │          │        │                   │                              │ https://avd.aquasec.com/nvd/cve-2025-68121                   │
  │         ├────────────────┼──────────┤        │                   ├──────────────────────────────┼──────────────────────────────────────────────────────────────┤
  │         │ CVE-2025-61726 │ HIGH     │        │                   │ 1.24.12, 1.25.6              │ golang: net/url: Memory exhaustion in query parameter        │
  │         │                │          │        │                   │                              │ parsing in net/url                                           │
  │         │                │          │        │                   │                              │ https://avd.aquasec.com/nvd/cve-2025-61726                   │
  │         ├────────────────┤          │        │                   ├──────────────────────────────┼──────────────────────────────────────────────────────────────┤
  │         │ CVE-2025-61729 │          │        │                   │ 1.24.11, 1.25.5              │ crypto/x509: golang: Denial of Service due to excessive      │
  │         │                │          │        │                   │                              │ resource consumption via crafted...                          │
  │         │                │          │        │                   │                              │ https://avd.aquasec.com/nvd/cve-2025-61729                   │
  │         ├────────────────┤          │        │                   ├──────────────────────────────┼──────────────────────────────────────────────────────────────┤
  │         │ CVE-2026-25679 │          │        │                   │ 1.25.8, 1.26.1               │ net/url: Incorrect parsing of IPv6 host literals in net/url  │
  │         │                │          │        │                   │                              │ https://avd.aquasec.com/nvd/cve-2026-25679                   │
  │         ├────────────────┤          │        │                   ├──────────────────────────────┼──────────────────────────────────────────────────────────────┤
  │         │ CVE-2026-27145 │          │        │                   │ 1.25.11, 1.26.4              │ crypto/x509: golang: golang crypto/x509: Denial of Service   │
  │         │                │          │        │                   │                              │ via excessive processing of DNS...                           │
  │         │                │          │        │                   │                              │ https://avd.aquasec.com/nvd/cve-2026-27145                   │
  │         ├────────────────┤          │        │                   ├──────────────────────────────┼──────────────────────────────────────────────────────────────┤
  │         │ CVE-2026-32280 │          │        │                   │ 1.25.9, 1.26.2               │ crypto/x509: crypto/tls: golang: Go: Denial of Service       │
  │         │                │          │        │                   │                              │ vulnerability in certificate chain building...               │
  │         │                │          │        │                   │                              │ https://avd.aquasec.com/nvd/cve-2026-32280                   │
  │         ├────────────────┤          │        │                   │                              ├──────────────────────────────────────────────────────────────┤
  │         │ CVE-2026-32281 │          │        │                   │                              │ crypto/x509: golang: Go crypto/x509: Denial of Service via   │
  │         │                │          │        │                   │                              │ inefficient certificate chain validation...                  │
  │         │                │          │        │                   │                              │ https://avd.aquasec.com/nvd/cve-2026-32281                   │
  │         ├────────────────┤          │        │                   │                              ├──────────────────────────────────────────────────────────────┤
  │         │ CVE-2026-32283 │          │        │                   │                              │ crypto/tls: golang: Go crypto/tls: Denial of Service via     │
  │         │                │          │        │                   │                              │ multiple TLS 1.3 key...                                      │
  │         │                │          │        │                   │                              │ https://avd.aquasec.com/nvd/cve-2026-32283                   │
  │         ├────────────────┤          │        │                   ├──────────────────────────────┼──────────────────────────────────────────────────────────────┤
  │         │ CVE-2026-33811 │          │        │                   │ 1.25.10, 1.26.3              │ net: golang: Go net package: Denial of Service via long      │
  │         │                │          │        │                   │                              │ CNAME response...                                            │
  │         │                │          │        │                   │                              │ https://avd.aquasec.com/nvd/cve-2026-33811                   │
  │         ├────────────────┤          │        │                   │                              ├──────────────────────────────────────────────────────────────┤
  │         │ CVE-2026-33814 │          │        │                   │                              │ net/http/internal/http2: golang: golang.org/x/net: Go        │
  │         │                │          │        │                   │                              │ HTTP/2: Denial of Service via malformed                      │
  │         │                │          │        │                   │                              │ SETTINGS_MAX_FRAME_SIZE frame...                             │
  │         │                │          │        │                   │                              │ https://avd.aquasec.com/nvd/cve-2026-33814                   │
  │         ├────────────────┤          │        │                   ├──────────────────────────────┼──────────────────────────────────────────────────────────────┤
  │         │ CVE-2026-33818 │          │        │                   │ 1.25.13, 1.26.6, 1.27.0-rc.3 │ encoding/asn1: golang: Go encoding/asn1: Denial of Service   │
  │         │                │          │        │                   │                              │ via excessive recursion in Unmarshal...                      │
  │         │                │          │        │                   │                              │ https://avd.aquasec.com/nvd/cve-2026-33818                   │
  │         ├────────────────┤          │        │                   ├──────────────────────────────┼──────────────────────────────────────────────────────────────┤
  │         │ CVE-2026-39820 │          │        │                   │ 1.25.10, 1.26.3              │ net/mail: golang: Go net/mail: Denial of Service via crafted │
  │         │                │          │        │                   │                              │ email inputs                                                 │
  │         │                │          │        │                   │                              │ https://avd.aquasec.com/nvd/cve-2026-39820                   │
  │         ├────────────────┤          │        │                   ├──────────────────────────────┼──────────────────────────────────────────────────────────────┤
  │         │ CVE-2026-39821 │          │        │                   │ 1.25.13, 1.26.6, 1.27.0-rc.3 │ golang.org/x/net/idna: golang: net/http:                     │
  │         │                │          │        │                   │                              │ golang.org/x/net/idna: Privilege escalation via incorrect    │
  │         │                │          │        │                   │                              │ Punycode label processing                                    │
  │         │                │          │        │                   │                              │ https://avd.aquasec.com/nvd/cve-2026-39821                   │
  │         ├────────────────┤          │        │                   ├──────────────────────────────┼──────────────────────────────────────────────────────────────┤
  │         │ CVE-2026-39822 │          │        │                   │ 1.25.12, 1.26.5, 1.27.0-rc.2 │ golang: Go os.Root: Symlink following vulnerability allows   │
  │         │                │          │        │                   │                              │ directory traversal                                          │
  │         │                │          │        │                   │                              │ https://avd.aquasec.com/nvd/cve-2026-39822                   │
  │         ├────────────────┤          │        │                   ├──────────────────────────────┼──────────────────────────────────────────────────────────────┤
  │         │ CVE-2026-39836 │          │        │                   │ 1.25.10, 1.26.3              │ net: golang: Go net package: Denial of Service via NUL byte  │
  │         │                │          │        │                   │                              │ in...                                                        │
  │         │                │          │        │                   │                              │ https://avd.aquasec.com/nvd/cve-2026-39836                   │
  │         ├────────────────┤          │        │                   │                              ├──────────────────────────────────────────────────────────────┤
  │         │ CVE-2026-42499 │          │        │                   │                              │ net/mail: golang: net/mail: Denial of Service via            │
  │         │                │          │        │                   │                              │ pathological email address parsing                           │
  │         │                │          │        │                   │                              │ https://avd.aquasec.com/nvd/cve-2026-42499                   │
  │         ├────────────────┤          │        │                   ├──────────────────────────────┼──────────────────────────────────────────────────────────────┤
  │         │ CVE-2026-42504 │          │        │                   │ 1.25.11, 1.26.4              │ mime: golang: Golang MIME: Denial of Service via             │
  │         │                │          │        │                   │                              │ maliciously-crafted MIME header                              │
  │         │                │          │        │                   │                              │ https://avd.aquasec.com/nvd/cve-2026-42504                   │
  │         ├────────────────┤          │        │                   ├──────────────────────────────┼──────────────────────────────────────────────────────────────┤
  │         │ CVE-2026-56853 │          │        │                   │ 1.25.13, 1.26.6, 1.27.0-rc.3 │ net/http: golang: Go net/http: Unencrypted HTTP/2            │
  │         │                │          │        │                   │                              │ connections vulnerable to Denial of Service...               │
  │         │                │          │        │                   │                              │ https://avd.aquasec.com/nvd/cve-2026-56853                   │
  │         ├────────────────┤          │        │                   │                              ├──────────────────────────────────────────────────────────────┤
  │         │ CVE-2026-56858 │          │        │                   │                              │ html/template: golang: Go html/template: Cross-Site          │
  │         │                │          │        │                   │                              │ Scripting via pathological input                             │
  │         │                │          │        │                   │                              │ https://avd.aquasec.com/nvd/cve-2026-56858                   │
  │         ├────────────────┤          │        │                   │                              ├──────────────────────────────────────────────────────────────┤
  │         │ CVE-2026-56859 │          │        │                   │                              │ encoding/xml: golang: Go: Denial of Service via XML decoding │
  │         │                │          │        │                   │                              │ recursion depth issue...                                     │
  │         │                │          │        │                   │                              │ https://avd.aquasec.com/nvd/cve-2026-56859                   │
  │         ├────────────────┤          │        │                   │                              ├──────────────────────────────────────────────────────────────┤
  │         │ CVE-2026-56860 │          │        │                   │                              │ net/url: golang: golang net/url: Denial of Service from      │
  │         │                │          │        │                   │                              │ quadratic complexity in path...                              │
  │         │                │          │        │                   │                              │ https://avd.aquasec.com/nvd/cve-2026-56860                   │
  │         ├────────────────┤          │        │                   │                              ├──────────────────────────────────────────────────────────────┤
  │         │ CVE-2026-56862 │          │        │                   │                              │ crypto/tls: golang: Golang crypto/tls: Denial of Service via │
  │         │                │          │        │                   │                              │ indefinite KeyUpdate messages                                │
  │         │                │          │        │                   │                              │ https://avd.aquasec.com/nvd/cve-2026-56862                   │
  └─────────┴────────────────┴──────────┴────────┴───────────────────┴──────────────────────────────┴──────────────────────────────────────────────────────────────┘
```

# For Redis image:

```
Report Summary
  ┌──────────────────────────────────┬────────┬─────────────────┬─────────┐
  │              Target              │  Type  │ Vulnerabilities │ Secrets │
  ├──────────────────────────────────┼────────┼─────────────────┼─────────┤
  │ redis:7.4-alpine (alpine 3.21.7) │ alpine │        0        │    -    │
  └──────────────────────────────────┴────────┴─────────────────┴─────────┘
```