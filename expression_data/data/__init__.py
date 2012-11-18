"""This app contains the views and models for expression data

Expression Objects
------------------

For microarray results (metadata in :class:`~experiments.models.MicroArrayExperiment`) there is only *gene* level data, as specified by the specific probe used.
For RNAseq results (metadata in :class:`~experiments.models.mRNASeqExperiment`), there is aggregated data at the level of the *gene*, *transcript*, *exon*, *promoter* and *splice site*.
Currently we are only able to work with gene level data.

Types of Data
-------------

The database can contain two types of data:

* SampleData level data, such as how many (hopefully normalized) counts are in each sample for each gene.
* ExperimentData, which includes the average counts for each group as well as statistical tests for differential expression.
"""