# Musterschreiben an Schulen

Letters to German schools whose content depends on parameters.
Parameters:

- Bundesland
- Attest: Hat der Schüler ein Attest, dass ihn von der Maskenpflicht befreit?
- Glaubhaftmachung: Sind die Eltern bereit, falls kein Attest vorliegt, eine Glaubhaftmachung abzuliefern, dass kein Attest getragen werden kann?

## Prerequisits

- Python 3.8

## Usage

Example: Dokument für Bundesland "Bayern", Option 1: kein Attest

	$ ./src/muster.py -o 1 Bayern

Print help:

	$ ./src/muster.py --help
