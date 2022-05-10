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

if [ $2 -le 125 ]; then
    fileary=(a b c d)
elif [ $2 -le 211 ]; then
    fileary=(a b c d e f)
elif [ $2 -le 232 ]; then
    fileary=(a b c d e f g h)
else
    fileary=(a b c d e f g ex)
fi

for i in ${fileary[@]}
do
touch ${dir}/${KIND}_$i.py
done