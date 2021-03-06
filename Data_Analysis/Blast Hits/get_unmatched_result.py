#!/usr/bin/python


import argparse

def main():

    parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("-b", "--blast", metavar="Blast_file", type=str, help="Path to blast out", required=True)
    parser.add_argument("-f", "--fasta", metavar="Fasta_file", type=str, help="Path to fasta file", required=True)
    parser.add_argument("-o", "--output", metavar="Output file with previous info", type = str, help="Output file", required=True)
    #Outfile is defualt Blast_results.tsv
    args = parser.parse_args()

    Pnummatch = 0
    lc = 0
    APnummatch = 0
    Fasta_Seqs=read_fasta(args.fasta)
    
    #get Pipeline name and Filter Name

    heads=args.fasta.split('_')
    sample=heads[0]
    pipe=heads[1]
    filt=heads[2]

    
    with open(args.output, "a") as out:
        
        with open(args.blast, "r") as blast:
            lc=0

            for line in blast:
                if lc == 3 and "Fields:" not in line:
                    lc = 0
                elif lc <= 4:
                    lc += 1
                else:
                    lc = 0
                    name,match,identity,align,mismatch,gap,qstart,qend,sstart,send,ev,bit = line.split("\t")
                    if identity == "100.000":
                        
                        #have to account for the carriage return
                        if (int(len(Fasta_Seqs[name]))-1) == int(align):
                            Pnummatch += 1
                        else:
                            score=float(align)/(float(len(Fasta_Seqs[name]))-1)
                            if score >= 0.97:
                                APnummatch += 1
                    elif float(identity) >= 97.0:
                        
                
                        if (int(len(Fasta_Seqs[name]))-1) == int(align):
                            APnummatch += 1
                        else:
                            Addmismatch = (int(len(Fasta_Seqs[name]))-1)-int(align)
                            newmismatch = Addmismatch + int(mismatch)
                            score = 1.0-(float(newmismatch))/(float(len(Fasta_Seqs[name]))-1)
                            if float(score) >= 0.97:
                                APnummatch += 1
        out.write("\n"+sample+"\t"+pipe+"\t"+filt+"\t"+str(Pnummatch)+"\t"+str(APnummatch))                
                    


    

def read_fasta(filename):


    seq = {}
    name = None


    with open(filename, "r") as fasta:

        for line in fasta:

            if line[0] == ">":
                name = line.split()[0][1:]

                seq[name] = ""

            else:

                line = line.rstrip("\r\n")
                seq[name] += line

    return seq

            
if __name__ == '__main__':
    main()
        

