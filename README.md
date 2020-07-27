# PathwayTools
# Language: Python
# Input: TXT
# Output: TXT
# Tested with: PluMA 1.1, Python 3.6
# Dependency: Pathway Tools database, PythonCyc 1.0

Get data from Pathway Tools (Karp et al, 2015) database.  This plugin requires
PathwayTools to be installed and running on some host.

The plugin accepts as input a tab-delimited TXT file of keyword-value pairs:
hostname: Name of the host where PathwayTools is running
datatype: pathway or taxa.  "pathway" will retrieve information on all pathways
in PathwayTools; "taxa" will retrieve information on all taxa.
