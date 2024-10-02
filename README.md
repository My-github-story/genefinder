# BioE_week_4 - Gene Finder Tool
This tool finds Open Reading Frames (ORFs) in FASTA files.
## Requirements
1) Python 3.6+
2) BioPython
## Installation
1) Clone this repository
2)Install dependencies: ```pip install biopython```

## Usage

### For simple gene finder
python genefinder.py input_file.fna

### For gene finder with reverse compliments
python genefinder_reverse.py input_file.fna

### For gene finder with length filter
python genefinder_filtered.py input_file.fna -l min_length

### For gene finder with length filter, rbs location, and rbs sequence
python genefinder_rbs.py input_file.fna -l min_length -u upstream_bp -r rbs_sequence

# Steps followed to create this repo
## Initialize Directory for Git
mkdir BioE_week_4
cd BioE_week_4
git init
touch genefinder.py README.md

## Implementing genefinder
nano genefinder.py
git add genefinder.py README.md
git commit -m "added genefinder.py"

# usage
python genefinder.py /home/khant0a/genomes/ecoli.fna > output1.txt

## Implementing gene finder with reverse complements
touch genefinder_reverse.py
nano genefinder_reverse.py
git add genefinder_reverse.py 
git commit -m "added genefinder_reverse.py"

# usage
python genefinder_reverse.py /home/khant0a/genomes/ecoli.fna > output2.txt

## Applying code to all 14 downloaded genomes
```find /home/khant0a/ncbi_dataset/data -type f -name "*GCF*.fna" | while read genome; do python genefinder_reverse.py "$genome"; done > all_orfs.txt```

## Implementing gene finder with length filter
touch genefinder_filtered.py
nano genefinder_filtered.py
git add genefinder_reverse.py 
git commit -m "added genefinder_filtered.py"

# usage
python genefinder_filtered.py /home/khant0a/genomes/ecoli.fna -l 100

## Implementing gene finder with length, rbs site and rbs type filter
touch genefinder_rbs.py
nano genefinder_rbs.py
git add genefinder_rbs.py 
git commit -m "added genefinder_rbs.py"

# usage
python genefinder_rbs.py /home/khant0a/genomes/ecoli.fna -l 100 -u 20 -r AGGAGG

## Push repo to github
git remote add origin https://github.com/ashhadm/BioE_week_4.git
git branch -M main
git push -u origin main
