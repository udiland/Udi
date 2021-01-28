import os
import pandas as pd
import re
import subprocess
import argparse
#
# pd.set_option('display.width', 320)
# pd.set_option('display.max_columns', None)
# # pd.set_option('display.max_rows', None)
# pd.set_option("max_colwidth", 150)



def get_fam_data(path_to_folder):
    '''
    :param path_to_folder: the path to the parent folder. in the parent folder there is a folder for each family
    :return: output a table of:
    Name of family: # of genes
    Total number of sgRNAs: #
    Number of genes: Number of sgRNAs
    '''
    folders = os.listdir(path_to_folder)
    for f in folders:
        # create an empty dataframe with column names
        columns = ["No. of genes in family","sgRNA","Genes","No. of genes","score", "Max percent of family"]
        df = pd.DataFrame(columns=columns)

        if f.startswith("HOM"):
            family_folder = path_to_folder + "/" + f

            # get the amount of genes in that family
            grp = "grep '>' " + family_folder + "/" + f + ".txt | uniq | wc -l"
            n_genes = int(subprocess.check_output(grp, shell=True))
            df.loc[0, "No. of genes in family"] = n_genes

            # get the result of the filtering
            tbl = pd.read_csv(path_to_folder + "/" + f + "/output_filtered_final.csv", na_values="")

            # check if there are no sgrna
            if tbl.iloc[0:1,:].isnull().values.all():
                print("No sgRNA for this family")
                df.loc[0,"No. of genes in family" ] = 0
            else:
                lst = []
                for i in range(tbl.shape[0]):  # loop over the table and get the score and number of genes for each sgRNA
                    df.loc[i, "sgRNA"] = tbl.iloc[i, 0]

                    df.loc[i, "score"] = tbl.iloc[i,1]

                    genes = re.findall("(Solyc.*?)\s", tbl.iloc[i,2])
                    df.loc[i,"Genes"] = genes

                    n_genes_per_sg = len(genes)
                    df.loc[i, "No. of genes"] = n_genes_per_sg
                    lst.append(n_genes_per_sg)

            # calculate the max percent of genes that have sgRNA in the family
            percent_sgRNA = n_genes/max(lst) * 100
            df.loc[0, "Max percent of family"] = percent_sgRNA

        # write the table
        df.to_csv(family_folder + "filter_stat.csv")



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--path_to_folder', '-path')
    args = parser.parse_args()

    get_fam_data(args.path_to_folder)



