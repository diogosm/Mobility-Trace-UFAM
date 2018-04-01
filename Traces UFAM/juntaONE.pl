#!perl

#os arquivos tem que estar na mesma pasta
#perl juntaONE.pl > caminhos.gpx.one

@arq1 = `cat "02_05_2012 21h31.gpx.one"`;
@arq2 = `cat "03_05_2012 18h49.gpx.one"`;
@arq3 = `cat "08_05_2012 18h28.gpx.one"`;
@arq4 = `cat "09_05_2012 20h58.gpx.one"`;
@arq5 = `cat "26_04_2012 18h26.gpx.one"`;

$menorArq=100000000000;

$tempoMin=100000000000;
$tempoMax=-1;
$minX=100000000000;
$maxX=-1;
$minY=100000000000;
$maxY=-1;

for($i=1;$i<6;$i++){
	$nome="arq$i";
	$linha = @$nome[0];

	if(@$nome < $menorArq){
		$menorArq = @$nome;
	}
	
	if($linha=~/(.+?) (.+?) (.+?) (.+?) (.+?) (.+?)$/){ #01
		if($1 < $tempoMin){
			$tempoMin = $1;
		}
		
		if($2 > $tempoMax){
			$tempoMax = $2;
		}
		
		if($3 < $minX){
			$minX = $3;
		}
		
		if($4 > $maxX){
			$maxX = $4;
		}
		
		if($5 < $minY){
			$minY = $5;
		}
		
		if($6 > $maxY){
			$maxY = $6;
		}
	}
}

print "$tempoMin $tempoMax $minX $maxX $minY $maxY\n";

for($i=0;$i<$menorArq-1;$i++){
	print @arq1[$i+1];
	print @arq2[$i+1];
	print @arq3[$i+1];
	print @arq4[$i+1];
	print @arq5[$i+1];
}

