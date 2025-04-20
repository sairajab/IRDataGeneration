# IRDataGeneration
Repo to use splicegrapher and idiffir to create IR data
Download and install SplceGrapher 2.7.0 (https://splicegrapher.sourceforge.net/index.html)
Download the genome annotaton fle(.gtf)
Run ```gene_model_to_splicegraph.py -m your_annotation_file.gtf -a -S -d reference``` , this will create a reference folder in which there will be splice graphers for each gene.
Run ```python get_AS_From_splicegrpah.py event_type path/to/reference```, this will create .txt file containing all AS events for the defined event (IR,A3,A5,SE)
Get all introns for the genome. You may use this repo (https://github.com/sairajab/RetrieveIntrons)
Run ```python get_retained_introns_from_IRevents.py``` to get the retained introns. Chnage the IR events file name (```ir_events_file```), all introns file name (```introns_file```) and output fie name (```output_file```). 
