<?php
fscanf(STDIN, "%d\n", $t);

for ($s = 0; $s < $t; $s++) {
    fscanf(STDIN, "%d %d", $a, $b);
    for ($x = 0; $x < $a; $x++)
        $g[$x] = array_map('intval', explode(' ', fgets(STDIN)));

        print_r($g);

}


