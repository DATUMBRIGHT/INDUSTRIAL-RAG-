Installation Instructions

Original Instructions

PanelView Plus 700 to 1500 and PanelView

Plus Compact 1000 Terminals and Display

Modules

Catalog Numbers 2711P-Kxxxx, 2711P-Txxxx, 2711P-Bxxxx, 2711P-RDxxxx, 2711PC-

## T10C4D1 Topic Page Summary of Changes 1 Important User Information 2 About This Publication 3

Hazardous Locations

5

Wiring and Safety Guidelines 8 About the PanelView Plus 700 to 1500 Terminals 9

| Troubleshooting   |                    |
|-------------------|--------------------|
|                   | Summary of Changes |

Updated the Attention note in the section titled External Power Supply for Nonisolated DC Terminals and in the section titled External Power for Isolated DC Terminals.

<!-- image -->

<!-- image -->

10

10

11

17

21

23

25

29

31

This document contains new and updated information as indicated in the following table.

Page

18

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

PanelView Plus 700 to 1500 and PanelView Plus Compact 1000 Terminals and Display Modules

Important User Information

Read this document and the documents listed in the additional resources section about installation, configuration, and operation of this equipment before you install, configure, operate, or maintain this product. Users are required to familiarize themselves with

installation and wiring instructions in addition to requirements of all applicable codes, laws, and standards.

Activities including installation, adjustments, putting into service, use, assembly, disassembly, and maintenance are required to be

If this equipment is used in a manner not specified by the manufacturer, the protection provided by the equipment may be impaired.

In no event will Rockwell Automation, Inc. be responsible or liable for indirect or consequential damages resulting from the use or application of this equipment. The examples and diagrams in this manual are included solely for illustrative purposes. Because of the many variables and requirements associated with any particular installation, Rockwell Automation, Inc. cannot assume responsibility or liability for actual

use based on the examples and diagrams. No patent liability is assumed by Rockwell Automation, Inc. with respect to use of information, circuits, equipment, or software described in this manual.

Reproduction of the contents of this manual, in whole or in part, without written permission of Rockwell Automation, Inc., is prohibited.

Throughout this manual, when necessary, we use notes to make you aware of safety considerations.

WARNING: Identifies information about practices or circumstances that can cause an explosion in a hazardous environment, which may lead to personal injury or death, property damage, or economic loss. Automation,Inc.with

ATTENTION: Identifies information about practices or circumstances that can lead to personal injury or death, l,inwholeorinpart, property damage, or economic loss. Attentions help you identify a hazard, avoid a hazard, and recognize the

consequence. weusenotestomake

IMPORTANT Identifies information that is critical for successful application and understanding of the product.

Labels may also be on or inside the equipment to provide specific precautions.

SHOCK HAZARD: Labels may be on or inside the equipment, for example, a drive or motor, to alert people that dangerous voltage may be present. esinformationabout economicloss.Attent nthatiscriticalforsu

lenttoprovidespecific

BURN HAZARD: Labels may be on or inside the equipment, for example, a drive or motor, to alert people that surfaces may reach dangerous temperatures.

ARC FLASH HAZARD: Labels may be on or inside the equipment, for example, a motor control center, to alert people to potential Arc Flash. Arc Flash will cause severe injury or death. Wear proper Personal Protective Equipment (PPE). Follow ALL Regulatory requirements for safe work practices and for Personal Protective elsmaybeonorinsid aybepresent.

Equipment (PPE).

2 Rockwell Automation Publication 2711P-IN001J-EN-P - April 2018

PanelView Plus 700 to 1500 and PanelView Plus Compact 1000 Terminals and Display Modules

About This Publication

This document provides instructions on how to install these devices in a panel.

· Factory-assembled PanelView™ Plus or PanelView Plus CE 700 to 1500 terminals

· PanelView Plus or PanelView Plus CE 700 to 1500 display modules

For complete information on installing, wiring, and troubleshooting the terminals, refer to the publications listed under Additional Resources

.

Rockwell Automation Publication 2711P-IN001J-EN-P - April 2018

3

<!-- image -->

<!-- image -->

PanelView Plus 700 to 1500 and PanelView Plus Compact 1000 Terminals and Display Modules

Environment and Enclosure

This equipment is intended for use in a Pollution Degree 2 industrial environment, in overvoltage Category II applications (as defined in IEC publication 60664-1), at altitudes up to

2000 m (6561 ft) without derating.

powered must also be connected to the secondary of an isolating transformer.

This equipment is considered Group 1, Class A industrial equipment according to IEC/CISPR

Publication 11. Without appropriate precautions, there may be potential difficulties ensuring electromagnetic compatibility in other environments due to conducted as well as radiated

disturbance. Korean Radio Wave Suitability Registration - This equipment is registered for Electromagnetic

Conformity Registration as business equipment (A), not home equipment. Sellers or users are required to take caution in this regard.

This equipment is supplied as open-type equipment. It must be mounted within an enclosure that is suitably designed for those specific environmental conditions that will be present and appropriately designed to prevent personal injury resulting from accessibility to live parts. The interior of the enclosure must be accessible only by the use of a tool. The terminals meet specified NEMA Type and IEC ratings only when mounted in a panel or enclosure with the

equivalent rating. Subsequent sections of this publication may contain additional information regarding specific enclosure type ratings that are required to comply with certain product safety certifications.

In addition to this publication, see: · Industrial Automation Wiring and Grounding Guidelines, for additional installation requirements, publication 1770-4.1 . · NEMA Standards publication 250 and IEC publication 60529, as applicable, for explanations of the degrees of protection provided by different types of enclosure.

ControlNet Communication Port

