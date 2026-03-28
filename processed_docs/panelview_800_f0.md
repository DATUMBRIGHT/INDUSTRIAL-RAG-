## Installation Instructions

Original Instructions

## PanelView 800 HMI Terminals

Catalog Numbers 2711R-T4T, 2711R-T7T, 2711R-T10T

| Topic Page                                   |
|----------------------------------------------|
| Summary of Changes 1                         |
| About This Publication 1                     |
| Environment and Enclosure 2                  |
| Preventing Electrostatic Discharge 2         |
| North American Hazardous Location Approval 3 |
| Catalog Number Explanation 4                 |
| About the Terminals 4                        |
| Parts List 6                                 |
| Install the Terminal 7                       |
| Product Dimensions 10                        |
| Choose a Power Supply 12                     |
| Connect Devices 15                           |
| Troubleshooting 16                           |
| Battery Replacement 16                       |
| Specifications 18                            |
| Additional Resources 20                      |

## Summary of Changes

This publication contains the following new or updated information. This list includes substantive updates only and is not intended to reflect all changes. Translated versions are not always available for each revision.

| Topic Page                     |
|--------------------------------|
| Updated Ground the Terminal 15 |

## About This Publication

This document provides instructions on how to install, wire, ground, and troubleshoot PanelView™ 800 terminals. It does not provide information on how to configure or run applications on the following devices: 2711R-T4T, 2711R-T7T, and 2711R-T10T.

<!-- image -->

<!-- image -->

## Environment and Enclosure

<!-- image -->

ATTENTION: This equipment is intended for use in a Pollution Degree 2 industrial environment, in overvoltage Category II applications (as defined in EN/IEC 60664-1), at altitudes up to 2000 m (6562 ft) without derating.

This equipment is not intended for use in residential environments and may not provide adequate protection to radio communication services in such environments.

This equipment is supplied as open-type equipment for indoor use. It must be mounted within an enclosure that is suitably designed for those specific environmental conditions that will be present and appropriately designed to prevent personal injury resulting from accessibility to live parts. The enclosure must have suitable flame-retardant properties to prevent or minimize the spread of flame, complying with a flame spread rating of 5VA or be approved for the application if nonmetallic. The interior of the enclosure must be accessible only by the use of a tool. Subsequent sections of this publication may contain more information regarding specific enclosure type ratings that are required to comply with certain product safety certifications.

In addition to this publication, see:

- Industrial Automation Wiring and Grounding Guidelines, publication 1770-4.1, for more installation requirements.
- NEMA Standard 250 and IEC 60529, as applicable, for explanations of the degrees of protection provided by different types of enclosure.

## Preventing Electrostatic Discharge

<!-- image -->

ATTENTION: This equipment is sensitive to electrostatic discharge, which can cause internal damage and affect normal operation. Follow these guidelines when you handle this equipment:

- Touch a grounded object to discharge potential static.
- Wear an approved grounding wriststrap.
- Do not touch connectors or pins on component boards.
- Do not touch circuit components inside the equipment.
- Use a static-safe workstation, if available.
- Store the equipment in appropriate static-safe packaging when not in use.

## North American Hazardous Location Approval

| The following information applies when operating this equipment in hazardous locations:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Informations sur l’utilisation de cet équipement en environnements dangereux:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Products marked “CL I, DIV 2, GP A, B, C, D” are suitable for use in Class I Division 2 Groups A, B, C, D, Hazardous Locations and nonhazardous locations only. Each product is supplied with markings on the rating nameplate indicating the hazardous location temperature code. When combining products within a system, the most adverse temperature code (lowest “T” number) may be used to help determine the overall temperature code of the system. Combinations of equipment in your system are subject to investigation by the local Authority Having Jurisdiction at the time of installation. | Les produits marqués “CL I, DIV 2, GP A, B, C, D” ne conviennent qu'à une utilisation en environnements de Classe I Division 2 Groupes A, B, C, D dangereux et non dangereux. Chaque produit est livré avec des marquages sur sa plaque d'identification qui indiquent le code de température pour les environnements dangereux. Lorsque plusieurs produits sont combinés dans un système, le code de température le plus défavorable (code de température le plus faible) peut être utilisé pour déterminer le code de température global du système. Les combinaisons d'équipements dans le système sont sujettes à inspection par les autorités locales qualifiées au moment de l'installation. |

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

## WARNING: EXPLOSION HAZARD

- Do not disconnect equipment unless power has been removed or the area is known to be nonhazardous.
- Do not disconnect connections to this equipment unless power has been removed or the area is known to be nonhazardous. Secure any external connections that mate to this equipment by using screws, sliding latches, threaded connectors, or other means provided with this product.
- Substitution of components may impair suitability for Class I Division 2.
- If this product contains batteries, they must only be changed in an area known to be nonhazardous.

## AVERTISSEMENT: RISQUE D'EXPLOSION

