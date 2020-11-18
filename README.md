# Bioinformatics Repositiory
## Contains various packages/classes for performing/processing bioinformatics related tasks/files

### Sub-directories:
* MSA: Processing MSA files (Not for performing MSA.... yet)

## Removing gaps from MSA for reprocessing

### MSA_Conv.sh - bash script that accomplishes this

* To install locally and be able to use globally (in any directory) on your local computer, use the following script:

```bash
sudo wget https://github.com/Mill6159/Bioinformatics/tree/master/MSA/BashScripts/MSA_Conv -P /usr/local/bin ;
cd /usr/local/bin ;
chmod u+x MSA_Conv ;
# chmod a+x MSA_Conv ;
cd ;
echo "You can now access MSA_Conv from any directory on this computer"
echo "Example: > MSA_Conv 'filename.fasta' "
``` 
