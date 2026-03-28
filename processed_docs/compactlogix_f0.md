## Technical Data

Original Instructions

## CompactLogix Controllers Specifications

Bulletins 1769 and 1768

| Topic Page                                                     |
|----------------------------------------------------------------|
| Summary of Changes 2                                           |
| Catalog Numbers 2                                              |
| CompactLogix 5370 Controllers 3                                |
| Armor CompactLogix and Armor Compact GuardLogix Controllers 25 |
| 1769 Packaged CompactLogix Controllers with Embedded I/O 29    |
| 1769 Modular CompactLogix Controllers 35                       |
| 1768 CompactLogix Controllers 38                               |
| Controller Memory Use 41                                       |
| Controller Compatibility 41                                    |
| Controller Connections 43                                      |
| CompactLogix Controller Accessories 45                         |
| Additional Resources 47                                        |

<!-- image -->

<!-- image -->

<!-- image -->

## Summary of Changes

This publication contains the following new or updated information. This list includes substantive updates only and is not intended to reflect all changes.

|                                                                                                                                                             | Topic Pages   |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------|
| Removed EAC certification for CompactLogix™ 5370 and Compact GuardLogix® 5370 Controllers, and Armor™ CompactLogix and Armor Compact GuardLogix Controllers | 5, 26         |

## Catalog Numbers

This publication is applicable to the following catalog numbers.

CompactLogix 5370 and Compact GuardLogix 5370 Controllers

1769-L16ER-BB1B, 1769-L18ER-BB1B, 1769-L18ERM-BB1B, 1769-L18ERM-BB1BK, 1769-L19ER-BB1B, 1769-L19ER-BB1BK, 1769-L24ER-QB1B, 1769-L24ER-QBFC1B, 1769-L24ER-QBFC1BK, 1769-L27ERM-QBFC1B, 1769-L30ER, 1769-L30ER-NSE, 1769-L30ERK, 1769-L30ERM, 1769-L30ERMK, 1769-L30ERMS, 1769-L33ER, 1769-L33ERK, 1769-L33ERM, 1769-L33ERMK, 1769-L33ERMS, 1769-L33ERMSK, 1769-L36ERM, 1769-L36ERMS, 1769-L37ERM, 1769-L37ERMK, 1769-L37ERMS, 1769-L37ERMSK, 1769-L38ERM, 1769-L38ERMK, 1769-L38ERMS, 1769-L38ERMSK

Armor CompactLogix and Armor Compact GuardLogix Controllers

1769-L33ERMO, 1769-L33ERMOS, 1769-L36ERMO, 1769-L36ERMOS, 1769-L37ERMO, 1769-L37ERMOS, 1769-L38ERMO, 1769-L38ERMOS

1769 Packaged Controllers

1769-L23-QBFC1B, 1769-L23E-QB1B, 1769-L23E-QBFC1B

1769 Modular Controllers

1769-L31, 1769-L32C, 1769-L35CR, 1769-L32E, 1769-L32EK, 1769-L35E

1768 Controllers

1768-L43, 1768-L43S, 1768-L45, 1768-L45S

Memory Cards

1784-CF128, 1784-SD1, 1784-SD2

## CompactLogix 5370 Controllers

## CompactLogix 5370 L1 Control System

<!-- image -->

## CompactLogix 5370 L2 Control System

<!-- image -->

## CompactLogix 5370 L3 Control System

<!-- image -->

CompactLogix 5370 controllers provide scalable controller solutions to address a wide variety of applications. All CompactLogix 5370 controllers provide the following functionality:

- Two Ethernet ports
- One USB port
- Support for local expansion modules
- Control of local and distributed I/O modules
- Use of 1784-SD1 or 1784-SD2 Secure Digital (SD) card for nonvolatile memory
- A battery is no longer necessary because of the internal energy-storage solution

Some CompactLogix 5370 controllers provide the following functionality:

- Built-in power supply
- Some combination of embedded digital, analog, and highspeed counter modules
- Support for Integrated Motion over an EtherNet/IP™ network
- Access to DeviceNet® networks

## Compact GuardLogix 5370 Control System

<!-- image -->

The Compact GuardLogix controller is a 1769-L3 CompactLogix controller that provides safety control to achieve SIL CL 3 according to EN62061 / EN 61511-1 / IEC 61508 and PLe according to EN ISO 13849-1. A major benefit of this system is that it's still one project; safety and standard control together.

|             | Application Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SIL 1, 2, 3 | The Compact GuardLogix controller system is type-approved and certified for use in safety applications up to and including SIL 3 according to IEC 61508, and applications up to and including PLe/Cat.4 according to ISO 13849-1. For more information, see these manuals: • GuardLogix 5570 and Compact GuardLogix 5370 Controllers Systems Safety Reference Manual, publication 1756-RM099 • Compact GuardLogix 5370 Controllers User Manual, publication 1769-UM002 • GuardLogix Safety Application Instruction Set Reference Manual, publication 1756-RM095 |

During development, safety and standard have the same rules. The following are allowed:

- Multiple programmers
- Online editing
- Forcing

Once the project is tested and ready for final validation, apply the safety application signature and safety-lock the application. This process sets the safety task to a SIL 3 integrity level. The Compact GuardLogix controller enforces the SIL 3 integrity level. When safety memory is locked and protected, the safety logic can't be modified and all safety functions operate with SIL 3 integrity. On the standard side of the Compact GuardLogix controller, all functions operate like a regular Logix controller. Thus online editing, forcing, and other activities are all allowed.

Standard logic and external devices, like HMIs or other controllers, can read safety memory with this level of integration. This level of integration removes the need to condition safety memory for use elsewhere. The result is easy systemwide integration and the ability to display safety status on displays or marquees. Use Guard I/O™ modules for field device connectivity. For safety interlocking between Compact GuardLogix controllers, use Ethernet or ControlNet® networks. Multiple Compact GuardLogix controllers can share safety data for zone to zone interlocking, or one Compact GuardLogix controller can use remote distributed safety I/O between different cells/areas.

## Features - CompactLogix 5370 Controllers and Compact GuardLogix 5370 Controllers

| Feature                                        | 1769-L16ER-BB1B 1769-L18ER-BB1B 1769-L18ERM-BB1B, 1769-L18ERM-BB1BK 1769-L19ER-BB1B, 1769-L19ER-BB1BK                                                                                                                                                                      | 1769-L24ER-QB1B 1769-L24ER-QBFC1B, 1769-L24ER-QBFC1BK 1769-L27ERM-QBFC1B                                                                                                                                                                                                   | 1769-L30ER, 1769-L30ERK 1769-L30ER-NSE 1769-L30ERM, 1769-L30ERMK 1769-L33ER, 1769-L33ERK 1769-L33ERM, 1769-L33ERMK, 1769-L36ERM, 1769-L37ERM, 1769-L37ERMK, 1769-L38ERM, 1769-L38ERMK                                                                                                                                                                                                             | 1769-L30ERMS 1769-L33ERMS, 1769-L33ERMSK 1769-L36ERMS 1769-L37ERMS, 1769-L37ERMSK 1769-L38ERMS, 1769-L38ERMSK                                                                                                                                                                                                                                                                                     |
|------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Controller tasks Continuous Periodic           | 32 tasks 100 programs/task                                                                                                                                                                                                                                                 |                                                                                                                                                                                                                                                                            |                                                                                                                                                                                                                                                                                                                                                                                                   |                                                                                                                                                                                                                                                                                                                                                                                                   |
| Built-in communication ports                   | • Two Ethernet ports - CompactLogix 5370 controllers have two Ethernet ports. The ports carry the same network traffic as part of the embedded switch of the controller. However, the controller uses only one IP address. • One USB port (only for temporary connection). | • Two Ethernet ports - CompactLogix 5370 controllers have two Ethernet ports. The ports carry the same network traffic as part of the embedded switch of the controller. However, the controller uses only one IP address. • One USB port (only for temporary connection). | • Two Ethernet ports - CompactLogix 5370 controllers have two Ethernet ports. The ports carry the same network traffic as part of the embedded switch of the controller. However, the controller uses only one IP address. • One USB port (only for temporary connection).                                                                                                                        | • Two Ethernet ports - CompactLogix 5370 controllers have two Ethernet ports. The ports carry the same network traffic as part of the embedded switch of the controller. However, the controller uses only one IP address. • One USB port (only for temporary connection).                                                                                                                        |
| Communication options                          | EtherNet/IP                                                                                                                                                                                                                                                                | • EtherNet/IP • DeviceNet via 1769-SDN scanner                                                                                                                                                                                                                             | • EtherNet/IP • DeviceNet via 1769-SDN scanner                                                                                                                                                                                                                                                                                                                                                    | • EtherNet/IP • DeviceNet via 1769-SDN scanner                                                                                                                                                                                                                                                                                                                                                    |
| EtherNet/IP node, max                          | • 1769-L16ER-BB1B: Up to 4 nodes • 1769-L18ER-BB1B, 1769-L18ERM-BB1B, 1769-L18ERM-BB1BK, 1769-L19ER-BB1B, 1769-L19ER-BB1BK: Up to 8 nodes                                                                                                                                  | • 1769-L24ER-QB1B, 1769-L24ER-QBFC1B, 1769-L24ER-QBFC1BK: Up to 8 nodes • 1769-L27ERM-QBFC1B: Up to 16 nodes                                                                                                                                                               | • 1769-L30ER, 1769-L30ER-NSE, 1769-L30ERK, 1769-L30ERM, 769-L30ERMK, 1769-L30ERMS: Up to 16 nodes • 1769-L33ER, 1769-L33ERK, 1769-L33ERM, 1769-L33ERMK, 1769-L33ERMS, 1769-L33ERMSK: Up to 32 nodes • 1769-L36ERM, 1769-L36ERMS: Up to 48 nodes • 1769-L37ERM, 1769-L37ERMK, 1769-L37ERMS, 1769-L37ERMSK: Up to 64 nodes • 1769-L38ERM, 1769-L38ERMK, 1769-L38ERMS, 1769-L38ERMSK: Up to 80 nodes | • 1769-L30ER, 1769-L30ER-NSE, 1769-L30ERK, 1769-L30ERM, 769-L30ERMK, 1769-L30ERMS: Up to 16 nodes • 1769-L33ER, 1769-L33ERK, 1769-L33ERM, 1769-L33ERMK, 1769-L33ERMS, 1769-L33ERMSK: Up to 32 nodes • 1769-L36ERM, 1769-L36ERMS: Up to 48 nodes • 1769-L37ERM, 1769-L37ERMK, 1769-L37ERMS, 1769-L37ERMSK: Up to 64 nodes • 1769-L38ERM, 1769-L38ERMK, 1769-L38ERMS, 1769-L38ERMSK: Up to 80 nodes |
| Controller connections                         | 256                                                                                                                                                                                                                                                                        | 256                                                                                                                                                                                                                                                                        | 256                                                                                                                                                                                                                                                                                                                                                                                               | 256                                                                                                                                                                                                                                                                                                                                                                                               |
| Embedded I/O modules                           | • 16 DC digital inputs • 16 DC digital outputs                                                                                                                                                                                                                             | All controllers: • 16 DC digital inputs • 16 DC digital outputs Only 1769-L24ER-QBFC1B, 1769-L24ER-QBFC1BK, and 1769-L27ERM-QBFC1B: • 4 high-speed counter modules • 4 high-speed counter module outputs • 4 universal analog inputs • 2 analog output points              | –                                                                                                                                                                                                                                                                                                                                                                                                 | –                                                                                                                                                                                                                                                                                                                                                                                                 |
| Sockets, max 32                                |                                                                                                                                                                                                                                                                            |                                                                                                                                                                                                                                                                            |                                                                                                                                                                                                                                                                                                                                                                                                   |                                                                                                                                                                                                                                                                                                                                                                                                   |
| Integrated Motion over an EtherNet/ IP network | 1769-L18ERM-BB1B, 1769-L18ERM-BB1BK: 1 or 2 axes                                                                                                                                                                                                                           | 1769-L27ERM-QBFC1B - As many as 4 axes                                                                                                                                                                                                                                     | • 1769-L30ERM, 1769-L30ERMK, 1769-L30ERMS: As many as 4 axes • 1769-L33ERM, 1769-L33ERMK, 1769-L33ERMS, 1769-L33ERMSK: As many as 8 axes • 1769-L36ERM, 1769-L36ERMS: As many as 16 axes • 1769-L37ERM, 1769-L37ERMK, 1769-L37ERMS, 1769-L37ERMSK: As many as 16 axes • 1769-L38ERM, 1769-L38ERMK, 1769-L38ERMS, 1769-L38ERMSK: As many as 16 axes                                                | • 1769-L30ERM, 1769-L30ERMK, 1769-L30ERMS: As many as 4 axes • 1769-L33ERM, 1769-L33ERMK, 1769-L33ERMS, 1769-L33ERMSK: As many as 8 axes • 1769-L36ERM, 1769-L36ERMS: As many as 16 axes • 1769-L37ERM, 1769-L37ERMK, 1769-L37ERMS, 1769-L37ERMSK: As many as 16 axes • 1769-L38ERM, 1769-L38ERMK, 1769-L38ERMS, 1769-L38ERMSK: As many as 16 axes                                                |
| Programming languages                          | • Relay ladder (1) • Structured Text • Function block • SFC                                                                                                                                                                                                                | • Relay ladder (1) • Structured Text • Function block • SFC                                                                                                                                                                                                                | • Relay ladder (1) • Structured Text • Function block • SFC                                                                                                                                                                                                                                                                                                                                       | • Relay ladder (1) • Structured Text • Function block • SFC                                                                                                                                                                                                                                                                                                                                       |
| Integrated safety –                            |                                                                                                                                                                                                                                                                            |                                                                                                                                                                                                                                                                            |                                                                                                                                                                                                                                                                                                                                                                                                   | Yes                                                                                                                                                                                                                                                                                                                                                                                               |

## Certifications - CompactLogix 5370 Controllers and Compact GuardLogix 5370 Controllers

| Certification(1)   | 1769-L16ER-BB1B 1769-L18ER-BB1B 1769-L18ERM-BB1B, 1769-L18ERM-BB1BK 1769-L19ER-BB1B, 1769-L19ER-BB1BK                                                                                                                                                                                       | 1769-L24ER-QB1B 1769-L24ER-QBFC1B, 1769-L24ER-QBFC1BK 1769-L27ERM-QBFC1B                                                                                                                                                                                                                    | 1769-L30ER, 1769-L30ERK 1769-L30ER-NSE 1769-L30ERM, 1769-L30ERMK 1769-L33ER, 1769-L33ERK 1769-L33ERM, 1769-L33ERMK 1769-L36ERM 1769-L37ERM, 1769-L37ERMK 1769-L38ERM, 1769-L38ERMK                                                   | 1769-L30ERMS 1769-L33ERMS, 1769-L33ERMSK 1769-L36ERMS 1769-L37ERMS, 1769-L37ERMSK 1769-L38ERMS, 1769-L38ERMSK                                                                                                                                                                                                                                                                                                                                                                                                             |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| c-UL-us            | UL Listed Industrial Control Equipment, certified for US and Canada. See UL File E65584. UL Listed for Class I, Division 2 Group A,B,C,D Hazardous Locations, certified for U.S. and Canada. See UL File E194810.                                                                           | UL Listed Industrial Control Equipment, certified for US and Canada. See UL File E322657. UL Listed for Class I, Division 2 Group A,B,C,D Hazardous Locations, certified for U.S. and Canada. See UL File E334470.                                                                          | UL Listed Industrial Control Equipment, certified for US and Canada. See UL File E65584. UL Listed for Class I, Division 2 Group A,B,C,D Hazardous Locations, certified for U.S. and Canada. See UL File E194810.                    | UL Listed Industrial Control Equipment, certified for US and Canada. See UL File E65584. UL Listed for Class I, Division 2 Group A,B,C,D Hazardous Locations, certified for U.S. and Canada. See UL File E194810.                                                                                                                                                                                                                                                                                                         |
| UKCA and CE        | UK Statutory Instrument 2016 No. 1091 and European Union 2014/30/EU EMC Directive, compliant with: EN 61131-2; Programmable Controllers (Clause 8, Zone A & B) EN 61326-1; Meas./Control/Lab., Industrial Requirements EN 61000-6-4; Industrial Emissions EN 61000-6-2; Industrial Immunity | UK Statutory Instrument 2016 No. 1091 and European Union 2014/30/EU EMC Directive, compliant with: EN 61131-2; Programmable Controllers (Clause 8, Zone A & B) EN 61326-1; Meas./Control/Lab., Industrial Requirements EN 61000-6-4; Industrial Emissions EN 61000-6-2; Industrial Immunity | UK Statutory Instrument 2016 No. 1091 and European Union 2014/30/ EU EMC Directive, compliant with: EN 61131-2; Programmable Controllers (Clause 8, Zone A & B) EN 61000-6-4; Industrial Emissions EN 61000-6-2; Industrial Immunity | UK Statutory Instrument 2016 No. 1091 and European Union 2014/30/EU EMC Directive, compliant with: EN 61131-2; Programmable Controllers (Clause 8, Zone A & B) EN 61326-3-1; Meas./Control/Lab., Immunity Requirements for safety systems and functions EN 61000-6-4; Industrial Emissions EN 61000-6-2; Industrial Immunity UK Statutory Instrument 2008 No. 1597 and European Union 2006/42/EC MD Directive, compliant with: EN 61508-1…7; General requirements EN ISO 13849-1; Safety-related parts of control systems |
| UKCA and CE        | UK Statutory Instrument 2012 No. 3032 and European Union 2011/65/EU RoHS Directive, compliant with: EN IEC 63000; Technical documentation                                                                                                                                                   | UK Statutory Instrument 2012 No. 3032 and European Union 2011/65/EU RoHS Directive, compliant with: EN IEC 63000; Technical documentation                                                                                                                                                   | UK Statutory Instrument 2012 No. 3032 and European Union 2011/65/EU RoHS Directive, compliant with: EN IEC 63000; Technical documentation                                                                                            | UK Statutory Instrument 2012 No. 3032 and European Union 2011/65/EU RoHS Directive, compliant with: EN IEC 63000; Technical documentation                                                                                                                                                                                                                                                                                                                                                                                 |
| RCM                | Australian Radiocommunications Act, compliant with: EN 61000-6-4; Industrial Emissions                                                                                                                                                                                                      | Australian Radiocommunications Act, compliant with: EN 61000-6-4; Industrial Emissions                                                                                                                                                                                                      | Australian Radiocommunications Act, compliant with: EN 61000-6-4; Industrial Emissions                                                                                                                                               | Australian Radiocommunications Act, compliant with: EN 61000-6-4; Industrial Emissions                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| IECEx —            |                                                                                                                                                                                                                                                                                             | IECEx System, compliant with: IEC 60079-0; General Requirements IEC 60079-7; Explosive Atmospheres, Protection “e” II 3 G Ex ec IIC T4 Gc IECEx UL 21.0112X                                                                                                                                 | —                                                                                                                                                                                                                                    | —                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| IECEx —            | European Union 2014/34/EU ATEX Directive, compliant with: EN 60079-0; General Requirements EN 60079-15; Potentially Explosive Atmospheres, Protection "n"                                                                                                                                   | European Union 2014/34/EU ATEX Directive, compliant with: EN 60079-0; General Requirements EN 60079-15; Potentially Explosive Atmospheres, Protection "n"                                                                                                                                   | European Union 2014/34/EU ATEX Directive, compliant with: EN 60079-0; General Requirements EN 60079-15; Potentially Explosive Atmospheres, Protection "n"                                                                            | –                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| IECEx —            | II 3 G Ex nA IIC T4 Gc ITS 12 ATEX 47611X (until Rev. 3)                                                                                                                                                                                                                                    | II 3 G Ex nA IIC T4 Gc DEMKO 12 ATEX 1116807X (until Rev. 3)                                                                                                                                                                                                                                | II 3 G Ex nA IIC T4 Gc ITS 09 ATEX 46118X (until Rev. 6)                                                                                                                                                                             | –                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| IECEx —            | Or                                                                                                                                                                                                                                                                                          | Or                                                                                                                                                                                                                                                                                          | Or                                                                                                                                                                                                                                   | Or                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| IECEx —            | UK Statutory Instrument 2016 No. 1107 and European Union 2014/34/EU ATEX Directive, compliant with: EN 60079-0; General Requirements EN 60079-7; Potentially Explosive Atmospheres, Protection “e”                                                                                          | UK Statutory Instrument 2016 No. 1107 and European Union 2014/34/EU ATEX Directive, compliant with: EN 60079-0; General Requirements EN 60079-7; Potentially Explosive Atmospheres, Protection “e”                                                                                          | UK Statutory Instrument 2016 No. 1107 and European Union 2014/34/EU ATEX Directive, compliant with: EN 60079-0; General Requirements EN 60079-7; Potentially Explosive Atmospheres, Protection “e”                                   | UK Statutory Instrument 2016 No. 1107 and European Union 2014/34/EU ATEX Directive, compliant with: EN 60079-0; General Requirements EN 60079-7; Potentially Explosive Atmospheres, Protection “e”                                                                                                                                                                                                                                                                                                                        |
| IECEx —            | II 3 G Ex ec IIC T4 Gc UL 21 ATEX 2603X (from Rev. 1) UL 22 UKEX 2515X (from Rev. 0)                                                                                                                                                                                                        | II 3 G Ex ec IIC T4 Gc DEMKO 12 ATEX 1116807X (from Rev. 4) UL 22 UKEX 2516X (from Rev. 0)                                                                                                                                                                                                  | II 3 G Ex ec IIC T5 Gc UL 21 ATEX 2603X (from Rev. 0) UL 22 UKEX 2515X (from Rev. 0)                                                                                                                                                 | II 3 G Ex ec IIC T5 Gc DEMKO 15 ATEX 1388X UL 22 UKEX 2514X (from Rev. 0)                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| TÜV —              |                                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                      | TÜV Certified for Functional Safety Capable of SIL 3                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                    | Morocco Arrêté ministériel n° 6404-15 du 29 ramadan 1436                                                                                                                                                                                                                                    | Morocco Arrêté ministériel n° 6404-15 du 29 ramadan 1436                                                                                                                                                                                                                                    | Morocco Arrêté ministériel n° 6404-15 du 29 ramadan 1436                                                                                                                                                                             | Morocco Arrêté ministériel n° 6404-15 du 29 ramadan 1436                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| CCC                | CNCA-C23-01:2019 䔂ⵖ䚍❡ㅷ雩霆㹊倶錞ⴭ ꣈旘歏孞 CNCA-C23-01:2019 CCC Implementation Rule Explosion-Proof Electrical Products CCC: 2020122309111609, 2021122309113974, 2021312309000565                                                                                                         | CNCA-C23-01:2019 䔂ⵖ䚍❡ㅷ雩霆㹊倶錞ⴭ ꣈旘歏孞 CNCA-C23-01:2019 CCC Implementation Rule Explosion-Proof Electrical Products CCC: 2020122309111609, 2021122309113974, 2021312309000565                                                                                                         | CNCA-C23-01:2019 䔂ⵖ䚍❡ㅷ雩霆㹊倶錞ⴭ ꣈旘歏孞 CNCA-C23-01:2019 CCC Implementation Rule Explosion-Proof Electrical Products CCC: 2020122309111609, 2021122309113974, 2021312309000565                                                  | CNCA-C23-01:2019 䔂ⵖ䚍❡ㅷ雩霆㹊倶錞ⴭ ꣈旘歏孞 CNCA-C23-01:2019 CCC Implementation Rule Explosion-Proof Electrical Products CCC: 2020122309111609, 2021122309113974, 2021312309000565                                                                                                                                                                                                                                                                                                                                       |
| KC                 | Korean Registration of Broadcasting and Communications Equipment, compliant with: Article 58-2 of Radio Waves Act, Clause 3                                                                                                                                                                 | Korean Registration of Broadcasting and Communications Equipment, compliant with: Article 58-2 of Radio Waves Act, Clause 3                                                                                                                                                                 | Korean Registration of Broadcasting and Communications Equipment, compliant with: Article 58-2 of Radio Waves Act, Clause 3                                                                                                          | Korean Registration of Broadcasting and Communications Equipment, compliant with: Article 58-2 of Radio Waves Act, Clause 3                                                                                                                                                                                                                                                                                                                                                                                               |
|                    | EtherNet/IP ODVA conformance tested to EtherNet/IP specifications.                                                                                                                                                                                                                          | EtherNet/IP ODVA conformance tested to EtherNet/IP specifications.                                                                                                                                                                                                                          | EtherNet/IP ODVA conformance tested to EtherNet/IP specifications.                                                                                                                                                                   | EtherNet/IP ODVA conformance tested to EtherNet/IP specifications.                                                                                                                                                                                                                                                                                                                                                                                                                                                        |

## Environmental Specifications - CompactLogix 5370 Controllers and Compact GuardLogix 5370 Controllers

