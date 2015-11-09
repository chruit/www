
echo "copy variables.less file"
copy variables.less bootstrap\less\variables.less
echo "changing to bootstrap dir for build"
cd bootstrap
call grunt
copy /Y dist\css\* ..\chru_dot_edu\chru_dot_edu\static\css
echo "returning to dir"
cd ..
echo "done building css for CHRU webpage"
