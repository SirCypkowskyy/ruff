# This test was originally written to check that a third-party dependency gets
# priority over stdlib. But it was not clearly the right choice[1].
#
# 2026-05-11: We now prefer the stdlib symbol because ty doesn't yet know
# whether the third-party package is a direct or transitive dependency.
#
# [1]: https://github.com/astral-sh/ruff/pull/22460#discussion_r2676343225
fullmatch<CURSOR: re.fullmatch>
