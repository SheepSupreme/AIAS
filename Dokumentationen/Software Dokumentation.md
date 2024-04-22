---
excalidraw-plugin: parsed
tags:
  - excalidraw
---
# Software
Die Software zur Ansteuerung des Schrittmotors besteht aus einem Hauptprogramm, in dem die serielle Kommunikation und die Befehlsausführung stattfinden. Alle notwendigen Unterprogramme zur Ansteuerung sind in einer speziell dafür geschriebenen Klasse enthalten. 
Diese Klasse ist in eine Header-Datei und eine .cpp-Datei unterteilt, um die Übersichtlichkeit zu verbessern.

==⚠  Switch to EXCALIDRAW VIEW in the MORE OPTIONS menu of this document. ⚠==


# Text Elements
Controller ^usSznX0d

Endschalter ^ItrOS45l

Platform ^MACu6yOQ

Normal Closed ^8yUq8XaX

Closed Loop  ^Ns8RnahQ

Controller ^xDQBA3ik

Schritt
Befehl ^Eyr1dcBL

Encoder ^iwynSGvF

Misst Rotor
Rotation ^kwAPI4WX

übergibt Messwert
an Controller ^kbmbhhvj

LOW ^4iHOs8VW

Controller ^G5MQLGYC

Endschalter ^POx9LDvr

Platform ^JP7jBBQa

HIGH ^elVAzUEU

Controller ^WOI4jE6u

Endschalter ^68kVP7XM

LOW ^JBLerr5o

Normal Open ^7GDFDQSJ

Platform ^QSSEQLGQ

bei Drahtbruch ^XCRSBcAC

fällt auf ^PefhRZpt

fällt nicht
auf ^NvB5eDfG

DRV 8825 ^7DWjcZPt

A ^rNENdTVy

Paket hinzufügen ^eucYAiYg

Haupt
Programm ^MbMNdj6L

SQL Datenbank ^s0b7IRmx

Arduino ^tHKbBkiq

Anfrage der Paketparameter ^07t0Ux5A

Übergabe der
Parameter ^Dfz58J30

GUI ^lT2mLICk

QR-Code Scanner ^MtnSI1s9

Einlesen der
Paket-ID ^0mWuzhvF

Erkennung des Pakets ^87L0f9Hv

Erstellen eines Objektes für den Timer des Pakets ^WockAW8N

LEDs ^lwNZtne4

Indikator für Paket Einlagerung ^276Ci32i

Chronologischer Ablauf ^v1lvIjmf

Auswurf des Pakets ^rEbcWyXd

Motoren ^OLJwWnoQ

Ansteuerung für Ausgabe (DRV8825) ^ybbLxPvq

Befehl für Ausgabe ^2ZvecqaU

Erkennung des Pakets ^wA5W8k1o

serielle Schnittstelle
(USB) ^ejGw5pLl

Mit dem QR-Code-Scanner wird die ID des Pakets eingelesen und über die serielle Schnittstelle an das
Hauptprogramm(Computer) weiter gegeben. Von dort aus wird eine Anfrage an die SQL Datenbank 
für die eingelesene ID gestartet. Die Datenbank antwortet mit allen Parameter(Eigenschaften) des Paketes. 
  ^6sHQiV6l

Indikator für Paket Einlagerung ^Z0mODqRe

Im Hauptprogramm wird ein Objekt für jedes Paket erstellt, dass die Parameter der Datenbank übernimmt.
Jedes Paket hat eine mit der Fälligkeitsdatum berechnete Ablaufzeit, nach der sortiert und eingelagert wird. ^8n0EDKX1

Das Hauptprogramm bestimmt das Regal in dem das Paket eingelagert werden soll um einen möglichst effizienten
Ablauf des Prozesses zu ermöglichen. Damit das Paket richtig eingelagert wird,
wird mithilfe von an den Regalen installierten LEDs das richtige Regal gekennzeichnet. ^KQ3XXUQG

Erstellen eines Objektes für den Timer des Pakets ^sgV9RFgA

Auswurf des Pakets ^LMazcfF7

Mit dem Auswurfbefehl kann die gewollte Anzahl an Pakete ausgeworfen werden. Die Reihenfolge,
in der die Pakete ausgeworfen werden, beginnt mit dem Paket, das die kürzeste Ablaufzeit hat 
und steigt dann auf. ^YVmCP9bq

µC ^jPodHZg9

Verarbeitung und
Serialisierung
gelesener Informationen  ^cDRTlMVe

QR-Code Scanner Modul ^Ppfp6eb6

Arduino ^uU2DDshE

Schnittstelle
seriell ^e32RdFWR

Hauptprogramm
main.cpp ^sorTEFRQ

stepper.h ^f8iKvtjv

stepper.cpp ^lnKIQrGQ

Schrittmotor Klasse ^Kfrg63UU

Initialisierung ^SeGSs16V

Deklaration ^hCxwTSH0

Instanziierung ^Q6NNuIQH

Kamera ^Wk7X7cFH

display.h ^3aSo0tyO

display.cpp ^VYcXZTSl

Display Klasse ^xc298Qst

Initialisierung ^LhLTNBvh

Deklaration ^tRktdXxC

Instanziierung ^TcjnFJP8


# Embedded files
2d6726517657bd9d21cbf16bbf7b445af4101c78: $$I_{Max} = I_{Mess} * 0.7$$