- PanelView Plus terminals with ControlNet communications ports include a Network
- Applications Port (NAP). This port is for temporarily connecting programming terminals to devices on a ControlNet network, and are not intended for continuous operation.

Rockwell Automation Publication 2711P-IN001J-EN-P - April 2018

4

<!-- image -->

PanelView Plus 700 to 1500 and PanelView Plus Compact 1000 Terminals and Display Modules

Hazardous Locations

This equipment is suitable for these locations:

· Class I, Division 2 Groups A, B, C, D

· Class II, Division 2 Groups F, G

· Ordinary, nonhazardous locations only

The following statement applies to use in hazardous locations.

Explosion Hazard

· Substitution of components may impair suitability for hazardous locations.

· Do not disconnect equipment unless power has been switched off and area is known to be nonhazardous.

· Do not connect or disconnect components unless power has been switched off.

· All wiring must comply with N.E.C. articles 501, 502, 503, and/or C.E.C. section 18-1J2 as appropriate.

· Peripheral equipment must be suitable for the location in which it is used.

- The terminals have a temperature code of T4 when operating in a 55 °C (131 °F) maximum
- ambient temperature. Do not install the terminals in environments where atmospheric gases have
- ignition temperatures less than 135 °C (275 °F).

Rockwell Automation Publication 2711P-IN001J-EN-P - April 2018

5

PanelView Plus 700 to 1500 and PanelView Plus Compact 1000 Terminals and Display Modules

Environnements dangereux

Cet équipement ne peut être utilisé que dans les environnements suivants:

· Classe I, Division 2, Groupes A, B, C, D

· Classe II, Division 2, Groupes F, G

· ou environnements non-dangereux

La mise en garde suivante s'applique à une utilisation en environnement dangereux.

DANGER D'EXPLOSION

· La substitution de composants peut rendre cet équipement impropre à une utilisation en environnement dangereux.

· Ne pas déconnecter l'équipement sans s'être assuré que l'alimentation est coupée ou que l'environnement est classé non dangereux.

· Ne pas connecter ou déconnecter des composants sans s'être assuré que l'alimentation est coupée.

· L'ensemble du câblage doit être conforme, selon le cas, aux articles 501-4(b), 502-4(b)

et 503-3(b) du Code national de l'électricité des Etats-Unis.

- L'équipement périphérique doit être adapté à l'environnement dans lequel il est utilisé.
- Le code de température de fonctionnement des terminaux PanelView Plus et PanelView Plus CE est T4 pour une température ambiante maximale de 55 °C. N'installez pas les terminaux dans des
- environnements contenant des gaz atmosphériques inflammables à moins de 135 °C.

6

Rockwell Automation Publication 2711P-IN001J-EN-P - April 2018

USB Ports

All PanelView Plus and PanelView Plus Compact terminals contain universal serial bus (USB)

ports that comply with hazardous location environments. This section details the field-wiring compliance requirements and is provided in accordance with the National Electrical Code,

article 500.

Associated Nonincendive Field Wiring Apparatus

PanelView Plus Host Product

PanelView Plus 700 to 1500 and PanelView Plus Compact 1000 Terminals and Display Modules

Nonincendive Field Wiring

USB Port

Table 1 - PanelView Plus USB Port Circuit Parameters

<!-- image -->

L

a

Groups A and B Groups C and D Groups A and B Groups C and D

15 μH

15 μH

Selected nonincendive field wiring apparatus must have nonincendive circuit parameters conforming with Table 2.

Table 2 - Required Circuit Parameters for the USB Peripheral Device

| ≥  V oc   | ≥  V oc   |
|-----------|-----------|
|           | ≥  I sc   |
|           | ≤  C a    |

Rockwell Automation Publication 2711P-IN001J-EN-P - April 2018

Nonincendive Field

Wiring Apparatus

USB

Peripheral

7

PanelView Plus 700 to 1500 and PanelView Plus Compact 1000 Terminals and Display Modules

Application Information

Per the National Electrical Code the circuit parameters of nonincendive field wiring apparatus for use in hazardous locations shall be coordinated with the associated nonincendive field wiring

apparatus such that their combination remains nonincendive. The PanelView Plus terminals and

The circuit parameters of the PanelView Plus USB port are given in Table 1. The USB peripheral device and its associated cabling shall have circuit parameters with the limits given in Table 2 for

them to remain nonincendive when used with the PanelView Plus USB port. If cable capacitance and inductance are not known the following values from ANSI/ISA-RP 12.06.01-2003 may be

used: Ccable = 197 μF/m (60 μF/ft) L cable = 0.7 μF/m (0.20 μH/ft)

Nonincendive field wiring must be wired and separated in accordance with 501.10(B)(3) of the National Electrical Code (NEC) ANSI/NFPA 70 or other local codes as applicable. This associated nonincendive field wiring apparatus has not been evaluated for use in combination with another associated nonincendive field wiring apparatus. Symbol Definitions

<!-- formula-not-decoded -->

Open circuit voltage of the host USB port.

I sc Maximum output current of the host USB port. V max Maximum applied voltage rating of the USB peripheral device. V shall be greater than or equal to V in Table 1 (V ≥ V

max oc max I max Maximum current to which the USB peripheral device can be subjected. I max shall be greater than or equal to I sc in Table 1 (I max ≥ I sc ).

C

i

Maximum internal capacitance of the USB peripheral device.

Maximum allowed capacitance of the USB peripheral device and its associated cable. The sum of Ci of the

USB peripheral device and Ccable of the associated cable shall be less than or equal to C

a

Maximum allowed inductance of the USB peripheral device and its associated cable. The sum of Li of the

USB peripheral device and Lcable of the associated cable shall be less than or equal to L

a

Use publication NFPA 70E, Electrical Safety Requirements for Employee Workplaces, IEC

60364 Electrical Installations in Buildings, or other applicable wiring safety requirements for the country of installation when wiring the devices. In addition to the NFPA guidelines:

· Connect the device and other similar electronic equipment to its own branch circuit.

| C a (C i + C cable  ≤ C a ).                                   |
|----------------------------------------------------------------|
| L i  Maximum internal inductance of the USB peripheral device. |
| L a (L i + L cable  ≤ L a ).                                   |
| Wiring and Safety Guidelines                                   |

· Protect the input power by a fuse or circuit breaker rated at no more than 15 A.

Rockwell Automation Publication 2711P-IN001J-EN-P - April 2018

## 8

oc ).