| Attribute                                                                                                                                                                  | 1769-L16ER-BB1B 1769-L18ER-BB1B 1769-L18ERM-BB1B, 1769-L18ERM-BB1BK 1769-L19ER-BB1B, 1769-L19ER-BB1BK                                                                     | 1769-L24ER-QB1B 1769-L24ER-QBFC1B, 1769-L24ER-QBFC1BK 1769-L27ERM-QBFC1B                                                                                                                                          | 1769-L30ER, 1769-L30ERK 1769-L30ER-NSE 1769-L30ERM, 1769-L30ERMK 1769-L33ER, 1769-L33ERK 1769-L33ERM, 1769-L33ERMK 1769-L36ERM, 1769-L37ERM, 1769-L37ERMK 1769-L38ERM, 1769-L38ERMK   | 1769-L30ERMS 1769-L33ERMS, 1769-L33ERMSK 1769-L36ERMS 1769-L37ERMS, 1769-L37ERMSK 1769-L38ERMS, 1769-L38ERMSK   | 1769-L23-QBFC1B 1769-L23E-QB1B 1769-L23E-QBFC1B                                                                                                                                                        |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Temperature, operating IEC 60068-2-1 (Test Ad, Operating Cold), IEC 60068-2-2 (Test Bd, Operating Dry Heat), IEC 60068-2-14 (Test Na, Operating Thermal Shock)             | -20…+60 °C (-4…+140 °F)                                                                                                                                                   | 0…60 °C (32…140 °F)                                                                                                                                                                                               | 0…60 °C (32…140 °F)                                                                                                                                                                   | 0…60 °C (32…140 °F)                                                                                             | 0…60 °C (32…140 °F)                                                                                                                                                                                    |
| Temperature, storage IEC 60068-2-1 (Test Ab, Unpackaged Nonoperating Cold), IEC 60068-2-2 (Test Bb, Unpackaged Nonoperating Dry Heat), IEC 60068-2-14 (Test Na, Unpackaged | -40…+85 °C (-40…+185 °F)                                                                                                                                                  | -40…+85 °C (-40…+185 °F)                                                                                                                                                                                          | -40…+85 °C (-40…+185 °F)                                                                                                                                                              | -40…+85 °C (-40…+185 °F)                                                                                        | -40…+85 °C (-40…+185 °F)                                                                                                                                                                               |
| Temperature, surrounding air, max                                                                                                                                          | 60 °C (140 °F)                                                                                                                                                            | 60 °C (140 °F)                                                                                                                                                                                                    | 60 °C (140 °F)                                                                                                                                                                        | 60 °C (140 °F)                                                                                                  | 60 °C (140 °F)                                                                                                                                                                                         |
| Relative humidity IEC 60068-2-30 (Test Db, Unpackaged Damp Heat)                                                                                                           | 5…95% noncondensing                                                                                                                                                       | 5…95% noncondensing                                                                                                                                                                                               | 5…95% noncondensing                                                                                                                                                                   | 5…95% noncondensing                                                                                             | 5…95% noncondensing                                                                                                                                                                                    |
| Vibration IEC 60068-2-6 (Test Fc, Operating)                                                                                                                               | 2 g @ 10…500 Hz (1)                                                                                                                                                       | 2 g @ 10…500 Hz (1)                                                                                                                                                                                               | 5 g @ 10…500 Hz                                                                                                                                                                       | 5 g @ 10…500 Hz                                                                                                 | 5 g @ 10…500 Hz                                                                                                                                                                                        |
| Shock, operating IEC 60068-2-27 (Test Ea, Unpackaged Shock)                                                                                                                | 30 g (1)                                                                                                                                                                  | 30 g (1)                                                                                                                                                                                                          | 20 g - DIN rail 30 g - Panel                                                                                                                                                          | 20 g - DIN rail 30 g - Panel                                                                                    | 20 g - DIN rail 30 g - Panel                                                                                                                                                                           |
| Shock, nonoperating IEC 60068-2-27 (Test Ea, Unpackaged Shock)                                                                                                             | 50 g (1)(2)                                                                                                                                                               | 50 g (1)(2)                                                                                                                                                                                                       | 30 g - DIN rail 40 g - Panel                                                                                                                                                          | 30 g - DIN rail 40 g - Panel                                                                                    | 30 g - DIN rail 40 g - Panel                                                                                                                                                                           |
| Emissions CISPR 11                                                                                                                                                         | IEC 61000-6-4                                                                                                                                                             | IEC 61000-6-4                                                                                                                                                                                                     | IEC 61000-6-4                                                                                                                                                                         | IEC 61000-6-4                                                                                                   | IEC 61000-6-4                                                                                                                                                                                          |
| ESD immunity IEC 61000-4-2                                                                                                                                                 | 6 kV contact discharges 8 kV air discharges                                                                                                                               | 6 kV contact discharges 8 kV air discharges                                                                                                                                                                       | 6 kV contact discharges 8 kV air discharges                                                                                                                                           | 6 kV contact discharges 8 kV air discharges                                                                     | 4 kV contact discharges 8 kV air discharges                                                                                                                                                            |
| Radiated RF immunity IEC 61000-4-3                                                                                                                                         | 10V/m with 1 kHz sine wave 80% AM from 80…6000 MHz                                                                                                                        | 10V/m with 1 kHz sine wave 80% AM from 80…6000 MHz                                                                                                                                                                | 10V/m with 1 kHz sine wave 80% AM from 80…6000 MHz                                                                                                                                    | 10V/m with 1 kHz sine wave 80% AM from 80…6000 MHz                                                              | 10V/m with 200 Hz 50% Pulse 100% AM at 900 MHz 10V/m with 200 Hz 50% Pulse 100% AM at 1890 MHz 10V/m with 1 kHz sine wave 80% AM from 80…2000 MHz 10V/m with 1 kHz sine wave 80% AM from 2000…2700 MHz |
| EFT/B immunity IEC 61000-4-4                                                                                                                                               | ±3 kV at 5 kHz on power ports ±3 kV at 5 kHz on signal ports ±3 kV at 5 kHz on communication ports                                                                        | ±3 kV at 5 kHz on power ports ±3 kV at 5 kHz on signal ports ±3 kV at 5 kHz on communication ports                                                                                                                | ±3 kV at 5 kHz on communication ports                                                                                                                                                 | ±3 kV at 5 kHz on communication ports ±4 kV at 5 kHz on Protective Earth (PE)                                   | ±2 kV at 5 kHz on power ports ±2 kV at 5 kHz on signal ports ±2 kV at 5 kHz on communication ports                                                                                                     |
| Surge transient immunity IEC 61000-4-5                                                                                                                                     | ±1 kV line-line (DM) and ±2 kV line-earth (CM) on power ports ±1 kV line-line (DM) and ±2 kV line-earth (CM) on signal ports ±2 kV line-earth (CM) on communication ports | ±1 kV line-line (DM) and ±2 kV line-earth (CM) on power ports ±1 kV line-line (DM) and ±2 kV line-earth (CM) on signal ports ±2 kV line-earth (CM) on shielded ports ±2 kV line-earth (CM) on communication ports | ±2 kV line-earth (CM) on communication ports                                                                                                                                          | ±2 kV line-earth (CM) on communication ports                                                                    | ±1 kV line-line (DM) and ±2 kV line earth (CM) on power ports ±1 kV line-line (DM) and ±2 kV line earth (CM) on signal ports ±2 kV line-earth (CM) on shielded ports ±2 kV line-earth (CM) on communication ports                                                                                                                                                                                                        |
| Conducted RF immunity IEC 61000-4-6                                                                                                                                        | 10V rms with 1 kHz sine wave 80% AM from 150 kHz…80 MHz                                                                                                                   | 10V rms with 1 kHz sine wave 80% AM from 150 kHz…80 MHz                                                                                                                                                           | 10V rms with 1 kHz sine wave 80% AM from 150 kHz…80 MHz                                                                                                                               | 10V rms with 1 kHz sine wave 80% AM from 150 kHz…80 MHz                                                         | 10V rms with 1 kHz sine wave 80% AM from 150 kHz…80 MHz                                                                                                                                                |

## Technical Specifications - CompactLogix 5370 Controllers and Compact GuardLogix 5370 Controllers

## Attribute

## 1769-L16ER-BB1B 1769-L18ER-BB1B 1769-L18ERM-BB1B,1769-L18ERM-BB1BK 1769-L19ER-BB1B, 1769-L19ER-BB1BK

## 1769-L24ER-QB1B 1769-L24ER-QBFC1B, 1769-L24ER-QBFC1BK 1769-L27ERM-QBFC1B

1769-L30ER, 1769-L30ERK

- 1769-L30ER-NSE

- 1769-L30ERM, 1769-L30ERMK

- 1769-L33ER, 1769-L33ERK,

- 1769-L33ERM, 1769-L33ERMK

- 1769-L36ERM

- 1769-L37ERM, 1769-L37ERMK

1769-L38ERM, 1769-L38ERMK

1769-L30ERMS

1769-L33ERMS, 1769-L33ERMSK

1769-L36ERMS

1769-L37ERMS, 1769-L37ERMSK

1769-L38ERMS, 1769-L38ERMSK

User memory

- 1769-L16ER-BB1B: 384 KB

- 1769-L18ER-BB1B, 1769-L18ERM-BB1B, 1769-L18ERM-BB1BK: 512 KB

- 1769-L19ER-BB1B, 1769-L19ER-BB1BK: 1 MB

- 1769-L24ER-QB1B, 1769-L24ER-QBFC1B, 1769-L24ER-QBFC1BK: 750 KB

- 1769-L27ERM-QBFC1B: 1 MB

- 1769-L30ER, 1769-L30ER-NSE, 1769-L30ERK, 1769-L30ERM, 1769-L30ERM: 1 MB

- 1769-L33ER, 1769-L33ERK, 1769-L33ERM, 1769-L33ERM: 2 MB

- 1769-L36ERM: 3 MB

- 1769-L37ERM, 1769-L37ERMK: 4 MB

- 1769-L38ERM, 1769-L38ERMK: 5 MB

- 1769-L30ERMS:

1 MB standard + 0.5 MB safety

- 1769-L33ERMS, 1769-L33ERMSK: 2 MB standard + 1 MB safety • 1769-L36ERMS:

- 3 MB standard + 1.5 MB safety • 1769-L37ERMS, 1769-L37ERMSK:

4 MB standard + 1.5 MB safety

• 1769-L38ERMS, 1769-L38ERMSK:

5 MB standard + 1.5 MB safety

## Optional nonvolatile memory

1784-SD1 card with 1 Gb of available memory (shipped with controller) 1784-SD2 card with 2 Gb of available memory (available for separate ordering)

## Number of local expansion modules, max (1)

- 1769-L16ER-BB1B:

6 - 1734 POINT I/O™ modules

- 1769-L18ER-BB1B, 1769-L18ERM-BB1B, 1769-L18ERM-BB1BK, 1769-L19ER-BB1B 1769-L19ER-BB1BK:

- 8 - 1734 POINT I/O modules

- 4 - 1769 Compact I/O™ modules

- 1769-L30ER, 1769-L30ER-NSE, 1769-L30ERK, 1769-L30ERM, 1769-L30ERMK, 1769- L30ERMS:

8 - 1769 Compact I/O modules

- 1769-L33ER, 1769-L33ERK, 1769-L33ERM, 1769-L33ERMK, 1769-L33ERMS, 1769-L33ERMSK: 16 - 1769 Compact I/O modules

- 1769-L36ERM, 1769-L36ERMS: 30 - 1769 Compact I/O modules

• 1769-L37ERM, 1769-L37ERMK, 1769-L37ERMS, 1769-L37ERMSK:

31 - 1769 Compact I/O modules

- 1769-L38ERM, 1769-L38ERMK, 1769-L38ERMS, 1769-L38ERMSK:

31 - 1769 Compact I/O modules

Number of I/O module banks, max

– 13

Current draw @ 5V DC, controller power

1 A

- 1769-L24ER-QB1B: 1.54 A

• 1769-L24ER-QBFC1B, 1769-L27ERM-QBFC1B: 1 A Values rated at these ambient temperatures: 40 °C (104 °F), 55 °C (131 °F), 60 °C (140 °F).

500 mA 850 mA

Current draw @ 24V DC, controller power

–

- 1769-L24ER-QB1B: 0.95 A • 1769-L24ER-QBFC1B, 1769-L27ERM-QBFC1B: 0.8 A Values rated at these ambient temperatures: 40 °C (104 °F),

225 mA 700 mA

Current draw @ 24V DC, field power, max

- 3 A - Combined total for all devices that draw current from field power connections Input: 5 mA Output: 500 mA

–

Power dissipation, max

11.5 W

- 1769-L24ER-QB1B: 12 W

- 1769-L24ER-QBFC1B, L27ERM-QBFC1B: 21 W

4.5 W 6.5 W

Isolation voltage

50V (continuous), Basic Insulation Type Tested at 500V AC for 60 s, System to Field

30V (continuous), Basic Insulation Type, USB to system, Ethernet to system and Ethernet to Ethernet Type tested at 500V AC for 60 s

50V, Basic Insulation Type Tested at 500V AC for 60 s, System to Communication ports.

Short circuit protection, field power

Internal fuse, Non-replaceable

–

Recommended external short circuit protection, field power

User-provided 4…5 A @ 3.15…5.5 A 2 t fuse

–

Weight, approx

0.66 kg (1.5 lb)

- 1769-L24ER-QB1B: 0.63 kg (1.39 lb)

- 1769-L24ER-QBFC1B, 1769-L27ERM-QBFC1B: 0.9 kg (1.9 lb)

0.31 kg (0.68 lb)

0.54 kg (1.18 lb)

Module width

100.00 mm (3.94 in.)

- 1769-L24ER-QB1B: 115.00 mm (4.53 in.)

- 1769-L24ER-QBFC1B and 1769-L27ERM-QBFC1B: 140 mm (5.51 in.)

55.00 mm (2.17 in.) 89.00 mm (3.50 in.)

Module location

DIN rail mount

DIN rail or panel mount

Panel-mount screw torque

- — 1.1…1.8 N•m (10…16 lb•in) - use M4 or #8 screws

Embedded power supply

24V DC input, isolated 24V DC Input, isolated

1769-PA2, 1769-PB2, 1769-PA4, 1769-PB4

## Technical Specifications - CompactLogix 5370 Controllers and Compact GuardLogix 5370 Controllers (Continued)

| Attribute                                                | 1769-L16ER-BB1B 1769-L18ER-BB1B 1769-L18ERM-BB1B,1769-L18ERM-BB1BK 1769-L19ER-BB1B, 1769-L19ER-BB1BK                                                                       | 1769-L24ER-QB1B 1769-L24ER-QBFC1B, 1769-L24ER-QBFC1BK 1769-L27ERM-QBFC1B                                                                                                   | 1769-L30ER, 1769-L30ERK 1769-L30ER-NSE 1769-L30ERM, 1769-L30ERMK 1769-L33ER, 1769-L33ERK, 1769-L33ERM, 1769-L33ERMK 1769-L36ERM 1769-L37ERM, 1769-L37ERMK 1769-L38ERM, 1769-L38ERMK   | 1769-L30ERMS 1769-L33ERMS, 1769-L33ERMSK 1769-L36ERMS 1769-L37ERMS, 1769-L37ERMSK 1769-L38ERMS, 1769-L38ERMSK                                                              |
|----------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Power supply distance rating                             | –                                                                                                                                                                          |                                                                                                                                                                            | • Controller and 1769-SDN: 4 • 1769 Compact I/O modules: 4…8, depending on module                                                                                                     | 4 (3 I/O modules between controller and power supply)                                                                                                                      |
| Wire category (2)                                        | 1 - signal ports 1 - power ports 2 - communication ports                                                                                                                   |                                                                                                                                                                            | 2 - communication ports                                                                                                                                                               |                                                                                                                                                                            |
|                                                          | Wire type, Ethernet RJ45 connector according to IEC 60603-7, 2 or 4 pair Category 5e minimum cable according to TIA 568 B.1 or Category 5 cable according to ISO/IEC 24702 | Wire type, Ethernet RJ45 connector according to IEC 60603-7, 2 or 4 pair Category 5e minimum cable according to TIA 568 B.1 or Category 5 cable according to ISO/IEC 24702 | Wire type, Ethernet RJ45 connector according to IEC 60603-7, 2 or 4 pair Category 5e minimum cable according to TIA 568 B.1 or Category 5 cable according to ISO/IEC 24702            | Wire type, Ethernet RJ45 connector according to IEC 60603-7, 2 or 4 pair Category 5e minimum cable according to TIA 568 B.1 or Category 5 cable according to ISO/IEC 24702 |
| Wire type, power terminals, and embedded I/O connections | Copper                                                                                                                                                                     |                                                                                                                                                                            | –                                                                                                                                                                                     |                                                                                                                                                                            |
| Wire size, power terminals(3)                            | 0.051…3.31 mm 2  (30…12 AWG) solid or stranded copper wire °° pp rated at 90 °C (194 °F), or greater, 1.2 mm (3/64 in.) insulation, max Each terminal accepts 1 or 2 wires                                                                                                                                                                            | 0.25…2.50 mm 2  (22…14 AWG) solid copper wire ° pp rated at 75 °C (167 °F), or greater 1.2 mm (3/64 in.) insulation, max Each terminal accepts only 1 wire                                                                                                                                                                            | –                                                                                                                                                                                     |                                                                                                                                                                            |
| Wire stripping length, power terminals (3)               |                                                                                                                                                                            | 10 mm (0.39 in) 8 mm (0.31 in) –                                                                                                                                           |                                                                                                                                                                                       |                                                                                                                                                                            |
| Screw torque, power terminals (3)                        |                                                                                                                                                                            | 0.5…0.6 N•m (4.4…5.3 lb•in) 1.0…1.2 N•m (8.9…10.6 lb•in) –                                                                                                                 |                                                                                                                                                                                       |                                                                                                                                                                            |
| Wire size, embedded I/ O connections                     | 0.205…1.31 mm 2  (24…16 AWG) solid or stranded copper wire ° rated at 90 °C (194 °F), or greater g 1.2 mm (3/64 in.) insulation, max or 90 °C (194 °F) Each terminal accepts only 1 wire                                                                                                                                                                            | 0.205…1.31 mm 2  (24…16 AWG) solid or stranded copper wire ° rated at 90 °C (194 °F), or greater g 1.2 mm (3/64 in.) insulation, max or 90 °C (194 °F) Each terminal accepts only 1 wire                                                                                                                                                                            | –                                                                                                                                                                                     |                                                                                                                                                                            |
| Wire stripping length, embedded I/O connections          |                                                                                                                                                                            | 10 mm (0.39 in) –                                                                                                                                                          |                                                                                                                                                                                       |                                                                                                                                                                            |
| North American temperature code                          | T4A                                                                                                                                                                        | T3C                                                                                                                                                                        | T5                                                                                                                                                                                    |                                                                                                                                                                            |
| IECEx temperature code                                   | –                                                                                                                                                                          | T4                                                                                                                                                                         | –                                                                                                                                                                                     |                                                                                                                                                                            |
| UKEX/ATEX temperature code                               | T4                                                                                                                                                                         |                                                                                                                                                                            | T5                                                                                                                                                                                    |                                                                                                                                                                            |
| Enclosure type rating                                    | None (open-style)                                                                                                                                                          |                                                                                                                                                                            |                                                                                                                                                                                       |                                                                                                                                                                            |

## Real-time Clock Accuracy

This table lists the real-time clock accuracy specifications for the CompactLogix 5370 controllers.

| Ambient Temperature Accuracy   |
|--------------------------------|
| 0 °C (32 °F) -143…+42 s/mo     |
| 25 °C (77 °F) -78…+91 s/mo     |
| 40 °C (104 °F) -101…+73 s/mo   |
| 60 °C (140 °F) -204…-4.50 s/mo |

## Real-time Clock Hold-up Times

This table lists the typical real-time clock hold-up specifications for the CompactLogix 5370 controllers.

IMPORTANT The values in this table are typical and can vary with some CompactLogix 5370 control systems.

| Ambient Temperature Holdup Time, Typical   |
|--------------------------------------------|
| 0 °C (32 °F) 40 days                       |
| 25 °C (77 °F) 35 days                      |
| 40 °C (104 °F) 28 days                     |
| 60 °C (140 °F) 16 days                     |

The I/O module support for CompactLogix 5370 controller systems varies by controller.

## I/O Module Support CompactLogix 5370 L1 Controllers

The CompactLogix 5370 L1 controllers offer an embedded I/O module and the option to use 1734 POINT I/O modules as local expansion modules.

The embedded I/O module provides the following:

- 16 sinking 24V DC digital input points
- 16 sourcing 24V DC digital output points

To use 1734 POINT I/O modules as local expansion modules, keep in mind the following:

- Local expansion modules must be installed in the same system as the CompactLogix 5370 L1 controller.
- The modules are installed to the right of the controller.
- The maximum number of local expansion modules available depends on the controller catalog of that system.

This table lists the number of 1734 POINT I/O modules the CompactLogix 5370 L1 controllers support. The minimum RPI of each I/O module is 1.0 ms and can be changed by 0.5 ms increments. You can use the maximum number of 1734 POINT I/O modules with these CompactLogix 5370 L1 controllers. The total current that the embedded I/O and local expansion modules draw can't exceed both the available POINTBus backplane current of 1 A and the field power current of 3 A.

## 1769-L1 Controllers - Local I/O Module Support

| Cat. No.                            | Local 1734 POINT I/O Modules Supported, Max   |
|-------------------------------------|-----------------------------------------------|
| 1769-L16ER-BB1B 6                   |                                               |
| 1769-L18ER-BB1B                     | 8                                             |
| 1769-L18ERM-BB1B, 1769-L18ERM-BB1BK | 8                                             |
| 1769-L19ER-BB1B, 1769-L19ER-BB1BK   | 8                                             |

<!-- image -->

Depending on the configuration of your application, you can use one of these devices to make additional POINTBus backplane current or field power current available:

|             | Device Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|-------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1734-EP24DC | POINT I/O Expansion Power Supply - An expansion power supply is installed between embedded I/O modules and local expansion modules or between local expansion modules. The expansion power supply breaks the available POINTBus backplane current between the modules to its left and right. With the expansion power supply installed, the modules to its left can draw up to 1 A of POINTBus backplane current. The modules to the right of the expansion power supply can draw as much current as the current provided by the expansion power supply. Additionally, the expansion power supply breaks the available field power current between the modules to its left and right. With the expansion power supply installed, the modules to its left can draw up to 3 A of field power current. The modules to the right of the expansion power supply can draw as much field power current as allowed by the expansion power supply. For more information on the 1734-EP24DC expansion power supply, see the POINT I/O 24V DC Expansion Power Supply Installation |
| 1734-FPD    | POINT I/O Field Power Distributor Module - A field power distributor module can also be installed between embedded I/O modules and local expansion modules or between local expansion modules. The field power distributor module breaks the available field power current between the modules to its left and right. With the field power distributor module installed, the modules to its left can draw up 3 A of field power current. The modules to the right of the field power distributor can draw as much field power current as allowed by the field power distributor. For more information on the 1734-FPD POINT I/O Field Power Distributor module, see the POINT I/O Field Power Distributor Module Installation Instructions, publication 1734-IN059 . IMPORTANT: Remember, the field power distributor module changes only the level of field power current available in the system. The module does not affect the level of POINTBus backplane current available.                                                                                      |

## Local I/O Performance of the CompactLogix 5371 L1 Controllers

The requested packet interval (RPI) defines the frequency at which the controller sends data to and receives data from I/O modules. You set an RPI rate for each I/O module in your system.

CompactLogix 5370 L1 controllers always attempt to scan an I/O module at the configured RPI rate. For individual I/O modules, a Module RPI Overlap minor fault occurs if there are enough I/O modules with RPI rates set too fast that they can't all be serviced in the allotted interval.

The specific configuration parameters for a system determine the impact on actual RPI rates. These configuration factors can impact the effective scan frequency for any individual module:

- Rates at which the RPI rates of other 1734 POINT I/O modules are set
- Number of other 1734 POINT I/O modules in the system
- Types of other 1734 POINT I/O modules in the system
- Application user task priorities

In general, follow these guidelines when setting the RPI rates in a CompactLogix 5370 L1 control system:

| Module Type Guidelines   |                                                                                                                                                                                                                                                                                                                                                                                                                              |
|--------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Digital                  | • 1…2 modules can be scanned in 2 ms. • 3…4 modules can be scanned in 4 ms. • 5…8 modules can be scanned in 8 ms. IMPORTANT: Remember that digital modules can be the embedded I/O module on the controller or 1734 POINT I/O modules that are used as local expansion modules. Therefore, the consideration for using two modules can be the embedded I/O module and a 1734 POINT I/O module or two 1734 POINT I/O modules. |
| Specialty and Analog     | • 1 module can be scanned at 20 ms. • For each additional module, add 20 ms. For example, if a CompactLogix 5370 L1 control system uses two analog modules, the module can be scanned in 40 ms.                                                                                                                                                                                                                              |
| 1734-485ASC              | The total data size for all ASC modules determines the RPI rates: • For total data size less than 20 bytes, each module can be scanned in 20 ms. • For data size greater than 20 bytes, use the size value as the RPI. For example, if the total data size is 40 bytes, each ASC module can be scanned in 40 ms.                                                                                                             |

You aren't required to set the RPI values of an individual 1734 POINT I/O module to the values listed previously. For example, if your application scans one or two modules, you do not have to use RPI rates of 2 ms. Remember, though, that higher RPI rates result in scanning the data less frequently.

The RPI shows how quickly modules can be scanned, not how quickly an application can use the data. The RPI is asynchronous to the program scan. Other factors, such as program execution duration, affect I/O throughput.

## Embedded Specifications - CompactLogix 5371 L1 Controllers

| Attribute                                        | 1769-L16ER-BB1B, 1769-L18ER-BB1B, 1769-L18ERM-BB1B, 1769-L18ERM-BB1BK, 1769-L19ER-BB1B, 1769-L19ER-BB1BK                        |
|--------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|
| Embedded DC Input Specifications                 | Embedded DC Input Specifications                                                                                                |
| Inputs                                           | 16                                                                                                                              |
| Voltage category                                 | 24V DC sink                                                                                                                     |
| Operating voltage range                          | 10…28.8V DC 24V DC nom                                                                                                          |
| Digital filter, off to on/on to off              | 0.5 ms hardware plus 0…65 ms (selectable)                                                                                       |
| Input delay, off to on/on to off                 |                                                                                                                                 |
| Off-state voltage, max                           | 5V DC                                                                                                                           |
| Off-state current, max                           | 1 mA                                                                                                                            |
| On-state current, min                            | 2 mA @ 24V DC                                                                                                                   |
| Input impedance, max                             | 5.4 kΩ                                                                                                                          |
| Cyclic update time                               | 1…750 ms                                                                                                                        |
| Isolation voltage                                | 50V DC (continuous), Basic Insulation Type Tested at 500V AC for 60 s, system to field No isolation between individual channels |
| IEC input compatibility                          | Type 3                                                                                                                          |
| Isolated groups                                  | None                                                                                                                            |
| Embedded DC Output Specifications                | Embedded DC Output Specifications                                                                                               |
| Outputs                                          | 16                                                                                                                              |
| Voltage category                                 | 24V DC source                                                                                                                   |
| Operating voltage range                          | 10…28.8V DC 24V DC nom                                                                                                          |
| Output delay, off to on                          | 0.1 ms                                                                                                                          |
| Output delay, on to off                          | 0.1 ms                                                                                                                          |
| Off-state leakage current, max                   | 0.5 mA @ 24V DC                                                                                                                 |
| On-state current, min 1 mA per channel           |                                                                                                                                 |
| On-state voltage drop, max 0.6V DC               |                                                                                                                                 |
| Current per point, max                           | 0.5 A                                                                                                                           |
| Current per module, max                          | 3 A                                                                                                                             |
| Surge current per point, max                     | 1 A for 100 ms per point, repeatable every 2 s                                                                                  |
| Isolation voltage                                | 50V DC (continuous), Basic Insulation Type Tested at 500V AC for 60 s, system to field No isolation between individual channels |
| Isolated groups None                             |                                                                                                                                 |
| Pilot duty rating                                | 0.5 A                                                                                                                           |
| Embedded Power Supply Specifications             | Embedded Power Supply Specifications                                                                                            |
| Input voltage range                              | 10…28.8V DC                                                                                                                     |
| Input voltage, nom                               | 24V DC                                                                                                                          |
| Line requirement (VDC), min 30VA                 |                                                                                                                                 |
| Available 5V DC POINTBus backplane current       | 1 A @ 5V DC                                                                                                                     |
| Current draw @ 24V DC, field power, max          | 3 A(1)                                                                                                                          |
| Inrush, max 10 A                                 |                                                                                                                                 |
| Line loss ride-through 10 ms…10 s                |                                                                                                                                 |
| Output bus current capacity, max 0.1…3 A @ 5V DC |                                                                                                                                 |
| Load current, min 300 mA                         |                                                                                                                                 |
| Power dissipation, max 12 W                      |                                                                                                                                 |
| Short circuit protection                         | Internal fuse Not replaceable                                                                                                   |
| Overvoltage protection Yes                       |                                                                                                                                 |

## I/O Module Support - CompactLogix 5370 L2 Controllers

The CompactLogix 5370 L2 controllers offer embedded I/O modules and the option to use 1769 Compact I/O modules as local expansion modules. This table describes the embedded I/O modules and local expansion modules that the CompactLogix 5370 L2 controllers support.

|                                       | Embedded I/O Module Support                  | Embedded I/O Module Support           | Embedded I/O Module Support   | Embedded I/O Module Support             | Embedded I/O Module Support   | Embedded I/O Module Support   | Local Expansion Modules Support   |
|---------------------------------------|----------------------------------------------|---------------------------------------|-------------------------------|-----------------------------------------|-------------------------------|-------------------------------|-----------------------------------|
| Cat. No.                              | Sinking/Sourcing 24V DC Digital Input Points | Sourcing 24V DC Digital Output Points | High-speed Counter Modules    | High-speed Counter Module Output Points | Universal Analog Input Points | Analog Output Points          | 1769 Compact I/O Modules          |
| 1769-L24ER-QB1B                       | 16 16                                        |                                       |                               |                                         | ––––                          |                               | As many as 4 modules              |
| 1769-L24ER-QBFC1B, 1769-L24ER-QBFC1BK | 16 16                                        |                                       |                               |                                         | 4442                          |                               | As many as 4 modules              |
| 1769-L27ERM-QBFC1B                    | 16 16                                        |                                       |                               |                                         | 4442                          |                               | As many as 4 modules              |

## IMPORTANT

Remember the following when using the embedded I/O modules on CompactLogix 5370 L2 controllers:

- 1769-L24ER-QB1B controller - The digital input points and digital output points are on one embedded I/O module. Therefore, the 1769-L24ER-QB1B controller is considered to have one embedded I/O module.
- 1769-L24ER-QBFC1B, 1769-L24ER-QBFC1BK, and 1769-L27ERM-QBFC1B controllers - The digital input points and digital output points are on one embedded I/O module. The high-speed counter module input/output points, universal analog input points, and analog output points are on another single embedded I/O module. Therefore, the 1769-L24ER-QBFC1B, 1769-L24ER-QBFC1BK, and 1769-L27ERM-QBFC1B controllers are considered to have two embedded I/O modules.

You configure an RPI rate for the embedded I/O modules to establish specific time intervals at which data is transmitted between the controller and the embedded I/O modules. The available RPI range of the embedded I/O modules is 0.5…750.0 ms and can be changed by 0.5 ms increments. The default setting is 20 ms.

To use 1769 Compact I/O modules as local expansion modules, keep in mind the following:

- Local expansion modules must be installed in the same system as the CompactLogix 5370 L2 controller.
- Local expansion modules are installed to the right of the embedded I/O modules.
- You must install a 1769-ECR Compact I/O end cap on the right side of the control system. The end cap can be installed on the right side of the embedded I/O module. If local expansion modules are used, the end cap can be installed on the right side of the 1769 Compact I/O module.

<!-- image -->

## CompactLogix 5370 L2 Controller r Local I/O Performance

The Requested Packet Interval (RPI) defines the frequency at which the controller sends data to and receives data from I/O modules. You set an RPI rate for each I/O module in your system in the programming software. You also set RPI rates through the programming software for embedded I/O modules, local expansion modules, and distributed I/O modules over an EtherNet/IP network .

The CompactLogix 5370 L2 controllers always attempt to scan an I/O module at the configured RPI rate. The controller scans distributed I/O modules at the configured RPI rates.

With embedded I/O modules and local expansion modules, however, some specific system-configuration parameters determine the actual rate at which the controller scans the modules. That is, the controller can be configured to scan an I/O module at one rate, but actually scan the module at another rate.

For individual I/O modules, a Module RPI Overlap minor fault occurs if there is at least one I/O module that can't be serviced within its RPI time.

The specific configuration parameters for a system determine the impact on actual RPI rates. These configuration factors can impact the effective scan frequency for any individual embedded or local expansion module:

- Rates at which the RPI values of the embedded I/O modules are set
- Number of embedded I/O modules that are used in the system
- Types of embedded I/O modules that are used in the system
- Rates at which RPI values for the 1769 Compact I/O module are set
- Number of 1769 Compact I/O modules in the system
- Types of 1769 Compact I/O modules in the system
- Application user task priorities

## RPI Rate Guidelines

| Type of Module Guidelines    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Digital and analog (any mix) | The following guidelines apply: • 1…2 modules can be scanned in 0.5 ms. • 3…4 modules can be scanned in 1 ms. • 5…6 modules can be scanned in 2 ms. • Some input modules have a fixed 8 ms filter, so selection of a faster RPI has no effect.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Specialty                    | The following conditions apply: • For every full-sized 1769-SDN module in the system, increase the RPI of every other module by 2 ms. • For every 1769-HSC module in the system, increase the RPI of every other module by 1 ms. • For every full-sized 1769-ASCII module system, increase the RPI of every other module by 1 ms. • For every 1769-SM2 module in the system, increase the RPI of every other module by 2 ms. For example, the system includes four I/O modules that are configured with an RPI = 1 ms and you add a 1769-SDN module to the system. You must increase the RPI value for all four I/O modules by 2 ms. Therefore, when the 1769-SDN module is added to the system, the four I/O modules use an RPI = 3 ms. If, in the same system, you add a second 1769-SDN module, the RPI value of the four I/O modules is increased to 5 ms. |

## IMPORTANT

The number of I/O modules can be the embedded I/O modules on the controller or 1769 Compact I/O modules that are used as local expansion modules.

Therefore, the consideration for using modules can be any of the following system configurations:

- Only embedded I/O modules
- Only 1769 Compact I/O modules
- Some combination of embedded I/O modules and 1769 Compact I/O modules

You can set individual RPI rates for 1769 Compact I/O modules higher than those values listed in this table. The RPI shows how quickly modules can be scanned, not how quickly an application can use the data. The RPI is asynchronous to the program scan. Other factors, such as program execution duration, affect I/O throughput.

## Embedded DC Specifications - CompactLogix 5370 L2 Controllers

|                                         | Attribute 1769-L24ER-QB1B                                                                                                             | 1769-L24ER-QBFC1B 1769-L24ER-QBFC1BK 1769-L27ERM-QBFC1B                                                                               |
|-----------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| Embedded DC Input Specifications        | Embedded DC Input Specifications                                                                                                      | Embedded DC Input Specifications                                                                                                      |
| Inputs                                  | 16                                                                                                                                    |                                                                                                                                       |
| Voltage category                        | 24V DC sink/source                                                                                                                    |                                                                                                                                       |
| Operating voltage range                 | 10…28.8V DC @ 40 °C (104 °F) 10…26.4V DC @ 60 °C (140 °F) 24V DC nom                                                                  | 10…28.8V DC @ 40 °C (104 °F) 10…27.0V DC @ 55 °C (131 °F) 10…26.4V DC @ 60 °C (140 °F) 24V DC nom                                     |
| Digital filter, off to on and on to off | 0 s, 100 µs, 500 µs, 1 ms, 2 ms, 4 ms, 8 ms                                                                                           | 0 s, 100 µs, 500 µs, 1 ms, 2 ms, 4 ms, 8 ms                                                                                           |
| Input delay, off to on and on to off    | 100 µs, min 8 ms, max                                                                                                                 |                                                                                                                                       |
| Off-state voltage, max                  | 5V DC                                                                                                                                 |                                                                                                                                       |
| Off-state current, max                  | 1.5 mA                                                                                                                                |                                                                                                                                       |
| On-state current, min                   | 2 mA @ 24V DC per channel                                                                                                             |                                                                                                                                       |
| On-state current, max                   | 5 mA @ 24V DC per channel                                                                                                             |                                                                                                                                       |
| Input impedance, max                    | 5.2 kΩ @ 24V DC 6.1 kΩ @ 30V DC                                                                                                       |                                                                                                                                       |
| Cyclic update time                      | 0.5…750 ms                                                                                                                            |                                                                                                                                       |
| Isolation voltage                       | 75V (continuous), Reinforced Insulation Type Type tested at 1200V AC for 1 s and at 1700V DC for 1 s; group to system, group to group | 75V (continuous), Reinforced Insulation Type Type tested at 1200V AC for 1 s and at 1700V DC for 1 s; group to system, group to group |
| IEC input compatibility                 | Type 3                                                                                                                                |                                                                                                                                       |
| Isolated groups                         | Group 1: inputs 0…7 Group 2: inputs 8…15 Isolated groups operate in either sink or source configurations                              | Group 1: inputs 0…7 Group 2: inputs 8…15 Isolated groups operate in either sink or source configurations                              |
| Embedded DC Output Specifications       | Embedded DC Output Specifications                                                                                                     | Embedded DC Output Specifications                                                                                                     |
| Outputs                                 | 16                                                                                                                                    |                                                                                                                                       |
| Voltage category                        | 24V DC source                                                                                                                         |                                                                                                                                       |
| Operating voltage range                 | 20.4…26.4V DC 24V DC nom                                                                                                              |                                                                                                                                       |
| Output delay, off to on                 | 0.05 ms                                                                                                                               |                                                                                                                                       |
| Output delay, on to off                 | 0.5 ms                                                                                                                                |                                                                                                                                       |
| Off-state leakage current, max          | 0.1 mA @ 26.4V DC                                                                                                                     |                                                                                                                                       |
|                                         | On-state current, max 0.5 mA @ 24V DC per channel                                                                                     |                                                                                                                                       |
| On-state voltage drop, max              | 1.0V DC @ 1.0 A                                                                                                                       |                                                                                                                                       |
| Current per point, max                  | 0.83 A @ 40 °C (104 °F) 0.5 A @ 60 °C (140 °F)                                                                                        | 0.83 A @ 40 °C (104 °F) 0.58 A @ 55 °C (131 °F) 0.5 A @ 60 °C (140 °F)                                                                |
| Current per module, max                 | 6.64 A @ 40 °C (104 °F) 4.0 A @ 60 °C (140 °F)                                                                                        | 6.64 A @ 40 °C (104 °F) 4.64 A @ 55 °C (131 °F) 4.0 A @ 60 °C (140 °F)                                                                |
| Surge current per point, max            | 2.0 A for 10 ms per point, repeatable every 2 s                                                                                       | 2.0 A for 10 ms per point, repeatable every 2 s                                                                                       |
| Isolation voltage                       | 75V (continuous), Reinforced Insulation Type Type tested at 1200V AC for 1 s and at 1700V DC for 1 s; group to system, group to group | 75V (continuous), Reinforced Insulation Type Type tested at 1200V AC for 1 s and at 1700V DC for 1 s; group to system, group to group |
| Isolated groups                         | Group 1: Outputs 0…7 Group 2: Outputs 8…15                                                                                            | Group 1: Outputs 0…7 Group 2: Outputs 8…15                                                                                            |

## Embedded DC Output Temperature Derating

The area within the curves represents the safe operating range for the embedded DC outputs under various conditions of usersupplied voltages and ambient temperatures.

## Maximum Amperes per Point Versus Temperature

<!-- image -->

## Maximum Amperes per Module Versus Temperature

<!-- image -->

## Embedded Analog Input Specifications CompactLogix 5370 L2 Controllers

## Embedded Analog Input Specifications CompactLogix 5370 L2 Controllers

|                                             | Attribute 1769-L24ER-QBFC1B, 1769-L24ER-QBFC1BK, 1769-L27ERM-QBFC1B                                                                                                                                                                                                                                                                                                                               |                                             |                                                                                                                                                                                                                                                                                                                                 |
|---------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs                                      | 4 channels of thermocouple/voltage/current 2 channels of RTD/Resistance inputs                                                                                                                                                                                                                                                                                                                    |                                             | Thermocouple types: • J at -210…+1200 °C (-328…+2192 °F): ±0.6 °C (1.1 °F) • N at -110…+1300 °C (-166…+2372 °F): ±1.0 °C (1.8 °F) • N at -200…-110 °C (-328…-166 °F): ±1.0 °C (1.8 °F) Attribute 1769-L24ER-QBFC1B, 1769-L24ER-QBFC1BK, 1769-L27ERM-QBFC1B                                                                      |
| Operating voltage range                     | 2.6…30.0V DC @ 40 °C (104 °F) 2.6…26.4V DC @ 55 °C (131 °F) 2.6…5V DC @ 60 °C (140 °F)                                                                                                                                                                                                                                                                                                            |                                             | • T at -170…+400 °C (-274…+752 °F): ±1.0 °C (1.8 °F) • T at -200…-170 °C (-328…-274 °F): ±1.0 °C (1.8 °F) • K at 1370…1372 °C (2498…2501.6 °F): ±1.2 °C (2.2 °F)                                                                                                                                                                |
| Input types                                 | • Thermocouple: J, K, T, E, R, S, B, N, and C • Voltage • Current • RTD: Platinum 385, Platinum 3916, Copper 426, Nickel 672, Nickel 618, Nickel-Iron 518 • Resistance Thermocouple:                                                                                                                                                                                                              |                                             | • K at -200…+1370 °C (-328…+2498 °F): ±1.0 °C (1.8 °F) • E at -200…+1000 °C (-328…+1832 °F): ±0.5 °C (0.9 °F) • S and R at 0…1768 °C (32…3214.4 °F): ±1.7 °C (3.1 °F) • S and R at -50…0 °C (-58…+32 °F): ±4.0 °C (7.2 °F) • B at 300…1820 °C (572…3308 °F): ±3.0 °C (5.4 °F) • B at 250…300 °C (482…572 °F): ±6.0 °C (10.8 °F) |
| Input ranges (1)                            | • 0…10V • -10V…+10V Current: • 0…20 mA • 4…20 mA RTD: • 0…100 Ω Platinum 385 • 0…200 Ω Platinum 385 • 0…500 Ω Platinum 385 • 0…1000 Ω Platinum 385 • 0…100 Ω Platinum 3916 • 0…200 Ω Platinum 3916 • 0…500 Ω Platinum 3916 • 0…1000 Ω Platinum 3916 • 0…10 Ω Copper 426 • 0…120 Ω Nickel 618 • 0…120 Ω Nickel 672 • 0…604 Ω Nickel-Iron 518 Resistance: • 0…150 Ω • 0…500 Ω • 0…1000 Ω • 0…3000 Ω | Accuracy, overall at 0…60 °C (32…140 °F)(2) | • 0…500 Ω: ±0.5 Ω • 0…1000 Ω: ±1.0 Ω • 0…3000 Ω: ±1.5 Ω Thermocouple types: ° pyp • J at -210…+1200 °C (-328…+2192 °F): ±0.9 °C (1.6 °F) • N at -110…+1300 °C (-166…+2372 °F): ±1.5 °C (2.7 °F) • N at -200…-110 °C (-328…-166 °F): ±1.5 °C (2.7 °F) • T at -170…+400 °C (-274…+752 °F): ±1.5 °C (2.7 °F) • T at -200…-170 °C (-328…-274 °F): ±1.5 °C (2.7 °F) • K at 1370…1372 °C (2498…2501.6 °F): ±1.8 °C (3.2 °F) • K at -200…+1370 °C (-328…+2498 °F): ±1.5 °C (2.7 °F) • E at -200…+1000 °C (-328…+1832 °F): ±0.8 °C (1.4 °F) • S and R at 0…1768 °C (32…3214.4 °F): ±3.5 °C (6.3 °F) • S and R at -50…0 °C (-58…+32 °F): ±4.0 °C (7.2 °F) • B at 300…1820 °C (572…3308 °F): ±4.5 °C (8.1 °F) • B at 250…300 °C (482…572 °F): ±9.0 °C (16.2 °F) • C at 0…2315 °C (32…4199 °F): ±3.5 °C (6.3 °F) Voltage inputs: • ±50 mV: ±25 µV • ±100 mV: ±30 µV • 0…5V: ±5 mV • 1…5V: ±4 mV • 0…10V: ±10 mV • ±10V: ±20 mV                                                                                                                                                                                                                                                                                                                                 |
| Resolution, max                             | 15 bits plus sign (Bipolar) 16 bits (Unipolar)                                                                                                                                                                                                                                                                                                                                                    |                                             | Current inputs: • 0…20 mA: ±50 µA                                                                                                                                                                                                                                                                                               |
| Input impedance  Converter type Sigma-Delta | Voltage: 10 MΩ Current: 250 Ω                                                                                                                                                                                                                                                                                                                                                                     |                                             | • 4…20 mA: ±40 µA RTD types: yp • Platinum 385: ±0.9 °C (1.6 °F)                                                                                                                                                                                                                                                                                                                                 |
| Cyclic update time                          | 11…5000 ms dependent on user configuration 30V AC/30V DC                                                                                                                                                                                                                                                                                                                                          |                                             | • Nickel: ±0.4 °C (0.7 °F) • Nickel-Iron: ±0.5 °C (0.9 °F) • Copper: ±1.1 °C (2.0 °F) Resistance types: (2) • 0…150 Ω: ±0.25 Ω                                                                                                                                                                                                  |
| Rated working voltage                       |                                                                                                                                                                                                                                                                                                                                                                                                   |                                             | • 0…500 Ω: ±0.8 Ω • 0…1000 Ω: ±1.5 Ω • 0…3000 Ω: ±2.5 Ω                                                                                                                                                                                                                                                                         |
| Common mode voltage                         | ±10V DC per channel                                                                                                                                                                                                                                                                                                                                                                               |                                             |                                                                                                                                                                                                                                                                                                                                 |
| Common mode rejection ratio, min            | 115 dB at 50 Hz at 10V 115 dB at 60 Hz at 10V                                                                                                                                                                                                                                                                                                                                                     |                                             |                                                                                                                                                                                                                                                                                                                                 |
| Normal mode rejection ratio, min            | 85 dB at 50 Hz at 1.5V 85 dB at 60 Hz at 1.5V                                                                                                                                                                                                                                                                                                                                                     |                                             |                                                                                                                                                                                                                                                                                                                                 |

## Embedded Analog Input Specifications CompactLogix 5370 L2 Controllers

|                                  | Attribute 1769-L24ER-QBFC1B, 1769-L24ER-QBFC1BK, 1769-L27ERM-QBFC1B                                                                                                                                                                                                                                                   |
|----------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Cold junction compensation accuracy at ° y  0…60 °C (32…140 °F)(2)                                  | ±1.3 °C (34.34 °F)                                                                                                                                                                                                                                                                                                    |
|                                  | Calibration Cyclic calibration by user configuration                                                                                                                                                                                                                                                                  |
| Non-linearity (in percent full scale)                                  | ±0.05%                                                                                                                                                                                                                                                                                                                |
| Repeatability at °° py  25 °C (77 °F) with 10 Hz filter                                  | Thermocouple types: ° pyp • J at -210…+1200 °C (-328…+2192 °F): ±0.1 °C (0.2 °F) • N at -110…+1300 °C (-166…+2372 °F): ±0.1 °C (0.2 °F) • N at -200…-110 °C (-328…-166 °F): ±0.25 °C (0.5 °F) • T at -170…+400 °C (-274…+752 °F): ±0.1 °C (0.2 °F) • T at -200…-170 °C (-328…-274 °F): ±1.5 °C (2.7 °F) • K at 1370…1372 °C (2498…2501.6 °F): ±0.15 °C (0.3 °F) • K at -170…+1370 °C (-274…+2498 °F): ±0.1° (0.2 °F) • K at -200…-170 °C (-328…-274 °F): ±2.0 °C (3.6 °F) • E at -200…+1000 °C (-328…+1832 °F): ±0.1° (0.2 °F) • S and R at 0…1768 °C (32…3214.4 °F): ±0.4 °C (0.7 °F) • S and R at -50…0 °C (-58…+32 °F): ±1.0 °C (1.8 °F) • B at 300…1820 °C (572…3308 °F): ±0.7 °C (1.3 °F) • B at 250…300 °C (482…572 °F): ±1.5 °C (2.7 °F) • C at 0…2315 °C (32…4199 °F): ±0.2 °C (0.4 °F) Voltage inputs: • ±50 mV: ±6 µA • ±100 mV: ±6 µV • 0…5V: ±150 mV • 1…5V: ±150 mV                                                                                                                                                                                                                                                                                                                       |
|                                  | • 0…10V: ±150 mV • ±10V: ±150 mV Current inputs: • 0…20 mA: ±0.3 µA • 4…20 mA: ±0.3 µA RTD types: • Platinum 385: ±0.2 °C (0.4 °F) • Platinum 3916: ±0.2 °C (0.4 °F) • Nickel: ±0.01 °C (0.02 °F) • Nickel-Iron: ±0.01 °C (0.02 °F) • Copper: ±0.2 °C (0.4 °F) Resistance types: • 0…150 Ω: ±0.04 Ω • 0…500 Ω: ±0.2 Ω |
| Overload at input terminals, max | Voltage: ±35V DC continuous Current: 32 mA continuous, ±7.6V DC                                                                                                                                                                                                                                                       |
| Channel diagnostics              | Invalid configuration, Over-, or underrange by bit reporting, open circuit                                                                                                                                                                                                                                            |
| Isolation voltage                | 30V AC/30V DC (continuous), reinforced insulation type Type tested at 720V DC for 60 s; inputs to system backplane                                                                                                                                                                                                    |

## Embedded Analog Output Specifications CompactLogix 5370 L2 Controllers

|                                                         | Attribute 1769-L24ER-QBFC1B, 1769-L24ER-QBFC1BK, 1769-L27ERM-QBFC1B                                                            |
|---------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| Outputs                                                 | 2 single-ended                                                                                                                 |
| Output types                                            | • Voltage • Current                                                                                                            |
| Output ranges (1)                                       | Voltage: • 0…5V • 1…5V • 0…10V • -10V…+10V Current: • 0…20 mA • 4…20 mA                                                        |
|                                                         | Converter type R-2R Ladder Voltage Switching                                                                                   |
| Resolution, max                                         | 15 bits plus sign (Bipolar) 16 bits (Unipolar)                                                                                 |
| Cyclic update time, nom                                 | 2.5 ms                                                                                                                         |
| Cyclic update time, max                                 | 9.5 ms                                                                                                                         |
| Current load on voltage output                          | 10 mA max                                                                                                                      |
| Resistive load on current output                        | 0…300 Ω                                                                                                                        |
| Load range on voltage output                            | > 1 kΩ at 10V DC                                                                                                               |
| Inductive load, max (current outputs)                   | 0.1 mH                                                                                                                         |
| Capacitive load, max (Voltage Outputs)                  | 1 µF                                                                                                                           |
| Accuracy, overall °° y at 25 °C (77 °F)                                                         | Voltage: ±0.5% full-scale Current: ±0.5% full-scale                                                                            |
| Accuracy, overall ° y at 0…60 °C (32…140 °F)                                                         | Voltage: ±0.8% full-scale Current: ±0.8% full-scale                                                                            |
| Accuracy drift with temperature                         | Voltage: ±0.0086% full-scale per °C ° g Current: ±0.0086% full-scale per °C                                                                                                                                |
| Output ripple range 0…50 kHz (referred to output range) | ±0.05%                                                                                                                         |
|                                                         | Non-linearity ±0.05% (in percent full-scale)                                                                                   |
| Repeatability ± 0.05%                                   |                                                                                                                                |
| Output impedance                                        | Voltage: <1 Ω Current: >1 MΩ                                                                                                   |
| Short circuit protection                                | Yes                                                                                                                            |
| Short circuit, nom                                      | Current: 16 mA                                                                                                                 |
| Open circuit, max                                       | 16V                                                                                                                            |
| Output response at system power-up and powerdown        | Current: ± 1.0V spike for < 5 ms Voltage: ± 1.0V DC spike < 5 ms                                                               |
| Isolation voltage                                       | 30V AC/30V DC (continuous), reinforced insulation type Type tested at 500V AC or 710V DC for 60 s; outputs to system backplane |

## Analog Input Ranges - CompactLogix 5370 L2 Controllers

| Input Type Normal Op. Range                                             | Full Range (1)                                                          | Raw/Prop. Data Units for Full Range   |                                                                | Scaled-for PID Values for Normal Operating Range          | Scaled-for-PID Values for Full Range   | Percent of Normal Op. Range Values   | Percent of Full Range Values      |
|-------------------------------------------------------------------------|-------------------------------------------------------------------------|---------------------------------------|----------------------------------------------------------------|----------|----------------------------------------|--------------------------------------|-----------------------------------|
| Input Type Normal Op. Range                                             | Full Range (1)                                                          | Raw/Prop. Data Units for Full Range   | °C °F °C °F                                                    | Scaled-for PID Values for Normal Operating Range          | Scaled-for-PID Values for Full Range   | Percent of Normal Op. Range Values   | Percent of Full Range Values      |
|                                                                         | -10…+10V DC -10.5V…+10.5V                                               | -32767… +32767                        | -10500…+10500 -1050…+1050                                      | 0…16,383 | -410…+16793                            | -10000… +10000                       | -10500…+10500                     |
|                                                                         |                                                                         |                                       | 0…5V DC -0.5V…+5.25V -500…+5250 -50…+525 -1638…+17202          |          |                                        |                                      | -1000…+10500                      |
|                                                                         | 0…10V DC -0.5V…+10.5V -500…+10500                                       |                                       |                                                                |          |                                        |                                      | -50…+1050 -819…+17202 -500…+10500 |
|                                                                         |                                                                         |                                       | 4…20 mA 3.2…21 mA 3200…21000 320…2100 -819…+17407 -500…+10625  |          |                                        |                                      |                                   |
|                                                                         |                                                                         |                                       | 1…5V DC 0.5V…5.25V 500…5250 50…525 -2048…+17407 -1250…+10625   |          |                                        |                                      |                                   |
|                                                                         |                                                                         |                                       | 0…20 mA 0…21 mA 0…21000 0…2100 0…17202 0…10500                 |          |                                        |                                      |                                   |
| J (-210…+1200) -2100…+12000 -3460…+21920 -210…+1200 -346…+2192          | J (-210…+1200) -2100…+12000 -3460…+21920 -210…+1200 -346…+2192          |                                       |                                                                |          |                                        | 0…16,383 0…10000                     |                                   |
| K (-200…+1372) -2000…+13720 -3280…+25020 -200…+1372 -328…+2502          | K (-200…+1372) -2000…+13720 -3280…+25020 -200…+1372 -328…+2502          |                                       |                                                                |          |                                        |                                      |                                   |
| T (-200…+400) -2000…+4000 -3280…+7520 -200…+400 -328…+752               | T (-200…+400) -2000…+4000 -3280…+7520 -200…+400 -328…+752               |                                       |                                                                |          |                                        |                                      |                                   |
|                                                                         |                                                                         |                                       | E (-200…+1000) -2000…+10000 -3280…+18320 -200…+1000 -328…+1832 |          |                                        |                                      |                                   |
|                                                                         |                                                                         |                                       | R (-50…+1768) -500…+17680 -580…+32140 -50…+1768 -58…+3214      |          |                                        |                                      |                                   |
|                                                                         |                                                                         |                                       | S (-50…+1768) -500…+17680 -580…+32140 -50…+1768 -58 …+3214     |          |                                        |                                      |                                   |
|                                                                         |                                                                         |                                       | 32767 B (250…1820) 2500…18200 4820…32767 250…1820 482…3308                                                                |          |                                        |                                      |                                   |
| +32767 N (-200…+1300) -2000…+13000 -3280…+23720 -200…+1300 -328…+2372                                                                         | +32767 N (-200…+1300) -2000…+13000 -3280…+23720 -200…+1300 -328…+2372                                                                         |                                       |                                                                |          |                                        |                                      |                                   |
| C (0…2315) 0…23150 320…32767 0…2315 32…4199                             | C (0…2315) 0…23150 320…32767 0…2315 32…4199                             |                                       |                                                                |          |                                        |                                      |                                   |
| -50…+50 mV -5000…+5000 -500…+500                                        | -50…+50 mV -5000…+5000 -500…+500                                        |                                       |                                                                |          |                                        |                                      |                                   |
| -100…+100 mV -10000…+10000 -1000…+1000                                  | -100…+100 mV -10000…+10000 -1000…+1000                                  |                                       |                                                                |          |                                        |                                      |                                   |
| 0…150 Ω                                                                 | 0…150 Ω                                                                 |                                       | 0…15000 0…1500                                                 |          |                                        |                                      |                                   |
| 0…500 Ω                                                                 | 0…500 Ω                                                                 |                                       | 0…5000 0…500                                                   |          |                                        |                                      |                                   |
| 0…1000 Ω                                                                | 0…1000 Ω                                                                |                                       | 0…10000 0…1000                                                 |          |                                        |                                      |                                   |
| 0…3000 Ω                                                                | 0…3000 Ω                                                                |                                       | 0…30000 0…3000                                                 |          |                                        |                                      |                                   |
| Platinum 385 (-200…+850) -2000…+8500 -3280…+15620 -200…+850 -328…+1562  | Platinum 385 (-200…+850) -2000…+8500 -3280…+15620 -200…+850 -328…+1562  |                                       |                                                                |          |                                        |                                      |                                   |
| Platinum 3916 (-200…+510) -2000…+5100 -3280…+9500 -200…+510 -328…+950   | Platinum 3916 (-200…+510) -2000…+5100 -3280…+9500 -200…+510 -328…+950   |                                       |                                                                |          |                                        |                                      |                                   |
| Copper 426 (-70…+150) -700…+1500 -940…+3020 -70…+1500 -94…+302          | Copper 426 (-70…+150) -700…+1500 -940…+3020 -70…+1500 -94…+302          |                                       |                                                                |          |                                        |                                      |                                   |
| Nickel 618 (-60…+250) -600…+2500 -760…+4820 -60…+250 -76…+482           | Nickel 618 (-60…+250) -600…+2500 -760…+4820 -60…+250 -76…+482           |                                       |                                                                |          |                                        |                                      |                                   |
| Nickel 672 (-80…+260) -800…+2600 -1120…+5000 -80…+260 -112…+500         | Nickel 672 (-80…+260) -800…+2600 -1120…+5000 -80…+260 -112…+500         |                                       |                                                                |          |                                        |                                      |                                   |
| Nickel-Iron 518 (-100…+200) -1000…+2000 -1480…+3920 -100…+200 -148…+392 | Nickel-Iron 518 (-100…+200) -1000…+2000 -1480…+3920 -100…+200 -148…+392 |                                       |                                                                |          |                                        |                                      |                                   |

(1) Includes amount over and under normal operating.

## Embedded Analog Output Module Data (1) ) - CompactLogix 5370 L2 Controllers

| Input Value                                                                 | Output Range State                                                    |                                                                                |                                                                                          |                               |                               |
|-----------------------------------------------------------------------------|-----------------------------------------------------------------------|--------------------------------------------------------------------------------|------------------------------------------------------------------------------------------|-------------------------------|-------------------------------|
| Controller Ordered Controller Ordered                                       | Controller Ordered                                                    | Embedded Analog Module Output                                                  | Controller Ordered Analog Module Output Controller Ordered Embedded Analog Module Output | Embedded Analog Module Output | Embedded Analog Module Output |
| Over 10.5V +11.0V +10.5V Over – – 11000 – 17202 – 11000 –                   |                                                                       |                                                                                |                                                                                          |                               |                               |
| +10.5V +10.5V +10.5V Over 32767 32767 10500 10500 16793 16793 10500 10500   |                                                                       |                                                                                |                                                                                          |                               |                               |
|                                                                             |                                                                       |                                                                                | +10.0V +10.0V Normal 31207 31207 10000 10000 16383 16383 10000 10000                     |                               |                               |
| ±10V                                                                        | 0.0V 0.0V Normal 0 0 0 0 8192 8192 0 0                                |                                                                                |                                                                                          |                               |                               |
|                                                                             | -10.0V -10.0V Normal -31207 -31207 -10000 -10000 0 0 -10000 -10000    |                                                                                |                                                                                          |                               |                               |
|                                                                             |                                                                       | -10.5V -10.5V -10.5V Under -32767 -32767 -10500 -10500 -410 -410 -10500 -10500 |                                                                                          |                               |                               |
| Under 10.5V -11.0V -10.5V Under – – -11000 -10500 -819 -410 -11000 -10500   |                                                                       |                                                                                |                                                                                          |                               |                               |
| Over 5.25V 5.5V +5.25V Over – – 5500 5250 18021 17202 11000 10500           |                                                                       |                                                                                |                                                                                          |                               |                               |
| 5.25V 5.25V +5.25V Over 32767 32767 5250 5250 17202 17202 10500 10500       |                                                                       |                                                                                |                                                                                          |                               |                               |
|                                                                             |                                                                       | 5.0V +5.0V Normal 31207 31207 5000 5000 16383 16383 10000 10000                |                                                                                          |                               |                               |
| 0…5.0V                                                                      | 0.0V 0.0V Normal 0 0 0 0 0 0 0 0                                      |                                                                                |                                                                                          |                               |                               |
|                                                                             | -0.5V -0.5V -0.5V Under -3121 -3121 -500 -500 -1638 -1638 -1000 -1000 |                                                                                |                                                                                          |                               |                               |
| Under -0.5V -1.0V -0.5V Under -6241 -3121 -500 -500 -3277 -1638 -2000 -1000 |                                                                       |                                                                                |                                                                                          |                               |                               |
| Over 10.5V 11.0V +10.5V Over                                                |                                                                       | – –                                                                            | 11000 10500 18021 17202 11000 10500                                                      |                               |                               |
| +10.5V +10.5V +10.5V Over 32767 32767 10500 10500 17202 17202 10500 10500   |                                                                       |                                                                                |                                                                                          |                               |                               |
| 0…10.0V                                                                     |                                                                       |                                                                                | +10.0V +10.0V Normal 31207 31207 10000 10000 16383 16383 10000 10000                     |                               |                               |
|                                                                             | 0.0V 0.0V Normal 0 0 0 0 0 0 0 0                                      |                                                                                |                                                                                          |                               |                               |
|                                                                             | -0.5V -0.5V -0.5V Under -1560 -1560 -500 -500 -819 -819 -500 -500     |                                                                                |                                                                                          |                               |                               |
| Under -5.0V -1.0V -0.5V Under -3121 -1560 -1000 -500 -1638 -819 -1000 -500  |                                                                       |                                                                                |                                                                                          |                               |                               |
| Over 21.0 mA +22.0 mA 21 mA Over – – 22000 21000 18431 17407 11250 10625    |                                                                       |                                                                                |                                                                                          |                               |                               |
| 21.0 mA +21.0 mA 21 mA Over 32767 32767 21000 21000 17407 17407 10625 10625 |                                                                       |                                                                                |                                                                                          |                               |                               |
|                                                                             |                                                                       |                                                                                | +20.0 mA 20 mA Normal 31207 31207 20000 20000 16383 16383 10000 10000                    |                               |                               |
| 4…20.0 mA                                                                   | +4.0 mA +4.0 mA Normal 6241 6241 4000 4000 0 0 0 0                    |                                                                                |                                                                                          |                               |                               |
| 3.2 mA +3.2 mA +3.2 mA Under 4993 4993 3200 3200 -819 -819 -500 -500        |                                                                       |                                                                                |                                                                                          |                               |                               |
| Under 3.2 0.0 mA +3.2 mA Under 0 4993 0 3200 -4096 -819 -2500 -500          |                                                                       |                                                                                |                                                                                          |                               |                               |
| Over 5.25V +5.5V +5.25V Over – – 5500 5250 18431 17407 11250 10625          |                                                                       |                                                                                |                                                                                          |                               |                               |
| +5.25V +5.25V +5.25V Over 32767 32767 5250 5250 17407 17407 10625 10625     |                                                                       |                                                                                |                                                                                          |                               |                               |
|                                                                             |                                                                       | +5.0V +5.0V Normal 31207 31207 5000 5000 16383 16383 10000 10000               |                                                                                          |                               |                               |
| 1…5.0V                                                                      | +1.0V +1.0V Normal 6241 6241 1000 1000 0 0 0 0                        |                                                                                |                                                                                          |                               |                               |
|                                                                             | 0.5V +0.5V +0.5V Under 3121 3121 500 500 -2048 -2048 -1250 -1250      |                                                                                |                                                                                          |                               |                               |
| Under 0.5V 0.0V 0.0V Under 0 3121 0 500 -4096 -2048 -2500 -1250             |                                                                       |                                                                                |                                                                                          |                               |                               |
| 21.0 mA 21.0 mA 21 mA Over 32767 32767 21000 21000 17202 17202 10500 10500  |                                                                       |                                                                                | Over 21.0 mA +22.0 mA 21 mA Over – – 22000 21000 18201 17202 11000 10500                 |                               |                               |
| 0…20.0 mA                                                                   |                                                                       |                                                                                | 20.0 mA 20 mA Normal 31207 31207 20000 20000 16383 16383 10000 10000                     |                               |                               |
| Under                                                                       | 0.0 mA 0.0 mA Normal 0 0 0 0 0 0 0 0                                  |                                                                                |                                                                                          |                               |                               |
| 0.0 mA                                                                      | -1.0 mA 0.0 mA Under -1560 0 0 -1000 -819 0 -500 0                    |                                                                                |                                                                                          |                               |                               |

## Embedded HSC Module Specifications CompactLogix 5370 L2 Controllers

| Attribute  1769-L24ER-QBFC1B, 1769-L24ER-QBFC1BK 1769-L27ERM-QBFC1B            |                      |
|--------------------------------------------------------------------------------|----------------------|
| Input Specifications                                                           | Input Specifications |
| Input frequency, max 250 kHz                                                   |                      |
| Input current, max 15 mA per channel                                           |                      |
| Input current, min 6.8 mA                                                      |                      |
| Input voltage range  2.6…30V DC(1)                                             |                      |
| On-state voltage, max 30V DC                                                   |                      |
| On-state current, min 6.8 mA                                                   |                      |
| Off-state voltage, max 1.0V DC                                                 |                      |
| Off-state current, max 1.5 mA                                                  |                      |
| Off-state leakage current, max  1.5 mA                                         |                      |
| Input impedance, nom 1950 Ω                                                    |                      |
| Pulse width, min 2.5 µs                                                        |                      |
| Phase separation, min 1.3 µs                                                   |                      |
| Isolation voltage Type tested at 1200V AC for 60 s; inputs to system backplane |                      |

## Output Specifications

| Output voltage range 5…30V DC              |                                                                                                                              |
|--------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|
| On-state voltage, max User power - 0.1V DC |                                                                                                                              |
| On-state output current, max               | 0.25 A per channel                                                                                                           |
| On-state output current, min               | 1 mA                                                                                                                         |
| On-state voltage drop, max 0.5V DC         |                                                                                                                              |
| Off-state leakage current, max             | 5 µA                                                                                                                         |
| Turn-on time, max 400 µs                   |                                                                                                                              |
| Turn-off time, max 200 µs                  |                                                                                                                              |
| Reverse polarity protection 30V DC         |                                                                                                                              |
| Isolation voltage                          | 75V (continuous), reinforced insulation type Type tested at 1200V AC for 60 s; inputs to system backplane and input to input |
| Current per channel, max                   | 1.0 A @ 40 °C (104 °F) 0.5 A @ 55 °C (131 °F) 0.25 A @ 60 °C (140 °F)                                                        |
| Current per module, max                    | 4.0 A @ 40 °C (104 °F) 2.0 A @ 55 °C (131 °F) 1.0 A @ 60 °C (140 °F)                                                         |

(1) See Maximum Input Voltage - 24V DC Operation temperature derating.

## Embedded HSC Module Temperature Derating

<!-- image -->

| Temperature  Derated Voltage (1)   |
|------------------------------------|
| 40 °C (104 °F) 30V DC              |
| 55 °C (131 °F) 26.4V DC            |
| 60 °C (140 °F) 5V DC               |

(1) You achieve an input voltage derating of 55...60 °C (131…140 °F) by using a dropping resistor.

For 24V DC input voltage, use a 2.4 kΩ, 1/2 W resistor.

For input voltages other than 24V DC, use a 1/2 W resistor with value: 125 x (Vin - 5V).

## Maximum Output Voltage - 24V DC Operation

<!-- image -->

| Temperature Derated Voltage    |
|--------------------------------|
| 40 °C (104 °F) 30V DC          |
| 55…60 °C (131…140 °F) 26.4V DC |

## Maximum Input Current Per Point - 5V DC Operation

<!-- image -->

| Temperature Derated Current   |
|-------------------------------|
| 0…40 °C (32…104 °F) 1 A       |
| 60 °C (140 °F) 0.5 A          |

## Maximum Output Current Per Point - 5V DC Operation

<!-- image -->

| Temperature Derated Current   |
|-------------------------------|
| 0…40 °C (32…104 °F) 4 A       |
| 60 °C (140 °F) 2 A            |

## Maximum Output Current Per Point - 24V DC Operation

<!-- image -->

| Temperature Derated Current   |
|-------------------------------|
| 0…40 °C (32…104 °F) 1 A       |
| 55 °C (131 °F) 0.5 A          |
| 60 °C (140 °F) 0.25 A         |

## Maximum Output Current Per Module - 24V DC Operation

<!-- image -->

| Temperature Derated Current   |
|-------------------------------|
| 40 °C (104 °F) 4 A            |
| 55 °C (131 °F) 2 A            |
| 60 °C (140 °F) 1 A            |

## Embedded Power Supply Specifications CompactLogix 5370 L2 Controllers

| Attribute                                 | 1769-L24ER-QB1B                                                                                                                | 1769-L24ER-QBFC1B, 1769- L24ER-QBFC1BK, 1769- L27ERM-QBFC1B                                                                    |
|-------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| Input voltage range                       | 19.2…31.2V DC                                                                                                                  | 19.2…31.2V DC                                                                                                                  |
| Input voltage, nom                        | 24V DC                                                                                                                         | 24V DC                                                                                                                         |
| Line requirement, max (1)                 | 2.1 A @ 24V DC, Class 2/SELV                                                                                                   | 2.1 A @ 24V DC, Class 2/SELV                                                                                                   |
| Available 5V DC bus current 1.54 A 1.0 A  |                                                                                                                                |                                                                                                                                |
| Available 24V DC bus current 0.95 A 0.8 A |                                                                                                                                |                                                                                                                                |
|                                           | Inrush, max < 30 A @ 19.2…31.2V DC                                                                                             | Inrush, max < 30 A @ 19.2…31.2V DC                                                                                             |
| Line loss ride-through 10 ms…10 s         |                                                                                                                                |                                                                                                                                |
| Short circuit protection                  | Internal fuse Not replaceable                                                                                                  | Internal fuse Not replaceable                                                                                                  |
| Overvoltage protection Yes                |                                                                                                                                |                                                                                                                                |
| Isolation voltage                         | 30V AC/30V DC (continuous), reinforced insulation type Type tested at 500V AC or 710V DC for 60 s; outputs to system backplane | 30V AC/30V DC (continuous), reinforced insulation type Type tested at 500V AC or 710V DC for 60 s; outputs to system backplane |

(1) Value rated at the following ambient temperatures: 40 °C (104 °F), 55 °C (131 °F), 60 °C
° (140 °F).

## I/O Module Support - CompactLogix 5370 L3 and Compact GuardLogix 5370 Controllers

The CompactLogix 5370 L3 controllers offer local expansion modules that are installed across up to three banks of modules. You must use 1769 Compact I/O modules with these controllers.

Remember the following when using I/O modules with the CompactLogix 5370 L3 and Compact GuardLogix 5370 controllers:

- The controller must be the leftmost module in the local bank of the system.
- The number of I/O modules that are supported in a controller system varies by controller catalog number.
- You can install I/O modules in as many as three banks, that is, the local bank and two additional banks.
- You can install as many as three I/O modules between the controller and power supply.
- You can install as many as eight I/O modules to the right of the power supply in the local bank.
- You can install as many as eight I/O modules on both the left and right sides of the power supply in additional banks.
- You must consider the distance rating and current draw of the controller and all I/O modules when designing your system.
- Systems with multiple banks can be installed vertically or horizontally.
- You must use expansion cables to connect banks in multi-bank systems.
- You must use an end cap at the end of the last bank in a system.

| Cat. No.                                                                                                                             |   Local 1769 Compact I/O Modules Supported, Max |
|--------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------|
| 1769-L30ER, 1769-L30ERK 1769-L30ER-NSE 1769-L30ERM, 1769-L30ERMK 1769-L30ERMS                                                        |                                               8 |
| 1769-L33ER, 1769-L33ERK 1769-L33ERM, 1769-L33ERMK 1769-L33ERM, 1769-L33ERMSK                                                         |                                              16 |
| 1769-L36ERM 1769-L36ERMS 1769-L37ERM, 1769-L37ERMK 1768-L37ERMS, 1768-L37ERMSK 1769-L38ERM, 1769-L38ERMK 1769-L38ERMS, 1769-L38ERMSK |                                              30 |

<!-- image -->

## Local I/O Performance of CompactLogix 5370 L3 Controllers

The requested packet interval (RPI) defines the frequency at which the controller sends data to and receives data from I/O modules. In the programming software, you set an RPI rate for each I/O module in your system.

The CompactLogix 5370 L3 controllers always attempt to scan an I/O module at the configured RPI rate. An I/O Task Overlap minor fault occurs if there isn't enough system bandwidth. This fault occurs if other, higher priority tasks help prevent the 1769 Compact I/O subsystem from completing before the next scheduled time for it to run again, which consumes system bandwidth. Higher priority tasks that help prevent the 1769 Compact I/O subsystem task from completing before the next scheduled time for it to run again use up system bandwidth.

For individual I/O modules, a Module RPI Overlap minor fault occurs if there is at least one I/O module that can't be serviced within its RPI time.

The specific configuration parameters for a system determine the impact on actual RPI rates. These configuration factors can impact the effective scan frequency for any individual module:

- Rates at which the RPI rates of other 1769 Compact I/O are set
- Number of other 1769 Compact I/O modules in the system
- Types of other 1769 Compact I/O modules in the system
- Application user task priorities

## RPI Rate Guidelines

| Type of Module Guidelines                             |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|-------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1769 Compact I/O digital and analog (any mix) modules | The following guidelines apply: • 1…2 modules can be scanned in 0.5 ms. • 3…4 modules can be scanned in 1 ms. • 5…30 modules can be scanned in 2 ms. • Some input modules have a fixed 8 ms filter, so selection of a faster RPI has no effect.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| 1769 Compact I/O specialty modules                    | The following conditions apply: • For every full-sized 1769-SDN module in the system, increase the RPI of every other module by 2 ms. • For every 1769-HSC module in the system, increase the RPI of every other module by 1 ms. • For every full-sized 1769-ASCII module system, increase the RPI of every other module by 1 ms. For every 1769-SM2 module in the system, increase the RPI of the other module by 2 ms. For example, the system includes four I/O modules that are configured with an RPI = 1 ms and you add a 1769-SDN module to the system. You must increase the RPI value for  all four I/O modules by 2 ms. Therefore, when the 1769-SDN module is added to the system, the four I/O modules use an RPI = 3 ms. If, in the same system, you add a second 1769-SDN module, the RPI value of the four digital I/O modules is increased to 5 ms. |

You can set individual RPI values of the 1769 Compact I/O module higher than these values. For example, if your application scans one or two modules, you do not have to use RPI values = 0.5 ms. You can set the RPI to a higher value, such as 1.0 ms, if necessary. Remember, higher RPI values result in scanning the data less frequently.

The RPI is asynchronous to the program scan. Other factors, such as program execution duration, affect I/O throughput.

## Minimum Spacing Requirements - CompactLogix 5370 Controllers and Compact GuardLogix 5370 Controllers

<!-- image -->

## Dimensions - CompactLogix 5370 L1 Controllers Dimensions - CompactLogix 5370 L2 Controllers

<!-- image -->

## Dimensions - CompactLogix 5370 L3 Controllers Dimensions - Compact GuardLogix 5370 Controllers Dimensions

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

## Armor CompactLogix and Armor Compact GuardLogix Controllers

<!-- image -->

<!-- image -->

The Armor CompactLogix and Armor Compact GuardLogix controllers extend the CompactLogix platform to the On-Machine™ space, this puts industrial control closer to the application and sometimes onto the machine itself. The safety controllers provide standard and safety memory. The memory that each catalog number supports is listed in the Technical Specifications table on page 27. The controllers also support two independent Ethernet ports to connect to an EtherNet/IP network.

## Features - Armor CompactLogix and Armor Compact GuardLogix Controllers

This safety controller supports the full temperature range as CompactLogix controllers, while offering global certifications and ratings for IP67 dust and water protection. It's certified for use in safety applications up to and including safety integrity level (SIL) 3 and Performance Level (e) in which the de-energized state is the safe state. With so many hardware functions in one device, the Armor CompactLogix and Armor Compact GuardLogix controllers provide the following benefits:

- Minimized cabinet hardware
- Simplified wiring layouts
- No required tools or specialty personnel for component replacement
- Improve Mean Time to Restoration (MTTR)
- Simplified troubleshooting
- Readily available system status without the need to open a cabinet or visit a control room

The Armor CompactLogix and Armor Compact GuardLogix controllers provide memory capacity for the most demanding applications. In some applications, for example, when you use these controllers on a Device Level Ring (DLR) network, resiliency is provided from the loss of one network connection and you can replacement devices while production is in progress.

Similar to the Compact GuardLogix controllers, the Armor Compact GuardLogix controllers offer the standard features of a CompactLogix controller and safety features. One difference is that the Armor Compact GuardLogix controllers can use I/O modules that are on-machine and are accessible over an EtherNet/IP network.

| Feature                                       | 1769-L33ERMO 1769-L36ERMO 1769-L37ERMO 1769-L38ERMO                                                                                                                                                                                                                       | 1769-L33ERMOS 1769-L36ERMOS 1769-L37ERMOS 1769-L38ERMOS                                                                                                                                                                                                                   |
|-----------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Controller tasks                              |                                                                                                                                                                                                                                                                           |                                                                                                                                                                                                                                                                           |
| Continuous Periodic                           | 32 tasks 100 programs/task                                                                                                                                                                                                                                                | 32 tasks 100 programs/task                                                                                                                                                                                                                                                |
| Built-in communication ports                  | • Two Ethernet ports - CompactLogix 5370 controllers have two Ethernet ports. The ports carry the same network traffic as part of the embedded switch of the controller. However, the controller uses only one IP address. • One USB port (only for temporary connection) | • Two Ethernet ports - CompactLogix 5370 controllers have two Ethernet ports. The ports carry the same network traffic as part of the embedded switch of the controller. However, the controller uses only one IP address. • One USB port (only for temporary connection) |
| Communication options EtherNet/IP             |                                                                                                                                                                                                                                                                           |                                                                                                                                                                                                                                                                           |
| EtherNet/IP node, max                         | • 1769-L33ERMO, 1769-L33ERMOS: Up to 32 nodes • 1769-L36ERMO, 1769-L36ERMOS: Up to 48 nodes • 1769-L37ERMO, 1769-L37ERMOS: Up to 64 nodes • 1769-L38ERMO, 1769-L38ERMOS: Up to 80 nodes                                                                                   | • 1769-L33ERMO, 1769-L33ERMOS: Up to 32 nodes • 1769-L36ERMO, 1769-L36ERMOS: Up to 48 nodes • 1769-L37ERMO, 1769-L37ERMOS: Up to 64 nodes • 1769-L38ERMO, 1769-L38ERMOS: Up to 80 nodes                                                                                   |
| Controller connections 256                    |                                                                                                                                                                                                                                                                           |                                                                                                                                                                                                                                                                           |
| Sockets, max 32                               |                                                                                                                                                                                                                                                                           |                                                                                                                                                                                                                                                                           |
| Integrated Motion over an EtherNet/IP network | • 1769-L33ERMO, 1769-L33ERMOS: As many as 8 axes • 1769-L36ERMO, 1769-L36ERMOS: As many as 16 axes • 1769-L37ERMO, 1769-L37ERMOS: As many as 16 axes • 1769-L38ERMO, 1769-L38ERMOS: As many as 16 axes                                                                    | • 1769-L33ERMO, 1769-L33ERMOS: As many as 8 axes • 1769-L36ERMO, 1769-L36ERMOS: As many as 16 axes • 1769-L37ERMO, 1769-L37ERMOS: As many as 16 axes • 1769-L38ERMO, 1769-L38ERMOS: As many as 16 axes                                                                    |
| Programming languages                         | • Relay ladder (1) • Structured Text • Function block • SFC                                                                                                                                                                                                               | • Relay ladder (1) • Structured Text • Function block • SFC                                                                                                                                                                                                               |
| Integrated safety — Yes                       |                                                                                                                                                                                                                                                                           |                                                                                                                                                                                                                                                                           |

- (1) The Armor Compact GuardLogix controllers support only the relay ladder programming language in the safety task. The Armor Compact GuardLogix controllers support all listed programming languages in the standard task.

## Certifications - Armor CompactLogix and Armor Compact GuardLogix Controllers

| Certification(1)                        | 1769-L33ERMO 1769-L36ERMO 1769-L37ERMO 1769-L38ERMO                                                                                                                                                                                 | 1769-L33ERMOS 1769-L36ERMOS 1769-L37ERMOS 1769-L38ERMOS                                                                                                                                                                                                                                                                                                                                                                                                            |
|-----------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| c-UL-us                                 | UL Listed Industrial Control Equipment, certified for US and Canada. See UL File E65584.                                                                                                                                            | UL Listed Industrial Control Equipment, certified for US and Canada. See UL File E65584.                                                                                                                                                                                                                                                                                                                                                                           |
| UKCA and CE                             | UK Statutory Instrument 2016 No. 1091 and European Union 2014/30/EU EMC Directive, compliant with: EN 61131-2; Programmable Controllers (Clause 8, Zone A & B) EN 61000-6-4; Industrial Emissions EN 61000-6-2; Industrial Immunity | UK Statutory Instrument 2016 No. 1091 and European Union 2014/30/EU EMC Directive, compliant with: EN 61131-2; Programmable Controllers (Clause 8, Zone A & B) EN 61326-3-1; Meas./Control/Lab., Immunity Requirements for safety systems and functions EN 61000-6-4; Industrial Emissions EN 61000-6-2; Industrial Immunity UK Statutory Instrument 2008 No. 1597 and European Union 2006/42/ EC MD Directive, compliant with: EN 61508-1…7; General requirements |
| UKCA and CE                             | UK Statutory Instrument 2012 No. 3032 and European Union 2011/65/EU RoHS Directive, compliant with:                                                                                                                                 | UK Statutory Instrument 2012 No. 3032 and European Union 2011/65/EU RoHS Directive, compliant with:                                                                                                                                                                                                                                                                                                                                                                |
| RCM                                     | Australian Radiocommunications Act, compliant with: EN 61000-6-4; Industrial Emissions                                                                                                                                              | Australian Radiocommunications Act, compliant with: EN 61000-6-4; Industrial Emissions                                                                                                                                                                                                                                                                                                                                                                             |
| TÜV certified for Functional Safety (2) | –                                                                                                                                                                                                                                   | Capable of Cat. 4/PL e according to EN ISO 13849-1 and SIL 3 according to EN 62061/IEC 61508                                                                                                                                                                                                                                                                                                                                                                       |
| KC                                      | Korean Registration of Broadcasting and Communications Equipment, compliant with:                                                                                                                                                   | Korean Registration of Broadcasting and Communications Equipment, compliant with:                                                                                                                                                                                                                                                                                                                                                                                  |
|                                         | Morocco Arrêté ministériel n° 6404-15 du 29 ramadan 1436                                                                                                                                                                            | Morocco Arrêté ministériel n° 6404-15 du 29 ramadan 1436                                                                                                                                                                                                                                                                                                                                                                                                           |

## Environmental Specifications - Armor CompactLogix and Armor Compact GuardLogix Controllers

| Feature                                                                                                                                                                       | 1769-L33ERMO, 1769-L33ERMOS 1769-L36ERMO, 1769-L36ERMOS 1769-L37ERMO, 1769-L37ERMOS 1769-L38ERMO, 1769-L38ERMOS   |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|
| Temperature, operating IEC 60068-2-1 (Test Ad, Operating Cold) IEC 60068-2-2 (Test Bd, Operating Dry Heat) IEC 60068-2-14 (Test Na, Operating Thermal Shock)                  | 0 °C < Ta < 60 °C (32 °F < Ta < 140 °F)                                                                           |
| Temperature, ambient, max 60 °C (140 °F)                                                                                                                                      |                                                                                                                   |
| Temperature, nonoperating IEC 60068-2-1 (Test Ab, Unpackaged Nonoperating Cold) IEC 60068-2-2 (Test Bb, Unpackaged Nonoperating Dry Heat) IEC 60068-2-14 (Test Na, Unpackaged | -40…+85 °C (-40…+185 °F)                                                                                          |
| Relative humidity IEC 60068-2-30 (Test Db, Unpackaged Damp Heat)                                                                                                              | 5…95% noncondensing                                                                                               |
| Vibration IEC 60068-2-6 (Test Fc, Operating)                                                                                                                                  | 2 g @ 10…500 Hz                                                                                                   |
| Shock, operating IEC 60068-2-27 (Test Ea, Unpackaged Shock)                                                                                                                   | 30 g                                                                                                              |
| Shock, nonoperating IEC 60068-2-27 (Test Ea, Unpackaged Shock)                                                                                                                | 30 g                                                                                                              |
|                                                                                                                                                                               | Emissions IEC 61000-6-4                                                                                           |
| ESD immunity IEC 61000-4-2                                                                                                                                                    | 6 kV contact discharges 8 kV air discharges                                                                       |
| Radiated RF immunity IEC 61000-4-3                                                                                                                                            | 10V/m with 1 kHz sine wave 80% AM from 80…6000 MHz                                                                |
| EFT/B immunity IEC 61000-4-4                                                                                                                                                  | ±3 kV at 5/100 kHz on power ports ±3 kV at 5/100 kHz on Ethernet ports                                            |
| Surge transient immunity IEC 61000-4-5                                                                                                                                        | ±1 kV line-line (DM) and ± 2 kV line-earth (CM) on power ports ±2 kV line-earth (CM) on Ethernet ports            |
| Conducted RF immunity IEC 61000-4-6                                                                                                                                           | 10V rms with 1 kHz sine wave 80% AM from 150 kHz…80 MHz                                                           |

## Technical Specifications - Armor CompactLogix and Armor Compact GuardLogix Controller

| Attribute                            | 1769-L33ERMO 1769-L36ERMO 1769-L37ERMO 1769-L38ERMO                                                                                                                                                                                                                                                                                                                                                    | 1769-L33ERMOS 1769-L36ERMOS 1769-L37ERMOS 1769-L38ERMOS                                                                                                                                                                                                                                                                                                                                                |
|--------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| User memory                          | • 1769-L33ERMO: 2 MB • 1769-L36ERMO: 3 MB • 1769-L37ERMO: 4 MB • 1769-L38ERMO: 5 MB                                                                                                                                                                                                                                                                                                                    | • 1769-L33ERMOS: 2 MB standard + 1 MB safety • 1769-L36ERMOS: 3 MB standard + 1.5 MB safety • 1769-L37ERMOS: 4 MB standard + 1.5 MB safety • 1769-L38ERMO: 5 MB + 1.5 MB safety                                                                                                                                                                                                                        |
| Optional nonvolatile memory          | • 1784-SD1 card with 1 Gb of available memory (shipped with controller) • 1784-SD2 card with 2 Gb of available memory (available for separate ordering)                                                                                                                                                                                                                                                | • 1784-SD1 card with 1 Gb of available memory (shipped with controller) • 1784-SD2 card with 2 Gb of available memory (available for separate ordering)                                                                                                                                                                                                                                                |
| Voltage and current ratings          | IN (Pins 2, 3) 18…32V DC, 8 A SELV IN (Pins 1, 4) 18…32V DC, 8 A SELV Out (Pins 1, 4) 18…32V DC, 8 A Out (Pins 2, 3) 18…32V DC, 6 A                                                                                                                                                                                                                                                                    | IN (Pins 2, 3) 18…32V DC, 8 A SELV IN (Pins 1, 4) 18…32V DC, 8 A SELV Out (Pins 1, 4) 18…32V DC, 8 A Out (Pins 2, 3) 18…32V DC, 6 A                                                                                                                                                                                                                                                                    |
| Power dissipation, max 7.5 W         |                                                                                                                                                                                                                                                                                                                                                                                                        |                                                                                                                                                                                                                                                                                                                                                                                                        |
| Power consumption, max 50VA @ 24V DC |                                                                                                                                                                                                                                                                                                                                                                                                        |                                                                                                                                                                                                                                                                                                                                                                                                        |
| Isolation voltage                    | 30V (continuous), Basic Insulation Type, Power to enclosure, Ethernet channels to Power, and non-redundant Ethernet channels to non-redundant Ethernet channels. No isolation between redundant Ethernet channels. Type tested at 2257V rms for 60 seconds between Input and pass through power to Ethernet ports. Type tested at 2257V rms for 60 seconds between Input power and pass through power. | 30V (continuous), Basic Insulation Type, Power to enclosure, Ethernet channels to Power, and non-redundant Ethernet channels to non-redundant Ethernet channels. No isolation between redundant Ethernet channels. Type tested at 2257V rms for 60 seconds between Input and pass through power to Ethernet ports. Type tested at 2257V rms for 60 seconds between Input power and pass through power. |
| Weight, approx (with mounting feet)  | 5.40 kg (11.90 lb)                                                                                                                                                                                                                                                                                                                                                                                     | 5.62 kg (12.40 lb)                                                                                                                                                                                                                                                                                                                                                                                     |
| Module location Panel mount          |                                                                                                                                                                                                                                                                                                                                                                                                        |                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                      | Panel-mount screw torque 6.6 N•m (58 lb•in) - use M6 screw                                                                                                                                                                                                                                                                                                                                             | Panel-mount screw torque 6.6 N•m (58 lb•in) - use M6 screw                                                                                                                                                                                                                                                                                                                                             |
| Wire category (1)                    | 3 - on USB ports 2 - on power ports 2 - on Ethernet ports                                                                                                                                                                                                                                                                                                                                              | 3 - on USB ports 2 - on power ports 2 - on Ethernet ports                                                                                                                                                                                                                                                                                                                                              |
| Wire type, Ethernet                  | RJ45 connector according to IEC 60603- 7, 2 or 4 pair Category 5e minimum cable according to TIA 568-B.1 or Category 5 cable according to ISO/IEC 24702                                                                                                                                                                                                                                                | M12, D-code, IP67 rated, quick disconnect cables Input and pass-through power connections are made via MINI sized, D-code, IP67 rated, quick disconnect cables                                                                                                                                                                                                                                         |
| Wire size                            | PE Ground: 1.3…5.2 mm² (16…10 AWG) Torque grounding screw to 2.0 N•m (17.7 lb•in)                                                                                                                                                                                                                                                                                                                      | PE Ground: 1.3…5.2 mm² (16…10 AWG) Torque grounding screw to 2.0 N•m (17.7 lb•in)                                                                                                                                                                                                                                                                                                                      |
| Enclosure type rating                | UL Type 4x Meets IP67 (when marked) with receptacle dust caps or cable termination                                                                                                                                                                                                                                                                                                                     | UL Type 4x Meets IP67 (when marked) with receptacle dust caps or cable termination                                                                                                                                                                                                                                                                                                                     |

## Minimum Spacing Requirements - Armor CompactLogix Controllers and Armor Compact GuardLogix Controllers

<!-- image -->

## Dimensions - Armor CompactLogix Controllers and Armor Compact GuardLogix Controllers

z

## Armor CompactLogix Controllers

<!-- image -->

<!-- image -->

## Armor Compact GuardLogix Controllers

<!-- image -->

<!-- image -->

## 1769 Packaged CompactLogix Controllers with Embedded I/O

<!-- image -->

The 1769-L23x controllers provide the following functionality:

- Built-in power supply
- Either two serial ports or one serial and one Ethernet port, depending on controller catalog number
- Combination of embedded digital, analog, and high-speed counter module I/O modules
- 1769-ECR right-end cap

## Features - 1769 Packaged CompactLogix Controllers

|                              |                                                     | Characteristic 1769-L23E-QB1B 1769-L23E-QBFC1B 1769-L23-QBFC1B                           |                                                                                          |
|------------------------------|-----------------------------------------------------|------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------|
| Available user memory 512 KB |                                                     |                                                                                          |                                                                                          |
| CompactFlash card –          |                                                     |                                                                                          |                                                                                          |
| Communication ports          | 1 Ethernet port 1 RS-232 serial port (DF1 or ASCII) | 1 Ethernet port 1 RS-232 serial port (DF1 or ASCII)                                      | 2 RS-232 ports (isolated DF1 or ASCII; only nonisolated DF1)                             |
| Embedded I/O                 | 16 DC inputs 16 DC outputs                          | 16 DC inputs 16 DC outputs 4 analog inputs 2 analog outputs 4 high-speed counter modules | 16 DC inputs 16 DC outputs 4 analog inputs 2 analog outputs 4 high-speed counter modules |
| Module expansion capacity    | Up to three additional 1769 modules                 | Up to two additional 1769 modules                                                        | Up to two additional 1769 modules                                                        |
| Embedded power supply 24V DC |                                                     |                                                                                          |                                                                                          |

You can add one or two additional 1769 modules to the right of the controller package. The modules that you can add depend on their current draw. Each packaged controller has the following amount of 5V DC bus current.

## 1769-L23x Available DC Current

| Controller Available 5V DC Bus Current   |
|------------------------------------------|
| 1769-L23E-QB1B 1000 mA                   |
| 1769-L23E-QBFC1B 450 mA                  |
| 1769-L23-QBFC1B 800 mA                   |

## Local I/O Performance 1769 Packaged CompactLogix L23 Controllers

The requested packet interval (RPI) defines the frequency at which the controller sends and receives all I/O data on the backplane. The default RPI is 5 ms. The combination of embedded I/O in the packaged controllers determines the fastest RPI that you can configure.

|                                  | Controller Guideline                                                      |
|----------------------------------|---------------------------------------------------------------------------|
|                                  | 1769-L23E-QB1B 1…4 modules can be scanned in 1.0 ms                       |
| 1769-L23E-QBFC1B 1769-L23-QBFC1B | 1…4 modules can be scanned in 1.5 ms 5…6 modules can be scanned in 2.0 ms |

You can always select an RPI that is slower than listed previously. These considerations show how fast modules can be scanned—not how fast an application can use the data. The RPI is asynchronous to the program scan. Other factors, such as program execution duration, affect I/O throughput.

## Certifications - 1769 Packaged CompactLogix Controllers

| Certification(1)   | 1769-L23-QBFC1B, 1769-L23E-QB1B, 1769-L23E-QBFC1B                                                                                                                                                                                                  |
|--------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| c-UL-us            | UL Listed Industrial Control Equipment, certified for US and Canada. See UL File E65584. UL Listed for Class I, Division 2 Group A,B,C,D Hazardous Locations, certified for U.S. and Canada. See UL File E194810.                                  |
| CE                 | European Union 2004/108/EC EMC Directive, compliant with: EN 61326-1; Meas./Control/Lab., Industrial Requirements EN 61000-6-2; Industrial Immunity EN 61000-6-4; Industrial Emissions EN 61131-2; Programmable Controllers (Clause 8, Zone A & B) |
| RCM                | Australian Radiocommunications Act, compliant with: AS/NZS CISPR 11; Industrial Emissions                                                                                                                                                          |
|                    | EtherNet/IP ODVA conformance tested to EtherNet/IP specifications                                                                                                                                                                                  |
| KC                 | Korean Registration of Broadcasting and Communications Equipment, compliant with: Article 58-2 of Radio Waves Act, Clause 3                                                                                                                        |

- (1) When marked. see the Product Certification link at rok.auto/certifications for Declarations of Conformity, Certificates, and other certification details.

## Environmental Specifications - CompactLogix 5370 Controllers and Compact GuardLogix 5370 Controllers

|                                                                                                                                                                                                        | Attribute 1769-L23-QBFC1B, 1769-L23E-QB1B, 1769-L23E-QBFC1B                                                                                                                                                       |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Temperature, operating IEC 60068-2-1 (Test Ad, Operating Cold), IEC 60068-2-2 (Test Bd, Operating Dry Heat), IEC 60068-2-14 (Test Na, Operating Thermal Shock)                                         | 0…60 °C (32…140 °F)                                                                                                                                                                                               |
| Temperature, storage IEC 60068-2-1 (Test Ab, Unpackaged Nonoperating Cold), IEC 60068-2-2 (Test Bb, Unpackaged Nonoperating Dry Heat), IEC 60068-2-14 (Test Na, Unpackaged Nonoperating Thermal Shock) | -40…+85 °C (-40…+185 °F)                                                                                                                                                                                          |
| Temperature, surrounding air, max                                                                                                                                                                      | 60 °C (140 °F)                                                                                                                                                                                                    |
| Relative humidity IEC 60068-2-30 (Test Db, Unpackaged Damp Heat)                                                                                                                                       | 5…95% noncondensing                                                                                                                                                                                               |
| Vibration IEC 60068-2-6 (Test Fc, Operating)                                                                                                                                                           | 5 g @ 10…500 Hz                                                                                                                                                                                                   |
| Shock, operating IEC 60068-2-27 (Test Ea, Unpackaged Shock)                                                                                                                                            | 20 g - DIN rail 30 g - Panel                                                                                                                                                                                      |
| Shock, nonoperating IEC 60068-2-27 (Test Ea, Unpackaged Shock)                                                                                                                                         | 30 g - DIN rail 40 g - Panel                                                                                                                                                                                      |
| Emissions CISPR 11                                                                                                                                                                                     | IEC 61000-6-4                                                                                                                                                                                                     |
| ESD immunity IEC 61000-4-2                                                                                                                                                                             | 4 kV contact discharges 8 kV air discharges                                                                                                                                                                       |
| Radiated RF immunity IEC 61000-4-3                                                                                                                                                                     | 10V/m with 200 Hz 50% Pulse 100% AM at 900 MHz 10V/m with 200 Hz 50% Pulse 100% AM at 1890 MHz 10V/m with 1 kHz sine wave 80% AM from 80…2000 MHz 10V/m with 1 kHz sine wave 80% AM from 2000…2700 MHz            |
| EFT/B immunity IEC 61000-4-4                                                                                                                                                                           | ±2 kV at 5 kHz on power ports ±2 kV at 5 kHz on signal ports ±2 kV at 5 kHz on communication ports                                                                                                                |
| Surge transient immunity IEC 61000-4-5                                                                                                                                                                 | ±1 kV line-line (DM) and ±2 kV line-earth (CM) on power ports ±1 kV line-line (DM) and ±2 kV line-earth (CM) on signal ports ±2 kV line-earth (CM) on shielded ports ±2 kV line-earth (CM) on communication ports |
| Conducted RF immunity IEC 61000-4-6                                                                                                                                                                    | 10V rms with 1 kHz sine wave 80% AM from 150 kHz…80 MHz                                                                                                                                                           |

## Technical Specifications - 1769 Packaged CompactLogix Controllers

| Attribute                                                            | 1769-L23E-QB1B                                                                                                                                            | 1769-L23E-QBFC1B                                                                                                                                          | 1769-L23-QBFC1B                                                                                                                                                 |
|----------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| User memory                                                          | 512 KB                                                                                                                                                    | 512 KB                                                                                                                                                    | 512 KB                                                                                                                                                          |
| Optional nonvolatile memory                                          | None                                                                                                                                                      | None                                                                                                                                                      | None                                                                                                                                                            |
| Number of expansion I/O modules, max                                 | 3 (limited by current draw of module)                                                                                                                     | 2 (limited by current draw of module)                                                                                                                     | 2 (limited by current draw of module)                                                                                                                           |
| Replacement battery                                                  | 1769-BA                                                                                                                                                   | 1769-BA                                                                                                                                                   | 1769-BA                                                                                                                                                         |
| Current draw @ 5V DC                                                 | 1000 mA 450 mA 800 mA                                                                                                                                     |                                                                                                                                                           |                                                                                                                                                                 |
| Current draw @ 24V DC                                                |                                                                                                                                                           | 700 mA 500 mA 600 mA                                                                                                                                      |                                                                                                                                                                 |
| Power dissipation                                                    |                                                                                                                                                           | 7.01 W 13.58 W 10.73 W                                                                                                                                    |                                                                                                                                                                 |
| Isolation voltage                                                    | 30V (continuous), basic insulation type Type tested at 710V DC for 60 s; RS-232 to system backplane, Ethernet to system backplane, and RS-232 to Ethernet | 30V (continuous), basic insulation type Type tested at 710V DC for 60 s; RS-232 to system backplane, Ethernet to system backplane, and RS-232 to Ethernet | 30V (continuous), basic insulation type Type tested at 710V DC for 60 s; RS-232 channel 0 to system backplane, no isolation between RS-232 channel 1 and system |
| Serial communication ports                                           | CH0 - RS-232 DF1, DH-485, ASCII Fully isolated 38.4 Kbps max                                                                                              | CH0 - RS-232 DF1, DH-485, ASCII Fully isolated 38.4 Kbps max                                                                                              | CH0 - RS-232 DF1, DH-485, ASCII Fully isolated 38.4 Kbps max CH1 - RS-232 DF1, DH-485 Nonisolated 38.4 Kbps max                                                 |
| Serial cables                                                        | 1756-CP3 or 1747-CP3, right angle connector to controller, straight to serial port, 3 m (9.84 ft)                                                         | 1756-CP3 or 1747-CP3, right angle connector to controller, straight to serial port, 3 m (9.84 ft)                                                         | 1756-CP3 or 1747-CP3, right angle connector to controller, straight to serial port, 3 m (9.84 ft)                                                               |
| Weight, approx                                                       | 0.91 kg (2 lb)                                                                                                                                            | 1.22 kg (2.7 lb)                                                                                                                                          | 1.22 kg (2.7 lb)                                                                                                                                                |
| Slot width                                                           | 1                                                                                                                                                         | 1                                                                                                                                                         | 1                                                                                                                                                               |
| Module location                                                      | DIN rail or panel mount                                                                                                                                   | DIN rail or panel mount                                                                                                                                   | DIN rail or panel mount                                                                                                                                         |
|                                                                      | Mounting screw torque 1.1…1.8 N•m (10…16 lb•in) - use M4 or #8 screws                                                                                     | Mounting screw torque 1.1…1.8 N•m (10…16 lb•in) - use M4 or #8 screws                                                                                     | Mounting screw torque 1.1…1.8 N•m (10…16 lb•in) - use M4 or #8 screws                                                                                           |
| Wire category (1)                                                    | 2 - on signal ports 2 - on power ports 2 - on communication ports                                                                                         | 2 - on signal ports 2 - on power ports 2 - on communication ports                                                                                         | 2 - on signal ports 2 - on power ports 2 - on communication ports                                                                                               |
| Wire type, Ethernet                                                  | RJ45 connector according to IEC 60603- 7, 2 or 4 pair Category 5e minimum cable according to TIA 568-B.1 or Category 5 cable according to ISO/IEC 24702   | RJ45 connector according to IEC 60603- 7, 2 or 4 pair Category 5e minimum cable according to TIA 568-B.1 or Category 5 cable according to ISO/IEC 24702   | –                                                                                                                                                               |
| Wire size, DC power                                                  | 0.25…2.5 mm 2  (22…14 AWG) solid or stranded copper wire ° pp rated at 75 °C (167 °F) or greater, 1.2 mm (3/64 in.)                                                                                                                                                           | 0.25…2.5 mm 2  (22…14 AWG) solid or stranded copper wire ° pp rated at 75 °C (167 °F) or greater, 1.2 mm (3/64 in.)                                                                                                                                                           | 0.25…2.5 mm 2  (22…14 AWG) solid or stranded copper wire ° pp rated at 75 °C (167 °F) or greater, 1.2 mm (3/64 in.)                                                                                                                                                                 |
| Wire size, digital I/O connections                                   | 0.5…0.8 mm 2 (20…18 AWG) solid or stranded copper wire ° pp rated at 75 °C (167 °F) or greater, 1.2 mm (3/64 in.) insulation max                                                                                                                                                           | 0.5…0.8 mm 2 (20…18 AWG) solid or stranded copper wire ° pp rated at 75 °C (167 °F) or greater, 1.2 mm (3/64 in.) insulation max                                                                                                                                                           | 0.5…0.8 mm 2 (20…18 AWG) solid or stranded copper wire ° pp rated at 75 °C (167 °F) or greater, 1.2 mm (3/64 in.) insulation max                                                                                                                                                                 |
| Wire size, embedded analog and high-speed counter module connections | 0.5…0.8 mm 2 (20…18 AWG) solid or stranded shielded copper wire rated at 75 °C (167 °F) or greater, 1.2 mm (3/64 in.) insulation max                      | 0.5…0.8 mm 2 (20…18 AWG) solid or stranded shielded copper wire rated at 75 °C (167 °F) or greater, 1.2 mm (3/64 in.) insulation max                      | 0.5…0.8 mm 2 (20…18 AWG) solid or stranded shielded copper wire rated at 75 °C (167 °F) or greater, 1.2 mm (3/64 in.) insulation max                            |
| North American temperature code                                      | T3C                                                                                                                                                       | T3C                                                                                                                                                       | T3C                                                                                                                                                             |
| Enclosure type rating                                                | None (open-style)                                                                                                                                         | None (open-style)                                                                                                                                         | None (open-style)                                                                                                                                               |

## Embedded DC Input Specifications

|                                | Attribute 1769-L23E-QB1B, 1769-L23E-QBFC1B, 1769-L23-QBFC1B                                                                         |
|--------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| Inputs                         | 16 (8 points/group)                                                                                                                 |
| Voltage category               | 24V DC sink/source                                                                                                                  |
| Operating voltage range        | 10…30V DC @ 30 °C (86 °F) 10…26.4V DC @ 60 °C (140 °F)                                                                              |
| Digital filter, off to on      | 0 s, 100 µs, 500 µs, 1 ms, 2 ms                                                                                                     |
| Input delay, off to on         | 100 µs (typical), 300 µs (max)                                                                                                      |
| Digital filter, on to off      | 0 s, 100 µs, 500 µs, 1 ms, 2 ms                                                                                                     |
| Input delay, on to off         | 250 µs (typical), 1 ms (max)                                                                                                        |
| Off-state voltage, max         | 5V DC                                                                                                                               |
| Off-state current, max         | 1.5 mA                                                                                                                              |
| On-state current, min          | 2 mA @ 10V DC                                                                                                                       |
| Inrush current, max            | 250 mA                                                                                                                              |
| Input impedance, max           | 3 kΩ                                                                                                                                |
| Cyclic update time             | 100 µs…750 ms                                                                                                                       |
| Isolation voltage              | 75V (continuous), basic insulation type Type tested at 1200V AC for 60 s; inputs to system backplane and input group to input group |
| IEC input compatibility Type 3 |                                                                                                                                     |
| Isolated groups                | Group 1: inputs 0…7 Group 2: inputs 8…15 Isolated groups operate in either sink or source configurations                            |

## Embedded DC Output Specifications

|                                                  | Attribute 1769-L23E-QB1B, 1769-L23E-QBFC1B, 1769-L23-QBFC1B                                           |
|--------------------------------------------------|-------------------------------------------------------------------------------------------------------|
| Outputs                                          | 16                                                                                                    |
| Voltage category                                 | 24V DC source                                                                                         |
| Operating voltage range                          | 20.4…26.4V DC                                                                                         |
| Output delay, off to on                          | 0.1 ms                                                                                                |
| Output delay, on to off                          | 1.0 ms                                                                                                |
| Off-state leakage current, max 1.0 mA @ 26.4V DC |                                                                                                       |
| On-state current, min 1.0 mA                     |                                                                                                       |
| On-state voltage drop, max                       | 1.0V DC @ 1.0 A                                                                                       |
| Current per point, max                           | 0.5 A @ 60 °C (140 °F) 1.0 A @ 30 °C (86 °F) Also see the derating graphs                             |
| Current per module, max                          | 4.0 A @ 60 °C (140 °F) 8.0 A @ 30 °C (86 °F) Also see the derating graphs on page 31                  |
| Surge current per point                          | 2 A for 10 ms per point, repeatable every 2 s                                                         |
| Load current, min                                | 3 mA per point                                                                                        |
| Isolation voltage                                | 75V (continuous), basic insulation type Type tested at 1200V AC for 60 s; outputs to system backplane |
|                                                  | Isolated groups Group 1: Outputs 0…15 (internally connected to common)                                |
| Pilot duty rating                                | 0.5 A, 24V DC @ 60 °C (140 °F) 1.0 A, 24V DC @ 30 °C (86 °F)                                          |

## Embedded DC Output Temperature Derating

<!-- image -->

## Embedded Analog Input Specifications

|                                          | Attribute 1769-L23E-QB1B, 1769-L23E-QBFC1B, 1769-L23-QBFC1B                                                                         |
|------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| Inputs                                   | 4 differential or single-ended                                                                                                      |
| Input range                              | 0…10.5V 0…21 mA                                                                                                                     |
| Resolution                               | 8 bits plus sign (sign is always positive).                                                                                         |
| Input impedance                          | Voltage: 150 kΩ nom Current: 150 Ω nom                                                                                              |
|                                          | Converter type Successive approximation                                                                                             |
| Response speed per channel 5 ms          |                                                                                                                                     |
| Rated working voltage 30V AC/30V DC      |                                                                                                                                     |
|                                          | Common mode voltage 10V DC max per channel                                                                                          |
| Common mode rejection                    | Greater than 60 dB at 60 Hz at 10V between inputs and analog common                                                                 |
| Normal mode rejection ratio None         |                                                                                                                                     |
| Accuracy, overall at 25 °C (77 °F)(1)    | Voltage: ±0.7% full-scale, Current: ±0.6% full-scale                                                                                |
| Accuracy, overall at 0…60 °C (32…140 °F) | Voltage: ±0.9% full-scale, Current: ±0.8% full-scale                                                                                |
|                                          | Accuracy drift Voltage: ±0.006% per °C, Current: ±0.006% per °C                                                                     |
|                                          | Calibration Not required; components provide accuracy                                                                               |
| Non-linearity (in percent full-scale)    | ±0.4%                                                                                                                               |
| Repeatability ±0.4%                      |                                                                                                                                     |
| Overload at input terminals, max         | Voltage: 20V continuous, 0.1 mA Current: 32 mA continuous, +5V DC                                                                   |
|                                          | Channel diagnostics Overrange by bit reporting                                                                                      |
| Isolation voltage                        | 30V (continuous), basic insulation type Type tested at 500V AC for 60 s; inputs to system backplane and outputs to system backplane |

## Embedded Analog Output Specifications

| Attribute                                               | 1769-L23E-QB1B, 1769-L23E-QBFC1B, 1769-L23- QBFC1B                                                                                  |
|---------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| Outputs                                                 | 2 single-ended                                                                                                                      |
| Output range                                            | 0…10.5V 0…21 mA                                                                                                                     |
| Converter type Resistor string                          |                                                                                                                                     |
|                                                         | Resolution, max 8 bits plus sign (sign is always positive, Bit 15 = 0)                                                              |
| Response speed per channel                              | 0.3 ms for rated resistance and rated inductance 3.0 ms for rated capacitance                                                       |
| Current load on voltage output 10 mA max                |                                                                                                                                     |
|                                                         | Resistive load on current output 0…300 Ω (includes wire resistance)                                                                 |
| Load range on voltage output > 1 kΩ at 10V DC           |                                                                                                                                     |
| Inductive load, max (current outputs)                   | 0.1 mH                                                                                                                              |
| Capacitive load, max (voltage outputs)                  | 1 µF                                                                                                                                |
| Accuracy, overall at 25 °C (77 °F)(1)                   | Voltage: ±0.5% full-scale Current: ±0.5% full-scale                                                                                 |
| Accuracy, overall at °° y 0…60 °C (32…140 °F)                                                         | Voltage: ±0.6% full-scale Current: ±1.0% full-scale                                                                                 |
| Accuracy drift with temperature                         | Voltage: ±0.01% full-scale per °C ° gp Current: ±0.01% full-scale per °C                                                                                                                                     |
| Output ripple range 0…50 kHz (referred to output range) | ±0.05%                                                                                                                              |
|                                                         | Non-linearity ±0.4% (in percent full-scale)                                                                                         |
|                                                         | Repeatability ±0.05% (in percent full-scale)                                                                                        |
| Output impedance 10 Ω nom                               |                                                                                                                                     |
| Open and short circuit protection Yes                   |                                                                                                                                     |
| Short circuit, max Current: 40 mA                       |                                                                                                                                     |
| Open circuit, max Voltage: 15V                          |                                                                                                                                     |
| Output response at system power-up and powerdown        | +2.0…-1.0V DC spike for less than 6 ms                                                                                              |
| Isolation voltage                                       | 30V (continuous), basic insulation type Type tested at 500V AC for 60 s; inputs to system backplane and outputs to system backplane |

## Embedded HSC Module Input Specifications

| Attribute 1769-L23E-QB1B, 1769-L23E-QBFC1B, 1769-L23-QBFC1B          |
|----------------------------------------------------------------------|
| Input frequency, max 250 kHz                                         |
| Input current, max 15 mA                                             |
| Input current, min 6.8 mA                                            |
| Input voltage range  -30…+30V DC(1)                                  |
| On-state voltage range 2.6…30V DC                                    |
| On-state current, min 6.8 mA                                         |
| Off-state voltage, max 1.0V DC                                       |
| Off-state current, max 1.5 mA                                        |
| Off-state leakage current, max 1.5 mA                                |
| Input impedance, nom 1950 Ω                                          |
| Pulse width, min 2.5 µs                                              |
| Phase separation, min 1.084 µs                                       |
| Isolation voltage Type tested at 1200V AC for 60 s; inputs to system |

<!-- image -->

## Embedded HSC Module Output Specifications

| Attribute 1769-L23E-QB1B, 1769-L23E-QBFC1B, 1769-L23-QBFC1B                                                                               |
|-------------------------------------------------------------------------------------------------------------------------------------------|
| Output voltage range 5…30V DC                                                                                                             |
| On-state voltage, max User power - 0.1V DC                                                                                                |
| On-state output current, max  1 A per point                                                                                               |
| 4 A per module                                                                                                                            |
| On-state output current, min 1 mA                                                                                                         |
| On-state voltage drop, max 0.5V DC                                                                                                        |
| Off-state leakage current, max 5 µA                                                                                                       |
| Turn-on time, max 400 µs                                                                                                                  |
| Turn-off time, max 200 µs                                                                                                                 |
| Reverse polarity protection 30V DC                                                                                                        |
| Isolation voltage 75V (continuous), basic insulation type Type tested at 1200V AC for 60 s; inputs to system backplane and input to input |

## Embedded HSC Module Temperature Derating

<!-- image -->

| Temperature  Derated Voltage (1)   |
|------------------------------------|
| 0…40 °C (32…104 °F) 30V DC         |
| 55 °C (131 °F) 26.4V DC            |
| 60 °C (140 °F) 5V DC               |

(1) You achieve an input voltage derating 55...60 °C (131…140 °F) by using a drop resistor. For 24V DC input voltage, use a 2.4 kΩ, 1/2 Watt resistor. For input voltages other than 24V DC, use a 1/2 W resistor with value: 125 x (Vin - 5V).

## Maximum Output Voltage - 24V DC Operation

<!-- image -->

| Temperature Derated Voltage    |
|--------------------------------|
| 0…40 °C (32…104 °F) 30V DC     |
| 55…60 °C (131…140 °F) 26.4V DC |

## Maximum Output Current Per Point - 5V DC Operation

<!-- image -->

| Temperature Derated Current   |
|-------------------------------|
| 0…40 °C (32…104 °F) 1 A       |
| 60 °C (140 °F) 0.5 A          |

## Maximum Output Current Per Module - 5V DC Operation

<!-- image -->

| Temperature Derated Current   |
|-------------------------------|
| 0…40 °C (32…104 °F) 4 A       |
| 60 °C (140 °F) 2 A            |

## Maximum Output Current Per Point - 24V DC Operation

<!-- image -->

| Temperature Derated Current   |
|-------------------------------|
| 0…40 °C (32…104 °F) 1 A       |
| 55 °C (131 °F) 0.5 A          |
| 60 °C (140 °F) 0.25 A         |

## Maximum Output Current Per Module - 5V DC Operation

<!-- image -->

| Temperature Derated Current   |
|-------------------------------|
| 0…40 °C (32…104 °F) 4 A       |
| 55 °C (131 °F) 2 A            |
| 60 °C (140 °F) 1 A            |

## Embedded Power Supply

| Attribute                            | 1769-L23E-QB1B, 1769-L23E-QBFC1B, 1769-L23-QBFC1B                                                   |
|--------------------------------------|-----------------------------------------------------------------------------------------------------|
| Input voltage range                  | 19.2…31.2V DC                                                                                       |
| Input voltage, nom                   | 24V AC                                                                                              |
| Line requirement, max 50VA at 24V DC |                                                                                                     |
| Available 5V DC bus current          | 1769-L23E-QB1B: 1 A (1000 mA) 1769-L23E-QBFC1B: 450 mA 1769-L23-QBFC1B: 800 mA                      |
|                                      | Inrush, max 30 A @ 31.2V DC                                                                         |
| Line loss ride-through 10 ms…10 s    |                                                                                                     |
| Output bus current capacity °° p 0…55 °C (32…131 °F) 55…60 °C (131…140 °F)                                      | 2 A @ 5V DC 0.8 A @ 24V DC See temperature derating graphs                                          |
| Load current, min                    | 0 mA @ 5V DC 0 mA @ 24V DC                                                                          |
| Short circuit protection             | Front access fuse Replacement part number: Wickmann 19193-6.3A                                      |
| Overvoltage protection Yes           |                                                                                                     |
| Isolation voltage                    | 75V (continuous), basic insulation type Type tested at 1200V AC for 60 s; power to system backplane |

## Embedded Power Supply Temperature Derating

<!-- image -->

## Minimum Spacing Requirements 1769 Packaged CompactLogix Controllers

<!-- image -->

## Dimensions - 1769 Packaged CompactLogix Controllers

<!-- image -->

## 1769-L23E-QBFC1B

<!-- image -->

<!-- image -->

## 1769 Modular CompactLogix Controllers

<!-- image -->

In a 1769-L3x controller system, the 1769 I/O modules can be placed to the left and the right of the power supply. As many as eight modules can be placed on each side of the power supply.

## Features - 1769 Modular CompactLogix Controllers

| Characteristic 1769-L31 1769-L32C          |                                      |                                 | 1769-L32E, 1769-L32EK               | 1769-L35CR 1769-L35E                |                                     |
|--------------------------------------------|--------------------------------------|---------------------------------|-------------------------------------|-------------------------------------|-------------------------------------|
| Available user memory 512 KB 750 KB 1.5 MB |                                      |                                 |                                     |                                     |                                     |
| CompactFlash card 1784-CF128               |                                      |                                 |                                     |                                     |                                     |
|                                            | 2 RS-232 ports (isolated             | 1 ControlNet port               | 1 Ethernet port                     | 1 ControlNet port                   | 1 Ethernet port                     |
| Communication ports                        | DF1 or ASCII; only nonisolate d DF1) |                                 | 1 RS-232 serial port (DF1 or ASCII) | 1 RS-232 serial port (DF1 or ASCII) | 1 RS-232 serial port (DF1 or ASCII) |
| Module expansion capacity                  | 16 1769 modules 30 1769 modules      | 16 1769 modules 30 1769 modules | 16 1769 modules 30 1769 modules     |                                     |                                     |
| Power supply distance rating               | 4 modules                            | 4 modules                       | 4 modules                           | 4 modules                           | 4 modules                           |

The CompactLogix controller has a power supply distance-rating of four modules. The controller must be the leftmost module in the first bank of the system. The maximum configuration for the first bank of a CompactLogix controller includes the following:

- The controller
- Three I/O modules to the left of the power supply
- Eight I/O modules to the right of the power supply

<!-- image -->

## Local I/O Performance 1769 CompactLogix L3 Controllers

You can configure an individual RPI for each local 1769 Compact I/O module. The RPI defines the frequency at which the controller sends and receives all I/O data on the backplane.

| Type of Module Guideline     |                                                                                                                                                                |
|------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Digital and analog (any mix) | 1…4 modules can be scanned in 1 ms 5…30 modules can be scanned in 2 ms Some input modules have a fixed 8 ms filter, so selection of a faster RPI has no effect |
| Specialty                    | Full-sized 1769-SDN modules add 2 ms per module 1769-HSC modules add 1 ms per module Full-sized 1769-ASCII modules add 1 ms per module                         |

You can always select an RPI that is slower than listed previously. These considerations show how fast modules can be scanned—not how fast an application can use the data. The RPI is asynchronous to the program scan. Other factors, such as program execution duration, affect I/O throughput.

## Certifications - 1769 Modular CompactLogix Controllers

| Certification(1)   | 1769-L31                                                                                                                                                                                                          | 1769-L32C 1769-L35CR                                                                                                                                                                                              | 1769-L32E, 1769-L32EK 1769-L35E                                                                                                                                                                                   |
|--------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| c-UL-us            | UL Listed Industrial Control Equipment, certified for US and Canada. See UL File E65584. UL Listed for Class I, Division 2 Group A,B,C,D Hazardous Locations, certified for U.S. and Canada. See UL File E194810. | UL Listed Industrial Control Equipment, certified for US and Canada. See UL File E65584. UL Listed for Class I, Division 2 Group A,B,C,D Hazardous Locations, certified for U.S. and Canada. See UL File E194810. | UL Listed Industrial Control Equipment, certified for US and Canada. See UL File E65584. UL Listed for Class I, Division 2 Group A,B,C,D Hazardous Locations, certified for U.S. and Canada. See UL File E194810. |
| CE                 | European Union 2004/108/EC EMC Directive, compliant with: EN 61000-6-2; Industrial Immunity EN 61000-6-4; Industrial Emissions                                                                                    | European Union 2004/108/EC EMC Directive, compliant with: EN 61000-6-2; Industrial Immunity EN 61000-6-4; Industrial Emissions                                                                                    | European Union 2004/108/EC EMC Directive, compliant with: EN 61000-6-2; Industrial Immunity EN 61000-6-4; Industrial Emissions                                                                                    |
|                    | EN 61326-1; Meas./Control/Lab., Industrial Requirements EN 61131-2; Programmable Controllers (Clause 8, Zone A & B)                                                                                               | EN 61326-1; Meas./Control/Lab., Industrial Requirements EN 61131-2; Programmable Controllers (Clause 8, Zone A & B)                                                                                               | –                                                                                                                                                                                                                 |
| RCM                | Australian Radiocommunications Act, compliant with: AS/NZS CISPR 11; Industrial Emissions                                                                                                                         | Australian Radiocommunications Act, compliant with: AS/NZS CISPR 11; Industrial Emissions                                                                                                                         | Australian Radiocommunications Act, compliant with: AS/NZS CISPR 11; Industrial Emissions                                                                                                                         |
| EX –               |                                                                                                                                                                                                                   |                                                                                                                                                                                                                   | European Union 94/9/EC ATEX Directive, compliant with: EN 60079-15; Potentially Explosive Atmospheres, Protection ’n’ EN 60079-0; General Requirements (Zone 2) II 3 G Ex nA IIC T4 Gc                            |
| ODVA               | –                                                                                                                                                                                                                 | ControlNet International conformance tested to ControlNet specifications                                                                                                                                          | ODVA conformance tested to EtherNet/IP specifications.                                                                                                                                                            |
| KC                 | Korean Registration of Broadcasting and Communications Equipment, compliant with: Article 58-2 of Radio Waves Act, Clause 3                                                                                       | Korean Registration of Broadcasting and Communications Equipment, compliant with: Article 58-2 of Radio Waves Act, Clause 3                                                                                       | Korean Registration of Broadcasting and Communications Equipment, compliant with: Article 58-2 of Radio Waves Act, Clause 3                                                                                       |

## Environmental Specifications - 1769 Modular CompactLogix Controllers

| Attribute 1769-L31                                                                                                                                                                                     |                                                                                                                                                 | 1769-L32C 1769-L35CR                                                                                                                            | 1769-L32E, 1769-L32EK 1769-L35E                                                                                                                 |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| Temperature, operating IEC 60068-2-1 (Test Ad, Operating Cold), IEC 60068-2-2 (Test Bd, Operating Dry Heat), IEC 60068-2-14 (Test Na, Operating Thermal Shock)                                         | 0…60 °C (32…140 °F)                                                                                                                             | 0…60 °C (32…140 °F)                                                                                                                             | 0…60 °C (32…140 °F)                                                                                                                             |
| Temperature, storage IEC 60068-2-1 (Test Ab, Unpackaged Nonoperating Cold), IEC 60068-2-2 (Test Bb, Unpackaged Nonoperating Dry Heat), IEC 60068-2-14 (Test Na, Unpackaged Nonoperating Thermal Shock) | -40…+85 °C (-40…+185 °F)                                                                                                                        | -40…+85 °C (-40…+185 °F)                                                                                                                        | -40…+85 °C (-40…+185 °F)                                                                                                                        |
| Temperature, surrounding air, max                                                                                                                                                                      | 60 °C (140 °F)                                                                                                                                  | 60 °C (140 °F)                                                                                                                                  | 60 °C (140 °F)                                                                                                                                  |
| Relative humidity IEC 60068-2-30 (Test Db, Unpackaged Damp Heat)                                                                                                                                       | 5…95% noncondensing                                                                                                                             | 5…95% noncondensing                                                                                                                             | 5…95% noncondensing                                                                                                                             |
| Vibration IEC 60068-2-6 (Test Fc, Operating)                                                                                                                                                           | 5 g @ 10…500 Hz                                                                                                                                 | 5 g @ 10…500 Hz                                                                                                                                 | 5 g @ 10…500 Hz                                                                                                                                 |
| Shock, operating IEC 60068-2-27 (Test Ea, Unpackaged Shock)                                                                                                                                            | 20 g - DIN rail 30 g - Panel                                                                                                                    | 20 g - DIN rail 30 g - Panel                                                                                                                    | 20 g - DIN rail 30 g - Panel                                                                                                                    |
| Shock, nonoperating IEC 60068-2-27 (Test Ea, Unpackaged Shock)                                                                                                                                         | 30 g - DIN rail 40 g - Panel                                                                                                                    | 30 g - DIN rail 40 g - Panel                                                                                                                    | 30 g - DIN rail 40 g - Panel                                                                                                                    |
| Emissions CISPR 11                                                                                                                                                                                     | IEC 61000-6-4                                                                                                                                   | IEC 61000-6-4                                                                                                                                   | IEC 61000-6-4                                                                                                                                   |
| ESD immunity IEC 61000-4-2                                                                                                                                                                             | 6 kV contact discharges 8 kV air discharges                                                                                                     | 6 kV contact discharges 8 kV air discharges                                                                                                     | 6 kV contact discharges 8 kV air discharges                                                                                                     |
| Radiated RF immunity IEC 61000-4-3                                                                                                                                                                     | 10V/m with 1 kHz sine wave 80% AM from 80…2000 MHz 10V/m with 200 Hz 50% Pulse 100% AM @ 900 MHz 10V/m with 200 Hz 50% Pulse 100% AM @ 1890 MHz | 10V/m with 1 kHz sine wave 80% AM from 80…2000 MHz 10V/m with 200 Hz 50% Pulse 100% AM @ 900 MHz 10V/m with 200 Hz 50% Pulse 100% AM @ 1890 MHz | 10V/m with 1 kHz sine wave 80% AM from 80…2000 MHz 10V/m with 200 Hz 50% Pulse 100% AM @ 900 MHz 10V/m with 200 Hz 50% Pulse 100% AM @ 1890 MHz |
| Radiated RF immunity IEC 61000-4-3                                                                                                                                                                     | –                                                                                                                                               | –                                                                                                                                               | 3V/m with 1 kHz sine wave 80% AM from 2000…2700 MHz                                                                                             |
| EFT/B immunity IEC 61000-4-4                                                                                                                                                                           | ±2 kV at 5 kHz on communication ports                                                                                                           | ±2 kV at 5 kHz on communication ports                                                                                                           | ±3 kV at 5 kHz on power ports ±3 kV at 5 kHz on communication ports                                                                             |
| Surge transient immunity IEC 61000-4-5                                                                                                                                                                 | Channel 0: ±2 kV line-earth (CM) on shielded ports Channel 1: ±1 kV line-earth (CM) on shielded ports                                           | ±2 kV line-earth (CM) on communication ports                                                                                                    | ±2 kV line-earth (CM) on communication ports                                                                                                    |
| Conducted RF immunity IEC 61000-4-6                                                                                                                                                                    | 10V rms with 1 kHz sine wave 80% AM from 150 kHz…80 MHz                                                                                         | 10V rms with 1 kHz sine wave 80% AM from 150 kHz…80 MHz                                                                                         | 10V rms with 1 kHz sine wave 80% AM from 150 kHz…80 MHz                                                                                         |

## Technical Specifications - 1769 Modular CompactLogix Controllers

| Attribute                                     | 1769-L31                                                                                                        | 1769-L32E, 1769-L32EK                                                                   | 1769-L32C                                                                                                | 1769- L35CR                                                                             | 1769- L35E                                                                              |
|-----------------------------------------------|-----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| User memory                                   | 512 KB                                                                                                          | 750 KB                                                                                  |                                                                                                          | 1.5 MB                                                                                  |                                                                                         |
| Optional nonvolatile memory                   | 1784-CF128                                                                                                      | 1784-CF128                                                                              | 1784-CF128                                                                                               | 1784-CF128                                                                              | 1784-CF128                                                                              |
| Number of I/O modules, max                    | 16 30                                                                                                           | 16 30                                                                                   | 16 30                                                                                                    |                                                                                         |                                                                                         |
| Number of I/O banks, max                      | 3                                                                                                               | 3                                                                                       | 3                                                                                                        | 3                                                                                       | 3                                                                                       |
| Number of expansion I/O modules, max          | 16 - 1769 modules 30 - 1769 modules                                                                             | 16 - 1769 modules 30 - 1769 modules                                                     | 16 - 1769 modules 30 - 1769 modules                                                                      |                                                                                         |                                                                                         |
| Replacement battery                           | 1769-BA                                                                                                         | 1769-BA                                                                                 | 1769-BA                                                                                                  | 1769-BA                                                                                 | 1769-BA                                                                                 |
| Current draw @ 5V DC                          |                                                                                                                 |                                                                                         |                                                                                                          | 330 mA 660 mA 650 mA 680 mA 660 mA                                                      |                                                                                         |
| Current draw @ 24V DC 40 mA 90 mA 40 mA 90 mA |                                                                                                                 |                                                                                         |                                                                                                          |                                                                                         |                                                                                         |
| Power dissipation                             |                                                                                                                 |                                                                                         |                                                                                                          | 2.61 W 5.5 W 4.21 W 4.36 W 5.5 W                                                        |                                                                                         |
|                                               | 30V (continuous), basic insulation type Type tested at 710V DC for 60 s                                         | 30V (continuous), basic insulation type Type tested at 710V DC for 60 s                 | 30V (continuous), basic insulation type Type tested at 710V DC for 60 s                                  | 30V (continuous), basic insulation type Type tested at 710V DC for 60 s                 | 30V (continuous), basic insulation type Type tested at 710V DC for 60 s                 |
| Isolation voltage                             | RS-232 channel 0 to system No isolation between RS 232 channel 1 and system                                                                                                                 | RS-232 to system, Ethernet to system, RS 232 to Ethernet                                                                                         | RS-232 to system, ControlNet to system, RS-232 to ControlNet, ControlNet channel A to ControlNet channel | B                                                                                       | RS-232 to system, Ethernet to system, RS-232 to Ethernet                                |
| Communication ports                           | CH0 - RS-232 DF1, DH-485, ASCII Fully isolated 38.4 Kbps max CH1 - RS-232 DF1, DH-485 Nonisolated 38.4 Kbps max | RS-232 Fully isolated 38.4 Kbps max Ethernet port 10/100 BASE-T                         | RS-232 Fully isolated 38.4 Kbps max ControlNet port                                                      | RS-232 Fully isolated 38.4 Kbps max ControlNet port                                     | RS-232 Fully isolated 38.4 Kbps max Ethernet port 10/100 BASE-T                         |
| Serial cables                                 | 1756-CP3 or 1747-CP3, right angle connector to controller, straight to serial port, 3 m                         | 1756-CP3 or 1747-CP3, right angle connector to controller, straight to serial port, 3 m | 1756-CP3 or 1747-CP3, right angle connector to controller, straight to serial port, 3 m                  | 1756-CP3 or 1747-CP3, right angle connector to controller, straight to serial port, 3 m | 1756-CP3 or 1747-CP3, right angle connector to controller, straight to serial port, 3 m |
| Weight, approx                                | 0.30 kg (0.66 lb)                                                                                               | 0.30 kg (0.66 lb)                                                                       | 0.32 kg (0.70 lb)                                                                                        | 0.32 kg (0.70 lb)                                                                       | 0.30 kg (0.66 lb)                                                                       |
| Slot width                                    | 1                                                                                                               | 1                                                                                       | 1                                                                                                        | 1                                                                                       | 1                                                                                       |
| Module location                               | DIN rail or panel mount                                                                                         | DIN rail or panel mount                                                                 | DIN rail or panel mount                                                                                  | DIN rail or panel mount                                                                 | DIN rail or panel mount                                                                 |
| Panel-mount screw torque                      | 1.1…1.8 N•m (10…16 lb•in) - use M4 or #8 screws                                                                 | 1.1…1.8 N•m (10…16 lb•in) - use M4 or #8 screws                                         | 1.1…1.8 N•m (10…16 lb•in) - use M4 or #8 screws                                                          | 1.1…1.8 N•m (10…16 lb•in) - use M4 or #8 screws                                         | 1.1…1.8 N•m (10…16 lb•in) - use M4 or #8 screws                                         |
| Power supply distance rating                  | 4 modules                                                                                                       | 4 modules                                                                               | 4 modules                                                                                                | 4 modules                                                                               | 4 modules                                                                               |
| Power supply                                  | 1769-PA2, 1769-PB2, 1769-PA4, 1769-PB4                                                                          | 1769-PA2, 1769-PB2, 1769-PA4, 1769-PB4                                                  | 1769-PA2, 1769-PB2, 1769-PA4, 1769-PB4                                                                   | 1769-PA2, 1769-PB2, 1769-PA4, 1769-PB4                                                  | 1769-PA2, 1769-PB2, 1769-PA4, 1769-PB4                                                  |
| Wire category (1)                             | 2 - on communication ports                                                                                      | 2 - on communication ports                                                              | 2 - on communication ports                                                                               | 2 - on communication ports                                                              | 2 - on communication ports                                                              |
| North American temp code                      |                                                                                                                 | T5 T4A                                                                                  | T5 T4A                                                                                                   | T5 T4A                                                                                  | T5 T4A                                                                                  |
| IEC temp code                                 |                                                                                                                 | — T4                                                                                    |                                                                                                          | –                                                                                       | T4                                                                                      |
| Enclosure type rating                         | None (open-style)                                                                                               | None (open-style)                                                                       | None (open-style)                                                                                        | None (open-style)                                                                       | None (open-style)                                                                       |

## Real-time Clock Accuracy

This table lists the real-time clock accuracy specifications for the 1769 Modular CompactLogix controllers.

| Ambient Temperature Accuracy   |
|--------------------------------|
| 0 °C (32 °F) +54…-56 s/mo      |
| 25 °C (77 °F) +9…-124 s/mo     |
| 40 °C (104 °F) -84…-234 s/mo   |
| 55 °C (131 °F) -228…-394 s/mo  |
| 60 °C (140 °F) -287…-459 s/mo  |

## Minimum Spacing Requirements 1769 Modular CompactLogix Controllers

<!-- image -->

## Dimensions - 1769 Modular CompactLogix Controllers

<!-- image -->

## 1768 CompactLogix Controllers

<!-- image -->

The 1768-L4x controller combines both a 1768 backplane and a 1769 backplane. The 1768 backplane supports the 1768 controller, the 1768 power supply, and a maximum of four 1768 modules. The 1769 backplane supports 1769 modules.

## Features - 1768 CompactLogix Controllers

|                                                                                         |                                                                                         | Characteristic 1768-L43 1768-L45 1768-L43S 1768-L45S                                    |                                                                                         |
|-----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| Available user memory 2 MB 3 MB                                                         | 2 MB standard 0.5 MB safety                                                             | 3 MB standard 1 MB safety                                                               |                                                                                         |
| CompactFlash card 1784-CF128                                                            | CompactFlash card 1784-CF128                                                            | CompactFlash card 1784-CF128                                                            | CompactFlash card 1784-CF128                                                            |
| EtherNet/IP (standard and safety) ControlNet (standard and safety) DeviceNet (standard) | EtherNet/IP (standard and safety) ControlNet (standard and safety) DeviceNet (standard) | EtherNet/IP (standard and safety) ControlNet (standard and safety) DeviceNet (standard) | EtherNet/IP (standard and safety) ControlNet (standard and safety) DeviceNet (standard) |
| Serial communication port 1 RS-232 port                                                 | Serial communication port 1 RS-232 port                                                 | Serial communication port 1 RS-232 port                                                 | Serial communication port 1 RS-232 port                                                 |
| Two 1768 modules Sixteen 1769 modules                                                   | Two 1768 modules Sixteen 1769 modules                                                   | Two 1768 modules Sixteen 1769 modules                                                   | Two 1768 modules Sixteen 1769 modules                                                   |
| Power supply distance rating –                                                          | Power supply distance rating –                                                          | Power supply distance rating –                                                          | Power supply distance rating –                                                          |
| Relay ladder Structured Text Function block Sequential Function Chart                   | Standard task: all languages Safety task: relay ladder, safety application instructions | Standard task: all languages Safety task: relay ladder, safety application instructions |                                                                                         |

## Compact GuardLogix Safety System

The Compact GuardLogix controller is a 1768-L4xS CompactLogix controller that provides safety control to achieve SIL 3/PLe according to ISO 13849. A major benefit of this system is that it's still one project; safety and standard control together. See page 3 for more information on how to develop projects with Compact GuardLogix controllers.

## Placement - 1768 CompactLogix L4 Controllers

In a 1768-L4x controller system, place 1768 modules between the power supply and the controller.

<!-- image -->

Place the 1769 modules to the right of the 1768 backplane:

- As many as eight 1769 modules can be attached to the right of the 1768 system.
- The 1769 I/O connected directly to the 1768 backplane does not need a 1769 power supply.
- Additional 1769 modules must be in additional I/O banks.
- Each additional I/O bank must have its own 1769 power supply.

Place the 1769 modules to the right of the controller.

<!-- image -->

## Local I/O Performance - 1768 CompactLogix L4 Controllers

Configure an individual RPI for each local 1769 Compact I/O module. Use the default RPI numbers that the programming software automatically assigns or select faster RPI values as fast as 1 ms. I/O module update times do not affect overall 1768 bus performance in the following situations:

- Use faster RPI values for time critical I/O without impacting overall 1769 Compact I/O performance.
- Use Immediate Output (IOT) instructions for further reduction in I/O module update times.

## Certifications - 1768 CompactLogix Controllers

| Certification(1)      | 1768-L43 1768-L45                                                                                                                                                                                                                                  | 1768-L43S 1768-L45S                                                                                                                                                                                                                                |
|-----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| c-UL-us               | UL Listed Industrial Control Equipment, certified for US and Canada. See UL File E65584. UL Listed for Class I, Division 2 Group A,B,C,D Hazardous Locations, certified for U.S. and Canada. See UL File E194810.                                  | UL Listed Industrial Control Equipment, certified for US and Canada. See UL File E65584. UL Listed for Class I, Division 2 Group A,B,C,D Hazardous Locations, certified for U.S. and Canada. See UL File E194810.                                  |
| CE                    | European Union 2004/108/EC EMC Directive, compliant with: EN 61326-1; Meas./Control/Lab., Industrial Requirements EN 61000-6-2; Industrial Immunity EN 61000-6-4; Industrial Emissions EN 61131-2; Programmable Controllers (Clause 8, Zone A & B) | European Union 2004/108/EC EMC Directive, compliant with: EN 61326-1; Meas./Control/Lab., Industrial Requirements EN 61000-6-2; Industrial Immunity EN 61000-6-4; Industrial Emissions EN 61131-2; Programmable Controllers (Clause 8, Zone A & B) |
|                       |                                                                                                                                                                                                                                                    | European Union 2006/42/EC MD, compliant with: EN 60204-1; Electrical equipment of machines EN ISO 13849-1; Safety-related parts of control systems EN 62061; Functional safety of safety-related control systems                                   |
| RCM                   | Australian Radiocommunications Act, compliant with: AS/NZS CISPR 11; Industrial Emissions                                                                                                                                                          | Australian Radiocommunications Act, compliant with: AS/NZS CISPR 11; Industrial Emissions                                                                                                                                                          |
| Ex –                  |                                                                                                                                                                                                                                                    | European Union 94/9/EC ATEX Directive, compliant with: EN 60079-15; Potentially Explosive Atmospheres, Protection ‘n’ EN60079-0; General Requirements II 3 G Ex nA nL IIC T4 Gc                                                                    |
| KC                    | Korean Registration of Broadcasting and Communications Equipment, compliant with: Article 58-2 of Radio Waves Act, Clause 3                                                                                                                        | Korean Registration of Broadcasting and Communications Equipment, compliant with: Article 58-2 of Radio Waves Act, Clause 3                                                                                                                        |
| Functional Safety (2) | –                                                                                                                                                                                                                                                  | Certified by TÜV: capable of SIL 1 to 3, according to IEC 61508; and PLe/Cat. 4 according to ISO 13849-1                                                                                                                                           |

## Environmental Specifications - 1768 CompactLogix Controllers

|                                                                                                                                                                                                        | Attribute 1768-L43, 1768-L43S, 1768-L45, 1768-L45S                                                                                                                                                  |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Temperature, operating IEC 60068-2-1 (Test Ad, Operating Cold) IEC 60068-2-2 (Test Bd, Operating Dry Heat) IEC 60068-2-14 (Test Na, Operating Thermal Shock)                                           | 0…60 °C (32…140 °F)                                                                                                                                                                                 |
| Temperature, storage IEC 60068-2-1 (Test Ab, Unpackaged Nonoperating Cold), IEC 60068-2-2 (Test Bb, Unpackaged Nonoperating Dry Heat), IEC 60068-2-14 (Test Na, Unpackaged Nonoperating Thermal Shock) | -40…+85 °C (-40…+185 °F)                                                                                                                                                                            |
| Temperature, surrounding air, max                                                                                                                                                                      | 60 °C (140 °F)                                                                                                                                                                                      |
| Relative humidity IEC 60068-2-30 (Test Db, Unpackaged Damp Heat)                                                                                                                                       | 5…95% noncondensing                                                                                                                                                                                 |
| Vibration IEC 60068-2-6 (Test Fc, Operating)                                                                                                                                                           | 5 g @ 10…500 Hz                                                                                                                                                                                     |
| Shock, operating IEC 60068-2-27 (Test Ea, Unpackaged Shock)                                                                                                                                            | 30 g                                                                                                                                                                                                |
| Shock, nonoperating IEC 60068-2-27 (Test Ea, Unpackaged Shock)                                                                                                                                         | 50 g                                                                                                                                                                                                |
| Emissions CISPR 11                                                                                                                                                                                     | IEC 61000-6-4                                                                                                                                                                                       |
| ESD immunity IEC 61000-4-2                                                                                                                                                                             | 6 kV contact discharges 8 kV air discharges                                                                                                                                                         |
| Radiated RF immunity IEC 61000-4-3                                                                                                                                                                     | 10V/m with 1 kHz sine wave 80% AM from 80…2000 MHz 10V/m with 200 Hz 50% Pulse 100% AM @ 900 MHz 10V/m with 200 Hz 50% Pulse 100% AM @ 1890 MHz 3V/m with 1 kHz sine wave 80% AM from 2000…2700 MHz |

## Environmental Specifications - 1768 CompactLogix Controllers

|                                        | Attribute 1768-L43, 1768-L43S, 1768-L45, 1768-L45S      |
|----------------------------------------|---------------------------------------------------------|
| EFT/B immunity IEC 61000-4-4           | ±4 kV at 5 kHz on communication ports                   |
| Surge transient immunity IEC 61000-4-5 | ±2 kV line-earth (CM) on communication ports            |
| Conducted RF immunity IEC 61000-4-6    | 10V rms with 1 kHz sine wave 80% AM from 150 kHz…80 MHz |

## Technical Specifications - 1768 CompactLogix Controllers

| Attribute                                 | 1768-L43                                                                                       | 1768-L43S                                                                                      | 1768-L45                                                                                       | 1768-L45S                                                                                      |
|-------------------------------------------|------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|
| User memory                               | 2 MB                                                                                           | 2 MB standard 0.5 MB safety                                                                    | 3 MB                                                                                           | 3 MB standard 1 MB safety                                                                      |
| Optional nonvolatile memory               | 1784-CF128                                                                                     | 1784-CF128                                                                                     | 1784-CF128                                                                                     | 1784-CF128                                                                                     |
| Number of 1768 modules, max 2 4           |                                                                                                |                                                                                                |                                                                                                |                                                                                                |
| Number of 1768 communication modules, max | 2                                                                                              | 2                                                                                              | 2                                                                                              | 2                                                                                              |
| Number of 1768 motion modules, max        | 2 4                                                                                            | 2 4                                                                                            |                                                                                                |                                                                                                |
| Number of 1769 I/O modules, max 16 30     |                                                                                                |                                                                                                |                                                                                                |                                                                                                |
|                                           | Number of I/O banks, max 2 3                                                                   | Number of I/O banks, max 2 3                                                                   |                                                                                                |                                                                                                |
| Replacement battery                       | –                                                                                              | –                                                                                              | –                                                                                              | –                                                                                              |
| Backplane current draw @ 24V DC           | 1.3 A                                                                                          |                                                                                                | 1.4 A 2.0 A 2.1 A                                                                              |                                                                                                |
| 1768 current draw @ 5V DC                 | 2.8 A 5.6 A                                                                                    | 2.8 A 5.6 A                                                                                    |                                                                                                |                                                                                                |
| 1769 current draw @ 5V DC                 | 2.0 A 2.0 A                                                                                    | 2.0 A 2.0 A                                                                                    |                                                                                                |                                                                                                |
| Total 1768 and 1769 current draw @ 5V DC  | 4.8 A 7.6 A                                                                                    | 4.8 A 7.6 A                                                                                    |                                                                                                |                                                                                                |
| Power dissipation                         | 6.3 W                                                                                          |                                                                                                | 7.5 W 8.3 W 9.5 W                                                                              |                                                                                                |
| Power consumption                         | 31.3 W                                                                                         |                                                                                                |                                                                                                | 33.6 W 48.0 W 50.4 W                                                                           |
| Isolation voltage                         | 30V (continuous), functional insulation type Type tested at 500V AC for 60 s; RS-232 to system | 30V (continuous), functional insulation type Type tested at 500V AC for 60 s; RS-232 to system | 30V (continuous), functional insulation type Type tested at 500V AC for 60 s; RS-232 to system | 30V (continuous), functional insulation type Type tested at 500V AC for 60 s; RS-232 to system |
| Communication ports                       | RS-232 Fully isolated, 38.4 Kbps max                                                           | RS-232 Fully isolated, 38.4 Kbps max                                                           | RS-232 Fully isolated, 38.4 Kbps max                                                           | RS-232 Fully isolated, 38.4 Kbps max                                                           |
| Serial cables                             | 1756-CP3 or 1747-CP3, right angle connector to controller, straight to serial port, 3 m        | 1756-CP3 or 1747-CP3, right angle connector to controller, straight to serial port, 3 m        | 1756-CP3 or 1747-CP3, right angle connector to controller, straight to serial port, 3 m        | 1756-CP3 or 1747-CP3, right angle connector to controller, straight to serial port, 3 m        |
| Weight, approx                            | 0.34 kg (11.99 oz)                                                                             | 0.45 kg (15.9 oz)                                                                              | 0.34 kg (11.99 oz)                                                                             | 0.45 kg (15.9 oz)                                                                              |
| Dimensions (HxWxD)                        | 131.1 x 56.4 x 121.1 mm (5.18 x 2.22 x 4.81 in.)                                               | 131.6 x 89.6 x 122.1 mm (5.18 x 3.53 x 4.81 in.)                                               | 131.1 x 56.4 x 121.1 mm (5.18 x 2.22 x 4.81 in.)                                               | 131.6 x 89.6 x 122.1 mm (5.18 x 3.53 x 4.81 in.)                                               |
| Slot width                                | 1                                                                                              | 1.5 1 1.5                                                                                      |                                                                                                |                                                                                                |
| Module location                           | DIN rail or panel mount                                                                        | DIN rail or panel mount                                                                        | DIN rail or panel mount                                                                        | DIN rail or panel mount                                                                        |
|                                           | Panel-mount screw torque 1.16 N•m (10 lb•in) - use M4 or #8 screws                             | Panel-mount screw torque 1.16 N•m (10 lb•in) - use M4 or #8 screws                             | Panel-mount screw torque 1.16 N•m (10 lb•in) - use M4 or #8 screws                             | Panel-mount screw torque 1.16 N•m (10 lb•in) - use M4 or #8 screws                             |
| Power supply distance rating              | 4 modules                                                                                      | 4 modules                                                                                      | 4 modules                                                                                      | 4 modules                                                                                      |
| Power supply                              | 1768-PA3, 1768-PB3                                                                             | 1768-PA3, 1768-PB3                                                                             | 1768-PA3, 1768-PB3                                                                             | 1768-PA3, 1768-PB3                                                                             |
| Wire category (1)                         | 2 - on communication ports                                                                     | 2 - on communication ports                                                                     | 2 - on communication ports                                                                     | 2 - on communication ports                                                                     |
| IEC temperature code                      | –                                                                                              |                                                                                                |                                                                                                | T4 — T4                                                                                        |
| North American temperature code           | T4                                                                                             | T4                                                                                             | T4                                                                                             | T4                                                                                             |
| Enclosure type rating                     | None (open-style)                                                                              | None (open-style)                                                                              | None (open-style)                                                                              | None (open-style)                                                                              |

## Power Dissipation - 1768 CompactLogix Controllers

## 1768-L43 and 1768-L43S

<!-- image -->

<!-- image -->

## Slot Numbering - 1768 CompactLogix Controllers

<!-- image -->

## Minimum Spacing Requirements - 1768 CompactLogix Controllers

<!-- image -->

## Dimensions - 1768 CompactLogix Controllers

1768-L43 and 1768-L45

<!-- image -->

1768-L43S and 1768-L45S

<!-- image -->

All 1768 L4 Controllers Side View

<!-- image -->

## Controller Memory Use

These equations provide an estimate of the memory that is needed for a controller. These numbers are rough estimates.

| Controller tasks               | _____ * 4000   | =   | _____ bytes (minimum 1 task)   |
|--------------------------------|----------------|-----|--------------------------------|
| Digital I/O points             | _____ * 400    | =   | _____ bytes                    |
| Analog I/O points              | _____ * 2600   | =   | _____ bytes                    |
| DeviceNet modules(1)           | _____ * 7400   | =   | _____ bytes                    |
| Other communication modules(2) | _____ * 2000   | =   | _____ bytes                    |
| Motion axes                    | _____ * 8000   | =   | _____ bytes                    |
| FactoryTalk® alarm instruction | _____ * 1000   | =   | _____ bytes (per alarm)        |
| FactoryTalk subscriber         | _____ * 10000  | =   | _____ bytes                    |

(1) The first DeviceNet module is 7400 bytes. Additional DeviceNet modules are 5800 bytes each.

(2) Count all communication modules in the system, not just the modules in the local chassis. This total includes device connection modules, adapters, and ports on PanelView™ terminals.

Reserve 20…30% of the controller memory for future expansion.

## Controller Compatibility

This section details the other devices that your controller can control and communicate with.

## Control Distributed I/O Modules

The controller can control these distributed I/O modules.

| I/O Modules                              | CompactLogix 5370 1768-ENBT 1769-L23Ex 1769-L32E, 1769-L32EK, 1769-L35E EtherNet/IP Network(1)   | 1768-CNB, 1768-CNBR 1769-L32C, 1769-L35CR ControlNet Network   | CompactLogix 5370 L2 and L3 1769-SDN DeviceNet Network(2) (3)     |
|------------------------------------------|--------------------------------------------------------------------------------------------------|----------------------------------------------------------------|-----|
| Chassis-based I/O                        |                                                                                                  |                                                                |     |
| 1746 SLC™ I/O                            | Yes                                                                                              | No                                                             | No  |
| 1756 ControlLogix® I/O                   | Yes                                                                                              | Yes                                                            | Yes |
| 1769 Compact I/O                         | No                                                                                               | No                                                             | Yes |
| 1771 Universal I/O                       | No                                                                                               | No                                                             | No  |
| In-cabinet I/O                           |                                                                                                  |                                                                |     |
| 1734 POINT I/O                           | Yes                                                                                              | Yes                                                            | Yes |
| 1734D POINTBlock I/O                     | Yes                                                                                              | Yes                                                            | Yes |
| 1790, 1790D, 1790P CompactBlock™ LDX I/O | No                                                                                               | No                                                             | Yes |
| 1791D, 1791P, 1791R CompactBlock I/O     | No                                                                                               | No                                                             | Yes |
| 1794 FLEX™ I/O                           | Yes                                                                                              | Yes                                                            | Yes |
| 1797 FLEX Ex™ I/O                        | Yes                                                                                              | Yes                                                            | No  |
| On-machine I/O                           |                                                                                                  |                                                                |     |
| 1732 ArmorBlock® I/O                     | Yes                                                                                              | No                                                             | Yes |
| 1738 ArmorPOINT® I/O                     | Yes                                                                                              | Yes                                                            | No  |
| 1792D ArmorBlock® MaXum™ I/O             | No                                                                                               | No                                                             | Yes |
| 1799 Embedded I/O                        | No                                                                                               | No                                                             | Yes |

(1) A non-EtherNet/IP CompactLogix controller requires a 1761-NET-ENI interface to connect to an EtherNet/IP network. This interface is only a messaging bridge.

(2) To control I/O, use a 1769-SDN scanner to connect the controller to the DeviceNet network.

(3) The 1769-SDN does not support safety communication to Guard I/O modules on a DeviceNet network.

## Control Safety I/O Modules

The Compact GuardLogix controller can control these safety I/O modules in a safety system.

| I/O Modules                     | EtherNet/IP   | ControlNet   |
|---------------------------------|---------------|--------------|
| 1791ES CompactBlock™ Guard I/O™ | Yes           | No           |
| 1734 POINT Guard I/O™           | Yes           | No           |

## Communicate with Devices

The controller can communicate with these devices.

| Device                                           | EtherNet/IP(1) Network   | ControlNet Network                            | DeviceNet(2) Network             | RS-232 (DF1) Network   | DH-485 Network   |
|--------------------------------------------------|--------------------------|-----------------------------------------------|----------------------------------|------------------------|------------------|
| Programmable controllers                         |                          |                                               |                                  |                        |                  |
| 1756 ControlLogix and 1756 GuardLogix            | Yes                      | Yes                                           | Yes                              | Yes                    | Yes              |
| CompactLogix 5370                                | Yes                      | No                                            | Yes(3)                           | Yes(4)                 | Yes(5)           |
| 1768-L4x CompactLogix                            | Yes                      | Yes                                           | Yes                              | Yes                    | Yes              |
| 1769-L3x CompactLogix                            | Yes                      | Yes                                           | Yes                              | Yes                    | Yes              |
| 1769-L23x CompactLogix                           | Yes                      | No                                            | Yes                              | Yes                    | Yes              |
| 1789 SoftLogix™ 5800                             | Yes                      | Yes                                           | Yes                              | Yes                    | No               |
| 1794 FlexLogix™                                  | Yes                      | Yes                                           | Yes                              | Yes                    | Yes              |
| PowerFlex® with DriveLogix™                      | Yes                      | Yes                                           | Yes                              | Yes                    | Yes              |
| 1785 PLC-5®                                      | Yes(6) (7)                          | Yes                                           | Yes(8)                           | Yes                    | —                |
| 1747 SLC                                         | Yes(9)                   | Yes                                           | Yes(4)                           | Yes                    | Yes              |
| 1761 MicroLogix™                                 | Yes                      | No                                            | Yes(4)                           | Yes                    | Yes              |
| 1762 MicroLogix                                  | Yes                      | No                                            | Yes(4)                           | Yes                    | Yes              |
| 1763 MicroLogix                                  | Yes                      | No                                            | Yes(4)                           | Yes                    | Yes              |
| 1764 MicroLogix                                  | Yes                      | No                                            | Yes(4)                           | Yes                    | Yes              |
| 1772 PLC-2®                                      | –                        | –                                             | –                                | Yes                    | –                |
| 1775 PLC-3®                                      | –                        | –                                             | –                                | Yes                    | –                |
| 5250 PLC-5/250                                   | –                        | –                                             | No                               | Yes                    | –                |
| Industrial Computers                             |                          |                                               |                                  |                        |                  |
| Allen-Bradley® industrial computers (all)( )(10) | Yes                      | Yes                                           | Yes                              | Yes                    | Yes              |
| Graphic Terminals                                |                          |                                               |                                  |                        |                  |
| PanelView™ Plus and PanelView CE terminals       | Yes                      | Yes                                           | Yes                              | Yes                    | Yes              |
| PanelView standard terminals                     | Yes                      | Yes                                           | Yes                              | Yes                    | Yes              |
| PanelView™ e terminals                           | No                       | No                                            | No                               | No                     | No               |
| Message Displays                                 |                          |                                               |                                  |                        |                  |
| InView™ message displays                         | Yes                      | Yes                                           | Yes                              | Yes                    | Yes              |
| Communication Devices                            |                          |                                               |                                  |                        |                  |
| Linking device (only ControlLogix controllers)   | 1788-EN2DN               | 1788-CN2DN 1788-CN2FF                         | 1788-EN2DN(11) 1788-CN2DN        |                        |                  |
| PCMCIA card                                      | –                        | 1784-PCC                                      | 1784-PCD                         |                        |                  |
| PCI card                                         |                          | 1784-PCIC 1784-PCICS                          | 1784-PCID 1784-PCIDS 1784-CPCIDS |                        |                  |
| Drives SCANport™ module                          |                          | 1203-FM1 1203-FB1(12)                         | –                                |                        |                  |
| Communication module                             |                          | 1203-CN(13) 1770-KFC15 1770-KFCD15 1747-KFC15 | 1770-KFD 1770-KFG                |                        |                  |
| Communication card                               |                          | 1784-PKTCS 1784-KTCS 1784-KTCX15              | 1784-PKTX 1784-PKTXD             |                        |                  |
| USB communication device                         |                          | 1784-U2CN                                     | 1784-U2DN                        |                        |                  |

(1) A non-EtherNet/IP CompactLogix controller requires a 1761-NET-ENI interface to connect to an EtherNet/IP network. This interface is only a messaging bridge.

(2) For DeviceNet access, use either a 1769-SDN scanner (control I/O and send/receive messages) or a 1761-NET-DNI interface (messaging bridge).

(3) The CompactLogix 5370 L1 controllers can't access a DeviceNet network and, therefore, can't communicate with other controllers on a DeviceNet network.

(4) The CompactLogix 5370 controllers do not have an embedded serial port. You must add external modules to communicate over an RS-232 (DF1) network.

(5) The CompactLogix 5370 controllers do not have an embedded serial port. You must add external modules to communicate over a DH-485 network.

(6) The Ethernet PLC-5 controller must be series C, firmware revision N.1 or later; series D, firmware revision E.1 or later; or series E, firmware revision D.1 or later.

(7) The 1785-ENET Ethernet communication interface module must be series A, firmware revision D or later.

(8) The PLC-5, SLC, and MicroLogix processors appear as I/O points to the Logix controller. Use the appropriate DeviceNet interface for the controller.

(9) Use a 1747-L55x controller with OS501 or later.

(10) Includes: Allen-Bradley integrated display computers with rotating media (HDD) or solid-state drives (SSD), Allen-Bradley non-display computers, and Allen-Bradley integrated display computers with keypad.

(11) The 1788-EN2DN does not support safety communication (CIP Safety™).

(12) Use a CIP™ generic MSG instruction to communicate with the 1203-FM1 SCANport module on a DIN rail that is remote to the controller. The remote DIN rail also requires a 1794-ACN15 or 1794ACNR15 ControlNet adapter.

(13) Use the generic module configuration to configure the 1203-CN1 module and a CIP generic MSG instruction to communicate with the module.

## Controller Connections

|                                                                                                   | • Controller-to-local I/O modules or local communication modules • Controller-to-remote I/O or remote communication modules                                                                                               |
|---------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| A CompactLogix system uses the connection types to establish communication links between devices: | • Controller-to-remote I/O (rack-optimized) modules • Produced and consumed tags • Messages • Controller access by the programming software • Controller access by RSLinx® Classic software for HMI or other applications |

You indirectly determine the number of connections the controller uses by configuring the controller to communicate with other devices in the system. The limit of connections can ultimately reside in the communication module you use for the connection. If a message path routes through a communication module, the connection that is related to the message also counts toward the connection limit of that communication module.

## CompactLogix 5370 Controller Ethernet Node Limits and Connections

| When designing a CompactLogix 5370 control system, you must consider the following:   | • Maximum number of Ethernet nodes available for the project of your controller • Connections   |
|---------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|

The controller that you select determines the number of Ethernet nodes available.

|                                                                      | Cat. No. Ethernet Nodes Supported   |
|----------------------------------------------------------------------|-------------------------------------|
| 1769-L16ER-BB1B 4                                                    |                                     |
| 1769-L18ER-BB1B 1769-L18ERM-BB1B, 1769-L18ERM-BB1BK                  | 8                                   |
| 1769-L24ER-QB1B 8 1769-L24ER-QBFC1B, 1769-L24ER-QBFC1BK              |                                     |
| 1769-L27ERM-QBFC1B 1769-L30ER, 1769-L30ERK 1769-L30ERM, 1769-L30ERMK | 16                                  |
| 1769-L30ER-NSE 1769-L33ER, 1769-L33ERK                               | 32                                  |
| 1769-L33ERM, 1769-L33ERMK                                            |                                     |
| 1769-L36ERMO 1769-L37ERM, 1769-L37ERMK 1769-L37ERMO(1)               | 48 64                               |
|                                                                      | 80                                  |
| 1769-L38ERM, 1769-L38ERMK                                            |                                     |
| 1769-L38ERMO(1)                                                      |                                     |

All CompactLogix 5370 controllers support 256 CIP™ connections and 120 TCP/IP connections.

## 1769-L23x CompactLogix Connections

The controller that you select determines the connections for I/O and messages.

| Controller Supports                  |
|--------------------------------------|
| 1769-L23EQB1B  32 CIP connections    |
| 8 TCP/IP connections 1769-L23EQBFC1B |

The total connection requirements for a 1769 CompactLogix system include both local and remote (distributed) connections. The controller supports 100 connections. The available remote connections depend on the network interface.

## 1769-L3x CompactLogix Connections

The controller that you select determines the connections for I/O and messages.

| Controller Supports             |                                          |
|---------------------------------|------------------------------------------|
| 1769-L32C 1769-L35CR            | 32 CIP connections                       |
| 1769-L32E, 1769-L32EK 1769-L35E | 32 CIP connections 32 TCP/IP connections |

The total connection requirements for a 1769 CompactLogix system include both local and remote (distributed) connections. The controller supports 100 connections. The available remote connections depend on the network interface.

## 1768-L4x CompactLogix Connections

The communication module that you select determines the connections for I/O and messages.

| Communication Module Supports   |                                           |
|---------------------------------|-------------------------------------------|
| 1768-ENBT 1768-EWEB             | 128 CIP connections 64 TCP/IP connections |
| 1768-CNB 1768-CNBR              | 48 CIP connections                        |

The total connection requirements for a 1768 CompactLogix system include both local and remote (distributed) connections. The controller supports 250 connections. The available remote connections depend on the network interface.

(1) Available at software version 31 and firmware revision 31.

## Determine Total Connection Use

The total connection requirements for a CompactLogix system include remote (distributed) connections. The available remote connections depend on the network interface.

The controllers support these numbers of total connections:

- 1769-L23x and 1769-L3x controllers support 100 total connections.
- 1768-L4x controllers support 250 total connections.
- CompactLogix 5370 controllers support 256 total connections.

When designing your CompactLogix system, to estimate the number of connections per connection type and the total connections that are used, use this table or the EtherNet/IP Capacity Tool Wizard that is embedded in the Integrated Architecture® Builder (IAB) software from Rockwell Automation.

| Connection Type                                                                                                           | Device Quantity   | Connections Per Device Total Connections   |
|---------------------------------------------------------------------------------------------------------------------------|-------------------|--------------------------------------------|
| Remote ControlNet communication module Configured as a direct (none) connection Configured as a rack-optimized connection |                   | 0 1                                        |
| Remote I/O module over a ControlNet network (direct connection)                                                           |                   | 1                                          |
| Remote Ethernet communication module Configured as a direct (none) connection Configured as a rack-optimized connection   |                   | 0 1                                        |
| Remote I/O module over an EtherNet/IP network (Direct connection)                                                         |                   | 1                                          |
| Remote device over a DeviceNet network (Accounted for in rack-optimized connection for local 1756-DNB module)             |                   | 0                                          |
| Produced tag and first consumer Each additional consumer                                                                  |                   | 2 1                                        |
| Consumed tag                                                                                                              |                   | 1                                          |
| Cached message                                                                                                            |                   | 1                                          |
| Message                                                                                                                   |                   | 1                                          |
| FactoryTalk® Linx subscriber (16 maximum)                                                                                 |                   | 1                                          |
| Total                                                                                                                     | Total             | Total                                      |

## CompactLogix Controller Accessories

These accessories are compatible with the indicated CompactLogix controllers.

## Memory Cards

Memory cards offer nonvolatile memory to store a user program and tag data on a controller. You can use the programming software to prompt the controller to save to or load from nonvolatile memory or you can configure the controller to load from nonvolatile memory on power-up.

| IMPORTANT   | The 1769-L23x packaged CompactLogix controllers do not offer a nonvolatile memory option.   |
|-------------|---------------------------------------------------------------------------------------------|

The CompactLogix 5370 controllers come with a 1784-SD1 Secure Digital (SD) card installed. Order a 1784-SD2 SD card separately for additional nonvolatile memory with the CompactLogix 5370 controllers.

You can use a 1784-CF128 CompactFlash card with the 1768 L4 and L3 modular CompactLogix controllers for a nonvolatile memory option. Insert the CompactFlash card into the memory card slot on the controller.

## Certifications - 1784 Memory Cards

| Certification(1)   | 1784-CF128, 1784-SD1, 1784-SD2                                                                                                                                                                                                                                                                                                                    |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CE                 | European Union 2014/30/EU EMC Directive, compliant with: • EN 61000-6-4; Industrial Emissions • EN 61326-1; Meas./Control/Lab., Industrial Requirements • EN 61000-6-2; Industrial Immunity • EN 61131-2; Programmable Controllers (Clause 8, Zone A & B) European Union 2011/65/EU RoHS, compliant with: • EN IEC 63000; Technical documentation |
| RCM                | Australian Radiocommunications Act, compliant with: AS/NZS CISPR 11; Industrial Emissions                                                                                                                                                                                                                                                         |
| KC                 | Korean Registration of Broadcasting and Communications Equipment, compliant with: Article 58-2 of Radio Waves Act, Clause 3                                                                                                                                                                                                                       |

## Environmental Specifications - 1784 Memory Cards

|                                                                                                                                                                                                        | Attribute 1784-CF128, 1784-SD1, 1784-SD2   |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------|
| Temperature, operating IEC 60068-2-1 (Test Ad, Operating Cold), IEC 60068-2-2 (Test Bd, Operating Dry Heat), IEC 60068-2-14 (Test Nb, Operating Thermal Shock)                                         | -25…+70 °C (-13…+158 °F)                   |
| Temperature, storage IEC 60068-2-1 (Test Ab, Unpackaged Nonoperating Cold), IEC 60068-2-2 (Test Bb, Unpackaged Nonoperating Dry Heat), IEC 60068-2-14 (Test Na, Unpackaged Nonoperating Thermal Shock) | -40…+85 °C (-40…+185 °F)                   |
| Relative humidity IEC 60068-2-30 (Test Db, Unpackaged Damp Heat)                                                                                                                                       | 5…95% noncondensing                        |
| Vibration IEC 60068-2-6 (Test Fc, Operating)                                                                                                                                                           | 2 g @ 10…500 Hz                            |
| Shock, operating IEC 60068-2-27 (Test Ea, Unpackaged Shock)                                                                                                                                            | 30 g                                       |
| Shock, nonoperating IEC 60068-2-27 (Test Ea, Unpackaged Shock)                                                                                                                                         | 50 g                                       |

## Environmental Specifications - 1784 Memory Cards

|                                    | Attribute 1784-CF128, 1784-SD1, 1784-SD2                                                                                                                                                            |
|------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Emissions CISPR 11                 | Group 1, Class A                                                                                                                                                                                    |
| ESD immunity IEC 61000-4-2         | 6 kV contact discharges 8 kV air discharges                                                                                                                                                         |
| Radiated RF immunity IEC 61000-4-3 | 10V/m with 1 kHz sine wave 80% AM from 80…2000 MHz 10V/m with 200 Hz 50% Pulse 100% AM @ 900 MHz 10V/m with 200 Hz 50% Pulse 100% AM @ 1890 MHz 3V/m with 1 kHz sine wave 80% AM from 2000…2700 MHz |

## Technical Specifications - 1784-CF128, 1784-SD1, 1784-SD2

| Attribute             | 1784-CF128                                | 1784-SD1                          | 1784-SD2                          |
|-----------------------|-------------------------------------------|-----------------------------------|-----------------------------------|
| Memory                | 128 MB                                    | 1 GB                              | 2 GB                              |
| Supported controllers | 1769 modular controllers 1768 controllers | CompactLogix 5370 controllers     | CompactLogix 5370 controllers     |
| Weight, approx        |                                           | 14.2 g (0.5 oz) 1.76 g (0.062 oz) | 14.2 g (0.5 oz) 1.76 g (0.062 oz) |

## 1769 CompactLogix Batteries

The 1769 L23 and L3x controllers come with one 1769-BA lithium battery.

The 1768 controllers and the CompactLogix 5370 controllers do not require a battery. The controller uses internal nonvolatile memory to store its program during shutdown. Energy that is stored in the system maintains controller power long enough to store the program to internal nonvolatile memory, but not the external CompactFlash card nor SD card respectively.

## Technical Specifications - 1769-BA

| Attribute                | 1769-BA                                                                                               |
|--------------------------|-------------------------------------------------------------------------------------------------------|
| Description              | Lithium battery (0.59 g)                                                                              |
| CompactLogix controllers | 1769-L23-QBFC1B, 1769-L23E-QB1B, 1769-L23E-QBFC1B 1769-L31 1769-L32C, 1769-L35CR 1769-L32E, 1769-L35E |

## Removable Terminal Kits

You can order removable terminal kits separately for the CompactLogix 5370 L1 and L2 controllers.

| Cat. No. Controllers Supported Description           |                                                                                                                                                                                                           |
|------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1769-RTB45 CompactLogix 5370 L1                      | • Four 10-pin connectors are used to connect the wiring to the embedded digital I/O module of the controller. • One 5-pin connector is used to connect an external 24V DC power source to the controller. |
| 1769-RTB40DIO CompactLogix 5370 L2                   | Four 10-pin connectors are used to connect the wiring to the embedded digital I/O module of the controller.                                                                                               |
| 1769-RTB40AIO  1769-L24ER-QBFC1B, 1769-L27ERM-QBFC1B | Four 10-pin connectors are used to connect the wiring to the embedded analog I/O module of the controller.                                                                                                |

## Cold Junction Compensation

The CompactLogix 5370 L2 controllers require the use of the 1769CJC CompactLogix CJC Sensor when the embedded analog input of the controller is configured for Thermocouple mode.

## Ethernet Communication Cables

<!-- image -->

| Connector Number   | Color 1585J-M8xBJM-2 1585J-M4TBJM-2   |                           |
|--------------------|---------------------------------------|---------------------------|
|                    | 1 White/Orange TxData +               | 1 White/Orange TxData +   |
|                    | 2 Orange TxData -                     | 2 Orange TxData -         |
|                    | 3 White/Green Recv Data +             | 3 White/Green Recv Data + |
|                    | 4 Blue Unused –                       |                           |
|                    | 5 White/Blue Unused –                 |                           |
|                    | 6 Green Recv Data -                   | 6 Green Recv Data -       |
|                    | 7 White/Brown Unused –                |                           |
|                    | 8 Brown Unused –                      |                           |

| Attribute       | Value                    |
|-----------------|--------------------------|
| Connector type  | RJ45 Male to RJ45 Male   |
| Connector angle | Straight-through         |
| Length          | Varies by catalog number |

## Serial Communication Cables

<!-- image -->

| Attribute       | 1756-CP3                                                     | 1747-CP3   |
|-----------------|--------------------------------------------------------------|------------|
| Connector type  | Female 9-pin D-shell                                         |            |
| Connector angle | Right angle connector to controller, straight to serial port |            |
| Length          | 3 m (118 in.)                                                |            |

## Additional Resources

These documents contain additional information concerning related products from Rockwell Automation. You can view or download publications at rok.auto/literature .

|                                                                                                                    | Resource Description                                                                                                                                                                                                                                                            |
|--------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Replacement Guidelines: Logix 5000™ Controllers Reference Manual, publication 1756-RM100                           | Provides guidelines on how to replace the following: • ControlLogix® 5560/5570 controller with a ControlLogix 5580 controller • CompactLogix 5370 L3 controllers with a CompactLogix 5380 controller                                                                            |
| CompactLogix 5370 Controllers System User Manual, publication 1769-UM021                                           | Provides information on how to configure, operate, and monitor Armor CompactLogix and CompactLogix 5370 controllers.                                                                                                                                                            |
| Compact GuardLogix 5370 Controllers User Manual, publication 1769-UM022                                            | Provides information on how to configure, operate, and monitor Armor Compact GuardLogix and Compact GuardLogix 5370 controllers                                                                                                                                                 |
| EtherNet/IP Network Devices User Manual, ENET-UM006                                                                | Describes how to configure and use EtherNet/IP devices to communicate on the EtherNet/IP network.                                                                                                                                                                               |
| Ethernet Reference Manual, ENET-RM002                                                                              | Describes basic Ethernet concepts, infrastructure components, and infrastructure features.                                                                                                                                                                                      |
| System Security Design Guidelines Reference Manual, SECURE-RM001                                                   | Provides guidance on how to conduct security assessments, implement Rockwell Automation products in a secure system, harden the control system, manage user access, and dispose of equipment.                                                                                   |
| UL Standards Listing for Industrial Control Products, publication CMPNTS-SR002                                     | Assists original equipment manufacturers (OEMs) with construction of panels, to help ensure that they conform to the requirements of Underwriters Laboratories.                                                                                                                 |
| American Standards, Configurations, and Ratings: Introduction to Motor Circuit Design, publication IC-AT001        | Provides an overview of American motor circuit design based on methods that are outlined in the NEC.                                                                                                                                                                            |
| Industrial Components Preventive Maintenance, Enclosures, and Contact Ratings Specifications, publication IC-TD002 | Provides a quick reference tool for Allen-Bradley industrial automation controls and assemblies.                                                                                                                                                                                |
| Safety Guidelines for the Application, Installation, and Maintenance of Solid-state Control, publication SGI-1.1   | Designed to harmonize with NEMA Standards Publication No. ICS 1.1-1987 and provides general guidelines for the application, installation, and maintenance of solid-state control in the form of individual devices or packaged assemblies incorporating solid-state components. |
| Industrial Automation Wiring and Grounding Guidelines, publication 1770-4.1                                        | Provides general guidelines for installing a Rockwell Automation industrial system.                                                                                                                                                                                             |
| Integrated Architecture Builder (IAB) Advanced EtherNet/IP capacity tool                                           | Provides EtherNet/IP network performance and Logix controller utilization estimates based on a particular system layout.                                                                                                                                                        |
|                                                                                                                    | Product Certifications website, rok.auto/certifications. Provides declarations of conformity, certificates, and other certification details.                                                                                                                                    |

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

Allen-Bradley, Armor, ArmorBlock, ArmorBlock MaXum, ArmorPOINT, Compact I/O, CompactBlock Guard I/O, CompactBlock I/O, CompactBlock LDX I/O, CompactLogix, ControlLogix, DriveLogix, expanding human possibility, FactoryTalk, FactoryTalk Linx, FLEX Ex, FLEX I/O, FlexLogix, Guard I/O, GuardLogix, Integrated Architecture Builder, InView, MicroLogix, On-Machine, PanelView terminal, PanelView e, PanelView Plus, PLC-2, PLC-3, PLC-5, POINT Guard I/O, POINT I/O, POINTBus, PowerFlex, Rockwell Automation, RSLinx Classic, SCANport, SLC, and SoftLogix, are trademarks of Rockwell Automation, Inc.

CIP, CIP Safety, ControlNet, DeviceNet, and EtherNet/IP are trademarks of ODVA, Inc.

Trademarks not belonging to Rockwell Automation are property of their respective companies.

Rockwell Automation maintains current product environmental compliance information on its website at rok.auto/pec .

Rockwell Otomasyon Ticaret A.Ş. Kar Plaza İş Merkezi E Blok Kat:6 34752, İçerenköy, İstanbul, Tel: +90 (216) 5698400 EEE Yönetmeliğine Uygundur

Connectwithus.

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

rockwellautomation.com expandinghumanpossibility

AMERlCAS:RockwellAutomation,1201SouthSec0ndStreet,Milwaukee,WI53204-2496USA,Tel:(1)414.382.2000,Fax:(1)414.382.4444 EUR0PE/MIDDLEEAST/AFRICA:RockwellAutomationNV,PegasusPark,DeKleetlaan12a,1831Diegem,Belgium,Tel:(32)26630600,Fax:(32)26630640 ASIAPACIFIC:RockwellAutomationSEAPteLtd,2CorporationRoad,#04-05,MainLobby,CorporationPlace,Singapore618494,Tel:(65)65106608,FAX:(65)65106699 UNITEDKINGD0M:RockwellAutomationLtd.,Pitfield,KilnFarm,MiltonKeynes,MK113DR,UnitedKingdom,Tel:(44)(1908)838-800,Fax:(44)(1908)261-917