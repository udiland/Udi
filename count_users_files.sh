




for user in $(ls -1d */); do n_files=$(find $user | wc -l); echo -e "$user\t$n_files"; done