- Couper le courant ou s'assurer que l'environnement est classé non dangereux avant de débrancher l'équipement.
- Couper le courant ou s'assurer que l'environnement est classé non dangereux avant de débrancher les connecteurs. Fixer tous les connecteurs externes reliés à cet équipement à l'aide de vis, loquets coulissants, connecteurs filetés ou autres moyens fournis avec ce produit.
- La substitution de composants peut rendre cet équipement inadapté à une utilisation en environnement de Classe I Division 2.
- S'assurer que l'environnement est classé non dangereux avant de changer les piles.

ATTENTION: This product is intended to be mounted to a well-grounded mounting surface such as a metal panel. Additional grounding connections from the power supply's mounting tabs or DIN rail (if used) are not required unless the mounting surface cannot be grounded. See Industrial Automation Wiring and Grounding Guidelines, publication 1770-4.1, for additional information.

ATTENTION: If this equipment is used in a manner not specified by the manufacturer, the protection provided by the equipment may be impaired.

ATTENTION: Do not place the module in direct sunlight. Prolonged exposure to direct sunlight could degrade the LCD.

ATTENTION: The USB device port is not intended for Customer use. The USB host port cable is not to exceed 3.0 m (9.84 ft).

<!-- image -->

## Catalog Number Explanation

| Catalog Number Operator Input Size Display Type   |           |
|---------------------------------------------------|-----------|
| 2711R-T4T Touch screen and function keys 4 in.    | Color TFT |
| 2711R-T7T Touch screen 7 in.                      | Color TFT |
| 2711R-T10T Touch screen 10 in.                    | Color TFT |

## About the Terminals

PanelView 800 terminals are operator interface devices for monitoring and controlling devices that are attached to a controller. HMI applications are created using Connected Components Workbench™ software, then downloaded to the terminal.

## PanelView 800 Terminal – 2711R-T4T

<!-- image -->

| Item Description Item Description                                    |                                                         |
|----------------------------------------------------------------------|---------------------------------------------------------|
| 1  Power status LED(1)                                               | 7 10/100 Mbit Ethernet port                             |
| 2 Touch display, function keys 8 RS-232 port                         |                                                         |
|                                                                      | 3 24V DC power input 9 RS-422 and RS-485 port           |
| 4  USB device port(2)                                                | 10 USB host port                                        |
| 5 microSD™ (Secure Digital) card slot 11 Diagnostic status indicator |                                                         |
|                                                                      | 6 Mounting slots 12 Replaceable real-time clock battery |

- (1) The Power Status LED is red when in screen saver or dimmer mode and green when in normal (operational) mode.

(2) The USB device port is not intended for Customer use.

## PanelView 800 Terminal – 2711R-T7T

<!-- image -->

| Item Description Item Description   |                                                                |
|-------------------------------------|----------------------------------------------------------------|
| 1  Power status LED(1)              | 7 Replaceable real-time clock battery                          |
|                                     | 2 Touch display 8 USB host port                                |
|                                     | 3 Mounting slots 9 Diagnostic status indicator                 |
|                                     | 4 RS-422 and RS-485 port 10 microSD (Secure Digital) card slot |
|                                     | 5 RS-232 port 11 24V DC power input                            |
| 6 10/100 Mbit Ethernet port 12      | USB device port(2)                                             |

- (1) The Power Status LED is red when in screen saver or dimmer mode and green when in normal (operational) mode.

(2) The USB device port is not intended for Customer use.

## PanelView 800 Terminal – 2711R-T10T

<!-- image -->

| Item Description Item Description   |                                                                |
|-------------------------------------|----------------------------------------------------------------|
| 1  Power status LED(1)              | 7 Replaceable real-time clock battery                          |
|                                     | 2 Touch display 8 USB host port                                |
|                                     | 3 Mounting slots 9 Diagnostic status indicator                 |
|                                     | 4 RS-422 and RS-485 port 10 microSD (Secure Digital) card slot |
|                                     | 5 RS-232 port 11 24V DC power input                            |
| 6 10/100 Mbit Ethernet port 12      | USB device port(2)                                             |

## Parts List

PanelView 800 terminals ship with these items:

- Power terminal block
- RS-422/RS-485 5-pin terminal block
- Lithium battery for real-time clock (pre-installed)
- Panel cutout template
- Mounting levers (four for 2711R-T4T, six for 2711R-T7T, and eight for 2711R-T10T)

## Install the Terminal

Before installing the terminal in a panel, review the minimum clearances, panel guidelines, panel cutout dimensions, and product dimensions.

## Minimum Spacing

Plan for adequate space around the terminal, inside the enclosure, for ventilation and cabling. Consider heat produced by other devices in the enclosure.

The ambient temperature around the terminal must be 0…50 °C (32…1 22 °F).

