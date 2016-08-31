# cleanSPAdesContigs

python script to easily clean contigs in an assembly file. Removed contigs with length smaller than 200bp or with coverage smaller than 5. 

# Updates
  (30th Aug 2016) - Changed coverage mininum from 10 to 5. Script now runs when SPAdes contigs headers have been modified: extra information added at the beginning or/end of the headers (keeping SPAdes headers inbetween) (by miguelpmachado)

# Dependencies
cleanSPAdesContigs has no dependencies

# Instalation
cleanSPAdesContigs is a standalone python script and does not require any installation. Simply clone the git repository:

    git clone https://github.com/cimendes/cleanSPAdesContigs.git

# Usage
    python cleanSpadesContigs.py <contig to clean> <name of the output file>