PanelView Plus 700 to 1500 and PanelView Plus Compact 1000 Terminals and Display Modules

· Route incoming power to the device by a separate path from the communication lines.

· Cross power and communication lines at right angles if they must cross.

· Communication lines can be installed in the same conduit as low-level

DC I/O lines (less than 10V).

· Shield and ground cables appropriately to avoid electromagnetic interference (EMI).

- For more information on grounding recommendations, refer to the National Electrical Code published by the National Fire Protection Association.

For more information, refer to Wiring and Grounding Guidelines for PanelView Plus Terminals

- Technical Data, publication 2711P-TD001. You can find this publication in the Literature Library website, http://literature.rockwellautomation.com .

About the PanelView Plus 700 to 1500 Terminals

The PanelView Plus terminals have these modular components: · Display module (700, 1000, 1250, and 1500) · Logic module with AC or DC power, CompactFlash card slot, Ethernet port, serial port, and USB ports

· Internal CompactFlash card with firmware or operating system, RAM memory (SO-

## DIMM)

· Communication module for specific communication protocols

These items can be ordered as separate components for field installation or factory assembled per

- your configuration. The base-configured unit includes the display module and the logic module
- with internal CompactFlash and RAM. Modular Components
- Communication Module
- Logic Module

Display Module red unit includes the display module and the logic module MI.

Serial Port USB Ports

If the modules are ordered separately, attach the logic and communication module to the display module before panel installation. See the instructions shipped with each module.

The logic module for the terminals is available with or without RAM and CompactFlash preinstalled. If memory is ordered separately, you must install the memory before attaching the

logic module to the display module. See the instructions shipped with the logic module.

Rockwell Automation Publication 2711P-IN001J-EN-P - April 2018

<!-- image -->

Power Input, AC or DC

Ethernet Port

9

PanelView Plus 700 to 1500 and PanelView Plus Compact 1000 Terminals and Display Modules

About the PanelView Plus Compact 1000 Terminal

The PanelView Plus Compact 1000 terminal has a fixed configuration. It does not support communication modules, or the replacement of the logic module. The 1000 terminal contains a

non-isolated DC power supply.

## ct1000Terminal

USB Ports RS-232 Serial Port terminal has a fixed configuration. It does not support acement of the logic module. The 10o0 terminal contains a

<!-- image -->

· CompactFlash Type 1 card slot

- Parts List

These items are shipped with the terminals:

· Power terminal block

- Mounting clips

· FactoryTalk View® software preloaded

· Installation instructions and panel cutout template

Required Tools

These tools are required for panel installation:

· Panel cutout tools

- Small, slotted screwdriver
- Torque wrench (lb·in)

Rockwell Automation Publication 2711P-IN001J-EN-P - April 2018

10

Power Input, 24V DC

Ethernet Port

PanelView Plus 700 to 1500 and PanelView Plus Compact 1000 Terminals and Display Modules

Install the Terminal

Before installing the terminal in a panel, review the following topics:

· Mounting clearances

· Panel cutout dimensions

Mounting Clearances

Allow adequate clearance around the terminal, inside the enclosure, for adequate ventilation.

Consider heat produced by other devices in the enclosure. The ambient temperature around the terminals must be between 0…55 °C (32…131 °F).

These minimum clearances are required for ventilation.

· Top clearance: 51 mm (2 in.)

· Bottom clearance: 102 mm (4 in.)

· Side clearances: 25 mm (1 in.)

· Back clearance: 25 mm (1 in.) Minimum side clearance for insertion of memory card is 102 mm (4 in.).

Panel Cutout Dimensions

Use the full size template shipped with your terminal to mark the cutout dimensions.

- Terminal Type

700 Keypad or Keypad and Touch

700 Touch

1000 Keypad or Keypad and Touch

1000 Touch

1250 Keypad or Keypad and Touch

Height, mm (in.) Width, mm (in.)

167 (6.57) 264 (10.39)

154 (6.08) 220 (8.67)

224 (8.8)

224 (8.8)

375 (14.75)

305 (12.00)

257 (10.11) 390 (15.35)

257 (10.11) 338 (13.29)

305 (12.00) 419 (16.50)

305 (12.00) 391 (15.40)

| 1500 Keypad or Keypad and Touch   |
|-----------------------------------|

Rockwell Automation Publication 2711P-IN001J-EN-P - April 2018

11

<!-- image -->

PanelView Plus 700 to 1500 and PanelView Plus Compact 1000 Terminals and Display Modules

Mount the Terminal in a Panel

Mounting clips secure the terminal to the panel. The number of clips you use

(4, 6, or 8) varies by terminal type.

Disconnect all electrical power from the panel before making the panel cutout.

Take precautions so metal cuttings do not enter any components already installed in the panel.

Failure to follow these instructions may result in personal injury or damage to panel components.

Follow these steps to mount the terminal in a panel. 1. Cut an opening in the panel by using the panel cutout shipped with the terminal.

2. Make sure the terminal sealing gasket is properly positioned on the terminal.

This gasket forms a compression type seal. Do not use sealing compounds.

hal in a panel.

- using the panel cutout shipped with the terminal.
- gasket is properly positioned on the terminal. on type seal. Do not use sealing compounds.

3. Install the legend strips before installing the terminal if you are using keypad legend

Be careful not to pinch the legend strip during installation.

<!-- image -->

12

Rockwell Automation Publication 2711P-IN001J-EN-P - April 2018

Sealing Gasket

<!-- image -->

PanelView Plus 700 to 1500 and PanelView Plus Compact 1000 Terminals and Display Modules

5. Slide the ends of the mounting clips into the slots on the terminal.

Mounting Clip

Mounting Clip Slot

- clips into the slots on the terminal.

6. Tighten the mounting clip screws by hand until the gasket seal contacts the mounting

<!-- image -->

- ews by hand until the gasket seal contacts the mounti

7. Tighten the mounting clip screws to a torque of 0.90…1.1 N·m

(8…10 lb·in) by using the specified torque sequence, making sure not to overtighten.

1 3 5

6 Clips

4 6 2

1

6

8 Clips

5 2

Tighten the mounting clips to the specified torque to provide a proper seal and prevent damage to the product. Rockwell Automation assumes no responsibility

for water or chemical damage to the product or other equipment within the enclosure because of improper installation.

<!-- image -->

Rockwell Automation Publication 2711P-IN001J-EN-P - April 2018

<!-- image -->

1

5

6Clips

3

7

8

4

13

PanelView Plus 700 to 1500 and PanelView Plus Compact 1000 Terminals and Display Modules

Product Dimensions

The table provides product dimensions for the terminals including depth dimensions for the:

· base configured unit (display module and logic module).

· base configured unit with communication module.

Height, Approx., mm (in.)

Width,

Approx., mm (in.)

700 Keypad or Keypad and Touch 193 (7.58) 290 (11.40)

700 Touch Screen 179 (7.04) 246 (9.68)

- 1000 Keypad or Keypad and Touch 248 (9.77) 399 (15.72)

1000 Touch Screen 248 (9.77) 329 (12.97)

| 1250 Keypad or Keypad and Touch 282 (11.12) 416 (16.36) 1250 Touch Screen 282 (11.12) 363 (14.30)   |
|-----------------------------------------------------------------------------------------------------|
| 1500 Keypad or Keypad and Touch 330 (12.97) 469 (18.46) 65 (2.55)                                   |
| 1500 Touch Screen 330 (12.97) 416 (16.36)                                                           |

Depth, Approx., mm (in.)

55 (2.18)

display to logic module

83 (3.27)

display to comm module display to logic module

93 (3.65)

display to comm module

The illustration shows product dimensions for the PanelView Plus and PanelView Plus Compact

1000 touch only terminals. The other size terminals look similar. Measurements are in mm (in.).

14

Rockwell Automation Publication 2711P-IN001J-EN-P - April 2018

Terminal Type

PanelView Plus 700 to 1500 and PanelView Plus Compact 1000 Terminals and Display Modules

1000 Terminal Dimensions

<!-- image -->

a 55 (2.18) Display to Logic Module b 83 (3.27) Display to Comm Module

248 (9.77)

248 (9.77)

Rockwell Automation Publication 2711P-IN001J-EN-P - April 2018

15

<!-- image -->

<!-- image -->

PanelView Plus 700 to 1500 and PanelView Plus Compact 1000 Terminals and Display Modules

Ethernet Wiring

Use Belden 7921A shielded Ethernet Category 5e cable according to TIA 568-B.1 and RJ45

connector according to IEC 60603-7 for compliance with Marine emissions limits and European

Union 89/336/EEC EMC Directive.

Remove and Install the Power Terminal Block The terminals are shipped with a power terminal block installed. You can remove the terminal block for ease of installation, wiring, and maintenance. Explosion Hazard

Substitution of components may impair suitability for hazardous locations.

Do not disconnect equipment unless power has been switched off and area is known to be

## nonhazardous.

Do not connect or disconnect components unless power has been switched off. All wiring must comply with N.E.C. articles 501, 502, 503, and/or C.E.C. section 18-1J2 as appropriate.

Peripheral equipment must be suitable for the location in which it is used.

Disconnect all power before installing or replacing components. Failure to disconnect power may result in electrical shock or damage to the terminal.

· Series A to D, DC logic modules use a 3-position terminal block.

· Series E or later, DC logic modules use a 2-position terminal block.

· All logic modules with an AC power input use a 3-position terminal block.

Rockwell Automation Publication 2711P-IN001J-EN-P - April 2018

16

PanelView Plus 700 to 1500 and PanelView Plus Compact 1000 Terminals and Display Modules

Follow these steps to remove the terminal block.

1. Loosen the two screws that secure the terminal block.

2. Gently pull the terminal block away from the connector.

- 2-position DC Terminal Block (series E or later)

3-position AC or DC

Terminal Block

2. Tighten the two screws that secure the terminal block to the connector.

<!-- image -->

DC-powered PanelView Plus devices have an integrated 24V DC power supply. Both isolated

- and non-isolated power supplies have these ratings:
- 24V DC nominal (18…32V DC)

· 70 W maximum (2.9 A at 24V DC)

The power supply is internally protected against reverse polarity of the DC+ and DC- connections. Connecting DC+ or DC- to the earth/ground terminal may damage the device.

The input power terminal block supports these wire sizes. Wire Specifications for DC Input Power Terminal Block

Logic Module Wire Type

Dual-wire

Gauge

(1)

Single-wire

Gauge

Series A to D Stranded or solid Cu 90 °C (194 °F) 22…16 AWG 22…14 AWG Series E and later

(1) Two-wire max per terminal.

Rockwell Automation Publication 2711P-IN001J-EN-P - April 2018

Terminal Screw

Torque

0.23…0.34 N·m

(2…3 lb·in)

0.56 N·m (5 lb·in)

17

<!-- image -->

<!-- image -->

PanelView Plus 700 to 1500 and PanelView Plus Compact 1000 Terminals and Display Modules

External Power Supply For Non-isolated DC Terminals

TIP

To identify non-isolated DC logic modules refer to the PanelView Plus Terminals User Manual, publication 2711P-UM001

.

Use a single, 24V DC power supply to power each PanelView Plus device, such as catalog terminal prevents ground loop currents from damaging the terminals.

## The output on the power supply must be isolated from the input and not connected to earth/

ground. Use a safety extra-low voltage (SELV) or protective extra-low voltage (PELV) power supply as required by local wiring codes for your installation. The SELV or PELV power sources provide

protection so that under normal and single-fault conditions, the voltage between the conductors, and between the conductors and functional earth or protective earth does not exceed a safe value.

Multiple AC Power Supplies to Power Multiple DC Terminals dc+ AC/DC Power Supply L1L2 dcdc+ dcL1L2 (2711P-RSACDIN) (2711P-RSACDIN) AC/DC Power Supply

Circuitry

<!-- image -->

Circuitry

PanelView Plus

Isolated DC logic modules are identified by catalog number 2711P-RPxDx

.

Use an SELV or PELV 24V DC power supply, such as catalog number 2711P-RSACDIN, to power the isolated DC PanelView Plus terminal.

The isolated DC terminals may be powered by the same power source as other equipment.

Use a safety extra-low voltage (SELV) or protective extra-low voltage (PELV) power supply as required by local wiring codes for your installation. The SELV or PELV power sources provide

protection so that under normal and single-fault conditions, the voltage between the conductors, and between the conductors and functional earth or protective earth does not

exceed a safe value.

18 Rockwell Automation Publication 2711P-IN001J-EN-P - April 2018

<!-- image -->

PanelView Plus 700 to 1500 and PanelView Plus Compact 1000 Terminals and Display Modules

Earth/Ground Connection

PanelView Plus devices with a DC power input have a earth/ground terminal that you must connect to a low-impedance earth/ground. The earth/ground connection is on the rear of the

display module.

immunity, reliability, and Electromagnetic Compliance (EMC) with the European Union (EU)

EMC directive for CE-mark conformance. This connection is required for safety by Underwriters

Laboratory.

The earth/ground terminal requires a minimum wire gauge. Earth/Ground Wire Specifications for DC Power

On most PanelView Plus devices, the earth/ground terminal is internally connected to the DCterminal within the product. Symbol Wire Type Wire Gauge Terminal Screw Torque GND Stranded or solid Cu 90 °C (194 °F) 14…10 AWG 1.13…1.36 N·m (10…12 lb·in)

Damage or malfunction can occur when a voltage potential exists between two separate ground points. Make sure the terminal does not serve as a conductive path between ground

The PanelView Plus devices have isolated and non-isolated communication ports.

| points at different potentials.   |
|-----------------------------------|

For more information refer to the PanelView Plus Terminals User Manual, publication 2711PUM001 .

Rockwell Automation Publication 2711P-IN001J-EN-P - April 2018

19

<!-- image -->

PanelView Plus 700 to 1500 and PanelView Plus Compact 1000 Terminals and Display Modules

Connect DC Power

Explosion Hazard - Do not disconnect equipment unless power has been switched off and area is known to be nonhazardous.

Disconnect all power before installing or replacing components. Failure to disconnect power

Follow these steps to connect the terminal DC power.

1. Verify that the terminal is not connected to a power source. 2. Secure the DC power wires to the terminal block.

Follow the markings on the terminal blocks and the terminal for proper connections. 3. Secure the earth/ground wire to the earth/ground terminal screw at the bottom of the display.

DC Power Supply Connections

<!-- image -->

20

GND

Rockwell Automation Publication 2711P-IN001J-EN-P - April 2018

3-position Terminal Block

(series A to D logic modules)

–

+

DC-

DC+

2-position Terminal Block

(series E or later logic modules)

–

+

DC - DC+

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

- IMPORTANT

PanelView Plus 700 to 1500 and PanelView Plus Compact 1000 Terminals and Display Modules

AC Power Connections

PanelView Plus devices with an integrated AC power supply have these power ratings:

· 85…264V AC (47…63 Hz)

· 160V A max

Wire Specifications for AC Input Power Terminal Block

Wire Type

Dual-wire

Gauge (1)

Single-wire

Gauge

Terminal Screw Torque

Stranded or solid Cu 90 °C (194 °F) 22…16 AWG 22…14 AWG 0.56 N·m (5 lb·in)

(1) Two-wire max. per terminal.

## Protective Earth and Functional Earth Connection

PanelView Plus devices with an AC power input have both a protective earth and functional

· Functional earth connection is on the back of the display.

| earth terminal that you must connect to a low-impedance earth ground.   |
|-------------------------------------------------------------------------|
| • Protective earth terminal is on the power input terminal block.       |

The functional earth and protective earth connections to ground are mandatory. The functional earth ground connection is required for electromagnetic compliance (EMC) with

the EU (European Union) EMC directive for CE-mark conformance. The protective earth ground connection is required for safety and regulatory compliance.

On PanelView Plus devices with an AC power input, you must connect both protective earth and functional earth to ground.

The protective earth and functional earth terminals require a minimum wire gauge. Functional Earth and Protective Earth Wire Specifications for AC Power

Connection

Wire Type

Wire Gauge

Terminal Screw

Torque

1.13… 1.36 N·m

(10…12 lb·in)

Protective earth Stranded or solid Cu 90 °C (194 °F) 14…12 AWG 0.56 N·m (5 lb·in) Functional earth GND Stranded or solid Cu 90 °C (194 °F) 14…10 AWG

Rockwell Automation Publication 2711P-IN001J-EN-P - April 2018

21

<!-- image -->

<!-- image -->

PanelView Plus 700 to 1500 and PanelView Plus Compact 1000 Terminals and Display Modules

Connect AC Power

Explosion Hazard - Do not connect or disconnect equipment while circuit is live unless area is known to be nonhazardous.

Disconnect all power before installing or replacing components. Failure to disconnect power

Improper wiring of power terminals may result in voltage at the communication connector shells. Refer to the following figure when wiring.

Do not apply power to the terminal until all wiring connections have been made. Failure to do so may result in electrical shock.

Follow these steps to connect the terminal to AC power.

1. Verify that the terminal is not connected to a power source. 2. Secure the AC power wires to the terminal block.

Follow the markings on terminal blocks and terminal for proper connections. 3. Secure the protective earth ground wire to the marked position of the power input terminal block.

4. Secure the functional earth ground wire to the functional earth ground screw on the

- back of the display to ground bus.

GND

<!-- image -->

22

Rockwell Automation Publication 2711P-IN001J-EN-P - April 2018

L1

L2/Neutral

Protective Earth to Ground Bus

<!-- image -->

PanelView Plus 700 to 1500 and PanelView Plus Compact 1000 Terminals and Display Modules

Battery Precautions

When you connect or disconnect the battery an electrical arc can occur. This could cause an explosion in hazardous location installations. Be sure that power is removed and the area is

nonhazardous before proceeding.

leaking batteries, see Guidelines for Handling Lithium Batteries, publication AG 5-4. Replace the battery only with the indicated catalog number.

Do not dispose of battery in a fire or incinerator. Dispose of used batteries in accordance with local regulations. Store batteries in a cool, dry environment. We recommend 25 °C (77 °F) with 40…60% relative humidity. You may store batteries for up to 30 days between -45…85 °C (-49…185 °F), such as

during transportation. To avoid possible leakage, do not store batteries above 60 °C (140 °F) for more than 30 days.

Replace the Battery

Follow these steps to replace the lithium battery in the logic module of PanelView Plus or PanelView Plus Compact terminals. 1. Disconnect power from the terminal.

2. Place the terminal, display side down, on a flat stable surface.

3. Detach the communication module, if attached, from the logic module by removing the four screws.

4. Loosen the six captive screws that attach the logic module to the display module.

Communication Module

Screw

- on a flat stable surface.
- Logic Module
- ch the logic module to the display module.

5. Carefully lift the logic module away from the terminal and turn over to expose the circuit

Rockwell Automation Publication 2711P-IN001J-EN-P - April 2018

23

<!-- image -->

Captive

Screw

PanelView Plus 700 to 1500 and PanelView Plus Compact 1000 Terminals and Display Modules

6. Locate the battery on the circuit board.

Use only replacement battery catalog number 2711P-RY2032.

9. Reattach the logic module by aligning the two connectors on the bottom of the module

<!-- image -->

- ideofthebattery. lifting up thc

battery catalog number 2711P-RY2032. onlyreplaceme

- the two connectors on the bottom of the module lule by alignin the eterminal

11. Tighten the six captive screws that secure the logic module to a torque of 0.58 N·m

<!-- image -->

24

Rockwell Automation Publication 2711P-IN001J-EN-P - April 2018

<!-- image -->

.

Troubleshooting

If the terminal is not operating correctly, check the power, display settings, status indicators, and review the system startup and error messages.

Check for Adequate Power

A terminal that does not receive adequate power could cause unpredictable behavior. Verify the power requirements in the Specifications table.

Check Status Indicators

The terminal has two status indicators to isolate operating problems.

· COMM indicator (green) for communication

· FAULT indicator (red) for hardware faults

COMM and FAULT Indicators operating problems.

- ication
- ults

When the terminal starts, the fault indicator should be off, except for a few brief flashes, and the comm indicator on. If the indicators remain off, the power supply or logic module has failed.

Check the power cable. If the power is not within range, replace the power supply. If the power is within range, replace the logic module. After a successful startup, both indicators are off and

<!-- image -->

Rockwell Automation Publication 2711P-IN001J-EN-P - April 2018

25

PanelView Plus 700 to 1500 and PanelView Plus Compact 1000 Terminals and Display Modules

12. Reattach the communication module, if necessary, and tighten the four screws to a torque of 0.58 N·m (5…7 lb·in)

This product contains a hermetically sealed lithium battery which may need to be replaced during the life of the product.

any unsorted municipal waste.

The collection and recyling of batteries helps protect the environment and contributes to the

- conservation of natural resources as valuable materials are recovered.

PanelView Plus 700 to 1500 and PanelView Plus Compact 1000 Terminals and Display Modules

The table shows indicator states if the terminal powers on and stops during startup.

Indicator States If the Terminal Stops During Startup

Fault (Red)

Indicator

(1)

Comm (Green)

Indicator

Description

Last firmware download failed.

Reload firmware using Firmware Upgrade Wizard (FUW) utility.

EBC boot loader firmware failed or is missing.

Blinking Blinking Reload firmware using Firmware Upgrade Wizard (FUW) utility.

## On

Windows CE OS firmware failed or is missing.

Reload firmware using Firmware Upgrade Wizard (FUW) utility.

· Check the brightness setting of the display. From Configuration mode on the terminal,

| On(2) Replace the logic module. Blinking  Fatal hardware error in display. Replace the display module.   |
|----------------------------------------------------------------------------------------------------------|
| (1) Blinking red indicates a recoverable error. (2) Solid red indicates a nonrecoverable or fatal error. |
| Check the Display                                                                                        |
| If the terminal display is dim or unreadable:                                                            |
| access Terminal Settings>Display Intensity.                                                              |

· Check the Screen Saver settings. The backlight may be turning off or dimming the display unexpectedly. From Configuration mode on the terminal, access Terminal

Settings&gt;Display&gt;Screen Saver.

Rockwell Automation Publication 2711P-IN001J-EN-P - April 2018

26

PanelView Plus 700 to 1500 and PanelView Plus Compact 1000 Terminals and Display Modules

Startup Information Messages

Startup information messages display in a specific sequence on the terminal during startup and typically display for a few seconds. These messages do not require that you perform any action.

Message # Message

Description

30 Watchdog Test Tests the watchdog circuitry to verify system integrity.

## 1

RAM Test

Tests the RAM memory.

31 Stuck Key Checks the integrity of the function key hardware. 31.5 Stuck Touch Checks the integrity of the touch screen hardware.

Locates and loads the most recent, valid registry. Multiple copies of the registry are maintained. If power is lost during a registry update, a valid registry is available

Checks for a new OS firmware upgrade on the external CompactFlash card and the

Transfers a new OS firmware upgrade from the external CompactFlash card to the terminal. Message may display for several minutes.

Programs the OS firmware just downloaded into the internal flash memory.

29 System Check ### Internal file system integrity check (### is percent progress indicator).

29.1 System Check Internal file system integrity check disabled. Contact technical support.

| 32 Battery Test  Checks the integrity of the battery hardware.                                  |
|-------------------------------------------------------------------------------------------------|
| 2.5 Registry Search the next time power is applied to the terminal.                             |
| 2 Image Search                                                                                  |
| serial port.                                                                                    |
| 50 External CF                                                                                  |
| 23 Internal CF                                                                                  |
| Message may display for several minutes. 24 CRC Check  Checks the integrity of the OS firmware. |
| 28 Starting System Launches the operating system (OS).                                          |

Rockwell Automation Publication 2711P-IN001J-EN-P - April 2018

27

PanelView Plus 700 to 1500 and PanelView Plus Compact 1000 Terminals and Display Modules

Startup Error Messages

When an error occurs, the terminal displays an error number with a text message. The word

ERROR! appears under the message in different languages.

# Displayed Message

Error # Message Description

1 RAM Test RAM test failure.

Error programming the new OS firmware to

internal CompactFlash card.

Checksum of the OS

Recommended Corrective Action

Reset the terminal. If error persists, reseat the SO-DIMM RAM

module. If error still persists, replace the logic module.

Reload the firmware. If error persists, replace the internal

CompactFlash card. If error still persists, replace the logic module.

Reload the firmware. If error persists, replace the internal

CompactFlash card. If error still persists, replace the logic

30 Watchdog Test Watchdog test failure. Reload the firmware. If error persists, replace the logic module.

Check that nothing is pressed against a key. Reset the terminal without key presses. If error persists, replace the display

Check that nothing is pressed against the touch screen. Reset the terminal without pressing the touch screen. If error persists,

replace the display module.

32 Battery Test Battery failure. Replace the battery. If error persists, replace the logic module.

Upgrade the system firmware to revision 3.10.03 or later.

Reload the firmware. If error persists, replace the internal

CompactFlash card. If error still persists, replace the logic

Reload the firmware. If error persists, replace the external

CompactFlash card and attempt the firmware upgrade again.

| 24 CRC Check  firmware failed. module.                                            |
|-----------------------------------------------------------------------------------|
| 31 Stuck Key Function key failure. module.                                        |
| 31.5 Stuck Touch Touch screen failure.                                            |
| 33.5 NVRAM Access  Nonvolatile memory                                             |
| failure.  40 EXE Check  System OS firmware is                                     |
| missing or corrupt. module. 50 External CF Error loading the OS firmware from the |
| external CompactFlash card.                                                       |

28

Rockwell Automation Publication 2711P-IN001J-EN-P - April 2018

23 Internal CF

Specifications

PanelView Plus Terminals - 2711P-Kxxxx, 2711P-Txxxx, 2711P-Bxxxx, 2711P-RDxxxx, 2711PC-

Txxxx

Attribute

Display type

Display size

700

Value

Color active matrix, thin film transistor (TFT), liquid crystal display

(LCD)

6.5 in.

## 1000 1250 10.4 in. 12.1 in.

1500

15 in.

70 W max (2.9 A @ 24V DC) 39 W typical (1.6 A @ 24V DC)

248 x 399 x 55 mm (9.77 x 15.72 x 2.18 in.)

248 x 329 x 55 mm (9.77 x 12.97 x 2.18 in.)

282 x 416 x 55 mm (11.12 x 16.36 x 2.18 in.)

282 x 363 x 55 mm (11.12 x 14.30 x 2.18 in.)

330 x 469 x 65 mm (12.97 x 18.46 x 2.55 in.)

330 x 416 x 65 mm ((12.97 x 16.37 x 2.55 in.)

|                                  | Display area (WxH)                                                                                               |
|----------------------------------|------------------------------------------------------------------------------------------------------------------|
|                                  | 132 x 99 mm (5.2 x 3.9 in.) 211 x 158 mm (8.3 x 6.2 in.)                                                         |
|                                  | 1250 1500 246 x 184 mm (9.7 in x 7.2 in.) 304 x 228 mm (12.0 x 9.0 in.)                                          |
|                                  | Display resolution                                                                                               |
|                                  | Power consumption, DC  Input voltage, AC  85… 264V AC (47…63 Hz) Power consumption, AC  160VA max (65VA typical) |
|                                  | PCI slot max. available power (1)                                                                                |
|                                  | Dimensions, Approx, (HxWxD) for based configured unit without communication module                               |
|                                  | 700 keypad, or keypad and touch 193 x 290 x 55 mm (7.58 x 11.40 x 2.18 in.)                                      |
|                                  | 700 touch 179 x 246 x 55 mm (7.04 x 9.68 x 2.18 in.)                                                             |
|                                  | 1000 keypad, or keypad and touch                                                                                 |
|                                  | 1250 keypad, or keypad and touch                                                                                 |
| 1500 keypad, or keypad and touch | 1500 keypad, or keypad and touch                                                                                 |
|                                  | (1) The PCI slot does not apply to the PanelView Plus Compact 1000 terminal.                                     |
|                                  | Rockwell Automation Publication 2711P-IN001J-EN-P - April 2018                                                   |

PanelView Plus 700 to 1500 and PanelView Plus Compact 1000 Terminals and Display Modules

29

PanelView Plus 700 to 1500 and PanelView Plus Compact 1000 Terminals and Display Modules

PanelView Plus Terminals - 2711P-Kxxxx, 2711P-Txxxx, 2711P-Bxxxx, 2711P-RDxxxx, 2711PC-

Txxxx

Weight, Approx for base configured unit without communication module

700 keypad, or keypad and touch

1000 keypad, or keypad and touch

1000 touch

1.9 kg (4.2 lb)

1.7 kg (3.8 lb)

2.9 kg (6.3 lb)

2.6 kg (5.7 lb)

## 1250 keypad, or keypad and touch 3.4 kg (7.6 lb)

1250 touch

3.2 kg (7.1 lb)

Battery-backed, + /- 2 minutes per month

| 1500 keypad, or keypad and touch  4.6 kg (10.0 lb)   | 1500 keypad, or keypad and touch  4.6 kg (10.0 lb)               |
|------------------------------------------------------|------------------------------------------------------------------|
|                                                      | Status indicators                                                |
|                                                      | Application flash memory                                         |
|                                                      | 700 to 1500 series D or earlier logic modules 2711P-RW1          |
|                                                      | 2711P-RW2                                                        |
|                                                      | 2711P-RW3 700 to 1500 series E or later logic modules 95 MB      |
|                                                      | 2711P-RW6                                                        |
|                                                      | 2711P-RW7 2711P-RW8                                              |
|                                                      | External CompactFlash storage                                    |
| Environmental Specifications Vibration               | Specification  Temperature, operating  Temperature, nonoperating |

Shock, operating

Shock, nonoperating

15 g at 11 ms

30 g at 11 ms

| Relative humidity  5…95% without condensation                                        |
|--------------------------------------------------------------------------------------|
| Enclosure ratings  NEMA Type 12, 13, 4X (indoor use only), IP54, IP65                |
| Airborne Contaminants  ANSI/ISA S71.04-1985 Severity Level G3 EN60654-4:1998 Class 3 |
| 30  Rockwell Automation Publication 2711P-IN001J-EN-P - April 2018                   |

Certifications

Certification (1)

c-UL-us

CE (EMC)

PanelView Plus 700 to 1500 and PanelView Plus Compact 1000 Terminals and Display Modules

UL Listed Industrial Control Equipment, certified for use in US and Canada. See File

E10314.

UL Listed Industrial Control Equipment for use in:

· Class III Hazardous Locations

European Union 89/336/EEC EMC Directive, compliant with:

EN 61000-6-2; Industrial Immunity

EN 61000-6-4; Industrial Emissions

Products identified with the suffix M in the catalog number, are certified to the

(1) See the Product Certification link on http://www.ab.com for declarations of conformity, certificates, and other certification details.

| CE (LVD) EN 61131-2; Programmable Controllers                                                                                                           |
|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| C-Tick  Australian Radiocommunications Act, compliant with: AS/NZS CISPR 11; Industrial Emissions Marine  requirements of one or more marine societies. |
| Additional Resources                                                                                                                                    |
| For additional information on the terminals, refer to these publications.                                                                               |
| Resource  Description                                                                                                                                   |

UM001

Wiring and Grounding Applications for

PanelView Plus devices Technical Data, publication 2711P-TD001

PanelView Plus Compact Terminals User Manual, terminals and gives information on how to install, operate, configure,

and troubleshoot these devices.

Provides additional information on how to wire and ground the

PanelView Plus and PanelView Plus CE terminals.

Provides an overview of the PanelView Plus Compact terminals and gives information on how to install, operate, configure, and

You can view or download publications and translated versions of the installation instructions at

To order paper copies of technical documentation, contact your local Rockwell Automation

| publication 2711PC-UM001 troubleshoot these devices.   |
|--------------------------------------------------------|
| http://literature.rockwellautomation.com .             |
| distributor or sales representative.                   |

Rockwell Automation Publication 2711P-IN001J-EN-P - April 2018

31

Rockwell Automation Support

For technical support, visit http://www.rockwellautomation.com/support/overview.page

Rockwell Automation maintains current product environmental information on its website at http://www.rockwellautomation.com/rockwellautomation/about-us/sustainability-ethics/product-environmental-compliance.page

Allen-Bradley, FactoryTalk View, PanelView, PanelView Plus, Rockwell Automation, and Rockwell Software are trademarks of Rockwell Automation, Inc.

Trademarks not belonging to Rockwell Automation are property of their respective companies.

Rockwell Otomasyon Ticaret A.Ş., Kar Plaza İş Merkezi E Blok Kat:6 34752 İçerenköy, İstanbul, Tel: +90 (216) 5698400

Publication 2711P-IN001J-EN-P - April 2018 Supersedes Publication 2711P-IN001I-EN-P - November 2009

Copyright © 2018 Rockwell Automation, Inc. All rights reserved. Printed in the U.S.A.

.

.