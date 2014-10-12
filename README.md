# BVG Verkehrsmeldungen

Bereitet die [Verkehrsmeldungen der BVG](http://www.bvg.de/de/Fahrinfo/Verkehrsmeldungen) als JSON-API auf.

## Beispiel

    ./app/bvg.py

```json
{
    "issue_count": 62, 
    "issues": [
        {
            "what": {
                "line": "U2", 
                "medium": "U-Bahn"
            }, 
            "when": {
                "begin": "2014-08-25T21:00:00", 
                "end": "2014-12-12T03:30:00"
            }, 
            "why": {
                "url": "http://www.bvg.de/de/Fahrinfo/Verkehrsmeldungen/de/Fahrinfo/Verkehrsmeldungen/Verkehrsmeldung-Detail?id=1900", 
                "reason": "Sperrung wegen Bauarbeiten der BVG"
            }, 
            "details": {
                "barrierfree": "Der Ersatzverkehr wird mit barrierefreien Fahrzeugen bedient und h\u00e4lt an den ausgewiesenen Ersatzhaltestellen. Bitte planen Sie eine l\u00e4ngere Fahrzeit ein und beachten Sie, dass eine Fahrradmitnahme in den Bussen nicht m\u00f6glich ist.", 
                "direction": "Beide", 
                "description": "Die Linie ist jeweils von Sonntag bis Donnerstag ab 21:00Uhr bis Betriebsschlu\u00df zwischen U Wittenbergplatz und U Bismarckstr. unterbrochen. In diesem Bereich besteht Ersatzverkehr mit Bussen. Am 2. und 3. Oktober verkehrt die Linie durchgehend."
            }, 
            "where": {
                "start": "U Wittenbergplatz", 
                "end": "U Bismarckstr."
            }, 
            "id": 1900
        }, 
        {
            "what": {
                "line": "U2", 
                "medium": "U-Bahn"
            }, 
            "when": {
                "begin": "2014-08-25T21:00:00", 
                "end": "2014-12-12T03:30:00"
            }, 
            "why": {
                "url": "http://www.bvg.de/de/Fahrinfo/Verkehrsmeldungen/de/Fahrinfo/Verkehrsmeldungen/Verkehrsmeldung-Detail?id=2025", 
                "reason": "Zusatzinformation: Haltestellen des Ersatzverkehrs"
            }, 
            "details": {
                "barrierfree": "Ja", 
                "url": "http://www.bvg.de/de/Fahrinfo/Verkehrsmeldungen/images/content/stoerungsmeldungen/U2_Ersatzhaltestellen_WittenberplatzBismarkstr.pdf", 
                "direction": "Beide", 
                "description": "W\u00e4hrend der Ma\u00dfnahme besteht Ersatzverkehr mit barrierefreien Bussen. Die Lage der Ersatzhaltestellen finden Sie in der PDF-Datei."
            }, 
            "where": {
                "start": "U Wittenbergplatz", 
                "end": "U Bismarckstra\u00dfe"
            }, 
            "id": 2025
        }, 
        {
            "what": {
                "line": "M4", 
                "medium": "MetroTram"
            }, 
            "when": {
                "begin": "2014-07-25T09:45:00", 
                "end": "2014-12-31T23:59:00"
            }, 
            "why": {
                "url": "http://www.bvg.de/de/Fahrinfo/Verkehrsmeldungen/de/Fahrinfo/Verkehrsmeldungen/Verkehrsmeldung-Detail?id=1789", 
                "reason": "Haltestellenverlegung am S Greifswalder Stra\u00dfe"
            }, 
            "details": {
                "barrierfree": "25.07.2014 09:45", 
                "direction": "beide", 
                "description": "Provisorische Haltestelle am S Greifswalder Stra\u00dfe wegen Bauma\u00dfnahmen der Berliner Wasserbetriebe voraussichtlich bis Ende des Jahres.Die Haltestellenzug\u00e4nge an den Treppen der Fu\u00dfg\u00e4ngerunterf\u00fchrung sowie in H\u00f6he der Kreuzung Greifswalder Stra\u00dfe/Grellstra\u00dfe sind gesperrt. Ersatzweise ist s\u00fcdwestlich der Bahnbr\u00fccke ein ampelgeregelter, provisorischer Fu\u00dfg\u00e4nger\u00fcbergang \u00fcber beide Richtungsfahrbahnen der Greifswalder Stra\u00dfe, einschlie\u00dflich eines Gleis\u00fcbergangs, in Betrieb genommen worden. Ein zweiter Zugang zu den Haltestellen befindet sich am \u00dcbergang Lilli-Hennoch-Stra\u00dfe."
            }, 
            "where": {
                "start": "S Greifswalder Stra\u00dfe", 
                "end": "S Greifswalder Stra\u00dfe"
            }, 
            "id": 1789
        }, 
        {
            "what": {
                "line": "M5", 
                "medium": "MetroTram"
            }, 
            "when": {
                "begin": "2014-09-22T04:00:00", 
                "end": null
            }, 
            "why": {
                "url": "http://www.bvg.de/de/Fahrinfo/Verkehrsmeldungen/de/Fahrinfo/Verkehrsmeldungen/Verkehrsmeldung-Detail?id=2702", 
                "reason": "Sperrung wegen Bauarbeiten der BVG"
            }, 
            "details": {
                "barrierfree": "22.09.2014 04:00", 
                "direction": "Beide", 
                "description": "Wegen Umbau- und Sanierungsarbeiten m\u00fcssen die Haltestellen bis auf weiteres verlegt werden. Die Ersatzhaltestellen befinden sich stadteinw\u00e4rts vor bzw. stadtausw\u00e4rts hinter der Kreuzung Landsberger Allee/ Storkower Stra\u00dfe."
            }, 
            "where": {
                "start": "S Landsberger Allee", 
                "end": "S Landsberger Allee"
            }, 
            "id": 2702
        }, 
        {
            "what": {
                "line": "M6", 
                "medium": "MetroTram"
            }, 
            "when": {
                "begin": "2014-09-22T04:00:00", 
                "end": null
            }, 
            "why": {
                "url": "http://www.bvg.de/de/Fahrinfo/Verkehrsmeldungen/de/Fahrinfo/Verkehrsmeldungen/Verkehrsmeldung-Detail?id=2704", 
                "reason": "Sperrung wegen Bauarbeiten der BVG"
            }, 
            "details": {
                "barrierfree": "22.09.2014 04:00", 
                "direction": "Beide", 
                "description": "Wegen Umbau- und Sanierungsarbeiten m\u00fcssen die Haltestellen bis auf weiteres verlegt werden. Die Ersatzhaltestellen befinden sich stadteinw\u00e4rts vor bzw. stadtausw\u00e4rts hinter der Kreuzung Landsberger Allee/ Storkower Stra\u00dfe."
            }, 
            "where": {
                "start": "S Landsberger Allee", 
                "end": "S Landsberger Allee"
            }, 
            "id": 2704
        }, 
        {
            "what": {
                "line": "M8", 
                "medium": "MetroTram"
            }, 
            "when": {
                "begin": "2014-09-22T04:00:00", 
                "end": null
            }, 
            "why": {
                "url": "http://www.bvg.de/de/Fahrinfo/Verkehrsmeldungen/de/Fahrinfo/Verkehrsmeldungen/Verkehrsmeldung-Detail?id=2700", 
                "reason": "Sperrung wegen Bauarbeiten der BVG"
            }, 
            "details": {
                "barrierfree": "22.09.2014 04:00", 
                "direction": "Beide", 
                "description": "Wegen Umbau- und Sanierungsarbeiten m\u00fcssen die Haltestellen bis auf weiteres verlegt werden. Die Ersatzhaltestellen befinden sich stadteinw\u00e4rts vor bzw. stadtausw\u00e4rts hinter der Kreuzung Landsberger Allee/ Storkower Stra\u00dfe."
            }, 
            "where": {
                "start": "S Landsberger Allee", 
                "end": "S Landsberger Allee"
            }, 
            "id": 2700
        }, 
        {
            "what": {
                "line": "M41", 
                "medium": "MetroBus"
            }, 
            "when": {
                "begin": "2014-05-22T07:30:00", 
                "end": null
            }, 
            "why": {
                "url": "http://www.bvg.de/de/Fahrinfo/Verkehrsmeldungen/de/Fahrinfo/Verkehrsmeldungen/Verkehrsmeldung-Detail?id=1572", 
                "reason": "Sperrung wegen Bauarbeiten der Wasserbetriebe"
            }, 
            "details": {
                "barrierfree": "22.05.2014 07:30", 
                "direction": "SONNENALLEE/ BAUMSCHULENSTR.", 
                "description": "Auf Grund von Bauarbeiten ist die Haltestelle Schulenburgpark in Fahrtrichtung Sonnenallee / Baumschulenstr. bis auf weiteres zur Sonnenallee hinter Jupiterstr. verlegt."
            }, 
            "where": {
                "start": "S K\u00f6llnische Heide", 
                "end": "Michael-Bohnen-Ring"
            }, 
            "id": 1572
        }, 
        {
            "what": {
                "line": "M45", 
                "medium": "MetroBus"
            }, 
            "when": {
                "begin": "2014-10-12T09:00:00", 
                "end": "2014-10-12T15:00:00"
            }, 
            "why": {
                "url": "http://www.bvg.de/de/Fahrinfo/Verkehrsmeldungen/de/Fahrinfo/Verkehrsmeldungen/Verkehrsmeldung-Detail?id=2968", 
                "reason": "Sperrung wegen Veranstaltung"
            }, 
            "details": {
                "barrierfree": "12.10.2014 09:00", 
                "direction": "Beide", 
                "description": "Die Linie muss in beiden Fahrtrichtungen \u00fcber Sophie-Charlotten-Str., Kaiserdamm, Bismarckstr. und Kaiser-Friedrich-Str. umgeleitet werden, bzw. verkehrt in beiden Fahrtrichtungen je nach Verlauf der Veranstaltung nur zwischen Johannesstift und S Westend und wird vom Spandauer Damm \u00fcber Sophie-Charlotten-Str. und Mollwitzstr. zum Heubnerweg umgeleitet und endet hier."
            }, 
            "where": {
                "start": "S Westend", 
                "end": "S+U Zoologischer Garten"
            }, 
            "id": 2968
        }, 
        {
            "what": {
                "line": "M46", 
                "medium": "MetroBus"
            }, 
            "when": {
                "begin": "2014-10-12T09:00:00", 
                "end": "2014-10-12T15:00:00"
            }, 
            "why": {
                "url": "http://www.bvg.de/de/Fahrinfo/Verkehrsmeldungen/de/Fahrinfo/Verkehrsmeldungen/Verkehrsmeldung-Detail?id=2966", 
                "reason": "Sperrung wegen Veranstaltung"
            }, 
            "details": {
                "barrierfree": "12.10.2014 09:00", 
                "direction": "Beide", 
                "description": "Die Linie verkehrt in beiden Fahrtrichtungen nur zwischen Britz-S\u00fcd und U Kurf\u00fcrstendamm und wird vom Kurf\u00fcrstendamm kommend \u00fcber Joachimstaler Str. und Bundesallee zum U Spichernstr. umgeleitet und endet hier. Die Haltestellen zwischen U Kurf\u00fcrstendamm und S+U Zoologischer Garten werden nicht bedient. Zum S+U Zoologischer Garten nutzen Sie bitte die U9 ab U Kurf\u00fcrstendamm bzw. U Spichernstr."
            }, 
            "where": {
                "start": "Europa-Center", 
                "end": "S+U Zoologischer Garten"
            }, 
            "id": 2966
        }, 
        {
            "what": {
                "line": "M49", 
                "medium": "MetroBus"
            }, 
            "when": {
                "begin": "2014-10-12T09:00:00", 
                "end": "2014-10-12T15:00:00"
            }, 
            "why": {
                "url": "http://www.bvg.de/de/Fahrinfo/Verkehrsmeldungen/de/Fahrinfo/Verkehrsmeldungen/Verkehrsmeldung-Detail?id=2988", 
                "reason": "Sperrung wegen Veranstaltung"
            }, 
            "details": {
                "barrierfree": "12.10.2014 09:00", 
                "direction": "Beide", 
                "description": "Die Linie verkehrt in beiden Fahrtrichtungen nur zwischen Nennhauser Damm und Haus des Rundfunks und endet hier. Die Haltestellen zwischen U Theodor-Heuss-Platz und S+U Zoologischer Garten werden nicht bedient. Zum S+U Zoologischer Garten nutzen Sie bitte die U2 ab U Theodor-Heuss-Platz."
            }, 
            "where": {
                "start": "U Theodor-Heuss-Platz", 
                "end": "S+U Zoologischer Garten"
            }, 
            "id": 2988
        }, 
        {
            "what": {
                "line": "TXL", 
                "medium": "Bus"
            }, 
            "when": {
                "begin": "2012-10-15T05:00:00", 
                "end": null
            }, 
            "why": {
                "url": "http://www.bvg.de/de/Fahrinfo/Verkehrsmeldungen/de/Fahrinfo/Verkehrsmeldungen/Verkehrsmeldung-Detail?id=1612", 
                "reason": "Sperrung wegen Bauarbeiten"
            }, 
            "details": {
                "barrierfree": "15.10.2012 05:00", 
                "direction": "Beide", 
                "description": "Die Linie muss in beiden Fahrtrichtungen vom Kapelle-Ufer \u00fcber Rahel-Hirsch-Str. nach Alt-Moabit umgeleitet werden. Die Haltestellen Washingtonplatz/Hauptbahnhof und S+U Hauptbahnhof werden nicht bedient. Daf\u00fcr werden in der Rahel-Hirsch-Str. hinter Friedrich-List-Ufer (Richtung Flughafen Tegel) bzw. gg\u00fc. Friedrich-List-Ufer (Fahrtrichtung S+U Alexanderplatz) Ersatzhaltestellen eingerichtet."
            }, 
            "where": {
                "start": "Karlplatz", 
                "end": "Kleiner Tiergarten"
            }, 
            "id": 1612
        }, 
        {
            "what": {
                "line": "100", 
                "medium": "Bus"
            }, 
            "when": {
                "begin": "2014-09-09T10:00:00", 
                "end": null
            }, 
            "why": {
                "url": "http://www.bvg.de/de/Fahrinfo/Verkehrsmeldungen/de/Fahrinfo/Verkehrsmeldungen/Verkehrsmeldung-Detail?id=2238", 
                "reason": "Sperrung wegen Bauarbeiten der Wasserbetriebe"
            }, 
            "details": {
                "barrierfree": "09.09.2014 10:00", 
                "direction": "Beide", 
                "description": "Die Linie muss  von der Scheidemannstr. kommend \u00fcber Yitzhak-Rabin-Str. und Stra\u00dfe des 17. Juni bzw. entgegengesetzt umgeleitet werden. Auf dem Umleitungsweg sind Yitzhak-Rabin-Rabin-Str. hinter Scheidemannstr., Stra\u00dfe des 17. Juni vor Kleiner Stern und Gro\u00dfer Stern vor Hofj\u00e4gerallee Ersatzhaltestellen eingerichtet. Die Haltestelle Schloss Bellevue ist ersatzlos aufgehoben."
            }, 
            "where": {
                "start": "Platz der Republik", 
                "end": "Gro\u00dfer Stern"
            }, 
            "id": 2238
        }, 
        {
            "what": {
                "line": "100", 
                "medium": "Bus"
            }, 
            "when": {
                "begin": "2014-10-12T09:00:00", 
                "end": "2014-10-12T15:00:00"
            }, 
            "why": {
                "url": "http://www.bvg.de/de/Fahrinfo/Verkehrsmeldungen/de/Fahrinfo/Verkehrsmeldungen/Verkehrsmeldung-Detail?id=2976", 
                "reason": "Sperrung wegen Veranstaltung"
            }, 
            "details": {
                "barrierfree": "12.10.2014 09:00", 
                "direction": "Beide", 
                "description": "Die Linie verkehrt nur zwischen S+U Alexanderplatz und Reichstag/Bundestag. Die Haltestellen zwischen Reichstag/Bundestag und S+U Zoologischer Garten werden nicht bedient. Zum S+U Zoologischer Garten nutzen Sie bitte die U2 ab S+U Potsdamer Platz."
            }, 
            "where": {
                "start": "Reichstag/Bundestag", 
                "end": "S+U Zoologischer Garten"
            }, 
            "id": 2976
        }, 
        {
            "what": {
                "line": "200", 
                "medium": "Bus"
            }, 
            "when": {
                "begin": "2014-10-12T09:00:00", 
                "end": "2014-10-12T15:00:00"
            }, 
            "why": {
                "url": "http://www.bvg.de/de/Fahrinfo/Verkehrsmeldungen/de/Fahrinfo/Verkehrsmeldungen/Verkehrsmeldung-Detail?id=2984", 
                "reason": "Sperrung wegen Veranstaltung"
            }, 
            "details": {
                "barrierfree": "12.10.2014 09:00", 
                "direction": "Beide", 
                "description": "Die Linie verkehrt in beiden Fahrtrichtungen nur zwische Michelangelostr. und Philharmonie. Die Haltestellen zwischen Philharmonie und S+U Zoologischer Garten werden nicht bedient. Zum S+U Zoologischer Garten nutzen Sie bitte die U2 ab S+U Potsdamer Platz."
            }, 
            "where": {
                "start": "Philharmonie", 
                "end": "S+U Zoologischer Garten"
            }, 
            "id": 2984
        }, 
        {
            "what": {
                "line": "X9", 
                "medium": "Express-Bus"
            }, 
            "when": {
                "begin": "2014-10-12T09:00:00", 
                "end": "2014-10-12T15:00:00"
            }, 
            "why": {
                "url": "http://www.bvg.de/de/Fahrinfo/Verkehrsmeldungen/de/Fahrinfo/Verkehrsmeldungen/Verkehrsmeldung-Detail?id=2964", 
                "reason": "Sperrung wegen Veranstaltung"
            }, 
            "details": {
                "barrierfree": "12.10.2014 09:00", 
                "direction": "Beide", 
                "description": "Die Linie verkehrt in beiden Fahrtrichtungen nur zwischen Flughafen Tegel und S+U Jungfernheide und endet hier. Die Abfahrt in Fahrtrichtung Flughafen Tegel erfolgt von der Max-Dorn-Str. \u00fcber Lise-Meitner-Str. und Olbersstr. zum Tegeler Weg."
            }, 
            "where": {
                "start": "S+U Jungfernheide", 
                "end": "S+U Zoologischer Garten"
            }, 
            "id": 2964
        }, 
        {
            "what": {
                "line": "X10", 
                "medium": "Express-Bus"
            }, 
            "when": {
                "begin": "2013-09-30T04:30:00", 
                "end": null
            }, 
            "why": {
                "url": "http://www.bvg.de/de/Fahrinfo/Verkehrsmeldungen/de/Fahrinfo/Verkehrsmeldungen/Verkehrsmeldung-Detail?id=1558", 
                "reason": "Sperrung wegen Bauarbeiten"
            }, 
            "details": {
                "barrierfree": "30.09.2013 04:30", 
                "direction": "S TELTOW STADT", 
                "description": "Von den Bauarbeiten betroffen sind nur die Teilfahrten der Linie in Fahrtrichtung Rammrathbr\u00fccke. Hier erfolgt die Umleitung ab Kreisverkehr Zehlendorfer Stra\u00dfe \u00fcber Zeppelinufer, Jahnstra\u00dfe, Oderstra\u00dfe und Katzbachstra\u00dfe zur Potsdamer Stra\u00dfe. Die Haltestellen in Teltow, Ruhlsdorfer Platz, Jahnstra\u00dfe und Striewitzweg werden bauzeitlich nicht bedient. Die R\u00fcckfahrt in Richtung Hertzallee, sowie die Teilfahrten in Richtung S Teltow Stadt sind von der Umleitung nicht betroffen und werden planm\u00e4\u00dfig durchgef\u00fchrt."
            }, 
            "where": {
                "start": "Alt-Sch\u00f6now", 
                "end": "Alt-Sch\u00f6now"
            }, 
            "id": 1558
        }, 
        {
            "what": {
                "line": "X10", 
                "medium": "Express-Bus"
            }, 
            "when": {
                "begin": "2014-10-12T09:00:00", 
                "end": "2014-10-12T15:00:00"
            }, 
            "why": {
                "url": "http://www.bvg.de/de/Fahrinfo/Verkehrsmeldungen/de/Fahrinfo/Verkehrsmeldungen/Verkehrsmeldung-Detail?id=2972", 
                "reason": "Sperrung wegen Veranstaltung"
            }, 
            "details": {
                "barrierfree": "12.10.2014 09:00", 
                "direction": "Beide", 
                "description": "Die Linie verkehrt in beiden Fahrtrichtungen nur zwischen Zehlendorf und U Adenauerplatz und wird zum U Wilmersdorfer Str. umgeleitet und endet hier. Die Abfahrt in Richtung Zehlendorf erfolgt von der Haltestelle U Adenauerplatz. Die Haltestellen zwischen U Adenauerplatz und S+U Zoologischer Garten werden nicht bedient."
            }, 
            "where": {
                "start": "U Adenauerplatz", 
                "end": "S+U Zoologischer Garten"
            }, 
            "id": 2972
        }, 
        {
            "what": {
                "line": "X11", 
                "medium": "Express-Bus"
            }, 
            "when": {
                "begin": "2014-04-07T10:00:00", 
                "end": "2014-10-17T13:00:00"
            }, 
            "why": {
                "url": "http://www.bvg.de/de/Fahrinfo/Verkehrsmeldungen/de/Fahrinfo/Verkehrsmeldungen/Verkehrsmeldung-Detail?id=1554", 
                "reason": "Sperrung wegen Bauarbeiten"
            }, 
            "details": {
                "barrierfree": "07.04.2014 10:00", 
                "direction": "Beide", 
                "description": "Die Linie muss in beiden Fahrtrichtungen von der Johannisthaler Chaussee  kommend \u00fcber Rudower Str., Neuk\u00f6llner Str., Flurweg, Petunienweg zur Johannisthaler Chaussee umgeleitet werden. Die Haltestelle Birkhuhnweg wird nicht bedient, ein Ersatzhalt im Petunienweg ist gegeben."
            }, 
            "where": {
                "start": "Johannisthaler Ch./Rudower Str.", 
                "end": "Stelzenweg"
            }, 
            "id": 1554
        }, 
        {
            "what": {
                "line": "X34", 
                "medium": "Express-Bus"
            }, 
            "when": {
                "begin": "2014-10-12T09:00:00", 
                "end": "2014-10-12T15:00:00"
            }, 
            "why": {
                "url": "http://www.bvg.de/de/Fahrinfo/Verkehrsmeldungen/de/Fahrinfo/Verkehrsmeldungen/Verkehrsmeldung-Detail?id=2980", 
                "reason": "Sperrung wegen Veranstaltung"
            }, 
            "details": {
                "barrierfree": "12.10.2014 09:00", 
                "direction": "Beide", 
                "description": "Die Linie verkehrt in beiden Fahrtrichtungen nur zwischen Kladow, Kaserne Hottengrund und S Messe Nord/ICC und endet hier. Die Haltestellen zwischen S Messe Nord/ICC und S+U Zoologischer Garten werden nicht bedient. Zum S+U Zoologischer Garten nutzen Sie bitte die U2 ab U Theodor-Heuss-Platz."
            }, 
            "where": {
                "start": "S Messe Nord/ICC", 
                "end": "S+U Zoologischer Garten"
            }, 
            "id": 2980
        }, 
        {
            "what": {
                "line": "X54", 
                "medium": "Express-Bus"
            }, 
            "when": {
                "begin": "2014-07-25T08:30:00", 
                "end": null
            }, 
            "why": {
                "url": "http://www.bvg.de/de/Fahrinfo/Verkehrsmeldungen/de/Fahrinfo/Verkehrsmeldungen/Verkehrsmeldung-Detail?id=1530", 
                "reason": "Sperrung wegen Bauarbeiten"
            }, 
            "details": {
                "barrierfree": "25.07.2014 08:30", 
                "direction": "S+U PANKOW", 
                "description": "Diese Linie wird von der Riesaer Stra\u00dfe kommend \u00fcber Hellersdorfer Stra\u00dfe, Alte Hellersdorfer Stra\u00dfe, Gothaer Str., Eisenacher Stra\u00dfe und Blumberger Damm zur Landsberger Allee umgeleitet. Die Haltestellen zwischen U Hellersdorf und Blumberger Damm/ Landsberger Allee werden bauzeitlich in Richtung Pankow nicht bedient. Bitte benutzen Sie ab Blumberger Damm/ Landsberger Allee die Linie X54 in Gegenrichtung."
            }, 
            "where": {
                "start": "U Hellersdorf", 
                "end": "Landsberger Allee/Blumberger D."
            }, 
            "id": 1530
        }, 
        {
            "what": {
                "line": "12", 
                "medium": "Stra\u00dfenbahn"
            }, 
            "when": {
                "begin": "2012-08-05T04:00:00", 
                "end": null
            }, 
            "why": {
                "url": "http://www.bvg.de/de/Fahrinfo/Verkehrsmeldungen/de/Fahrinfo/Verkehrsmeldungen/Verkehrsmeldung-Detail?id=1542", 
                "reason": "Linienma\u00dfnahmen"
            }, 
            "details": {
                "barrierfree": "05.08.2012 04:00", 
                "direction": "Beide", 
                "description": "Die Linie verkehrt ab Zionskirchplatz in ver\u00e4nderter Linienf\u00fchrung \u00fcber Weinbergsweg - Rosenthaler Platz - Hackescher Markt - Oranienburger Str. - Friedrichstr. zur Endhaltestelle Am Kupfergraben."
            }, 
            "where": {
                "start": "U Oranienburger Tor", 
                "end": "Zionskirchplatz"
            }, 
            "id": 1542
        }, 
        {
            "what": {
                "line": "21", 
                "medium": "Stra\u00dfenbahn"
            }, 
            "when": {
                "begin": "2014-07-14T04:00:00", 
                "end": "2014-10-18T04:00:00"
            }, 
            "why": {
                "url": "http://www.bvg.de/de/Fahrinfo/Verkehrsmeldungen/de/Fahrinfo/Verkehrsmeldungen/Verkehrsmeldung-Detail?id=1614", 
                "reason": "Sperrung wegen Bauarbeiten der DB"
            }, 
            "details": {
                "barrierfree": "14.07.2014 04:00", 
                "direction": "Beide", 
                "description": "Auf Grund von Br\u00fcckenbauarbeiten der Deutschen Bahn ist die Linie zwischen S Rummelsburg und Marktstr. unterbrochen. Eine Verbindung zwischen diesen Haltestellen ist nur fu\u00dfl\u00e4ufig (ca. 250 Meter) m\u00f6glich."
            }, 
            "where": {
                "start": "S Rummelsburg", 
                "end": "Marktstr."
            }, 
            "id": 1614
        }, 
        {
            "what": {
                "line": "61", 
                "medium": "Stra\u00dfenbahn"
            }, 
            "when": {
                "begin": "2014-10-06T10:00:00", 
                "end": "2014-11-03T02:00:00"
            }, 
            "why": {
                "url": "http://www.bvg.de/de/Fahrinfo/Verkehrsmeldungen/de/Fahrinfo/Verkehrsmeldungen/Verkehrsmeldung-Detail?id=2828", 
                "reason": "Sperrung wegen Bauarbeiten der BVG"
            }, 
            "details": {
                "barrierfree": "Der Ersatzverkehr h\u00e4lt, soweit m\u00f6glich, an den bzw. in H\u00f6he der Stra\u00dfenbahnhaltestellen und wird mit barrierefreien Fahrzeugen bedient. Bitte planen Sie eine l\u00e4ngere Fahrzeit ein und beachten Sie, dass eine Fahrradmitnahme in den Bussen nicht m\u00f6glich ist.", 
                "direction": "Beide", 
                "description": "Die Linie verkehrt nur zwischen Karl-Ziegler-Str. und Hirschgarten und verkehrt weiter im Linienverlauf der Linie 60 bis Altes Wasserwerk. Ein Ersatzverkehr mit Bussen ist eingerichtet."
            }, 
            "where": {
                "start": "Hirschgarten", 
                "end": "Rahnsdorf/Waldsch\u00e4nke"
            }, 
            "id": 2828
        }, 
        {
            "what": {
                "line": "62", 
                "medium": "Stra\u00dfenbahn"
            }, 
            "when": {
                "begin": "2014-10-11T07:50:00", 
                "end": "2014-10-12T15:50:00"
            }, 
            "why": {
                "url": "http://www.bvg.de/de/Fahrinfo/Verkehrsmeldungen/de/Fahrinfo/Verkehrsmeldungen/Verkehrsmeldung-Detail?id=2922", 
                "reason": "Sperrung wegen Bauarbeiten der BVG"
            }, 
            "details": {
                "barrierfree": "Der Ersatzverkehr h\u00e4lt, soweit m\u00f6glich, an den bzw. in H\u00f6he der Stra\u00dfenbahnhaltestellen und wird mit barrierefreien Fahrzeugen bedient. Bitte planen Sie eine l\u00e4ngere Fahrzeit ein und beachten Sie, dass eine Fahrradmitnahme in den Bussen nicht m\u00f6glich ist.", 
                "direction": "Beide", 
                "description": "Auf Grund von Fahrleitungsarbeiten ist die Linie zwischen Bahnhofstr./Lindenstr. und M\u00fcggelheimer Str./Wendenschlo\u00dfstr. jeweils am 11.10.2014 in der Zeit zwischen ca. 7:50 Uhr und ca. 19:50 Uhr und am 12.10.2014 in der Zeit zwischen ca. 7:50 Uhr und ca. 15:50 unterbrochen. Im s\u00fcdlichen Linienabschnitt verkehrt die Linie zwischen Wendenschlo\u00df und Krankenhaus K\u00f6penick/S\u00fcdseite. Zwischen Bahnhofstr./Lindenstr. und M\u00fcggelheimer Str./Wendenschlo\u00dfstr. ist ein Ersatzverkehr mit Bussen eingerichtet."
            }, 
            "where": {
                "start": "Bahnhofstr./Lindenstr.", 
                "end": "M\u00fcggelhm.Str./Wendenschlo\u00dfstr."
            }, 
            "id": 2922
        }, 
        {
            "what": {
                "line": "67", 
                "medium": "Stra\u00dfenbahn"
            }, 
            "when": {
                "begin": "2014-10-11T07:50:00", 
                "end": "2014-10-12T15:50:00"
            }, 
            "why": {
                "url": "http://www.bvg.de/de/Fahrinfo/Verkehrsmeldungen/de/Fahrinfo/Verkehrsmeldungen/Verkehrsmeldung-Detail?id=2920", 
                "reason": "Sperrung wegen Bauarbeiten der BVG"
            }, 
            "details": {
                "barrierfree": "Der Ersatzverkehr h\u00e4lt, soweit m\u00f6glich, an den bzw. in H\u00f6he der Stra\u00dfenbahnhaltestellen und wird mit barrierefreien Fahrzeugen bedient. Bitte planen Sie eine l\u00e4ngere Fahrzeit ein und beachten Sie, dass eine Fahrradmitnahme in den Bussen nicht m\u00f6glich ist.", 
                "direction": "Beide", 
                "description": "Auf Grund von Fahrleitungsarbeiten ist die Linie zwischen Bahnhofstr./Lindenstr. und Krankenhaus K\u00f6penick/S\u00fcdseite jeweils am 11.10.2014 in der Zeit zwischen ca. 7:50 Uhr und ca. 19:50 Uhr und am 12.10.2014 in der Zeit zwischen ca. 7:50 Uhr und ca. 15:50 unterbrochen. Ein Ersatzverkehr mit Bussen ist eingerichtet."
            }, 
            "where": {
                "start": "Bahnhofstr./Lindenstr.", 
                "end": "Krkhs. K\u00f6penick/S\u00fcdseite"
            }, 
            "id": 2920
        }, 
        {
            "what": {
                "line": "101", 
                "medium": "Bus"
            }, 
            "when": {
                "begin": "2014-10-12T09:00:00", 
                "end": "2014-10-12T15:00:00"
            }, 
            "why": {
                "url": "http://www.bvg.de/de/Fahrinfo/Verkehrsmeldungen/de/Fahrinfo/Verkehrsmeldungen/Verkehrsmeldung-Detail?id=2978", 
                "reason": "Sperrung wegen Veranstaltung"
            }, 
            "details": {
                "barrierfree": "12.10.2014 09:00", 
                "direction": "Beide", 
                "description": "Die Linie verkehrt im n\u00f6rdlichen Linienabschnitt nur zwischen U Turmstr. und Helmholtzstr. und wird \u00fcber Dovebr\u00fccke, Einsteinufer, Marchstr., Ernst-Reuter-Platz zur Otto-Suhr-Alle umgeleitet und endet hier. Im s\u00fcdlichen Linienabschnitt verkehrt die Linie nur zwischen Sachtlebenstr. und  U Konstanzer Str. und wird \u00fcber Brandenburgische Str. und Kurf\u00fcrstendamm zum Olivaer Platz umgeleitet und endet hier. Die Haltestellen zwischen Helmholtzstr. und U Konstanzer Str. werden nicht bedient."
            }, 
            "where": {
                "start": "Helmholtzstr.", 
                "end": "U Konstanzer Str."
            }, 
            "id": 2978
        }, 
        {
            "what": {
                "line": "106", 
                "medium": "Bus"
            }, 
            "when": {
                "begin": "2014-10-12T09:00:00", 
                "end": "2014-10-12T15:00:00"
            }, 
            "why": {
                "url": "http://www.bvg.de/de/Fahrinfo/Verkehrsmeldungen/de/Fahrinfo/Verkehrsmeldungen/Verkehrsmeldung-Detail?id=2986", 
                "reason": "Sperrung wegen Veranstaltung"
            }, 
            "details": {
                "barrierfree": "12.10.2014 09:00", 
                "direction": "Beide", 
                "description": "Die Linie muss in Fahrtrichtung Lindenhof \u00fcber Bartningallee, Kirchstr., Alt-Moabit, Invalidenstr., Tiergartentunnel und Tiergartenstr. zur Klingelh\u00f6ferstr. umgeleitet werden. Die Haltestellen zwischen U Hansaplatz und Nord. Botschaften/Adenauer Stiftg. werden nicht bedient. Auf dem Umleitungsweg wird nur die Haltestelle Lehrter Str./Invalidenstr. (zum S+U Hauptbahnhof) bedient."
            }, 
            "where": {
                "start": "U Hansaplatz", 
                "end": "Nord.Botschaften/Adenauer-Stiftg"
            }, 
            "id": 2986
        }, 
        {
            "what": {
                "line": "109", 
                "medium": "Bus"
            }, 
            "when": {
                "begin": "2014-10-12T09:00:00", 
                "end": "2014-10-12T15:00:00"
            }, 
            "why": {
                "url": "http://www.bvg.de/de/Fahrinfo/Verkehrsmeldungen/de/Fahrinfo/Verkehrsmeldungen/Verkehrsmeldung-Detail?id=2982", 
                "reason": "Sperrung wegen Veranstaltung"
            }, 
            "details": {
                "barrierfree": "12.10.2014 09:00", 
                "direction": "Beide", 
                "description": "Die Linie muss in beiden Fahrtrichtungen \u00fcber Hardenbergstr., Ernst-Reuter-Platz und Bismarckstr. zur Kaiser-Friedrich-Str. umgeleitet bzw. verkehrt je nach Verlauf der Laufveranstaltung nur zwischen Flughafen Tegel und S+U Jungfernheide und endet hier. Die Haltestellen zwischen S+U Zoologischer Garten und S+U Jungfernheide werden nicht bedient. Die auf dem Umleitungsweg befindlichen Haltestellen werden angefahren."
            }, 
            "where": {
                "start": "S+U Zoologischer Garten", 
                "end": "U Jakob-Kaiser-Platz"
            }, 
            "id": 2982
        }, 
        {
            "what": {
                "line": "110", 
                "medium": "Bus"
            }, 
            "when": {
                "begin": "2014-10-12T09:00:00", 
                "end": "2014-10-12T15:00:00"
            }, 
            "why": {
                "url": "http://www.bvg.de/de/Fahrinfo/Verkehrsmeldungen/de/Fahrinfo/Verkehrsmeldungen/Verkehrsmeldung-Detail?id=2990", 
                "reason": "Sperrung wegen Veranstaltung"
            }, 
            "details": {
                "barrierfree": "12.10.2014 09:00", 
                "direction": "Beide", 
                "description": "Die Linie muss in beiden Fahrtrichtungen von der Brandenburgischen Str. \u00fcber Lewishamstr. und Kaiser-Friedrich-Str. zum Stuttgarter Platz umgeleitet werden und endet am U Wilmersdorfer Str. Die Haltestellen zwischen Hochmeisterplatz und S+U Zoologischer Garten werden nicht bedient. Zur Weiterfahrt in Richtung S+U Zoologischer Garten nutzen Sie bitte die Buslinien M19 und M29 bis U Kurf\u00fcrstendamm."
            }, 
            "where": {
                "start": "U Adenauerplatz", 
                "end": "S+U Zoologischer Garten"
            }, 
            "id": 2990
        }, 
        {
            "what": {
                "line": "130", 
                "medium": "Bus"
            }, 
            "when": {
                "begin": "2014-03-17T04:00:00", 
                "end": null
            }, 
            "why": {
                "url": "http://www.bvg.de/de/Fahrinfo/Verkehrsmeldungen/de/Fahrinfo/Verkehrsmeldungen/Verkehrsmeldung-Detail?id=1512", 
                "reason": "Sperrung wegen Bauarbeiten"
            }, 
            "details": {
                "barrierfree": "17.03.2014 04:00", 
                "direction": "Beide", 
                "description": "Die Haltestelle Radelandstr./Pflegeheim ist wegen Bauarbeiten in beiden Fahrtrichtungen bis auf weiteres in die Stadtrandstr. verlegt."
            }, 
            "where": {
                "start": "Radelandstr./Pflegeheim", 
                "end": "Radelandstr./Pflegeheim"
            }, 
            "id": 1512
        }, 
        {
            "what": {
                "line": "139", 
                "medium": "Bus"
            }, 
            "when": {
                "begin": "2013-06-24T15:00:00", 
                "end": null
            }, 
            "why": {
                "url": "http://www.bvg.de/de/Fahrinfo/Verkehrsmeldungen/de/Fahrinfo/Verkehrsmeldungen/Verkehrsmeldung-Detail?id=1528", 
                "reason": "Sperrung wegen Bauarbeiten"
            }, 
            "details": {
                "barrierfree": "24.06.2013 15:00", 
                "direction": "HAKENFELDE WERDERSTR.", 
                "description": "Die Linie muss in Fahrtrichtung Werderstr. vom Rohrdamm kommend \u00fcber Wohlrabedamm und Siemensdamm zur Nonnendammallee umgeleitet werden. Die Haltestelle Wernerwerkdamm ist verlegt in den Wohlrabedamm hinter Rohrdamm."
            }, 
            "where": {
                "start": "Rohrdamm/Wasserwerk", 
                "end": "Quellweg"
            }, 
            "id": 1528
        }, 
        {
            "what": {
                "line": "150", 
                "medium": "Bus"
            }, 
            "when": {
                "begin": "2014-10-11T08:00:00", 
                "end": "2014-10-13T00:00:00"
            }, 
            "why": {
                "url": "http://www.bvg.de/de/Fahrinfo/Verkehrsmeldungen/de/Fahrinfo/Verkehrsmeldungen/Verkehrsmeldung-Detail?id=1784", 
                "reason": "Sperrung wegen Bauarbeiten"
            }, 
            "details": {
                "barrierfree": "11.10.2014 08:00", 
                "direction": "S BUCH", 
                "description": "Die Linie muss in Fahrtrichtung S Buch von der Bucher Chaussee kommend \u00fcber Achillesstr., R\u00f6l\u00e4nder Str., Hubertusdamm, S Karow, Hubertusdamm, Bahnhofstr., Alt-Karow, Frundsbergstr. zur Endstelle Linie 350 umgeleitet werden. Die Abfahrt in Fahrtrichtung U Osloer Str. erfolgt von der Frundsbergstr. \u00fcber Lanker Str., Bahnhofstr., Hubertusdamm, S-Karow, Hubertusdamm, R\u00f6l\u00e4nder Str. und Achillesstr.  zur Bucher Chaussee. Die Haltestellen zwischen Stra\u00dfe 42 und  Buch werden nicht bedient. Die auf dem Umleitungsweg befindlichen Haltestellen der Linie 350 werden angefahren. Fahrg\u00e4ste mit Fahrziel S Buch fahren bis S Karow und steigen hier in die S Bahn."
            }, 
            "where": {
                "start": "U Osloer Str.", 
                "end": "U Osloer Str."
            }, 
            "id": 1784
        }, 
        {
            "what": {
                "line": "160", 
                "medium": "Bus"
            }, 
            "when": {
                "begin": "2014-04-27T04:00:00", 
                "end": null
            }, 
            "why": {
                "url": "http://www.bvg.de/de/Fahrinfo/Verkehrsmeldungen/de/Fahrinfo/Verkehrsmeldungen/Verkehrsmeldung-Detail?id=1564", 
                "reason": "Sperrung wegen Bauarbeiten der DB"
            }, 
            "details": {
                "barrierfree": "27.04.2014 04:00", 
                "direction": "Beide", 
                "description": "Die Linie verkehrt w\u00e4hrend der Br\u00fcckenbauarbeiten in beiden Fahrtrichtungen nur zwischen Siriusstr. und S Sch\u00f6neweide. Der Linienabschnitt zwischen S Sch\u00f6neweide/Sterndamm und Hasselwerder wird nicht bedient."
            }, 
            "where": {
                "start": "S Sch\u00f6neweide/Sterndamm", 
                "end": "Hasselwerderstr."
            }, 
            "id": 1564
        }, 
        {
            "what": {
                "line": "167", 
                "medium": "Bus"
            }, 
            "when": {
                "begin": "2014-08-10T20:00:00", 
                "end": null
            }, 
            "why": {
                "url": "http://www.bvg.de/de/Fahrinfo/Verkehrsmeldungen/de/Fahrinfo/Verkehrsmeldungen/Verkehrsmeldung-Detail?id=1384", 
                "reason": "Sperrung wegen Bauarbeiten der DB"
            }, 
            "details": {
                "barrierfree": "10.08.2014 20:00", 
                "direction": "U BODDINSTR.", 
                "description": "Die Linie wird nur in Richtung U Boddinstr. von der Oberspreestr. kommend \u00fcber Friedlander Str. - Ostritzer Str. - Bruno-B\u00fcrgel-Weg  zur Schnellerstr. umgeleitet."
            }, 
            "where": {
                "start": "S Spindlersfeld", 
                "end": "Bruno-B\u00fcrgel-Weg"
            }, 
            "id": 1384
        }, 
        {
            "what": {
                "line": "167", 
                "medium": "Bus"
            }, 
            "when": {
                "begin": "2014-08-10T20:00:00", 
                "end": "2014-12-31T00:00:00"
            }, 
            "why": {
                "url": "http://www.bvg.de/de/Fahrinfo/Verkehrsmeldungen/de/Fahrinfo/Verkehrsmeldungen/Verkehrsmeldung-Detail?id=2121", 
                "reason": "Abweichende Linienf\u00fchrung in der Oberspreestra\u00dfe"
            }, 
            "details": {
                "barrierfree": "Ja", 
                "url": "http://www.bvg.de/de/Fahrinfo/Verkehrsmeldungen/images/content/stoerungsmeldungen/Oberspreestrasse_Bus-167.pdf", 
                "direction": "U Boddinstra\u00dfe", 
                "description": "Wegen Stra\u00dfenbauarbeiten in der Oberspreestra\u00dfe muss die Linie, bis voraussichtlich Dezember 2014, umgeleitet werden:Die Umleitung ist nur in Richtung U Boddinstra\u00dfe n\u00f6tig:von Oberspreestra\u00dfe > Friedlander Stra\u00dfe > Ostritzer Stra\u00dfe > Bruno-B\u00fcrgel-Weg > Schnellerstra\u00dfe.In Richtung K\u00f6penick, M\u00fcggelschl\u00f6\u00dfchenweg fahren die Busse planm\u00e4\u00dfig.Entfallende Haltestellen in Richtung U Boddinstra\u00dfe:Oberspreestra\u00dfe/Bundeswehr und B\u00e4renlauchstra\u00dfeVerlegte Haltestellen:Friedlander Stra\u00dfe wird in die Friedlander Stra\u00dfe ca. 30 m hinter der Oberspreestra\u00dfe verlegt.Zus\u00e4tzliche Haltestellen:im Bruno-B\u00fcrgel-Weg n\u00f6rdlich vom S Oberspree"
            }, 
            "where": {
                "start": "Friedlander Stra\u00dfe", 
                "end": "Bruno-B\u00fcrgel-Weg"
            }, 
            "id": 2121
        }, 
        {
            "what": {
                "line": "167", 
                "medium": "Bus"
            }, 
            "when": {
                "begin": "2014-10-07T06:30:00", 
                "end": null
            }, 
            "why": {
                "url": "http://www.bvg.de/de/Fahrinfo/Verkehrsmeldungen/de/Fahrinfo/Verkehrsmeldungen/Verkehrsmeldung-Detail?id=2916", 
                "reason": "Sperrung wegen Bauarbeiten"
            }, 
            "details": {
                "barrierfree": "07.10.2014 06:30", 
                "direction": "K\u00d6PENICK M\u00dcGGEL- SCHL\u00d6\u00dfCHENWEG", 
                "description": "Auf Grund von Stra\u00dfenbauarbeiten ist die Haltestelle Oberspreestr./Bundeswehr in Fahrtrichtung K\u00f6penick, M\u00fcggelschl\u00f6\u00dfchenweg bis auf weiteres ersatzlos aufgehoben."
            }, 
            "where": {
                "start": "Bruno-B\u00fcrgel-Weg", 
                "end": "Friedlander Str."
            }, 
            "id": 2916
        }, 
        {
            "what": {
                "line": "184", 
                "medium": "Bus"
            }, 
            "when": {
                "begin": "2013-09-30T04:30:00", 
                "end": null
            }, 
            "why": {
                "url": "http://www.bvg.de/de/Fahrinfo/Verkehrsmeldungen/de/Fahrinfo/Verkehrsmeldungen/Verkehrsmeldung-Detail?id=1516", 
                "reason": "Sperrung wegen Bauarbeiten"
            }, 
            "details": {
                "barrierfree": "30.09.2013 04:30", 
                "direction": "TELTOW WARTHESTR.", 
                "description": "Diese Linie wird voraussichtlich bis zum Fr\u00fchjahr 2015, nur in Fahrtrichtung Teltow, Warthestra\u00dfe, ab Kreisverkehr Lichterfelder Allee \u00fcber Sch\u00f6nower Stra\u00dfe, Zeppelinufer, Jahnstra\u00dfe und Oderstra\u00dfe umgeleitet. Die Haltestellen in Teltow, Ruhlsdorfer Platz, Jahnstra\u00dfe und Striewitzweg werden bauzeitlich nicht bedient. Ersatzweise halten die Busse in Teltow an den auf dem Umleitungsweg befindlichen Haltestellen."
            }, 
            "where": {
                "start": "Reichartstr.", 
                "end": "Teltow, Einkaufszentrum Oderstr."
            }, 
            "id": 1516
        }, 
        {
            "what": {
                "line": "184", 
                "medium": "Bus"
            }, 
            "when": {
                "begin": "2014-09-15T07:00:00", 
                "end": null
            }, 
            "why": {
                "url": "http://www.bvg.de/de/Fahrinfo/Verkehrsmeldungen/de/Fahrinfo/Verkehrsmeldungen/Verkehrsmeldung-Detail?id=2124", 
                "reason": "Sperrung wegen Bauarbeiten"
            }, 
            "details": {
                "barrierfree": "15.09.2014 07:00", 
                "direction": "Beide", 
                "description": "Die Linie wird in beiden Fahrtrichtungen \u00fcber Kaiserin-Augusta-Str. umgeleitet. In Fahrtrichtung Teltow sind die Haltestellen U Kaiserin-Augusta-Str. bzw. Albrechtstr./Manteuffelstr. zum Tempelhofer Damm hinter Albrechtstr. bzw. zur Manteuffelstr. hinter Kaiserin-Augusta-Str., in Fahrtrichtung S S\u00fcdkreuz zur Kaiserin-Augusta-Str. hinter Manteuffelstr. bzw. zum Tempelhofer Damm vor Albrechtstr. verlegt."
            }, 
            "where": {
                "start": "Rathaus Tempelhof", 
                "end": "Friedrich-Wilhelm-Str."
            }, 
            "id": 2124
        }, 
        {
            "what": {
                "line": "187", 
                "medium": "Bus"
            }, 
            "when": {
                "begin": "2014-10-12T09:00:00", 
                "end": "2014-10-12T15:00:00"
            }, 
            "why": {
                "url": "http://www.bvg.de/de/Fahrinfo/Verkehrsmeldungen/de/Fahrinfo/Verkehrsmeldungen/Verkehrsmeldung-Detail?id=2994", 
                "reason": "Sperrung wegen Veranstaltung"
            }, 
            "details": {
                "barrierfree": "12.10.2014 09:00", 
                "direction": "Beide", 
                "description": "Die Linie muss in Fahrtrichtung Halbauer Weg \u00fcber Alt-Moabit, Invalidenstr., Tiergartentunnel und Tiergartenstr. zur Klingelh\u00f6ferstr. umgeleitet werden. Die Haltestellen zwischen Alt-Moabit/Rathenower Str. und Nord. Botschaften/Adenauer Stiftg. werden nicht bedient. Die auf dem Umleitungsweg befindlichen Haltestellen werden angefahren."
            }, 
            "where": {
                "start": "Alt-Moabit/Rathenower Str.", 
                "end": "L\u00fctzowplatz"
            }, 
            "id": 2994
        }, 
        {
            "what": {
                "line": "194", 
                "medium": "Bus"
            }, 
            "when": {
                "begin": "2014-06-30T04:00:00", 
                "end": "2014-10-20T04:00:00"
            }, 
            "why": {
                "url": "http://www.bvg.de/de/Fahrinfo/Verkehrsmeldungen/de/Fahrinfo/Verkehrsmeldungen/Verkehrsmeldung-Detail?id=1620", 
                "reason": "Sperrung wegen Bauarbeiten der DB"
            }, 
            "details": {
                "barrierfree": "30.06.2014 04:00", 
                "direction": "Beide", 
                "description": "Die Linie muss in beiden Fahrtrichtungen \u00fcber Hauptstr. und Schlichtallee umgeleitet werden. Die Haltestellen S Rummelsburg und S N\u00f6ldnerplatz/Schlichtallee werden nicht bedient. Daf\u00fcr sind auf dem Umleitungsweg in der Hauptstr. in H\u00f6he Haus Nr.4A bzw. gegen\u00fcber und Schlichtallee/Fischerstr. Ersatzhaltestellen eingerichtet."
            }, 
            "where": {
                "start": "S Ostkreuz", 
                "end": "W\u00f6nnichstr."
            }, 
            "id": 1620
        }, 
        {
            "what": {
                "line": "197", 
                "medium": "Bus"
            }, 
            "when": {
                "begin": "2014-07-25T08:30:00", 
                "end": null
            }, 
            "why": {
                "url": "http://www.bvg.de/de/Fahrinfo/Verkehrsmeldungen/de/Fahrinfo/Verkehrsmeldungen/Verkehrsmeldung-Detail?id=1532", 
                "reason": "Sperrung wegen Bauarbeiten"
            }, 
            "details": {
                "barrierfree": "25.07.2014 08:30", 
                "direction": "Beide", 
                "description": "Die Linie wird in Richtung S Mahlsdorf vom Blumberger Damm kommend \u00fcber Eisenacher Str. zur Gothaer Str. und in Richtung Prerower Platz von der Alten Hellersdorfer Str. kommend  \u00fcber Zossener Str. zur Landsberger Allee umgeleitet. Die Buslinie X54 bedient bauzeitlich die Haltestellen der Linie 197 zwischen Blumberger Damm und Kaulsdorfer Stra\u00dfe."
            }, 
            "where": {
                "start": "Landsberger Allee/Blumberger D.", 
                "end": "Spremberger Str."
            }, 
            "id": 1532
        }, 
        {
            "what": {
                "line": "245", 
                "medium": "Bus"
            }, 
            "when": {
                "begin": "2014-07-02T04:00:00", 
                "end": null
            }, 
            "why": {
                "url": "http://www.bvg.de/de/Fahrinfo/Verkehrsmeldungen/de/Fahrinfo/Verkehrsmeldungen/Verkehrsmeldung-Detail?id=1418", 
                "reason": "Sperrung wegen Bauarbeiten"
            }, 
            "details": {
                "barrierfree": "02.07.2014 04:00", 
                "direction": "Beide", 
                "description": "Die Linie muss in Fahrtrichtung S+U Zoologischer Garten \u00fcber Caroline-Michaelis-Str., Julie-Wolfthorn-Str., Zinnowitzer Str., Chausseestr., Habersaathstr. und Schwarzer Weg umgeleitet werden."
            }, 
            "where": {
                "start": "S Nordbahnhof/Gartenstr.", 
                "end": "Invalidenpark"
            }, 
            "id": 1418
        }, 
        {
            "what": {
                "line": "245", 
                "medium": "Bus"
            }, 
            "when": {
                "begin": "2014-10-12T09:00:00", 
                "end": "2014-10-12T15:00:00"
            }, 
            "why": {
                "url": "http://www.bvg.de/de/Fahrinfo/Verkehrsmeldungen/de/Fahrinfo/Verkehrsmeldungen/Verkehrsmeldung-Detail?id=2974", 
                "reason": "Sperrung wegen Veranstaltung"
            }, 
            "details": {
                "barrierfree": "12.10.2014 09:00", 
                "direction": "Beide", 
                "description": "Die Linie verkehrt in beiden Fahrtrichtungen nur zwischen S Nordbahnhof und Marchbr\u00fccke und endet hier. Die Haltestellen zwischen Marchbr\u00fccke und S+U Zoologischer Garten werden nicht bedient."
            }, 
            "where": {
                "start": "Marchbr\u00fccke", 
                "end": "S+U Zoologischer Garten"
            }, 
            "id": 2974
        }, 
        {
            "what": {
                "line": "246", 
                "medium": "Bus"
            }, 
            "when": {
                "begin": "2014-01-17T05:00:00", 
                "end": null
            }, 
            "why": {
                "url": "http://www.bvg.de/de/Fahrinfo/Verkehrsmeldungen/de/Fahrinfo/Verkehrsmeldungen/Verkehrsmeldung-Detail?id=1574", 
                "reason": "Sperrung wegen Bauarbeiten"
            }, 
            "details": {
                "barrierfree": "17.01.2014 05:00", 
                "direction": "Beide", 
                "description": "Die Linie verkehrt bis auf weiteres nur zwischen U Friedrich-Wilhelm-Platz und S+U Hermannstra\u00dfe.  Fahrg\u00e4ste mit dem Fahrtziel S K\u00f6llnische Heide  nutzen  bitte ab S+U Hermannstr. die S45, S46 oder S47. Vom  S K\u00f6llnische Heide verkehrt die neu eingerichtete Linie 341 als Ersatz f\u00fcr die Linie 246 \u00fcber Planetenstra\u00dfe> Neuk\u00f6llnische Allee > Haberstra\u00dfe > Bergiusstra\u00dfe > Nobelstra\u00dfe >Neuk\u00f6llnische Allee und  Jupiterstra\u00dfe zur Sonnenallee (S K\u00f6llnische Heide) als Ringlinie. Fahrg\u00e4ste mit dem Fahrtziel Lahnstra\u00dfe nutzen die ab S+U Hermannstra\u00dfe die neu eingerichtete Linie 377. Ausgew\u00e4hlte Fahrten der Linie  246 bieten zwischen 6 Uhr und 7 Uhr sowie gegen 22 Uhr von Tempelhof kommend eine umsteigefreie Verbindung  als Linie  370 zum U Grenzallee (U7) und zur\u00fcck."
            }, 
            "where": {
                "start": "S+U Hermannstr./Silbersteinstr.", 
                "end": "Neuk\u00f6llnische Al./Forsthausallee"
            }, 
            "id": 1574
        }, 
        {
            "what": {
                "line": "249", 
                "medium": "Bus"
            }, 
            "when": {
                "begin": "2014-10-12T09:00:00", 
                "end": "2014-10-12T15:00:00"
            }, 
            "why": {
                "url": "http://www.bvg.de/de/Fahrinfo/Verkehrsmeldungen/de/Fahrinfo/Verkehrsmeldungen/Verkehrsmeldung-Detail?id=2992", 
                "reason": "Sperrung wegen Veranstaltung"
            }, 
            "details": {
                "barrierfree": "12.10.2014 09:00", 
                "direction": "Beide", 
                "description": "Die Linie muss in Fahrtrichtung S+U Zoologischer Garten \u00fcber Uhlandstr. und Kurf\u00fcrstendamm zur Joachimstaler Str. umgeleitet werden und endet am U Kurf\u00fcrstendamm. In Fahrtrichtung Roseneck fahren die Busse ab U Kurf\u00fcrstendamm."
            }, 
            "where": {
                "start": "Lietzenburger Str./Uhlandstr.", 
                "end": "S+U Zoologischer Garten"
            }, 
            "id": 2992
        }, 
        {
            "what": {
                "line": "259", 
                "medium": "Bus"
            }, 
            "when": {
                "begin": "2014-08-24T04:00:00", 
                "end": null
            }, 
            "why": {
                "url": "http://www.bvg.de/de/Fahrinfo/Verkehrsmeldungen/de/Fahrinfo/Verkehrsmeldungen/Verkehrsmeldung-Detail?id=1470", 
                "reason": "Linienma\u00dfnahmen"
            }, 
            "details": {
                "barrierfree": "24.08.2014 04:00", 
                "direction": "Beide", 
                "description": "Die Linie wird statt \u00fcber Schwanebecker Chaussee \u00fcber Lindenberger Weg zum S-Bahnhof Buch gef\u00fchrt. Die Linie 259 verkehrt mit folgender Wegf\u00fchrung: Buchholz-West, Aubertstra\u00dfe - Blankenfelder Stra\u00dfe - Rosenthaler Weg - Triftstra\u00dfe - Sch\u00f6nerlinder Stra\u00dfe - Sch\u00f6nerlinder Chaussee - Wiltbergstra\u00dfe - Lindenberger Weg - Kleiststra\u00dfe - Lindenberger Stra\u00dfe - Bucher Chaussee - Dorfstra\u00dfe - Stichfahrt Schwanebeck Schule - Dorfstra\u00dfe - Bernauer Stra\u00dfe - Karl-Marx-Stra\u00dfe - Dorfstra\u00dfe - Malchower Chaussee - Berliner Allee - Indira-Gandhi-Stra\u00dfe - Hansastra\u00dfe -Giersstra\u00dfe - Falkenberger Stra\u00dfe - Stadion Buschallee, Hansastra\u00dfe."
            }, 
            "where": {
                "start": "S Buch", 
                "end": "Lindenberg, Bernauer Str."
            }, 
            "id": 1470
        }, 
        {
            "what": {
                "line": "259", 
                "medium": "Bus"
            }, 
            "when": {
                "begin": "2014-09-30T04:00:00", 
                "end": null
            }, 
            "why": {
                "url": "http://www.bvg.de/de/Fahrinfo/Verkehrsmeldungen/de/Fahrinfo/Verkehrsmeldungen/Verkehrsmeldung-Detail?id=2854", 
                "reason": "Sperrung wegen Bauarbeiten"
            }, 
            "details": {
                "barrierfree": "30.09.2014 04:00", 
                "direction": "STAD.BUSCHALLEE/ HANSASTR.", 
                "description": "Die Linie muss in Fahrtrichtung Stadion Buschallee/Hansastr. von der Wiltbergstr. \u00fcber Alt-Buch und Schwanebecker Chaussee zur Bucher Chaussee umgeleitet werden. Die Haltestellen zwischen S Buch und Schwanebeck/Neue K\u00e4rntner Str. werden nicht bedient. Daf\u00fcr werden die auf dem Umleitungsweg befindlichen Haltestellen Alt-Buch/Karower Str., Schwanebecker Chaussee und Schwanebeck, Lindenberger Str. angefahren."
            }, 
            "where": {
                "start": "S Buch", 
                "end": "Schwanebeck, Neue K\u00e4rntner Str."
            }, 
            "id": 2854
        }, 
        {
            "what": {
                "line": "277", 
                "medium": "Bus"
            }, 
            "when": {
                "begin": "2014-01-17T05:00:00", 
                "end": null
            }, 
            "why": {
                "url": "http://www.bvg.de/de/Fahrinfo/Verkehrsmeldungen/de/Fahrinfo/Verkehrsmeldungen/Verkehrsmeldung-Detail?id=1386", 
                "reason": "Sperrung wegen Bauarbeiten"
            }, 
            "details": {
                "barrierfree": "17.01.2014 05:00", 
                "direction": "Beide", 
                "description": "Die Linie verkehrt bis auf weiteres nur zwischen Stadtrandsiedlung und S+U Hermannstra\u00dfe. Zum Erreichen der Industrieanrainer Neuk\u00f6lln, Am Oberhafen nutzen Sie bitte die neu eingerichtete Linie 370 ab S+U Hermannstra\u00dfe \u00fcber Silbersteinstr., Lahnstr., Naumburger Str. und Grenzallee. Den Streckenabschnitt vom S Pl\u00e4nterwald bis Grenzallee/Neuk\u00f6llnische Allee  und dann weiter \u00fcber die Lahnstra\u00dfe > Silbersteinstra\u00dfe zum S+U Hermannstra\u00dfe bef\u00e4hrt neu die Linie  377."
            }, 
            "where": {
                "start": "S+U Hermannstr.", 
                "end": "S Pl\u00e4nterwald"
            }, 
            "id": 1386
        }, 
        {
            "what": {
                "line": "296", 
                "medium": "Bus"
            }, 
            "when": {
                "begin": "2014-09-16T09:00:00", 
                "end": null
            }, 
            "why": {
                "url": "http://www.bvg.de/de/Fahrinfo/Verkehrsmeldungen/de/Fahrinfo/Verkehrsmeldungen/Verkehrsmeldung-Detail?id=2014", 
                "reason": "Sperrung wegen Bauarbeiten der Wasserbetriebe"
            }, 
            "details": {
                "barrierfree": "16.09.2014 09:00", 
                "direction": "S+U LICHTENBERG", 
                "description": "Die Linie muss in Fahrtrichtung S+U Lichtenberg von der Rummelsburger Str. kommend \u00fcber Robert-Uhrig-Str. umgeleitet werden. Die Haltestelle Rummelsburger Str./U Friedrichsfelde ist ersatzlos aufgehoben. Die Haltestelle U Friedrichsfelde ist verlegt zur Robert-Uhrig-Str. vor Zachertstr."
            }, 
            "where": {
                "start": "Schwarzmeerstr.", 
                "end": "Lincolnstr./Einbecker Str."
            }, 
            "id": 2014
        }, 
        {
            "what": {
                "line": "309", 
                "medium": "Bus"
            }, 
            "when": {
                "begin": "2014-10-12T09:00:00", 
                "end": "2014-10-12T15:00:00"
            }, 
            "why": {
                "url": "http://www.bvg.de/de/Fahrinfo/Verkehrsmeldungen/de/Fahrinfo/Verkehrsmeldungen/Verkehrsmeldung-Detail?id=2970", 
                "reason": "Sperrung wegen Veranstaltung"
            }, 
            "details": {
                "barrierfree": "12.10.2014 09:00", 
                "direction": "Beide", 
                "description": "Die Linie muss in Fahrtrichtung Schlosspark-Klinik von der Suarezstr. \u00fcber Kaiserdamm zur Sophie-Charlotten-Str. umgeleitet bzw. je nach Verlauf der Veranstaltung in beiden Fahrtrichtungen eingestellt werden. Die Haltestellen zwischen U Sophie-Charlotte-Platz und Mollwitzstr. werden nicht bedient."
            }, 
            "where": {
                "start": "Mollwitzstr.", 
                "end": "U Wilmersdorfer Str."
            }, 
            "id": 2970
        }, 
        {
            "what": {
                "line": "353", 
                "medium": "Bus"
            }, 
            "when": {
                "begin": "2014-08-24T04:00:00", 
                "end": null
            }, 
            "why": {
                "url": "http://www.bvg.de/de/Fahrinfo/Verkehrsmeldungen/de/Fahrinfo/Verkehrsmeldungen/Verkehrsmeldung-Detail?id=1474", 
                "reason": "Linienma\u00dfnahmen"
            }, 
            "details": {
                "barrierfree": "24.08.2014 04:00", 
                "direction": "Beide", 
                "description": "Die Linie wird zur Endstelle Buch, P\u00f6lnitzweg gef\u00fchrt. Die Linie 353 verkehrt mit folgender Wegf\u00fchrung: Buch, P\u00f6lnitzweg - P\u00f6lnitzweg - Hobrechtsfelder Chaussee - Wiltbergstra\u00dfe - (zur\u00fcck: Wiltbergstra\u00dfe - R\u00f6bellweg - P\u00f6lnitzweg) - Lindenberger Weg - Biomedizinscher Campus Berlin Buch - Campus Buch"
            }, 
            "where": {
                "start": "S Buch", 
                "end": "Campus Buch"
            }, 
            "id": 1474
        }, 
        {
            "what": {
                "line": "390", 
                "medium": "Bus"
            }, 
            "when": {
                "begin": "2014-08-24T04:00:00", 
                "end": null
            }, 
            "why": {
                "url": "http://www.bvg.de/de/Fahrinfo/Verkehrsmeldungen/de/Fahrinfo/Verkehrsmeldungen/Verkehrsmeldung-Detail?id=1476", 
                "reason": "Linienma\u00dfnahmen"
            }, 
            "details": {
                "barrierfree": "24.08.2014 04:00", 
                "direction": "Beide", 
                "description": "Das Verkehrsangebot wird im Bereich Brandenburg verbessert.  Die Linie 390 verkehrt mit folgender Wegf\u00fchrung: Lindenberg, Klarah\u00f6h - Wendeschleife Klarah\u00f6h - Birkholzer Weg - Lindenberger Weg - Lindenberger Stra\u00dfe - Dorfstra\u00dfe - M\u00e4rkische Allee - Havemannstra\u00dfe- Schorfheidestra\u00dfe - Feldstra\u00dfe - Dorfstra\u00dfe - Lindenberger Stra\u00dfe - Bahnstra\u00dfe - Enrst-Th\u00e4lmann-Stra\u00dfe - Kirschenallee - Fasanenstra\u00dfe - Blumberger Chaussee - Mehrower Stra\u00dfe - Ahrensfelder Chaussee - Dorfstra\u00dfe - Ahrensfelder Chaussee - Mehrower Stra\u00dfe - Mehrower Chaussee - Ahrensfelder Chaussee - Dorfstra\u00dfe - Ahrensfelder Chaussee - Mehrower Chaussee - Mehrower Stra\u00dfe - Blumberger Chaussee - Freienwalder Chaussee - Bahnhofstra\u00dfe - Kleine Bahnhofstra\u00dfe - Mittelstra\u00dfe - Berliner Stra\u00dfe - Schulstra\u00dfe - Schlo\u00dfstra\u00dfe - Berliner Stra\u00dfe - Freienwalder Chaussee - Birkholzer Stra\u00dfe - Am Bahnhof - Bahnhofstra\u00dfe - Blumberg, Bahnhof"
            }, 
            "where": {
                "start": "S Ahrensfelde", 
                "end": "Mehrow, Kirche"
            }, 
            "id": 1476
        }, 
        {
            "what": {
                "line": "N2", 
                "medium": "Nachtbus"
            }, 
            "when": {
                "begin": "2014-02-17T23:00:00", 
                "end": null
            }, 
            "why": {
                "url": "http://www.bvg.de/de/Fahrinfo/Verkehrsmeldungen/de/Fahrinfo/Verkehrsmeldungen/Verkehrsmeldung-Detail?id=1388", 
                "reason": "Sperrung wegen Bauarbeiten"
            }, 
            "details": {
                "barrierfree": "17.02.2014 23:00", 
                "direction": "U RUHLEBEN", 
                "description": "Die Linie muss in Fahrtrichtung U Ruhleben von der Berliner Str. kommend \u00fcber Maximilianstr. und M\u00fchlenstr. zur Berliner Str. umgeleitet werden. Die Haltestelle U Vinetastr. ist zur M\u00fchlenstr. vor Tiroler Str. verlegt."
            }, 
            "where": {
                "start": "S+U Pankow", 
                "end": "Sch\u00f6nhauser Allee/Bornholmer Str"
            }, 
            "id": 1388
        }, 
        {
            "what": {
                "line": "N7", 
                "medium": "Nachtbus"
            }, 
            "when": {
                "begin": "2013-03-26T00:01:00", 
                "end": null
            }, 
            "why": {
                "url": "http://www.bvg.de/de/Fahrinfo/Verkehrsmeldungen/de/Fahrinfo/Verkehrsmeldungen/Verkehrsmeldung-Detail?id=1544", 
                "reason": "Sperrung wegen Bauarbeiten der BVG"
            }, 
            "details": {
                "barrierfree": "26.03.2013 00:01", 
                "direction": "S+U-BAHNHOF RATHAUS SPANDAU", 
                "description": "Die Linie muss in Fahrtrichtung S+U Rathaus Spandau von der Bismarckstr. kommend \u00fcber Wilmersdorfer Str. und Zillestr. zur Richard-Wagner-Str. umgeleitet werden. Die Haltestelle U Bismarckstr. wird nicht bedient. Daf\u00fcr ist in der Wilmersdorfer Str. in H\u00f6he Hausnummer 141 eine Ersatzhaltestelle eingerichtet."
            }, 
            "where": {
                "start": "Kaiser-Friedrich-Str./Kantstr.", 
                "end": "U Richard-Wagner-Platz"
            }, 
            "id": 1544
        }, 
        {
            "what": {
                "line": "N7", 
                "medium": "Nachtbus"
            }, 
            "when": {
                "begin": "2014-08-04T23:00:00", 
                "end": null
            }, 
            "why": {
                "url": "http://www.bvg.de/de/Fahrinfo/Verkehrsmeldungen/de/Fahrinfo/Verkehrsmeldungen/Verkehrsmeldung-Detail?id=1618", 
                "reason": "Sperrung wegen Bauarbeiten der BVG"
            }, 
            "details": {
                "barrierfree": "04.08.2014 23:00", 
                "direction": "FLUGH SCH\u00d6NEFELD AIRPORT", 
                "description": "Die Linie muss in Fahrtrichtung Flughafen Sch\u00f6nefeld \u00fcber Erkstr., Sonnenallee und Saalestr. umgeleitet werden. Zum Erreichen der Haltestelle Alfred-Scholz-Platz nutzen Sie bitte die Haltestelle U Rathaus Neuk\u00f6lln. Die Haltestellen U Karl-Marx-Str. und Karl-Marx-Platz werden nicht bedient. Daf\u00fcr wird die auf dem Umleitungsweg befindliche Haltestelle Hertzbergplatz angefahren."
            }, 
            "where": {
                "start": "U Rathaus Neuk\u00f6lln", 
                "end": "S+U Neuk\u00f6lln"
            }, 
            "id": 1618
        }, 
        {
            "what": {
                "line": "N9", 
                "medium": "Nachtbus"
            }, 
            "when": {
                "begin": "2013-02-19T00:00:00", 
                "end": null
            }, 
            "why": {
                "url": "http://www.bvg.de/de/Fahrinfo/Verkehrsmeldungen/de/Fahrinfo/Verkehrsmeldungen/Verkehrsmeldung-Detail?id=1568", 
                "reason": "Sperrung wegen Bauarbeiten der Wasserbetriebe"
            }, 
            "details": {
                "barrierfree": "19.02.2013 00:00", 
                "direction": "U OSLOER STR.", 
                "description": "Die Linie muss in Fahrtrichtung U Osloer Str. von der Hardenbergstr. \u00fcber Ernst-Reuter-Platz und Stra\u00dfe des 17. Juni zur Bachstr. umgeleitet werden."
            }, 
            "where": {
                "start": "S+U Rathaus Steglitz", 
                "end": "S+U Rathaus Steglitz"
            }, 
            "id": 1568
        }, 
        {
            "what": {
                "line": "N16", 
                "medium": "Nachtbus"
            }, 
            "when": {
                "begin": "2014-10-06T20:00:00", 
                "end": "2014-10-20T05:00:00"
            }, 
            "why": {
                "url": "http://www.bvg.de/de/Fahrinfo/Verkehrsmeldungen/de/Fahrinfo/Verkehrsmeldungen/Verkehrsmeldung-Detail?id=2864", 
                "reason": "Sperrung wegen Bauarbeiten"
            }, 
            "details": {
                "barrierfree": "06.10.2014 20:00", 
                "direction": "Beide", 
                "description": "Die Linie muss in beiden Fahrtrichtungen \u00fcber Breitestr. und Schlo\u00dfstr. umgeleitet werden. Die Haltestelle Alter Markt/Landtag ist f\u00fcr beide Fahrtrichtungen in die Breite Str. verlegt. Die Haltestelle Lange Br\u00fccke ist ersatzlos aufgehoben."
            }, 
            "where": {
                "start": "S Potsdam Hauptbahnhof", 
                "end": "Platz der Einheit/Bildungsforum"
            }, 
            "id": 2864
        }, 
        {
            "what": {
                "line": "N40", 
                "medium": "Nachtbus"
            }, 
            "when": {
                "begin": "2014-07-02T04:00:00", 
                "end": null
            }, 
            "why": {
                "url": "http://www.bvg.de/de/Fahrinfo/Verkehrsmeldungen/de/Fahrinfo/Verkehrsmeldungen/Verkehrsmeldung-Detail?id=1550", 
                "reason": "Sperrung wegen Bauarbeiten"
            }, 
            "details": {
                "barrierfree": "02.07.2014 04:00", 
                "direction": "Beide", 
                "description": "Die Linie muss in Fahrtrichtung Friedrichshain/W\u00fchlischplatz von der Invalidenstr. kommend \u00fcber Caroline-Michaelis-Str., Julie-Wolfthorn-Str. und Gartenstr. zur Invalidenstr. bzw. in Fahrtrichtung U Turmstr. von der Invalidenstr. \u00fcber Gartenstr., Julie-Wolfthorn-Str., Zinnowitzer Str., Chausseestr., Habersaathstr. und Schwarzer Weg zur Invalidenstr. umgeleitet werden. In Fahrtrichtung Friedrichshain/W\u00fchlischplatz ist die Haltestelle S Nordbahnhof in zur Julie-Wolfthorn-Str. vor Gartenstr. bzw. in Fahrtrichtung U Turmstr. sind die Haltestellen S Nordbahnhof zur Julie-Wolfthorn-Str. hinter Gartenstr., U Naturkundemuseum zur Zinnowitzer Str. vor Chausseestr. verlegt. Die Haltestelle Invalidenpark ist wieder am planm\u00e4\u00dfigen Standort eingerichtet."
            }, 
            "where": {
                "start": "S Nordbahnhof", 
                "end": "Pappelplatz"
            }, 
            "id": 1550
        }, 
        {
            "what": {
                "line": "N40", 
                "medium": "Nachtbus"
            }, 
            "when": {
                "begin": "2014-09-30T00:30:00", 
                "end": null
            }, 
            "why": {
                "url": "http://www.bvg.de/de/Fahrinfo/Verkehrsmeldungen/de/Fahrinfo/Verkehrsmeldungen/Verkehrsmeldung-Detail?id=2742", 
                "reason": "Sperrung wegen Bauarbeiten der BVG"
            }, 
            "details": {
                "barrierfree": "30.09.2014 00:30", 
                "direction": "W\u00dcHLISCHPLATZ", 
                "description": "Die Linie wird in Fahrtrichtung W\u00fchlischplatz \u00fcber Julie-Wolfthorn-Stra\u00dfe, Bernauer Stra\u00dfe und Brunnenstra\u00dfe umgeleitet."
            }, 
            "where": {
                "start": "S Nordbahnhof", 
                "end": "Brunnenstr./Invalidenstr."
            }, 
            "id": 2742
        }, 
        {
            "what": {
                "line": "N50", 
                "medium": "Nachtbus"
            }, 
            "when": {
                "begin": "2014-09-16T09:00:00", 
                "end": null
            }, 
            "why": {
                "url": "http://www.bvg.de/de/Fahrinfo/Verkehrsmeldungen/de/Fahrinfo/Verkehrsmeldungen/Verkehrsmeldung-Detail?id=2012", 
                "reason": "Sperrung wegen Bauarbeiten der Wasserbetriebe"
            }, 
            "details": {
                "barrierfree": "16.09.2014 09:00", 
                "direction": "BUCHHOLZ-WEST HUGENOTTENPLATZ", 
                "description": "Die Linie muss in Fahrtrichtung Hugenottenplatz von der Rummelsburger Str. kommend \u00fcber Robert-Uhrig-Str. umgeleitet werden. Die Haltestelle U Friedrichsfelde ist verlegt zur Robert-Uhrig-Str. vor Zachertstr."
            }, 
            "where": {
                "start": "Schwarzmeerstr.", 
                "end": "Lincolnstr./Einbecker Str."
            }, 
            "id": 2012
        }, 
        {
            "what": {
                "line": "N67", 
                "medium": "Nachtbus"
            }, 
            "when": {
                "begin": "2014-04-27T04:00:00", 
                "end": null
            }, 
            "why": {
                "url": "http://www.bvg.de/de/Fahrinfo/Verkehrsmeldungen/de/Fahrinfo/Verkehrsmeldungen/Verkehrsmeldung-Detail?id=1390", 
                "reason": "Sperrung wegen Bauarbeiten der DB"
            }, 
            "details": {
                "barrierfree": "27.04.2014 04:00", 
                "direction": "Beide", 
                "description": "Die Linie wird w\u00e4hrend der Br\u00fcckenbauarbeiten in Fahrtrichtung S Sch\u00f6neweide \u00fcber Michael-Br\u00fcckner-Str., Fennstr. und Schnellerstr. zur Hasselwerder Str. umgeleitet und endet hier. Die Abfahrt in Fahrtrichtung U Stadtmitte bzw. U M\u00e4rkisches Museum erfolgt in der Hasselwerder Str. Die Haltestelle S Sch\u00f6neweide/Sterndamm wird nicht bedient."
            }, 
            "where": {
                "start": "S Sch\u00f6neweide", 
                "end": "S Sch\u00f6neweide/Sterndamm"
            }, 
            "id": 1390
        }, 
        {
            "what": {
                "line": "N94", 
                "medium": "Nachtbus"
            }, 
            "when": {
                "begin": "2014-06-30T04:00:00", 
                "end": "2014-10-20T04:00:00"
            }, 
            "why": {
                "url": "http://www.bvg.de/de/Fahrinfo/Verkehrsmeldungen/de/Fahrinfo/Verkehrsmeldungen/Verkehrsmeldung-Detail?id=1616", 
                "reason": "Sperrung wegen Bauarbeiten der DB"
            }, 
            "details": {
                "barrierfree": "30.06.2014 04:00", 
                "direction": "Beide", 
                "description": "Die Linie muss in beiden Fahrtrichtungen \u00fcber Hauptstr. und Schlichtallee umgeleitet werden. Die Haltestellen S Rummelsburg und S N\u00f6ldnerplatz/Schlichtallee werden nicht bedient. Daf\u00fcr sind auf dem Umleitungsweg in der Hauptstr. in H\u00f6he Haus Nr.4A bzw. gegen\u00fcber und Schlichtallee/Fischerstr. Ersatzhaltestellen eingerichtet."
            }, 
            "where": {
                "start": "S Ostkreuz", 
                "end": "L\u00fcckstr./Weitlingstr."
            }, 
            "id": 1616
        }
    ], 
    "source_root_url": "http://www.bvg.de/de/Fahrinfo/Verkehrsmeldungen"
}
```

## Installation

Die App läuft unter Python und nutzt [Flask](http://flask.pocoo.org) und [Beautiful Soup](http://www.crummy.com/software/BeautifulSoup/). Die Installation ist einfach:

    virtualenv venv
    source venv/bin/activate
    pip install -r requirements.txt

## Lizenz

Die stammen von den Webseiten der [Berliner Verkehrsbetriebe](http://www.bvg.de/de/). Eine Klärung der Nutzungsbedinungen steht noch aus. Die Nutzung dieses Programmes und der dadurch bereitgestellten API ist nur zum persönlichen privaten Gebrauch gestattet. Jede weitergehende Nutzung, insbesondere die gewerbliche Vervielfältigung, Verbreitung, oder Veröffentlichung zu gewerblichen Zwecken ist untersagt.
