#!/bin/bash

# Pass a list of IPs/URL and count the invalid responses per target
# Workaround script you can use curl/wget or even python for this.
# Another way to get Status Code - curl -I -s https://www.google.com | head -1 |cut -d " " -f 2
# The targets can be a file as well
#     while IFS= read -r target; do
#           //Action
#     done < targets.txt

targets=(www.google.com www.fb.com 127.0.0.1  https://regex101.com/retry shubham.github.io http://localhost https://regex101.com/fun)

invalid_status=(300 301 302 400 403 404)
rm target.txt

for target in ${targets[@]}; do
  echo "Checking Target: $target"
  count=$(curl -o /dev/null -s -w "%{http_code}\n" $target)
  
  for status in ${invalid_status[@]}; do
         if [ $status -eq $count ]
         then
           echo $t >> target.txt
        # else
        #    echo "else condition if any"
         fi
  done
done

uniq -c target.txt | awk '{print $2": "$1}'
