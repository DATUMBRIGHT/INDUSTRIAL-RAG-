Original Instructions

## Kinetix 5500 Servo Drives

Catalog Numbers 2198-H003-ERS, 2198-H008-ERS, 2198-H015-ERS, 2198-H025-ERS, 2198-H040-ERS, 2198-H070-ERS, 2198-H003-ERS2, 2198-H008-ERS2, 2198-H015-ERS2, 2198-H025-ERS2, 2198-H040-ERS2, 2198-H070-ERS2

| Topic                                                          |   Page |
|----------------------------------------------------------------|--------|
| Summary of Changes                                             |      1 |
| About the Kinetix 5500 Drives                                  |      1 |
| Catalog Number Explanation                                     |      2 |
| Before You Begin                                               |      2 |
| Remove the Grounding Screws in Ungrounded Power Configurations |      2 |
| Install the Kinetix 5500 Servo Drive                           |      3 |
| Connector Data                                                 |      6 |
| Wiring Requirements                                            |      9 |
| Attach the Motor Cable Shield Clamp                            |      9 |
| Circuit Breaker/Fuse Selection                                 |     12 |
| Motor Overload Protection                                      |     14 |
| Additional Resources                                           |     15 |

## Summary of Changes

This publication contains new and updated information as indicated in the following table.

| Topic                                                                                                      |   Page |
|------------------------------------------------------------------------------------------------------------|--------|
| Added specifications per EU and UK Ecodesign, including efficiency class to the additional resources table |     15 |

## About the Kinetix 5500 Drives

Kinetix® 5500 servo drives provide an Integrated Motion over the EtherNet/IP™ network solution for applications with output power and current requirements in the range of 0.2…14.6 kW and 1.4…32.5 A 0-pk, respectively.

See the Kinetix 5500 Servo Drives User Manual, publication 2198-UM001, for detailed information on wiring, applying power, troubleshooting, and integration with ControlLogix® 5570, ControlLogix 5580, and GuardLogix® 5570, or CompactLogix™ 5370 and Compact GuardLogix 5370 controllers.

<!-- image -->

<!-- image -->

## Catalog Number Explanation

This publication applies to the following Kinetix 5500 servo drives. For connecting safe torque-off signals, hardwired drives use the safe torque-off (STO) connector and ship with the protective cover removed. Integrated safe torque-off drives do not use the STO connector and ship with the protective cover in place. See Connector Data on page 6 to locate the cover.

## Kinetix 5500 Drive Catalog Numbers

| Drive Cat. No. (hardwired STO)   | Drive Cat. No. (integrated STO)   |    | Frame Size Input Voltage                                                       | Continuous Output Power kW   |   Continuous Output Current A 0-pk |
|----------------------------------|-----------------------------------|----|--------------------------------------------------------------------------------|------------------------------|------------------------------------|
| 2198-H003-ERS                    | 2198-H003-ERS2                    |    | 195…264V rms, single-phase 195…264V rms, three-phase 324…528V rms, three-phase | 0.2 kW 0.3 kW 0.6 kW         |                                1.4 |
| 2198-H008-ERS                    | 2198-H008-ERS2                    |    | 195…264V rms, single-phase 195…264V rms, three-phase 324…528V rms, three-phase | 0.5 kW 0.8 kW 1.6 kW         |                                3.5 |
| 2198-H015-ERS                    | 2198-H015-ERS2                    | 2  | 195…264V rms, single-phase 195…264V rms, three-phase 324…528V rms, three-phase | 1.0 kW 1.5 KW 3.2 kW         |                                7.1 |
| 2198-H025-ERS                    | 2198-H025-ERS2                    | 2  | 195…264V rms, three-phase 324…528V rms, three-phase                            | 2.4 kW 5.1 kW                |                               11.3 |
| 2198-H040-ERS                    | 2198-H040-ERS2                    | 2  | 195…264V rms, three-phase 324…528V rms, three-phase                            | 4.0 kW 8.3 kW                |                               18.4 |
| 2198-H070-ERS                    | 2198-H070-ERS2 3                  |    | 195…264V rms, three-phase 324…528V rms, three-phase                            | 7.0 kW 14.6 kW               |                               32.5 |

## Before You Begin

Remove all packing material, wedges, and braces from within and around the components. After unpacking, check the item nameplate catalog number against the purchase order.

The Kinetix 5500 servo drives ship with the following:

- Wiring plug connector set for mains input power (IPD), 24V control input power (CP), digital inputs (IOD), motor power (MP), motor brake (BC), and safe torque-off (STO)
- 2198-KITCON-DSL connector kit for motor feedback connections
- Wiring plug connector for shunt power (RC) connections that is installed on the drive
- These installation instructions, publication 2198-IN001

<!-- image -->

Replacement connector sets are also available. See the Kinetix 5700, 5500, 5300, and 5100 Servo Drives Specifications, publication KNXTD003, for more information.

## Remove the Grounding Screws in Ungrounded Power Configurations

Remove the grounding screws only when using ungrounded, corner-grounded, or impedance-grounded power configurations. Removing the screws involves gaining access, opening the side door, and removing the screws.

IMPORTANT If you have grounded wye power distribution, you do not need to remove the screws. Go to Install the Kinetix 5500 Servo Drive on page 3 . Removing the grounding screws can affect EMC performance.

Removing the grounding screws in multi-axis configurations is best done when the drive is removed from the panel and placed on its side on a solid surface that is equipped as a grounded static-safe workstation.

<!-- image -->

ATTENTION: Because the unit no longer maintains line-to-neutral voltage protection, the risk of equipment damage exists when you remove the grounding screws.

<!-- image -->

