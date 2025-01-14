BASEDIR=$(realpath $(dirname $0))
cd $BASEDIR && poetry run start
echo "Mouse switcher failed to start"
exit 1