| Catalog Number Top Bottom Sides Back   |                                                                    |
|----------------------------------------|--------------------------------------------------------------------|
|                                        | 2711R-T4T 51 mm (2 in.) 51 mm (2 in.) 51 mm (2 in.) 51 mm (2 in.)  |
|                                        | 2711R-T7T 51 mm (2 in.) 51 mm (2 in.) 25 mm (1 in.) 51 mm (2 in.)  |
|                                        | 2711R-T10T 51 mm (2 in.) 25 mm (1 in.) 25 mm (1 in.) 51 mm (2 in.) |

<!-- image -->

WARNING: When you insert or remove the microSD card while power is on, an electrical arc can occur. This could cause an explosion in hazardous location installations.

Be sure that power is removed or the area is nonhazardous before proceeding.

<!-- image -->

The minimum spacing requirements are sufficient for connecting cables and inserting or removing a memory card. Plan for additional clearance if using the USB host port on the back of the unit.

## Mounting Angle

You can mount the terminal vertically against the panel, or tilted forward or backwards, up to a 60° angle. For 
°°° y gpp 
mounting angles greater than 60°, the operating temperature is restricted to 40 °C (104 °F).

## Panel Guidelines

Supporting panels must be at least 16 gauge to provide proper sealing against water and dust and to provide proper support. The panel surface must be flat and free of imperfections to maintain an adequate seal and NEMA Type ratings.

## Panel Cutout Dimensions

Use the template shipped with your terminal to mark the cutout dimensions.

| Catalog Number Height, approx., mm (in.) Width, approx., mm (in.)   |
|---------------------------------------------------------------------|
| 2711R-T4T 99.0 ±0.5 (3.89 ±0.02) 119.0 ±0.5 (4.68 ±0.02)            |
| 2711R-T7T 125.0 ±0.5 (4.92 ±0.02) 179.0 ±0.5 (7.05 ±0.02)           |
| 2711R-T10T 206.0 ±0.5 (8.11 ±0.02) 269.0 ±0.5 (10.59 ±0.02)         |

## Mount the PanelView 800 Terminal in a Panel

Mounting levers secure the PanelView 800 terminal to the panel.

<!-- image -->

<!-- image -->

<!-- image -->

ATTENTION: Follow these guidelines when mounting the terminal in a panel.

- Disconnect all electrical power from the panel before making the panel cutout.
- Make sure that the area around the panel cutout is clear.
- Take precautions so metal cuttings do not enter any components that are already installed in the panel.
- Failure to follow these instructions may result in personal injury or damage to panel components.

WARNING: If you connect or disconnect the serial cable with power applied to this module or the serial device on the other end of the cable, an electrical arc can occur. This could cause an explosion in hazardous location installations.

Be sure that power is removed or the area is nonhazardous before proceeding.

WARNING: When used in a Class I Division 2, hazardous location, this equipment must be mounted in a suitable enclosure with the proper wiring method that complies with the governing electrical codes.

Follow these steps to mount the terminal in a panel.

1. Cut an opening in the panel using the template shipped with the terminal.
2. Make sure that the sealing gasket is properly positioned on the terminal. This gasket forms a compression type seal. Do not use sealing compounds.
3. Place the terminal in the panel cutout.

## IMPORTANT

The terminal temperature must be greater than 0 °C (32 °F) during panel installation.

4. Insert all mounting levers into the mounting slots on the terminal. Slide each lever until the short, flat side of the lever touches the surface of the panel.
5. When all levers are in place, slide each lever an additional notch or two until you hear a click.

<!-- image -->

6. Rotate each lever in the direction that is indicated until it is in the final latch position. Follow the latching sequence for the optimum terminal fit.

<!-- image -->

<!-- image -->

Use this table as a guide to provide an adequate gasket seal between the terminal and the panel.

<!-- image -->

| Terminal Markings for Alignment   | Lever Position  Panel Thickness Range Typical Gauge   |
|-----------------------------------|-------------------------------------------------------|
| 6 1 2 1  4 3  6 5                 | 1 1.52…2.01 mm (0.060…0.079 in.) 16                   |
| 6 1 2 1  4 3  6 5                 | 2 2.03…2.64 mm (0.08…0.104 in.) 14                    |
| 6 1 2 1  4 3  6 5                 | 3 2.67…3.15 mm (0.105…0.124 in.) 12                   |
| 6 1 2 1  4 3  6 5                 | 4 3.17…3.66 mm (0.125…0.144 in.) 10                   |
| 6 1 2 1  4 3  6 5                 | 5 3.68…4.16 mm (0.145…0.164 in.) 8/9                  |
| 6 1 2 1  4 3  6 5                 | 6 4.19…4.75 mm (0.165…0.187 in.) 7                    |

## Remove the PanelView 800 Terminal from the Panel

Follow these steps to remove the terminal from the panel.

1. Disconnect power to the terminal.
2. Release the mounting lever by rotating it in the direction indicated, slide it to the bottom of the mounting slot, and remove it.

<!-- image -->

## 3. Grip the sides of the bezel and gently pull the terminal out of the panel opening.

<!-- image -->

## Product Dimensions

PanelView 800 Terminal – 2711R-T4T

<!-- image -->

