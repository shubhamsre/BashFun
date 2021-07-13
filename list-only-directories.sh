#!/bin/bash
#The following code snippet will list all the leaf directories(a directory with no sub-directory) in any input path with full path to the directory.

module_dir=($(find $(pwd)/deployment/ -maxdepth 10 -type d -not -path '*/exclude-some-directory/*'))

for module in ${module_dir[@]}
  do
    ls -Rd $module/*/ > /dev/null 2>&1
    result=$?
    if [[ $result != 0 ]]
    then
      echo $module
    fi
done
