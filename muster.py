#!/usr/bin/env python3

from enum import Enum
import argparse

skip = False


class Options(Enum):
    ATTEST = 1
    NO_ATTEST = 2
    LIST = 3


def main(
        options,
        glaubhaftmachung,
        bundesland
):

    # Glaubhaftmachung:
    """
    Für folgende Bundesländer:
        Bayern
        Brandenburg
        Niedersachsen
        Sachsen-Anhalt
        Thüringen
    """


    print_skip(
"""Sehr geehrte Damen und Herren,

Ich bin Elternteil von [Kind]. Laut Artikel 6 Abs. 2 Grundgesetz sind Pflege und Erziehung der Kinder das natürliche Recht der Eltern und die zuvörderst ihnen obliegende Pflicht.

Im Rahmen meines Pflege- und Erziehungsauftrages stelle ich fest, dass mein Kind vom Tragen der Mund-Nasenbedeckung in der Schule ausgenommen ist.

Die Verpflichtung meines Kindes, eine Mund-Nasen-Bedeckung zu tragen, ist zur Minderung des Übertragsungsrisikos von SARS-COV-2 nicht geeignet und stellt einen unverhältnismäßigen Eingriff in die Grundrechte meines Kindes aus Artikel 2 Abs. 1 und Art. 2 Abs. 2 S. 1 GG dar.

Dies ergibt sich aus Folgendem:

1. Fehlender Nachweis einer Schutzwirkung vor SARS-COV-2

Eine Schutzwirkung der Mund-Nasen-Bedeckung vor der Übertragung von SARS-COV-2 ist ausweislich der Hinweise des Bundesinstituts für Arzneimittel und Medizinprodukte (BfArM) zur Verwendung von Mund–Nasen-Bedeckungen u.A. im Zusammenhang mit dem Coronavirus nicht nachgewiesen (vgl. https://www.bfarm.de/SharedDocs/Risikoinformationen/Medizinprodukte/DE/schutzmasken.html Stand: 26.06.2020).

2. Gefahr der Gesundheitsschädigung meines Kindes

Das Tragen einer Mund-Nasen-Bedeckung kann wissenschaftlich erwiesenermaßen gesundheitsschädigend sein. Dies gilt in a) psychischer und b) physischer Hinsicht.

a) Laut aktueller Studie zu psychischen und psychovegetativen Beschwerden mit den aktuellen Mund-Nasenschutz-Verordnungen der Diplom-Psychologin Daniela Prousa (abrufbar unter http://dx.doi.org/10.23668/psycharchives.3135 ) hat „die Maske“ das Potenzial, über entstehende Aggression starke psychovegetative Stressreaktionen zu bahnen, die signifikant mit dem Grad belastender Nachwirkungen korrelieren. Ca. 60% der sich deutlich mit den Verordnungen belastet erlebenden Menschen erlebt schon jetzt schwere (psychosoziale) Folgen, wie eine stark reduzierte Teilhabe am Leben in der Gesellschaft aufgrund von aversionsbedingtem MNS-Vermeidungsbestreben, sozialen Rückzug, herabgesetzte gesundheitliche Selbstfürsorge (bis hin zur Vermeidung von Arztterminen) oder die Verstärkung vorbestandener gesundheitlicher Probleme (posttraumatische Belastungsstörungen, Herpes, Migräne).

b) In physischer Hinsicht wurde durch die publizierte Studie Fikenzer, S., Uhe, T., Lavall, D. et al. Effects of surgical and FFP2/N95 face masks on cardiopulmonary exercise capacity. Clin Res Cardiol (2020) https://doi.org/10.1007/s00392-020-01704-y nachgewiesen, dass die so genannte kardiopulmonale Leistungsfähigkeit durch beide Masken-Typen signifikant reduziert wird. Die Masken beeinträchtigen die Atmung, vor allem das Volumen und die höchstmögliche Geschwindigkeit der Luft beim Ausatmen. Die maximal mögliche Kraft auf dem Fahrrad-Ergometer war deutlich reduziert. Im Stoffwechsel wurde eine schnellere Ansäuerung des Blutes bei Anstrengung registriert (Laktat). Mit Fragebögen beurteilten die Teilnehmer zudem systematisch ihr subjektives Empfinden. Auch hier zeigte sich eine erhebliche Beeinträchtigung verschiedener Parameter des Wohlbefindens ( https://www.uniklinikum-leipzig.de/presse/Seiten/Pressemitteilung_7089.aspx ). Ebenso wies Frau Dr. Butz einen signifikanten Anstieg der CO2-Werte im Blut durch das 30 minütige Tagen von OP Masken nach. Diese sog. Hyperkapnie kann verschiedene Hirnfunktionen einschränken (vgl. https://mediatum.ub.tum.de/doc/602557/602557.pdf?fbclid=IwAR2LEU08iFloOPJsBKYb9SOjwCORq3dLLhfzJy3aq35TUFdUdcUpSbJHvE4).
Im Ergebnis bedeutet dies, dass durch das Tragen der genannten Masken eine objektiv messbare gesundheitliche Beeinträchtigung der Körperfunktion Atmung verursacht wird, verschiedene Hirnfunktionen eingeschränkt und subjektiv eine mehr als nur unerhebliche Beeinträchtigung des körperlichen Wohlbefindens hervorgerufen werden können.

3. Nach dem o.g. Hinweisschreiben des BfArM gibt es unbedingt zu berücksichtigende Regeln zum Tragen einer Mund-Nasen-Bedeckung. Die Berücksichtigung jener Regeln kann ich nicht überwachen, soweit mein Kind sich in der Schule aufhält.

Mein Kind wird, sofern es durch die Schule dazu gebracht wird, eine Mund-Nasen-Bedeckung zu tragen, mindestens den o.g. Gesundheitsgefahren ausgesetzt, trotz gleichzeitig bestehender erheblicher Zweifel daran, ob durch die Mund-Nasen-Bedeckung überhaupt eine Schutzwirkung vor Sars-CoV-2 bewirkt wird. Ich möchte darauf hinweisen, dass die Schule die Verantwortung hierfür trägt. Daraus folgen erhebliche Haftungsrisiken für die Schule. Die Regeln des BfArM zum Tragen einer Mund-Nasen-Bedeckung dienen offenbar dazu, die folgenden Gefahrenquellen für die Gesundheit im Zusammenhang mit dem Tragen einer Mund-Nasen-Bedeckung zu reduzieren:

    • Kontamination der Innenseite der Maske
    • Behinderung der Atmung
    • Kontamination der Hände
    • Durchfeuchtung der Maske
    • Schimmelbildung

Für Gesundheitsschäden aufgrund dieser Gefahrenquellen, die durch schulischerseits veranlasstes Tragen einer Mund-Nasen-Bedeckung verursacht werden, haftet die Schule.

Es obliegt insoweit der Schulleitung, zur Minimierung des eigenen Haftungsrisikos organisatorisch sicherzustellen, dass die jeweilige Aufsichtspersonen die Einhaltung der Regeln des BfArM kontrolliert.

Überdies haftet die jeweilige Aufsichtsperson zivil- und strafrechtlich persönlich für Schäden, die das Kind durch das Tragen der Mund-Nasen-Bedeckung unter der Aufsicht der jewiligen Aufsichtsperson nimmt."""
        )
    if options == Options.LIST:
        print_skip(
"""

Mein Kind wird daher jedenfalls so lange keine Mund-Nasen-Bedeckung tragen, bis die Schule sicherstellt, dass die Aufsicht über das ordnungsgemäße Tragen einer Mund-Nasen-Bedeckung durch das Aufsichtspersonal in der von mir vorgeschriebenen Form laut anliegender Checkliste übernommen wird. Dies ist durch Unterschriften auf der Checkliste zu bestätigen."""
        )
    else:
        print_skip(
"""

4. Die Regelungen zum Tragen einer Mund-Nasen-Bedeckung selbst sehen vor, dass mein Kind keine Mund-Nasen-Bedeckung tragen muss."""
        )

        # Baden-Württemberg
        if bundesland == "Baden-Württemberg":
            print_skip(
"""

Laut § 3 I Nr. 6 der Verordnung der Landesregierung über infektionsschützende Maßnahmen gegen die Ausbreitung des Virus SARS-CoV-2 (Corona-Verordnung – CoronaVO) vom 23. Juni 2020 in der ab 6. August 2020 gültigen Fassung besteht ab den auf den Grundschulen aufbauenden Schulen (ab der 5. Klasse) für Kinder bis zum Vollendeten 6. Lebensjahr auf dem Schulgelände und in den Gebäuden die Pflicht, eine sog. Alltagsmaske tragen, mit Ausnahme des Unterrichts.

Eine Verpflichtung zum Tragen einer Mund-Nasen-Bedeckung besteht jedoch nach § 3 Abs. 2 Nr. 2 derselben Verordnung nicht für Personen, denen das Tragen einer Mund-Nasen-Bedeckung aus gesundheitlichen oder sonstigen Gründen nicht möglich oder nicht zumutbar ist.

Mein Kind kann aufgrund einer gesundheitlichen Beeinträchtigung keine Mund-Nasen-Bedeckung tragen."""
            )
            if options == Options.ATTEST:
                print_skip(
"""

Ein Erfordernis der Glaubhaftmachung hierzu besteht zwar nicht. Um Ihnen entgegenzukommen lege ich jedoch anliegendes Attest vor."""
                )
            else:
                print_skip(
"""

Ein Erfordernis der Glaubhaftmachung hierzu besteht rechtlich nicht. Von einer Glaubhaftmachung wird daher abgesehen."""
            )

        # Bayern
        elif bundesland == "Bayern":
            print_skip(
"""

Gemäß der 6. BayIfSMV (Bayerische Infektionsschutzmaßnahmenverordnung) vom 19. Juni 2020 in Verbindung mit dem Corona-Pandemie Rahmen-Hygieneplan zur Umsetzung des Schutz- und Hygienekonzepts für Schulen nach der jeweils geltenden Infektionsschutzmaßnahmenverordnung vom 01.08.2020 besteht für Kinder ab dem 6. Geburtstag die Pflicht zum Tragen einer Mund-Nasen-Bedeckung (MNB) oder einer geeigneten textilen Barriere im Sinne einer MNB (sogenannte community masks oder Behelfsmasken, z. B. Textilmasken aus Baumwolle). Diese Pflicht umfasst alle Räume und Begegnungsflächen im Schulgebäude (wie z.B. Unterrichtsräume, Fachräume, Turnhallen, Flure, Gänge, Treppenhäuser, im Sanitärbereich, beim Pausenverkauf, in der Mensa, während der Pausen und im Verwaltungsbereich) und auch im freien Schulgelände (wie z.B. Pausenhof, Sportstätten).

Ausgenommen von dieser Pflicht sind alle Personen, die glaubhaft machen können, dass ihnen das Tragen einer Mund-Nasen-Bedeckung aufgrund einer Behinderung oder aus gesundheitlichen Gründen nicht möglich oder unzumutbar ist (§ 1 Abs. 2 der 6. BayIfSMV).

Mein Kind kann aufgrund einer gesundheitlichen Beeinträchtigung keine Mund-Nasen-Bedeckung tragen."""
            )
            if options == Options.ATTEST:
                print_skip(
"""

Ich weise dies durch die Vorlage des anliegenden Attestes nach."""
                )
            else:
                if glaubhaftmachung:
                    print_skip(
"""

Der Nennung von gesundheitlichen Details ist aus datenschutzrechtlichen Gründen (vgl. Art. 9 DSGVO) nicht zur Glaubhaftmachung geeignet. Um Ihnen entgegenzukommen erkläre ich mich bereit, stattdessen eine eidesstattliche Versicherung darüber abzugeben, dass bei meinem Kind gesundheitliche Gründe dem Tragen einer Mund-Nasen-Bedeckung entgegenstehen."""
                    )
                else:
                    print_skip(
"""

Der Zusatz der Pflicht zur Glaubhaftmachtung entfaltet schon deshalb keine Wirksamkeit, weil der Adressat der der Glaubhaftmachtung (derjenige, dem gegenüber die Glaubhaftmachtung zu erfolgen hat) nicht genannt ist. Von einer Glaubhaftmachung wird daher abgesehen."""
                )

        # Berlin
        if bundesland == "Berlin":
            print_skip(
"""

Laut § 4 Abs. 2 Nr. 2 SARS-CoV-2-Infektionsschutzverordnung in der Fassung der Dritten Verordnung zur Änderung der SARS-CoV-2-Infektionsschutzverordnung vom 4. August 2020, verkündet im Gesetz- und Verordnungsblatt für Berlin, 76. Jahrgang, Nr. 37 vom 7. August 2020, S. 658 ff. gilt die Pflicht zum Tragen einer Mund-Nasen-Bedeckung nicht für Personen, die aufgrund einer gesundheitlichen Beeinträchtigung oder einer Behinderung keine Mund-Nasen-Bedeckung tragen können.

Mein Kind kann aufgrund einer gesundheitlichen Beeinträchtigung keine Mund-Nasen-Bedeckung tragen."""
            )
            if options == Options.ATTEST:
                print_skip(
"""

Ein Erfordernis der Glaubhaftmachung hierzu besteht zwar nicht. Um Ihnen entgegenzukommen lege ich jedoch anliegendes Attest vor."""
                )
            else:
                print_skip(
"""

Ein Erfordernis der Glaubhaftmachung hierzu besteht rechtlich nicht. Von einer Glaubhaftmachung wird daher abgesehen."""
                )

        # Brandenburg
        elif bundesland == "Brandenburg":
            print_skip(
"""

Die Verordnung über den Umgang mit dem SARS-CoV-2-Virus und COVID-19 in Brandenburg in der Fassung der Verordnung zur Änderung der SARS-CoV-2-Umgangsverordnung vom 26. Juni 2020, verkündet im Gesetz- und Verordnungsblatt für das Land Brandenburg 31. Jahrgang vom 26. Juni 2020 Nummer 54, bestimmt in § 2 Abs. 1 Nr. 8 die Pflicht zum Tragen einer Mund-Nasen-Bedeckung in den Innenbereichen von Schulen nach § 16 des Brandenburgischen Schulgesetzes und in freier Trägerschaft außerhalb des Unterrichts, der Ganztagsangebote sowie der sonstigen pädagogischen Angebote. 

Selbst wenn eine solche Pflicht aber bestünde, so würde sie nach den Maßstäben der Verordnung nicht unbeschränkt gelten.

Laut § 2 Abs. 2 derselben Verordnung muss die Mund-Nasen-Bedeckung aufgrund ihrer Beschaffenheit geeignet sein, eine Ausbreitung von übertragungsfähigen Tröpfchenpartikeln beim Husten, Niesen, Sprechen oder Atmen zu verringern, unabhängig von einer Kennzeichnung oder zertifizierten Schutzkategorie. Bei Mund-Nasen-Bedeckungen ist eine solche Geeignetheit indes, wie oben ausgeführt, nicht nachgewiesen. Die Pflicht zum Tragen einer solchen gilt schon deshalb nicht.

Nach § 2 Abs. 3 Nr. 3 derselben Verordnung sind ferner von der Pflicht zum Tragen einer Mund-Nasen-Bedeckung Personen ausgenommen, denen die Verwendung einer Mund-Nasen-Bedeckung wegen einer Behinderung oder aus gesundheitlichen Gründen nicht möglich oder unzumutbar ist; dies sei in geeigneter Weise glaubhaft zu machen.

Mein Kind kann aufgrund einer gesundheitlichen Beeinträchtigung keine Mund-Nasen-Bedeckung tragen."""
            )
            if options == Options.ATTEST:
                print_skip(
"""

Ich weise dies durch die Vorlage des anliegenden Attestes nach."""
                )
            else:
                if glaubhaftmachung:
                    print_skip(
"""

Der Nennung von gesundheitlichen Details ist aus datenschutzrechtlichen Gründen (vgl. Art. 9 DSGVO) nicht zur Glaubhaftmachung geeignet. Um Ihnen entgegenzukommen erkläre ich mich bereit, stattdessen eine eidesstattliche Versicherung darüber abzugeben, dass bei meinem Kind gesundheitliche Gründe dem Tragen einer Mund-Nasen-Bedeckung entgegenstehen."""
                    )
                else:
                    print_skip(
"""

Der Zusatz der Pflicht zur Glaubhaftmachtung entfaltet schon deshalb keine Wirksamkeit, weil der Adressat der der Glaubhaftmachtung (derjenige, dem gegenüber die Glaubhaftmachtung zu erfolgen hat) nicht genannt ist. Von einer Glaubhaftmachung wird daher abgesehen."""
                    )

        # Bremen
        elif bundesland == "Bremen":
            print_skip(
"""

Gemäß der dreizehnten Coronaverordnung vom 5. August 2020 i.V.m. dem Rahmenkonzept für das Schuljahr 2020/21 vom 14.07. soll eine Mund-Nasen-Bedeckung innerhalb des Schulgebäudes dann getragen werden, wenn Abstände nicht eingehalten werden können. 

Nach § 3 Abs. 3 Nr. 3 deserlben Verordnung gilt diese Pflicht jedoch nicht, für Personen, denen die Verwendung einer Mund-Nasen-Bedeckung wegen einer Behinderung, einer Schwangerschaft oder aus gesundheitlichen Gründen nicht möglich oder nicht zumutbar ist."""
            )
            if options == Options.ATTEST:
                print_skip(
"""

Ein Erfordernis der Glaubhaftmachung hierzu besteht zwar nicht. Um Ihnen entgegenzukommen lege ich jedoch anliegendes Attest vor."""
                )
            else:
                print_skip(
"""

Ein Erfordernis der Glaubhaftmachung hierzu besteht rechtlich nicht. Von einer Glaubhaftmachung wird daher abgesehen."""
                )

        # Hamburg
        elif bundesland == "Hamburg":
            print_skip(
"""

Der gemäß § 23 Abs. 1 S. 2 der Verordnung zur Eindämmung der Ausbreitung des Coronavirus SARS-CoV-2 in der Freien und Hansestadt Hamburg (Hamburgische SARS-CoV-2-Eindämmungsverordnung – HmbSARS-CoV-2-EindämmungsVO, HmbGVBl. Nr. 41 vom 7. August 2020 von der Schulbehörde aufgestellte Muster-Corona-Hygieneplan für alle staatlichen Schulen in der Freien und Hansestadt Hamburg in der 2. überarbeiteten Fassung, sieht unter 3. Absatz 2 die grundsätzliche Pflicht aller Personen vor, an den Schulen während der Schulzeit bis auf Weiteres eine Mund-Nasen-Bedeckung zu tragen („Maskenpflicht“).

Laut Ziffer 3., Absatz 2 Nummer 5. des Muster-Hygieneplans ist von der Maskenpflicht ausgenommen, wer aus gesundheitlichen Gründen keine MNB tragen kann oder darf.

Mein Kind kann aufgrund einer gesundheitlichen Beeinträchtigung keine Mund-Nasen-Bedeckung tragen."""
            )
            if options == Options.ATTEST:
                print_skip(
"""

Ein Erfordernis der Glaubhaftmachung hierzu besteht zwar nicht. Um Ihnen entgegenzukommen lege ich jedoch anliegendes Attest vor."""
                )
            else:
                print_skip(
"""

Ein Erfordernis der Glaubhaftmachung hierzu besteht rechtlich nicht. Von einer Glaubhaftmachung wird daher abgesehen."""
                )

        # Hessen
        elif bundesland == "Hessen":
            print_skip(
"""

In der 2. Corona-VO (Krankenhäuser, Senioren- und Plfegeeinrichtungen, Schul-und Kitabesuch; gültig ab 1. August 2020) sowie der 2. Corona-VO (Krankenhäuser, Senioren- und Pflegeeinrichtungen, Schul- und Kitabesuch; gültig ab 17. August 2020) ist in § 3 Abs. 1 S. 2 bzw. S. 3 vorgesehen, dass die Leiterin oder der Leiter allgemein oder für bestimmte Fallgruppen anordnen kann, dass außerhalb des Präsenzunterrichts im Klassen- oder Kursverband eine Mund-Nasen-Bedeckung nach § 1a Satz 2 derselben Verordnung zu tragen ist.

Mund-Nasen-Bedeckung im Sinne des Satz 1 ist jede Bedeckung vor Mund und Nase, die auf Grund ihrer Beschaffenheit unabhängig von einer Kennzeichnung oder zertifizierten Schutzkategorie geeignet ist, eine Ausbreitung von übertragungsfähigen Tröpfchenpartikeln oder Aerosolen durch Husten, Niesen oder Aussprache zu verringern. Bei Mund-Nasen-Bedeckungen ist eine solche Geeignetheit indes, wie oben ausgeführt, nicht nachgewiesen. Eine Pflicht zum Tragen einer solchen kann schon deshalb keine Wirkung entfalten.

Falls es nichts desto trotz zu einer solchen Anordnung kommt, gilt die Pflicht jedenfalls nach § 1a S. 3 derselben Verordnung nicht für Kinder unter 6 Jahren oder Personen, die aufgrund einer gesundheitlichen Beeinträchtigung oder einer Behinderung keine Mund-Nasen-Bedeckung tragen können. 

Mein Kind kann aufgrund einer gesundheitlichen Beeinträchtigung keine Mund-Nasen-Bedeckung tragen."""
            )
            if options == Options.ATTEST:
                print_skip(
"""

Ein Erfordernis der Glaubhaftmachung hierzu besteht zwar nicht. Um Ihnen entgegenzukommen lege ich jedoch anliegendes Attest vor."""
                )
            else:
                print_skip(
"""

Ein Erfordernis der Glaubhaftmachung hierzu besteht rechtlich nicht. Von einer Glaubhaftmachung wird daher abgesehen."""
                )

        # Mecklenburg-Vorpommern
        elif bundesland == "MV":
            print_skip(
"""

Eine Pflicht zum Tragen einer Mund-Nasen-Bedeckung in der Schule ist in der Verordnung der Landesregierung zur Corona-Lockerungs-LVO MV und zur Änderung der Quarantäneverordnung GS Meckl.-Vorp. Gl.-Nr. B 2126 - 13 - 20 in der Fassung der Verordnung der Landesregierung zur Änderung der Corona-Lockerungs-LVO MV und zur Änderung der Quarantäneverordnung GS Meckl.-Vorp. vom 12. August 2020, Gesetz- und Verordnungsblatt für Mecklenburg-Vorpommern Nr. 52, S. 670 nicht enthalten.

Es enthält lediglich der § 1 S. 3 derselben Verordnung die Empfehlung, eine Mund-Nasen-Bedeckung (zum Beispiel Alltagsmaske, Schal, Tuch) zu tragen.

Selbst, wenn eine solche Pflicht anderweitig bestünde, so sieht die Verordnung stets vor, dass Menschen, die aufgrund einer medizinischen oder psychischen Beeinträchtigung oder wegen einer Behinderung keine Mund-Nasen-Bedeckung tragen können und dies durch eine ärztliche Bescheinigung nachweisen können, ausgenommen sind.

Mein Kind kann aufgrund einer gesundheitlichen Beeinträchtigung keine Mund-Nasen-Bedeckung tragen."""
            )
            if options == Options.ATTEST:
                print_skip(
"""

Ich weise dies durch die Vorlage des anliegenden Attestes nach."""
                )
            else:
                print_skip(
"""

Der Zusatz der Pflicht zur Beibringung einer ärztlichen Bescheinigung entfaltet schon deshalb keine Wirksamkeit, weil der Vorlageadressat nicht in der Verordnung genannt ist. Von einem Nachweis wird daher abgesehen."""
                )

        # Niedersachsen
        elif bundesland == "Niedersachsen":
            print_skip(
"""

Gemäß § 17 Abs. 1 Satz 4 der Niedersächsischen Corona-Verordnung vom 10. Juli 2020 in der Fassung vom 31. Juli 2020 hat außerhalb von Unterrichts- und Arbeitsräumen jede Person eine Mund-Nasen-Bedeckung in von der Schule besonders gekennzeichneten Bereichen zu tragen, in denen aufgrund der örtlichen Gegebenheiten die Einhaltung des Abstandsgebots nach § 1 Abs. 3 S. 1 zwischen Personen, die nicht derselben Gruppe im Sinne des Satzes 1 angehörten (zu Personen anderer Kohorten), nicht gewährleistet werden kann.

Nach dem Niedersächsischen Rahmen-Hygieneplan Corona Schule vom 05.08.2020 sind Personen, für die aufgrund einer körperlichen, geistigen oder psychischen Beeinträchtigung oder einer Vorerkrankung, zum Beispiel einer schweren Herz- oder Lungenerkrankung, das Tragen einer MNB nicht zumutbar ist und die dies glaubhaft machen können, sind von der Verpflichtung ausgenommen."""
            )
            if options == Options.ATTEST:
                print_skip(
"""

Ich weise dies durch die Vorlage des anliegenden Attestes nach."""
                )
            else:
                if glaubhaftmachung:
                    print_skip(
"""

Der Nennung von gesundheitlichen Details ist aus datenschutzrechtlichen Gründen (vgl. Art. 9 DSGVO) nicht zur Glaubhaftmachung geeignet. Um Ihnen entgegenzukommen erkläre ich mich bereit, stattdessen eine eidesstattliche Versicherung darüber abzugeben, dass bei meinem Kind gesundheitliche Gründe dem Tragen einer Mund-Nasen-Bedeckung entgegenstehen."""
                    )
                else:
                    print_skip(
"""

Der Zusatz der Pflicht zur Glaubhaftmachtung entfaltet schon deshalb keine Wirksamkeit, weil der Adressat der der Glaubhaftmachtung (derjenige, dem gegenüber die Glaubhaftmachtung zu erfolgen hat) nicht genannt ist. Von einer Glaubhaftmachung wird daher abgesehen."""
                    )

        # Nordrhein-Westfalen
        elif bundesland == "NRW":
            print_skip(
"""

Nach § 1 Abs. 3 der Verordnung zum Schutz vor Neuinfizierungen mit dem Coronavirus SARS-CoV-2 im Bereich der Betreuungsinfrastruktur (Coronabetreuungsverordnung – CoronaBetrVO), verkündet im Gesetz- und Verordnungsblatt (GV. NRW.) Ausgabe 2020 Nr. 33a vom 11.8.2020 Seite 721a bis 768 sind alle Personen, die sich in einem Schulgebäude oder auf einem Schulgrundstück aufhalten, auch im Unterricht, verpflichtet, eine Mund-Nasen-Bedeckung zu tragen, soweit sich aus den Absätzen 4 bis 6 nichts anderes ergibt.

Nach § 1 Abs. 6 derselben Verordnung kann die Schulleiterin oder der Schulleiter entscheiden, dass das Tragen einer Mund-Nasen-Bedeckung im Einzelfall aus medizinischen Gründen oder auf Grund einer Beeinträchtigung ausgeschlossen ist.

Mein Kind kann aufgrund einer gesundheitlichen Beeinträchtigung keine Mund-Nasen-Bedeckung tragen."""
            )
            if options == Options.ATTEST:
                print_skip(
"""

Die Schulleiterin oder der Schulleiter ist kraft seines Amtes mangels medizinischer Schulung nicht dazu in der Lage, die Frage zu beurteilen, ob das Tragen einer Mund-Nasen-Bedeckung im Einzelfall aus medizinischen Gründen oder auf Grund einer Beeinträchtigung ausgeschlossen ist. Er kann die Regelung aus tatsächlichen Gründen nicht ausführen. Sie ist daher nichtig. Um Ihnen entgegenzukommen lege ich jedoch anliegendes Attest vor."""
                )
            else:
                print_skip(
"""

Die Schulleiterin oder der Schulleiter ist kraft seines Amtes mangels medizinischer Schulung nicht dazu in der Lage, die Frage zu beurteilen, ob das Tragen einer Mund-Nasen-Bedeckung im Einzelfall aus medizinischen Gründen oder auf Grund einer Beeinträchtigung ausgeschlossen ist. Er kann die Regelung aus tatsächlichen Gründen nicht ausführen. Sie ist daher nichtig. Von einer Glaubhaftmachung oder einem sonstigen Nachweis wird daher abgesehen."""
                )

        # Rheinland-Pfalz
        elif bundesland == "RLP":
            print_skip(
"""

Gemäß § 12 Abs. 1 Satz 2 der Zehnte Corona-Bekämpfungsverordnung Rheinland-Pfalz vom 19.Juni 2020 in Verbindung Hygieneplan-Corona für die Schulen in Rheinland-Pfalz in Verbindung mit dem Hygieneplan-Corona für die Schulen in Rheinland-Pfalz (4. überarbeitete Fassung, gültig ab 01.08.2020) wird nach Ziffer 1. unter dem 5. Bulletpoint das Tragen einer Mund-Nasen-Bedeckung in den Fluren, Gängen und Treppenhäusern, in der Aula, beim Einkauf am Schulkiosk sowie in der Mensa(dies gilt nicht am Platz), als persönliche Hygienemaßnahme bezeichnet.

Eine Pflicht zum Tragen einer Mund-Nasen-Bedeckung ist darin nicht bestimmt. 

Selbst, wenn eine solche Pflicht bestünde, so sieht § 1 Abs. 4 Nr. 2 der Zehnten Corona-Bekämpfungsverordnung Rheinland-Pfalz vom 19. Juni 2020 vor, dass diese nicht für Personen gilt, denen dies wegen einer Behinderung oder aus gesundheitlichen Gründen nicht möglich oder unzumutbar ist; dies sei durch ärztliche Bescheinigung nachzuweisen

Mein Kind kann aufgrund einer gesundheitlichen Beeinträchtigung keine Mund-Nasen-Bedeckung tragen."""
            )
            if options == Options.ATTEST:
                print_skip(
"""

Ein Erfordernis der Glaubhaftmachung hierzu besteht zwar nicht. Um Ihnen entgegenzukommen lege ich jedoch anliegendes Attest vor."""
                )
            else:
                print_skip(
"""

Der Zusatz der Pflicht zur Beibringung einer ärztlichen Bescheinigung entfaltet schon deshalb keine Wirksamkeit, weil der Vorlageadressat nicht in der Verordnung genannt ist. Von einem Nachweis wird daher abgesehen."""
                )

        # Saarland
        elif bundesland == "Saarland":
            print_skip(
"""

Gemäß § 1 Abs. 2 S. 1 der Verordnung zum Wiedereinstieg in den regulären Schulbetrieb und den Betrieb sonstiger Bildungseinrichtungen sowie zum Betrieb von Kindertageseinrichtungen, verkündet im Amtsblatt des Saarlandes Teil I vom 8. August 2020, sind ab dem Inkrafttreten nach Art 4 derselben Verordnung ab dem 15. August 2020 alle Schulen verpflichtet, die Vorgaben des „Musterhygieneplans Saarland zum Infektionsschutz in Schulen im Rahmen der Corona-Pandemiemaßnahmen“ vom 7. August 2020 in der jeweils geltenden Fassung (https://corona.saarland.de/DE/service/downloads/_documents/schule-elterninformationen/dld_hygienemassnahmen-schule-2020-07-03.html) einzuhalten.

Nach Punkt 3.4 des Musterhygieneplans Saarland zum Infektionsschutz in Schulen im Rahmen der Corona-Pandemiemaßnahmen vom 07.08.2020 ist das Tragen einer MNB ist während des Unterrichtsbetriebs im Schulgebäude, d.h. vom Betreten des Schulgebäudes bis zum Tisch im Klassen-oder Kursraum, sowie generell in den Fluren, Gängen, Treppenhäusern, im Sanitärbereich, beim Pausenverkauf sowie in der Mensa, im Verwaltungsbereich und Lehrerzimmer (jeweils nicht am Tisch!) verpflichtend, soweit dem keine medizinischen Gründe entgegenstehen.

Mein Kind kann aufgrund einer gesundheitlichen Beeinträchtigung keine Mund-Nasen-Bedeckung tragen."""
            )
            if options == Options.ATTEST:
                print_skip(
"""

Ein Erfordernis der Glaubhaftmachung hierzu besteht zwar nicht. Um Ihnen entgegenzukommen lege ich jedoch anliegendes Attest vor."""
                )
            else:
                print_skip(
"""

Ein Erfordernis der Glaubhaftmachung hierzu besteht rechtlich nicht. Von einer Glaubhaftmachung wird daher abgesehen."""
                )

        # Sachsen
        elif bundesland == "Sachsen":
            print_skip(
"""

Laut Allgemeinverfügung zur Regelung des Betriebs von Einrichtungen der Kindertagesbetreuung, von Schulen und Schulinternaten im Zusammenhang mit der Bekämpfung der SARS-CoV-2-Pandemie vom 13. August 2020 besteht nach Ziffer 3.3. für Schüler und Lehrkräfte keine „Maskentragungspflicht“. Es soll Ihnen lediglich durch Hinweisplakate oder regelmäßige „Belehrungen“ empfohlen werden, eine Mund- Nasen-Bedeckung zu tragen.

Diese Empfehlung wurde zur Kenntnis genommen. Gem. Art. 6 Abs. 2 GG sind Pflege und Erziehung der Kinder jedoch das natürliche Recht der Eltern und die zuvörderst ihnen obliegende Pflicht. Es wird daher gebeten, von weitergehenden "Belehrungen" Abstand zu nehmen."""
            )

        # Sachsen-Anhalt
        elif bundesland == "Sachsen-Anhalt":
            print_skip(
"""

Laut siebter SARS-CoV-2-Eindämmungsverordnung — 7. SARS-CoV-2-EindV vom 30. Juni 2020 i.V.m. dem Rahmenplan für die Hygienemaßnahmen, den Infektions- und Arbeitsschutz an Schulen im Land Sachsen-Anhalt während der Corona-Pandemie vom 18. August 2020 gilt eine Pflicht zum Tragen einer Mund-Nasen-Bedeckung außerhalb des eigentlichen Unterrichts.

Diese Pflicht gilt allerdings nicht für Personen, denen die Verwendung einer Mund-NasenBedeckung wegen einer Behinderung, einer Schwangerschaft oder aus gesundheitlichen Gründen nicht möglich oder unzumutbar ist; dies ist in geeigneter Weise (z. B. durch plausible mündliche Erklärung, Schwerbehindertenausweis, ärztliche Bescheinigung) glaubhaft zu machen. Zur Überwachung der Pflicht zur Mund-Nasen-Bedeckung eingesetzte Personen sind über die Ausnahmen in geeigneter Weise zu unterrichten."""
            )
            if options == Options.ATTEST:
                print_skip(
"""

Ich weise dies durch die Vorlage des anliegenden Attestes nach."""
                )
            else:
                if glaubhaftmachung:
                    print_skip(
"""

Ich biete der Schule an, zur Glaubhaftmachtung gesundheitlicher Beeiniträchtigungen meines Kindes beim Tragen einer Mund-Nasen-Bedeckung, eine eidesstattliche Versicherung abzugeben"""
                    )
                else:
                    print_skip(
"""

Der Nennung von gesundheitlichen Details ist aus datenschutzrechtlichen Gründen (vgl. Art. 9 DSGVO) nicht zur Glaubhaftmachung geeignet. Um Ihnen entgegenzukommen erkläre ich mich bereit, stattdessen eine eidesstattliche Versicherung darüber abzugeben, dass bei meinem Kind gesundheitliche Gründe dem Tragen einer Mund-Nasen-Bedeckung entgegenstehen."""
                    )

        # Schleswig-Holstein
        elif bundesland == "SH":
            print_skip(
"""

In der Landesverordnung zur Bekämpfung des Coronavirus SARS-CoV-2 (Corona-Bekämpfungsverordnung – Corona-BekämpfVO) vom 26. Juni 2020 ist keine Pflicht zum Tragen einer Mund-Nasen-Bedeckung normiert. Es gibt lediglich eine rechtlich nicht bindende "dringende Empfehlung" des Bildungsministeriums, in den ersten zwei Unterrichtswochen in der Schule eine Mund-Nasen-Bedeckung zu tragen. In keinem Fall dürfen Sie irgendwie Druck auf mein Kind ausüben, eine Mund-Nasen-Bedeckung zu tragen."""
            )

        # Thüringen
        elif bundesland == "Thüringen":
            print_skip(
"""

Nach § 19 Abs. 1 der Thüringer Verordnung über die Infektionsschutzregeln zur Eindämmung der Ausbreitung des Coronavirus SARS-CoV-2 in Kindertageseinrichtungen, Schulen und für den Sportbetrieb vom 12. Juni 2020 soll eine Mund-Nasen-Bedeckung nach § 6 Abs. 3 bis 5 ThürSARSCoV-2-IfS-GrundV0 in Situationen getragen werden, in denen das Mindestabstandsgebot nach § 1 Abs. 1 ThürSARS-CoV-2-IfS-GrundV0 nicht eingehalten werden kann, insbesondere bei Raumwechseln in den Pausen. In den Unterrichtsräumen oder bei Aufenthalt im Freien ist bei gewährleistetem Mindestabstand das Tragen einer Mund-Nasen-Bedeckung nicht erforderlich.

Nach § 6 Abs. 3 Nr. 2 der Thüringer Verordnung zur Neuordnung der erforderlichen Maßnahmen zur Eindämmung der Ausbreitung des Coronavirus SARS-CoV-2 sowie zur Verbesserung der infektionsschutzrechtlichen Handlungsmöglichkeiten vom 9. Juni 2020 gilt diese Pflicht nicht Personen, denen die Verwendung einer Mund-Nasen-Bedeckung wegen Behinderung oder aus gesundheitlichen oder anderen Gründen nicht möglich oder unzumutbar ist; dies ist in geeigneter Weise glaubhaft zu machen."""
            )
            if options == Options.ATTEST:
                print_skip(
"""

Ich weise dies durch die Vorlage des anliegenden Attestes nach."""
                )
            else:
                if glaubhaftmachung:
                    print_skip(
"""

Der Nennung von gesundheitlichen Details ist aus datenschutzrechtlichen Gründen (vgl. Art. 9 DSGVO) nicht zur Glaubhaftmachung geeignet. Um Ihnen entgegenzukommen erkläre ich mich bereit, stattdessen eine eidesstattliche Versicherung darüber abzugeben, dass bei meinem Kind gesundheitliche Gründe dem Tragen einer Mund-Nasen-Bedeckung entgegenstehen."""
                    )
                else:
                    print_skip(
"""

Der Zusatz der Pflicht zur Glaubhaftmachtung entfaltet schon deshalb keine Wirksamkeit, weil der Adressat der der Glaubhaftmachtung (derjenige, dem gegenüber die Glaubhaftmachtung zu erfolgen hat)  nicht genannt ist. Von einer Glaubhaftmachung wird daher abgesehen."""
                    )

        else:
            raise Exception(
                    "invalid Bundesland"
            )
    print_skip(
"""

Soweit für mein Kind von der Pflicht, eine Mund-Nasen-Bedeckung zu tragen nicht abgesehen wird, bitte ich um Übersendung eines Rechtsmittelfähigen Bescheides und werde sodann einstweiligen Rechtsschutz in Anspruch nehmen.

Dieses Schreiben habe ich mit Hilfe des Teams von KlagePaten.eu erstellt."""
        )

def print_skip( s ):
    lines = s.split('\n')
    if skip and len( lines ) > 3:
        print( lines[0] + '\n...\n' + lines[-1], end='')
    else:
        print( '\n'.join(lines), end='')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument(
            '-s', '--skip',
            action='store_true',
            default=False,
            help=''
    )
    parser.add_argument(
            '-o', '--opt',
            type=int,
            required=True,
            help='1: attest, 2: no attest, 3: list'
    )
    parser.add_argument(
            '-g', '--glaubhaftmachung',
            action='store_true',
            default=False,
            help='glaubhaftmachung'
    )
    parser.add_argument(
            'bundesland',
            help=''
    )
    args = parser.parse_args()

    if args.opt == 1:
        options = Options.ATTEST
    elif args.opt == 2:
        options = Options.NO_ATTEST
    else:
        print( f"opt: {args.opt}" )
        options = Options.LIST
    if args.skip:
        skip=True
    print( f"options: {options}" )
    print( f"glaubhaftmachung: {args.glaubhaftmachung}" )
    print( f"DOCUMENT:" )
    print( f"-------------------------------" )

    main(
            options = options,
            glaubhaftmachung = args.glaubhaftmachung,
            bundesland = args.bundesland
    )