PanelView 800 Terminal – 2711R-T7T

<!-- image -->

<!-- image -->

## PanelView 800 Terminal – 2711R-T10T

<!-- image -->

## PanelView 800 Terminal Dimensions

| Catalog Number   | Height, approx. Width, approx. Overall Depth, approx.  Mounted Depth, approx.     |
|------------------|-----------------------------------------------------------------------------------|
|                  | abcd                                                                              |
|                  | 2711R-T4T 116 mm (4.57 in.) 138 mm (5.43 in.) 43 mm (1.69 in.) 39 mm (1.54 in.)   |
|                  | 2711R-T7T 144 mm (5.67 in.) 197 mm (7.76 in.) 54 mm (2.13 in.) 50 mm (1.97 in.)   |
|                  | 2711R-T10T 225 mm (8.86 in.) 287 mm (11.30 in.) 55 mm (2.17 in.) 51 mm (2.01 in.) |

## USB Ports

You can power USB peripherals directly from the PanelView 800 terminal. If the USB peripheral is not powered directly from the PanelView USB port either:

- Install the USB peripheral in the same enclosure as the PanelView 800 terminal and make sure it is connected to the same ground system.
- Connect to the USB peripheral through a galvanically isolated hub.

<!-- image -->

<!-- image -->

WARNING: If you connect or disconnect the communications cable with power applied to this module or any device on the network, an electrical arc can occur. This could cause an explosion in hazardous location installations.

Be sure that power is removed or the area is nonhazardous before proceeding.

WARNING: If you connect or disconnect the USB cable with power applied to this module or any device on the USB network, an electrical arc can occur. This could cause an explosion in hazardous location installations.

Be sure that power is removed or the area is nonhazardous before proceeding.

## Choose a Power Supply

Use a dedicated 24V DC, Class 2 Safety Extra-low Voltage (SELV) or Protective Extra-low Voltage (PELV) power supply to power each PanelView 800 terminal.

<!-- image -->

ATTENTION: Use a Class 2, Safety Extra-low Voltage (SELV), or Protective Extra-low Voltage (PELV) power supply as required by local wiring codes for your installation. These power supplies provide protection so that under normal and single-fault conditions, the voltage between the conductors, and between conductors and functional earth, does not exceed a safe value.

<!-- image -->

<!-- image -->

WARNING: When you insert or remove connections while power is on, an electrical arc can occur. This could cause an explosion in hazardous location installations. Be sure that power is removed or the area is nonhazardous before proceeding. Repeated electrical arcing causes excessive wear to contacts on both the module and its mating connector. Worn contacts may create electrical resistance that can affect module operation.

WARNING: Do not connect directly to line voltage. Line voltage must be supplied by a suitable, approved isolating transformer or power supply having short circuit capacity not exceeding 100VA maximum or equivalent.

PanelView 800 terminals have been tested to operate with 1606-XLP power supplies. To use another power supply, review the criteria in the table.

## Power Supply Criteria

| If the PanelView 800 terminal Use a Description                                             |                                                                        |                                                                                                                                                                                                        |
|---------------------------------------------------------------------------------------------|------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Connects to equipment with isolated communication ports Does not connect to other equipment | SELV or PELV power supply                                              | Other equipment can share this power supply with the PanelView 800 terminal if no ground loops are created. A PELV power source internally connects the negative power terminal to the chassis ground. |
| Connects to equipment with nonisolated communication ports                                  | Dedicated, isolated, and ungrounded SELV source to power each terminal | This helps prevent ground loops from damaging the devices.                                                                                                                                             |

## Remove the Power Terminal Block

PanelView 800 terminals ship with a power terminal block installed. You can remove the power terminal block for ease of installation, wiring, and maintenance.

<!-- image -->

ATTENTION: Disconnect all power before installing or replacing components. Failure to disconnect power may result in electrical shock or damage to the terminal.

<!-- image -->

WARNING: When you connect or disconnect the Removable Power Terminal Block (RTB) while the module is powered, an electrical arc can occur. This could cause an explosion in hazardous location installations.

Be sure that power is removed or the area is nonhazardous before proceeding.

Follow these steps to remove the terminal block.

1. Insert the tip of a small, flat-blade, screwdriver into the terminal block access slot.
2. Gently pry the terminal block away from the terminal to release the locking mechanism.

<!-- image -->

Follow these steps to replace the terminal block.

1. Press the terminal block base in first with the block leaning outward.
2. Gently push the top of the terminal block back to a vertical position to snap in the locking tab.

## Connect Power

All PanelView 800 terminals connect to a 24V DC power source. The table shows the power ratings for each device.

## Power Ratings

|                 | Catalog Number Input Voltage Range Power Consumption, Max       |
|-----------------|-----------------------------------------------------------------|
| 2711R-T4T       | 18…32V DC (24V DC nom) 9 W 18…32V DC (24V DC nom)2711R-T7T 11 W |
| 2711R-T10T 14 W | 18…32V DC (24V DC nom) 9 W 18…32V DC (24V DC nom)2711R-T7T 11 W |
|                 | 18…32V DC (24V DC nom) 9 W 18…32V DC (24V DC nom)2711R-T7T 11 W |

