#!/bin/bash

for i in *; do mv "$i" "${i/$1/$2}"; done


