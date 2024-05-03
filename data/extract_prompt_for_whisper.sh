#!/bin/zsh
cat "the dude 084.txt" | sed -n "/^Description:/,/^Transcript:/ {/^Transcript:/d;  /^$/d; p;}" 
