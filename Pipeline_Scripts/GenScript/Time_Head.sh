./Dada2Pipe.sh ../../Config/dada2/time/5k.txt low &
./Dada2Pipe.sh ../../Config/dada2/time/10k.txt low &
./Dada2Pipe.sh ../../Config/dada2/time/20k.txt low &
wait
./Dada2Pipe.sh ../../Config/dada2/time/30k.txt low &
./Dada2Pipe.sh ../../Config/dada2/time/40k.txt low &
wait
./UsearchPipe.sh ../../Config/unoise/time/5k.txt low &
./UsearchPipe.sh ../../Config/unoise/time/10k.txt low &
./UsearchPipe.sh ../../Config/unoise/time/20k.txt low &
wait
./UsearchPipe.sh ../../Config/unoise/time/30k.txt low &
./UsearchPipe.sh ../../Config/unoise/time/40k.txt low &
wait
./DeblurPipeP.sh ../../Config/deblur/time/5kdeblur.txt low &
./DeblurPipeP.sh ../../Config/deblur/time/10kdeblur.txt low &
./DeblurPipeP.sh ../../Config/deblur/time/20kdeblur.txt low &
wait
./DeblurPipeP.sh ../../Config/deblur/time/30kdeblur.txt low &
./DeblurPipeP.sh ../../Config/deblur/time/40kdeblur.txt low &


wait
