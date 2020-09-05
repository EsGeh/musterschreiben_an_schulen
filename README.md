# Musterschreiben an Schulen

Letters to German schools whose content depends on parameters.
Parameters:

- Bundesland
- Attest: Hat der Schüler ein Attest, dass ihn von der Maskenpflicht befreit?
- Glaubhaftmachung: Sind die Eltern bereit, falls kein Attest vorliegt, eine Glaubhaftmachung abzuliefern, dass kein Attest getragen werden kann?

## Prerequisits

- Python 3.8

## Print single case

Example: Dokument für Bundesland "Bayern", Option: Attest

	$ ./src/muster.py -o attest Bayern

Print help:

	$ ./src/muster.py --help

## Generate all cases

	$ ./src/gen_all_docs.py

This will write the output for all cases to `./output/` as text files, conveniently named.