ATTENTION: To avoid personal injury, the grounding screws access door must be kept closed when power is applied. If power was present and then removed, wait at least 5 minutes for the DC-bus voltage to dissipate and verify that no DC-bus voltage exists before accessing the grounding screws.

## Remove the Grounding Screws

<!-- image -->

<!-- image -->

ATTENTION: Risk of equipment damage exists. The drive ground configuration must be accurately determined. Leave the grounding screws installed for grounded power configurations (default). Remove the screws for ungrounded, ungrounded, corner-grounded, and impedancegrounded power.

## Grounding Screw Configurations

| Ground Configuration  (1)                                  | Grounding Screw Configuration           | Benefits of Configuration                                                                                                            |
|------------------------------------------------------------|-----------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| Grounded (wye)                                             | Both screws installed (default setting) | • UL and EMC compliance • Reduced electrical noise • Most stable operation • Reduced voltage stress on components and motor bearings |
| • AC fed ungrounded • Corner grounded • Impedance grounded | Both screws removed                     | • Helps avoid severe equipment damage when ground faults occurs • Reduced leakage current                                            |
| Single-phase input power                                   | AC screw removed (2)                    | Minimizes leakage current for single-phase operation                                                                                 |

## Install the Kinetix 5500 Servo Drive

These procedures assume that you have prepared your panel and understand how to bond your system. For installation instructions regarding equipment and accessories not included here, refer to the instructions that came with those products.

<!-- image -->

SHOCK HAZARD: To avoid hazard of electrical shock, perform all mounting and wiring of the Kinetix 5500 drive prior to applying power. Once power is applied, connector terminals can have voltage present even when not in use.

<!-- image -->

ATTENTION: Plan the installation of your system so that you can perform all cutting, drilling, tapping, and welding with the system removed from the enclosure. Because the system is of the open type construction, be careful to keep any metal debris from falling into it. Metal debris or other foreign matter can become lodged in the circuitry and result in damage to components.

## Mount the Kinetix 5500 Drive

Follow these steps to mount the drive in single-axis configurations.

1. Observe these clearance requirements when mounting a single drive to the panel:
- Additional clearance is required for cables and wires or the shared-bus connection system connected to the top of the drive.
- Additional clearance is required if other devices are installed above and/or below the drive and have clearance requirements of their own.
- Additional clearance left and right of the drive is required when mounted adjacent to noise sensitive equipment or clean wire ways.
- The recommended minimum cabinet depth is 300 mm (11.81 in.).

40 mm (1.57 in.) clearance above drive for airflow and installation.

<!-- image -->

40 mm (1.57 in.) clearance below drive for airflow and installation.

Refer to the Kinetix 5700, 5500, 5300, and 5100 Servo Drives Specifications, publication KNX-TD003, for Kinetix 5500 drive dimensions.

## IMPORTANT Mount the drive in an upright position as shown. Do not mount the drive on its side.

In multi-axis shared-bus configurations, drives must be spaced by aligning the zero-stack tab and cutout. For mounting, sizing, and configuring shared-bus configurations, refer to the Kinetix 5500 Servo Drives User Manual, publication 2198-UM001 .

<!-- image -->

Bus-bar system used in bus-sharing configurations is not shown for clarity.

