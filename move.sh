files=~/Documents/Atcoder-Beginner-Contest/problems/AGC/*
for filepath in $files; do
    if [ -d $filepath/a ]; then
        continue
    else
        for file in $filepath/*; do
            f=${file##*_}
            f=${f%.*}
            mkdir $filepath/$f
            mv $file $filepath/$f/${file##*/}
        done
    fi
done
