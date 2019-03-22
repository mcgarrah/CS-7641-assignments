# How to update a fork with the upstream master

```
$ cd CS-7641-assignments/

$ dir
assignment1  assignment2  assignment3  assignment4  data  LICENSE  README.md

$ git remote -v
origin  https://github.com/mcgarrah/CS-7641-assignments.git (fetch)
origin  https://github.com/mcgarrah/CS-7641-assignments.git (push)

$ git remote add upstream https://github.com/cmaron/CS-7641-assignments

$ git remote -v
origin  https://github.com/mcgarrah/CS-7641-assignments.git (fetch)
origin  https://github.com/mcgarrah/CS-7641-assignments.git (push)
upstream        https://github.com/cmaron/CS-7641-assignments (fetch)
upstream        https://github.com/cmaron/CS-7641-assignments (push)

$ git fetch upstream
remote: Enumerating objects: 42, done.
remote: Counting objects: 100% (42/42), done.
remote: Total 64 (delta 42), reused 42 (delta 42), pack-reused 22
Unpacking objects: 100% (64/64), done.
From https://github.com/cmaron/CS-7641-assignments
 * [new branch]      master              -> upstream/master
 * [new branch]      strftime-format-fix -> upstream/strftime-format-fix

$ git checkout master
Already on 'master'
M       data/loader.py
Your branch is up to date with 'origin/master'.

$ git merge upstream/master
Auto-merging assignment2/README.md
Merge made by the 'recursive' strategy.
 assignment2/README.md                  |  11 ++
 assignment2/plotting.py                |   5 +-
 assignment3/README.md                  |  15 +-
 assignment3/experiments/ICA.py         |   2 +-
 assignment3/experiments/PCA.py         |   2 +-
 assignment3/experiments/RF.py          |   2 +-
 assignment3/experiments/RP.py          |   2 +-
 assignment3/experiments/SVD.py         |   2 +-
 assignment3/experiments/__init__.py    | 271 +--------------------------------
 assignment3/experiments/base.py        |  13 +-
 assignment3/experiments/benchmark.py   |   2 +-
 assignment3/experiments/scoring.py     |   2 +-
 assignment3/requirements-no-tables.txt |   9 ++
 assignment3/requirements.txt           |   1 +
 assignment3/run_clustering.sh          |  21 +--
 assignment3/run_experiment.py          |  39 +++--
 16 files changed, 94 insertions(+), 305 deletions(-)
 create mode 100644 assignment3/requirements-no-tables.txt
```
