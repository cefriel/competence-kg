#!/bin/sh

# ** Remove comment if you want to re-generate the data **
# echo "Generating data..."
# python generate.py

while true;
do
    sleep 5
    if curl -s -I http://competence-kg-neo4j:7474 | grep -q "200 OK"
    then
        echo "Loading data in Neo4j..."
        python load.py
        break
    else
        echo "Neo4j not ready yet"
        continue
    fi
done
