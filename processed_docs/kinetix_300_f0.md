Installation Instructions

Kinetix 300 EtherNet/IP Indexing

Servo Drives

<!-- image -->

Catalog Numbers 2097-V31PR0, 2097-V31PR2, 2097-V32PR0, 2097-V32PR2,

2097-V32PR4, 2097-V33PR1, 2097-V33PR3, 2097-V33PR5, 2097-V33PR6, 2097-V34PR3,

2097-V34PR5, 2097-V34PR6

## Topic Page About the Kinetix 300 Drives 1

Important User Information 2

Catalog Number Explanation 3 Before You Begin 4

Safety Information 4

Install the Kinetix 300 Drive 5

Connector Data 7

Power Wiring Requirements 12

Motor Overload Protection 15

Circuit Breaker/Fuse Selection 16

Additional Resources 19

About the Kinetix 300 Drives

Kinetix® 300 EtherNet/IP indexing servo drives provide an Ethernet-enabled solution for applications with output power requirements in the range of 0.4…3.0 kW (2…12 A rms).

See the Kinetix 300 EtherNet/IP Indexing Servo Drives User Manual, publication

2097-UM001, for detailed information on how to wire, apply power, troubleshoot, and integrate

with ControlLogix®, CompactLogix™, or MicroLogix™ controller platforms.

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

2

Kinetix 300 EtherNet/IP Indexing Servo Drive

Important User Information

Read this document and the documents listed in the additional resources section about installation, configuration, and operation of this equipment before you install, configure, operate, or maintain this product. Users are required to familiarize themselves with

installation and wiring instructions in addition to requirements of all applicable codes, laws, and standards.

Activities including installation, adjustments, putting into service, use, assembly, disassembly, and maintenance are required to be carried out by suitably trained personnel in accordance with applicable code of practice.

If this equipment is used in a manner not specified by the manufacturer, the protection provided by the equipment may be impaired.

In no event will Rockwell Automation, Inc. be responsible or liable for indirect or consequential damages resulting from the use or application of this equipment. The examples and diagrams in this manual are included solely for illustrative purposes. Because of the many variables and requirements associated with any particular installation, Rockwell Automation, Inc. cannot assume responsibility or liability for actual

use based on the examples and diagrams. No patent liability is assumed by Rockwell Automation, Inc. with respect to use of information, circuits, equipment, or software described in this manual.

Reproduction of the contents of this manual, in whole or in part, without written permission of Rockwell Automation, Inc., is prohibited.

Throughout this manual, when necessary, we use notes to make you aware of safety considerations.

WARNING: Identifies information about practices or circumstances that can cause an explosion in a hazardous environment, which may lead to personal injury or death, property damage, or economic loss.

ATTENTION: Identifies information about practices or circumstances that can lead to personal injury or death, property damage, or economic loss. Attentions help you identify a hazard, avoid a hazard, and recognize the

consequence.

IMPORTANT Identifies information that is critical for successful application and understanding of the product.

Labels may also be on or inside the equipment to provide specific precautions.

SHOCK HAZARD: Labels may be on or inside the equipment, for example, a drive or motor, to alert people that dangerous voltage may be present.

BURN HAZARD: Labels may be on or inside the equipment, for example, a drive or motor, to alert people that surfaces may reach dangerous temperatures.

ARC FLASH HAZARD: Labels may be on or inside the equipment, for example, a motor control center, to alert people to potential Arc Flash. Arc Flash will cause severe injury or death. Wear proper Personal Protective Equipment (PPE). Follow ALL Regulatory requirements for safe work

practices and for Personal Protective Equipment (PPE).

Rockwell Automation Publication 2097-IN001K-EN-P - September 2015

Catalog Number Explanation

This publication applies to the following Kinetix 300 drives.

Kinetix 300 Drives (single-phase)

2097-V31PR0

120/240V, 1 Ø

2097-V31PR2 5.7

2097-V32PR0

2.8

240V, 1 Ø2097-V32PR2 5.7

240V, 1 Ø

2097-V32PR4 11.3

240V, 3 Ø

| Kinetix 300 Drives (single- or three-phase)   | Continuous Output   |
|-----------------------------------------------|---------------------|
| Cat. No. Input Voltage  Current A (0-pk)      | Continuous Output   |
|                                               | 2.8 120V, 1 Ø 2097-V33PR3 5.7                     |
| 240V3 Ø 2097-V33PR5 11.3                                               | 2.8 120V, 1 Ø 2097-V33PR3 5.7                     |
|                                               | 2.8 120V, 1 Ø 2097-V33PR3 5.7                     |