The internal, nonisolated power supply is protected against reverse polarity of the DC+ and DC- connections.

<!-- image -->

ATTENTION: Connecting DC+ or DC- source to the functional earth terminal may damage the device. Miswiring the DC+ source to the DC- input while connected to other equipment through nonisolated ports may cause a ground loop current and damage the device.

<!-- image -->

WARNING: Use supply wires suitable for 30 °C (86 °F) above surrounding ambient.

<!-- image -->

WARNING: If you connect or disconnect wiring while the power is on, an electrical arc can occur. This could cause an explosion in hazardous location installations. Be sure that power is removed or the area is nonhazardous before proceeding.

The input power terminal block supports these wire sizes.

## Wire Specifications for Input Power Terminal Block

| Wire Type                           | Dual-wire Gauge (1)        | Single-wire Gauge          | Terminal Screw Torque     |
|-------------------------------------|----------------------------|----------------------------|---------------------------|
| Stranded or solid Cu 90 °C (194 °F) | 0.33…1.31 mm 2 (22…16 AWG) | 0.33…2.08 mm 2 (22…14 AWG) | 0.45…0.56 N•m (4…5 lb•in) |

<!-- image -->

ATTENTION: Disconnect all power before installing or replacing components. Failure to disconnect power may result in electrical shock or damage to the terminal.

<!-- image -->

ATTENTION: Do not wire more than 2 conductors on any single terminal.

Follow these steps to connect power.

1. Verify that the terminal is not connected to a power source.
2. Secure the 24V DC power wires to the terminal block.
3. Secure the functional earth ground wire to the functional earth ground terminal screw on the terminal block.
4. Apply 24V DC power to the terminal.

<!-- image -->

## Ground the Terminal

PanelView 800 terminals have a functional earth terminal that you must connect to a low-impedance earth ground. The functional earth connection is on the power input terminal block.

<!-- image -->

ATTENTION: The functional earth connection to ground is mandatory. This connection is required for noise immunity, reliability, and Electromagnetic Compliance (EMC) with the European Union (EU) EMC Directive for CE marking conformance.

The functional earth terminal wiring requires a minimum wire gauge.

## Functional Earth Wire Specifications

<!-- image -->

|                                     |                           | FE Symbol Wire Type Wire Gauge Terminal Screw Torque   |
|-------------------------------------|---------------------------|--------------------------------------------------------|
| Stranded or solid Cu 90 °C (194 °F) | 2.08…3.31 mm2 (14…12 AWG) | 0.45…0.56 N•m (4…5 lb•in)                              |

## Connect Devices

Use these cables for connecting devices to PanelView 800 terminals.

Cables for PanelView 800 Terminals

| Catalog Number Description                                                |
|---------------------------------------------------------------------------|
| 2711P-CBL-EX04 Ethernet crossover CAT5 cable 4.3 m (14 ft)                |
| 1747-CP3 Serial 9-pin D-shell to 9-pin D-shell null modem cable           |
| 1761-CBL-PM02 Serial 9-pin D-shell to 8-pin mini DIN cable, 2 m (6.56 ft) |
| 2711C-CBL-AB03 RS-485 5-pin to RJ45 cable                                 |

## RS-422/RS-485 Port

The RS-422/RS-485 port is an isolated port that supports point-to-point communications. RS-422 supports both full-duplex and half-duplex mode. RS-485 only supports half-duplex mode.

- In full-duplex mode, both devices can transmit and receive simultaneously. The transmit and receive pair are wired individually.
- In half-duplex mode, only one device can transmit at a time while the other device receives. One differential, twisted-pair connects to both receive and transmit pairs (R and T and on one wire, R- and Ton the other).

## RS-422/RS-485 Connector Pinout

| Pin Signal   |
|--------------|
| 1 T          |
| 2 T–         |
| 3 R          |
| 4 R–         |
| 5 S (Shield) |

The RS-422/485 port has an integrated 120 ohm termination between the R and R- signal pair. This value is compatible with RS-422 and RS-485 electrical specifications. Additional termination on the PanelView 800 terminal end of communication cables is not required.

## Troubleshooting

If your terminal does not start up correctly, check for adequate power and indicator states during power-up.

## Check for Adequate Power

A terminal that does not receive adequate power could cause unpredictable behavior. Verify the power requirements in the Specifications table.

## Interpret the LED Indicators at Startup

The PanelView 800 terminals have indicators to isolate operating problems. They can be seen through the battery cover on the back of the unit.

- Comm indicator for communications
- Fault indicator for hardware faults

At startup, the Fault indicator is off, except for a few brief flashes, and the Comm indicator is on. If the indicators remain off, check the power cable. After a successful startup, both indicators are off and controlled by the application running on the terminal.

