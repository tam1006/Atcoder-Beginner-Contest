# zsh problems.sh ABC 240

CURRENT=$(cd $(dirname $0);pwd)
dir=problems/$1/$2

if [ $1 = ABC ]; then
    KIND=abc$2
    if [ $2 -le 125 ]; then
        fileary=(a b c d)
    elif [ $2 -le 211 ]; then
        fileary=(a b c d e f)
    elif [ $2 -le 232 ]; then
        fileary=(a b c d e f g h)
    else
        fileary=(a b c d e f g ex)
    fi
elif [ $1 = ARC ]; then
    KIND=arc$2
    fileary=(a b c d e f)
elif [ $1 = AGC ]; then
    KIND=agc$2
    if [ $2 -le 57 ]; then
        fileary=(a b c d)
    elif [ $2 -le 103 ]; then
        fileary=(c d e f)
    else
        fileary=(a b c d e f)
    fi
elif [ $1 = Other ]; then
    KIND=$2
    fileary=(a b c d e f)
else
    echo "Error: $1"
    exit 1
fi

mkdir ${dir}

for i in ${fileary[@]}
do
touch ${dir}/${KIND}_$i.py
done