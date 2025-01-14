BASEDIR=$(realpath $(dirname $0))
cd $BASEDIR && poetry run start
exit 0