2. Mount the Kinetix 5500 drive to the cabinet subpanel with M4 (#8-32) steel machine screws torqued to 2.0 N·m (17.7 lb·in), max.

## Product Dimensions

Included in this figure are the drill hole patterns for standalone drives. Refer to the Kinetix 5500 Servo Drives User Manual, publication 2198-UM001, for multi-axis drill-hole patterns.

## Kinetix 5500 Drives with 2198-KITCON-DSL Connector Kit

<!-- image -->

| Kinetix 5500 Drive             |       | A        | B                      | C mm (in.)   | D mm (in.)            | E mm (in.)   | Drill Hole Patterns                   | Drill Hole Patterns   |
|--------------------------------|-------|----------|------------------------|--------------|-----------------------|--------------|---------------------------------------|-----------------------|
| Cat. No.                       | Frame | mm (in.) | mm (in.)               |              |                       |              | F mm (in.)                            | G mm (in.)            |
| 2198-H003-ERSx  2198-H008-ERSx | 1     |          | 50 (1.97) 170 (6.69)   |              | 200 (7.87) 226 (8.90) |              | 215 (8.46) 193.68 (7.62) 4.51 (0.18)  |                       |
| 2198-H015-ERSx 2198-H025-ERSx  | 2     |          | 55 (2.16) 225 (8.86)   |              | 200 (7.87) 226 (8.90) |              | 265 (10.43) 243.84 (9.60) 5.00 (0.20) |                       |
| 2198-H040-ERSx 2198-H070-ERSx  | 3     |          | 85.2 (3.35) 250 (9.84) |              | 200 (7.87) 226 (8.90) |              | 294 (11.57) 273.70 (10.78) 0.0        |                       |

## Kinetix 5500 Drives with 2198-H2DCK Converter Kit

<!-- image -->

Refer to Kinetix 5700, 5500, 5300, and 5100 Servo Drives Specifications, publication KNX-TD003, for motor/actuator compatibility with the 2198-H2DCK converter kit and product dimensions.

## Connector Data

Use this illustration to identify the Kinetix 5500 drive features and indicators.

## Kinetix 5500 Drive Features and Indicators

<!-- image -->

| Item Description                                 |
|--------------------------------------------------|
| 1 Motor cable shield clamp                       |
| 2  Converter kit mounting hole (under cover) (1) |
| 3 Motor feedback (MF) connector                  |
| 4 Digital inputs (IOD) connector                 |
| 5 Ethernet (PORT1) RJ45 connector                |
| 6 Ethernet (PORT2) RJ45 connector                |
| 7 Zero-stack mounting tab/cutout                 |

<!-- image -->

| Item Description                   |
|------------------------------------|
| 8 Module status indicator          |
| 9 Network status indicator         |
| 10 LCD display                     |
| 11 Navigation push buttons         |
| 12 Link speed status indicators    |
| 13 Link/Activity status indicators |
| 14 Motor power (MP) connector      |

- (1) Protective knock-out covers the 2198-H2DCK converter kit mounting hole. Remove knock-out for use with the converter kit.
- (2) DC bus connector ships with protective knock-out cover that can be removed for use in shared-bus configurations.
- (3) Protective knock-out cover is removed on 2198-Hxxx-ERS (hardwired STO) drives.

## Kinetix 5500 Drive Connectors

|     | Designator Description                                  | Connector                                                                      |
|-----|---------------------------------------------------------|--------------------------------------------------------------------------------|
| IPD | AC mains input power                                    | 4-position plug, terminal screws                                               |
| DC  |                                                         | DC common bus power 2-position (T-connector used in shared-bus configurations) |
| CP  |                                                         | 24V control input power 2-position plug, terminal screws                       |
| RC  | Shunt power                                             | 2-position plug, terminal screws                                               |
| MP  | Motor power                                             | 4-position plug, terminal screws                                               |
| MF  | Motor feedback                                          | 2-position plug, spring terminals                                              |
| BC  | Brake power                                             | 2-position plug, terminal screws                                               |
| IOD | Digital inputs                                          | 4-position plug, spring terminals                                              |
|     | STO Safe torque off                                     | 5-position plugs, spring terminals, 2x (2 rows of 5 pins)                      |
|     | PORT1, PORT2 Ethernet communication ports RJ45 Ethernet |                                                                                |

## Mains Input Power (IPD) Connector

|    | IPD Pin Description     | Signal   |
|----|-------------------------|----------|
|    | Chassis ground          |          |
| L3 | Three-phase input power | L3       |
| L2 | Three-phase input power | L2       |
| L1 | Three-phase input power | L1       |

| Description                                                                     |
|---------------------------------------------------------------------------------|
| 15 Motor brake (BC) connector                                                   |
| 16 Ground terminal                                                              |
| 17 Shunt resistor (RC) connector                                                |
| 18 AC mains input power (IPD) connector                                         |
| 19  DC bus (DC) connector (under cover) (2)                                     |
| 20 24V control input power (CP) connector                                       |
| 21  Safe torque-off (STO) connector  (3) (applies to only 2198-Hxxx-ERS drives) |

<!-- image -->

## Shunt Power (RC) Connector Pinout

|    | RC Pin Description                 | Signal   |
|----|------------------------------------|----------|
|  1 | Shunt connections (frames 2 and 3) | DC+      |
|  2 | Shunt connections (frames 2 and 3) | SH       |
|  1 | Shunt connections (frame 1)        | SH       |
|  2 | Shunt connections (frame 1)        | DC+      |

## DC Bus (DC) Connector Pinout

|    | DC Pin Description   | Signal   |
|----|----------------------|----------|
|  1 | DC bus connections   | DC          |
|  2 | DC bus connections   | DC+      |

## Control Input Power (CP) Connector Pinout

|    | CP Pin Description                  | Signal   |
|----|-------------------------------------|----------|
|  1 | 24V power supply, customer-supplied | 24V+     |
|  2 | 24V common                          | 24V          |

## Motor Power (MP) Connector Pinout

|    | MP Pin Description                                 | Signal Color   |         |
|----|----------------------------------------------------|----------------|---------|
| U  | Three-phase motor power Three-phase motor powerV V |                | U Brown |
|    | Three-phase motor power Three-phase motor powerV V |                | Black   |
|    | Three-phase motor power Three-phase motor powerV V | W W            | Blue    |
|    | Chassis ground                                     |                | Green   |

## Motor Feedback (MF) Connector Pinout

| MF Pin (1)   | Description                                                                                    | Signal   |       |
|--------------|------------------------------------------------------------------------------------------------|----------|-------|
| 1            | Bidirectional data and power for digital encoder interface                                     | D+       | Pin 1 |
| 2            | Bidirectional data and power for digital encoder interface                                     | D          | Pin 1 |
| SHIELD       | Cable shield and grounding plate (internal to 2198-KITCON-DSL connector kit) termination point | SHIELD   | Pin 2 |
| SHIELD       | Cable shield and shield clamp (internal to 2198-H2DCK converter kit) termination point         |          |       |

## Motor Brake (BC) Connector Pinout

|     | BC Pin Description      | Signal   |     |
|-----|-------------------------|----------|-----|
| 1 2 | Motor brake connections | MBRK+ MBRK          | 2 1 |

## Digital Inputs (IOD) Connector Pinout

|    | IOD Pin Description                                               | Signal   |
|----|-------------------------------------------------------------------|----------|
|  1 | 24V current-sinking fast input #1. This is a dual-function input. | IN1 (1)  |
|  2 | I/O common for customer-supplied 24V supply.                      | COM      |
|  3 | 24V current-sinking fast input #2.                                | IN2      |
|  4 | I/O cable shield termination point.                               | SHLD     |

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

Pin 1

<!-- image -->

## Safe Torque Off (STO) Connector Pinout

|    | STO Pin Description                                                                       | Signal   |
|----|-------------------------------------------------------------------------------------------|----------|
| 1  | Safety bypass plus signal. Connect to both safety inputs to disable the STO function. SB+ |          |
| 2  | Safety bypass minus signal. Connect to safety common to disable the STO function. SB                                                                                           |          |
| 3  | STO input 1 (SS_IN_CH0).                                                                  | S1       |
|    | 4 STO input common (SCOM) .                                                               | SC       |
| 5  | STO input 2 (SS_IN_CH1).                                                                  | S2       |

IMPORTANT The safe torque-off (STO) connector applies to only the 2198-Hxxx-ERS drives.

The 2198-Hxxx-ERS drives ship with the safe torque-off function enabled. Connect the safe torque-off inputs to a safety circuit or install bypass wiring to enable motion. Refer to the Kinetix 5500 Servo Drives User Manual, publication 2198-UM001, for more information.

## Ethernet Communication PORT1 and PORT2 Pinout

|     | Port Pin Description            | Signal   |
|-----|---------------------------------|----------|
| 1   | Transmit port (+) data terminal | TD+      |
| 2   | Transmit port (-) data terminal | TD          |
| 3   | Receive port (+) data terminal  | RD+      |
| 4 – |                                 | –        |
| 5 – |                                 | –        |
| 6   | Receive port (-) data terminal  | RD          |
| 7 – |                                 | –        |
|     | 8 –                             | –        |

<!-- image -->

<!-- image -->

## Wiring Requirements

Wire must be copper with 75  C (167  F) minimum rating. Phasing of mains AC power is arbitrary and earth ground connection is required for safe and proper operation .

IMPORTANT The National Electrical Code and local electrical codes take precedence over the values and methods provided.

## Kinetix 5500 Drive Power and I/O Wiring Requirements

| Kinetix 5500 Drive                                                          | Description                                        | Connects to Terminals                           | Connects to Terminals   | Wire Size                                                                  | Strip Length   | Torque Value N•m (lb•in)   |
|-----------------------------------------------------------------------------|----------------------------------------------------|-------------------------------------------------|-------------------------|----------------------------------------------------------------------------|----------------|----------------------------|
| Cat. No.                                                                    |                                                    |                                                 | Pin Signal              | mm 2  (AWG)                                                                | mm (in.)       |                            |
| 2198-H003-ERSx 2198-H008-ERSx 2198-H015-ERSx  2198-H025-ERSx 2198-H040-ERSx | Mains input (1)  power (single-axis IPD connector) | IPD-1 IPD-2 IPD-3 IPD-4                         | L1 L2 L3                | 1.5…4 (16…12)                                                              | 7.0 (0.28)     | 0.5…0.6 (4.4…5.3)          |
| 2198-H070-ERSx                                                              | Mains input (1)  power (single-axis IPD connector) | IPD-1 IPD-2 IPD-3 IPD-4                         | L1 L2 L3                | 1.5…6 (16…10)                                                              | 10.0 (0.39)    | 0.5…0.6 (4.4…5.3)          |
| 2198-H003-ERSx 2198-H008-ERSx 2198-H015-ERSx 2198-H025-ERSx 2198-H040-ERSx  | Motor power                                        | MP-1 MP-2 MP-3 MP-4                             | W V U                   | Motor power cable depends on motor/drive combination. 0.75…2.5 (2) (18…14) | 8.0 (0.31)     | 0.5…0.6 (4.4…5.3)          |
| 2198-H070-ERSx                                                              | Motor power                                        | MP-1 MP-2 MP-3 MP-4                             | W V U                   | 2.5…6 (2) (14…10)                                                          | 10.0 (0.39)    | 0.5…0.8 (4.4…7.1)          |
| 2198-Hxxx-ERSx                                                              | PELV/SELV 24V power (single-axis CP connector)     | CP-1 CP-2                                       | 24V+ 24V                         | 2.5…0.5 (14…20)                                                            | 7.0 (0.28)     | 0.22…0.25 (1.9…2.2)        |
| 2198-Hxxx-ERSx                                                              | Brake power                                        | BC-1 BC-2                                       | MBRK+ MBRK-             | —  (3)                                                                     | 7.0 (0.28)     | 0.22…0.25 (1.9…2.2)        |
| 2198-Hxxx-ERSx                                                              | DC Bus power                                       | DC-1 DC-2                                       | DC+ DC-                 | —  (4)                                                                     | —  (4)         | —  (4)                     |
| 2198-Hxxx-ERSx                                                              | Shunt power (frames 2 and 3)                       | RC-1 RC-2                                       | DC+ SH                  | 0.5…4.0 (20…12)  (20…12) 8.0 (0.31) (4.4…5.3) Shunt power RC-1SH                                                                            | 8.0 (0.31)     | 0.5…0.6                    |
| 2198-Hxxx-ERSx                                                              | (frame 1) (5)                                      | RC-1 RC-2                                       | SH DC+                  | 0.2…1.5                                                                    | 10.0 (0.39)    | —  (6)                     |
| 2198-Hxxx-ERSx                                                              | Safety  Digital inputs                             | ST0-1 ST0-2 ST0-3 ST0-4 ST0-5 IOD-1 IOD-2 IOD-3 | SB+ SB S1 SC S2 IN1 (7) COM IN2                         | (24…16)  0.2…1.5 (24…16)                                                   | 10.0 (0.39)    | —  (6)                     |

<!-- image -->

- (5) These signals and the safe torque-off (STO) connector apply to only the 2198-Hxxx-ERS drives.

(6) This connector uses spring tension to hold wires in place.

- (7) This signal has dual-functionality. You can use IN1 (IOD-1) as registration or Home input.

<!-- image -->

ATTENTION: To avoid personal injury and/or equipment damage, observe the following:

- Make sure installation complies with specifications regarding wire types, conductor sizes, branch circuit protection, and disconnect devices. The National Electrical Code (NEC) and local codes outline provisions for safely installing electrical equipment.
- Use motor power connectors only for connection purposes. Do not use them to turn the unit on and off.
- Ground shielded power cables to prevent potentially high voltages on the shield.

## Attach the Motor Cable Shield Clamp

A shield clamp and two screws are supplied with each Kinetix 5500 drive. Use the clamp to bond the motor cable shield-braid to chassis ground.

## IMPORTANT

- Loosen the screw, if needed, until you can start threading both clamp screws with the cable shield under the clamp.
- Make sure the cable clamp tightens around the cable shield and provides a good bond between the cable shield and the drive chassis.

## Kinetix VP Servo Motors

These examples illustrate 2090-CSxM1DF/DG motor cables with connections to Kinetix VP motors and using 2198-KITCON-DSL feedback connector kits. If your motor connections are coming from other compatible Allen-Bradley® servo motors/actuators, see Other Allen-Bradley Motors and Actuators on page 11 .

## Cable Shield Clamp Installation

<!-- image -->

When the drive/motor combination calls for 18 AWG cable, the feedback

IMPORTANT cable routes around the motor cable shield clamp.

<!-- image -->

IMPORTANT When the drive/motor combination calls for 14 or 10 AWG cable, the feedback cable routes along with the power and brake wiring.

<!-- image -->

<!-- image -->

## Other Allen-Bradley Motors and Actuators

The other compatible Allen-Bradley motors and actuators require the 2198-H2DCK converter kit for wiring motor feedback. A clamp spacer is included with the kit for motor power/brake cable diameters that are too small for a tight fit within the drive clamp alone.

## IMPORTANT

If the power/brake cable shield has a loose fit inside the shield clamp, insert the clamp spacer between the shield clamp and the drive to reduce the clamp diameter. When the clamp screws are tight, 2.0 N·m (17.7 lb·in), the result must be a high-frequency bond between the cable shield and the drive chassis.

## Cable Clamp Attachment

<!-- image -->

Refer to the Kinetix 5500 Servo Drives User Manual, publication 2198-UM001, for detailed information on wiring the 2198-H2DCK feedback converter kit and attaching the motor power/brake shield clamp.

## Ground Your Kinetix 5500 Drive to the Subpanel

Ground Kinetix 5500 drives and 2198-CAPMOD-1300 capacitor modules to a bonded cabinet ground bus with a braided ground strap. Keep the braided ground strap as short as possible for optimum bonding.

## Connecting the Braided Ground Strap

<!-- image -->

| Item Description                                 |
|--------------------------------------------------|
| 1 Ground screw (green) 2.0 N•m (17.5 lb•in), max |
| 2 Braided ground strap (customer supplied)       |
| 3 Ground grid or power distribution ground       |
| 4  Bonded cabinet ground bus (customer supplied) |

Refer to the System Design for Control of Electrical Noise Reference Manual, publication GMC-RM001, for more information.

## Circuit Breaker/Fuse Selection

The Kinetix 5500 drives use internal solid-state motor short-circuit protection and, when protected by suitable branch circuit protection, are rated for use on a circuit capable of delivering up to 200,000 A (fuses) and 65,000 A (circuit breakers).

## Standalone Drive Systems

| Kinetix 5500 Drives   | Kinetix 5500 Drives                     | UL Applications               | UL Applications                                              | IEC (non-UL) Applications   | IEC (non-UL) Applications    |
|-----------------------|-----------------------------------------|-------------------------------|--------------------------------------------------------------|-----------------------------|------------------------------|
|                       | Drive Cat. No. Drive Voltage, nom Phase | Bussmann Fuses Cat. No.       | Molded Case CB Cat. No.                                      | DIN gG Fuses Amps (max)     | Molded Case CB Cat. No.      |
| 2198-H003-ERSx        | 240V                                    | Single-phase KTK-R-2          | 140U-D6D2-B10 140UT-D7D2-B10                                 | 2                           | 140U-D6D2-B10 140UT-D7D2-B10 |
| 2198-H003-ERSx        | 240/480V                                | Three-phase KTK-R-3           | 140U-D6D3-B20 140UT-D7D3-B20                                 | 4                           | 140U-D6D3-B20 140UT-D7D3-B20 |
| 2198-H008-ERSx        |                                         | 240V Single-phase KTK-R-5     | 140U-D6D2-B20 140UT-D7D2-B20                                 | 6                           | 140U-D6D2-B20 140UT-D7D2-B20 |
| 2198-H008-ERSx        | 240/480V Three-phase KTK-R-7            |                               | 140U-D6D3-B60 140UT-D7D3-B60                                 | 6                           | 140U-D6D3-B60 140UT-D7D3-B60 |
| 2198-H015-ERSx        |                                         | 240V Single-phase KTK-R-10    | 140U-D6D2-B80 140UT-D7D2-B80                                 | 10                          | 140U-D6D2-B80 140UT-D7D2-B80 |
| 2198-H015-ERSx        | 240/480V Three-phase KTK-R-15           |                               | 140U-D6D3-C12 140UT-D7D3-C12                                 | 16                          | 140U-D6D3-C12 140UT-D7D3-C12 |
| 2198-H025-ERSx        |                                         | 240/480V Three-phase KTK-R-20 | 140U-D6D3-C20 140UT-D7D3-C20                                 | 20                          | 140U-D6D3-C20 140UT-D7D3-C20 |
| 2198-H040-ERSx        |                                         | 240/480V Three-phase KTK-R-25 | 140U-D6D3-C25 140UT-D7D3-C25                                 | 25                          | 140U-D6D3-C25 140UT-D7D3-C25 |
| 2198-H070-ERSx        |                                         |                               | 240/480V Three-phase LPJ-35SP 140G-G6C3-C40 35 140G-G6C3-C40 |                             |                              |

## Shared DC (common-bus) Drive Systems

| Kinetix 5500 Drive Cat. No.   | Drive Voltage, (three-phase) nom   | UL Applications         | UL Applications              | IEC (non-UL) Applications   | IEC (non-UL) Applications    |
|-------------------------------|------------------------------------|-------------------------|------------------------------|-----------------------------|------------------------------|
| Kinetix 5500 Drive Cat. No.   | Drive Voltage, (three-phase) nom   | Bussmann Fuses Cat. No. | Molded Case CB Cat. No.      | DIN gG Fuses Amps (max)     | Molded Case CB Cat. No.      |
| 2198-H003-ERSx                | 240/480V                           | KTK-R-10                | —                            | 10                          | —                            |
| 2198-H008-ERSx                | 240/480V                           | KTK-R-10                | —                            | 10                          | —                            |
| 2198-H015-ERSx                | 240/480V                           | KTK-R-15                | 140U-D6D3-C15 140UT-D7D3-C15 | 16                          | 140U-D6D3-C15 140UT-D7D3-C15 |
| 2198-H025-ERSx                | 240/480V                           | KTK-R-20                | 140U-D6D3-C20 140UT-D7D3-C20 | 20                          | 140U-D6D3-C20 140UT-D7D3-C20 |
| 2198-H040-ERSx                | 240/480V                           | KTK-R-25                | 140U-D6D3-C25 140UT-D7D3-C25 | 25                          | 140U-D6D3-C25 140UT-D7D3-C25 |
| 2198-H070-ERSx                | 240/480V                           | LPJ-35SP                | 140G-G6C3-C40                | 35                          | 140G-G6C3-C40                |

## Shared AC Drive Systems

Input Power UL Circuit-protection Specifications

| Kinetix 5500 Drive Cat. No.   | Drive Voltage, (three-phase) nom Bussmann Fuses Cat. No.   | Molded Case CB Cat. No.             | Molded Case CB Cat. No.      | Molded Case CB Cat. No.                                 | Molded Case CB Cat. No.   |
|-------------------------------|------------------------------------------------------------|-------------------------------------|------------------------------|---------------------------------------------------------|---------------------------|
|                               |                                                            |                                     |                              | 2 Axes 3 Axes 4 Axes 5 Axes 2 Axes 3 Axes 4 Axes 5 Axes |                           |
| 2198-H003-ERSx                | 240/480V KTK-R-15 —                                        |                                     |                              |                                                         |                           |
| 2198-H008-ERSx                | 240/480V KTK-R-15 —                                        |                                     |                              |                                                         |                           |
| 2198-H015-ERSx                | 240/480V KTK-R-20 KTK-R-25 —                               | 140U-D6D3-C15 140UT-D7D3-C15        | 140U-D6D3-C20 140UT-D7D3-C20 | —                                                       |                           |
| 2198-H025-ERSx                | 240/480V KTK-R-30 —                                        | 140U-D6D3-C25 140UT-D7D3-C25        | 140U-D6D3-C30 140UT-D7D3-C30 | —                                                       |                           |
| 2198-H040-ERSx                | 240/480V LPJ-35SP LPJ-45SP — —                             |                                     |                              |                                                         |                           |
| 2198-H070-ERSx                |                                                            | 240/480V LPJ-60SP — 140G-G6C3-C60 — |                              |                                                         |                           |

## Input Power IEC (non-UL) Circuit-protection Specifications

| Kinetix 5500 Drive Cat. No.   | Drive Voltage, (three-phase) nom DIN gG Fuses Amps (max)   |                                                         | Molded Case CB Cat. No.      | Molded Case CB Cat. No.      | Molded Case CB Cat. No.   | Molded Case CB Cat. No.   |
|-------------------------------|------------------------------------------------------------|---------------------------------------------------------|------------------------------|------------------------------|---------------------------|---------------------------|
|                               |                                                            | 2 Axes 3 Axes 4 Axes 5 Axes 2 Axes 3 Axes 4 Axes 5 Axes |                              |                              |                           |                           |
| 2198-H003-ERSx                | 240/480V 16 —                                              |                                                         |                              |                              |                           |                           |
| 2198-H008-ERSx                | 240/480V 16 —                                              |                                                         |                              |                              |                           |                           |
| 2198-H015-ERSx                | 240/480V 20 25 —                                           |                                                         | 140U-D6D3-C15 140UT-D7D3-C15 | 140U-D6D3-C20 140UT-D7D3-C20 | —                         | —                         |
| 2198-H025-ERSx                | 240/480V 32 —                                              |                                                         | 140U-D6D3-C25 140UT-D7D3-C25 | 140U-D6D3-C30 140UT-D7D3-C30 | —                         | —                         |
| 2198-H040-ERSx                | 240/480V 35 —                                              |                                                         | —                            | —                            | —                         | —                         |
| 2198-H070-ERSx                | 240/480V 63 —                                              |                                                         | 140G-G6C3-C60 —              |                              |                           |                           |

## Shared AC/DC and Hybrid Systems

Input Power UL Circuit-protection Specifications

| Kinetix 5500 Drive Cat. No.   | Drive Voltage, (three-phase) nom   |                                       |    |          |                                                         | Molded Case CB Cat. No.      | Molded Case CB Cat. No.      | Molded Case CB Cat. No.   | Molded Case CB Cat. No.                   | Molded Case CB Cat. No.   | Molded Case CB Cat. No.   | Molded Case CB Cat. No.   | Molded Case CB Cat. No.   |
|-------------------------------|------------------------------------|---------------------------------------|----|----------|---------------------------------------------------------|------------------------------|------------------------------|---------------------------|-------------------------------------------|---------------------------|---------------------------|---------------------------|---------------------------|
| Kinetix 5500 Drive Cat. No.   | Drive Voltage, (three-phase) nom   |                                       |    |          | 2 Axes 3 Axes 4 Axes 5 Axes 6 Axes 7 Axes 8 Axes 2 Axes |                              |                              |                           | 3 Axes 4 Axes 5 Axes 6 Axes 7 Axes 8 Axes |                           |                           |                           |                           |
| 2198-H003-ERSx                | 240/480V KTK-R-10                  |                                       |    |          | KTK-R-15 —                                              | KTK-R-15 —                   |                              |                           |                                           |                           |                           |                           |                           |
| 2198-H008-ERSx                | 240/480V KTK-R-15                  |                                       |    | KTK-R-20 | KTK-R-20                                                | —                            | —                            | —                         | —                                         | —                         | —                         | —                         | —                         |
| 2198-H015-ERSx                | 240/480V KTK-R-20                  |                                       | —  | —        | —                                                       | 140U-D6D3-C15 140UT-D7D3-C15 | 140U-D6D3-C20 140UT-D7D3-C20 | —                         | —                                         | —                         | —                         | —                         |                           |
| 2198-H025-ERSx                | 240/480V KTK-R-30                  |                                       | —  | —        | —                                                       | 140U-D6D3-C20 140UT-D7D3-C20 | 140U-D6D3-C30 140UT-D7D3-C30 | —                         | —                                         | —                         | —                         | —                         |                           |
| 2198-H040-ERSx                |                                    | 240/480V KTK-R-30 LPJ-45SP LPJ-50SP — |    |          |                                                         | 140U-D6D3-C30 140UT-D7D3-C30 | —                            | —                         | —                                         | —                         | —                         | —                         | —                         |
| 2198-H070-ERSx                | 240/480V LPJ-50SP —                |                                       |    |          |                                                         | 140G-G6C3-C50 —              |                              |                           |                                           |                           |                           |                           |                           |

## Input Power IEC (non-UL) Circuit-protection Specifications

| Kinetix 5500 Drives Cat. No.   | Drive Voltage, (three-phase) nom   |    |                                                                                                   |    | Molded Case CB Cat. No.      | Molded Case CB Cat. No.      | Molded Case CB Cat. No.   | Molded Case CB Cat. No.   | Molded Case CB Cat. No.   | Molded Case CB Cat. No.   | Molded Case CB Cat. No.   | Molded Case CB Cat. No.   |
|--------------------------------|------------------------------------|----|---------------------------------------------------------------------------------------------------|----|------------------------------|------------------------------|---------------------------|---------------------------|---------------------------|---------------------------|---------------------------|---------------------------|
| Kinetix 5500 Drives Cat. No.   | Drive Voltage, (three-phase) nom   |    | 2 Axes 3 Axes 4 Axes 5 Axes 6 Axes 7 Axes 8 Axes 2 Axes 3 Axes 4 Axes 5 Axes 6 Axes 7 Axes 8 Axes |    |                              |                              |                           |                           |                           |                           |                           |                           |
| 2198-H003-ERSx                 | 240/480V 10                        |    |                                                                                                   | 16 | —                            |                              |                           |                           |                           |                           |                           |                           |
| 2198-H008-ERSx                 | 240/480V 16                        |    | —                                                                                                 |    | —                            |                              |                           |                           |                           |                           |                           |                           |
| 2198-H015-ERSx                 | 240/480V 20                        | —  |                                                                                                   |    | 140U-D6D3-C15 140UT-D7D3-C15 | 140U-D6D3-C20 140UT-D7D3-C20 | —                         |                           |                           |                           |                           |                           |
| 2198-H025-ERSx                 | 240/480V 32                        | —  |                                                                                                   |    | 140U-D6D3-C20 140UT-D7D3-C20 | 140U-D6D3-C30 140UT-D7D3-C30 | —                         |                           |                           |                           |                           |                           |
| 2198-H040-ERSx                 | 240/480V 32 —                      |    |                                                                                                   |    | 140U-D6D3-C30 140UT-D7D3-C30 | —                            |                           |                           |                           |                           |                           |                           |
| 2198-H070-ERSx                 | 240/480V 50 —                      |    |                                                                                                   |    | 140G-G6C3-C50 —              |                              |                           |                           |                           |                           |                           |                           |

## Motor Overload Protection

This servo drive uses solid-state motor overload protection that operates in accordance with UL requirements. Motor overload protection is provided by algorithms (thermal memory) that predict actual motor temperature that is based on operating conditions.

In addition to thermal memory protection, this drive provides an input for an external temperature sensor/thermistor device, embedded in the motor, to support the UL requirement for motor overload protection.

Servo drives using DSL (digital servo link) encoder technology require the encoder to perform motor temperature monitoring and transmit the data over the single motor cable. Kinetix VP motors use DSL technology that performs this function. No additional wiring is required.

Some motors supported by this drive (firmware revision 3.001 or earlier) do not contain temperature sensors/thermistors; therefore, motor overload protection against excessive consecutive motor overloads with power cycling is not supported. Beginning with firmware revision 4.001 (and later) thermal retention is supported regardless of the motor or encoder type in use.

This servo drive meets the following UL requirements for solid-state overload protection.

| Motor Overload Protection Trip Point   | Value         |
|----------------------------------------|---------------|
| Ultimately                             | 100% overload |
| Within 8 minutes                       | 200% overload |
| Within 20 seconds                      | 600% overload |

<!-- image -->

ATTENTION: To avoid damage to your motor due to overheating caused by excessive, successive motor overload trips, follow the wiring diagram provided in the user manual for your motor and drive combination.

Refer to your servo drive user manual for the interconnect diagram that illustrates the wiring between your motor and drive.

## Additional Resources

These documents contain additional information concerning related products from Rockwell Automation. You can view or download publications at rok.auto/literature .

| Resource                                                                                                                             | Description                                                                                                                                                     |
|--------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Kinetix 5500 Servo Drives User Manual, publication 2198-UM001                                                                        | Information on installing, configuring, starting, and troubleshooting your Kinetix 5500 servo drive system.                                                     |
| Kinetix Rotary Motion Specifications, publication KNX-TD001                                                                          | Product specifications for Kinetix VPL, VPC, VPF, VPH, and VPS; Kinetix MPL, MPM, MPF, and MPS; Kinetix TLY and TL; Kinetix MMA; and Kinetix HPK rotary motors. |
| Kinetix Linear Motion Specifications Technical Data, publication KNX-TD002                                                           | Product specifications for Kinetix MPAS and MPMA linear stages, Kinetix MPAR and MPAI electric cylinders, and Kinetix LDC and LDL linear motors.                |
| Kinetix 5700, 5500, 5300, and 5100 Servo Drives Specifications, publication KNX-TD003                                                | Provides product specifications for Kinetix Integrated Motion over the EtherNet/IP network and EtherNet/IP networking servo drive families.                     |
| Kinetix Rotary and Linear Motion Cable Specifications Technical Data, publication KNX-TD004                                          | Product specifications for Kinetix 2090 motor and interface cables.                                                                                             |
| Kinetix Servo Drive Performance Specifications per Ecodesign Regulation (EU) 2019/1781 and UK SI 2021 No. 745, publication KNX-TD006 | Provides specifications per EU and UK Ecodesign, including efficiency class.                                                                                    |
| Kinetix 5500 Feedback Connector Kit Installation Instructions, publication 2198-IN002                                                | Information on installing and wiring the Kinetix 5500 motor feedback connector kit.                                                                             |
| Kinetix 5000 AC Line Filter Installation Instructions, publication 2198-IN003                                                        | Information on installing and wiring the Kinetix 5500 AC line filters.                                                                                          |
| Hiperface-to-DSL Feedback Converter Kit Installation Instructions, publication 2198-IN006                                            | Information on installing and wiring the Hiperface-to-DSL feedback converter kit.                                                                               |
| Kinetix 300 Shunt Resistor Installation Instructions, publication 2097-IN002                                                         | Information on installing and wiring these external shunt resistors for your Kinetix 5500 servo drives.                                                         |
| Industrial Automation Wiring and Grounding Guidelines, publication 1770-4.1                                                          | Provides general guidelines for installing a Rockwell Automation industrial system.                                                                             |
| Product Certifications website: rok.auto/certifications                                                                              | Provides declarations of conformity, certificates, and other certification details.                                                                             |

## Rockwell Automation Support

Use these resources to access support information.

| Technical Support Center                         | Find help with how-to videos, FAQs, chat, user forums, Knowledgebase, and product notification updates.               | rok.auto/support   |
|--------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|--------------------|
| Local Technical Support Phone Numbers            | Locate the telephone number for your country.  rok.auto/phonesupport                                                  |                    |
| Technical Documentation Center                   | Quickly access and download technical specifications, installation instructions, and user manuals.  rok.auto/techdocs |                    |
| Literature Library                               | Find installation instructions, manuals, brochures, and technical data publications.  rok.auto/literature             |                    |
| Product Compatibility and Download Center (PCDC) | Download firmware, associated files (such as AOP, EDS, and DTM), and access product release notes.                    | rok.auto/pcdc      |

## Documentation Feedback

Your comments help us serve your documentation needs better. If you have any suggestions on how to improve our content, complete the form at rok.auto/docfeedback .

## Waste Electrical and Electronic Equipment (WEEE)

<!-- image -->

At the end of life, this equipment should be collected separately from any unsorted municipal waste.

Rockwell Automation maintains current product environmental compliance information on its website at rok.auto/pec .

Rockwell Otomasyon Ticaret A.Ş. Kar Plaza İş Merkezi E Blok Kat:6 34752 İçerenköy, İstanbul, Tel: +90 (216) 5698400 EEE Yönetmeliğine Uygundur

Connectwithus.

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

rockwellautomation.com expandinghumanpossibility°

AMERICAS:RockwellAutomation,1201SouthSec0ndStreet,Milwaukee,W153204-2496USA,Tel:(1)414.382.2000,Fax:（1)414.382.4444 EUR0PE/MIDDLEEAST/AFRICA:RockwellAutomationNV,PegasusPark,DeKleetlaan12a,1831Diegem,Belgium,Tel:(32)26630600,Fax:(32)26630640 ASIAPACIFIC:RockwellAutomationSEAPteLtd,2CorporationRoad,#04-05,MainLobby,CorporationPlace,Singapore618494,Tel:（65）65106608,FAX:(65）65106699 UNITEDKINGD0M:RockwellAutomationLtd.,Pitfield,KilnFarm,MiltonKeynes,MK113DR,UnitedKingdom,Tel:(44)（1908)838-800,Fax:(44)（1908)261-917

Allen-Bradley, CompactLogix, ControlLogix, expanding human possibility, GuardLogix, Kinetix, and Rockwell Automation are trademarks of Rockwell Automation, Inc.

EtherNet/IP is a trademark of ODVA, Inc.

Trademarks not belonging to Rockwell Automation are property of their respective companies.

<!-- image -->

<!-- image -->