The following table shows the indicator states if the terminal stops during startup.

## Fault Indicator States During Startup

| Fault (Red) Indicator State                                               | Comm (Green) Indicator State  Description Recommended Action                     |                                |                                |
|---------------------------------------------------------------------------|----------------------------------------------------------------------------------|--------------------------------|--------------------------------|
| Potentially recoverable errors                                            | Potentially recoverable errors                                                   | Potentially recoverable errors | Potentially recoverable errors |
| Blinking Off Last firmware download failed Reload the firmware            |                                                                                  |                                |                                |
|                                                                           | Blinking Blinking EBC boot loader firmware failed or missing Reload the firmware |                                |                                |
| Blinking On Windows® CE OS firmware failed or missing Reload the firmware |                                                                                  |                                |                                |
| Nonrecoverable or fatal errors                                            | Nonrecoverable or fatal errors                                                   | Nonrecoverable or fatal errors | Nonrecoverable or fatal errors |
|                                                                           | On Off Fatal hardware error Replace the terminal                                 |                                |                                |

## Battery Replacement

The PanelView 800 terminals contain a lithium battery that is intended to be replaced during the life of the product. The battery provides battery backup for the real-time clock. It is not used for application backup or retention.

<!-- image -->

WARNING: Verify that power has been removed from the terminal before replacing the battery. Work in a static-free environment and wear a properly grounded electrostatic discharge (ESD) wristband. Be careful when touching any of the exposed electronic components to help prevent damage from ESD.

<!-- image -->

<!-- image -->

WARNING: To avoid the danger of explosion, only replace the battery with 2711P-RY2032 or a manufacturer's equivalent such as the Matsushita or Duracell DL2032.

For safety information on the handling of lithium batteries, see the Guidelines for Handling Lithium Batteries, publication AG 5-4 .

Do not dispose of battery in a fire or incinerator. Dispose of used batteries in accordance with local regulations.

<!-- image -->

WARNING: When you connect or disconnect the battery an electrical arc can occur. This could cause an explosion in hazardous location installations. Be sure that the area is nonhazardous before proceeding.

For safety information on the handling of lithium batteries, including handling and disposal of leaking batteries, see the Guidelines for Handling Lithium Batteries, publication AG 5-4 .

## Battery Removal

<!-- image -->

This product contains a lithium battery that may need to be replaced during the life of the product. At the end of its life, the battery contained in this product should be collected separately from any unsorted municipal waste. The collection and recycling of batteries helps protect the environment and contributes to the conservation of natural resources as valuable materials are received.

<!-- image -->

ATTENTION: Battery contains Perchlorate Material – Special handling may apply. See www.dtsc.ca.gov/perchlorate .

This perchlorate warning only applies to primary Lithium Manganese Dioxide (LiMnO2) cells or batteries, and products containing these cells or batteries, sold or distributed in California, USA.

The battery is on the back of the terminals. No special tools are required to remove the battery cover, but a flattip screwdriver may be required to remove the battery.

<!-- image -->

This equipment is sensitive to electrostatic discharge (ESD). Follow ESD prevention guidelines when handling this equipment.

<!-- image -->

## Specifications

PanelView 800 – 2711R-T4T, 2711R-T7T, 2711R-T10T

