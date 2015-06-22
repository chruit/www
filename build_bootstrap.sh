#!/usr/bin/env bash

echo "changing to bootstrap dir"
cd bootstrap-3.3.5
grunt
cp dist/css/* ../chru_dot_edu/chru_dot_edu/static/css/
echo "returning to dir"
cd ..
echo "done building css for CHRU"