2097-V33PR6 17.0

| Kinetix 300 Drives (three-phase)                           |     |
|------------------------------------------------------------|-----|
| Cat. No. Input Voltage  Continuous Output Current A (0-pk) | 2.8 |
| 480V, 3 Ø 480V, 3 Ø2097-V34PR5 5.7                         | 2.8 |
| 2097-V34PR6 8.5                                            | 2.8 |
|                                                            | 2.8 |

Rockwell Automation Publication 2097-IN001K-EN-P - September 2015

Kinetix 300 EtherNet/IP Indexing Servo Drive

Continuous Output

2.8

Features

·

120V Doubler mode

·

·

Safe torque-off

Integrated AC line filter

·

Safe torque-off

Features

Safe torque-off

Features

Safe torque-off

3

<!-- image -->

<!-- image -->

4

Kinetix 300 EtherNet/IP Indexing Servo Drive

Before You Begin

Remove all packing material, wedges, and braces from within and around the components. After unpacking, check the item nameplate catalog number against the purchase order.

The Kinetix 300 drive ships with the following:

·

General-purpose power input (IPD) header, back-up power (BP) header, shunt resistor, and DC bus (BC) header, motor power (MP) header, and safe torque-off (STO) header

· A ground clamp that also provides strain relief for motor power cable

·

These installation instructions, publication 2097-IN001

TIP

The connector kit for motor feedback (catalog number 2090-K2CK-D15M) is not provided.

Replacement connector sets (catalog number 2097-CONN1) are also available.

- See the Kinetix Motion Accessories Specifications Technical Data, publication GMC-TD004, for more information.
- Safety Information

SHOCK HAZARD: Capacitors retain charge for approximately 300 s after power is removed. Disconnect

incoming power and wait at least five minutes before touching the

drive. Failure to observe this precaution could result in severe

bodily injury or loss of life.

<!-- image -->

WARNING: The opening of branch-circuit protective device can be an indication that a fault has been interrupted. To reduce the risk of fire or electric shock, parts that carry current and other components of the controller must be examined and replaced if damaged.

<!-- image -->

Rockwell Automation Publication 2097-IN001K-EN-P - September 2015

RISQUE DE CHOC: Les condensateurs restent sous charge pendant environ 300

secondes après une coupure de courant.

Couper l'alimentation et patienter pendant au moins 5 minutes avant de

toucher l'entraînement. Le non-respect de cette précaution peut entraîner des

blessures corporelles graves ou la mort.

AVERTISSEMENT: Le déclenchement du dispositif de protection du circuit de

dérivation peut être dû à une coupure qui résulte d'un courant de défaut. Pour

limiter le risque d'incendie ou de choc

électrique, examiner les pièces porteuses de courant et les autres éléments du

contrôleur et les remplacer s'ils sont endommagés. En cas de grillage de

l'élément traverse par le courant dans un relais de surcharge, le relais tout entier

doit être remplacé.

<!-- image -->

<!-- image -->

Install the Kinetix 300 Drive

These procedures assume that you have prepared your panel, and understand how to bond your system. For installation instructions regarding equipment and accessories that are not included

here, refer to the instructions that came with those products you apply power. Once power is applied, connector terminals can have voltage present even when

not in use.

ATTENTION: Plan the installation of your system so that you can cut, drill, tap, and weld with the system removed from the enclosure. Because the system is open-type construction, be careful to keep metal debris from falling into it. Metal debris or other foreign matter can become lodged in

Mount the Kinetix 300 Drive the circuitry and result in damage to components.

Follow these steps to mount the drive.

1. Observe these clearance requirements when mounting the drive to the panel. IMPORTANT Mount the module in an upright position as shown. Do not mount the module on its side.

- A

25 mm (1.0 in.) Clearance for Airflow and Installation

3 mm (0.12 in.) Side Clearance 3 mm (0.12 in.) Side Clearance

Extra clearance and different hole patterns are required for side mount and rear mount AC line filters. See the table and step 2 for more details.

More clearance is required depending on the other accessories installed.

More clearance is required for the cable and wires that are connected to the

An extra 150 mm (6.0 in.) clearance is required when the drive is mounted next to noise sensitive equipment or clean wireways.

<!-- image -->

| 25 mm (1.0 in.) Clearance    |
|------------------------------|
| for Airflow and Installation |

Kinetix 300 EtherNet/IP Indexing Servo Drive

Drive

Cat. No.

2097-V31PR0

2097-V31PR2

2097-V32PR0

