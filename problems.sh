# zsh problems.sh ABC 240

CURRENT=$(cd $(dirname $0);pwd)
dir=problems/$1/$2

if [ $1 = ABC ]; then
    KIND=abc$2
elif [ $1 = ARC ]; then
    KIND=arc$2
elif [ $1 = AGC ]; then
    KIND=agc$2
else
    echo "Error: $1"
    exit 1
fi

mkdir ${dir}

for i in a b c d e f g ex
do
touch ${dir}/${KIND}_$i.py
done