# Bash Scripts README

## Script 1 - MSA_Conv

Converts MSA back to unaligned FASTA format (i.e. Blast file). This is very useful when trimming MSA's and attempting to re-align  

To install locally:  
**(1)** Download from GitHub: 

**(2)** Grab script from downloads directory and drop it into "/usr/local/bin"

**(3)** Give the executable the appropriate permissions

**(4)** Run the exectuable from any directory on the computer!

*To install as described above, simply copy and paste the below script into your terminal*

```bash
sudo wget https://github.com/Mill6159/Bioinformatics/tree/master/MSA/BashScripts/MSA_Conv -P /usr/local/bin ;
cd /usr/local/bin ;
chmod u+x MSA_Conv ;
# chmod a+x MSA_Conv ;
cd ;
echo "You can now access MSA_Conv from any directory on this computer"
echo "Example: > MSA_Conv 'filename.fasta' "
```

*Note the following:*
* ```chmod u+x``` - grants executable permissions to the current user

* ```chmod a+x``` - grants executable permissions to all users

