<?php
fscanf(STDIN, "%d\n", $t);

function p($y, $f)
{
    $z = !preg_match('/^1?$|^(11+?)\1+$/x', str_repeat('1', $y));
    if ($f==0) {
        return $z;
    } else {
        return !$z;
    }
}



  


function e($o, $p)
{
global $v,$m,$n, $g, $f;
    $q = [-1, 0, 0,  1];
    $r = [0,  -1, 1,  0];
    $v[$o][$p]=true;
    for ($s=0;$s<4;$s++) {
        $x=$o+$q[$s];
        $y=$p+$r[$s];
        // echo $g[$x][$y];
        if ($x>=0 && $x<$m && $y>=0 && $y<$n && !$v[$x][$y] && p($g[$x][$y], $f ) ){
            e($x, $y);
        } 
    }
}

function f1()
{
    global $m,$n, $f, $g, $v;
    $c=0;
    for ($a = 0; $a < $m; $a++) {
        for ($b = 0; $b < $n; $b++) {
            $v[$a][$b]=false;
        }
    }

    for ($a = 0; $a < $m; $a++) {
        for ($b = 0; $b < $n; $b++) {
            if ($v[$a][$b]==false && p($g[$a][$b], $f)) {
                e($a, $b);
                $c++;
                //print("c is ".$c);
            }
        }
    }
    return $c;
}


for ($s = 0; $s < $t; $s++) {
    fscanf(STDIN, "%d %d", $m, $n);
    for ($x = 0; $x < $m; $x++)
        {$g[$x] = array_map('intval', explode(' ', fgets(STDIN)));}

  $f=0;
print(f1()." ");
$f=1;
print(f1()."\n");

}