| Value                                                                                                                                                                                         | Value                                                                                                                                                                                         | Value                                                                                                                                                                                         |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                                                                                                                                                                               |                                                                                                                                                                                               | 2711R-T4T 2711R-T7T 2711R-T10T                                                                                                                                                                |
| Display type Color transmissive TFT active matrix LCD, widescreen format                                                                                                                      | Display type Color transmissive TFT active matrix LCD, widescreen format                                                                                                                      | Display type Color transmissive TFT active matrix LCD, widescreen format                                                                                                                      |
|                                                                                                                                                                                               |                                                                                                                                                                                               | Display size 4 in. 7 in. 10 in.                                                                                                                                                               |
| 95 x 53.9 mm (3.74 X 2.12 in.)                                                                                                                                                                | Display area  153.6 x 86.6 mm (6.05 x 3.41 in.)                                                                                                                                               | 211.2 x 158.4 mm (8.31 x 6.24 in.)                                                                                                                                                            |
|                                                                                                                                                                                               | Resolution (pixels) 480 x 272 800 x 480 800 x 600                                                                                                                                             |                                                                                                                                                                                               |
| Backlight lifespan, min 40,000 hours                                                                                                                                                          | Backlight lifespan, min 40,000 hours                                                                                                                                                          | Backlight lifespan, min 40,000 hours                                                                                                                                                          |
| Analog touch and function keys                                                                                                                                                                | Operator input  Analog touch                                                                                                                                                                  | Operator input  Analog touch                                                                                                                                                                  |
| USB port and microSD (Secure Digital) card Industrial grade microSD cards recommended. Supports SDSC and Class 6 and Class 10 SDHC microSD cards, FAT32/16 formats, up to 32 GB maximum size. | USB port and microSD (Secure Digital) card Industrial grade microSD cards recommended. Supports SDSC and Class 6 and Class 10 SDHC microSD cards, FAT32/16 formats, up to 32 GB maximum size. | USB port and microSD (Secure Digital) card Industrial grade microSD cards recommended. Supports SDSC and Class 6 and Class 10 SDHC microSD cards, FAT32/16 formats, up to 32 GB maximum size. |
| Programming port Ethernet port                                                                                                                                                                | Programming port Ethernet port                                                                                                                                                                | Programming port Ethernet port                                                                                                                                                                |
| Battery lifespan, min 5 years @ 25 °C (77 °F)                                                                                                                                                 | Battery lifespan, min 5 years @ 25 °C (77 °F)                                                                                                                                                 | Battery lifespan, min 5 years @ 25 °C (77 °F)                                                                                                                                                 |
| Real-time clock Yes                                                                                                                                                                           | Real-time clock Yes                                                                                                                                                                           | Real-time clock Yes                                                                                                                                                                           |
| Input voltage range 18…32V DC (24V DC nom)                                                                                                                                                    | Input voltage range 18…32V DC (24V DC nom)                                                                                                                                                    | Input voltage range 18…32V DC (24V DC nom)                                                                                                                                                    |
|                                                                                                                                                                                               |                                                                                                                                                                                               | Power consumption, max 9 W 11 W 14 W                                                                                                                                                          |
| Weight, approx. 0.333 kg (0.73 lb) 0.651 kg (1.44 lb) 1.64 kg (3.62 lb)                                                                                                                       |                                                                                                                                                                                               |                                                                                                                                                                                               |
| 116 x 138 x 43 mm (4.56 x 5.43 x 1.69 in.)                                                                                                                                                    | Dimensions (HxWxD), approx.  144 x 197 x 54 mm (5.67 x 7.75 x 2.13 in.)                                                                                                                       | 225 x 287 x 55 mm (8.86 x 11.3 x 2.16 in.)                                                                                                                                                    |

## General Specifications

| Attribute Value              |                                                                        |
|------------------------------|------------------------------------------------------------------------|
| Wire size                    | Input Power Terminal Block ° p Stranded or solid, Cu 90 °C (194 °F) Single-Wire Gauge: 0.33…2.08 mm 2 (22...14 AWG) Dual-wire Gauge: 0.33…1.31 mm 2 (22…16 AWG)                                                                        |
| Wire type Copper             |                                                                        |
| Wiring category (1)          | 3 – on power ports 2 – on communication ports                          |
|                              | Enclosure type ratings Meets NEMA/UL Type 4X (indoor) 12, 13, and IP65 |
| North American temp code T4A |                                                                        |

## Environmental Specifications

| Attribute Value                                 |                                                                     |
|-------------------------------------------------|---------------------------------------------------------------------|
| Temperature, operating                          | IEC 60068-2-1 (Test Ad, Operating Cold), IEC 60068-2-2 (Test Bd, Operating Dry Heat), IEC 60068-2-14 (Test Nb, Operating Thermal Shock): °° 0…50 °C (32…122 °F)                                                                     |
| Temperature, nonoperating                       | IEC 60068-2-1 (Test Ab, Unpackaged Nonoperating Cold), IEC 60068-2-2 (Test Bb, Unpackaged Nonoperating Dry Heat), IEC 60068-2-14 (Test Na, Unpackaged Nonoperating Thermal Shock): °° -25…+70 °C (-13…+158 °F)                                                                     |
| Temperature, surrounding air, max               | 50 °C (122 °F)                                                      |
| Heat dissipation 2711R-T4T 2711R-T7T 2711R-T10T | 23 BTU/hr 34 BTU/hr 61 BTU/hr                                       |
| Relative humidity                               | IEC 60068-2-30 (Test Db, Unpackaged Damp Heat): 5…95% noncondensing |
| Vibration                                       | IEC 60068-2-6 (Test Fc, Operating): 2 g @ 10…500 Hz                 |
| Shock, operating                                | IEC 60068-2-27 (Test Ea, Unpackaged Shock): 15 g                    |
| Shock, nonoperating                             | IEC 60068-2-27 (Test Ea, Unpackaged Shock): 30 g                    |
|                                                 | Emissions IEC 61000-6-4                                             |
| ESD immunity                                    | IEC 61000-4-2: 6 kV contact discharges 8 kV air discharges          |
| Radiated RF immunity                            | IEC 61000-4-3: 10V/m with 1 kHz sine-wave 80% AM from 80…6000 MHz   |

## Environmental Specifications (Continued)

| Attribute Value          |                                                                                                                           |
|--------------------------|---------------------------------------------------------------------------------------------------------------------------|
| EFT/B immunity           | IEC 61000-4-4: ±2 kV @ 5 kHz on power ports ±1 kV @ 5 kHz on communication ports                                          |
| Surge transient immunity | IEC 61000-4-5: ±500V line-line(DM) and ±500V line-earth(CM) on DC power ports ±1 kV line-earth(CM) on communication ports |
| Conducted RF immunity    | IEC 61000-4-6: 10V rms with 1 kHz sine-wave 80% AM from 150 kHz…80 MHz                                                    |