2097-V32PR2

2097-V32PR4

2097-V33PR1

2097-V33PR3

A

mm (in.)

185 (7.29)

230 (9.04)

185 (7.29)

2097-V33PR5

2097-V33PR6 230 (9.04)

2097-V34PR3

185 (7.29)

2097-V34PR5

2097-V34PR6 230 (9.04)

(1) If you are using an AC line filter, add 50

mm (2 in.).

Rockwell Automation Publication 2097-IN001K-EN-P - September 2015

(1)

(1)

5

6

Kinetix 300 EtherNet/IP Indexing Servo Drive

2. Mount the Kinetix 300 drive to the cabinet subpanel with an M4 (#6-32) steel machine screw torqued to 1.1 N·m (9.8 lb·in).

For catalog numbers 2097-V33PR1, 2097-V33PR3, 2097-V33PR5, 2097-V34PR3, and

2097-V34PR5 that use an AC line filter, refer to the AC Line Filter Installation

Instructions, publication 2097-IN003, for the subpanel mounting hole pattern.

Kinetix 300 Drive Mounting Dimensions

- A Dimensions are in mm (in.).

7.1 (0.28) 5.0 (0.19)

9.7

(0.38)

<!-- image -->

B

30.8

(1.21)

300

38.1

(1.5)

Extra clearance below the connector kit is necessary to provide the

Dimensions mm (in.)

AB AB

2097-V31PR0 185.1 (7.29) 68.0 (2.68) 2097-V33PR3 185.1 (7.29) 68.5 (2.70)

2097-V31PR2 185.1 (7.29) 68.5 (2.70) 2097-V33PR5 185.1 (7.29) 94.4 (3.72)

2097-V32PR0 229.6 (9.04) 68.0 (2.68) 2097-V33PR6 229.6 (9.04) 68.0 (2.68)

2097-V32PR2 229.6 (9.04) 68.5 (2.70) 2097-V34PR3 185.1 (7.29) 68.5 (2.70)

2097-V32PR4 229.6 (9.04) 86.8 (3.42) 2097-V34PR5 185.1 (7.29) 94.4 (3.72)

2097-V33PR1 185.1 (7.29) 68.0 (2.68) 2097-V34PR6 229.6 (9.04) 68.0 (2.68)

Rockwell Automation Publication 2097-IN001K-EN-P - September 2015

| Rockwell Automation Publication 2097-IN001K-EN-P - September 2015   |
|---------------------------------------------------------------------|

Ø 4.57

(0.18) 3x

182

(7.18)

190

(7.50)

Connector Data

Use this illustration to identify the Kinetix 300 drive features and indicators.

Kinetix 300 Drive Features and Indicators

12

11

<!-- image -->

Item Description

1 Ground lug

2 Status and diagnostic display

3 Display-control push buttons (3)

4 Back-up power (BP) connector

5 Shunt resistor and DC bus (BC) connector

6 Ground lug

7 Bottom mounting flange

8 Motor feedback (MF) connector

9 I/O (IOD) connector

10 Ethernet communication port (Port 1)

11 Memory module

12 Top mounting flange

13 Mains (IPD) connector

14 Motor power (MP) connector

15 Safe torque-off (STO) connector

16 Heat sink (on some models)

Bottom View

(2097-V33PR5

Kinetix 300 drive is shown)

14

15

Rockwell Automation Publication 2097-IN001K-EN-P - September 2015

| 4   |
|-----|

Top View

(2097-V33PR5

Kinetix 300 drive is shown)

13

<!-- image -->

1

2

3

Kinetix 300 EtherNet/IP Indexing Servo Drive

7

8

Kinetix 300 EtherNet/IP Indexing Servo Drive

Kinetix 300 Drive Connectors

Designator Description Connector

IPD AC mains input power 4-position plug/header

PORT1 Ethernet communication port RJ45 Ethernet

IOD I/O SCSI 50-pin high-density connector

MF Motor feedback 15-pin high-density D-shell (male)

BP Back-up power 2-pin quick-connect terminal block

BC Shunt resistor and DC bus 5-pin quick-connect terminal block

MP Motor power 6-pin quick-connect terminal block

STO Safe torque-off (STO) terminal 6-pin quick-connect terminal block

| Mains (IPD) Connector Pinout       |
|------------------------------------|
| IPD Designator Description Signal  |
| L3 AC power in (3-phase models) L3 |
| L2 AC power in L2                  |
| L1 AC power in L1                  |

PE Protective earth (ground) PE

Pin Orientation for 8-pin Ethernet Communication Port (port 1)

Port 1 Pin Description Signal

1 Transmit port (+) data terminal + TX

2 Transmit port (-) data terminal - TX

3 Receive port (+) data terminal + RX

4– –

## 5– –

6 Receive port (-) data terminal - RX

7– –

8– –

<!-- image -->

Rockwell Automation Publication 2097-IN001K-EN-P - September 2015

1

8

I/O (IOD) Connector Pinout

IOD Pin Description Signal

1 Master encoder A+/Step+ input MA+

2 Master encoder A-/Step- input MA-

4 Master encoder B-/Direction- input MB-

5 Drive logic common GND

6 Reserved –

7 Buffered encoder output: channel A+ BA+

8 Buffered encoder output: channel A- BA-

9 Buffered encoder output: channel B+ BB+

10 Buffered encoder output: channel B- BB-

11 Buffered encoder output: channel Z+ BZ+

12 Buffered encoder output: channel Z- BZ-

13…21 Reserved –

22 Analog common ACOM

23 Analog output (max 10 mA) AO

24 Positive (+) of analog signal input AIN1+

25 Negative (-) of analog signal input AIN1-

26 Digital input group ACOM terminal IN\_A\_COM

<!-- image -->

27 Digital input A1 IN\_A1

28 Digital input A2 IN\_A2

29 Digital input A3 IN\_A3

30 Digital input A4 IN\_A4

31 Digital input group BCOM terminal IN\_B\_COM

32 Digital input B1 IN\_B1

33 Digital input B2 IN\_B2

34 Digital input B3 IN\_B3

35 Digital input B4 IN\_B4

36 Digital input Group CCOM Terminal IN\_C\_COM

37 Digital input C1 IN\_C1

38 Digital input C2 IN\_C2

39 Digital input C3 IN\_C3

Rockwell Automation Publication 2097-IN001K-EN-P - September 2015

Kinetix 300 EtherNet/IP Indexing Servo Drive

1

25

26

50

9

10

Kinetix 300 EtherNet/IP Indexing Servo Drive

I/O (IOD) Connector Pinout (continued)

IOD Pin Description Signal

40 Digital input C4 IN\_C4

41 Ready output collector RDY+

42 Ready output emitter RDY-

43 Programmable output #1 collector OUT1-C

44 Programmable output #1 emitter OUT1-E

45 Programmable output #2 collector OUT2-C

46 Programmable output #2 emitter OUT2-E

47 Programmable output #3 collector OUT3-C

48 Programmable output #3 emitter OUT3-E

49 Programmable output #4 collector OUT4-C

50 Programmable output #4 emitter OUT4-E

Control Power Back-up (BP) Connector Pinout

Description Signal

+24V Positive 24V DC +24V DC

-24V 24V DC power supply return Return

| BP         |
|------------|
| Designator |

## Shunt Resistor and DC Bus (BC) Pinout

Description Signal

+

+ +

| Positive DC bus and shunt resistor   |
|--------------------------------------|

SH Shunt resistor SH

## –

Negative DC bus

– –

Rockwell Automation Publication 2097-IN001K-EN-P - September 2015

–

<!-- image -->

1

25

26

50

Motor Power (MP) Pinout

MP

Description Signal

Designator

PE Protective earth (ground) PE

V Motor power out V

U Motor power out U

| Motor Feedback (MF) Connector Pinout   |
|----------------------------------------|
| MF Pin Description  (1)                |
| 1  Sine differential input+            |
| AM+ differential input+                |
| 2  Sine differential input AM- differential input                                        |

## 3

Cosine differential input+

BM+ differential input+

| 4  Cosine differential input BM- differential input                                                                    |
|--------------------------------------------------------------------|
| 5  Data differential input +                                       |
| 10  Data differential input -                                      |
| 11 Motor thermal switch (normally closed)                          |
| (2) Not applicable unless motor has integrated thermal protection. |

<!-- image -->

(2)

Signal

SIN+

AM+

SIN-

AM-

COS+

BM+

COS-

BM-

DATA+

IM+

6 Common ECOM

7 Encoder power (+9V) EPWR\_9V

8 Single-ended 5V Hall effect commutation S3

9 Reserved –

<!-- image -->

DATA-

IM-

TS

12 Single-ended 5V Hall effect commutation S1

13 Single-ended 5V Hall effect commutation S2

14 Encoder power (+5V) EPWR\_5V

15 Reserved –

(1) Determine which power supply your encoder requires and connect to only the specified supply. Do not make connections to both

.

ATTENTION: To avoid damage to components, determine which power supply your encoder requires and connect encoder power to either the 5V or 9V supply, but not both.

Rockwell Automation Publication 2097-IN001K-EN-P - September 2015

Kinetix 300 EtherNet/IP Indexing Servo Drive

(1)

(1)

Pin 15

Pin 11

Pin 6

11

Pin 10

Pin 5

Pin 1

12

Kinetix 300 EtherNet/IP Indexing Servo Drive

Safe Torque-off (STO) Pinout

STO Pin Description Signal

1 +24V DC output from the drive +24V DC Control

2 +24V DC output common Control COM

3 Safety status Safety Status

4 Safety input 1 (+24V DC to enable) Safety Input 1

5 Safety common Safety COM

6 Safety input 2 (+24V DC to enable) Safety Input 2

The Kinetix 300 drives ship with the safe torque-off circuitry enabled. Connect the safe torque-off inputs to a safety circuit or install motion-allowed jumpers to obtain motion. See the

Kinetix 300 EtherNet/IP Indexing Servo Drives User Manual, publication 2097-UM001, for

| Power Wiring Requirements   |
|-----------------------------|

Wire must be copper with 75 °C (167 °F) minimum rating. The phase connections of the main AC power are arbitrary and an earth-ground connection is required for safe and proper operation.

IMPORTANT

The National Electrical Code and local electrical codes take precedence over the values and methods provided.

Kinetix 300 Drive Power-Wiring Requirements Cat. No. Description Terminals Recommended Wire Size mm

2

(AWG)

Strip

Length

Torque

Value

mm2 (AWG)
mm (in.)
N·m (lb·in) Pin Signal

2.5 (14)

mm (in.)

7 (0.28)

2097-V31PR0 2097-V32PR0 2097-V32PR2

2097-V33PR1

## 2097-V33PR3 2097-V34PR3

2097-V34PR5

L3

L2

| 2097-V34PR6                          | Mains input power   | L1 PE                                                             |          |
|--------------------------------------|---------------------|-------------------------------------------------------------------|----------|
| 2097-V32PR4                          |                     |                                                                   | 4.0 (12) |
| 2097-V33PR5  2097-V31PR2 2097-V33PR6 |                     |                                                                   |          |
|                                      |                     | Rockwell Automation Publication 2097-IN001K-EN-P - September 2015 |          |

0.5 (4.5)

0.56…0.79

(5.0…7.0)

<!-- image -->

Cat. No. Description

2097-V31PR0

2097-V32PR0

2097-V32PR2

2097-V32PR4

## 2097-V33PR1 2097-V33PR3

Kinetix 300 EtherNet/IP Indexing Servo Drive

Kinetix 300 Drive Power-Wiring Requirements (continued)

Terminals Recommended

Wire Size mm

2

(AWG)

Strip

Length

Torque

Value

mm2 (AWG)
mm (in.)
N·m (lb·in) Pin Signal

PE

W

mm (in.)

2.5 (14) 7 (0.28) 0.5 (4.5)

2097-V33PR6 4.0 (12) 7 (0.28) 0.5 (4.5)

2.5 (14) 7 (0.28) 0.5 (4.5)

2097-V33PR6 4.0 (12) 7 (0.28) 0.5 (4.5)

1.5 (16) 6 (0.25) 0.5 (4.5)

Installation complies with specifications regarding wire types, conductor sizes, branch circuit protection, and disconnect devices. The National Electrical Code (NEC) and local codes outline

Motor power connectors are used only for connection purposes. Do not use motor power connectors to turn the unit on and off.

|                          | 2097-V33PR5 2097-V34PR3 2097-V34PR5 Motor power   | 2097-V33PR5 2097-V34PR3 2097-V34PR5 Motor power                                                                                 |                               | V U             |
|--------------------------|---------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|-------------------------------|-----------------|
|                          | 2097-V34PR6 2097-V31PR2                           |                                                                                                                                 |                               |                 |
| 2097-V31PR0 2097-V32PR0  | 2097-V31PR0 2097-V32PR0                           | 2097-V32PR2 2097-V32PR4 2097-V33PR1 2097-V33PR3 2097-V33PR5 + + SH                                                              | Shunt resistor and DC bus (1) |                 |
|                          |                                                   | 2097-V34PR6 2097-V31PR2                                                                                                         |                               |                 |
| 2097-V3xPRx  2097-V3xPRx | 2097-V3xPRx  2097-V3xPRx                          |                                                                                                                                 | STO-1 (2)                     | +24V DC Control |
|                          |                                                   | (1) Use only for shunt on.                                                                                                      |                               |                 |
|                          |                                                   | (2) Use only for bypassing the STO circuit.                                                                                     |                               |                 |
|                          |                                                   | ATTENTION: To avoid personal injury and equipment damage, make sure •  provisions for safely installing electrical equipment. • |                               |                 |

·

Shielded power cables are grounded to help prevent potentially high voltages on the shield.

- Rockwell Automation Publication 2097-IN001K-EN-P - September 2015

13

14

Kinetix 300 EtherNet/IP Indexing Servo Drive

Ground Your Kinetix 300 Drive to the Subpanel

If the Kinetix 300 drive is mounted on a painted subpanel, ground to a bonded cabinet-ground bus with a braided ground strap or 4.0 mm

Connect the Braided Ground Strap

Braided

Ground Strap

(12 AWG) solid-copper wire, 100 mm (3.9 in.) long.

Bonded Cabinet

Ground Bus

Ground Grid or Power Ground Stud

Distribution Ground

For dimensions, see Kinetix 300 Drive Mounting Dimensions on page 6

<!-- image -->

Rockwell Automation Publication 2097-IN001K-EN-P - September 2015

2

.

Kinetix 300 Drive Motor-power Wire Shielding

A motor-power ground clamp and two #6-32 x 1 screws are supplied with the Kinetix 300 drive.

Install the supplied motor-power ground clamp within 50…75 mm (2…3 in.) of the drive by using the two #6-32 x 1 screws.

## Motor-power Ground Clamp

25 (1.0)

34.0

(1.34)

12.7

(0.50)

<!-- image -->

50…75

(2…3)

This servo drive uses solid-state motor overload protection that operates in accordance with

UL 508C. Motor overload protection algorithms (thermal memory) predict actual motor temperature that is based on operating conditions as long as control power is continuously

applied. However, when control power is removed, thermal memory is not retained.

This drive also provides an input for an external temperature sensor or thermistor device, which is embedded in the motor, to support the UL requirement for motor overload protection.

The drive supports some motors that do not contain temperature sensors or thermistors;

therefore, motor overload protection against excessive consecutive motor overloads followed by power-up is not supported.

Rockwell Automation Publication 2097-IN001K-EN-P - September 2015

Kinetix 300 EtherNet/IP Indexing Servo Drive

15

16

Kinetix 300 EtherNet/IP Indexing Servo Drive

This servo drive meets the following UL 508C requirements for solid-state overload protection.

Motor Overload Protection Trip Point Value

Ultimately 100% overload

Within 8 minutes 200% overload

Within 20 seconds 600% overload

ATTENTION: Avoid overheat damage to your motor from excessive and successive motor overload faults by following the motor and drive-combination wiring diagram that is provided in

See your servo drive user manual for the interconnect diagram that illustrates the wiring between

| your motor and drive.  the user manual.   |
|-------------------------------------------|

<!-- image -->

Circuit Breaker/Fuse Selection The Kinetix 300 drives use internal solid-state motor short-circuit protection. When protected by suitable branch circuit protection the drives are rated for use on a circuit that can deliver up to

100,000 A.

See Kinetix 300 Drive Power Specifications in Kinetix Servo Drives Specifications Technical

Data, publication GMC-TD003 for input current and inrush current specifications for your

Kinetix 300 drive.

See Circuit Breaker/Fuse Specifications on page 17 and page 18 for recommended circuit breakers and fuses.

Rockwell Automation Publication 2097-IN001K-EN-P - September 2015

Circuit Breaker/Fuse Specifications

The following fuses and Allen-Bradley® circuit breakers are recommended for use with

2097-VxxPRx drives.

Fuse and Circuit Breaker Specifications for UL Applications

Cat. No. Drive

Voltage

Single-phase

2097-V31PR0 120V (voltage doubler)

(Bussmann)

Cat. No.

Motor Protection CB,

Self-protected CMC

Cat. No.

KTK-R-20 (20A) 1489-M1C200 140M-D8E-C20

120/240V Single-phase KTK-R-10 (10A) 1489-M1C100 140M-C2E-C10

120V

Single-phase

KTK-R-30 (30A) 1489-M1C300 140M-F8E-C32

120/240V Single-phase KTK-R-20 (20A) 1489-M1C200 140M-D8E-C20

KTK-R-20 (20A) 1489-M1C150 140M-D8E-C16

240V Single-phase2097-V32PR2 KTK-R-20 (20A) 1489-M1C200 140M-D8E-C20

2097-V32PR4 KTK-R-30 (30A) 1489-M1C300 140M-F8E-C32

120/240V Single-phase KTK-R-20 (20A) 1489-M1C200 140M-D8E-C20

240V Three-phase KTK-R-15 (15A) 1489-M3C150 140M-D8E-C16

120/240V Single-phase KTK-R-20 (20A) 1489-M1C200 140M-D8E-C20

240V Three-phase KTK-R-15 (15A) 1489-M3C150 140M-D8E-C16

120/240V Single-phase KTK-R-30 (30A) 1489-M1C300 140M-F8E-C32

240V Three-phase KTK-R-20 (20A) 1489-M3C200 140M-D8E-C20

140M-F8E-C32

KTK-R-10 (10A) 1489-M3C100 140M-C2E-C10

480V Three-phase2097-V34PR5 KTK-R-10 (10A) 1489-M3C100 140M-C2E-C10

2097-V34PR6 KTK-R-20 (20A) 1489-M3C200 140M-D8E-C20

Refer to http://ab.rockwellautomation.com/allenbradley/productdirectory.page? for product literature with specific short-circuit ratings.

| 2097-V31PR2 2097-V32PR0                                                                                                    | (voltage doubler)                           |                                                                                                             |
|----------------------------------------------------------------------------------------------------------------------------|---------------------------------------------|-------------------------------------------------------------------------------------------------------------|
|                                                                                                                            | 240V Single-phase                           |                                                                                                             |
| 2097-V33PR1                                                                                                                |                                             |                                                                                                             |
| 2097-V33PR3                                                                                                                |                                             |                                                                                                             |
| 2097-V33PR5                                                                                                                |                                             |                                                                                                             |
|                                                                                                                            | 120/240V Single-phase  N/A                  | LPJ-40SP (40A)                                                                                              |
| 2097-V33PR6                                                                                                                |                                             | Class J                                                                                                     |
|                                                                                                                            | 240V Three-phase KTK-R-30 (30A) 1489-M3C300 |                                                                                                             |
| 2097-V34PR3                                                                                                                |                                             |                                                                                                             |
|                                                                                                                            | 480V Three-phase                            |                                                                                                             |
| (1) Bulletin 1492 and 1489 circuit protection devices have lower short-circuit current ratings than Bulletin 140M devices. |                                             | (2) For UL applications, Bulletin 140M devices are applied as self-protected combination motor controllers. |
|                                                                                                                            |                                             | (2) For UL applications, Bulletin 140M devices are applied as self-protected combination motor controllers. |

Rockwell Automation Publication 2097-IN001K-EN-P - September 2015

Miniature CB (1)

Cat. No.

Kinetix 300 EtherNet/IP Indexing Servo Drive

17

(1)(2)

18

Kinetix 300 EtherNet/IP Indexing Servo Drive

Fuse and Circuit Breaker Specifications IEC (non-UL) Applications

Cat. No. Drive

Voltage

120V

Single-phase

(voltage doubler)

Phase Miniature CB (1)

Cat. No.

Motor Protection CB (1)

Cat. No.

1489-M1C200 1492-SPM1D200 140M-D8E-C20

120/240V Single-phase 1489-M1C100 1492-SPM1D100 140M-C2E-C10

## 120V

Single-phase

(voltage doubler)

1489-M1C300 1492-SPM1D300 140M-F8E-C32

120/240V Single-phase 1489-M1C200 1492-SPM1D200 140M-D8E-C20

1489-M1C150 1492-SPM1D150 140M-D8E-C16

240V Single-phase2097-V32PR2 1489-M1C200 1492-SPM1D200 140M-D8E-C20

2097-V32PR4 1489-M1C300 1492-SPM1D320 140M-F8E-C32

120/240V Single-phase 1489-M1C200 1492-SPM1D200 140M-D8E-C20

240V Three-phase 1489-M3C150 1492-SPM3D150 140M-D8E-C16

120/240V Single-phase 1489-M1C200 1492-SPM1D200 140M-D8E-C20

240V Three-phase 1489-M3C150 1492-SPM3D150 140M-D8E-C16

120/240V Single-phase 1489-M1C300 1492-SPM1D300 140M-F8E-C32

240V Three-phase 1489-M3C200 1492-SPM3D200 140M-D8E-C20

140M-F8E-C32

1489-M3C100 1492-SPM3D100 140M-C2E-C10

480V Three-phase2097-V34PR5 1489-M3C100 1492-SPM3D100 140M-C2E-C10

2097-V34PR6 1489-M3C200 1492-SPM3D200 140M-D8E-C20

Refer to http://ab.rockwellautomation.com/allenbradley/productdirectory.page? for product literature with specific short-circuit ratings

2097-V31PR2

|             | 240V Single-phase                                                                                                          |
|-------------|----------------------------------------------------------------------------------------------------------------------------|
| 2097-V33PR1 |                                                                                                                            |
| 2097-V33PR3 |                                                                                                                            |
| 2097-V33PR5 |                                                                                                                            |
| 2097-V33PR5 | 120/240V Single-phase N/A N/A                                                                                              |
| 2097-V33PR6 | 240V Three-phase 1489-M3C300 1492-SPM3D300                                                                                 |
| 2097-V34PR3 |                                                                                                                            |
|             | 480V Three-phase                                                                                                           |
|             | (1) Bulletin 1492 and 1489 circuit protection devices have lower short-circuit current ratings than Bulletin 140M devices. |

Rockwell Automation Publication 2097-IN001K-EN-P - September 2015

Additional Resources

These documents contain information about related products from Rockwell Automation.

Resource Description

Kinetix 300 EtherNet/IP Indexing Servo Drives User Manual, publication 2097-UM001

Kinetix Servo Drives Specifications Technical Data, publication GMC-TD003

Provides information on how to install, configure, start up, and

Provides product specifications for Kinetix Integrated Motion over EtherNet/IP, Integrated Motion over SERCOS interface,

EtherNet/IP network, and component servo drive families.

Kinetix Motion Accessories Specifications Technical Data, publication GMC-TD004 Provides product specifications for Bulletin 2090 motor and interface cables, Low-profile connector kits, drive power components, and other servo drive accessory items.

You can view or download publications at http://www.rockwellautomation.com/literature. To order paper copies of technical documentation, contact your local Allen-Bradley distributor or

| Rockwell Automation sales representative.   |
|---------------------------------------------|

Rockwell Automation Publication 2097-IN001K-EN-P - September 2015

Kinetix 300 EtherNet/IP Indexing Servo Drive

19

Rockwell Automation Support

Rockwell Automation provides technical information on the Web to assist you in using its products.

At http://www.rockwellautomation.com/support you can find technical and application notes, sample code, and links to software service packs. You can also visit our Support Center at https://rockwellautomation.custhelp.com/ for software updates, support chats

and forums, technical information, FAQs, and to sign up for product notification updates.

In addition, we offer multiple support programs for installation, configuration, and troubleshooting. For more information, contact your local distributor or Rockwell Automation representative, or visit http://www.rockwellautomation.com/services/online-phone

Installation Assistance

If you experience a problem within the first 24 hours of installation, please review the information that's contained in this manual. You can also contact a special Customer Support number for initial help in getting your product up and running.

United States or Canada 1.440.646.3434

Outside United States or Use the Worldwide Locator at http://www.rockwellautomation.com/rockwellautomation/support/overview.page, or contact your local Rockwell Automation representative.

Canada

New Product Satisfaction Return Rockwell Automation tests all of its products to help ensure that they are fully operational when shipped from the manufacturing

Contact your distributor. You must provide a Customer Support case number (call the phone number

Outside United States Please contact your local Rockwell Automation representative for the return procedure.

| facility. However, if your product is not functioning and needs to be returned, follow these procedures.   |
|------------------------------------------------------------------------------------------------------------|
| United States  above to obtain one) to your distributor to complete the return process.                    |

Documentation Feedback

Your comments will help us serve your documentation needs better. If you have any suggestions on how to improve this document, complete this form, publication RA-DU002, available at http://www.rockwellautomation.com/literature/

| Rockwell Automation maintains current product environmental information on its website at   |
|---------------------------------------------------------------------------------------------|

.

http://www.rockwellautomation.com/rockwellautomation/about-us/sustainability-ethics/product-environmental-compliance.page

Allen-Bradley, ControlLogix, CompactLogix, Kinetix, MicroLogix, Rockwell Software, and Rockwell Automation are trademarks of Rockwell Automation, Inc.

Trademarks not belonging to Rockwell Automation are property of their respective companies.

Rockwell Otomasyon Ticaret A.Ş., Kar Plaza İş Merkezi E Blok Kat:6 34752 İçerenköy, İstanbul, Tel: +90 (216) 5698400

Publication 2097-IN001K-EN-P - September 2015

Supersedes Publication 2097-IN001J-EN-P - December 2014 Copyright © 2015 Rockwell Automation, Inc. All rights reserved. Printed in the U.S.A.

(13496813)

.

<!-- image -->

.