%%
# Drawing
```json
{
	"type": "excalidraw",
	"version": 2,
	"source": "https://github.com/zsviczian/obsidian-excalidraw-plugin/releases/tag/2.0.20",
	"elements": [
		{
			"type": "rectangle",
			"version": 384,
			"versionNonce": 1606399961,
			"isDeleted": false,
			"id": "8-EKURg1TI7bN6K2cfZo1",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "dashed",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 4372.347628767799,
			"y": -920.2201036448416,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 549.6706530209902,
			"height": 593.7913650693112,
			"seed": 993132058,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 3
			},
			"boundElements": [],
			"updated": 1713771502122,
			"link": null,
			"locked": false
		},
		{
			"type": "line",
			"version": 336,
			"versionNonce": 1628688282,
			"isDeleted": false,
			"id": "lkJRPwRMOc3swYUoxdqm9",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "dashed",
			"roughness": 1,
			"opacity": 50,
			"angle": 0,
			"x": 113.72062522694284,
			"y": -97.5351369944542,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 529.4261767454741,
			"height": 1.9994468718880967,
			"seed": 1902846142,
			"groupIds": [],
			"frameId": "IagBYhze8sjgDkoZ4gj5i",
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1712826540973,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					529.4261767454741,
					1.9994468718880967
				]
			]
		},
		{
			"type": "rectangle",
			"version": 1286,
			"versionNonce": 1183190790,
			"isDeleted": false,
			"id": "nO0C3FApY5d4VdigDiaru",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 206.34210305763295,
			"y": 27.38559132964727,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 59.04901772977437,
			"height": 61.29511560443,
			"seed": 1322469026,
			"groupIds": [
				"iYK-n4O5PXvMKUQNIN4Vr"
			],
			"frameId": "IagBYhze8sjgDkoZ4gj5i",
			"roundness": null,
			"boundElements": [],
			"updated": 1712826540973,
			"link": null,
			"locked": false
		},
		{
			"type": "rectangle",
			"version": 1218,
			"versionNonce": 1475005530,
			"isDeleted": false,
			"id": "SeRcrCmJIIyeEknyF5hNj",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 219.5346839669002,
			"y": 43.43875667413252,
			"strokeColor": "#000000",
			"backgroundColor": "black",
			"width": 29.78586167252632,
			"height": 31.873793322238196,
			"seed": 1136009826,
			"groupIds": [
				"iYK-n4O5PXvMKUQNIN4Vr"
			],
			"frameId": "IagBYhze8sjgDkoZ4gj5i",
			"roundness": null,
			"boundElements": [],
			"updated": 1712826540973,
			"link": null,
			"locked": false
		},
		{
			"type": "line",
			"version": 1034,
			"versionNonce": 171589190,
			"isDeleted": false,
			"id": "PphCZ-0BK5uf7AyY3zowX",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 220.62805763891598,
			"y": 11.909369972746646,
			"strokeColor": "#000000",
			"backgroundColor": "black",
			"width": 0.7515244268512646,
			"height": 16.193175852278152,
			"seed": 390563362,
			"groupIds": [
				"iYK-n4O5PXvMKUQNIN4Vr"
			],
			"frameId": "IagBYhze8sjgDkoZ4gj5i",
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1712826540973,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					-0.7515244268512646,
					16.193175852278152
				]
			]
		},
		{
			"type": "line",
			"version": 1075,
			"versionNonce": 2084843802,
			"isDeleted": false,
			"id": "zxNmfq24J2AaQqL4czMw0",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 254.7911643575691,
			"y": 11.584109986343975,
			"strokeColor": "#000000",
			"backgroundColor": "black",
			"width": 0.7515244268512646,
			"height": 16.193175852278152,
			"seed": 41316834,
			"groupIds": [
				"iYK-n4O5PXvMKUQNIN4Vr"
			],
			"frameId": "IagBYhze8sjgDkoZ4gj5i",
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1712826540973,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					-0.7515244268512646,
					16.193175852278152
				]
			]
		},
		{
			"type": "line",
			"version": 1064,
			"versionNonce": 2116453766,
			"isDeleted": false,
			"id": "uQaTtHuK3FLbhaQMpA0Tw",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 238.85874202567848,
			"y": 12.268325417856914,
			"strokeColor": "#000000",
			"backgroundColor": "black",
			"width": 0.7515244268512646,
			"height": 16.193175852278152,
			"seed": 1213326754,
			"groupIds": [
				"iYK-n4O5PXvMKUQNIN4Vr"
			],
			"frameId": "IagBYhze8sjgDkoZ4gj5i",
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1712826540973,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					-0.7515244268512646,
					16.193175852278152
				]
			]
		},
		{
			"type": "line",
			"version": 1119,
			"versionNonce": 1100152282,
			"isDeleted": false,
			"id": "3sPyMiyCJyCfE1KJJvftf",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 222.3243834710403,
			"y": 90.41334228437634,
			"strokeColor": "#000000",
			"backgroundColor": "black",
			"width": 0.7515244268512646,
			"height": 16.193175852278152,
			"seed": 1913184610,
			"groupIds": [
				"iYK-n4O5PXvMKUQNIN4Vr"
			],
			"frameId": "IagBYhze8sjgDkoZ4gj5i",
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1712826540973,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					-0.7515244268512646,
					16.193175852278152
				]
			]
		},
		{
			"type": "line",
			"version": 1091,
			"versionNonce": 327673030,
			"isDeleted": false,
			"id": "sdMWTxv-wqVr83m15F_vK",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 235.29533579878958,
			"y": 90.84963442745973,
			"strokeColor": "#000000",
			"backgroundColor": "black",
			"width": 0.7515244268512646,
			"height": 16.193175852278152,
			"seed": 183133474,
			"groupIds": [
				"iYK-n4O5PXvMKUQNIN4Vr"
			],
			"frameId": "IagBYhze8sjgDkoZ4gj5i",
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1712826540973,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					-0.7515244268512646,
					16.193175852278152
				]
			]
		},
		{
			"type": "line",
			"version": 1066,
			"versionNonce": 887763610,
			"isDeleted": false,
			"id": "x1eTEE9-zHIvRBQKs8cMB",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 251.04086433601438,
			"y": 89.98420820141794,
			"strokeColor": "#000000",
			"backgroundColor": "black",
			"width": 0.7515244268512646,
			"height": 16.193175852278152,
			"seed": 1550151906,
			"groupIds": [
				"iYK-n4O5PXvMKUQNIN4Vr"
			],
			"frameId": "IagBYhze8sjgDkoZ4gj5i",
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1712826540973,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					-0.7515244268512646,
					16.193175852278152
				]
			]
		},
		{
			"type": "line",
			"version": 1173,
			"versionNonce": 201022470,
			"isDeleted": false,
			"id": "iSDNsraYTDI9kCiIIjvBw",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 1.5619589856492286,
			"x": 274.56294885868317,
			"y": 36.63431426157243,
			"strokeColor": "#000000",
			"backgroundColor": "black",
			"width": 0.7515244268512646,
			"height": 16.193175852278152,
			"seed": 705234082,
			"groupIds": [
				"iYK-n4O5PXvMKUQNIN4Vr"
			],
			"frameId": "IagBYhze8sjgDkoZ4gj5i",
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1712826540973,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					-0.7515244268512646,
					16.193175852278152
				]
			]
		},
		{
			"type": "line",
			"version": 1220,
			"versionNonce": 1224527706,
			"isDeleted": false,
			"id": "W_VRUUbwZG_O38tyFFAhl",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 1.5619589856492286,
			"x": 274.9794026095577,
			"y": 51.798721769485184,
			"strokeColor": "#000000",
			"backgroundColor": "black",
			"width": 0.7515244268512646,
			"height": 16.193175852278152,
			"seed": 1837375586,
			"groupIds": [
				"iYK-n4O5PXvMKUQNIN4Vr"
			],
			"frameId": "IagBYhze8sjgDkoZ4gj5i",
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1712826540973,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					-0.7515244268512646,
					16.193175852278152
				]
			]
		},
		{
			"type": "line",
			"version": 1225,
			"versionNonce": 1836968774,
			"isDeleted": false,
			"id": "US-Wzz9YRI9-s23zak3Oe",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 1.5619589856492286,
			"x": 275.8086958520445,
			"y": 66.45827546696208,
			"strokeColor": "#000000",
			"backgroundColor": "black",
			"width": 0.7515244268512646,
			"height": 16.193175852278152,
			"seed": 312853538,
			"groupIds": [
				"iYK-n4O5PXvMKUQNIN4Vr"
			],
			"frameId": "IagBYhze8sjgDkoZ4gj5i",
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1712826540973,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					-0.7515244268512646,
					16.193175852278152
				]
			]
		},
		{
			"type": "line",
			"version": 1216,
			"versionNonce": 572380186,
			"isDeleted": false,
			"id": "ifxx2gbMhEZz5bvmwwrl7",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 1.5619589856492286,
			"x": 197.05885191618214,
			"y": 34.18539890408559,
			"strokeColor": "#000000",
			"backgroundColor": "black",
			"width": 0.7515244268512646,
			"height": 16.193175852278152,
			"seed": 861728738,
			"groupIds": [
				"iYK-n4O5PXvMKUQNIN4Vr"
			],
			"frameId": "IagBYhze8sjgDkoZ4gj5i",
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1712826540973,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					-0.7515244268512646,
					16.193175852278152
				]
			]
		},
		{
			"type": "line",
			"version": 1241,
			"versionNonce": 1986826886,
			"isDeleted": false,
			"id": "3TEtXZAzlt435kxFNWihq",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 1.5619589856492286,
			"x": 198.24276045765114,
			"y": 47.842641492851754,
			"strokeColor": "#000000",
			"backgroundColor": "black",
			"width": 0.7515244268512646,
			"height": 16.193175852278152,
			"seed": 1404609442,
			"groupIds": [
				"iYK-n4O5PXvMKUQNIN4Vr"
			],
			"frameId": "IagBYhze8sjgDkoZ4gj5i",
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1712826540973,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					-0.7515244268512646,
					16.193175852278152
				]
			]
		},
		{
			"type": "line",
			"version": 1218,
			"versionNonce": 1648378074,
			"isDeleted": false,
			"id": "-HKu6nzlc9smrYZUH-0vm",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 1.5619589856492286,
			"x": 197.18987465522528,
			"y": 64.57206746919408,
			"strokeColor": "#000000",
			"backgroundColor": "black",
			"width": 0.7515244268512646,
			"height": 16.193175852278152,
			"seed": 501735266,
			"groupIds": [
				"iYK-n4O5PXvMKUQNIN4Vr"
			],
			"frameId": "IagBYhze8sjgDkoZ4gj5i",
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1712826540973,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					-0.7515244268512646,
					16.193175852278152
				]
			]
		},
		{
			"type": "rectangle",
			"version": 267,
			"versionNonce": 293884358,
			"isDeleted": false,
			"id": "25mdWAF4rzKa1UN_NRbEZ",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 153.50647476819722,
			"y": -1.714076086152943,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 167.30390908350887,
			"height": 163.43022337167497,
			"seed": 2132602594,
			"groupIds": [],
			"frameId": "IagBYhze8sjgDkoZ4gj5i",
			"roundness": {
				"type": 3
			},
			"boundElements": [],
			"updated": 1712826540973,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 175,
			"versionNonce": 1962349978,
			"isDeleted": false,
			"id": "usSznX0d",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 161.19510606986216,
			"y": 113.24779928354894,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 151.40625,
			"height": 31.019799299007236,
			"seed": 372101602,
			"groupIds": [],
			"frameId": "IagBYhze8sjgDkoZ4gj5i",
			"roundness": null,
			"boundElements": [],
			"updated": 1712826540973,
			"link": null,
			"locked": false,
			"fontSize": 25.8498327491727,
			"fontFamily": 3,
			"text": "Controller",
			"rawText": "Controller",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "Controller",
			"lineHeight": 1.2,
			"baseline": 25
		},
		{
			"type": "line",
			"version": 578,
			"versionNonce": 1239558406,
			"isDeleted": false,
			"id": "B2K9Bh5ZBTQCB8Xopi8JV",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 941.0077343698662,
			"y": 86.56705795800366,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 212.1166214516586,
			"height": 2.6451578865729743,
			"seed": 125334206,
			"groupIds": [],
			"frameId": "IagBYhze8sjgDkoZ4gj5i",
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1712826540973,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					212.1166214516586,
					2.6451578865729743
				]
			]
		},
		{
			"type": "rectangle",
			"version": 320,
			"versionNonce": 1534415450,
			"isDeleted": false,
			"id": "xh_GhMyYKhosXCUKlDgAj",
			"fillStyle": "cross-hatch",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 538.1799795429118,
			"y": -8.595327289335557,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 77.81294832430956,
			"height": 186.9685240616061,
			"seed": 1335299042,
			"groupIds": [],
			"frameId": "IagBYhze8sjgDkoZ4gj5i",
			"roundness": {
				"type": 3
			},
			"boundElements": [],
			"updated": 1712826540973,
			"link": null,
			"locked": false
		},
		{
			"type": "line",
			"version": 288,
			"versionNonce": 1057167430,
			"isDeleted": false,
			"id": "r7N3jOnDDvb2kJ5CUtJW2",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "dashed",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 583.4028806572484,
			"y": -17.279380955139402,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"width": 2.5474337982060433,
			"height": 184.5148345274799,
			"seed": 928340030,
			"groupIds": [],
			"frameId": "IagBYhze8sjgDkoZ4gj5i",
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1712826540973,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					-2.5474337982060433,
					-184.5148345274799
				]
			]
		},
		{
			"type": "text",
			"version": 580,
			"versionNonce": 2022569754,
			"isDeleted": false,
			"id": "ItrOS45l",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "dashed",
			"roughness": 1,
			"opacity": 100,
			"angle": 4.7230104007270555,
			"x": 474.34760183819947,
			"y": 48.811775042933206,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 170.478515625,
			"height": 31.749084531450897,
			"seed": 558674046,
			"groupIds": [],
			"frameId": "IagBYhze8sjgDkoZ4gj5i",
			"roundness": null,
			"boundElements": [],
			"updated": 1712826540973,
			"link": null,
			"locked": false,
			"fontSize": 26.45757044287575,
			"fontFamily": 3,
			"text": "Endschalter",
			"rawText": "Endschalter",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "Endschalter",
			"lineHeight": 1.2,
			"baseline": 26
		},
		{
			"type": "rectangle",
			"version": 450,
			"versionNonce": 415506310,
			"isDeleted": false,
			"id": "ujuVuac5HQPHgBasAOVcE",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 215.06168555847148,
			"y": -154.3358132239171,
			"strokeColor": "#000000",
			"backgroundColor": "#e9ecef",
			"width": 186.61446791482808,
			"height": 105.43189823221053,
			"seed": 1014524350,
			"groupIds": [],
			"frameId": "IagBYhze8sjgDkoZ4gj5i",
			"roundness": {
				"type": 3
			},
			"boundElements": [
				{
					"type": "text",
					"id": "MACu6yOQ"
				}
			],
			"updated": 1712826540974,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 421,
			"versionNonce": 1555301338,
			"isDeleted": false,
			"id": "MACu6yOQ",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 233.36891951588552,
			"y": -120.81986410781185,
			"strokeColor": "#000000",
			"backgroundColor": "#e9ecef",
			"width": 150,
			"height": 38.4,
			"seed": 34454782,
			"groupIds": [],
			"frameId": "IagBYhze8sjgDkoZ4gj5i",
			"roundness": null,
			"boundElements": [],
			"updated": 1712826540974,
			"link": null,
			"locked": false,
			"fontSize": 32,
			"fontFamily": 3,
			"text": "Platform",
			"rawText": "Platform",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "ujuVuac5HQPHgBasAOVcE",
			"originalText": "Platform",
			"lineHeight": 1.2,
			"baseline": 31
		},
		{
			"type": "text",
			"version": 619,
			"versionNonce": 2070036166,
			"isDeleted": false,
			"id": "8yUq8XaX",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 216.49086341140963,
			"y": -258.6024181284691,
			"strokeColor": "#000000",
			"backgroundColor": "#e9ecef",
			"width": 327.5390625,
			"height": 51.6,
			"seed": 1350546430,
			"groupIds": [],
			"frameId": "IagBYhze8sjgDkoZ4gj5i",
			"roundness": null,
			"boundElements": [],
			"updated": 1712826540974,
			"link": null,
			"locked": false,
			"fontSize": 43,
			"fontFamily": 3,
			"text": "Normal Closed",
			"rawText": "Normal Closed",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "Normal Closed",
			"lineHeight": 1.2,
			"baseline": 41
		},
		{
			"type": "text",
			"version": 86,
			"versionNonce": 301627546,
			"isDeleted": false,
			"id": "Ns8RnahQ",
			"fillStyle": "cross-hatch",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 590.2042149758776,
			"y": -899.5416662052002,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 302.34375,
			"height": 51.6,
			"seed": 124107646,
			"groupIds": [],
			"frameId": "2WcXcC6ozWX6UZtjXOLUt",
			"roundness": null,
			"boundElements": [],
			"updated": 1712826540974,
			"link": null,
			"locked": false,
			"fontSize": 43,
			"fontFamily": 3,
			"text": "Closed Loop ",
			"rawText": "Closed Loop ",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "Closed Loop ",
			"lineHeight": 1.2,
			"baseline": 41
		},
		{
			"type": "rectangle",
			"version": 1325,
			"versionNonce": 2071623174,
			"isDeleted": false,
			"id": "OxPnkcK-YZM0qMWUWYk1-",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 918.202795371259,
			"y": -778.4666366921654,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 59.04901772977437,
			"height": 61.29511560443,
			"seed": 1471489762,
			"groupIds": [
				"CM6HyDD9pGG02ImmR4kYg"
			],
			"frameId": "2WcXcC6ozWX6UZtjXOLUt",
			"roundness": null,
			"boundElements": [],
			"updated": 1712826540974,
			"link": null,
			"locked": false
		},
		{
			"type": "rectangle",
			"version": 1257,
			"versionNonce": 1746163034,
			"isDeleted": false,
			"id": "rC-EcSEL0O55tlecZyIH9",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 931.3953762805262,
			"y": -762.4134713476801,
			"strokeColor": "#000000",
			"backgroundColor": "black",
			"width": 29.78586167252632,
			"height": 31.873793322238196,
			"seed": 1307703970,
			"groupIds": [
				"CM6HyDD9pGG02ImmR4kYg"
			],
			"frameId": "2WcXcC6ozWX6UZtjXOLUt",
			"roundness": null,
			"boundElements": [],
			"updated": 1712826540974,
			"link": null,
			"locked": false
		},
		{
			"type": "line",
			"version": 1073,
			"versionNonce": 302630214,
			"isDeleted": false,
			"id": "9InpVVmRcH_JM-5Hl4HGY",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 932.488749952542,
			"y": -793.942858049066,
			"strokeColor": "#000000",
			"backgroundColor": "black",
			"width": 0.7515244268512646,
			"height": 16.193175852278152,
			"seed": 1423857250,
			"groupIds": [
				"CM6HyDD9pGG02ImmR4kYg"
			],
			"frameId": "2WcXcC6ozWX6UZtjXOLUt",
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1712826540974,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					-0.7515244268512646,
					16.193175852278152
				]
			]
		},
		{
			"type": "line",
			"version": 1114,
			"versionNonce": 1079286298,
			"isDeleted": false,
			"id": "CFYLpwNfMx528LUr9JKbb",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 966.6518566711951,
			"y": -794.2681180354687,
			"strokeColor": "#000000",
			"backgroundColor": "black",
			"width": 0.7515244268512646,
			"height": 16.193175852278152,
			"seed": 1028209186,
			"groupIds": [
				"CM6HyDD9pGG02ImmR4kYg"
			],
			"frameId": "2WcXcC6ozWX6UZtjXOLUt",
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1712826540974,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					-0.7515244268512646,
					16.193175852278152
				]
			]
		},
		{
			"type": "line",
			"version": 1103,
			"versionNonce": 275590278,
			"isDeleted": false,
			"id": "iAzy1QdGPsdiE3Z5kAKWP",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 950.7194343393045,
			"y": -793.5839026039557,
			"strokeColor": "#000000",
			"backgroundColor": "black",
			"width": 0.7515244268512646,
			"height": 16.193175852278152,
			"seed": 1713481186,
			"groupIds": [
				"CM6HyDD9pGG02ImmR4kYg"
			],
			"frameId": "2WcXcC6ozWX6UZtjXOLUt",
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1712826540974,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					-0.7515244268512646,
					16.193175852278152
				]
			]
		},
		{
			"type": "line",
			"version": 1158,
			"versionNonce": 1504593626,
			"isDeleted": false,
			"id": "I6Im9Q8GEsHJZvPKr3jCf",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 934.1850757846663,
			"y": -715.4388857374363,
			"strokeColor": "#000000",
			"backgroundColor": "black",
			"width": 0.7515244268512646,
			"height": 16.193175852278152,
			"seed": 2021038498,
			"groupIds": [
				"CM6HyDD9pGG02ImmR4kYg"
			],
			"frameId": "2WcXcC6ozWX6UZtjXOLUt",
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1712826540974,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					-0.7515244268512646,
					16.193175852278152
				]
			]
		},
		{
			"type": "line",
			"version": 1130,
			"versionNonce": 341945286,
			"isDeleted": false,
			"id": "bYIqaPcDJySUL2ZHHmpCo",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 947.1560281124156,
			"y": -715.0025935943529,
			"strokeColor": "#000000",
			"backgroundColor": "black",
			"width": 0.7515244268512646,
			"height": 16.193175852278152,
			"seed": 595006818,
			"groupIds": [
				"CM6HyDD9pGG02ImmR4kYg"
			],
			"frameId": "2WcXcC6ozWX6UZtjXOLUt",
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1712826540974,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					-0.7515244268512646,
					16.193175852278152
				]
			]
		},
		{
			"type": "line",
			"version": 1105,
			"versionNonce": 481581978,
			"isDeleted": false,
			"id": "Ns8Q9nxMYXu13vgz3aQTg",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 962.9015566496404,
			"y": -715.8680198203947,
			"strokeColor": "#000000",
			"backgroundColor": "black",
			"width": 0.7515244268512646,
			"height": 16.193175852278152,
			"seed": 1483872546,
			"groupIds": [
				"CM6HyDD9pGG02ImmR4kYg"
			],
			"frameId": "2WcXcC6ozWX6UZtjXOLUt",
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1712826540974,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					-0.7515244268512646,
					16.193175852278152
				]
			]
		},
		{
			"type": "line",
			"version": 1212,
			"versionNonce": 2080654086,
			"isDeleted": false,
			"id": "jLtx14L97AggN3tlJgqSB",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 1.5619589856492286,
			"x": 986.4236411723092,
			"y": -769.2179137602402,
			"strokeColor": "#000000",
			"backgroundColor": "black",
			"width": 0.7515244268512646,
			"height": 16.193175852278152,
			"seed": 114730210,
			"groupIds": [
				"CM6HyDD9pGG02ImmR4kYg"
			],
			"frameId": "2WcXcC6ozWX6UZtjXOLUt",
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1712826540974,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					-0.7515244268512646,
					16.193175852278152
				]
			]
		},
		{
			"type": "line",
			"version": 1259,
			"versionNonce": 1738135642,
			"isDeleted": false,
			"id": "TeEV1xmHvMLbQta-7E9LJ",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 1.5619589856492286,
			"x": 986.8400949231838,
			"y": -754.0535062523275,
			"strokeColor": "#000000",
			"backgroundColor": "black",
			"width": 0.7515244268512646,
			"height": 16.193175852278152,
			"seed": 1479784610,
			"groupIds": [
				"CM6HyDD9pGG02ImmR4kYg"
			],
			"frameId": "2WcXcC6ozWX6UZtjXOLUt",
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1712826540974,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					-0.7515244268512646,
					16.193175852278152
				]
			]
		},
		{
			"type": "line",
			"version": 1264,
			"versionNonce": 1506931270,
			"isDeleted": false,
			"id": "XLmXADCduq9U__RtAAVkm",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 1.5619589856492286,
			"x": 987.6693881656705,
			"y": -739.3939525548506,
			"strokeColor": "#000000",
			"backgroundColor": "black",
			"width": 0.7515244268512646,
			"height": 16.193175852278152,
			"seed": 1815630946,
			"groupIds": [
				"CM6HyDD9pGG02ImmR4kYg"
			],
			"frameId": "2WcXcC6ozWX6UZtjXOLUt",
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1712826540974,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					-0.7515244268512646,
					16.193175852278152
				]
			]
		},
		{
			"type": "line",
			"version": 1255,
			"versionNonce": 1513209114,
			"isDeleted": false,
			"id": "ay_V6-b4gJ0hyqDkS4rTF",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 1.5619589856492286,
			"x": 908.9195442298081,
			"y": -771.666829117727,
			"strokeColor": "#000000",
			"backgroundColor": "black",
			"width": 0.7515244268512646,
			"height": 16.193175852278152,
			"seed": 347306018,
			"groupIds": [
				"CM6HyDD9pGG02ImmR4kYg"
			],
			"frameId": "2WcXcC6ozWX6UZtjXOLUt",
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1712826540974,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					-0.7515244268512646,
					16.193175852278152
				]
			]
		},
		{
			"type": "line",
			"version": 1280,
			"versionNonce": 1755822470,
			"isDeleted": false,
			"id": "xJom07XignB_nwZKliUYc",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 1.5619589856492286,
			"x": 910.1034527712771,
			"y": -758.0095865289609,
			"strokeColor": "#000000",
			"backgroundColor": "black",
			"width": 0.7515244268512646,
			"height": 16.193175852278152,
			"seed": 294921186,
			"groupIds": [
				"CM6HyDD9pGG02ImmR4kYg"
			],
			"frameId": "2WcXcC6ozWX6UZtjXOLUt",
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1712826540974,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					-0.7515244268512646,
					16.193175852278152
				]
			]
		},
		{
			"type": "line",
			"version": 1257,
			"versionNonce": 569313754,
			"isDeleted": false,
			"id": "dN9v-ML9Fg6U8wlOXeP2T",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 1.5619589856492286,
			"x": 909.0505669688513,
			"y": -741.2801605526186,
			"strokeColor": "#000000",
			"backgroundColor": "black",
			"width": 0.7515244268512646,
			"height": 16.193175852278152,
			"seed": 1290360738,
			"groupIds": [
				"CM6HyDD9pGG02ImmR4kYg"
			],
			"frameId": "2WcXcC6ozWX6UZtjXOLUt",
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1712826540974,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					-0.7515244268512646,
					16.193175852278152
				]
			]
		},
		{
			"type": "rectangle",
			"version": 312,
			"versionNonce": 2143459526,
			"isDeleted": false,
			"id": "dP3uXh-NLM730FtY58YU0",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 865.3671670818233,
			"y": -807.5663041079656,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 167.30390908350887,
			"height": 163.43022337167497,
			"seed": 383914850,
			"groupIds": [],
			"frameId": "2WcXcC6ozWX6UZtjXOLUt",
			"roundness": {
				"type": 3
			},
			"boundElements": [
				{
					"id": "T19-vkApf_wa_3Vx3vSpX",
					"type": "arrow"
				},
				{
					"id": "W1DsYrgL2mpaW-WDxLpui",
					"type": "arrow"
				}
			],
			"updated": 1712826540974,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 265,
			"versionNonce": 1172618906,
			"isDeleted": false,
			"id": "xDQBA3ik",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 873.4804208530433,
			"y": -687.3700936102507,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 151.40625,
			"height": 31.019799299007236,
			"seed": 1640847138,
			"groupIds": [],
			"frameId": "2WcXcC6ozWX6UZtjXOLUt",
			"roundness": null,
			"boundElements": [
				{
					"id": "W1DsYrgL2mpaW-WDxLpui",
					"type": "arrow"
				}
			],
			"updated": 1712826540974,
			"link": null,
			"locked": false,
			"fontSize": 25.8498327491727,
			"fontFamily": 3,
			"text": "Controller",
			"rawText": "Controller",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "Controller",
			"lineHeight": 1.2,
			"baseline": 25
		},
		{
			"type": "ellipse",
			"version": 340,
			"versionNonce": 113217542,
			"isDeleted": false,
			"id": "iDpRgM7khGL76u1Ox-p40",
			"fillStyle": "cross-hatch",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 408.9099854850666,
			"y": -786.9208969635719,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 161.79483715637468,
			"height": 150.1625067189922,
			"seed": 1063810110,
			"groupIds": [],
			"frameId": "2WcXcC6ozWX6UZtjXOLUt",
			"roundness": {
				"type": 2
			},
			"boundElements": [
				{
					"id": "T19-vkApf_wa_3Vx3vSpX",
					"type": "arrow"
				}
			],
			"updated": 1712826540974,
			"link": null,
			"locked": false
		},
		{
			"type": "arrow",
			"version": 753,
			"versionNonce": 1925569370,
			"isDeleted": false,
			"id": "T19-vkApf_wa_3Vx3vSpX",
			"fillStyle": "cross-hatch",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 853.622669586347,
			"y": -732.2858576543823,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 246.68385440328188,
			"height": 25.84385555320955,
			"seed": 1952137826,
			"groupIds": [],
			"frameId": "2WcXcC6ozWX6UZtjXOLUt",
			"roundness": {
				"type": 2
			},
			"boundElements": [
				{
					"type": "text",
					"id": "Eyr1dcBL"
				}
			],
			"updated": 1712826540974,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "dP3uXh-NLM730FtY58YU0",
				"focus": 0.18157691964988326,
				"gap": 11.744497495476253
			},
			"endBinding": {
				"elementId": "pdm2Ds__UVCusCUqE-Som",
				"focus": 0.16974878717500538,
				"gap": 18.256783930943243
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					-246.68385440328188,
					25.84385555320955
				]
			]
		},
		{
			"type": "text",
			"version": 33,
			"versionNonce": 1771806534,
			"isDeleted": false,
			"id": "Eyr1dcBL",
			"fillStyle": "cross-hatch",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 547.436996861394,
			"y": -562.2919784610007,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 82.03125,
			"height": 48,
			"seed": 1721725794,
			"groupIds": [],
			"frameId": "2WcXcC6ozWX6UZtjXOLUt",
			"roundness": null,
			"boundElements": [],
			"updated": 1712826540974,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 3,
			"text": "Schritt\nBefehl",
			"rawText": "Schritt\nBefehl",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "T19-vkApf_wa_3Vx3vSpX",
			"originalText": "Schritt\nBefehl",
			"lineHeight": 1.2,
			"baseline": 42
		},
		{
			"type": "rectangle",
			"version": 117,
			"versionNonce": 1189437466,
			"isDeleted": false,
			"id": "pdm2Ds__UVCusCUqE-Som",
			"fillStyle": "cross-hatch",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 389.87531062541996,
			"y": -798.553146721451,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 198.80672062670192,
			"height": 175.54205975193702,
			"seed": 1006308606,
			"groupIds": [],
			"frameId": "2WcXcC6ozWX6UZtjXOLUt",
			"roundness": {
				"type": 3
			},
			"boundElements": [
				{
					"id": "T19-vkApf_wa_3Vx3vSpX",
					"type": "arrow"
				}
			],
			"updated": 1712826540974,
			"link": null,
			"locked": false
		},
		{
			"type": "freedraw",
			"version": 42,
			"versionNonce": 213108358,
			"isDeleted": false,
			"id": "rJIXMDHMMf2froxxYx7kK",
			"fillStyle": "cross-hatch",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 568.5898498037578,
			"y": -777.4034990241212,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 0.0001,
			"height": 0.0001,
			"seed": 13918590,
			"groupIds": [],
			"frameId": "2WcXcC6ozWX6UZtjXOLUt",
			"roundness": null,
			"boundElements": [],
			"updated": 1712826540974,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.0001,
					0.0001
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "freedraw",
			"version": 42,
			"versionNonce": 506875098,
			"isDeleted": false,
			"id": "7BD8fE0lEnbGlhDGRHC8p",
			"fillStyle": "cross-hatch",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 414.1974377491506,
			"y": -778.460965273087,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 0.0001,
			"height": 0.0001,
			"seed": 872720958,
			"groupIds": [],
			"frameId": "2WcXcC6ozWX6UZtjXOLUt",
			"roundness": null,
			"boundElements": [],
			"updated": 1712826540974,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.0001,
					0.0001
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "freedraw",
			"version": 42,
			"versionNonce": 1086653894,
			"isDeleted": false,
			"id": "_xUlY6jFQ87twnjzh2oH1",
			"fillStyle": "cross-hatch",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 413.13997150018474,
			"y": -647.3331737534929,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 0.0001,
			"height": 0.0001,
			"seed": 304655102,
			"groupIds": [],
			"frameId": "2WcXcC6ozWX6UZtjXOLUt",
			"roundness": null,
			"boundElements": [],
			"updated": 1712826540974,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.0001,
					0.0001
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "freedraw",
			"version": 42,
			"versionNonce": 1582014874,
			"isDeleted": false,
			"id": "aXhVcw91w3jtFKFNLDTOT",
			"fillStyle": "cross-hatch",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 563.3024378794254,
			"y": -645.2182009158096,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 0.0001,
			"height": 0.0001,
			"seed": 1178297278,
			"groupIds": [],
			"frameId": "2WcXcC6ozWX6UZtjXOLUt",
			"roundness": null,
			"boundElements": [],
			"updated": 1712826540974,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.0001,
					0.0001
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "ellipse",
			"version": 151,
			"versionNonce": 921459974,
			"isDeleted": false,
			"id": "mW3bQMEPk164eEZCWPaDG",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 462.8415709773569,
			"y": -729.8167513653774,
			"strokeColor": "#1971c2",
			"backgroundColor": "#a5d8ff",
			"width": 47.586707318992126,
			"height": 42.29929539465974,
			"seed": 2031604862,
			"groupIds": [],
			"frameId": "2WcXcC6ozWX6UZtjXOLUt",
			"roundness": {
				"type": 2
			},
			"boundElements": [
				{
					"id": "TEjO-ozN_jP5L7gEMw2Yv",
					"type": "arrow"
				}
			],
			"updated": 1712826540974,
			"link": null,
			"locked": false
		},
		{
			"type": "rectangle",
			"version": 172,
			"versionNonce": 1113087578,
			"isDeleted": false,
			"id": "wKeEaizdQAhnceij3MdpT",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 342.2886033064277,
			"y": -522.5502200674455,
			"strokeColor": "#1971c2",
			"backgroundColor": "#a5d8ff",
			"width": 197.74917369823277,
			"height": 53.931585492290424,
			"seed": 2057437218,
			"groupIds": [],
			"frameId": "2WcXcC6ozWX6UZtjXOLUt",
			"roundness": {
				"type": 3
			},
			"boundElements": [
				{
					"id": "TEjO-ozN_jP5L7gEMw2Yv",
					"type": "arrow"
				},
				{
					"id": "W1DsYrgL2mpaW-WDxLpui",
					"type": "arrow"
				}
			],
			"updated": 1712826540974,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 116,
			"versionNonce": 1957088326,
			"isDeleted": false,
			"id": "iwynSGvF",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 389.8752702856683,
			"y": -513.3179299698147,
			"strokeColor": "#000000",
			"backgroundColor": "#a5d8ff",
			"width": 98.4375,
			"height": 28.799999999999997,
			"seed": 1491948578,
			"groupIds": [],
			"frameId": "2WcXcC6ozWX6UZtjXOLUt",
			"roundness": null,
			"boundElements": [],
			"updated": 1712826540974,
			"link": null,
			"locked": false,
			"fontSize": 24,
			"fontFamily": 3,
			"text": "Encoder",
			"rawText": "Encoder",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "Encoder",
			"lineHeight": 1.2,
			"baseline": 23
		},
		{
			"type": "arrow",
			"version": 132,
			"versionNonce": 657425178,
			"isDeleted": false,
			"id": "TEjO-ozN_jP5L7gEMw2Yv",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 466.0140907435094,
			"y": -535.2400167537937,
			"strokeColor": "#1971c2",
			"backgroundColor": "#a5d8ff",
			"width": 21.149647697329783,
			"height": 138.53021662136143,
			"seed": 340674878,
			"groupIds": [],
			"frameId": "2WcXcC6ozWX6UZtjXOLUt",
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1712826540974,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "wKeEaizdQAhnceij3MdpT",
				"focus": 0.18250644947038341,
				"gap": 12.689796686348245
			},
			"endBinding": {
				"elementId": "mW3bQMEPk164eEZCWPaDG",
				"focus": -0.24390775610756443,
				"gap": 13.750673613413348
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					21.149647697329783,
					-138.53021662136143
				]
			]
		},
		{
			"type": "text",
			"version": 134,
			"versionNonce": 1204900742,
			"isDeleted": false,
			"id": "kwAPI4WX",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 368.72566292809006,
			"y": -607.1488511965165,
			"strokeColor": "#1971c2",
			"backgroundColor": "#a5d8ff",
			"width": 103.125,
			"height": 38.4,
			"seed": 1799701246,
			"groupIds": [],
			"frameId": "2WcXcC6ozWX6UZtjXOLUt",
			"roundness": null,
			"boundElements": [],
			"updated": 1712826540974,
			"link": null,
			"locked": false,
			"fontSize": 16,
			"fontFamily": 3,
			"text": "Misst Rotor\nRotation",
			"rawText": "Misst Rotor\nRotation",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "Misst Rotor\nRotation",
			"lineHeight": 1.2,
			"baseline": 34
		},
		{
			"type": "arrow",
			"version": 154,
			"versionNonce": 1464078298,
			"isDeleted": false,
			"id": "W1DsYrgL2mpaW-WDxLpui",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 546.3827358574622,
			"y": -525.7226994938462,
			"strokeColor": "#1971c2",
			"backgroundColor": "#a5d8ff",
			"width": 311.9573035356151,
			"height": 122.6679405086125,
			"seed": 1759038270,
			"groupIds": [],
			"frameId": "2WcXcC6ozWX6UZtjXOLUt",
			"roundness": {
				"type": 2
			},
			"boundElements": [
				{
					"type": "text",
					"id": "kbmbhhvj"
				}
			],
			"updated": 1712826540974,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "wKeEaizdQAhnceij3MdpT",
				"focus": 0.1706452878223732,
				"gap": 6.34495885280171
			},
			"endBinding": {
				"elementId": "xDQBA3ik",
				"focus": 0.2705945860716945,
				"gap": 15.140381459965909
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					311.9573035356151,
					-122.6679405086125
				]
			]
		},
		{
			"type": "text",
			"version": 132,
			"versionNonce": 984150726,
			"isDeleted": false,
			"id": "kbmbhhvj",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 485.64575489492654,
			"y": -405.9847061243444,
			"strokeColor": "#1971c2",
			"backgroundColor": "#a5d8ff",
			"width": 159.375,
			"height": 38.4,
			"seed": 355078334,
			"groupIds": [],
			"frameId": "2WcXcC6ozWX6UZtjXOLUt",
			"roundness": null,
			"boundElements": [],
			"updated": 1712826540974,
			"link": null,
			"locked": false,
			"fontSize": 16,
			"fontFamily": 3,
			"text": "übergibt Messwert\nan Controller",
			"rawText": "übergibt Messwert\nan Controller",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "W1DsYrgL2mpaW-WDxLpui",
			"originalText": "übergibt Messwert\nan Controller",
			"lineHeight": 1.2,
			"baseline": 34
		},
		{
			"type": "text",
			"version": 317,
			"versionNonce": 1453917338,
			"isDeleted": false,
			"id": "4iHOs8VW",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 1024.9301671615422,
			"y": 48.240959692996455,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "#a5d8ff",
			"width": 56.25,
			"height": 38.4,
			"seed": 154085090,
			"groupIds": [],
			"frameId": "IagBYhze8sjgDkoZ4gj5i",
			"roundness": null,
			"boundElements": [],
			"updated": 1712826540974,
			"link": null,
			"locked": false,
			"fontSize": 32,
			"fontFamily": 3,
			"text": "LOW",
			"rawText": "LOW",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "LOW",
			"lineHeight": 1.2,
			"baseline": 31
		},
		{
			"type": "line",
			"version": 401,
			"versionNonce": 130722310,
			"isDeleted": false,
			"id": "t9eXA252N4DgGOVpSIA1h",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "dashed",
			"roughness": 1,
			"opacity": 50,
			"angle": 0,
			"x": 728.5619194104921,
			"y": -104.92010356707135,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 529.4261767454741,
			"height": 1.9994468718880967,
			"seed": 420128702,
			"groupIds": [],
			"frameId": "IagBYhze8sjgDkoZ4gj5i",
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1712826540974,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					529.4261767454741,
					1.9994468718880967
				]
			]
		},
		{
			"type": "rectangle",
			"version": 1351,
			"versionNonce": 789668186,
			"isDeleted": false,
			"id": "B9T5AxB58xBTcyrg9m3oF",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 821.1833972411822,
			"y": 20.000624757030096,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 59.04901772977437,
			"height": 61.29511560443,
			"seed": 588972030,
			"groupIds": [
				"nVsZziJN14dqDR7lyA-aJ"
			],
			"frameId": "IagBYhze8sjgDkoZ4gj5i",
			"roundness": null,
			"boundElements": [],
			"updated": 1712826540974,
			"link": null,
			"locked": false
		},
		{
			"type": "rectangle",
			"version": 1283,
			"versionNonce": 238254406,
			"isDeleted": false,
			"id": "w04olBnCpDPhJ-kg-Zsgg",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 834.3759781504494,
			"y": 36.05379010151535,
			"strokeColor": "#000000",
			"backgroundColor": "black",
			"width": 29.78586167252632,
			"height": 31.873793322238196,
			"seed": 1911967806,
			"groupIds": [
				"nVsZziJN14dqDR7lyA-aJ"
			],
			"frameId": "IagBYhze8sjgDkoZ4gj5i",
			"roundness": null,
			"boundElements": [],
			"updated": 1712826540974,
			"link": null,
			"locked": false
		},
		{
			"type": "line",
			"version": 1099,
			"versionNonce": 1003496986,
			"isDeleted": false,
			"id": "H55lG3LiDastgQWViCzcf",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 835.4693518224652,
			"y": 4.524403400129472,
			"strokeColor": "#000000",
			"backgroundColor": "black",
			"width": 0.7515244268512646,
			"height": 16.193175852278152,
			"seed": 561879166,
			"groupIds": [
				"nVsZziJN14dqDR7lyA-aJ"
			],
			"frameId": "IagBYhze8sjgDkoZ4gj5i",
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1712826540974,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					-0.7515244268512646,
					16.193175852278152
				]
			]
		},
		{
			"type": "line",
			"version": 1140,
			"versionNonce": 1161846918,
			"isDeleted": false,
			"id": "IKXNcKAzVapCgNimM7lUZ",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 869.6324585411184,
			"y": 4.1991434137268016,
			"strokeColor": "#000000",
			"backgroundColor": "black",
			"width": 0.7515244268512646,
			"height": 16.193175852278152,
			"seed": 695326910,
			"groupIds": [
				"nVsZziJN14dqDR7lyA-aJ"
			],
			"frameId": "IagBYhze8sjgDkoZ4gj5i",
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1712826540974,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					-0.7515244268512646,
					16.193175852278152
				]
			]
		},
		{
			"type": "line",
			"version": 1129,
			"versionNonce": 1977111258,
			"isDeleted": false,
			"id": "oyhuG4bwmnQeiXvX6b_q1",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 853.7000362092277,
			"y": 4.883358845239741,
			"strokeColor": "#000000",
			"backgroundColor": "black",
			"width": 0.7515244268512646,
			"height": 16.193175852278152,
			"seed": 1634996478,
			"groupIds": [
				"nVsZziJN14dqDR7lyA-aJ"
			],
			"frameId": "IagBYhze8sjgDkoZ4gj5i",
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1712826540974,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					-0.7515244268512646,
					16.193175852278152
				]
			]
		},
		{
			"type": "line",
			"version": 1184,
			"versionNonce": 816734150,
			"isDeleted": false,
			"id": "cno6Pu6IhwZwnWuuztwXV",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 837.1656776545896,
			"y": 83.02837571175917,
			"strokeColor": "#000000",
			"backgroundColor": "black",
			"width": 0.7515244268512646,
			"height": 16.193175852278152,
			"seed": 84230462,
			"groupIds": [
				"nVsZziJN14dqDR7lyA-aJ"
			],
			"frameId": "IagBYhze8sjgDkoZ4gj5i",
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1712826540974,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					-0.7515244268512646,
					16.193175852278152
				]
			]
		},
		{
			"type": "line",
			"version": 1156,
			"versionNonce": 1069344666,
			"isDeleted": false,
			"id": "zgsdS18VS8QwBwh8qnjK0",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 850.1366299823388,
			"y": 83.46466785484256,
			"strokeColor": "#000000",
			"backgroundColor": "black",
			"width": 0.7515244268512646,
			"height": 16.193175852278152,
			"seed": 931555710,
			"groupIds": [
				"nVsZziJN14dqDR7lyA-aJ"
			],
			"frameId": "IagBYhze8sjgDkoZ4gj5i",
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1712826540974,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					-0.7515244268512646,
					16.193175852278152
				]
			]
		},
		{
			"type": "line",
			"version": 1131,
			"versionNonce": 1419409158,
			"isDeleted": false,
			"id": "556lK3NeHoT0ltOZrEOU6",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 865.8821585195636,
			"y": 82.59924162880077,
			"strokeColor": "#000000",
			"backgroundColor": "black",
			"width": 0.7515244268512646,
			"height": 16.193175852278152,
			"seed": 137923006,
			"groupIds": [
				"nVsZziJN14dqDR7lyA-aJ"
			],
			"frameId": "IagBYhze8sjgDkoZ4gj5i",
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1712826540975,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					-0.7515244268512646,
					16.193175852278152
				]
			]
		},
		{
			"type": "line",
			"version": 1238,
			"versionNonce": 833676378,
			"isDeleted": false,
			"id": "OsmjC5CQguj4Yq5xKQ5DI",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 1.5619589856492286,
			"x": 889.4042430422325,
			"y": 29.249347688955254,
			"strokeColor": "#000000",
			"backgroundColor": "black",
			"width": 0.7515244268512646,
			"height": 16.193175852278152,
			"seed": 1983685118,
			"groupIds": [
				"nVsZziJN14dqDR7lyA-aJ"
			],
			"frameId": "IagBYhze8sjgDkoZ4gj5i",
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1712826540975,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					-0.7515244268512646,
					16.193175852278152
				]
			]
		},
		{
			"type": "line",
			"version": 1285,
			"versionNonce": 696362566,
			"isDeleted": false,
			"id": "PtecUic-hlRH2nPsXmsqp",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 1.5619589856492286,
			"x": 889.820696793107,
			"y": 44.41375519686801,
			"strokeColor": "#000000",
			"backgroundColor": "black",
			"width": 0.7515244268512646,
			"height": 16.193175852278152,
			"seed": 1955836478,
			"groupIds": [
				"nVsZziJN14dqDR7lyA-aJ"
			],
			"frameId": "IagBYhze8sjgDkoZ4gj5i",
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1712826540975,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					-0.7515244268512646,
					16.193175852278152
				]
			]
		},
		{
			"type": "line",
			"version": 1290,
			"versionNonce": 1703364890,
			"isDeleted": false,
			"id": "fi9D3irrjw4RJf6vFn6Ho",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 1.5619589856492286,
			"x": 890.6499900355938,
			"y": 59.073308894344905,
			"strokeColor": "#000000",
			"backgroundColor": "black",
			"width": 0.7515244268512646,
			"height": 16.193175852278152,
			"seed": 1847507582,
			"groupIds": [
				"nVsZziJN14dqDR7lyA-aJ"
			],
			"frameId": "IagBYhze8sjgDkoZ4gj5i",
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1712826540975,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					-0.7515244268512646,
					16.193175852278152
				]
			]
		},
		{
			"type": "line",
			"version": 1281,
			"versionNonce": 272690566,
			"isDeleted": false,
			"id": "c-tnReR_Hzh8ipcTri066",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 1.5619589856492286,
			"x": 811.9001460997314,
			"y": 26.800432331468414,
			"strokeColor": "#000000",
			"backgroundColor": "black",
			"width": 0.7515244268512646,
			"height": 16.193175852278152,
			"seed": 1235139262,
			"groupIds": [
				"nVsZziJN14dqDR7lyA-aJ"
			],
			"frameId": "IagBYhze8sjgDkoZ4gj5i",
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1712826540975,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					-0.7515244268512646,
					16.193175852278152
				]
			]
		},
		{
			"type": "line",
			"version": 1306,
			"versionNonce": 1119032794,
			"isDeleted": false,
			"id": "I7lvrBwRvAkRyScL3e0Je",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 1.5619589856492286,
			"x": 813.0840546412004,
			"y": 40.45767492023458,
			"strokeColor": "#000000",
			"backgroundColor": "black",
			"width": 0.7515244268512646,
			"height": 16.193175852278152,
			"seed": 1840558846,
			"groupIds": [
				"nVsZziJN14dqDR7lyA-aJ"
			],
			"frameId": "IagBYhze8sjgDkoZ4gj5i",
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1712826540975,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					-0.7515244268512646,
					16.193175852278152
				]
			]
		},
		{
			"type": "line",
			"version": 1283,
			"versionNonce": 1175801030,
			"isDeleted": false,
			"id": "oD16o8An5fFKmqiVLmyU3",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 1.5619589856492286,
			"x": 812.0311688387745,
			"y": 57.18710089657691,
			"strokeColor": "#000000",
			"backgroundColor": "black",
			"width": 0.7515244268512646,
			"height": 16.193175852278152,
			"seed": 1155638078,
			"groupIds": [
				"nVsZziJN14dqDR7lyA-aJ"
			],
			"frameId": "IagBYhze8sjgDkoZ4gj5i",
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1712826540975,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					-0.7515244268512646,
					16.193175852278152
				]
			]
		},
		{
			"type": "rectangle",
			"version": 332,
			"versionNonce": 1246186138,
			"isDeleted": false,
			"id": "5BDksADbf4yqcvNyvBcx1",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 768.3477689517465,
			"y": -9.099042658770145,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 167.30390908350887,
			"height": 163.43022337167497,
			"seed": 1099336574,
			"groupIds": [],
			"frameId": "IagBYhze8sjgDkoZ4gj5i",
			"roundness": {
				"type": 3
			},
			"boundElements": [],
			"updated": 1712826540975,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 240,
			"versionNonce": 1486603270,
			"isDeleted": false,
			"id": "G5MQLGYC",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 776.0364002534114,
			"y": 105.86283271093168,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 151.40625,
			"height": 31.019799299007236,
			"seed": 1642359742,
			"groupIds": [],
			"frameId": "IagBYhze8sjgDkoZ4gj5i",
			"roundness": null,
			"boundElements": [],
			"updated": 1712826540975,
			"link": null,
			"locked": false,
			"fontSize": 25.8498327491727,
			"fontFamily": 3,
			"text": "Controller",
			"rawText": "Controller",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "Controller",
			"lineHeight": 1.2,
			"baseline": 25
		},
		{
			"type": "line",
			"version": 591,
			"versionNonce": 1660348250,
			"isDeleted": false,
			"id": "GGEL8C0RPjyxVmlUPJn5k",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 325.46129969649144,
			"y": 84.05168723083375,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"width": 212.1166214516586,
			"height": 2.6451578865729743,
			"seed": 874267646,
			"groupIds": [],
			"frameId": "IagBYhze8sjgDkoZ4gj5i",
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1712826540975,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					212.1166214516586,
					2.6451578865729743
				]
			]
		},
		{
			"type": "rectangle",
			"version": 385,
			"versionNonce": 433148742,
			"isDeleted": false,
			"id": "2J1xEcNRnmjWaQtCwPj8G",
			"fillStyle": "cross-hatch",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 1153.021273726461,
			"y": -15.98029386195276,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 77.81294832430956,
			"height": 186.9685240616061,
			"seed": 1513034814,
			"groupIds": [],
			"frameId": "IagBYhze8sjgDkoZ4gj5i",
			"roundness": {
				"type": 3
			},
			"boundElements": [],
			"updated": 1712826540975,
			"link": null,
			"locked": false
		},
		{
			"type": "line",
			"version": 353,
			"versionNonce": 622128154,
			"isDeleted": false,
			"id": "euJaHqAHvlDdK90z-YvcB",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "dashed",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 1198.2441748407978,
			"y": -24.664347527756604,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"width": 2.5474337982060433,
			"height": 184.5148345274799,
			"seed": 234740862,
			"groupIds": [],
			"frameId": "IagBYhze8sjgDkoZ4gj5i",
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1712826540975,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					-2.5474337982060433,
					-184.5148345274799
				]
			]
		},
		{
			"type": "text",
			"version": 645,
			"versionNonce": 336788102,
			"isDeleted": false,
			"id": "POx9LDvr",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "dashed",
			"roughness": 1,
			"opacity": 100,
			"angle": 4.7230104007270555,
			"x": 1089.1888960217486,
			"y": 41.42680847031602,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 170.478515625,
			"height": 31.749084531450897,
			"seed": 625581246,
			"groupIds": [],
			"frameId": "IagBYhze8sjgDkoZ4gj5i",
			"roundness": null,
			"boundElements": [],
			"updated": 1712826540975,
			"link": null,
			"locked": false,
			"fontSize": 26.45757044287575,
			"fontFamily": 3,
			"text": "Endschalter",
			"rawText": "Endschalter",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "Endschalter",
			"lineHeight": 1.2,
			"baseline": 26
		},
		{
			"type": "rectangle",
			"version": 491,
			"versionNonce": 647256282,
			"isDeleted": false,
			"id": "yuYIqBIoGZ0EUFTHOZDna",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 815.2940993252729,
			"y": -158.47442384641653,
			"strokeColor": "#000000",
			"backgroundColor": "#e9ecef",
			"width": 186.61446791482808,
			"height": 105.43189823221053,
			"seed": 364074238,
			"groupIds": [],
			"frameId": "IagBYhze8sjgDkoZ4gj5i",
			"roundness": {
				"type": 3
			},
			"boundElements": [
				{
					"type": "text",
					"id": "JP7jBBQa"
				}
			],
			"updated": 1712826540975,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 464,
			"versionNonce": 2115877318,
			"isDeleted": false,
			"id": "JP7jBBQa",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 833.6013332826869,
			"y": -124.95847473031127,
			"strokeColor": "#000000",
			"backgroundColor": "#e9ecef",
			"width": 150,
			"height": 38.4,
			"seed": 2025588030,
			"groupIds": [],
			"frameId": "IagBYhze8sjgDkoZ4gj5i",
			"roundness": null,
			"boundElements": [],
			"updated": 1712826540975,
			"link": null,
			"locked": false,
			"fontSize": 32,
			"fontFamily": 3,
			"text": "Platform",
			"rawText": "Platform",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "yuYIqBIoGZ0EUFTHOZDna",
			"originalText": "Platform",
			"lineHeight": 1.2,
			"baseline": 31
		},
		{
			"type": "text",
			"version": 436,
			"versionNonce": 1191718298,
			"isDeleted": false,
			"id": "elVAzUEU",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 394.10827947109976,
			"y": 40.79185044677399,
			"strokeColor": "#e03131",
			"backgroundColor": "#ffffff",
			"width": 75,
			"height": 38.4,
			"seed": 264547710,
			"groupIds": [],
			"frameId": "IagBYhze8sjgDkoZ4gj5i",
			"roundness": null,
			"boundElements": [],
			"updated": 1712826540975,
			"link": null,
			"locked": false,
			"fontSize": 32,
			"fontFamily": 3,
			"text": "HIGH",
			"rawText": "HIGH",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "HIGH",
			"lineHeight": 1.2,
			"baseline": 31
		},
		{
			"type": "line",
			"version": 459,
			"versionNonce": 789483782,
			"isDeleted": false,
			"id": "_yx2ALcNN6P_b0ucgZtvr",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "dashed",
			"roughness": 1,
			"opacity": 50,
			"angle": 0,
			"x": 467.0292189001243,
			"y": 492.5333494726773,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 505.00089213541196,
			"height": 0.10915891749414186,
			"seed": 1208896958,
			"groupIds": [],
			"frameId": "IagBYhze8sjgDkoZ4gj5i",
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1712826540975,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					505.00089213541196,
					0.10915891749414186
				]
			]
		},
		{
			"type": "rectangle",
			"version": 1416,
			"versionNonce": 2074307162,
			"isDeleted": false,
			"id": "wm26uEABuLtZE4ujqgUqf",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 539.8540131719038,
			"y": 613.6735739951032,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 59.04901772977437,
			"height": 61.29511560443,
			"seed": 1052370430,
			"groupIds": [
				"wpbK81cVNYlfrvGojM0RI"
			],
			"frameId": "IagBYhze8sjgDkoZ4gj5i",
			"roundness": null,
			"boundElements": [],
			"updated": 1712826540975,
			"link": null,
			"locked": false
		},
		{
			"type": "rectangle",
			"version": 1348,
			"versionNonce": 308445254,
			"isDeleted": false,
			"id": "i2Pu5xH2nmYTnfTbNSH-g",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 553.0465940811711,
			"y": 629.7267393395884,
			"strokeColor": "#000000",
			"backgroundColor": "black",
			"width": 29.78586167252632,
			"height": 31.873793322238196,
			"seed": 1153988158,
			"groupIds": [
				"wpbK81cVNYlfrvGojM0RI"
			],
			"frameId": "IagBYhze8sjgDkoZ4gj5i",
			"roundness": null,
			"boundElements": [],
			"updated": 1712826540975,
			"link": null,
			"locked": false
		},
		{
			"type": "line",
			"version": 1164,
			"versionNonce": 456724250,
			"isDeleted": false,
			"id": "is7XGZDVKfSHyEy7iYuH0",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 554.1399677531869,
			"y": 598.1973526382026,
			"strokeColor": "#000000",
			"backgroundColor": "black",
			"width": 0.7515244268512646,
			"height": 16.193175852278152,
			"seed": 1662713470,
			"groupIds": [
				"wpbK81cVNYlfrvGojM0RI"
			],
			"frameId": "IagBYhze8sjgDkoZ4gj5i",
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1712826540975,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					-0.7515244268512646,
					16.193175852278152
				]
			]
		},
		{
			"type": "line",
			"version": 1205,
			"versionNonce": 469141382,
			"isDeleted": false,
			"id": "nzPjHSZsTxGImQDYuOTTh",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 588.30307447184,
			"y": 597.8720926517999,
			"strokeColor": "#000000",
			"backgroundColor": "black",
			"width": 0.7515244268512646,
			"height": 16.193175852278152,
			"seed": 1584561854,
			"groupIds": [
				"wpbK81cVNYlfrvGojM0RI"
			],
			"frameId": "IagBYhze8sjgDkoZ4gj5i",
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1712826540975,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					-0.7515244268512646,
					16.193175852278152
				]
			]
		},
		{
			"type": "line",
			"version": 1194,
			"versionNonce": 708582362,
			"isDeleted": false,
			"id": "fe-PYbSpKdSGqepstTkLQ",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 572.3706521399494,
			"y": 598.5563080833128,
			"strokeColor": "#000000",
			"backgroundColor": "black",
			"width": 0.7515244268512646,
			"height": 16.193175852278152,
			"seed": 997193470,
			"groupIds": [
				"wpbK81cVNYlfrvGojM0RI"
			],
			"frameId": "IagBYhze8sjgDkoZ4gj5i",
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1712826540975,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					-0.7515244268512646,
					16.193175852278152
				]
			]
		},
		{
			"type": "line",
			"version": 1249,
			"versionNonce": 1007134406,
			"isDeleted": false,
			"id": "Nhe4_-tzxYbZlwK9O6Gcv",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 555.8362935853112,
			"y": 676.7013249498323,
			"strokeColor": "#000000",
			"backgroundColor": "black",
			"width": 0.7515244268512646,
			"height": 16.193175852278152,
			"seed": 1117022014,
			"groupIds": [
				"wpbK81cVNYlfrvGojM0RI"
			],
			"frameId": "IagBYhze8sjgDkoZ4gj5i",
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1712826540975,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					-0.7515244268512646,
					16.193175852278152
				]
			]
		},
		{
			"type": "line",
			"version": 1221,
			"versionNonce": 650088602,
			"isDeleted": false,
			"id": "07wNknIzS1R46PxoAZ0GU",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 568.8072459130605,
			"y": 677.1376170929157,
			"strokeColor": "#000000",
			"backgroundColor": "black",
			"width": 0.7515244268512646,
			"height": 16.193175852278152,
			"seed": 71356286,
			"groupIds": [
				"wpbK81cVNYlfrvGojM0RI"
			],
			"frameId": "IagBYhze8sjgDkoZ4gj5i",
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1712826540975,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					-0.7515244268512646,
					16.193175852278152
				]
			]
		},
		{
			"type": "line",
			"version": 1196,
			"versionNonce": 1395842566,
			"isDeleted": false,
			"id": "x9O0rmKnHImiaT2c8wmph",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 584.5527744502853,
			"y": 676.2721908668739,
			"strokeColor": "#000000",
			"backgroundColor": "black",
			"width": 0.7515244268512646,
			"height": 16.193175852278152,
			"seed": 1555443646,
			"groupIds": [
				"wpbK81cVNYlfrvGojM0RI"
			],
			"frameId": "IagBYhze8sjgDkoZ4gj5i",
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1712826540975,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					-0.7515244268512646,
					16.193175852278152
				]
			]
		},
		{
			"type": "line",
			"version": 1303,
			"versionNonce": 1417047386,
			"isDeleted": false,
			"id": "STifqGVnYkPRI0qUOhlmI",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 1.5619589856492286,
			"x": 608.0748589729538,
			"y": 622.9222969270284,
			"strokeColor": "#000000",
			"backgroundColor": "black",
			"width": 0.7515244268512646,
			"height": 16.193175852278152,
			"seed": 2014676990,
			"groupIds": [
				"wpbK81cVNYlfrvGojM0RI"
			],
			"frameId": "IagBYhze8sjgDkoZ4gj5i",
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1712826540975,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					-0.7515244268512646,
					16.193175852278152
				]
			]
		},
		{
			"type": "line",
			"version": 1350,
			"versionNonce": 645213510,
			"isDeleted": false,
			"id": "9Q-mG554ULS0YuNTDZSyi",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 1.5619589856492286,
			"x": 608.4913127238284,
			"y": 638.0867044349411,
			"strokeColor": "#000000",
			"backgroundColor": "black",
			"width": 0.7515244268512646,
			"height": 16.193175852278152,
			"seed": 1449121854,
			"groupIds": [
				"wpbK81cVNYlfrvGojM0RI"
			],
			"frameId": "IagBYhze8sjgDkoZ4gj5i",
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1712826540975,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					-0.7515244268512646,
					16.193175852278152
				]
			]
		},
		{
			"type": "line",
			"version": 1355,
			"versionNonce": 145994266,
			"isDeleted": false,
			"id": "JiChRI2Drc7hZ3vtYNsAh",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 1.5619589856492286,
			"x": 609.3206059663154,
			"y": 652.746258132418,
			"strokeColor": "#000000",
			"backgroundColor": "black",
			"width": 0.7515244268512646,
			"height": 16.193175852278152,
			"seed": 1333141630,
			"groupIds": [
				"wpbK81cVNYlfrvGojM0RI"
			],
			"frameId": "IagBYhze8sjgDkoZ4gj5i",
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1712826540975,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					-0.7515244268512646,
					16.193175852278152
				]
			]
		},
		{
			"type": "line",
			"version": 1346,
			"versionNonce": 1395364998,
			"isDeleted": false,
			"id": "mbNfUUjCFMRdVqDBS31ee",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 1.5619589856492286,
			"x": 530.570762030453,
			"y": 620.4733815695415,
			"strokeColor": "#000000",
			"backgroundColor": "black",
			"width": 0.7515244268512646,
			"height": 16.193175852278152,
			"seed": 387539134,
			"groupIds": [
				"wpbK81cVNYlfrvGojM0RI"
			],
			"frameId": "IagBYhze8sjgDkoZ4gj5i",
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1712826540975,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					-0.7515244268512646,
					16.193175852278152
				]
			]
		},
		{
			"type": "line",
			"version": 1371,
			"versionNonce": 1986682586,
			"isDeleted": false,
			"id": "yQnQ2qRy1EW_07tNG36Kq",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 1.5619589856492286,
			"x": 531.754670571922,
			"y": 634.1306241583077,
			"strokeColor": "#000000",
			"backgroundColor": "black",
			"width": 0.7515244268512646,
			"height": 16.193175852278152,
			"seed": 1089116414,
			"groupIds": [
				"wpbK81cVNYlfrvGojM0RI"
			],
			"frameId": "IagBYhze8sjgDkoZ4gj5i",
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1712826540975,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					-0.7515244268512646,
					16.193175852278152
				]
			]
		},
		{
			"type": "line",
			"version": 1348,
			"versionNonce": 1125323718,
			"isDeleted": false,
			"id": "b3Xl-gSIhjAsOskt1YecD",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 1.5619589856492286,
			"x": 530.7017847694962,
			"y": 650.86005013465,
			"strokeColor": "#000000",
			"backgroundColor": "black",
			"width": 0.7515244268512646,
			"height": 16.193175852278152,
			"seed": 1147849022,
			"groupIds": [
				"wpbK81cVNYlfrvGojM0RI"
			],
			"frameId": "IagBYhze8sjgDkoZ4gj5i",
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1712826540975,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					-0.7515244268512646,
					16.193175852278152
				]
			]
		},
		{
			"type": "rectangle",
			"version": 397,
			"versionNonce": 2049799066,
			"isDeleted": false,
			"id": "rHV2GGkZw_chMn2wfSiHX",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 487.018384882468,
			"y": 584.573906579303,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 167.30390908350887,
			"height": 163.43022337167497,
			"seed": 16445822,
			"groupIds": [],
			"frameId": "IagBYhze8sjgDkoZ4gj5i",
			"roundness": {
				"type": 3
			},
			"boundElements": [],
			"updated": 1712826540975,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 305,
			"versionNonce": 541633286,
			"isDeleted": false,
			"id": "WOI4jE6u",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 494.70701618413295,
			"y": 699.5357819490048,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 151.40625,
			"height": 31.019799299007236,
			"seed": 1104941502,
			"groupIds": [],
			"frameId": "IagBYhze8sjgDkoZ4gj5i",
			"roundness": null,
			"boundElements": [],
			"updated": 1712826540975,
			"link": null,
			"locked": false,
			"fontSize": 25.8498327491727,
			"fontFamily": 3,
			"text": "Controller",
			"rawText": "Controller",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "Controller",
			"lineHeight": 1.2,
			"baseline": 25
		},
		{
			"type": "line",
			"version": 715,
			"versionNonce": 1714417754,
			"isDeleted": false,
			"id": "ZG98IQVlmcXjN3wgMKi-m",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 657.4604855833171,
			"y": 677.5181042155018,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 61.96595244208618,
			"height": 0.15267315338201115,
			"seed": 1110387198,
			"groupIds": [],
			"frameId": "IagBYhze8sjgDkoZ4gj5i",
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1712826540975,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					61.96595244208618,
					-0.15267315338201115
				]
			]
		},
		{
			"type": "rectangle",
			"version": 445,
			"versionNonce": 1229544006,
			"isDeleted": false,
			"id": "wpqB0Fi8Et09-GHuhXpBw",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 871.6918896571829,
			"y": 577.6926553761202,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 77.81294832430956,
			"height": 186.9685240616061,
			"seed": 821377598,
			"groupIds": [],
			"frameId": "IagBYhze8sjgDkoZ4gj5i",
			"roundness": {
				"type": 3
			},
			"boundElements": [],
			"updated": 1712826540975,
			"link": null,
			"locked": false
		},
		{
			"type": "line",
			"version": 418,
			"versionNonce": 1313133850,
			"isDeleted": false,
			"id": "HUbY9-jCv2utSv_0HdzPv",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "dashed",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 916.9147907715196,
			"y": 569.0086017103165,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"width": 2.5474337982060433,
			"height": 184.5148345274799,
			"seed": 890192510,
			"groupIds": [],
			"frameId": "IagBYhze8sjgDkoZ4gj5i",
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1712826540975,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					-2.5474337982060433,
					-184.5148345274799
				]
			]
		},
		{
			"type": "text",
			"version": 710,
			"versionNonce": 1156718982,
			"isDeleted": false,
			"id": "68kVP7XM",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "dashed",
			"roughness": 1,
			"opacity": 100,
			"angle": 4.7230104007270555,
			"x": 807.8595119524706,
			"y": 635.0997577083891,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 170.478515625,
			"height": 31.749084531450897,
			"seed": 1899905726,
			"groupIds": [],
			"frameId": "IagBYhze8sjgDkoZ4gj5i",
			"roundness": null,
			"boundElements": [],
			"updated": 1712826540975,
			"link": null,
			"locked": false,
			"fontSize": 26.45757044287575,
			"fontFamily": 3,
			"text": "Endschalter",
			"rawText": "Endschalter",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "Endschalter",
			"lineHeight": 1.2,
			"baseline": 26
		},
		{
			"type": "text",
			"version": 477,
			"versionNonce": 1407132122,
			"isDeleted": false,
			"id": "JBLerr5o",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 678.3551098101088,
			"y": 690.4328397881452,
			"strokeColor": "#000000",
			"backgroundColor": "#e9ecef",
			"width": 56.25,
			"height": 38.4,
			"seed": 136526590,
			"groupIds": [],
			"frameId": "IagBYhze8sjgDkoZ4gj5i",
			"roundness": null,
			"boundElements": [],
			"updated": 1712826540975,
			"link": null,
			"locked": false,
			"fontSize": 32,
			"fontFamily": 3,
			"text": "LOW",
			"rawText": "LOW",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "LOW",
			"lineHeight": 1.2,
			"baseline": 31
		},
		{
			"type": "text",
			"version": 683,
			"versionNonce": 914358470,
			"isDeleted": false,
			"id": "7GDFDQSJ",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 860.4907511066876,
			"y": -264.19475045666604,
			"strokeColor": "#000000",
			"backgroundColor": "#e9ecef",
			"width": 277.1484375,
			"height": 51.6,
			"seed": 541010750,
			"groupIds": [],
			"frameId": "IagBYhze8sjgDkoZ4gj5i",
			"roundness": null,
			"boundElements": [],
			"updated": 1712826540975,
			"link": null,
			"locked": false,
			"fontSize": 43,
			"fontFamily": 3,
			"text": "Normal Open",
			"rawText": "Normal Open",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "Normal Open",
			"lineHeight": 1.2,
			"baseline": 41
		},
		{
			"type": "rectangle",
			"version": 610,
			"versionNonce": 1913771674,
			"isDeleted": false,
			"id": "279na1VVB9qRc4t8LezDS",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 505.0669018250486,
			"y": 440.4588776749881,
			"strokeColor": "#000000",
			"backgroundColor": "#e9ecef",
			"width": 186.61446791482808,
			"height": 105.43189823221053,
			"seed": 1988664382,
			"groupIds": [],
			"frameId": "IagBYhze8sjgDkoZ4gj5i",
			"roundness": {
				"type": 3
			},
			"boundElements": [
				{
					"type": "text",
					"id": "QSSEQLGQ"
				}
			],
			"updated": 1712826540975,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 583,
			"versionNonce": 1368389638,
			"isDeleted": false,
			"id": "QSSEQLGQ",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 523.3741357824626,
			"y": 473.9748267910934,
			"strokeColor": "#000000",
			"backgroundColor": "#e9ecef",
			"width": 150,
			"height": 38.4,
			"seed": 1978033278,
			"groupIds": [],
			"frameId": "IagBYhze8sjgDkoZ4gj5i",
			"roundness": null,
			"boundElements": [],
			"updated": 1712826540976,
			"link": null,
			"locked": false,
			"fontSize": 32,
			"fontFamily": 3,
			"text": "Platform",
			"rawText": "Platform",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "279na1VVB9qRc4t8LezDS",
			"originalText": "Platform",
			"lineHeight": 1.2,
			"baseline": 31
		},
		{
			"type": "line",
			"version": 749,
			"versionNonce": 1234170714,
			"isDeleted": false,
			"id": "sgdKPiF0UXBOnQMZXiGRn",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 787.970258251612,
			"y": 675.8123343332068,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"width": 83.41607342656187,
			"height": 1.0853072176016099,
			"seed": 249636030,
			"groupIds": [],
			"frameId": "IagBYhze8sjgDkoZ4gj5i",
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1712826540976,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					83.41607342656187,
					-1.0853072176016099
				]
			]
		},
		{
			"type": "line",
			"version": 274,
			"versionNonce": 1310656326,
			"isDeleted": false,
			"id": "DhoVN73LFYvGH3GB2-5PE",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 719.80314220431,
			"y": 677.3322784598938,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "#a5d8ff",
			"width": 19.584888432388652,
			"height": 23.31531796021136,
			"seed": 1931074814,
			"groupIds": [],
			"frameId": "IagBYhze8sjgDkoZ4gj5i",
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1712826540976,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					10.258761248304154,
					-10.258761248304097
				],
				[
					19.584888432388652,
					13.056556711907263
				]
			]
		},
		{
			"type": "line",
			"version": 333,
			"versionNonce": 1823242266,
			"isDeleted": false,
			"id": "-zVsnPmSu8AZb4YaM10HE",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 3.116087979126595,
			"x": 766.4337959129089,
			"y": 670.4827290025935,
			"strokeColor": "#e03131",
			"backgroundColor": "#a5d8ff",
			"width": 19.584888432388652,
			"height": 23.31531796021136,
			"seed": 2014416190,
			"groupIds": [],
			"frameId": "IagBYhze8sjgDkoZ4gj5i",
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1712826540976,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					10.258761248304154,
					-10.258761248304097
				],
				[
					19.584888432388652,
					13.056556711907263
				]
			]
		},
		{
			"type": "line",
			"version": 199,
			"versionNonce": 1552559750,
			"isDeleted": false,
			"id": "BvsO9EJ2BwHS_sjy_RqZA",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 740.4388270719992,
			"y": 690.1770520290003,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "#a5d8ff",
			"width": 3.2314742883495455,
			"height": 10.987017511226924,
			"seed": 455685502,
			"groupIds": [],
			"frameId": "IagBYhze8sjgDkoZ4gj5i",
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1712826540976,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					3.2314742883495455,
					-10.987017511226924
				]
			]
		},
		{
			"type": "line",
			"version": 171,
			"versionNonce": 727344346,
			"isDeleted": false,
			"id": "XF2upZxBEeVPfqiQMIfLC",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 765.6443363828025,
			"y": 661.0937834338542,
			"strokeColor": "#e03131",
			"backgroundColor": "#a5d8ff",
			"width": 3.2314742883495455,
			"height": 10.987017511226924,
			"seed": 94492094,
			"groupIds": [],
			"frameId": "IagBYhze8sjgDkoZ4gj5i",
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1712826540976,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					-3.2314742883495455,
					10.987017511226924
				]
			]
		},
		{
			"type": "text",
			"version": 272,
			"versionNonce": 428764614,
			"isDeleted": false,
			"id": "XCRSBcAC",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 579.7465802123234,
			"y": 381.6533895734934,
			"strokeColor": "#e03131",
			"backgroundColor": "#a5d8ff",
			"width": 287.109375,
			"height": 42,
			"seed": 278687230,
			"groupIds": [],
			"frameId": "IagBYhze8sjgDkoZ4gj5i",
			"roundness": null,
			"boundElements": [],
			"updated": 1712826540976,
			"link": null,
			"locked": false,
			"fontSize": 35,
			"fontFamily": 3,
			"text": "bei Drahtbruch",
			"rawText": "bei Drahtbruch",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "bei Drahtbruch",
			"lineHeight": 1.2,
			"baseline": 33
		},
		{
			"type": "arrow",
			"version": 204,
			"versionNonce": 1596766618,
			"isDeleted": false,
			"id": "aC1pROdoZk7wjcG2ZX_S_",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 514.5933263650315,
			"y": 201.64880247813596,
			"strokeColor": "#e03131",
			"backgroundColor": "#ff8787",
			"width": 130.02886897188324,
			"height": 162.53606683903593,
			"seed": 379519486,
			"groupIds": [],
			"frameId": "IagBYhze8sjgDkoZ4gj5i",
			"roundness": {
				"type": 2
			},
			"boundElements": [
				{
					"type": "text",
					"id": "PefhRZpt"
				}
			],
			"updated": 1712826540976,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "triangle",
			"points": [
				[
					0,
					0
				],
				[
					130.02886897188324,
					162.53606683903593
				]
			]
		},
		{
			"type": "text",
			"version": 108,
			"versionNonce": 38323462,
			"isDeleted": false,
			"id": "PefhRZpt",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 802.8188944804687,
			"y": 259.42178473710874,
			"strokeColor": "#e03131",
			"backgroundColor": "#ff8787",
			"width": 152.9296875,
			"height": 34.8,
			"seed": 1591608738,
			"groupIds": [],
			"frameId": "IagBYhze8sjgDkoZ4gj5i",
			"roundness": null,
			"boundElements": [],
			"updated": 1712826540976,
			"link": null,
			"locked": false,
			"fontSize": 29,
			"fontFamily": 3,
			"text": "fällt auf",
			"rawText": "fällt auf",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "aC1pROdoZk7wjcG2ZX_S_",
			"originalText": "fällt auf",
			"lineHeight": 1.2,
			"baseline": 28
		},
		{
			"type": "arrow",
			"version": 228,
			"versionNonce": 928413274,
			"isDeleted": false,
			"id": "YpGHsURfbetpE98STEim9",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 943.2823760665622,
			"y": 187.42695185080265,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "#ff8787",
			"width": 127.9971981689136,
			"height": 170.66298256073355,
			"seed": 1391808894,
			"groupIds": [],
			"frameId": "IagBYhze8sjgDkoZ4gj5i",
			"roundness": {
				"type": 2
			},
			"boundElements": [
				{
					"type": "text",
					"id": "NvB5eDfG"
				}
			],
			"updated": 1712826540976,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "triangle",
			"points": [
				[
					0,
					0
				],
				[
					-127.9971981689136,
					170.66298256073355
				]
			]
		},
		{
			"type": "text",
			"version": 106,
			"versionNonce": 1748382790,
			"isDeleted": false,
			"id": "NvB5eDfG",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 475.9921818279423,
			"y": 244.05353304335136,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "#ff8787",
			"width": 186.9140625,
			"height": 69.6,
			"seed": 654738302,
			"groupIds": [],
			"frameId": "IagBYhze8sjgDkoZ4gj5i",
			"roundness": null,
			"boundElements": [],
			"updated": 1712826540976,
			"link": null,
			"locked": false,
			"fontSize": 29,
			"fontFamily": 3,
			"text": "fällt nicht\nauf",
			"rawText": "fällt nicht\nauf",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "YpGHsURfbetpE98STEim9",
			"originalText": "fällt nicht\nauf",
			"lineHeight": 1.2,
			"baseline": 62
		},
		{
			"type": "rectangle",
			"version": 345,
			"versionNonce": 78289690,
			"isDeleted": false,
			"id": "kb1670-JuStu8LvqRWwuJ",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 96.02456581021193,
			"y": 1088.3653302495895,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 164.2489804821738,
			"height": 284.0000152587892,
			"seed": 340063742,
			"groupIds": [],
			"frameId": "jerA-kzSGpDyDfhi2SeEA",
			"roundness": null,
			"boundElements": [
				{
					"type": "text",
					"id": "7DWjcZPt"
				}
			],
			"updated": 1712826540976,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 358,
			"versionNonce": 1697889158,
			"isDeleted": false,
			"id": "7DWjcZPt",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 111.35218105129883,
			"y": 1161.9653378789842,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 133.59375,
			"height": 136.79999999999998,
			"seed": 374315966,
			"groupIds": [],
			"frameId": "jerA-kzSGpDyDfhi2SeEA",
			"roundness": null,
			"boundElements": [],
			"updated": 1712826540976,
			"link": null,
			"locked": false,
			"fontSize": 57,
			"fontFamily": 3,
			"text": "DRV\n8825",
			"rawText": "DRV 8825",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "kb1670-JuStu8LvqRWwuJ",
			"originalText": "DRV 8825",
			"lineHeight": 1.2,
			"baseline": 123
		},
		{
			"type": "line",
			"version": 2310,
			"versionNonce": 94119898,
			"isDeleted": false,
			"id": "nzq9Q0heiVckvcwnNRjop",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 6.279401307468326,
			"x": 425.3337540790693,
			"y": 1264.588665635022,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"width": 62.95791196418768,
			"height": 49.50018171543616,
			"seed": 1316462882,
			"groupIds": [
				"bJ-8eh_kjkltsNFpruJk1",
				"Jvrk76x16pqcnIP-wfpYo",
				"vkSgm-Em5A-KGaPtX8xDL",
				"SnoAbrznAzV8b0BaMdRl0"
			],
			"frameId": "jerA-kzSGpDyDfhi2SeEA",
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1712826540976,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					0.7891264851633601,
					-24.996263464941304
				],
				[
					11.245052413572049,
					-37.77213145813402
				],
				[
					31.78700123048332,
					-43.23108554817799
				],
				[
					51.860406196815354,
					-37.79128568301108
				],
				[
					62.11905050393612,
					-24.325865594233626
				],
				[
					62.95791196418768,
					-3.6438015778128694
				],
				[
					58.92382167639496,
					6.26909616725818
				]
			]
		},
		{
			"type": "line",
			"version": 1354,
			"versionNonce": 1333680838,
			"isDeleted": false,
			"id": "E4dWbKU4TD2bk-sRTU-Q7",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 6.279401307468326,
			"x": 424.38618358616407,
			"y": 1264.7812033569842,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"width": 58.5926147308669,
			"height": 0,
			"seed": 791149054,
			"groupIds": [
				"8fOFpnkmaARR8F3jL12dz",
				"cu9B6vLLYTcEfl-F16Y8M",
				"SnoAbrznAzV8b0BaMdRl0"
			],
			"frameId": "jerA-kzSGpDyDfhi2SeEA",
			"roundness": null,
			"boundElements": [],
			"updated": 1712826540976,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					-58.5926147308669,
					0
				]
			]
		},
		{
			"type": "line",
			"version": 2424,
			"versionNonce": 842931354,
			"isDeleted": false,
			"id": "hH24QH4g2ipNxUBbhUeVY",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 6.2794013074683335,
			"x": 542.6959112864084,
			"y": 1263.6450305043638,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"width": 62.95791196418768,
			"height": 49.50018171543616,
			"seed": 854273250,
			"groupIds": [
				"tWNa7pMPLB8nmUnCfDAoF",
				"yiStG22UJ0wlT-h1C7B1J",
				"bp0bC5CUl5nDT-BiJ-2tp",
				"SnoAbrznAzV8b0BaMdRl0"
			],
			"frameId": "jerA-kzSGpDyDfhi2SeEA",
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1712826540976,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					-0.7891264851633601,
					-24.996263464941304
				],
				[
					-11.245052413572049,
					-37.77213145813402
				],
				[
					-31.78700123048332,
					-43.23108554817799
				],
				[
					-51.860406196815354,
					-37.79128568301108
				],
				[
					-62.11905050393612,
					-24.325865594233626
				],
				[
					-62.95791196418768,
					-3.6438015778128694
				],
				[
					-58.92382167639496,
					6.26909616725818
				]
			]
		},
		{
			"type": "line",
			"version": 2454,
			"versionNonce": 766710278,
			"isDeleted": false,
			"id": "v2vIb4VOCeB98jGkZ-pfg",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 6.279401307468326,
			"x": 479.7370662391787,
			"y": 1263.3980456573545,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"width": 62.95791196418768,
			"height": 49.50018171543617,
			"seed": 643041854,
			"groupIds": [
				"tCbOOPG_PxMj8sWjD91kM",
				"nJK6m7eCBfCkjG3CxkKq0",
				"cRa_KnpQNzS5M8t8IsX8z",
				"SnoAbrznAzV8b0BaMdRl0"
			],
			"frameId": "jerA-kzSGpDyDfhi2SeEA",
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1712826540976,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					0.7891264851633601,
					-24.996263464941304
				],
				[
					11.245052413572049,
					-37.77213145813402
				],
				[
					31.78700123048332,
					-43.23108554817799
				],
				[
					51.860406196815354,
					-37.79128568301108
				],
				[
					62.11905050393612,
					-24.325865594233626
				],
				[
					62.95791196418768,
					-3.6438015778128694
				],
				[
					58.92382167639496,
					6.26909616725818
				]
			]
		},
		{
			"type": "line",
			"version": 2409,
			"versionNonce": 138639706,
			"isDeleted": false,
			"id": "sSmP7ne2rjUmlUVn1rhX2",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 6.2794013074683335,
			"x": 596.8549008942813,
			"y": 1262.9477134863791,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"width": 62.95791196418768,
			"height": 49.50018171543616,
			"seed": 544686242,
			"groupIds": [
				"vziK9X5vqAY3PyMIRi2_o",
				"pbH9S9IEuBhmPqAAz4Z-x",
				"Zc-owYicppEF4ZWkfAkHV",
				"SnoAbrznAzV8b0BaMdRl0"
			],
			"frameId": "jerA-kzSGpDyDfhi2SeEA",
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1712826540976,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					-0.7891264851633601,
					-24.996263464941304
				],
				[
					-11.245052413572049,
					-37.77213145813402
				],
				[
					-31.78700123048332,
					-43.23108554817799
				],
				[
					-51.860406196815354,
					-37.79128568301108
				],
				[
					-62.11905050393612,
					-24.325865594233626
				],
				[
					-62.95791196418768,
					-3.6438015778128694
				],
				[
					-58.92382167639496,
					6.26909616725818
				]
			]
		},
		{
			"type": "line",
			"version": 1479,
			"versionNonce": 718201158,
			"isDeleted": false,
			"id": "ehfYIji7P2vbtTk37wuw5",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 6.279401307468326,
			"x": 655.3678091682092,
			"y": 1263.8293483282114,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"width": 58.5926147308669,
			"height": 0,
			"seed": 907285118,
			"groupIds": [
				"et3l0iNk6RGnL3F_ynCnP",
				"5crwYk2CAoet_zHTcSUBi",
				"SnoAbrznAzV8b0BaMdRl0"
			],
			"frameId": "jerA-kzSGpDyDfhi2SeEA",
			"roundness": null,
			"boundElements": [],
			"updated": 1712826540976,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					-58.5926147308669,
					0
				]
			]
		},
		{
			"type": "line",
			"version": 452,
			"versionNonce": 1459568154,
			"isDeleted": false,
			"id": "R6PQo9xBmJjr8HthtRRCA",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 397.66760111965846,
			"y": 1264.151056416819,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"width": 134.25921357852627,
			"height": 1.2317169371651744,
			"seed": 940783970,
			"groupIds": [],
			"frameId": "jerA-kzSGpDyDfhi2SeEA",
			"roundness": null,
			"boundElements": [],
			"updated": 1712826540976,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					-134.25921357852627,
					1.2317169371651744
				]
			]
		},
		{
			"type": "line",
			"version": 2453,
			"versionNonce": 170838150,
			"isDeleted": false,
			"id": "KPLA-SSS3ITvnkGDVruJM",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 9.437784544040007,
			"x": 534.089569406112,
			"y": 1201.123838387309,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 62.95791196418768,
			"height": 49.50018171543616,
			"seed": 1308434466,
			"groupIds": [
				"B9k5N1GIwgyC6whkdeAAF",
				"bWVuy9tV4r3KOn6DzTK5Q",
				"WnSzmCrsY_bXtjRpUKXIc",
				"5FtwGFsidzU-6nsSX-pTW"
			],
			"frameId": "jerA-kzSGpDyDfhi2SeEA",
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1712826540976,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					0.7891264851633601,
					-24.996263464941304
				],
				[
					11.245052413572049,
					-37.77213145813402
				],
				[
					31.78700123048332,
					-43.23108554817799
				],
				[
					51.860406196815354,
					-37.79128568301108
				],
				[
					62.11905050393612,
					-24.325865594233626
				],
				[
					62.95791196418768,
					-3.6438015778128694
				],
				[
					58.92382167639496,
					6.26909616725818
				]
			]
		},
		{
			"type": "line",
			"version": 1497,
			"versionNonce": 191130330,
			"isDeleted": false,
			"id": "fva49DVXdoRh9xkwtJA1h",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 9.437784544040007,
			"x": 657.1036692330815,
			"y": 1165.0100267603582,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 58.5926147308669,
			"height": 0,
			"seed": 1130941410,
			"groupIds": [
				"U9m0cDvF2Q6gVR2Fs-OOd",
				"6DwgdSCkstFYXnTXtKd9M",
				"5FtwGFsidzU-6nsSX-pTW"
			],
			"frameId": "jerA-kzSGpDyDfhi2SeEA",
			"roundness": null,
			"boundElements": [],
			"updated": 1712826540976,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					-58.5926147308669,
					0
				]
			]
		},
		{
			"type": "line",
			"version": 2567,
			"versionNonce": 462407622,
			"isDeleted": false,
			"id": "iXdhMqg-HB7Er3JgNP5i-",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 9.437784544040014,
			"x": 543.0574178447076,
			"y": 1201.1574503200363,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 62.95791196418768,
			"height": 49.50018171543616,
			"seed": 770244514,
			"groupIds": [
				"FBSJ6sX03bq9X3he3XpJN",
				"ZN8aptOTPSnqhn-W_4o-Q",
				"FGtBk9XiAQoRcYUS9spJk",
				"5FtwGFsidzU-6nsSX-pTW"
			],
			"frameId": "jerA-kzSGpDyDfhi2SeEA",
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1712826540976,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					-0.7891264851633601,
					-24.996263464941304
				],
				[
					-11.245052413572049,
					-37.77213145813402
				],
				[
					-31.78700123048332,
					-43.23108554817799
				],
				[
					-51.860406196815354,
					-37.79128568301108
				],
				[
					-62.11905050393612,
					-24.325865594233626
				],
				[
					-62.95791196418768,
					-3.6438015778128694
				],
				[
					-58.92382167639496,
					6.26909616725818
				]
			]
		},
		{
			"type": "line",
			"version": 2597,
			"versionNonce": 2080767898,
			"isDeleted": false,
			"id": "6jxemtXqeyrMtbSaqvE7F",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 9.437784544040007,
			"x": 479.6739355925197,
			"y": 1201.4008701301764,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 62.95791196418768,
			"height": 49.50018171543617,
			"seed": 162315106,
			"groupIds": [
				"ghrJ29MIy9J57lkcRB71s",
				"LDfYatdhDJD6-GkgDaO1J",
				"Ari77NDE9dAilfQpX6Jbj",
				"5FtwGFsidzU-6nsSX-pTW"
			],
			"frameId": "jerA-kzSGpDyDfhi2SeEA",
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1712826540976,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					0.7891264851633601,
					-24.996263464941304
				],
				[
					11.245052413572049,
					-37.77213145813402
				],
				[
					31.78700123048332,
					-43.23108554817799
				],
				[
					51.860406196815354,
					-37.79128568301108
				],
				[
					62.11905050393612,
					-24.325865594233626
				],
				[
					62.95791196418768,
					-3.6438015778128694
				],
				[
					58.92382167639496,
					6.26909616725818
				]
			]
		},
		{
			"type": "line",
			"version": 2552,
			"versionNonce": 789503750,
			"isDeleted": false,
			"id": "zp1xHWt4XMj2WHlRQ4mg1",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 9.437784544040014,
			"x": 488.8943545991018,
			"y": 1200.9453507638145,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 62.95791196418768,
			"height": 49.50018171543616,
			"seed": 1963130658,
			"groupIds": [
				"fkZkzQfgeO2i1wUh2xef_",
				"_ZnIG14KMVamuDJgkao7E",
				"vU6QZQwpzPczaJ-okR-6u",
				"5FtwGFsidzU-6nsSX-pTW"
			],
			"frameId": "jerA-kzSGpDyDfhi2SeEA",
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1712826540976,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					-0.7891264851633601,
					-24.996263464941304
				],
				[
					-11.245052413572049,
					-37.77213145813402
				],
				[
					-31.78700123048332,
					-43.23108554817799
				],
				[
					-51.860406196815354,
					-37.79128568301108
				],
				[
					-62.11905050393612,
					-24.325865594233626
				],
				[
					-62.95791196418768,
					-3.6438015778128694
				],
				[
					-58.92382167639496,
					6.26909616725818
				]
			]
		},
		{
			"type": "line",
			"version": 1622,
			"versionNonce": 890698842,
			"isDeleted": false,
			"id": "khxppLPlkKCd21mL7PISw",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 9.437784544040007,
			"x": 426.1386210307895,
			"y": 1162.0836136943817,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 58.5926147308669,
			"height": 0,
			"seed": 1817889506,
			"groupIds": [
				"sxTlUzZTGNTG1gEks3NJp",
				"RV2wDAwvDDM9GJW9wmGbJ",
				"5FtwGFsidzU-6nsSX-pTW"
			],
			"frameId": "jerA-kzSGpDyDfhi2SeEA",
			"roundness": null,
			"boundElements": [],
			"updated": 1712826540976,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					-58.5926147308669,
					0
				]
			]
		},
		{
			"type": "line",
			"version": 555,
			"versionNonce": 153685574,
			"isDeleted": false,
			"id": "QgB0vRz5lLzHStkuX3dSR",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 396.7041331334276,
			"y": 1160.9425103289107,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 134.25921357852627,
			"height": 1.2317169371651744,
			"seed": 105062050,
			"groupIds": [],
			"frameId": "jerA-kzSGpDyDfhi2SeEA",
			"roundness": null,
			"boundElements": [],
			"updated": 1712826540976,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					-134.25921357852627,
					1.2317169371651744
				]
			]
		},
		{
			"type": "line",
			"version": 406,
			"versionNonce": 1147822362,
			"isDeleted": false,
			"id": "W0ulPaymKJXiKgqPhzrmv",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 654.7300756669499,
			"y": 1165.720447368115,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 393.1418766870478,
			"height": 49.402897275028636,
			"seed": 529322146,
			"groupIds": [],
			"frameId": "jerA-kzSGpDyDfhi2SeEA",
			"roundness": null,
			"boundElements": [],
			"updated": 1712826540976,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					0.876379705584668,
					-47.32162919103507
				],
				[
					-392.2654969814631,
					-49.402897275028636
				]
			]
		},
		{
			"type": "ellipse",
			"version": 569,
			"versionNonce": 1455117702,
			"isDeleted": false,
			"id": "y_P7kd7_Kq9zICGV7YAK_",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 429.8764997591172,
			"y": 1283.1377678730526,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"width": 88.43424297394736,
			"height": 81.86621939644624,
			"seed": 1024381886,
			"groupIds": [],
			"frameId": "jerA-kzSGpDyDfhi2SeEA",
			"roundness": null,
			"boundElements": [],
			"updated": 1712826540976,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 245,
			"versionNonce": 91434458,
			"isDeleted": false,
			"id": "rNENdTVy",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 458.33299099921885,
			"y": 1295.022692503001,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"width": 30.46875,
			"height": 62.4,
			"seed": 106326206,
			"groupIds": [],
			"frameId": "jerA-kzSGpDyDfhi2SeEA",
			"roundness": null,
			"boundElements": [],
			"updated": 1712826540976,
			"link": null,
			"locked": false,
			"fontSize": 52,
			"fontFamily": 3,
			"text": "A",
			"rawText": "A",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "A",
			"lineHeight": 1.2,
			"baseline": 49
		},
		{
			"type": "line",
			"version": 283,
			"versionNonce": 553825478,
			"isDeleted": false,
			"id": "Eqsa8LEDZxsVXUWWTFbNa",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 431.627677186444,
			"y": 1327.792608564762,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"width": 168.9879704188707,
			"height": 0,
			"seed": 1241930366,
			"groupIds": [],
			"frameId": "jerA-kzSGpDyDfhi2SeEA",
			"roundness": null,
			"boundElements": [],
			"updated": 1712826540976,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					-168.9879704188707,
					0
				]
			]
		},
		{
			"type": "line",
			"version": 335,
			"versionNonce": 1833198234,
			"isDeleted": false,
			"id": "UqZZUzfa-hWnsr3_xzPxg",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 655.7775528609851,
			"y": 1262.9992775601916,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"width": 134.84016089019008,
			"height": 64.79333100457052,
			"seed": 1625218210,
			"groupIds": [],
			"frameId": "jerA-kzSGpDyDfhi2SeEA",
			"roundness": null,
			"boundElements": [],
			"updated": 1712826540976,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					0,
					63.042153577243425
				],
				[
					-134.84016089019008,
					64.79333100457052
				]
			]
		},
		{
			"type": "frame",
			"version": 30,
			"versionNonce": 1100753926,
			"isDeleted": false,
			"id": "2WcXcC6ozWX6UZtjXOLUt",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 222.5480350253697,
			"y": -1022.8001320942012,
			"strokeColor": "#bbb",
			"backgroundColor": "transparent",
			"width": 1032.6587438961878,
			"height": 622.2430827959593,
			"seed": 1900630882,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1712826540976,
			"link": null,
			"locked": false,
			"customData": {
				"frameColor": {
					"stroke": "#2B2B2B",
					"fill": "#525252",
					"nameColor": "#858585"
				}
			},
			"name": null
		},
		{
			"type": "frame",
			"version": 159,
			"versionNonce": 1452343130,
			"isDeleted": false,
			"id": "IagBYhze8sjgDkoZ4gj5i",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 19.546959317576466,
			"y": -307.8824365689411,
			"strokeColor": "#bbb",
			"backgroundColor": "transparent",
			"width": 1310.6822453934176,
			"height": 1147.3985482139856,
			"seed": 1422252514,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1712826540976,
			"link": null,
			"locked": false,
			"customData": {
				"frameColor": {
					"stroke": "#2B2B2B",
					"fill": "#525252",
					"nameColor": "#858585"
				}
			},
			"name": null
		},
		{
			"type": "text",
			"version": 537,
			"versionNonce": 1451539270,
			"isDeleted": false,
			"id": "eucYAiYg",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 1955.3721904520908,
			"y": -832.25354034908,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 297.3958740234375,
			"height": 45,
			"seed": 464758398,
			"groupIds": [],
			"frameId": "USCQ4VQrG23dpX1fI6OzG",
			"roundness": null,
			"boundElements": [],
			"updated": 1712826540976,
			"link": null,
			"locked": false,
			"fontSize": 36,
			"fontFamily": 1,
			"text": "Paket hinzufügen",
			"rawText": "Paket hinzufügen",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "Paket hinzufügen",
			"lineHeight": 1.25,
			"baseline": 32
		},
		{
			"type": "rectangle",
			"version": 735,
			"versionNonce": 1303118874,
			"isDeleted": false,
			"id": "o_WSLRdnnnf3JX4V2uTOv",
			"fillStyle": "cross-hatch",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 1980.8323284513253,
			"y": -724.104471197595,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "#ff8787",
			"width": 232.800048828125,
			"height": 140.79998779296872,
			"seed": 1303783102,
			"groupIds": [],
			"frameId": "USCQ4VQrG23dpX1fI6OzG",
			"roundness": {
				"type": 3
			},
			"boundElements": [
				{
					"type": "text",
					"id": "MbMNdj6L"
				},
				{
					"id": "TzIRrHT83YKIImLndK4l6",
					"type": "arrow"
				},
				{
					"id": "2o2cCu96Xa46EpdxmHTmo",
					"type": "arrow"
				},
				{
					"id": "5pltV6RBSRITOddCQfivD",
					"type": "arrow"
				},
				{
					"id": "krFiiEK4DaYJcHdYtX9an",
					"type": "arrow"
				},
				{
					"id": "rTng_lWavz7Ytq1IGrWrX",
					"type": "arrow"
				}
			],
			"updated": 1712826540976,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 603,
			"versionNonce": 907633286,
			"isDeleted": false,
			"id": "MbMNdj6L",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 2016.0703731900949,
			"y": -698.7044773011106,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 162.32395935058594,
			"height": 90,
			"seed": 1409195774,
			"groupIds": [],
			"frameId": "USCQ4VQrG23dpX1fI6OzG",
			"roundness": null,
			"boundElements": [],
			"updated": 1712826540976,
			"link": null,
			"locked": false,
			"fontSize": 36,
			"fontFamily": 1,
			"text": "Haupt\nProgramm",
			"rawText": "Haupt\nProgramm",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "o_WSLRdnnnf3JX4V2uTOv",
			"originalText": "Haupt\nProgramm",
			"lineHeight": 1.25,
			"baseline": 77
		},
		{
			"type": "rectangle",
			"version": 922,
			"versionNonce": 1552445658,
			"isDeleted": false,
			"id": "IiaC57xg-CAkmuqpKGejJ",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 2609.7590208612773,
			"y": -731.5962170567086,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 232.68296337689117,
			"height": 145,
			"seed": 588123966,
			"groupIds": [],
			"frameId": "USCQ4VQrG23dpX1fI6OzG",
			"roundness": {
				"type": 3
			},
			"boundElements": [
				{
					"type": "text",
					"id": "s0b7IRmx"
				},
				{
					"id": "TzIRrHT83YKIImLndK4l6",
					"type": "arrow"
				},
				{
					"id": "krFiiEK4DaYJcHdYtX9an",
					"type": "arrow"
				}
			],
			"updated": 1712826540976,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 804,
			"versionNonce": 1662460358,
			"isDeleted": false,
			"id": "s0b7IRmx",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 2633.3105321517737,
			"y": -704.0962170567086,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 185.57994079589844,
			"height": 90,
			"seed": 2001041278,
			"groupIds": [],
			"frameId": "USCQ4VQrG23dpX1fI6OzG",
			"roundness": null,
			"boundElements": [],
			"updated": 1712826540976,
			"link": null,
			"locked": false,
			"fontSize": 36,
			"fontFamily": 1,
			"text": "SQL\nDatenbank",
			"rawText": "SQL Datenbank",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "IiaC57xg-CAkmuqpKGejJ",
			"originalText": "SQL Datenbank",
			"lineHeight": 1.25,
			"baseline": 77
		},
		{
			"type": "rectangle",
			"version": 652,
			"versionNonce": 1454982554,
			"isDeleted": false,
			"id": "12UIdako53uO-SoVizW7B",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 1657.91247983937,
			"y": -700.3545263124104,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 158.89776114277035,
			"height": 91.81776310571388,
			"seed": 1491457982,
			"groupIds": [],
			"frameId": "USCQ4VQrG23dpX1fI6OzG",
			"roundness": {
				"type": 3
			},
			"boundElements": [
				{
					"type": "text",
					"id": "tHKbBkiq"
				},
				{
					"id": "2o2cCu96Xa46EpdxmHTmo",
					"type": "arrow"
				},
				{
					"id": "5pltV6RBSRITOddCQfivD",
					"type": "arrow"
				},
				{
					"id": "Z_ggFUbXLxo2Uu5iMoMZZ",
					"type": "arrow"
				},
				{
					"id": "ZMSoxaGJRVqF8cjMAGs4b",
					"type": "arrow"
				},
				{
					"id": "rTng_lWavz7Ytq1IGrWrX",
					"type": "arrow"
				},
				{
					"id": "HxTi6vGofjcUaLbJPS9un",
					"type": "arrow"
				}
			],
			"updated": 1712826540976,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 631,
			"versionNonce": 10156294,
			"isDeleted": false,
			"id": "tHKbBkiq",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 1675.0273760357552,
			"y": -676.9456447595535,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 124.66796875,
			"height": 45,
			"seed": 537931774,
			"groupIds": [],
			"frameId": "USCQ4VQrG23dpX1fI6OzG",
			"roundness": null,
			"boundElements": [],
			"updated": 1712826540976,
			"link": null,
			"locked": false,
			"fontSize": 36,
			"fontFamily": 1,
			"text": "Arduino",
			"rawText": "Arduino",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "12UIdako53uO-SoVizW7B",
			"originalText": "Arduino",
			"lineHeight": 1.25,
			"baseline": 32
		},
		{
			"type": "arrow",
			"version": 2346,
			"versionNonce": 1027547001,
			"isDeleted": false,
			"id": "TzIRrHT83YKIImLndK4l6",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 2228.706729345544,
			"y": -689.1619946549407,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 370.51321175590056,
			"height": 14.109441335827682,
			"seed": 2026209342,
			"groupIds": [],
			"frameId": "USCQ4VQrG23dpX1fI6OzG",
			"roundness": {
				"type": 2
			},
			"boundElements": [
				{
					"type": "text",
					"id": "07t0Ux5A"
				}
			],
			"updated": 1713771496250,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "o_WSLRdnnnf3JX4V2uTOv",
				"gap": 15.074352066093525,
				"focus": -0.4069198058147243
			},
			"endBinding": {
				"elementId": "IiaC57xg-CAkmuqpKGejJ",
				"gap": 10.53907975983293,
				"focus": 0.637029669978335
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					370.51321175590056,
					-14.109441335827682
				]
			]
		},
		{
			"type": "text",
			"version": 361,
			"versionNonce": 1176627270,
			"isDeleted": false,
			"id": "07t0Ux5A",
			"fillStyle": "cross-hatch",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 1739.7034551575762,
			"y": -513.2167153228545,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 158.11985778808594,
			"height": 50,
			"seed": 1726400638,
			"groupIds": [],
			"frameId": "USCQ4VQrG23dpX1fI6OzG",
			"roundness": null,
			"boundElements": [],
			"updated": 1712826540976,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "Anfrage der\nPaketparameter",
			"rawText": "Anfrage der Paketparameter",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "TzIRrHT83YKIImLndK4l6",
			"originalText": "Anfrage der Paketparameter",
			"lineHeight": 1.25,
			"baseline": 43
		},
		{
			"type": "arrow",
			"version": 1794,
			"versionNonce": 1214978809,
			"isDeleted": false,
			"id": "2o2cCu96Xa46EpdxmHTmo",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 1968.8071702650486,
			"y": -653.7558723521416,
			"strokeColor": "#2f9e44",
			"backgroundColor": "transparent",
			"width": 139.35394289915666,
			"height": 1.1554576486968244,
			"seed": 1244989630,
			"groupIds": [],
			"frameId": "USCQ4VQrG23dpX1fI6OzG",
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1713771496250,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "o_WSLRdnnnf3JX4V2uTOv",
				"gap": 12.025158186276713,
				"focus": 0.01564120406174326
			},
			"endBinding": {
				"elementId": "12UIdako53uO-SoVizW7B",
				"gap": 12.64298638375135,
				"focus": 0.05602201462114541
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					-139.35394289915666,
					1.1554576486968244
				]
			]
		},
		{
			"type": "arrow",
			"version": 1790,
			"versionNonce": 379154617,
			"isDeleted": false,
			"id": "5pltV6RBSRITOddCQfivD",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 1825.2880540437661,
			"y": -669.6891008550499,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 132.5898336311309,
			"height": 3.139139651269943,
			"seed": 1649492222,
			"groupIds": [],
			"frameId": "USCQ4VQrG23dpX1fI6OzG",
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1713771496250,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "12UIdako53uO-SoVizW7B",
				"gap": 8.477813061625739,
				"focus": -0.2754085583129834
			},
			"endBinding": {
				"elementId": "o_WSLRdnnnf3JX4V2uTOv",
				"gap": 22.954440776428328,
				"focus": 0.3065108982274966
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					132.5898336311309,
					-3.139139651269943
				]
			]
		},
		{
			"type": "arrow",
			"version": 2165,
			"versionNonce": 1486247225,
			"isDeleted": false,
			"id": "krFiiEK4DaYJcHdYtX9an",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 2597.8900751829674,
			"y": -609.5120491822526,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 367.60651609583647,
			"height": 7.705526704543786,
			"seed": 1388081470,
			"groupIds": [],
			"frameId": "USCQ4VQrG23dpX1fI6OzG",
			"roundness": {
				"type": 2
			},
			"boundElements": [
				{
					"type": "text",
					"id": "Dfz58J30"
				}
			],
			"updated": 1713771496250,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "IiaC57xg-CAkmuqpKGejJ",
				"gap": 11.868945678309956,
				"focus": -0.6258011061179128
			},
			"endBinding": {
				"elementId": "o_WSLRdnnnf3JX4V2uTOv",
				"gap": 16.651181807680587,
				"focus": 0.7507820686359143
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					-367.60651609583647,
					7.705526704543786
				]
			]
		},
		{
			"type": "text",
			"version": 383,
			"versionNonce": 1158483654,
			"isDeleted": false,
			"id": "Dfz58J30",
			"fillStyle": "cross-hatch",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 1755.3169196741117,
			"y": -422.6592858299806,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 127.139892578125,
			"height": 50,
			"seed": 651663742,
			"groupIds": [],
			"frameId": "USCQ4VQrG23dpX1fI6OzG",
			"roundness": null,
			"boundElements": [],
			"updated": 1712826540977,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "Übergabe der\nParameter",
			"rawText": "Übergabe der\nParameter",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "krFiiEK4DaYJcHdYtX9an",
			"originalText": "Übergabe der\nParameter",
			"lineHeight": 1.25,
			"baseline": 43
		},
		{
			"type": "text",
			"version": 607,
			"versionNonce": 690268314,
			"isDeleted": false,
			"id": "lT2mLICk",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 2060.0013261828412,
			"y": -772.0049009467606,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 73.72798156738281,
			"height": 45,
			"seed": 1440987582,
			"groupIds": [],
			"frameId": "USCQ4VQrG23dpX1fI6OzG",
			"roundness": null,
			"boundElements": [],
			"updated": 1712826540977,
			"link": null,
			"locked": false,
			"fontSize": 36,
			"fontFamily": 1,
			"text": "GUI",
			"rawText": "GUI",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "GUI",
			"lineHeight": 1.25,
			"baseline": 32
		},
		{
			"type": "rectangle",
			"version": 805,
			"versionNonce": 1732986374,
			"isDeleted": false,
			"id": "ISnOHbpQ23D16ZmrDCtJL",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 1553.3654153871912,
			"y": -494.2701179666316,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 131.02445030573122,
			"height": 79.82037012077393,
			"seed": 1191301630,
			"groupIds": [],
			"frameId": "USCQ4VQrG23dpX1fI6OzG",
			"roundness": {
				"type": 3
			},
			"boundElements": [
				{
					"type": "text",
					"id": "MtnSI1s9"
				},
				{
					"id": "Z_ggFUbXLxo2Uu5iMoMZZ",
					"type": "arrow"
				}
			],
			"updated": 1712826540977,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 858,
			"versionNonce": 2054718810,
			"isDeleted": false,
			"id": "MtnSI1s9",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 1577.7976768559747,
			"y": -479.3599329062446,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 82.15992736816406,
			"height": 50,
			"seed": 1429398078,
			"groupIds": [],
			"frameId": "USCQ4VQrG23dpX1fI6OzG",
			"roundness": null,
			"boundElements": [],
			"updated": 1712826540977,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "QR-Code\nScanner",
			"rawText": "QR-Code Scanner",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "ISnOHbpQ23D16ZmrDCtJL",
			"originalText": "QR-Code Scanner",
			"lineHeight": 1.25,
			"baseline": 43
		},
		{
			"type": "arrow",
			"version": 1541,
			"versionNonce": 332696953,
			"isDeleted": false,
			"id": "Z_ggFUbXLxo2Uu5iMoMZZ",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 1613.2262381458977,
			"y": -498.48866254080644,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 113.50046714435234,
			"height": 99.26097932922812,
			"seed": 1398270590,
			"groupIds": [],
			"frameId": "USCQ4VQrG23dpX1fI6OzG",
			"roundness": {
				"type": 2
			},
			"boundElements": [
				{
					"type": "text",
					"id": "0mWuzhvF"
				}
			],
			"updated": 1713771496251,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "ISnOHbpQ23D16ZmrDCtJL",
				"gap": 4.218544574174899,
				"focus": -0.5048292216643319
			},
			"endBinding": {
				"elementId": "12UIdako53uO-SoVizW7B",
				"gap": 10.787121336661983,
				"focus": -0.41074114913095244
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					113.50046714435234,
					-99.26097932922812
				]
			]
		},
		{
			"type": "text",
			"version": 285,
			"versionNonce": 1454557722,
			"isDeleted": false,
			"id": "0mWuzhvF",
			"fillStyle": "cross-hatch",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 1017.0465705950269,
			"y": -365.1191522054204,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 115.45989990234375,
			"height": 50,
			"seed": 271706814,
			"groupIds": [],
			"frameId": "USCQ4VQrG23dpX1fI6OzG",
			"roundness": null,
			"boundElements": [],
			"updated": 1712826540977,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "Einlesen der\nPaket-ID",
			"rawText": "Einlesen der\nPaket-ID",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "Z_ggFUbXLxo2Uu5iMoMZZ",
			"originalText": "Einlesen der\nPaket-ID",
			"lineHeight": 1.25,
			"baseline": 43
		},
		{
			"type": "rectangle",
			"version": 281,
			"versionNonce": 977927302,
			"isDeleted": false,
			"id": "tdQWym0eNkKvEEC0rxgDY",
			"fillStyle": "cross-hatch",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 1587.4841376626114,
			"y": -320.41558268513006,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "#4dabf7",
			"width": 254.10803286733676,
			"height": 88.34217731905281,
			"seed": 1516364542,
			"groupIds": [],
			"frameId": "USCQ4VQrG23dpX1fI6OzG",
			"roundness": null,
			"boundElements": [
				{
					"type": "text",
					"id": "87L0f9Hv"
				}
			],
			"updated": 1712826540977,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 250,
			"versionNonce": 1690728154,
			"isDeleted": false,
			"id": "87L0f9Hv",
			"fillStyle": "cross-hatch",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 1619.8002009102447,
			"y": -311.2444940256037,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "#a5d8ff",
			"width": 189.4759063720703,
			"height": 70,
			"seed": 73978686,
			"groupIds": [],
			"frameId": "USCQ4VQrG23dpX1fI6OzG",
			"roundness": null,
			"boundElements": [],
			"updated": 1712826540977,
			"link": null,
			"locked": false,
			"fontSize": 28,
			"fontFamily": 1,
			"text": "Erkennung des\nPakets",
			"rawText": "Erkennung des Pakets",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "tdQWym0eNkKvEEC0rxgDY",
			"originalText": "Erkennung des Pakets",
			"lineHeight": 1.25,
			"baseline": 59
		},
		{
			"type": "rectangle",
			"version": 345,
			"versionNonce": 170163142,
			"isDeleted": false,
			"id": "TCMMRKKiDLDPTv_Qf7qg_",
			"fillStyle": "cross-hatch",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 1843.5773212021513,
			"y": -275.6966511369102,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "#ff8787",
			"width": 529.0608104310902,
			"height": 43.12567024312421,
			"seed": 1755822974,
			"groupIds": [],
			"frameId": "USCQ4VQrG23dpX1fI6OzG",
			"roundness": null,
			"boundElements": [
				{
					"type": "text",
					"id": "WockAW8N"
				}
			],
			"updated": 1712826540977,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 352,
			"versionNonce": 1967557530,
			"isDeleted": false,
			"id": "WockAW8N",
			"fillStyle": "cross-hatch",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 1856.6379540788294,
			"y": -266.6338160153481,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "#ffc9c9",
			"width": 502.9395446777344,
			"height": 25,
			"seed": 1834982334,
			"groupIds": [],
			"frameId": "USCQ4VQrG23dpX1fI6OzG",
			"roundness": null,
			"boundElements": [],
			"updated": 1712826540977,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "Erstellen eines Objektes für den Timer des Pakets",
			"rawText": "Erstellen eines Objektes für den Timer des Pakets",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "TCMMRKKiDLDPTv_Qf7qg_",
			"originalText": "Erstellen eines Objektes für den Timer des Pakets",
			"lineHeight": 1.25,
			"baseline": 18
		},
		{
			"type": "rectangle",
			"version": 659,
			"versionNonce": 1357714182,
			"isDeleted": false,
			"id": "ILNNYDyfsF3ZJbh3vapga",
			"fillStyle": "cross-hatch",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 1460.0600773997965,
			"y": -676.910227541703,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 101.246130001432,
			"height": 45,
			"seed": 145847294,
			"groupIds": [],
			"frameId": "USCQ4VQrG23dpX1fI6OzG",
			"roundness": {
				"type": 3
			},
			"boundElements": [
				{
					"type": "text",
					"id": "lwNZtne4"
				},
				{
					"id": "ZMSoxaGJRVqF8cjMAGs4b",
					"type": "arrow"
				}
			],
			"updated": 1712826540977,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 649,
			"versionNonce": 1315309658,
			"isDeleted": false,
			"id": "lwNZtne4",
			"fillStyle": "cross-hatch",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 1474.339155889282,
			"y": -671.910227541703,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 72.68797302246094,
			"height": 35,
			"seed": 1151222846,
			"groupIds": [],
			"frameId": "USCQ4VQrG23dpX1fI6OzG",
			"roundness": null,
			"boundElements": [],
			"updated": 1712826540977,
			"link": null,
			"locked": false,
			"fontSize": 28,
			"fontFamily": 1,
			"text": "LEDs",
			"rawText": "LEDs",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "ILNNYDyfsF3ZJbh3vapga",
			"originalText": "LEDs",
			"lineHeight": 1.25,
			"baseline": 24
		},
		{
			"type": "arrow",
			"version": 1624,
			"versionNonce": 1596474169,
			"isDeleted": false,
			"id": "ZMSoxaGJRVqF8cjMAGs4b",
			"fillStyle": "cross-hatch",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 1646.6706776444976,
			"y": -651.4633156063969,
			"strokeColor": "#2f9e44",
			"backgroundColor": "transparent",
			"width": 77.42356463409897,
			"height": 4.621650145637432,
			"seed": 1124535422,
			"groupIds": [],
			"frameId": "USCQ4VQrG23dpX1fI6OzG",
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1713771496251,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "12UIdako53uO-SoVizW7B",
				"gap": 11.241802194872662,
				"focus": -0.16575908029033767
			},
			"endBinding": {
				"elementId": "ILNNYDyfsF3ZJbh3vapga",
				"gap": 7.940905609170159,
				"focus": -0.2025951140452286
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					-77.42356463409897,
					-4.621650145637432
				]
			]
		},
		{
			"type": "rectangle",
			"version": 402,
			"versionNonce": 2012736794,
			"isDeleted": false,
			"id": "ohLes0qXLLXl6NSeLGMDI",
			"fillStyle": "cross-hatch",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 1844.3217290385755,
			"y": -320.8855434756414,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "#2f9e44",
			"width": 529.0608104310902,
			"height": 43.12567024312421,
			"seed": 1101843646,
			"groupIds": [],
			"frameId": "USCQ4VQrG23dpX1fI6OzG",
			"roundness": null,
			"boundElements": [
				{
					"type": "text",
					"id": "276Ci32i"
				}
			],
			"updated": 1712826540977,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 448,
			"versionNonce": 362580358,
			"isDeleted": false,
			"id": "276Ci32i",
			"fillStyle": "cross-hatch",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 1952.2222514416208,
			"y": -311.8227083540793,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "#ffc9c9",
			"width": 313.259765625,
			"height": 25,
			"seed": 506496254,
			"groupIds": [],
			"frameId": "USCQ4VQrG23dpX1fI6OzG",
			"roundness": null,
			"boundElements": [],
			"updated": 1712826540977,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "Indikator für Paket Einlagerung",
			"rawText": "Indikator für Paket Einlagerung",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "ohLes0qXLLXl6NSeLGMDI",
			"originalText": "Indikator für Paket Einlagerung",
			"lineHeight": 1.25,
			"baseline": 18
		},
		{
			"type": "arrow",
			"version": 374,
			"versionNonce": 124729818,
			"isDeleted": false,
			"id": "xWvKqZ7BdH0CEdBIO8eyT",
			"fillStyle": "cross-hatch",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 1553.3049539582844,
			"y": -332.29818030849816,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "#2f9e44",
			"width": 1181.6356897493165,
			"height": 1.021355059011114,
			"seed": 1511208254,
			"groupIds": [],
			"frameId": "USCQ4VQrG23dpX1fI6OzG",
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1712826540977,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					1181.6356897493165,
					-1.021355059011114
				]
			]
		},
		{
			"type": "text",
			"version": 248,
			"versionNonce": 1436379334,
			"isDeleted": false,
			"id": "v1lvIjmf",
			"fillStyle": "cross-hatch",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 2013.3134780948444,
			"y": -373.02391195318285,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "#2f9e44",
			"width": 303.6318664550781,
			"height": 35,
			"seed": 515235198,
			"groupIds": [],
			"frameId": "USCQ4VQrG23dpX1fI6OzG",
			"roundness": null,
			"boundElements": [],
			"updated": 1712826540977,
			"link": null,
			"locked": false,
			"fontSize": 28,
			"fontFamily": 1,
			"text": "Chronologischer Ablauf",
			"rawText": "Chronologischer Ablauf",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "Chronologischer Ablauf",
			"lineHeight": 1.25,
			"baseline": 24
		},
		{
			"type": "rectangle",
			"version": 2204,
			"versionNonce": 1809772186,
			"isDeleted": false,
			"id": "xGu_6VgRY435jp8fcWMCZ",
			"fillStyle": "cross-hatch",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 2385.045919708964,
			"y": -318.9266534171496,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "#a24db3",
			"width": 306.71636213538955,
			"height": 88.34217731905281,
			"seed": 1096383934,
			"groupIds": [],
			"frameId": "USCQ4VQrG23dpX1fI6OzG",
			"roundness": null,
			"boundElements": [
				{
					"type": "text",
					"id": "rEbcWyXd"
				}
			],
			"updated": 1712826540977,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 394,
			"versionNonce": 2025873414,
			"isDeleted": false,
			"id": "rEbcWyXd",
			"fillStyle": "cross-hatch",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 2398.5581535110337,
			"y": -292.25556475762323,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "#a5d8ff",
			"width": 279.69189453125,
			"height": 35,
			"seed": 1193219582,
			"groupIds": [],
			"frameId": "USCQ4VQrG23dpX1fI6OzG",
			"roundness": null,
			"boundElements": [],
			"updated": 1712826540977,
			"link": null,
			"locked": false,
			"fontSize": 28,
			"fontFamily": 1,
			"text": "Auswurf des Pakets",
			"rawText": "Auswurf des Pakets",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "xGu_6VgRY435jp8fcWMCZ",
			"originalText": "Auswurf des Pakets",
			"lineHeight": 1.25,
			"baseline": 24
		},
		{
			"type": "arrow",
			"version": 1496,
			"versionNonce": 1893061113,
			"isDeleted": false,
			"id": "rTng_lWavz7Ytq1IGrWrX",
			"fillStyle": "cross-hatch",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 1968.2761431344697,
			"y": -637.0829780796087,
			"strokeColor": "#ac60bb",
			"backgroundColor": "#a24db3",
			"width": 136.9801295126083,
			"height": 2.196094568669082,
			"seed": 1762108990,
			"groupIds": [],
			"frameId": "USCQ4VQrG23dpX1fI6OzG",
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1713771496251,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "o_WSLRdnnnf3JX4V2uTOv",
				"gap": 12.55618531685559,
				"focus": -0.20139508028569186
			},
			"endBinding": {
				"elementId": "12UIdako53uO-SoVizW7B",
				"gap": 14.485772639720835,
				"focus": 0.4464512629956613
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					-136.9801295126083,
					2.196094568669082
				]
			]
		},
		{
			"type": "rectangle",
			"version": 1059,
			"versionNonce": 50491206,
			"isDeleted": false,
			"id": "ygFvF6JNRoJ0s3mc0SHvp",
			"fillStyle": "cross-hatch",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 1581.2041527390672,
			"y": -896.5473180378474,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 155.83964780673296,
			"height": 82.38659277478573,
			"seed": 401878654,
			"groupIds": [],
			"frameId": "USCQ4VQrG23dpX1fI6OzG",
			"roundness": {
				"type": 3
			},
			"boundElements": [
				{
					"type": "text",
					"id": "OLJwWnoQ"
				},
				{
					"id": "HxTi6vGofjcUaLbJPS9un",
					"type": "arrow"
				}
			],
			"updated": 1712826540977,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 1035,
			"versionNonce": 2014547994,
			"isDeleted": false,
			"id": "OLJwWnoQ",
			"fillStyle": "cross-hatch",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 1589.22999470884,
			"y": -877.8540216504546,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 139.7879638671875,
			"height": 45,
			"seed": 10858174,
			"groupIds": [],
			"frameId": "USCQ4VQrG23dpX1fI6OzG",
			"roundness": null,
			"boundElements": [],
			"updated": 1712826540977,
			"link": null,
			"locked": false,
			"fontSize": 36,
			"fontFamily": 1,
			"text": "Motoren",
			"rawText": "Motoren",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "ygFvF6JNRoJ0s3mc0SHvp",
			"originalText": "Motoren",
			"lineHeight": 1.25,
			"baseline": 32
		},
		{
			"type": "arrow",
			"version": 2494,
			"versionNonce": 165251321,
			"isDeleted": false,
			"id": "HxTi6vGofjcUaLbJPS9un",
			"fillStyle": "cross-hatch",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 1731.2745302482645,
			"y": -709.6662927868307,
			"strokeColor": "#ac60bb",
			"backgroundColor": "transparent",
			"width": 37.00282439088278,
			"height": 94.56828153224649,
			"seed": 264054526,
			"groupIds": [],
			"frameId": "USCQ4VQrG23dpX1fI6OzG",
			"roundness": {
				"type": 2
			},
			"boundElements": [
				{
					"type": "text",
					"id": "ybbLxPvq"
				}
			],
			"updated": 1713771496251,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "12UIdako53uO-SoVizW7B",
				"gap": 9.311766474420267,
				"focus": 0.15932290063010027
			},
			"endBinding": {
				"elementId": "ygFvF6JNRoJ0s3mc0SHvp",
				"gap": 9.92615094398451,
				"focus": -0.1610586372658212
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					-37.00282439088278,
					-94.56828153224649
				]
			]
		},
		{
			"type": "text",
			"version": 305,
			"versionNonce": 1780382938,
			"isDeleted": false,
			"id": "ybbLxPvq",
			"fillStyle": "cross-hatch",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 1016.7932564645575,
			"y": -573.9504335529539,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 201.55984497070312,
			"height": 50,
			"seed": 1975228222,
			"groupIds": [],
			"frameId": "USCQ4VQrG23dpX1fI6OzG",
			"roundness": null,
			"boundElements": [],
			"updated": 1712826540977,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "Ansteuerung für\nAusgabe (DRV8825)",
			"rawText": "Ansteuerung für Ausgabe (DRV8825)",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "HxTi6vGofjcUaLbJPS9un",
			"originalText": "Ansteuerung für Ausgabe (DRV8825)",
			"lineHeight": 1.25,
			"baseline": 43
		},
		{
			"type": "line",
			"version": 249,
			"versionNonce": 716690886,
			"isDeleted": false,
			"id": "4RicNSiKx4k-o9ZLm98xH",
			"fillStyle": "cross-hatch",
			"strokeWidth": 4,
			"strokeStyle": "dashed",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 2378.593924435252,
			"y": -366.07560061263666,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 2.2737367544323206e-13,
			"height": 172.71405329369702,
			"seed": 721551230,
			"groupIds": [],
			"frameId": "USCQ4VQrG23dpX1fI6OzG",
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1712826540977,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					2.2737367544323206e-13,
					172.71405329369702
				]
			]
		},
		{
			"type": "text",
			"version": 289,
			"versionNonce": 1571672474,
			"isDeleted": false,
			"id": "2ZvecqaU",
			"fillStyle": "cross-hatch",
			"strokeWidth": 4,
			"strokeStyle": "dashed",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 2292.2367841932714,
			"y": -181.4502646352729,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 189.6598358154297,
			"height": 25,
			"seed": 1943101374,
			"groupIds": [],
			"frameId": "USCQ4VQrG23dpX1fI6OzG",
			"roundness": null,
			"boundElements": [],
			"updated": 1712826540977,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "Befehl für Ausgabe",
			"rawText": "Befehl für Ausgabe",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "Befehl für Ausgabe",
			"lineHeight": 1.25,
			"baseline": 18
		},
		{
			"type": "text",
			"version": 304,
			"versionNonce": 2047159558,
			"isDeleted": false,
			"id": "wA5W8k1o",
			"fillStyle": "cross-hatch",
			"strokeWidth": 4,
			"strokeStyle": "dashed",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 1916.3157344899782,
			"y": -80.61096623129777,
			"strokeColor": "#6899db",
			"backgroundColor": "transparent",
			"width": 386.5318908691406,
			"height": 45,
			"seed": 1682618366,
			"groupIds": [],
			"frameId": "USCQ4VQrG23dpX1fI6OzG",
			"roundness": null,
			"boundElements": [],
			"updated": 1712826540977,
			"link": null,
			"locked": false,
			"fontSize": 36,
			"fontFamily": 1,
			"text": "Erkennung des Pakets",
			"rawText": "Erkennung des Pakets",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "Erkennung des Pakets",
			"lineHeight": 1.25,
			"baseline": 32
		},
		{
			"type": "line",
			"version": 491,
			"versionNonce": 1978961498,
			"isDeleted": false,
			"id": "9tBnn0t9vpPHXwdNZuKlr",
			"fillStyle": "cross-hatch",
			"strokeWidth": 4,
			"strokeStyle": "dashed",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 1895.8156255735805,
			"y": -740.4372073597541,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0,
			"height": 181.6475153064473,
			"seed": 1684998206,
			"groupIds": [],
			"frameId": "USCQ4VQrG23dpX1fI6OzG",
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1712826540977,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					0,
					181.6475153064473
				]
			]
		},
		{
			"type": "text",
			"version": 556,
			"versionNonce": 2082839622,
			"isDeleted": false,
			"id": "ejGw5pLl",
			"fillStyle": "cross-hatch",
			"strokeWidth": 4,
			"strokeStyle": "dashed",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 1765.4347553372886,
			"y": -548.8635979068886,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 200.13978576660156,
			"height": 50,
			"seed": 874467454,
			"groupIds": [],
			"frameId": "USCQ4VQrG23dpX1fI6OzG",
			"roundness": null,
			"boundElements": [],
			"updated": 1712826540977,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "serielle Schnittstelle\n(USB)",
			"rawText": "serielle Schnittstelle\n(USB)",
			"textAlign": "center",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "serielle Schnittstelle\n(USB)",
			"lineHeight": 1.25,
			"baseline": 43
		},
		{
			"type": "text",
			"version": 1184,
			"versionNonce": 2009445146,
			"isDeleted": false,
			"id": "6sHQiV6l",
			"fillStyle": "cross-hatch",
			"strokeWidth": 4,
			"strokeStyle": "dashed",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 1588.6462204587353,
			"y": -27.320718010406722,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1096.2191162109375,
			"height": 100,
			"seed": 1864143038,
			"groupIds": [],
			"frameId": "USCQ4VQrG23dpX1fI6OzG",
			"roundness": null,
			"boundElements": [],
			"updated": 1712826540977,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "Mit dem QR-Code-Scanner wird die ID des Pakets eingelesen und über die serielle Schnittstelle an das\nHauptprogramm(Computer) weiter gegeben. Von dort aus wird eine Anfrage an die SQL Datenbank \nfür die eingelesene ID gestartet. Die Datenbank antwortet mit allen Parameter(Eigenschaften) des Paketes. \n ",
			"rawText": "Mit dem QR-Code-Scanner wird die ID des Pakets eingelesen und über die serielle Schnittstelle an das\nHauptprogramm(Computer) weiter gegeben. Von dort aus wird eine Anfrage an die SQL Datenbank \nfür die eingelesene ID gestartet. Die Datenbank antwortet mit allen Parameter(Eigenschaften) des Paketes. \n ",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "Mit dem QR-Code-Scanner wird die ID des Pakets eingelesen und über die serielle Schnittstelle an das\nHauptprogramm(Computer) weiter gegeben. Von dort aus wird eine Anfrage an die SQL Datenbank \nfür die eingelesene ID gestartet. Die Datenbank antwortet mit allen Parameter(Eigenschaften) des Paketes. \n ",
			"lineHeight": 1.25,
			"baseline": 93
		},
		{
			"type": "text",
			"version": 302,
			"versionNonce": 1682556178,
			"isDeleted": false,
			"id": "Z0mODqRe",
			"fillStyle": "cross-hatch",
			"strokeWidth": 4,
			"strokeStyle": "dashed",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 1867.400000164618,
			"y": 105.09176012393107,
			"strokeColor": "#2f9e44",
			"backgroundColor": "transparent",
			"width": 563.867578125,
			"height": 45,
			"seed": 285722878,
			"groupIds": [],
			"frameId": "USCQ4VQrG23dpX1fI6OzG",
			"roundness": null,
			"boundElements": [],
			"updated": 1713620703159,
			"link": null,
			"locked": false,
			"fontSize": 36,
			"fontFamily": 1,
			"text": "Indikator für Paket Einlagerung",
			"rawText": "Indikator für Paket Einlagerung",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "Indikator für Paket Einlagerung",
			"lineHeight": 1.25,
			"baseline": 32
		},
		{
			"type": "text",
			"version": 807,
			"versionNonce": 362037210,
			"isDeleted": false,
			"id": "8n0EDKX1",
			"fillStyle": "cross-hatch",
			"strokeWidth": 4,
			"strokeStyle": "dashed",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 1591.4957933112573,
			"y": 358.79609347152666,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1080.71923828125,
			"height": 50,
			"seed": 2036463934,
			"groupIds": [],
			"frameId": "USCQ4VQrG23dpX1fI6OzG",
			"roundness": null,
			"boundElements": [],
			"updated": 1712826540977,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "Im Hauptprogramm wird ein Objekt für jedes Paket erstellt, dass die Parameter der Datenbank übernimmt.\nJedes Paket hat eine mit der Fälligkeitsdatum berechnete Ablaufzeit, nach der sortiert und eingelagert wird.",
			"rawText": "Im Hauptprogramm wird ein Objekt für jedes Paket erstellt, dass die Parameter der Datenbank übernimmt.\nJedes Paket hat eine mit der Fälligkeitsdatum berechnete Ablaufzeit, nach der sortiert und eingelagert wird.",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "Im Hauptprogramm wird ein Objekt für jedes Paket erstellt, dass die Parameter der Datenbank übernimmt.\nJedes Paket hat eine mit der Fälligkeitsdatum berechnete Ablaufzeit, nach der sortiert und eingelagert wird.",
			"lineHeight": 1.25,
			"baseline": 43
		},
		{
			"type": "text",
			"version": 649,
			"versionNonce": 1823720134,
			"isDeleted": false,
			"id": "KQ3XXUQG",
			"fillStyle": "cross-hatch",
			"strokeWidth": 4,
			"strokeStyle": "dashed",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 1584.7067210148734,
			"y": 158.29473287735766,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1107.0791015625,
			"height": 75,
			"seed": 1871454590,
			"groupIds": [],
			"frameId": "USCQ4VQrG23dpX1fI6OzG",
			"roundness": null,
			"boundElements": [],
			"updated": 1712826540977,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "Das Hauptprogramm bestimmt das Regal in dem das Paket eingelagert werden soll um einen möglichst effizienten\nAblauf des Prozesses zu ermöglichen. Damit das Paket richtig eingelagert wird,\nwird mithilfe von an den Regalen installierten LEDs das richtige Regal gekennzeichnet.",
			"rawText": "Das Hauptprogramm bestimmt das Regal in dem das Paket eingelagert werden soll um einen möglichst effizienten\nAblauf des Prozesses zu ermöglichen. Damit das Paket richtig eingelagert wird,\nwird mithilfe von an den Regalen installierten LEDs das richtige Regal gekennzeichnet.",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "Das Hauptprogramm bestimmt das Regal in dem das Paket eingelagert werden soll um einen möglichst effizienten\nAblauf des Prozesses zu ermöglichen. Damit das Paket richtig eingelagert wird,\nwird mithilfe von an den Regalen installierten LEDs das richtige Regal gekennzeichnet.",
			"lineHeight": 1.25,
			"baseline": 68
		},
		{
			"type": "text",
			"version": 273,
			"versionNonce": 837700878,
			"isDeleted": false,
			"id": "sgV9RFgA",
			"fillStyle": "cross-hatch",
			"strokeWidth": 4,
			"strokeStyle": "dashed",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 1679.2364967074016,
			"y": 301.7267931234377,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"width": 905.291180419922,
			"height": 45,
			"seed": 650592702,
			"groupIds": [],
			"frameId": "USCQ4VQrG23dpX1fI6OzG",
			"roundness": null,
			"boundElements": [],
			"updated": 1713620703165,
			"link": null,
			"locked": false,
			"fontSize": 36,
			"fontFamily": 1,
			"text": "Erstellen eines Objektes für den Timer des Pakets",
			"rawText": "Erstellen eines Objektes für den Timer des Pakets",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "Erstellen eines Objektes für den Timer des Pakets",
			"lineHeight": 1.25,
			"baseline": 32
		},
		{
			"type": "text",
			"version": 175,
			"versionNonce": 344314839,
			"isDeleted": false,
			"id": "LMazcfF7",
			"fillStyle": "cross-hatch",
			"strokeWidth": 4,
			"strokeStyle": "dashed",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 1939.9748387339455,
			"y": 455.53831725827,
			"strokeColor": "#a24db3",
			"backgroundColor": "transparent",
			"width": 359.60386439732144,
			"height": 45,
			"seed": 1110727166,
			"groupIds": [],
			"frameId": "USCQ4VQrG23dpX1fI6OzG",
			"roundness": null,
			"boundElements": [],
			"updated": 1713771411475,
			"link": null,
			"locked": false,
			"fontSize": 36,
			"fontFamily": 1,
			"text": "Auswurf des Pakets",
			"rawText": "Auswurf des Pakets",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "Auswurf des Pakets",
			"lineHeight": 1.25,
			"baseline": 31
		},
		{
			"type": "text",
			"version": 534,
			"versionNonce": 1528140122,
			"isDeleted": false,
			"id": "YVmCP9bq",
			"fillStyle": "cross-hatch",
			"strokeWidth": 4,
			"strokeStyle": "dashed",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 1603.0061256784556,
			"y": 529.2689712921064,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 952.09912109375,
			"height": 75,
			"seed": 1490315838,
			"groupIds": [],
			"frameId": "USCQ4VQrG23dpX1fI6OzG",
			"roundness": null,
			"boundElements": [],
			"updated": 1712826540977,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "Mit dem Auswurfbefehl kann die gewollte Anzahl an Pakete ausgeworfen werden. Die Reihenfolge,\nin der die Pakete ausgeworfen werden, beginnt mit dem Paket, das die kürzeste Ablaufzeit hat \nund steigt dann auf.",
			"rawText": "Mit dem Auswurfbefehl kann die gewollte Anzahl an Pakete ausgeworfen werden. Die Reihenfolge,\nin der die Pakete ausgeworfen werden, beginnt mit dem Paket, das die kürzeste Ablaufzeit hat \nund steigt dann auf.",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "Mit dem Auswurfbefehl kann die gewollte Anzahl an Pakete ausgeworfen werden. Die Reihenfolge,\nin der die Pakete ausgeworfen werden, beginnt mit dem Paket, das die kürzeste Ablaufzeit hat \nund steigt dann auf.",
			"lineHeight": 1.25,
			"baseline": 68
		},
		{
			"type": "frame",
			"version": 160,
			"versionNonce": 936003910,
			"isDeleted": false,
			"id": "USCQ4VQrG23dpX1fI6OzG",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 1452.7875782827819,
			"y": -964.1859369839381,
			"strokeColor": "#bbb",
			"backgroundColor": "transparent",
			"width": 1432.0045824559825,
			"height": 1763.2162435662822,
			"seed": 1332329570,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1712826540977,
			"link": null,
			"locked": false,
			"customData": {
				"frameColor": {
					"stroke": "#2B2B2B",
					"fill": "#525252",
					"nameColor": "#858585"
				}
			},
			"name": null
		},
		{
			"type": "line",
			"version": 65,
			"versionNonce": 936269338,
			"isDeleted": false,
			"id": "skH_gFwfWRgF4btcUoaC0",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 571.4750185593281,
			"y": 1314.2947252855715,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"width": 25.44283274118891,
			"height": 13.047588666855518,
			"seed": 593703806,
			"groupIds": [],
			"frameId": "jerA-kzSGpDyDfhi2SeEA",
			"roundness": null,
			"boundElements": [],
			"updated": 1712826540977,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					-25.44283274118891,
					13.047588666855518
				]
			]
		},
		{
			"type": "line",
			"version": 65,
			"versionNonce": 863842438,
			"isDeleted": false,
			"id": "x6dx8xJDDqVthMUBmodeN",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 549.294082984853,
			"y": 1328.6470529100723,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"width": 22.833305053297636,
			"height": 13.047588666855518,
			"seed": 1656198270,
			"groupIds": [],
			"frameId": "jerA-kzSGpDyDfhi2SeEA",
			"roundness": null,
			"boundElements": [],
			"updated": 1712826540977,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					22.833305053297636,
					13.047588666855518
				]
			]
		},
		{
			"type": "ellipse",
			"version": 66,
			"versionNonce": 848331482,
			"isDeleted": false,
			"id": "dDcE7s85iSI9gpkHsdxIz",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 168.53468087829947,
			"y": 1104.9106873177025,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 47.81836122997731,
			"height": 47.8183612299772,
			"seed": 1388817698,
			"groupIds": [],
			"frameId": "jerA-kzSGpDyDfhi2SeEA",
			"roundness": null,
			"boundElements": [],
			"updated": 1712826540977,
			"link": null,
			"locked": false
		},
		{
			"type": "line",
			"version": 161,
			"versionNonce": 1590767558,
			"isDeleted": false,
			"id": "2-gbnyavRg5R9Z-tTpB67",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 201.511143762061,
			"y": 1138.102470897195,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 19.32928522410583,
			"height": 18.38547132258668,
			"seed": 1496405310,
			"groupIds": [],
			"frameId": "jerA-kzSGpDyDfhi2SeEA",
			"roundness": null,
			"boundElements": [],
			"updated": 1712826540977,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					-19.32928522410583,
					-18.38547132258668
				]
			]
		},
		{
			"type": "line",
			"version": 189,
			"versionNonce": 367990682,
			"isDeleted": false,
			"id": "71Fe4EF9iVcQpLwjhU2gZ",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 200.80837733018757,
			"y": 1117.4285819958598,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 16.737056959424706,
			"height": 22.288325834486386,
			"seed": 1036799074,
			"groupIds": [],
			"frameId": "jerA-kzSGpDyDfhi2SeEA",
			"roundness": null,
			"boundElements": [],
			"updated": 1712826540978,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					-16.737056959424706,
					22.288325834486386
				]
			]
		},
		{
			"type": "image",
			"version": 146,
			"versionNonce": 1440958214,
			"isDeleted": false,
			"id": "eo8jwBGc",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 326.78515153074943,
			"y": 1418.2346733175727,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 276.80583413135014,
			"height": 30.514028959361433,
			"seed": 95853,
			"groupIds": [],
			"frameId": "jerA-kzSGpDyDfhi2SeEA",
			"roundness": null,
			"boundElements": [],
			"updated": 1712826540978,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "2d6726517657bd9d21cbf16bbf7b445af4101c78",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "frame",
			"version": 73,
			"versionNonce": 1646072922,
			"isDeleted": false,
			"id": "jerA-kzSGpDyDfhi2SeEA",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 19.294559477448047,
			"y": 1000.7941988359814,
			"strokeColor": "#bbb",
			"backgroundColor": "transparent",
			"width": 756.3567284492137,
			"height": 558.7691850424355,
			"seed": 1646986558,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1712826540978,
			"link": null,
			"locked": false,
			"customData": {
				"frameColor": {
					"stroke": "#2B2B2B",
					"fill": "#525252",
					"nameColor": "#858585"
				}
			},
			"name": null
		},
		{
			"type": "rectangle",
			"version": 184,
			"versionNonce": 1691069050,
			"isDeleted": false,
			"id": "dHFhR7zYg-MMRKDx2kJo0",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 2281.75966272054,
			"y": 1101.8595042840511,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 104.866917527108,
			"height": 244.06467935563637,
			"seed": 1767874850,
			"groupIds": [],
			"frameId": "ZONEsn6KtZZVIJt09sJpm",
			"roundness": {
				"type": 3
			},
			"boundElements": [
				{
					"id": "5KQlGLFyGmA-xLN1XmkgM",
					"type": "arrow"
				},
				{
					"id": "fenbQ3vrFE8y-krcn60yw",
					"type": "arrow"
				}
			],
			"updated": 1713637163610,
			"link": null,
			"locked": false
		},
		{
			"type": "ellipse",
			"version": 183,
			"versionNonce": 166567290,
			"isDeleted": false,
			"id": "QwEShOPT3SxeavhfXPG2c",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 2311.7130589109975,
			"y": 1163.2911637109364,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 47.629353090057066,
			"height": 45.724208037104745,
			"seed": 2014299646,
			"groupIds": [],
			"frameId": "ZONEsn6KtZZVIJt09sJpm",
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1713637163610,
			"link": null,
			"locked": false
		},
		{
			"type": "ellipse",
			"version": 243,
			"versionNonce": 1141890618,
			"isDeleted": false,
			"id": "-AQiZJ4AMDxGWdNsPiie-",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 2318.619264235419,
			"y": 1248.547785686426,
			"strokeColor": "#e03131",
			"backgroundColor": "#fa5252",
			"width": 34.293156027828445,
			"height": 34.29319236614106,
			"seed": 866552702,
			"groupIds": [],
			"frameId": "ZONEsn6KtZZVIJt09sJpm",
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1713637163610,
			"link": null,
			"locked": false
		},
		{
			"type": "arrow",
			"version": 257,
			"versionNonce": 916169318,
			"isDeleted": false,
			"id": "5KQlGLFyGmA-xLN1XmkgM",
			"fillStyle": "cross-hatch",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 2281.5419744203587,
			"y": 1242.5286030424297,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "#ff8787",
			"width": 316.1119976717582,
			"height": 0.1426128323780631,
			"seed": 493964286,
			"groupIds": [],
			"frameId": "ZONEsn6KtZZVIJt09sJpm",
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1713637207144,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "dHFhR7zYg-MMRKDx2kJo0",
				"focus": -0.15288484998944152,
				"gap": 1
			},
			"endBinding": {
				"elementId": "Jaxy_XdNuoq_BaGgGTHJS",
				"focus": 0.1306743325797587,
				"gap": 4.125000000000114
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "triangle",
			"points": [
				[
					0,
					0
				],
				[
					-316.1119976717582,
					-0.1426128323780631
				]
			]
		},
		{
			"type": "rectangle",
			"version": 93,
			"versionNonce": 1909028602,
			"isDeleted": false,
			"id": "Jaxy_XdNuoq_BaGgGTHJS",
			"fillStyle": "cross-hatch",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 1748.406916612254,
			"y": 1098.9720741141643,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 212.8980601363462,
			"height": 253.57921614728775,
			"seed": 97819426,
			"groupIds": [],
			"frameId": "ZONEsn6KtZZVIJt09sJpm",
			"roundness": {
				"type": 3
			},
			"boundElements": [
				{
					"id": "TdyUi4FHD_E6f1jMSI-dj",
					"type": "arrow"
				},
				{
					"id": "5KQlGLFyGmA-xLN1XmkgM",
					"type": "arrow"
				}
			],
			"updated": 1713637168307,
			"link": null,
			"locked": false
		},
		{
			"type": "rectangle",
			"version": 1193,
			"versionNonce": 1247664826,
			"isDeleted": false,
			"id": "vecjlH6f2WyY9Tyfo2P_E",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 1826.360096345688,
			"y": 1146.2202844378198,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 59.04901772977437,
			"height": 61.29511560443,
			"seed": 518540514,
			"groupIds": [
				"cB4Kz_nzM--f4PmIOumHe"
			],
			"frameId": "ZONEsn6KtZZVIJt09sJpm",
			"roundness": null,
			"boundElements": [],
			"updated": 1713637168307,
			"link": null,
			"locked": false
		},
		{
			"type": "rectangle",
			"version": 1125,
			"versionNonce": 503739258,
			"isDeleted": false,
			"id": "uB2ix8dlNI_Ulnz8SdOIW",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 1839.5526772549551,
			"y": 1162.273449782305,
			"strokeColor": "#000000",
			"backgroundColor": "black",
			"width": 29.78586167252632,
			"height": 31.873793322238196,
			"seed": 1339056290,
			"groupIds": [
				"cB4Kz_nzM--f4PmIOumHe"
			],
			"frameId": "ZONEsn6KtZZVIJt09sJpm",
			"roundness": null,
			"boundElements": [],
			"updated": 1713637168307,
			"link": null,
			"locked": false
		},
		{
			"type": "line",
			"version": 941,
			"versionNonce": 1251865658,
			"isDeleted": false,
			"id": "GHVMeI85sxsi2k3pexdsf",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 1840.646050926971,
			"y": 1130.7440630809192,
			"strokeColor": "#000000",
			"backgroundColor": "black",
			"width": 0.7515244268512646,
			"height": 16.193175852278152,
			"seed": 436206690,
			"groupIds": [
				"cB4Kz_nzM--f4PmIOumHe"
			],
			"frameId": "ZONEsn6KtZZVIJt09sJpm",
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1713637168307,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					-0.7515244268512646,
					16.193175852278152
				]
			]
		},
		{
			"type": "line",
			"version": 982,
			"versionNonce": 570907898,
			"isDeleted": false,
			"id": "P4DcNooXTA6teAOX70tR3",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 1874.809157645624,
			"y": 1130.4188030945165,
			"strokeColor": "#000000",
			"backgroundColor": "black",
			"width": 0.7515244268512646,
			"height": 16.193175852278152,
			"seed": 2068193314,
			"groupIds": [
				"cB4Kz_nzM--f4PmIOumHe"
			],
			"frameId": "ZONEsn6KtZZVIJt09sJpm",
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1713637168307,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					-0.7515244268512646,
					16.193175852278152
				]
			]
		},
		{
			"type": "line",
			"version": 971,
			"versionNonce": 1103474106,
			"isDeleted": false,
			"id": "DjsSH5tTtdXj52tU3rF2G",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 1858.8767353137334,
			"y": 1131.1030185260295,
			"strokeColor": "#000000",
			"backgroundColor": "black",
			"width": 0.7515244268512646,
			"height": 16.193175852278152,
			"seed": 1603390434,
			"groupIds": [
				"cB4Kz_nzM--f4PmIOumHe"
			],
			"frameId": "ZONEsn6KtZZVIJt09sJpm",
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1713637168307,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					-0.7515244268512646,
					16.193175852278152
				]
			]
		},
		{
			"type": "line",
			"version": 1026,
			"versionNonce": 519825018,
			"isDeleted": false,
			"id": "-UPvgu2u45-v-aYmgfF5U",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 1842.3423767590953,
			"y": 1209.248035392549,
			"strokeColor": "#000000",
			"backgroundColor": "black",
			"width": 0.7515244268512646,
			"height": 16.193175852278152,
			"seed": 1559363490,
			"groupIds": [
				"cB4Kz_nzM--f4PmIOumHe"
			],
			"frameId": "ZONEsn6KtZZVIJt09sJpm",
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1713637168307,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					-0.7515244268512646,
					16.193175852278152
				]
			]
		},
		{
			"type": "line",
			"version": 998,
			"versionNonce": 309135162,
			"isDeleted": false,
			"id": "qDbgks3bpXlGtSht21Fhd",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 1855.3133290868445,
			"y": 1209.6843275356323,
			"strokeColor": "#000000",
			"backgroundColor": "black",
			"width": 0.7515244268512646,
			"height": 16.193175852278152,
			"seed": 1872083810,
			"groupIds": [
				"cB4Kz_nzM--f4PmIOumHe"
			],
			"frameId": "ZONEsn6KtZZVIJt09sJpm",
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1713637168307,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					-0.7515244268512646,
					16.193175852278152
				]
			]
		},
		{
			"type": "line",
			"version": 973,
			"versionNonce": 1685852154,
			"isDeleted": false,
			"id": "NpWRg7IStOF7fGcgKnvnE",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 1871.0588576240693,
			"y": 1208.8189013095905,
			"strokeColor": "#000000",
			"backgroundColor": "black",
			"width": 0.7515244268512646,
			"height": 16.193175852278152,
			"seed": 902561570,
			"groupIds": [
				"cB4Kz_nzM--f4PmIOumHe"
			],
			"frameId": "ZONEsn6KtZZVIJt09sJpm",
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1713637168307,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					-0.7515244268512646,
					16.193175852278152
				]
			]
		},
		{
			"type": "line",
			"version": 1080,
			"versionNonce": 1496055994,
			"isDeleted": false,
			"id": "0RsFwhom2j0TWnaw5GFh8",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 1.5619589856492286,
			"x": 1894.5809421467382,
			"y": 1155.469007369745,
			"strokeColor": "#000000",
			"backgroundColor": "black",
			"width": 0.7515244268512646,
			"height": 16.193175852278152,
			"seed": 738446050,
			"groupIds": [
				"cB4Kz_nzM--f4PmIOumHe"
			],
			"frameId": "ZONEsn6KtZZVIJt09sJpm",
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1713637168307,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					-0.7515244268512646,
					16.193175852278152
				]
			]
		},
		{
			"type": "line",
			"version": 1127,
			"versionNonce": 1008720250,
			"isDeleted": false,
			"id": "HJBiCUYtj8teL_gDVerIJ",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 1.5619589856492286,
			"x": 1894.9973958976127,
			"y": 1170.6334148776577,
			"strokeColor": "#000000",
			"backgroundColor": "black",
			"width": 0.7515244268512646,
			"height": 16.193175852278152,
			"seed": 1758207650,
			"groupIds": [
				"cB4Kz_nzM--f4PmIOumHe"
			],
			"frameId": "ZONEsn6KtZZVIJt09sJpm",
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1713637168307,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					-0.7515244268512646,
					16.193175852278152
				]
			]
		},
		{
			"type": "line",
			"version": 1132,
			"versionNonce": 1822071354,
			"isDeleted": false,
			"id": "gFQ_kFWHaY-Rr7xft6ogz",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 1.5619589856492286,
			"x": 1895.8266891400995,
			"y": 1185.2929685751346,
			"strokeColor": "#000000",
			"backgroundColor": "black",
			"width": 0.7515244268512646,
			"height": 16.193175852278152,
			"seed": 1490287202,
			"groupIds": [
				"cB4Kz_nzM--f4PmIOumHe"
			],
			"frameId": "ZONEsn6KtZZVIJt09sJpm",
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1713637168307,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					-0.7515244268512646,
					16.193175852278152
				]
			]
		},
		{
			"type": "line",
			"version": 1123,
			"versionNonce": 1769947898,
			"isDeleted": false,
			"id": "N33JeyTIQ7jQEYXst_UcP",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 1.5619589856492286,
			"x": 1817.076845204237,
			"y": 1153.0200920122581,
			"strokeColor": "#000000",
			"backgroundColor": "black",
			"width": 0.7515244268512646,
			"height": 16.193175852278152,
			"seed": 2062179874,
			"groupIds": [
				"cB4Kz_nzM--f4PmIOumHe"
			],
			"frameId": "ZONEsn6KtZZVIJt09sJpm",
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1713637168307,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					-0.7515244268512646,
					16.193175852278152
				]
			]
		},
		{
			"type": "line",
			"version": 1148,
			"versionNonce": 1565578170,
			"isDeleted": false,
			"id": "k9Zj4qegYEQMPGOOVwPYc",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 1.5619589856492286,
			"x": 1818.260753745706,
			"y": 1166.6773346010243,
			"strokeColor": "#000000",
			"backgroundColor": "black",
			"width": 0.7515244268512646,
			"height": 16.193175852278152,
			"seed": 469649890,
			"groupIds": [
				"cB4Kz_nzM--f4PmIOumHe"
			],
			"frameId": "ZONEsn6KtZZVIJt09sJpm",
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1713637168307,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					-0.7515244268512646,
					16.193175852278152
				]
			]
		},
		{
			"type": "line",
			"version": 1125,
			"versionNonce": 707939450,
			"isDeleted": false,
			"id": "XbrPnwLywG2DX3deK-2x4",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 1.5619589856492286,
			"x": 1817.2078679432802,
			"y": 1183.4067605773666,
			"strokeColor": "#000000",
			"backgroundColor": "black",
			"width": 0.7515244268512646,
			"height": 16.193175852278152,
			"seed": 320781730,
			"groupIds": [
				"cB4Kz_nzM--f4PmIOumHe"
			],
			"frameId": "ZONEsn6KtZZVIJt09sJpm",
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1713637168307,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					-0.7515244268512646,
					16.193175852278152
				]
			]
		},
		{
			"type": "text",
			"version": 144,
			"versionNonce": 1978051898,
			"isDeleted": false,
			"id": "jPodHZg9",
			"fillStyle": "cross-hatch",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 1817.564861139349,
			"y": 1247.1649068708011,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 73.828125,
			"height": 75.6,
			"seed": 641301310,
			"groupIds": [],
			"frameId": "ZONEsn6KtZZVIJt09sJpm",
			"roundness": null,
			"boundElements": [],
			"updated": 1713637168307,
			"link": null,
			"locked": false,
			"fontSize": 63,
			"fontFamily": 3,
			"text": "µC",
			"rawText": "µC",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "µC",
			"lineHeight": 1.2,
			"baseline": 60
		},
		{
			"type": "text",
			"version": 474,
			"versionNonce": 1311286906,
			"isDeleted": false,
			"id": "cDRTlMVe",
			"fillStyle": "cross-hatch",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 1972.04146371304,
			"y": 1144.5648960575595,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 313.875,
			"height": 80.36129032258066,
			"seed": 564127550,
			"groupIds": [],
			"frameId": "ZONEsn6KtZZVIJt09sJpm",
			"roundness": null,
			"boundElements": [],
			"updated": 1713637209404,
			"link": null,
			"locked": false,
			"fontSize": 22.322580645161292,
			"fontFamily": 3,
			"text": "Verarbeitung und\nSerialisierung\ngelesener Informationen ",
			"rawText": "Verarbeitung und\nSerialisierung\ngelesener Informationen ",
			"textAlign": "center",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "Verarbeitung und\nSerialisierung\ngelesener Informationen ",
			"lineHeight": 1.2,
			"baseline": 75
		},
		{
			"type": "arrow",
			"version": 907,
			"versionNonce": 1707368121,
			"isDeleted": false,
			"id": "TdyUi4FHD_E6f1jMSI-dj",
			"fillStyle": "cross-hatch",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 1744.041301510681,
			"y": 1220.0161066078176,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 180.99322656122808,
			"height": 2.047298957746989,
			"seed": 1136637090,
			"groupIds": [],
			"frameId": "ZONEsn6KtZZVIJt09sJpm",
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1713771496251,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "Jaxy_XdNuoq_BaGgGTHJS",
				"gap": 4.365615101573098,
				"focus": 0.05468270794133961
			},
			"endBinding": {
				"elementId": "GEcIiSLhlg3GKMchi7uWJ",
				"gap": 2.6672108419403457,
				"focus": 0.09580988201968854
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "triangle",
			"points": [
				[
					0,
					0
				],
				[
					-180.99322656122808,
					2.047298957746989
				]
			]
		},
		{
			"type": "rectangle",
			"version": 312,
			"versionNonce": 1526107046,
			"isDeleted": false,
			"id": "GEcIiSLhlg3GKMchi7uWJ",
			"fillStyle": "cross-hatch",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 1254.4123306598744,
			"y": 1150.9205288028054,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 305.9685334476382,
			"height": 132.75610632469525,
			"seed": 609923326,
			"groupIds": [],
			"frameId": "ZONEsn6KtZZVIJt09sJpm",
			"roundness": {
				"type": 3
			},
			"boundElements": [
				{
					"type": "text",
					"id": "uU2DDshE"
				},
				{
					"id": "TdyUi4FHD_E6f1jMSI-dj",
					"type": "arrow"
				}
			],
			"updated": 1713637105196,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 240,
			"versionNonce": 203544793,
			"isDeleted": false,
			"id": "uU2DDshE",
			"fillStyle": "cross-hatch",
			"strokeWidth": 4,
			"strokeStyle": "dashed",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 1320.8216190850824,
			"y": 1186.048581965153,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 173.14995659722223,
			"height": 62.5,
			"seed": 1535855294,
			"groupIds": [],
			"frameId": "ZONEsn6KtZZVIJt09sJpm",
			"roundness": null,
			"boundElements": [],
			"updated": 1713771411463,
			"link": null,
			"locked": false,
			"fontSize": 50,
			"fontFamily": 3,
			"text": "Arduino",
			"rawText": "Arduino",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "GEcIiSLhlg3GKMchi7uWJ",
			"originalText": "Arduino",
			"lineHeight": 1.2,
			"baseline": 44
		},
		{
			"type": "rectangle",
			"version": 130,
			"versionNonce": 1210336314,
			"isDeleted": false,
			"id": "qenJPhUWuzyprUdP0QHB8",
			"fillStyle": "cross-hatch",
			"strokeWidth": 4,
			"strokeStyle": "dashed",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 1712.9140396683363,
			"y": 926.6402919370996,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 886.6941107592528,
			"height": 563.5605332709506,
			"seed": 1324490814,
			"groupIds": [],
			"frameId": "ZONEsn6KtZZVIJt09sJpm",
			"roundness": {
				"type": 3
			},
			"boundElements": [],
			"updated": 1713637120543,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 120,
			"versionNonce": 1878990758,
			"isDeleted": false,
			"id": "Ppfp6eb6",
			"fillStyle": "cross-hatch",
			"strokeWidth": 4,
			"strokeStyle": "dashed",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 1836.8525140668153,
			"y": 965.1931145677374,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 615.234375,
			"height": 60,
			"seed": 474774270,
			"groupIds": [],
			"frameId": "ZONEsn6KtZZVIJt09sJpm",
			"roundness": null,
			"boundElements": [],
			"updated": 1713637121918,
			"link": null,
			"locked": false,
			"fontSize": 50,
			"fontFamily": 3,
			"text": "QR-Code Scanner Modul",
			"rawText": "QR-Code Scanner Modul",
			"textAlign": "center",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "QR-Code Scanner Modul",
			"lineHeight": 1.2,
			"baseline": 48
		},
		{
			"type": "line",
			"version": 72,
			"versionNonce": 234857370,
			"isDeleted": false,
			"id": "Km0LELvaKOZAWcahSE17p",
			"fillStyle": "cross-hatch",
			"strokeWidth": 4,
			"strokeStyle": "dashed",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 1640.3511268977493,
			"y": 928.423752036238,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"width": 1.7833920670918815,
			"height": 551.0765166731212,
			"seed": 1070824318,
			"groupIds": [],
			"frameId": "ZONEsn6KtZZVIJt09sJpm",
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1712826540978,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					-1.7833920670918815,
					551.0765166731212
				]
			]
		},
		{
			"type": "text",
			"version": 82,
			"versionNonce": 233929478,
			"isDeleted": false,
			"id": "e32RdFWR",
			"fillStyle": "cross-hatch",
			"strokeWidth": 4,
			"strokeStyle": "dashed",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 1476.1416052279799,
			"y": 1490.9002687093594,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"width": 236.1328125,
			"height": 74.39999999999999,
			"seed": 51544802,
			"groupIds": [],
			"frameId": "ZONEsn6KtZZVIJt09sJpm",
			"roundness": null,
			"boundElements": [],
			"updated": 1712826540978,
			"link": null,
			"locked": false,
			"fontSize": 31,
			"fontFamily": 3,
			"text": "Schnittstelle\nseriell",
			"rawText": "Schnittstelle\nseriell",
			"textAlign": "center",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "Schnittstelle\nseriell",
			"lineHeight": 1.2,
			"baseline": 66
		},
		{
			"type": "text",
			"version": 210,
			"versionNonce": 699139834,
			"isDeleted": false,
			"id": "Wk7X7cFH",
			"fillStyle": "cross-hatch",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 2463.1950597622717,
			"y": 1068.625118252448,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 126.5625,
			"height": 43.199999999999996,
			"seed": 129448294,
			"groupIds": [],
			"frameId": "ZONEsn6KtZZVIJt09sJpm",
			"roundness": null,
			"boundElements": [
				{
					"id": "fenbQ3vrFE8y-krcn60yw",
					"type": "arrow"
				}
			],
			"updated": 1713637163610,
			"link": null,
			"locked": false,
			"fontSize": 36,
			"fontFamily": 3,
			"text": "Kamera",
			"rawText": "Kamera",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "Kamera",
			"lineHeight": 1.2,
			"baseline": 34
		},
		{
			"type": "arrow",
			"version": 220,
			"versionNonce": 716208806,
			"isDeleted": false,
			"id": "fenbQ3vrFE8y-krcn60yw",
			"fillStyle": "cross-hatch",
			"strokeWidth": 4,
			"strokeStyle": "dashed",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 2456.9450597622717,
			"y": 1108.2084770170964,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 53.125,
			"height": 21.209226526699013,
			"seed": 1267654246,
			"groupIds": [],
			"frameId": "ZONEsn6KtZZVIJt09sJpm",
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1713637163844,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "Wk7X7cFH",
				"focus": 0.2085991426835542,
				"gap": 6.25
			},
			"endBinding": {
				"elementId": "dHFhR7zYg-MMRKDx2kJo0",
				"focus": -0.46638393834961744,
				"gap": 17.19347951462396
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "triangle",
			"points": [
				[
					0,
					0
				],
				[
					-53.125,
					21.209226526699013
				]
			]
		},
		{
			"type": "frame",
			"version": 51,
			"versionNonce": 540811354,
			"isDeleted": false,
			"id": "ZONEsn6KtZZVIJt09sJpm",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 1128.8076456132483,
			"y": 889.5420425853365,
			"strokeColor": "#bbb",
			"backgroundColor": "transparent",
			"width": 1573.6104151903157,
			"height": 894.3846833193797,
			"seed": 1375980798,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1712826540978,
			"link": null,
			"locked": false,
			"customData": {
				"frameColor": {
					"stroke": "#2B2B2B",
					"fill": "#525252",
					"nameColor": "#858585"
				}
			},
			"name": null
		},
		{
			"type": "rectangle",
			"version": 643,
			"versionNonce": 993750105,
			"isDeleted": false,
			"id": "BJNgOemEXP4xtbPiKUlhG",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 3707.572894117001,
			"y": -811.6352524291942,
			"strokeColor": "#000000",
			"backgroundColor": "#fab005",
			"width": 393.57199823302795,
			"height": 171.99999999999997,
			"seed": 675824062,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 3
			},
			"boundElements": [
				{
					"type": "text",
					"id": "sorTEFRQ"
				},
				{
					"id": "UN9xXsb0z4alyQPCABYDj",
					"type": "arrow"
				},
				{
					"id": "3GDEnfnV_GX5rfI7R9ILJ",
					"type": "arrow"
				}
			],
			"updated": 1713771491394,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 711,
			"versionNonce": 1985296889,
			"isDeleted": false,
			"id": "sorTEFRQ",
			"fillStyle": "cross-hatch",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 3732.972174483515,
			"y": -779.6352524291942,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 342.7734375,
			"height": 108,
			"seed": 1630984354,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1713771481269,
			"link": null,
			"locked": false,
			"fontSize": 45,
			"fontFamily": 3,
			"text": "Hauptprogramm\nmain.cpp",
			"rawText": "Hauptprogramm\nmain.cpp",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "BJNgOemEXP4xtbPiKUlhG",
			"originalText": "Hauptprogramm\nmain.cpp",
			"lineHeight": 1.2,
			"baseline": 97
		},
		{
			"type": "rectangle",
			"version": 550,
			"versionNonce": 378361017,
			"isDeleted": false,
			"id": "72FOu8bc3FAm7i_QDmLz-",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 4489.565197662357,
			"y": -775.2748887840647,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "#a5d8ff",
			"width": 250.8685837190788,
			"height": 98.53389969054295,
			"seed": 924061090,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 3
			},
			"boundElements": [
				{
					"type": "text",
					"id": "f8iKvtjv"
				},
				{
					"id": "UN9xXsb0z4alyQPCABYDj",
					"type": "arrow"
				},
				{
					"id": "ciMmSPNNYrasMRDrbW0_Y",
					"type": "arrow"
				},
				{
					"id": "X1Z3xtNrJiR6wCvnP5vDK",
					"type": "arrow"
				}
			],
			"updated": 1713771502122,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 568,
			"versionNonce": 1599362457,
			"isDeleted": false,
			"id": "f8iKvtjv",
			"fillStyle": "cross-hatch",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 4496.347145771896,
			"y": -753.0079389387932,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 237.3046875,
			"height": 54,
			"seed": 321715070,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1713771502122,
			"link": null,
			"locked": false,
			"fontSize": 45,
			"fontFamily": 3,
			"text": "stepper.h",
			"rawText": "stepper.h",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "72FOu8bc3FAm7i_QDmLz-",
			"originalText": "stepper.h",
			"lineHeight": 1.2,
			"baseline": 43
		},
		{
			"type": "rectangle",
			"version": 604,
			"versionNonce": 1234089465,
			"isDeleted": false,
			"id": "E148KwF7X1VybXMuoEvHC",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 4499.528014230818,
			"y": -527.1249795900883,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "#a5d8ff",
			"width": 305.37372399138206,
			"height": 118,
			"seed": 1349544958,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 3
			},
			"boundElements": [
				{
					"type": "text",
					"id": "lnKIQrGQ"
				},
				{
					"id": "ciMmSPNNYrasMRDrbW0_Y",
					"type": "arrow"
				},
				{
					"id": "X1Z3xtNrJiR6wCvnP5vDK",
					"type": "arrow"
				}
			],
			"updated": 1713771502122,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 636,
			"versionNonce": 102207193,
			"isDeleted": false,
			"id": "lnKIQrGQ",
			"fillStyle": "cross-hatch",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 4507.19534497651,
			"y": -495.1249795900883,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 290.0390625,
			"height": 54,
			"seed": 700333118,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1713771502122,
			"link": null,
			"locked": false,
			"fontSize": 45,
			"fontFamily": 3,
			"text": "stepper.cpp",
			"rawText": "stepper.cpp",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "E148KwF7X1VybXMuoEvHC",
			"originalText": "stepper.cpp",
			"lineHeight": 1.2,
			"baseline": 43
		},
		{
			"type": "arrow",
			"version": 1642,
			"versionNonce": 19694425,
			"isDeleted": false,
			"id": "UN9xXsb0z4alyQPCABYDj",
			"fillStyle": "cross-hatch",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 4479.060807759263,
			"y": -715.5120736600361,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 370.0357731833192,
			"height": 1.714664079082013,
			"seed": 1279339162,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1713771502122,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "72FOu8bc3FAm7i_QDmLz-",
				"gap": 10.504389903093397,
				"focus": -0.19757747983810153
			},
			"endBinding": {
				"elementId": "BJNgOemEXP4xtbPiKUlhG",
				"gap": 7.880142225914824,
				"focus": 0.14711709241463594
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "triangle",
			"points": [
				[
					0,
					0
				],
				[
					-370.0357731833192,
					1.714664079082013
				]
			]
		},
		{
			"type": "arrow",
			"version": 1419,
			"versionNonce": 280306007,
			"isDeleted": false,
			"id": "ciMmSPNNYrasMRDrbW0_Y",
			"fillStyle": "cross-hatch",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 4620.677451504822,
			"y": -534.993606899436,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0.29954447377167526,
			"height": 129.9719231122798,
			"seed": 1663951898,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1713771502323,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "E148KwF7X1VybXMuoEvHC",
				"focus": -0.20535748351112476,
				"gap": 7.868627309347744
			},
			"endBinding": {
				"elementId": "72FOu8bc3FAm7i_QDmLz-",
				"focus": -0.0417190296553662,
				"gap": 11.775459081805934
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "triangle",
			"points": [
				[
					0,
					0
				],
				[
					-0.29954447377167526,
					-129.9719231122798
				]
			]
		},
		{
			"type": "text",
			"version": 364,
			"versionNonce": 492886617,
			"isDeleted": false,
			"id": "Kfrg63UU",
			"fillStyle": "cross-hatch",
			"strokeWidth": 4,
			"strokeStyle": "dashed",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 4394.356047449533,
			"y": -883.4528026965774,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 500.9765625,
			"height": 54,
			"seed": 2071934150,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1713771502122,
			"link": null,
			"locked": false,
			"fontSize": 45,
			"fontFamily": 3,
			"text": "Schrittmotor Klasse",
			"rawText": "Schrittmotor Klasse",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "Schrittmotor Klasse",
			"lineHeight": 1.2,
			"baseline": 43
		},
		{
			"type": "arrow",
			"version": 928,
			"versionNonce": 2134898583,
			"isDeleted": false,
			"id": "X1Z3xtNrJiR6wCvnP5vDK",
			"fillStyle": "cross-hatch",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 4644.425312157781,
			"y": -661.0108721479595,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 0,
			"height": 112.14020302381107,
			"seed": 1467559514,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1713771502323,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "72FOu8bc3FAm7i_QDmLz-",
				"focus": -0.2345915315473385,
				"gap": 15.730116945562258
			},
			"endBinding": {
				"elementId": "E148KwF7X1VybXMuoEvHC",
				"focus": -0.051016596758326364,
				"gap": 21.745689534060148
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "triangle",
			"points": [
				[
					0,
					0
				],
				[
					0,
					112.14020302381107
				]
			]
		},
		{
			"type": "text",
			"version": 300,
			"versionNonce": 1408161817,
			"isDeleted": false,
			"id": "SeGSs16V",
			"fillStyle": "cross-hatch",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 4398.084742937983,
			"y": -624.2436062636924,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 210.111328125,
			"height": 41.4,
			"seed": 2090163802,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1713771502122,
			"link": null,
			"locked": false,
			"fontSize": 36,
			"fontFamily": 2,
			"text": "Initialisierung",
			"rawText": "Initialisierung",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "Initialisierung",
			"lineHeight": 1.15,
			"baseline": 33
		},
		{
			"type": "text",
			"version": 333,
			"versionNonce": 812543225,
			"isDeleted": false,
			"id": "hCxwTSH0",
			"fillStyle": "cross-hatch",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 4664.647420598919,
			"y": -622.4052008926825,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 182.091796875,
			"height": 41.4,
			"seed": 202209030,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1713771502122,
			"link": null,
			"locked": false,
			"fontSize": 36,
			"fontFamily": 2,
			"text": "Deklaration",
			"rawText": "Deklaration",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "Deklaration",
			"lineHeight": 1.15,
			"baseline": 33
		},
		{
			"type": "text",
			"version": 384,
			"versionNonce": 99366489,
			"isDeleted": false,
			"id": "Q6NNuIQH",
			"fillStyle": "cross-hatch",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 4126.14859610824,
			"y": -764.7634187226871,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 224.138671875,
			"height": 41.4,
			"seed": 1491682522,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1713771504354,
			"link": null,
			"locked": false,
			"fontSize": 36,
			"fontFamily": 2,
			"text": "Instanziierung",
			"rawText": "Instanziierung",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "Instanziierung",
			"lineHeight": 1.15,
			"baseline": 33
		},
		{
			"type": "rectangle",
			"version": 241,
			"versionNonce": 1223214231,
			"isDeleted": false,
			"id": "dGAYTccmktWMbGQiPiuJT",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "dashed",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 3031.723629697402,
			"y": -920.7731384157014,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 549.6706530209902,
			"height": 593.7913650693112,
			"seed": 523692889,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 3
			},
			"boundElements": [
				{
					"id": "3GDEnfnV_GX5rfI7R9ILJ",
					"type": "arrow"
				}
			],
			"updated": 1713771487510,
			"link": null,
			"locked": false
		},
		{
			"type": "rectangle",
			"version": 407,
			"versionNonce": 1027419735,
			"isDeleted": false,
			"id": "KhmrmBfHn4c693pwy59LP",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 3148.941198591959,
			"y": -775.8279235549244,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "#a5d8ff",
			"width": 250.8685837190788,
			"height": 98.53389969054295,
			"seed": 1473386553,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 3
			},
			"boundElements": [
				{
					"type": "text",
					"id": "3aSo0tyO"
				},
				{
					"id": "8fjZPIFOmm3PSgDiKnFat",
					"type": "arrow"
				},
				{
					"id": "kgiZjz-ytsEiuHDJjUg3y",
					"type": "arrow"
				},
				{
					"id": "3GDEnfnV_GX5rfI7R9ILJ",
					"type": "arrow"
				}
			],
			"updated": 1713771487510,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 431,
			"versionNonce": 376117623,
			"isDeleted": false,
			"id": "3aSo0tyO",
			"fillStyle": "cross-hatch",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 3155.7231467014985,
			"y": -753.5609737096529,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 237.3046875,
			"height": 54,
			"seed": 842311961,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1713771475523,
			"link": null,
			"locked": false,
			"fontSize": 45,
			"fontFamily": 3,
			"text": "display.h",
			"rawText": "display.h",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "KhmrmBfHn4c693pwy59LP",
			"originalText": "display.h",
			"lineHeight": 1.2,
			"baseline": 43
		},
		{
			"type": "rectangle",
			"version": 462,
			"versionNonce": 180651737,
			"isDeleted": false,
			"id": "RuFKccM4iLp5Ip4rgT6J4",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 3157.0520728861147,
			"y": -527.678014360948,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "#a5d8ff",
			"width": 305.37372399138206,
			"height": 118,
			"seed": 1204952569,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 3
			},
			"boundElements": [
				{
					"type": "text",
					"id": "VYcXZTSl"
				},
				{
					"id": "8fjZPIFOmm3PSgDiKnFat",
					"type": "arrow"
				},
				{
					"id": "kgiZjz-ytsEiuHDJjUg3y",
					"type": "arrow"
				}
			],
			"updated": 1713771496253,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 501,
			"versionNonce": 444079929,
			"isDeleted": false,
			"id": "VYcXZTSl",
			"fillStyle": "cross-hatch",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 3164.7194036318056,
			"y": -495.67801436094805,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 290.0390625,
			"height": 54,
			"seed": 934147801,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1713771496253,
			"link": null,
			"locked": false,
			"fontSize": 45,
			"fontFamily": 3,
			"text": "display.cpp",
			"rawText": "display.cpp",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "RuFKccM4iLp5Ip4rgT6J4",
			"originalText": "display.cpp",
			"lineHeight": 1.2,
			"baseline": 43
		},
		{
			"type": "arrow",
			"version": 987,
			"versionNonce": 481387673,
			"isDeleted": false,
			"id": "8fjZPIFOmm3PSgDiKnFat",
			"fillStyle": "cross-hatch",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 3278.6708614228355,
			"y": -535.5466416702959,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0.6449286597098762,
			"height": 129.97192311227957,
			"seed": 1952166841,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1713771496253,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "RuFKccM4iLp5Ip4rgT6J4",
				"gap": 7.868627309347744,
				"focus": -0.2052553075334839
			},
			"endBinding": {
				"elementId": "KhmrmBfHn4c693pwy59LP",
				"gap": 11.775459081805934,
				"focus": -0.04171902965538006
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "triangle",
			"points": [
				[
					0,
					0
				],
				[
					0.6449286597098762,
					-129.97192311227957
				]
			]
		},
		{
			"type": "text",
			"version": 264,
			"versionNonce": 909177463,
			"isDeleted": false,
			"id": "xc298Qst",
			"fillStyle": "cross-hatch",
			"strokeWidth": 4,
			"strokeStyle": "dashed",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 3116.695101764552,
			"y": -882.1540308268122,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 369.140625,
			"height": 54,
			"seed": 1375655065,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1713771475524,
			"link": null,
			"locked": false,
			"fontSize": 45,
			"fontFamily": 3,
			"text": "Display Klasse",
			"rawText": "Display Klasse",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "Display Klasse",
			"lineHeight": 1.2,
			"baseline": 43
		},
		{
			"type": "arrow",
			"version": 496,
			"versionNonce": 1204933209,
			"isDeleted": false,
			"id": "kgiZjz-ytsEiuHDJjUg3y",
			"fillStyle": "cross-hatch",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 3303.448313692632,
			"y": -661.5639069188192,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 0.885271627504153,
			"height": 112.14020302381095,
			"seed": 1414191481,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1713771496253,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "KhmrmBfHn4c693pwy59LP",
				"gap": 15.730116945562258,
				"focus": -0.2351388808378834
			},
			"endBinding": {
				"elementId": "RuFKccM4iLp5Ip4rgT6J4",
				"gap": 21.745689534060148,
				"focus": -0.051016596758329556
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "triangle",
			"points": [
				[
					0,
					0
				],
				[
					-0.885271627504153,
					112.14020302381095
				]
			]
		},
		{
			"type": "text",
			"version": 156,
			"versionNonce": 278003895,
			"isDeleted": false,
			"id": "LhLTNBvh",
			"fillStyle": "cross-hatch",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 3057.460743867586,
			"y": -624.7966410345521,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 210.111328125,
			"height": 41.4,
			"seed": 1015235161,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1713771475524,
			"link": null,
			"locked": false,
			"fontSize": 36,
			"fontFamily": 2,
			"text": "Initialisierung",
			"rawText": "Initialisierung",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "Initialisierung",
			"lineHeight": 1.15,
			"baseline": 33
		},
		{
			"type": "text",
			"version": 189,
			"versionNonce": 1981731287,
			"isDeleted": false,
			"id": "tRktdXxC",
			"fillStyle": "cross-hatch",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 3324.0234215285213,
			"y": -622.9582356635424,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 182.091796875,
			"height": 41.4,
			"seed": 1467715385,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1713771475524,
			"link": null,
			"locked": false,
			"fontSize": 36,
			"fontFamily": 2,
			"text": "Deklaration",
			"rawText": "Deklaration",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "Deklaration",
			"lineHeight": 1.15,
			"baseline": 33
		},
		{
			"type": "arrow",
			"version": 1830,
			"versionNonce": 1585098233,
			"isDeleted": false,
			"id": "3GDEnfnV_GX5rfI7R9ILJ",
			"fillStyle": "cross-hatch",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 3407.303994337253,
			"y": -729.9713774415809,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 298.4829035744938,
			"height": 0.044918161373743715,
			"seed": 1547095159,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1713771496253,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "KhmrmBfHn4c693pwy59LP",
				"gap": 7.494212026214882,
				"focus": -0.06960232116570984
			},
			"endBinding": {
				"elementId": "BJNgOemEXP4xtbPiKUlhG",
				"gap": 1.7859962052548326,
				"focus": 0.04953322359191456
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "triangle",
			"points": [
				[
					0,
					0
				],
				[
					298.4829035744938,
					0.044918161373743715
				]
			]
		},
		{
			"type": "text",
			"version": 380,
			"versionNonce": 15154903,
			"isDeleted": false,
			"id": "TcjnFJP8",
			"fillStyle": "cross-hatch",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 3435.0316318341347,
			"y": -775.6489522693143,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 224.138671875,
			"height": 41.4,
			"seed": 891258071,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1713771496984,
			"link": null,
			"locked": false,
			"fontSize": 36,
			"fontFamily": 2,
			"text": "Instanziierung",
			"rawText": "Instanziierung",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "Instanziierung",
			"lineHeight": 1.15,
			"baseline": 33
		}
	],
	"appState": {
		"theme": "dark",
		"viewBackgroundColor": "#ffffff",
		"currentItemStrokeColor": "#000000",
		"currentItemBackgroundColor": "transparent",
		"currentItemFillStyle": "cross-hatch",
		"currentItemStrokeWidth": 4,
		"currentItemStrokeStyle": "dashed",
		"currentItemRoughness": 0,
		"currentItemOpacity": 100,
		"currentItemFontFamily": 3,
		"currentItemFontSize": 36,
		"currentItemTextAlign": "center",
		"currentItemStartArrowhead": null,
		"currentItemEndArrowhead": "triangle",
		"scrollX": -2461.886937823718,
		"scrollY": 1179.8852722562935,
		"zoom": {
			"value": 0.44999999999999996
		},
		"currentItemRoundness": "round",
		"gridSize": null,
		"gridColor": {
			"Bold": "#C9C9C9FF",
			"Regular": "#EDEDEDFF"
		},
		"currentStrokeOptions": null,
		"previousGridSize": null,
		"frameRendering": {
			"enabled": true,
			"clip": true,
			"name": true,
			"outline": true
		}
	},
	"files": {}
}
```
%%