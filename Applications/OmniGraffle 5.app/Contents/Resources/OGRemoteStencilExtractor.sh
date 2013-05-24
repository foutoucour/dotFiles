#!/bin/zsh -f

set -e

DOWNLOAD_FILE=$1
if [ -z "$DOWNLOAD_FILE" ]; then
  echo "No source file specified!"
  exit 0;
fi

TMPDIR=`mktemp -dt OG`

pushd $TMPDIR

case "$DOWNLOAD_FILE" in
    *.tar)
        tar -xf $DOWNLOAD_FILE
        ;;
    *.tgz)
        tar -xzf $DOWNLOAD_FILE
        ;;
    *.tar.gz)
        tar -xzf $DOWNLOAD_FILE
        ;;
    *.tbz)
        tar -xjf $DOWNLOAD_FILE
        ;;
    *.tar.bz2)
        tar -xjf $DOWNLOAD_FILE
        ;;
    *.gz)
        gunzip $DOWNLOAD_FILE
        ;;
    *.zip)
        ditto -xk $DOWNLOAD_FILE $TMPDIR
        ;;
    *)
        rm -r $TMPDIR
        ;;
esac

echo $TMPDIR

popd
