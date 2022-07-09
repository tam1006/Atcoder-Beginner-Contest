files=~/Documents/Atcoder-Beginner-Contest/problems/ABC/*
for filepath in $files; do
    if [ -d $filepath/a ]; then
        for f in $filepath/*; do
            echo $f
        done
    fi
done
