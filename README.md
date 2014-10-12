# BVG Verkehrsmeldungen

Bereitet die [Verkehrsmeldungen der BVG](http://www.bvg.de/de/Fahrinfo/Verkehrsmeldungen) als JSON-API auf.

## Beispiel

    ./app/bvg.py

```json
{
  "date_updated": "2014-10-12T02:16:24.472136", 
  "issue_count": 62, 
  "request_url": "http://localhost:5000/", 
  "issues": [
    {
      "where": {
        "start": "U Wittenbergplatz", 
        "end": "U Bismarckstr."
      }, 
      "what": {
        "line": "U2", 
        "medium": "U-Bahn"
      }, 
      "when": {
        "begin": "2014-08-25T21:00:00", 
        "end": "2014-12-12T03:30:00"
      }, 
      "id": 1900, 
      "why": {
        "url": "http://www.bvg.de/de/Fahrinfo/Verkehrsmeldungen/de/Fahrinfo/Verkehrsmeldungen/Verkehrsmeldung-Detail?id=1900", 
        "reason": "Sperrung wegen Bauarbeiten der BVG"
      }
    }, 
    {
      "where": {
        "start": "U Wittenbergplatz", 
        "end": "U Bismarckstra\u00dfe"
      }, 
      "what": {
        "line": "U2", 
        "medium": "U-Bahn"
      }, 
      "when": {
        "begin": "2014-08-25T21:00:00", 
        "end": "2014-12-12T03:30:00"
      }, 
      "id": 2025, 
      "why": {
        "url": "http://www.bvg.de/de/Fahrinfo/Verkehrsmeldungen/de/Fahrinfo/Verkehrsmeldungen/Verkehrsmeldung-Detail?id=2025", 
        "reason": "Zusatzinformation: Haltestellen des Ersatzverkehrs"
      }
    }, 
    {
      "where": {
        "start": "S Greifswalder Stra\u00dfe", 
        "end": "S Greifswalder Stra\u00dfe"
      }, 
      "what": {
        "line": "M4", 
        "medium": "MetroTram"
      }, 
      "when": {
        "begin": "2014-07-25T09:45:00", 
        "end": "2014-12-31T23:59:00"
      }, 
      "id": 1789, 
      "why": {
        "url": "http://www.bvg.de/de/Fahrinfo/Verkehrsmeldungen/de/Fahrinfo/Verkehrsmeldungen/Verkehrsmeldung-Detail?id=1789", 
        "reason": "Haltestellenverlegung am S Greifswalder Stra\u00dfe"
      }
    }, 
    {
      "where": {
        "start": "S Landsberger Allee", 
        "end": "S Landsberger Allee"
      }, 
      "what": {
        "line": "M5", 
        "medium": "MetroTram"
      }, 
      "when": {
        "begin": "2014-09-22T04:00:00", 
        "end": null
      }, 
      "id": 2702, 
      "why": {
        "url": "http://www.bvg.de/de/Fahrinfo/Verkehrsmeldungen/de/Fahrinfo/Verkehrsmeldungen/Verkehrsmeldung-Detail?id=2702", 
        "reason": "Sperrung wegen Bauarbeiten der BVG"
      }
    }, 
    {
      "where": {
        "start": "S Landsberger Allee", 
        "end": "S Landsberger Allee"
      }, 
      "what": {
        "line": "M6", 
        "medium": "MetroTram"
      }, 
      "when": {
        "begin": "2014-09-22T04:00:00", 
        "end": null
      }, 
      "id": 2704, 
      "why": {
        "url": "http://www.bvg.de/de/Fahrinfo/Verkehrsmeldungen/de/Fahrinfo/Verkehrsmeldungen/Verkehrsmeldung-Detail?id=2704", 
        "reason": "Sperrung wegen Bauarbeiten der BVG"
      }
    }, 
    {
      "where": {
        "start": "S Landsberger Allee", 
        "end": "S Landsberger Allee"
      }, 
      "what": {
        "line": "M8", 
        "medium": "MetroTram"
      }, 
      "when": {
        "begin": "2014-09-22T04:00:00", 
        "end": null
      }, 
      "id": 2700, 
      "why": {
        "url": "http://www.bvg.de/de/Fahrinfo/Verkehrsmeldungen/de/Fahrinfo/Verkehrsmeldungen/Verkehrsmeldung-Detail?id=2700", 
        "reason": "Sperrung wegen Bauarbeiten der BVG"
      }
    }, 
    {
      "where": {
        "start": "S K\u00f6llnische Heide", 
        "end": "Michael-Bohnen-Ring"
      }, 
      "what": {
        "line": "M41", 
        "medium": "MetroBus"
      }, 
      "when": {
        "begin": "2014-05-22T07:30:00", 
        "end": null
      }, 
      "id": 1572, 
      "why": {
        "url": "http://www.bvg.de/de/Fahrinfo/Verkehrsmeldungen/de/Fahrinfo/Verkehrsmeldungen/Verkehrsmeldung-Detail?id=1572", 
        "reason": "Sperrung wegen Bauarbeiten der Wasserbetriebe"
      }
    }, 
    {
      "where": {
        "start": "S Westend", 
        "end": "S+U Zoologischer Garten"
      }, 
      "what": {
        "line": "M45", 
        "medium": "MetroBus"
      }, 
      "when": {
        "begin": "2014-10-12T09:00:00", 
        "end": "2014-10-12T15:00:00"
      }, 
      "id": 2968, 
      "why": {
        "url": "http://www.bvg.de/de/Fahrinfo/Verkehrsmeldungen/de/Fahrinfo/Verkehrsmeldungen/Verkehrsmeldung-Detail?id=2968", 
        "reason": "Sperrung wegen Veranstaltung"
      }
    }, 
    {
      "where": {
        "start": "Europa-Center", 
        "end": "S+U Zoologischer Garten"
      }, 
      "what": {
        "line": "M46", 
        "medium": "MetroBus"
      }, 
      "when": {
        "begin": "2014-10-12T09:00:00", 
        "end": "2014-10-12T15:00:00"
      }, 
      "id": 2966, 
      "why": {
        "url": "http://www.bvg.de/de/Fahrinfo/Verkehrsmeldungen/de/Fahrinfo/Verkehrsmeldungen/Verkehrsmeldung-Detail?id=2966", 
        "reason": "Sperrung wegen Veranstaltung"
      }
    }, 
    {
      "where": {
        "start": "U Theodor-Heuss-Platz", 
        "end": "S+U Zoologischer Garten"
      }, 
      "what": {
        "line": "M49", 
        "medium": "MetroBus"
      }, 
      "when": {
        "begin": "2014-10-12T09:00:00", 
        "end": "2014-10-12T15:00:00"
      }, 
      "id": 2988, 
      "why": {
        "url": "http://www.bvg.de/de/Fahrinfo/Verkehrsmeldungen/de/Fahrinfo/Verkehrsmeldungen/Verkehrsmeldung-Detail?id=2988", 
        "reason": "Sperrung wegen Veranstaltung"
      }
    }, 
    {
      "where": {
        "start": "Karlplatz", 
        "end": "Kleiner Tiergarten"
      }, 
      "what": {
        "line": "TXL", 
        "medium": "Bus"
      }, 
      "when": {
        "begin": "2012-10-15T05:00:00", 
        "end": null
      }, 
      "id": 1612, 
      "why": {
        "url": "http://www.bvg.de/de/Fahrinfo/Verkehrsmeldungen/de/Fahrinfo/Verkehrsmeldungen/Verkehrsmeldung-Detail?id=1612", 
        "reason": "Sperrung wegen Bauarbeiten"
      }
    }, 
    {
      "where": {
        "start": "Platz der Republik", 
        "end": "Gro\u00dfer Stern"
      }, 
      "what": {
        "line": "100", 
        "medium": "Bus"
      }, 
      "when": {
        "begin": "2014-09-09T10:00:00", 
        "end": null
      }, 
      "id": 2238, 
      "why": {
        "url": "http://www.bvg.de/de/Fahrinfo/Verkehrsmeldungen/de/Fahrinfo/Verkehrsmeldungen/Verkehrsmeldung-Detail?id=2238", 
        "reason": "Sperrung wegen Bauarbeiten der Wasserbetriebe"
      }
    }, 
    {
      "where": {
        "start": "Reichstag/Bundestag", 
        "end": "S+U Zoologischer Garten"
      }, 
      "what": {
        "line": "100", 
        "medium": "Bus"
      }, 
      "when": {
        "begin": "2014-10-12T09:00:00", 
        "end": "2014-10-12T15:00:00"
      }, 
      "id": 2976, 
      "why": {
        "url": "http://www.bvg.de/de/Fahrinfo/Verkehrsmeldungen/de/Fahrinfo/Verkehrsmeldungen/Verkehrsmeldung-Detail?id=2976", 
        "reason": "Sperrung wegen Veranstaltung"
      }
    }, 
    {
      "where": {
        "start": "Philharmonie", 
        "end": "S+U Zoologischer Garten"
      }, 
      "what": {
        "line": "200", 
        "medium": "Bus"
      }, 
      "when": {
        "begin": "2014-10-12T09:00:00", 
        "end": "2014-10-12T15:00:00"
      }, 
      "id": 2984, 
      "why": {
        "url": "http://www.bvg.de/de/Fahrinfo/Verkehrsmeldungen/de/Fahrinfo/Verkehrsmeldungen/Verkehrsmeldung-Detail?id=2984", 
        "reason": "Sperrung wegen Veranstaltung"
      }
    }, 
    {
      "where": {
        "start": "S+U Jungfernheide", 
        "end": "S+U Zoologischer Garten"
      }, 
      "what": {
        "line": "X9", 
        "medium": "Express-Bus"
      }, 
      "when": {
        "begin": "2014-10-12T09:00:00", 
        "end": "2014-10-12T15:00:00"
      }, 
      "id": 2964, 
      "why": {
        "url": "http://www.bvg.de/de/Fahrinfo/Verkehrsmeldungen/de/Fahrinfo/Verkehrsmeldungen/Verkehrsmeldung-Detail?id=2964", 
        "reason": "Sperrung wegen Veranstaltung"
      }
    }, 
    {
      "where": {
        "start": "Alt-Sch\u00f6now", 
        "end": "Alt-Sch\u00f6now"
      }, 
      "what": {
        "line": "X10", 
        "medium": "Express-Bus"
      }, 
      "when": {
        "begin": "2013-09-30T04:30:00", 
        "end": null
      }, 
      "id": 1558, 
      "why": {
        "url": "http://www.bvg.de/de/Fahrinfo/Verkehrsmeldungen/de/Fahrinfo/Verkehrsmeldungen/Verkehrsmeldung-Detail?id=1558", 
        "reason": "Sperrung wegen Bauarbeiten"
      }
    }, 
    {
      "where": {
        "start": "U Adenauerplatz", 
        "end": "S+U Zoologischer Garten"
      }, 
      "what": {
        "line": "X10", 
        "medium": "Express-Bus"
      }, 
      "when": {
        "begin": "2014-10-12T09:00:00", 
        "end": "2014-10-12T15:00:00"
      }, 
      "id": 2972, 
      "why": {
        "url": "http://www.bvg.de/de/Fahrinfo/Verkehrsmeldungen/de/Fahrinfo/Verkehrsmeldungen/Verkehrsmeldung-Detail?id=2972", 
        "reason": "Sperrung wegen Veranstaltung"
      }
    }, 
    {
      "where": {
        "start": "Johannisthaler Ch./Rudower Str.", 
        "end": "Stelzenweg"
      }, 
      "what": {
        "line": "X11", 
        "medium": "Express-Bus"
      }, 
      "when": {
        "begin": "2014-04-07T10:00:00", 
        "end": "2014-10-17T13:00:00"
      }, 
      "id": 1554, 
      "why": {
        "url": "http://www.bvg.de/de/Fahrinfo/Verkehrsmeldungen/de/Fahrinfo/Verkehrsmeldungen/Verkehrsmeldung-Detail?id=1554", 
        "reason": "Sperrung wegen Bauarbeiten"
      }
    }, 
    {
      "where": {
        "start": "S Messe Nord/ICC", 
        "end": "S+U Zoologischer Garten"
      }, 
      "what": {
        "line": "X34", 
        "medium": "Express-Bus"
      }, 
      "when": {
        "begin": "2014-10-12T09:00:00", 
        "end": "2014-10-12T15:00:00"
      }, 
      "id": 2980, 
      "why": {
        "url": "http://www.bvg.de/de/Fahrinfo/Verkehrsmeldungen/de/Fahrinfo/Verkehrsmeldungen/Verkehrsmeldung-Detail?id=2980", 
        "reason": "Sperrung wegen Veranstaltung"
      }
    }, 
    {
      "where": {
        "start": "U Hellersdorf", 
        "end": "Landsberger Allee/Blumberger D."
      }, 
      "what": {
        "line": "X54", 
        "medium": "Express-Bus"
      }, 
      "when": {
        "begin": "2014-07-25T08:30:00", 
        "end": null
      }, 
      "id": 1530, 
      "why": {
        "url": "http://www.bvg.de/de/Fahrinfo/Verkehrsmeldungen/de/Fahrinfo/Verkehrsmeldungen/Verkehrsmeldung-Detail?id=1530", 
        "reason": "Sperrung wegen Bauarbeiten"
      }
    }, 
    {
      "where": {
        "start": "U Oranienburger Tor", 
        "end": "Zionskirchplatz"
      }, 
      "what": {
        "line": "12", 
        "medium": "Stra\u00dfenbahn"
      }, 
      "when": {
        "begin": "2012-08-05T04:00:00", 
        "end": null
      }, 
      "id": 1542, 
      "why": {
        "url": "http://www.bvg.de/de/Fahrinfo/Verkehrsmeldungen/de/Fahrinfo/Verkehrsmeldungen/Verkehrsmeldung-Detail?id=1542", 
        "reason": "Linienma\u00dfnahmen"
      }
    }, 
    {
      "where": {
        "start": "S Rummelsburg", 
        "end": "Marktstr."
      }, 
      "what": {
        "line": "21", 
        "medium": "Stra\u00dfenbahn"
      }, 
      "when": {
        "begin": "2014-07-14T04:00:00", 
        "end": "2014-10-18T04:00:00"
      }, 
      "id": 1614, 
      "why": {
        "url": "http://www.bvg.de/de/Fahrinfo/Verkehrsmeldungen/de/Fahrinfo/Verkehrsmeldungen/Verkehrsmeldung-Detail?id=1614", 
        "reason": "Sperrung wegen Bauarbeiten der DB"
      }
    }, 
    {
      "where": {
        "start": "Hirschgarten", 
        "end": "Rahnsdorf/Waldsch\u00e4nke"
      }, 
      "what": {
        "line": "61", 
        "medium": "Stra\u00dfenbahn"
      }, 
      "when": {
        "begin": "2014-10-06T10:00:00", 
        "end": "2014-11-03T02:00:00"
      }, 
      "id": 2828, 
      "why": {
        "url": "http://www.bvg.de/de/Fahrinfo/Verkehrsmeldungen/de/Fahrinfo/Verkehrsmeldungen/Verkehrsmeldung-Detail?id=2828", 
        "reason": "Sperrung wegen Bauarbeiten der BVG"
      }
    }, 
    {
      "where": {
        "start": "Bahnhofstr./Lindenstr.", 
        "end": "M\u00fcggelhm.Str./Wendenschlo\u00dfstr."
      }, 
      "what": {
        "line": "62", 
        "medium": "Stra\u00dfenbahn"
      }, 
      "when": {
        "begin": "2014-10-11T07:50:00", 
        "end": "2014-10-12T15:50:00"
      }, 
      "id": 2922, 
      "why": {
        "url": "http://www.bvg.de/de/Fahrinfo/Verkehrsmeldungen/de/Fahrinfo/Verkehrsmeldungen/Verkehrsmeldung-Detail?id=2922", 
        "reason": "Sperrung wegen Bauarbeiten der BVG"
      }
    }, 
    {
      "where": {
        "start": "Bahnhofstr./Lindenstr.", 
        "end": "Krkhs. K\u00f6penick/S\u00fcdseite"
      }, 
      "what": {
        "line": "67", 
        "medium": "Stra\u00dfenbahn"
      }, 
      "when": {
        "begin": "2014-10-11T07:50:00", 
        "end": "2014-10-12T15:50:00"
      }, 
      "id": 2920, 
      "why": {
        "url": "http://www.bvg.de/de/Fahrinfo/Verkehrsmeldungen/de/Fahrinfo/Verkehrsmeldungen/Verkehrsmeldung-Detail?id=2920", 
        "reason": "Sperrung wegen Bauarbeiten der BVG"
      }
    }, 
    {
      "where": {
        "start": "Helmholtzstr.", 
        "end": "U Konstanzer Str."
      }, 
      "what": {
        "line": "101", 
        "medium": "Bus"
      }, 
      "when": {
        "begin": "2014-10-12T09:00:00", 
        "end": "2014-10-12T15:00:00"
      }, 
      "id": 2978, 
      "why": {
        "url": "http://www.bvg.de/de/Fahrinfo/Verkehrsmeldungen/de/Fahrinfo/Verkehrsmeldungen/Verkehrsmeldung-Detail?id=2978", 
        "reason": "Sperrung wegen Veranstaltung"
      }
    }, 
    {
      "where": {
        "start": "U Hansaplatz", 
        "end": "Nord.Botschaften/Adenauer-Stiftg"
      }, 
      "what": {
        "line": "106", 
        "medium": "Bus"
      }, 
      "when": {
        "begin": "2014-10-12T09:00:00", 
        "end": "2014-10-12T15:00:00"
      }, 
      "id": 2986, 
      "why": {
        "url": "http://www.bvg.de/de/Fahrinfo/Verkehrsmeldungen/de/Fahrinfo/Verkehrsmeldungen/Verkehrsmeldung-Detail?id=2986", 
        "reason": "Sperrung wegen Veranstaltung"
      }
    }, 
    {
      "where": {
        "start": "S+U Zoologischer Garten", 
        "end": "U Jakob-Kaiser-Platz"
      }, 
      "what": {
        "line": "109", 
        "medium": "Bus"
      }, 
      "when": {
        "begin": "2014-10-12T09:00:00", 
        "end": "2014-10-12T15:00:00"
      }, 
      "id": 2982, 
      "why": {
        "url": "http://www.bvg.de/de/Fahrinfo/Verkehrsmeldungen/de/Fahrinfo/Verkehrsmeldungen/Verkehrsmeldung-Detail?id=2982", 
        "reason": "Sperrung wegen Veranstaltung"
      }
    }, 
    {
      "where": {
        "start": "U Adenauerplatz", 
        "end": "S+U Zoologischer Garten"
      }, 
      "what": {
        "line": "110", 
        "medium": "Bus"
      }, 
      "when": {
        "begin": "2014-10-12T09:00:00", 
        "end": "2014-10-12T15:00:00"
      }, 
      "id": 2990, 
      "why": {
        "url": "http://www.bvg.de/de/Fahrinfo/Verkehrsmeldungen/de/Fahrinfo/Verkehrsmeldungen/Verkehrsmeldung-Detail?id=2990", 
        "reason": "Sperrung wegen Veranstaltung"
      }
    }, 
    {
      "where": {
        "start": "Radelandstr./Pflegeheim", 
        "end": "Radelandstr./Pflegeheim"
      }, 
      "what": {
        "line": "130", 
        "medium": "Bus"
      }, 
      "when": {
        "begin": "2014-03-17T04:00:00", 
        "end": null
      }, 
      "id": 1512, 
      "why": {
        "url": "http://www.bvg.de/de/Fahrinfo/Verkehrsmeldungen/de/Fahrinfo/Verkehrsmeldungen/Verkehrsmeldung-Detail?id=1512", 
        "reason": "Sperrung wegen Bauarbeiten"
      }
    }, 
    {
      "where": {
        "start": "Rohrdamm/Wasserwerk", 
        "end": "Quellweg"
      }, 
      "what": {
        "line": "139", 
        "medium": "Bus"
      }, 
      "when": {
        "begin": "2013-06-24T15:00:00", 
        "end": null
      }, 
      "id": 1528, 
      "why": {
        "url": "http://www.bvg.de/de/Fahrinfo/Verkehrsmeldungen/de/Fahrinfo/Verkehrsmeldungen/Verkehrsmeldung-Detail?id=1528", 
        "reason": "Sperrung wegen Bauarbeiten"
      }
    }, 
    {
      "where": {
        "start": "U Osloer Str.", 
        "end": "U Osloer Str."
      }, 
      "what": {
        "line": "150", 
        "medium": "Bus"
      }, 
      "when": {
        "begin": "2014-10-11T08:00:00", 
        "end": "2014-10-13T00:00:00"
      }, 
      "id": 1784, 
      "why": {
        "url": "http://www.bvg.de/de/Fahrinfo/Verkehrsmeldungen/de/Fahrinfo/Verkehrsmeldungen/Verkehrsmeldung-Detail?id=1784", 
        "reason": "Sperrung wegen Bauarbeiten"
      }
    }, 
    {
      "where": {
        "start": "S Sch\u00f6neweide/Sterndamm", 
        "end": "Hasselwerderstr."
      }, 
      "what": {
        "line": "160", 
        "medium": "Bus"
      }, 
      "when": {
        "begin": "2014-04-27T04:00:00", 
        "end": null
      }, 
      "id": 1564, 
      "why": {
        "url": "http://www.bvg.de/de/Fahrinfo/Verkehrsmeldungen/de/Fahrinfo/Verkehrsmeldungen/Verkehrsmeldung-Detail?id=1564", 
        "reason": "Sperrung wegen Bauarbeiten der DB"
      }
    }, 
    {
      "where": {
        "start": "S Spindlersfeld", 
        "end": "Bruno-B\u00fcrgel-Weg"
      }, 
      "what": {
        "line": "167", 
        "medium": "Bus"
      }, 
      "when": {
        "begin": "2014-08-10T20:00:00", 
        "end": null
      }, 
      "id": 1384, 
      "why": {
        "url": "http://www.bvg.de/de/Fahrinfo/Verkehrsmeldungen/de/Fahrinfo/Verkehrsmeldungen/Verkehrsmeldung-Detail?id=1384", 
        "reason": "Sperrung wegen Bauarbeiten der DB"
      }
    }, 
    {
      "where": {
        "start": "Friedlander Stra\u00dfe", 
        "end": "Bruno-B\u00fcrgel-Weg"
      }, 
      "what": {
        "line": "167", 
        "medium": "Bus"
      }, 
      "when": {
        "begin": "2014-08-10T20:00:00", 
        "end": "2014-12-31T00:00:00"
      }, 
      "id": 2121, 
      "why": {
        "url": "http://www.bvg.de/de/Fahrinfo/Verkehrsmeldungen/de/Fahrinfo/Verkehrsmeldungen/Verkehrsmeldung-Detail?id=2121", 
        "reason": "Abweichende Linienf\u00fchrung in der Oberspreestra\u00dfe"
      }
    }, 
    {
      "where": {
        "start": "Bruno-B\u00fcrgel-Weg", 
        "end": "Friedlander Str."
      }, 
      "what": {
        "line": "167", 
        "medium": "Bus"
      }, 
      "when": {
        "begin": "2014-10-07T06:30:00", 
        "end": null
      }, 
      "id": 2916, 
      "why": {
        "url": "http://www.bvg.de/de/Fahrinfo/Verkehrsmeldungen/de/Fahrinfo/Verkehrsmeldungen/Verkehrsmeldung-Detail?id=2916", 
        "reason": "Sperrung wegen Bauarbeiten"
      }
    }, 
    {
      "where": {
        "start": "Reichartstr.", 
        "end": "Teltow, Einkaufszentrum Oderstr."
      }, 
      "what": {
        "line": "184", 
        "medium": "Bus"
      }, 
      "when": {
        "begin": "2013-09-30T04:30:00", 
        "end": null
      }, 
      "id": 1516, 
      "why": {
        "url": "http://www.bvg.de/de/Fahrinfo/Verkehrsmeldungen/de/Fahrinfo/Verkehrsmeldungen/Verkehrsmeldung-Detail?id=1516", 
        "reason": "Sperrung wegen Bauarbeiten"
      }
    }, 
    {
      "where": {
        "start": "Rathaus Tempelhof", 
        "end": "Friedrich-Wilhelm-Str."
      }, 
      "what": {
        "line": "184", 
        "medium": "Bus"
      }, 
      "when": {
        "begin": "2014-09-15T07:00:00", 
        "end": null
      }, 
      "id": 2124, 
      "why": {
        "url": "http://www.bvg.de/de/Fahrinfo/Verkehrsmeldungen/de/Fahrinfo/Verkehrsmeldungen/Verkehrsmeldung-Detail?id=2124", 
        "reason": "Sperrung wegen Bauarbeiten"
      }
    }, 
    {
      "where": {
        "start": "Alt-Moabit/Rathenower Str.", 
        "end": "L\u00fctzowplatz"
      }, 
      "what": {
        "line": "187", 
        "medium": "Bus"
      }, 
      "when": {
        "begin": "2014-10-12T09:00:00", 
        "end": "2014-10-12T15:00:00"
      }, 
      "id": 2994, 
      "why": {
        "url": "http://www.bvg.de/de/Fahrinfo/Verkehrsmeldungen/de/Fahrinfo/Verkehrsmeldungen/Verkehrsmeldung-Detail?id=2994", 
        "reason": "Sperrung wegen Veranstaltung"
      }
    }, 
    {
      "where": {
        "start": "S Ostkreuz", 
        "end": "W\u00f6nnichstr."
      }, 
      "what": {
        "line": "194", 
        "medium": "Bus"
      }, 
      "when": {
        "begin": "2014-06-30T04:00:00", 
        "end": "2014-10-20T04:00:00"
      }, 
      "id": 1620, 
      "why": {
        "url": "http://www.bvg.de/de/Fahrinfo/Verkehrsmeldungen/de/Fahrinfo/Verkehrsmeldungen/Verkehrsmeldung-Detail?id=1620", 
        "reason": "Sperrung wegen Bauarbeiten der DB"
      }
    }, 
    {
      "where": {
        "start": "Landsberger Allee/Blumberger D.", 
        "end": "Spremberger Str."
      }, 
      "what": {
        "line": "197", 
        "medium": "Bus"
      }, 
      "when": {
        "begin": "2014-07-25T08:30:00", 
        "end": null
      }, 
      "id": 1532, 
      "why": {
        "url": "http://www.bvg.de/de/Fahrinfo/Verkehrsmeldungen/de/Fahrinfo/Verkehrsmeldungen/Verkehrsmeldung-Detail?id=1532", 
        "reason": "Sperrung wegen Bauarbeiten"
      }
    }, 
    {
      "where": {
        "start": "S Nordbahnhof/Gartenstr.", 
        "end": "Invalidenpark"
      }, 
      "what": {
        "line": "245", 
        "medium": "Bus"
      }, 
      "when": {
        "begin": "2014-07-02T04:00:00", 
        "end": null
      }, 
      "id": 1418, 
      "why": {
        "url": "http://www.bvg.de/de/Fahrinfo/Verkehrsmeldungen/de/Fahrinfo/Verkehrsmeldungen/Verkehrsmeldung-Detail?id=1418", 
        "reason": "Sperrung wegen Bauarbeiten"
      }
    }, 
    {
      "where": {
        "start": "Marchbr\u00fccke", 
        "end": "S+U Zoologischer Garten"
      }, 
      "what": {
        "line": "245", 
        "medium": "Bus"
      }, 
      "when": {
        "begin": "2014-10-12T09:00:00", 
        "end": "2014-10-12T15:00:00"
      }, 
      "id": 2974, 
      "why": {
        "url": "http://www.bvg.de/de/Fahrinfo/Verkehrsmeldungen/de/Fahrinfo/Verkehrsmeldungen/Verkehrsmeldung-Detail?id=2974", 
        "reason": "Sperrung wegen Veranstaltung"
      }
    }, 
    {
      "where": {
        "start": "S+U Hermannstr./Silbersteinstr.", 
        "end": "Neuk\u00f6llnische Al./Forsthausallee"
      }, 
      "what": {
        "line": "246", 
        "medium": "Bus"
      }, 
      "when": {
        "begin": "2014-01-17T05:00:00", 
        "end": null
      }, 
      "id": 1574, 
      "why": {
        "url": "http://www.bvg.de/de/Fahrinfo/Verkehrsmeldungen/de/Fahrinfo/Verkehrsmeldungen/Verkehrsmeldung-Detail?id=1574", 
        "reason": "Sperrung wegen Bauarbeiten"
      }
    }, 
    {
      "where": {
        "start": "Lietzenburger Str./Uhlandstr.", 
        "end": "S+U Zoologischer Garten"
      }, 
      "what": {
        "line": "249", 
        "medium": "Bus"
      }, 
      "when": {
        "begin": "2014-10-12T09:00:00", 
        "end": "2014-10-12T15:00:00"
      }, 
      "id": 2992, 
      "why": {
        "url": "http://www.bvg.de/de/Fahrinfo/Verkehrsmeldungen/de/Fahrinfo/Verkehrsmeldungen/Verkehrsmeldung-Detail?id=2992", 
        "reason": "Sperrung wegen Veranstaltung"
      }
    }, 
    {
      "where": {
        "start": "S Buch", 
        "end": "Lindenberg, Bernauer Str."
      }, 
      "what": {
        "line": "259", 
        "medium": "Bus"
      }, 
      "when": {
        "begin": "2014-08-24T04:00:00", 
        "end": null
      }, 
      "id": 1470, 
      "why": {
        "url": "http://www.bvg.de/de/Fahrinfo/Verkehrsmeldungen/de/Fahrinfo/Verkehrsmeldungen/Verkehrsmeldung-Detail?id=1470", 
        "reason": "Linienma\u00dfnahmen"
      }
    }, 
    {
      "where": {
        "start": "S Buch", 
        "end": "Schwanebeck, Neue K\u00e4rntner Str."
      }, 
      "what": {
        "line": "259", 
        "medium": "Bus"
      }, 
      "when": {
        "begin": "2014-09-30T04:00:00", 
        "end": null
      }, 
      "id": 2854, 
      "why": {
        "url": "http://www.bvg.de/de/Fahrinfo/Verkehrsmeldungen/de/Fahrinfo/Verkehrsmeldungen/Verkehrsmeldung-Detail?id=2854", 
        "reason": "Sperrung wegen Bauarbeiten"
      }
    }, 
    {
      "where": {
        "start": "S+U Hermannstr.", 
        "end": "S Pl\u00e4nterwald"
      }, 
      "what": {
        "line": "277", 
        "medium": "Bus"
      }, 
      "when": {
        "begin": "2014-01-17T05:00:00", 
        "end": null
      }, 
      "id": 1386, 
      "why": {
        "url": "http://www.bvg.de/de/Fahrinfo/Verkehrsmeldungen/de/Fahrinfo/Verkehrsmeldungen/Verkehrsmeldung-Detail?id=1386", 
        "reason": "Sperrung wegen Bauarbeiten"
      }
    }, 
    {
      "where": {
        "start": "Schwarzmeerstr.", 
        "end": "Lincolnstr./Einbecker Str."
      }, 
      "what": {
        "line": "296", 
        "medium": "Bus"
      }, 
      "when": {
        "begin": "2014-09-16T09:00:00", 
        "end": null
      }, 
      "id": 2014, 
      "why": {
        "url": "http://www.bvg.de/de/Fahrinfo/Verkehrsmeldungen/de/Fahrinfo/Verkehrsmeldungen/Verkehrsmeldung-Detail?id=2014", 
        "reason": "Sperrung wegen Bauarbeiten der Wasserbetriebe"
      }
    }, 
    {
      "where": {
        "start": "Mollwitzstr.", 
        "end": "U Wilmersdorfer Str."
      }, 
      "what": {
        "line": "309", 
        "medium": "Bus"
      }, 
      "when": {
        "begin": "2014-10-12T09:00:00", 
        "end": "2014-10-12T15:00:00"
      }, 
      "id": 2970, 
      "why": {
        "url": "http://www.bvg.de/de/Fahrinfo/Verkehrsmeldungen/de/Fahrinfo/Verkehrsmeldungen/Verkehrsmeldung-Detail?id=2970", 
        "reason": "Sperrung wegen Veranstaltung"
      }
    }, 
    {
      "where": {
        "start": "S Buch", 
        "end": "Campus Buch"
      }, 
      "what": {
        "line": "353", 
        "medium": "Bus"
      }, 
      "when": {
        "begin": "2014-08-24T04:00:00", 
        "end": null
      }, 
      "id": 1474, 
      "why": {
        "url": "http://www.bvg.de/de/Fahrinfo/Verkehrsmeldungen/de/Fahrinfo/Verkehrsmeldungen/Verkehrsmeldung-Detail?id=1474", 
        "reason": "Linienma\u00dfnahmen"
      }
    }, 
    {
      "where": {
        "start": "S Ahrensfelde", 
        "end": "Mehrow, Kirche"
      }, 
      "what": {
        "line": "390", 
        "medium": "Bus"
      }, 
      "when": {
        "begin": "2014-08-24T04:00:00", 
        "end": null
      }, 
      "id": 1476, 
      "why": {
        "url": "http://www.bvg.de/de/Fahrinfo/Verkehrsmeldungen/de/Fahrinfo/Verkehrsmeldungen/Verkehrsmeldung-Detail?id=1476", 
        "reason": "Linienma\u00dfnahmen"
      }
    }, 
    {
      "where": {
        "start": "S+U Pankow", 
        "end": "Sch\u00f6nhauser Allee/Bornholmer Str"
      }, 
      "what": {
        "line": "N2", 
        "medium": "Nachtbus"
      }, 
      "when": {
        "begin": "2014-02-17T23:00:00", 
        "end": null
      }, 
      "id": 1388, 
      "why": {
        "url": "http://www.bvg.de/de/Fahrinfo/Verkehrsmeldungen/de/Fahrinfo/Verkehrsmeldungen/Verkehrsmeldung-Detail?id=1388", 
        "reason": "Sperrung wegen Bauarbeiten"
      }
    }, 
    {
      "where": {
        "start": "Kaiser-Friedrich-Str./Kantstr.", 
        "end": "U Richard-Wagner-Platz"
      }, 
      "what": {
        "line": "N7", 
        "medium": "Nachtbus"
      }, 
      "when": {
        "begin": "2013-03-26T00:01:00", 
        "end": null
      }, 
      "id": 1544, 
      "why": {
        "url": "http://www.bvg.de/de/Fahrinfo/Verkehrsmeldungen/de/Fahrinfo/Verkehrsmeldungen/Verkehrsmeldung-Detail?id=1544", 
        "reason": "Sperrung wegen Bauarbeiten der BVG"
      }
    }, 
    {
      "where": {
        "start": "U Rathaus Neuk\u00f6lln", 
        "end": "S+U Neuk\u00f6lln"
      }, 
      "what": {
        "line": "N7", 
        "medium": "Nachtbus"
      }, 
      "when": {
        "begin": "2014-08-04T23:00:00", 
        "end": null
      }, 
      "id": 1618, 
      "why": {
        "url": "http://www.bvg.de/de/Fahrinfo/Verkehrsmeldungen/de/Fahrinfo/Verkehrsmeldungen/Verkehrsmeldung-Detail?id=1618", 
        "reason": "Sperrung wegen Bauarbeiten der BVG"
      }
    }, 
    {
      "where": {
        "start": "S+U Rathaus Steglitz", 
        "end": "S+U Rathaus Steglitz"
      }, 
      "what": {
        "line": "N9", 
        "medium": "Nachtbus"
      }, 
      "when": {
        "begin": "2013-02-19T00:00:00", 
        "end": null
      }, 
      "id": 1568, 
      "why": {
        "url": "http://www.bvg.de/de/Fahrinfo/Verkehrsmeldungen/de/Fahrinfo/Verkehrsmeldungen/Verkehrsmeldung-Detail?id=1568", 
        "reason": "Sperrung wegen Bauarbeiten der Wasserbetriebe"
      }
    }, 
    {
      "where": {
        "start": "S Potsdam Hauptbahnhof", 
        "end": "Platz der Einheit/Bildungsforum"
      }, 
      "what": {
        "line": "N16", 
        "medium": "Nachtbus"
      }, 
      "when": {
        "begin": "2014-10-06T20:00:00", 
        "end": "2014-10-20T05:00:00"
      }, 
      "id": 2864, 
      "why": {
        "url": "http://www.bvg.de/de/Fahrinfo/Verkehrsmeldungen/de/Fahrinfo/Verkehrsmeldungen/Verkehrsmeldung-Detail?id=2864", 
        "reason": "Sperrung wegen Bauarbeiten"
      }
    }, 
    {
      "where": {
        "start": "S Nordbahnhof", 
        "end": "Pappelplatz"
      }, 
      "what": {
        "line": "N40", 
        "medium": "Nachtbus"
      }, 
      "when": {
        "begin": "2014-07-02T04:00:00", 
        "end": null
      }, 
      "id": 1550, 
      "why": {
        "url": "http://www.bvg.de/de/Fahrinfo/Verkehrsmeldungen/de/Fahrinfo/Verkehrsmeldungen/Verkehrsmeldung-Detail?id=1550", 
        "reason": "Sperrung wegen Bauarbeiten"
      }
    }, 
    {
      "where": {
        "start": "S Nordbahnhof", 
        "end": "Brunnenstr./Invalidenstr."
      }, 
      "what": {
        "line": "N40", 
        "medium": "Nachtbus"
      }, 
      "when": {
        "begin": "2014-09-30T00:30:00", 
        "end": null
      }, 
      "id": 2742, 
      "why": {
        "url": "http://www.bvg.de/de/Fahrinfo/Verkehrsmeldungen/de/Fahrinfo/Verkehrsmeldungen/Verkehrsmeldung-Detail?id=2742", 
        "reason": "Sperrung wegen Bauarbeiten der BVG"
      }
    }, 
    {
      "where": {
        "start": "Schwarzmeerstr.", 
        "end": "Lincolnstr./Einbecker Str."
      }, 
      "what": {
        "line": "N50", 
        "medium": "Nachtbus"
      }, 
      "when": {
        "begin": "2014-09-16T09:00:00", 
        "end": null
      }, 
      "id": 2012, 
      "why": {
        "url": "http://www.bvg.de/de/Fahrinfo/Verkehrsmeldungen/de/Fahrinfo/Verkehrsmeldungen/Verkehrsmeldung-Detail?id=2012", 
        "reason": "Sperrung wegen Bauarbeiten der Wasserbetriebe"
      }
    }, 
    {
      "where": {
        "start": "S Sch\u00f6neweide", 
        "end": "S Sch\u00f6neweide/Sterndamm"
      }, 
      "what": {
        "line": "N67", 
        "medium": "Nachtbus"
      }, 
      "when": {
        "begin": "2014-04-27T04:00:00", 
        "end": null
      }, 
      "id": 1390, 
      "why": {
        "url": "http://www.bvg.de/de/Fahrinfo/Verkehrsmeldungen/de/Fahrinfo/Verkehrsmeldungen/Verkehrsmeldung-Detail?id=1390", 
        "reason": "Sperrung wegen Bauarbeiten der DB"
      }
    }, 
    {
      "where": {
        "start": "S Ostkreuz", 
        "end": "L\u00fcckstr./Weitlingstr."
      }, 
      "what": {
        "line": "N94", 
        "medium": "Nachtbus"
      }, 
      "when": {
        "begin": "2014-06-30T04:00:00", 
        "end": "2014-10-20T04:00:00"
      }, 
      "id": 1616, 
      "why": {
        "url": "http://www.bvg.de/de/Fahrinfo/Verkehrsmeldungen/de/Fahrinfo/Verkehrsmeldungen/Verkehrsmeldung-Detail?id=1616", 
        "reason": "Sperrung wegen Bauarbeiten der DB"
      }
    }
  ], 
  "source_url": "http://www.bvg.de/de/Fahrinfo/Verkehrsmeldungen"
}
```

## Installation

Die App läuft unter Python und nutzt [Flask](http://flask.pocoo.org) und [Beautiful Soup](http://www.crummy.com/software/BeautifulSoup/). Die Installation ist einfach:

    virtualenv venv
    source venv/bin/activate
    pip install -r requirements.txt

## Danksagung

Die Daten kommen von den [Berliner Verkehrsbetrieben](http://www.bvg.de/de/).
