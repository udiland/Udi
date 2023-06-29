# !/bin/bash

#PBS -S /bin/bash
#PBS -r y
#PBS -q itaym
#PBS -v PBS_O_SHELL=bash,PBS_ENVIRONMENT=PBS_BATCH
#PBS -N get_storage
#PBS -e /groups/itay_mayrose/udiland/cluster_scripts/user_storage_24_11.ER
#PBS -o /groups/itay_mayrose/udiland/cluster_scripts/user_storage_24_11.OU
#PBS -l select=ncpus=1:mem=8gb

cd /groups/itay_mayrose

for user in $(ls -1d */); do (du -sh $user);done

