#!/usr/bin/env zsh

###########################################################
# Script Description #

###########################################################
echo "#############################################################"
echo "------> Converting MSA alignment back to unaligned FASTA file"

## Define variable inputs
# Raise error if not provided

NAME=${1?Error: no name given}


# Remove file extension from input file name

NAME2=$(echo "$NAME" | cut -f 1 -d '.')

# Remove all gaps in input MSA file
# and output a new file with the same base name
# as the input file
# is this impacting the FASTA headers?! Does not seem like it.. but I may need to be slightly more clever

#cat $NAME | sed 's/[.-]//g' | more > ${NAME2}_NoGaps.fasta &
cat $NAME | sed 's/[-]//g' | more > ${NAME2}_NoGaps.fasta &
pid=$!

# If this script is killed, kill the `file conversion'.
trap "kill $pid 2> /dev/null" EXIT

# While copy is running...
while kill -0 $pid 2> /dev/null; do
    # Do stuff
    #echo "Running"
    TIME=$(ps -p $pid -o time | sed -n '2 p')
    echo "Total time elapsed: $TIME"
    sleep 0.2
done

# Disable the trap on a normal exit.
trap - EXIT


echo "------> MSA was converted and placed into file: $NAME2"
echo "#############################################################"