## Certifications

| Certification (when product is marked) (1)   | Value                                                                                                                                                                                                                                                                           |
|----------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| c-UL-us                                      | UL Listed Industrial Control Equipment, certified for US and Canada. See UL File E322657. UL Listed for Class I Division 2 Group A, B, C, D Hazardous Locations, certified for U.S. and Canada. See UL File E334470.                                                            |
| CE                                           | European Union 2014/30/EU EMC Directive, compliant with: EN 61000-6-2; Industrial Immunity EN 61000-6-4; Industrial Emissions EN 61131-2; Programmable Controllers (Clause 8, Zone A & B) European Union 2011/65/EU RoHS, compliant with: EN IEC 63000; Technical documentation |
| RCM                                          | Australian Radiocommunications Act, compliant with: AS/NZS CISPR 11; Industrial Emissions                                                                                                                                                                                       |
| KC                                           | Korean Registration of Broadcasting and Communications Equipment, compliant with: Article 58-2 of Radio Waves Act, Clause 3                                                                                                                                                     |
|                                              | Morocco Arrêté ministériel n° 6404-15 du 29 ramadan 1436                                                                                                                                                                                                                        |
| UKCA                                         | 2016 No. 1091 – Electromagnetic Compatibility Regulations 2012 No. 3032 – Restriction of the Use of Certain Hazardous Substances in Electrical and Electronic Equipment Regulations                                                                                             |

## Additional Resources

For more information on the products that are described in this publication, use these resources.

|                                                                             | Resource Description                                                                             |
|-----------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|
| PanelView 800 HMI Terminals User Manual, publication 2711R-UM001            | Provides information on how to configure, use, and troubleshoot your PanelView 800 HMI terminal. |
| Industrial Automation Wiring and Grounding Guidelines, publication 1770-4.1 | Provides general guidelines for installing a Rockwell Automation industrial system.              |
| Product Certifications website, rok.auto/certifications                     | Provides declarations of conformity, certificates, and other certification details.              |

You can view or download publications at rok.auto/literature .

## Notes:

## Notes:

## Notes:

## Rockwell Automation Support

Use these resources to access support information.

| Technical Support Center                         | Find help with how-to videos, FAQs, chat, user forums, Knowledgebase, and product notification updates.   | rok.auto/support      |
|--------------------------------------------------|-----------------------------------------------------------------------------------------------------------|-----------------------|
| Local Technical Support Phone Numbers            | Locate the telephone number for your country.                                                             | rok.auto/phonesupport |
| Technical Documentation Center                   | Quickly access and download technical specifications, installation instructions, and user manuals.        | rok.auto/techdocs     |
| Literature Library                               | Find installation instructions, manuals, brochures, and technical data publications.                      | rok.auto/literature   |
| Product Compatibility and Download Center (PCDC) | Download firmware, associated files (such as AOP, EDS, and DTM), and access product release notes.        | rok.auto/pcdc         |

## Documentation Feedback

Your comments help us serve your documentation needs better. If you have any suggestions on how to improve our content, complete the form at rok.auto/docfeedback .

## Waste Electrical and Electronic Equipment (WEEE)

<!-- image -->

At the end of life, this equipment should be collected separately from any unsorted municipal waste.

Rockwell Automation maintains current product environmental compliance information on its website at rok.auto/pec .

Rockwell Otomasyon Ticaret A.Ş. Kar Plaza İş Merkezi E Blok Kat:6 34752, İçerenköy, İstanbul, Tel: +90 (216) 5698400 EEE Yönetmeliğine Uygundur

Connectwithus.

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

rockwellautomation.com expandinghumanpossibility

AMERICAS:RockwellAutomation,1201SouthSec0ndStreet,Milwaukee,WI53204-2496USA,Tel:(1)414.382.2000 EUROPE/MIDDLEEAST/AFRICA:RockwellAutomation NV,Pegasus Park,DeKleetlaan12a,1831Diegem,Belgium,Tel:(32)26630600 ASIA PACIFIC:RockwellAutomationSEAPte Ltd,2 Corporation Road,#04-05,MainLobby,CorporationPlace,Singapore 618494,Tel:(65)65106608 UNITED KINGDOM: Rockwell Automation Ltd., Pitfield, Kiln Farm, Milton Keynes, MK113DR, United Kingdom, Tel:(44)(1908)838-800

Allen-Bradley, Connected Components Workbench, expanding human possibility, FactoryTalk, PanelView, Rockwell Automation, and TechConnect are trademarks of Rockwell Automation, Inc.

microSD is a trademark of SD-3C.

Windows is a trademark of Microsoft Corporation.

Trademarks not belonging to Rockwell Automation are property of their respective companies.

<!-- image -->

PN-721963