## PanelView Plus Terminals

Catalog Number 2711P (400, 600, 700, 1000, 1250, 1500 Terminals)

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

## Important User Information

Read this document and the documents listed in the additional resources section about installation, configuration, and operation of this equipment before you install, configure, operate, or maintain this product. Users are required to familiarize themselves with installation and wiring instructions in addition to requirements of all applicable codes, laws, and standards.

Activities including installation, adjustments, putting into service, use, assembly, disassembly, and maintenance are required to be carried out by suitably trained personnel in accordance with applicable code of practice.

If this equipment is used in a manner not specified by the manufacturer, the protection provided by the equipment may be impaired.

In no event will Rockwell Automation, Inc. be responsible or liable for indirect or consequential damages resulting from the use or application of this equipment.

The examples and diagrams in this manual are included solely for illustrative purposes. Because of the many variables and requirements associated with any particular installation, Rockwell Automation, Inc. cannot assume responsibility or liability for actual use based on the examples and diagrams.

No patent liability is assumed by Rockwell Automation, Inc. with respect to use of information, circuits, equipment, or software described in this manual.

Reproduction of the contents of this manual, in whole or in part, without written permission of Rockwell Automation, Inc., is prohibited.

Throughout this manual, when necessary, we use notes to make you aware of safety considerations.

<!-- image -->

WARNING: Identifies information about practices or circumstances that can cause an explosion in a hazardous environment, which may lead to personal injury or death, property damage, or economic loss.

<!-- image -->

IMPORTANT

ATTENTION: Identifies information about practices or circumstances that can lead to personal injury or death, property damage, or economic loss. Attentions help you identify a hazard, avoid a hazard, and recognize the consequence.

Identifies information that is critical for successful application and understanding of the product.

Labels may also be on or inside the equipment to provide specific precautions.

<!-- image -->

SHOCK HAZARD: Labels may be on or inside the equipment, for example, a drive or motor, to alert people that dangerous voltage may be present.

<!-- image -->

<!-- image -->

BURN HAZARD: Labels may be on or inside the equipment, for example, a drive or motor, to alert people that surfaces may reach dangerous temperatures.

ARC FLASH HAZARD: Labels may be on or inside the equipment, for example, a motor control center, to alert people to potential Arc Flash. Arc Flash will cause severe injury or death. Wear proper Personal Protective Equipment (PPE). Follow ALL Regulatory requirements for safe work practices and for Personal Protective Equipment (PPE).

Preface

|                    | Summary of Changes . . . . . . . . .  . . . . . . . . . . . . . . . . . .                                       | . . . . . . . . . . . . . . . . 7      |
|--------------------|-----------------------------------------------------------------------------------------------------------------|----------------------------------------|
|                    | Intended Audience . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7   |                                        |
|                    | Parts List . . . . . . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                   | . . . . . . . . . . . . . 7            |
|                    | Additional Resources . . . . . . . .  . . . . . . . . . . . . . . . . . . .                                     | . . . . . . . . . . . . . . . . 8      |
|                    | Software and Firmware Upgrades.  . . . . . . . . . . . . . . . . .                                              | . . . . . . . . . . . . . . 8          |
|                    | Chapter 1                                                                                                       |                                        |
| Overview           | Chapter Objectives. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9   |                                        |
|                    | Software Support. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9 |                                        |
|                    | PanelView Plus 400 and 600 Terminals . . . . . . . . . . . . . . . . . . . . . . . . . 10                       |                                        |
|                    | PanelView Plus 700 to 1500 Terminals . . . . . . . . . . . . . . . . . . . . . . . . . 15                       |                                        |
|                    | Catalog Number Configuration . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21                 |                                        |
|                    | PanelView Plus Product Components . . . . . . . . . . . . . . . . . . . . . . . . . . 21                        |                                        |
|                    | Chapter 2                                                                                                       |                                        |
| Installation       | Chapter Objectives. . . . . . . . .  . . . . . . . . . . . . . . . . . .                                        | . . . . . . . . . . . . . . . . . 29   |
|                    | Hazardous Locations . . . . . . . . .  . . . . . . . . . . . . . . . . .                                        | . . . . . . . . . . . . . . . . 29     |
|                    | Environment and Enclosure. . . .  . . . . . . . . . . . . . . . . .                                             | . . . . . . . . . . . . . . . 32       |
|                    | Outdoor Installation for High-bright Displays. . . . . . . . . . . . . . . . . . . 32                           |                                        |
|                    | Required Tools . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . .                                     | . . . . . . . . . . . . . . . . . 34   |
|                    | Clearances . . . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . .                                 | . . . . . . . . . . . . . . . . . . 34 |
|                    | Cutout Dimensions . . . . .  . . . . . . . . . . . . . . . . . . . .                                            | . . . . . . . . . . . . . . . . . . 34 |
|                    | Mount the 400 or 600 Terminal in a Panel . . . . . . . . . . . . . . . . . . . . . . 35                         |                                        |
|                    | Mount the 700 to 1500 Terminal in a Panel . . . . . . . . . . . . . . . . . . . . . 37                          |                                        |
|                    | Product Dimensions. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 39      |                                        |
|                    | Chapter 3                                                                                                       |                                        |
| Power Connections  | Chapter Objectives. . . . . . . . .  . . . . . . . . . . . . . . . . . .                                        | . . . . . . . . . . . . . . . . . 45   |
|                    | Wiring and Safety Guidelines .  . . . . . . . . . . . . . . . . .                                               | . . . . . . . . . . . . . . . . 45     |
|                    | Remove and Install the Power Terminal Block. . . . . . . . . . . . . . . . . . . 46                             |                                        |
|                    | DC Power Connections . . . . . .  . . . . . . . . . . . . . . . . .                                             | . . . . . . . . . . . . . . . . 49     |
|                    | AC Power Connections . . . . . . .  . . . . . . . . . . . . . . . . .                                           | . . . . . . . . . . . . . . . 54       |
|                    | Reset the Terminals . . . . . . . .  . . . . . . . . . . . . . . . . . .                                        | . . . . . . . . . . . . . . . . . 56   |
|                    | Chapter 4                                                                                                       |                                        |
| Configuration Mode | Chapter Objectives. . . . . . . . .  . . . . . . . . . . . . . . . . . .                                        | . . . . . . . . . . . . . . . . . 59   |
|                    | Access Configuration Mode.  . . . . . . . . . . . . . . . . . .                                                 | . . . . . . . . . . . . . . . . . 59   |
|                    | Load an Application. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 63     |                                        |
|                    | Run an Application . . . . .  . . . . . . . . . . . . . . . . . . . .                                           | . . . . . . . . . . . . . . . . . . 64 |
|                    | Application Settings . . . . .  . . . . . . . . . . . . . . . . . . . .                                         | . . . . . . . . . . . . . . . . . . 64 |
|                    | Terminal Settings . . . . . . . . .  . . . . . . . . . . . . . . . . . . .                                      | . . . . . . . . . . . . . . . . . 64   |
|                    | Configure Communication . . . . .  . . . . . . . . . . . . . . . .                                              | . . . . . . . . . . . . . . . 65       |
|                    | Configure Network Information .  . . . . . . . . . . . . . . . .                                                | . . . . . . . . . . . . . . 70         |

|                           | Configure Diagnostics . . . . . . .  . . . . . . . . . . . . . . . . . .                         | . . . . . . . . . . . . . . . . 74                  |
|---------------------------|--------------------------------------------------------------------------------------------------|-----------------------------------------------------|
|                           | Manage Files on the Terminal . . . . . . . . . .                                                 | . . . . . . . . . . . . .  . . . . . . . . . . . 76 |
|                           | Modify Display Settings .  . . . . . . . . . . . . . . . . . . . .                               | . . . . . . . . . . . . . . . . . . 79              |
|                           | Font Linking . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . .                      | . . . . . . . . . . . . . . . . . . 83              |
|                           | Configure Keypad, Keyboard, or Mouse. . . . . . . . . . . . . . . . . . . . . . . . . 84         |                                                     |
|                           | Configure the Touch Screen   . . . . . . . . . . . . . . . . . .                                 | . . . . . . . . . . . . . . . . . 86                |
|                           | Configure Print Options. . . . . .  . . . . . . . . . . . . . . . . .                            | . . . . . . . . . . . . . . . . 89                  |
|                           | Configure Startup Options  . . . . . . . . . . . . . . . . . . .                                 | . . . . . . . . . . . . . . . . . 91                |
|                           | Configure Startup Tests . . . . . .  . . . . . . . . . . . . . . . . .                           | . . . . . . . . . . . . . . . . 97                  |
|                           | View and Clear the System Event Log. . . . . . . . . . . . . . . . . . . . . . . . . . . 99      |                                                     |
|                           | Display Terminal Information . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 100 |                                                     |
|                           | Display FactoryTalk View ME Station Information . . . . . . . . . . . . . 102                    |                                                     |
|                           | Modify the Date, Time, or Time Zone . . . . . . . . . . . . . . . . . . . . . . . . . 103        |                                                     |
|                           | Modify Regional Settings . . . .  . . . . . . . . . . . . . . . . .                              | . . . . . . . . . . . . . . . . 106                 |
|                           | Chapter 5                                                                                        |                                                     |
| Windows CE .NET Operating | Chapter Objectives. . . . . . . . .  . . . . . . . . . . . . . . . . . .                         | . . . . . . . . . . . . . . . . 111                 |
| System                    | Windows CE .NET Architecture.  . . . . . . . . . . . . . . .                                     | . . . . . . . . . . . . . . 111                     |
|                           | Windows CE .NET Programs . .  . . . . . . . . . . . . . . . .                                    | . . . . . . . . . . . . . . 112                     |
|                           | Windows CE .NET Operating System . . . . . . . . . . . . . . . . . . . . . . . . . 113           |                                                     |
|                           | PanelView Plus CE Memory . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 117 |                                                     |
|                           | Control Panel Applications . . .  . . . . . . . . . . . . . . . . .                              | . . . . . . . . . . . . . . . 119                   |
|                           | Chapter 6                                                                                        |                                                     |
| Install and Replace       | Chapter Objectives. . . . . . . . .  . . . . . . . . . . . . . . . . . .                         | . . . . . . . . . . . . . . . . 139                 |
| Components                | Required Tools . . . . . . . . . . .  . . . . . . . . . . . . . . . . . .                        | . . . . . . . . . . . . . . . . . 139               |
|                           | Precautions . . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . .                   | . . . . . . . . . . . . . . . . . 139               |
|                           | Component Compatibility for PanelView Plus CE Terminals . . . 140                                |                                                     |
|                           | Component Compatibility for PanelView Plus Terminals . . . . . . . 140                           |                                                     |
|                           | Install RAM or Internal CompactFlash . . . . . . . . . . . . . . . . . . . . . . . . 141         |                                                     |
|                           | Install or Replace the Logic Module. . . . . . . . . . . . . . . . . . . . . . . . . . . . 142   |                                                     |
|                           | Install or Replace a Communication Module . . . . . . . . . . . . . . . . . . . 145              |                                                     |
|                           | Replace the Display Module. . . .  . . . . . . . . . . . . . . . .                               | . . . . . . . . . . . . . . . 149                   |
|                           | Replace the Battery . . . . . . . .  . . . . . . . . . . . . . . . . . .                         | . . . . . . . . . . . . . . . . . 151               |
|                           | Replace the Bezel. . . . . . . . . .  . . . . . . . . . . . . . . . . . .                        | . . . . . . . . . . . . . . . . . 153               |
|                           | Replace the Backlight . . . . . . .  . . . . . . . . . . . . . . . . . .                         | . . . . . . . . . . . . . . . . 156                 |
|                           | Remove the Product ID Label . .  . . . . . . . . . . . . . . . .                                 | . . . . . . . . . . . . . . . 160                   |
|                           | Replace the Keypad Legend Inserts . . . . . . . . . . . . . . . . . . . . . . . . . . . . 160    |                                                     |
|                           | Use an External CompactFlash Card. . . . . . . . . . . . . . . . . . . . . . . . . . . 162       |                                                     |
|                           | Chapter 7                                                                                        |                                                     |
| Terminal Connections      | Chapter Objectives. . . . . . . . .  . . . . . . . . . . . . . . . . . .                         | . . . . . . . . . . . . . . . . 163                 |
|                           | Wiring and Safety Guidelines .  . . . . . . . . . . . . . . . . .                                | . . . . . . . . . . . . . . . 163                   |
|                           | Logic Controller Cable Charts .  . . . . . . . . . . . . . . . .                                 | . . . . . . . . . . . . . . . 164                   |
|                           | Communication Port Isolation .  . . . . . . . . . . . . . . . .                                  | . . . . . . . . . . . . . . . 167                   |
|                           | USB Ports . . . . . . . . . .  . . . . . . . . . . . . . . . . . . . . .                         | . . . . . . . . . . . . . . . . . . . . 168         |

|                         | Serial Connections . . . . . . . . .  . . . . . . . . . . . . . . . . . .                                               | . . . . . . . . . . . . . . . . 169       |
|-------------------------|-------------------------------------------------------------------------------------------------------------------------|-------------------------------------------|
|                         | Ethernet Connections . . .  . . . . . . . . . . . . . . . . . . .                                                       | . . . . . . . . . . . . . . . . . . 172   |
|                         | DH-485/DH+/Remote I/O Module . . . . . . . . . . . . . .                                                                | . . . . . . . . . . . . 174               |
|                         | ControlNet Module. . . . . . . . .  . . . . . . . . . . . . . . . . .                                                   | . . . . . . . . . . . . . . . . 180       |
|                         | DeviceNet Module . . . . . . . . . .  . . . . . . . . . . . . . . . . .                                                 | . . . . . . . . . . . . . . . . 183       |
|                         | Chapter 8                                                                                                               |                                           |
| Upgrade Firmware        | Chapter Objectives. . . . . . . . .  . . . . . . . . . . . . . . . . . .                                                | . . . . . . . . . . . . . . . . 189       |
|                         | Transfer Applications . .  . . . . . . . . . . . . . . . . . . . .                                                      | . . . . . . . . . . . . . . . . . . 189   |
|                         | Create an ActiveSync Connection . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 189                           |                                           |
|                         | Firmware Upgrade Wizard.  . . . . . . . . . . . . . . . . . .                                                           | . . . . . . . . . . . . . . . . . 191     |
|                         | Upgrade Firmware with a CompactFlash Card . . . . . . . . . . . . . . . . . 192                                         |                                           |
|                         | Upgrade Firmware with a Network (Ethernet) Connection. . . . . . 195                                                    |                                           |
|                         | Upgrade the Operating System (OS). . . . . . . . . . . . . . . . . . . . . . . . . . . 202                              |                                           |
|                         | Chapter 9                                                                                                               |                                           |
| Troubleshoot the System | Chapter Objectives. . . . . . . . .  . . . . . . . . . . . . . . . . . .                                                | . . . . . . . . . . . . . . . . 205       |
|                         | Status Indicators . . . . . . . . .  . . . . . . . . . . . . . . . . . . .                                              | . . . . . . . . . . . . . . . . . 205     |
|                         | Isolate the Problem . . . . . . . . .  . . . . . . . . . . . . . . . . . .                                              | . . . . . . . . . . . . . . . . 206       |
|                         | Startup Information Messages . .  . . . . . . . . . . . . . . . .                                                       | . . . . . . . . . . . . . . . 209         |
|                         | Startup Sequence. . . . . . . . . .  . . . . . . . . . . . . . . . . . .                                                | . . . . . . . . . . . . . . . . . 210     |
|                         | Startup Error Messages . .  . . . . . . . . . . . . . . . . . . .                                                       | . . . . . . . . . . . . . . . . . . 211   |
|                         | Check Terminal Components. . .  . . . . . . . . . . . . . . . .                                                         | . . . . . . . . . . . . . . 212           |
|                         | Ethernet Connnection  . . . . . . . . . . . . . . . . . . . .                                                           | . . . . . . . . . . . . . . . . . . . 215 |
|                         | Application Does Not Run  . . . . . . . . . . . . . . . . . .                                                           | . . . . . . . . . . . . . . . . . 216     |
|                         | Configuration Mode Access. . . .  . . . . . . . . . . . . . . . .                                                       | . . . . . . . . . . . . . . . 216         |
|                         | File System Errors . . . . . . . . .  . . . . . . . . . . . . . . . . . .                                               | . . . . . . . . . . . . . . . . . 216     |
|                         | Advanced Diagnostics for CE Terminals . . . . . . . . . . . . . . . . . . . . . . . 217                                 |                                           |
|                         | System Identification Errors . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 218                    |                                           |
|                         | Restart in Safe Mode . . . . . .  . . . . . . . . . . . . . . . . . .                                                   | . . . . . . . . . . . . . . . . . 219     |
|                         | Chapter 10                                                                                                              |                                           |
| Maintenance             | Chapter Objectives. . . . . . . . .  . . . . . . . . . . . . . . . . . .                                                | . . . . . . . . . . . . . . . . 221       |
|                         | Clean the Display Window  . . . . . . . . . . . . . . . . . .                                                           | . . . . . . . . . . . . . . . . . 221     |
|                         | Disposal Information. . .  . . . . . . . . . . . . . . . . . . . .                                                      | . . . . . . . . . . . . . . . . . . 221   |
|                         | Appendix A                                                                                                              |                                           |
| Specifications          | Electrical . . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . . .                                         | . . . . . . . . . . . . . . . . . . 223   |
|                         | Environmental . . . . . . .  . . . . . . . . . . . . . . . . . . . . .                                                  | . . . . . . . . . . . . . . . . . . . 223 |
|                         | Display . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 224 |                                           |
|                         | Mechanical . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . .                                             | . . . . . . . . . . . . . . . . . . 225   |
|                         | General. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 226  |                                           |
|                         | Agency Certifications. . . . . . . .  . . . . . . . . . . . . . . . . .                                                 | . . . . . . . . . . . . . . . . 226       |

Appendix B

| Compatible USB Devices       | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . . . 227   |                                             |
|------------------------------|----------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------|
|                              | Appendix C                                                                                                                       |                                             |
| Available Fonts for Terminal | Download Fonts to Terminal . .  . . . . . . . . . . . . . . . .                                                                  | . . . . . . . . . . . . . . . 229           |
| Applications                 | PanelView Plus CE Accessories CD. . . . . . . . . . . . . . . . . . . . . . . . . . . 229                                        |                                             |
|                              | Machine Edition Fonts CD . . . .  . . . . . . . . . . . . . . . .                                                                | . . . . . . . . . . . . . . . 230           |
|                              | Appendix D                                                                                                                       |                                             |
| Programmable Key Definitions | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . . . 233   |                                             |
|                              | Appendix E                                                                                                                       |                                             |
| Security Considerations      | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . . . 235   |                                             |
|                              | Index                                                                                                                            |                                             |
|                              | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                | . . . . . . . . . . . . . . . . . . . . 237 |

## Summary of Changes

## Intended Audience

## Parts List

This preface provides information on these topics.

-  Intended audience
-  Parts list
-  Additional resources
-  Software and firmware upgrades

This manual contains new and updated information as indicated in the following table.

| Topic                                    | Pages              |
|------------------------------------------|--------------------|
| Updated the power supply catalog number. | 18, 26, 50, and 51 |

Use this manual if you are responsible for installing, operating, or troubleshooting the PanelView Plus or PanelView Plus CE terminals.

No special knowledge is required to understand this manual or operate the terminal. However, you must understand the functions and operations of FactoryTalk View Machine Edition (ME) applications that will run on the terminal. Consult the application designer for this information.

Equipment installers must be familiar with standard panel installation techniques.

The PanelView Plus terminals are shipped with these items.

-  Power terminal block
-  FactoryTalk View ME runtime software, preloaded
-  Mounting levers for 400 and 600 terminals, quantity eight
-  Mounting clips for 700 to 1500 terminals, quantity four to eight
-  Installation instructions
-  Panel cutout template

Additional items are shipped with the PanelView Plus CE terminals.

-  Windows CE .NET operating system preloaded with Terminal Services and Internet Explorer
-  PanelView Plus CE Accessory CD with utilities and software development kit for C++
-  Microsoft Windows CE license agreement

## Additional Resources

## Software and Firmware Upgrades

For additional information, refer to these publications, that you can download from http://literature.rockwellautomation.com .

| Resource                                                                                           | Description                                                                                      |
|----------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|
| DeviceNet Communications for PanelView Plus Terminals User Manual, publication 2711P-UM004         | Provides procedures for creating a DeviceNet application to run on a PanelView Plus terminal.    |
| ControlNet Communications for PanelView Plus Terminals User Manual, publication 2711P-UM003        | Provides procedures for creating a ControlNet application to run on a PanelView Plus terminal.   |
| Modbus Applications for PanelView Plus Terminals User Manual, publication 2711P-UM002              | Provides procedures for creating a Modbus application to run on a PanelView Plus terminal.       |
| Wiring and Grounding Guidelines for PanelView Plus Devices Technical Data, publication 2711P-TD001 | Provides grounding and wiring guidelines for PanelView Plus terminals.                           |
| Software Development Kit for PanelView Plus CE Terminals User Manual, publication 2711P-UM005      | Provides information for programmers to develop CE applications for PanelView Plus CE terminals. |

You may also want to refer to:

-  online help for FactoryTalk View Studio or RSLinx software.
-  documentation for your controller.

To receive software updates (software serial number required) and firmware upgrades for your terminal:

-  call your local Rockwell Automation sales office or distributor.
-  access the Product Compatibility and Download Center at http://www.rockwellautomation.com/rockwellautomation/support/pcdc .page.

## Chapter Objectives

## Software Support

## Overview

This chapter gives an overview of the PanelView Plus terminals.

-  Software support
-  PanelView Plus 400 and 600 features
-  PanelView Plus 700 to 1500 features
-  Catalog number configuration
-  Product components

Each PanelView Plus and PanelView Plus CE terminal is preloaded with FactoryTalk View Machine Edition runtime and terminal configuration software that does not require activation. Machine Edition applications for the terminals are created using FactoryTalk View Studio software.

Users, other than equipment operators, can view a running Machine Edition application in read-only mode within a Web browser using ViewPoint software. This software is an add-on capability provided with FactoryTalk View Studio.

## IMPORTANT

ViewPoint software requires terminals with a Series E or later logic module and a minimum of 128 MB RAM. You can also order an internal CompactFlash card with FactoryTalk View software, catalog number 2711P-RWx , to support any series logic module, catalog number 2711P-RPxx .

The open Windows CE.NET environment of the PanelView Plus CE terminals provides:

-  familiar Windows desktop and user interface.
-  terminal server-client support to configured servers
-  Internet Explorer web browser.
-  software development kit to support custom C++ applications for Windows CE.NET operating system.
-  third-party device support for Windows CE.NET operating system.
-  Windows CE.NET operating system provides these programs:
- – File viewers for MS Office: Excel, Word, PowerPoint
- – PDF file viewer
- – WordPad text editor
- – WebServer application
- – FTP server
- – Support for the .NET compact framework

## PanelView Plus 400 and 600 Terminals

Some of the above software applications are included on the PanelView Plus CE Accessory CD.

The PanelView Plus 400 and 600 terminals offer:

-  base-configured units.
-  communication modules.
-  power supply, AC or DC.
-  grayscale and color displays.

<!-- image -->

<!-- image -->

<!-- image -->

The PanelView Plus 400 and 600 terminals are HMI devices that provide these features:

-  PanelView Plus 400 terminals
- – Color or grayscale graphic displays
- – Keypad or keypad and touch screen input support
-  PanelView Plus 600 terminals
- – Color or grayscale graphic displays
- – Keypad, touch screen, or keypad and touch screen input
-  Base-configured unit
- – RS-232 only
- – RS-232, Ethernet, and modular communications interface
-  Communication modules provide add-on capability to base-configured units with a modular communications interface
-  Power input, AC (85…264V) or DC (18…30V)
-  CompactFlash card slot supports Type 1 CompactFlash cards
-  USB port for attaching mouse, keyboard, printer, bar code scanner, and other devices
-  Same panel cutouts as the PanelView Standard 550 terminals

## Base-configured Units

The base-configured unit of the 400 and 600 terminals is available in two versions.

-  Base unit with RS-232 port and one USB port
-  Base unit with RS-232 port, 10/100BaseT Ethernet port, one USB port, and a network interface for a communication module

## Base Unit with RS-232 Only

<!-- image -->

## Base Unit with RS-232, Ethernet Port, and Modular Communications Interface

<!-- image -->

## Communication Modules

You can attach a communication module with a network interface to the base-configured unit of the PanelView Plus 400 and 600 terminals to increase your communication capability with these networks:

-  DH-485
-  DH+
-  Isolated RS-232
-  ControlNet

The communication module installs easily on the back of the unit.

<!-- image -->

## Power Options

The base-configured unit of the PanelView Plus 400 and 600 terminals is available with either AC (85…264V) or DC (18…30V) power input providing application flexibility.

## Display and Input Options

PanelView Plus 400 and 600 terminals are available with these display and operator input options:

-  400 terminals: 3.8 in. grayscale (320 x 240) graphics display with keypad or 3.5 in. (320 x 240) color with keypad or keypad and touch support
-  600 terminals: 5.5 in. color or grayscale (320 x 240) graphics display with keypad, touch screen, or keypad and touch support

## Touch Screen

The PanelView Plus 600 terminals offer an analog resistive touch screen for touch input.

600 Touch Grayscale or Color Terminal

<!-- image -->

IMPORTANT

The touch screen may be operated with a finger, gloved finger, or plastic stylus device with a minimum tip radius of 1.3 mm (0.051 in.) to prevent damage to the touch screen. Using any other object or tool may damage the touch screen.

## Keypad or Keypad and Touch

The keypad versions of the PanelView Plus 400 and 600 terminals are available with these options:

-  400 terminals: grayscale display with keypad or color display with keypad or keypad and touch input
-  400 and 600 terminals offer an analog resistive touch screen for touch input.
-  600 terminals: color or grayscale displays with either keypad, or keypad and touch input

## 400 Grayscale with Keypad, or 400 Color with Keypad or Keypad and Touch

<!-- image -->

8 Programmable Function Keys

<!-- image -->

10 Relegendable Programmable Function Keys

| Keys                                 | Description                                                                                                                                                     |
|--------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 400 F1 through F8 600 F1 through F10 | Programmable keys that initiate functions on terminal display. Replaceable legends are available for the 600 terminals allowing for custom function key labels. |
| Numeric Keypad                       | 0…9, ., -, Backspace, Enter, Left and Right Tab keys, Shift keys                                                                                                |
| Navigation Keys                      | Use the arrow keys for navigation. Use the Alt+arrow keys to activate home, end, page up, and page down functions.                                              |

## IMPORTANT

The keypad is designed for finger or gloved finger operation. The touch screen may be operated with a finger, gloved finger, or plastic touch screen stylus with a minimum tip radius of 1.3 mm (0.051 in.) to prevent damage to the touch screen.

Using any other object or tool may damage the touch screen or keypad.

## PanelView Plus 700 to 1500 Terminals

Overview

Chapter 1

This section gives an overview of the PanelView Plus 700, 1000, 1250, 1250H, and 1500 terminals.

-  Modular components
-  Base-configured unit
-  Communication modules
-  Logic module, standard or CE
-  Power supply, AC or DC
-  Display modules

<!-- image -->

The PanelView Plus 700 to 1500 terminals are HMI devices that offer these features:

-  Graphic color-display modules with keypad, touch screen, or keypad and touch screen support
-  Analog resistive touch screen
-  Ethernet and serial communications
-  Modular communication interface for easy add-on capability
-  Memory expansion modules for field upgrades to 256 MB RAM and 512 MB CompactFlash
-  Power input, AC (85…264V AC) or DC (18…32V DC)
-  CompactFlash card slot supports Type 1 CompactFlash cards
-  USB ports provide connections for keyboard, mouse, and printer
-  Field replaceable bezels
-  Same panel cutouts as the PanelView Standard and PanelView Enhanced terminals
-  Standard or CE logic module

## Modular Components

The terminals use modular components allowing for flexible configuration, installation, and upgrades. You can order items as separate components or factory assembled per your configuration.

<!-- image -->

## Base-configured Unit

The base-configured unit of the terminal consists of:

-  display module (700, 1000, 1250, 1500) with keypad, touch, or keypad and touch input.
-  logic module.

<!-- image -->

The logic module contains:

-  24V DC input (18…32V) or AC input (85…264V).
-  SDRAM and flash memory, various sizes.
-  10/100 BaseT Ethernet port.
-  serial RS-232 port for file transfers, printing, and logic controller communications.
-  two USB ports for attaching mouse, keyboard, or printer.
-  card slot for Type I CompactFlash cards.
-  battery-backed real-time clock.

## Logic Modules and CompactFlash

The logic module is available with or without internal CompactFlash. The contents of the internal CompactFlash is what differentiates a PanelView Plus device from a PanelView Plus CE device.

-  For the PanelView Plus terminals, the internal CompactFlash contains FactoryTalk View ME software and flash memory.
-  For the PanelView Plus CE terminals, the internal CompactFlash contains the open Windows CE operating system, FactoryTalk View ME software, and flash memory.

The internal CompactFlash is available in different sizes and can be ordered separately or bundled with the logic module.

## Communication Modules

You can attach a communication module with a network interface to the base-configured unit of the terminal to increase your communication capability with these networks:

-  DH+/DH-485
-  ControlNet

The communication module installs easily on top of the logic module on the back of the unit.

<!-- image -->

## Power Options

The basic configured units of the 700 to 1500 PanelView Plus terminals provide application flexibility with three available power power options:

-  AC (85...264V)
-  unisolated DC (18...32V)
-  isolated DC (18...32V)

For DC applications using AC power, a remote AC-to-DC power supply, cat. no. 1606-XLE120E, is available for DIN-rail mounting.

## Display Modules

The terminals offer a range of TFT color graphic displays with either keypad, touch screen, or keypad and touch screen support.

-  700 (6.5 in.)
-  1000 (10.4 in.)
-  1250 (12.1 in.)
-  1500 (15 in.)

The 700 and 1250 touch displays are available in conformal-coated options. A 1250 high-bright, touch display module is available for outdoor installations. Plus the 1250 and 1500 touch displays offer an integral antiglare overlay.

All displays have common features and firmware providing for easy migration to a larger display. Field-replaceable bezels are also available.

## Touch Screen

Touch-screen displays are analog resistive and similar except for size.

<!-- image -->

## IMPORTANT

The touch screen may be operated with a finger, gloved finger, or plastic stylus device with a minimum tip radius of 1.3 mm (0.051 in.) to prevent damage to the touch screen. Using any other object or tool may damage the touch screen.

## Keypad or Keypad and Touch

All displays are similar except for size and the number of function keys available.

<!-- image -->

## IMPORTANT

The keypad is designed for finger or gloved finger operation. The touch screen may be operated with a finger, gloved finger, or plastic stylus device with a minimum tip radius of 1.3 mm (0.051 in.) to prevent damage to the touch screen.

Using any other object or tool may damage the touch screen or keypad.

The Kxx and Fxx function keys on the keypad terminals are programmable.

| Function Keys   | Function Keys                                                               | Description                                                                                                                                                 |
|-----------------|-----------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Function Keys   | Function Keys                                                               | Programmable keys that initiate functions on terminal display. Replaceable legends are available for the terminals allowing for custom function key labels. |
|                 | 700 (F1 through F10, K1 through K12)                                        | Programmable keys that initiate functions on terminal display. Replaceable legends are available for the terminals allowing for custom function key labels. |
|                 | 1000 (F1 through F16, K1 through K16)                                       | Programmable keys that initiate functions on terminal display. Replaceable legends are available for the terminals allowing for custom function key labels. |
|                 | 1250 (F1 through F20, K1 through K20) 1500 (F1 through F20, K1 through K20) | Programmable keys that initiate functions on terminal display. Replaceable legends are available for the terminals allowing for custom function key labels. |
| Numeric Keypad  | Numeric Keypad                                                              | 0…9, ., -, Backspace, Enter, Left and Right tab, Shift, Esc, Ctrl, Alt keys.                                                                                |
| Navigation Keys | Navigation Keys                                                             | Use the arrow keys to move cursor in lists and select objects. Alt+arrow key activates home, end, page up, page down functions.                             |

Catalog Number Configuration The table shows the catalog number explanation for configured versions of the
PlViPld PlViPlCE ilNll biif PanelView Plus and PanelView Plus CE terminals. Not all combinations of options are available for sale.

<!-- image -->

## PanelView Plus Product Components

Components are available as separate catalog numbers for field installation or replacement.

## Display Modules (700 to 1500 only)

| Cat. No. Description                                              |
|-------------------------------------------------------------------|
| 2711P-RDK7C 700 keypad color display                              |
| 2711P-RDT7C 700 touch color display                               |
| 2711P-RDT7CM 700 touch color display, marine certified            |
| 2711P-RDB7C 700 keypad and touch color display                    |
| 2711P-RDB7CM 700 keypad and touch color display, marine certified |
| 2711P-RDT7CK Conformal-coated 700 touch color display             |
| 2711P-RDK10C 1000 keypad color display                            |
| 2711P-RDT10C 1000 touch color display                             |
| 2711P-RDT10CM 1000 touch display, marine certified                |
| 2711P-RDB10C 1000 keypad and touch color display                  |
| 2711P-RDB10CM 1000 keypad and touch display, marine certified     |
| 2711P-RDK12C 1250 keypad color display                            |
| 2711P-RDT12C 1250 touch color display                             |
| 2711P-RDT12AG 1250 touch color display with antiglare overlay     |
| 2711P-RDT12CK Conformal-coated 1250 touch color display           |
| 2711P-RDT12H 1250 high-bright touch color display                 |
| 2711P-RDB12C 1250 keypad and touch color display                  |
| 2711P-RDK15C 1500 keypad color display                            |

## Display Modules (700 to 1500 only)

| Cat. No. Description                                          |
|---------------------------------------------------------------|
| 2711P-RDT15C 1500 touch color display                         |
| 2711P-RDT15AG 1500 touch color display with antiglare overlay |
| 2711P-RDB15C 1500 keypad and touch color display              |

## Logic Modules (700 to 1500 only)

|                                                     | Cat. No. Description                                                           |
|-----------------------------------------------------|--------------------------------------------------------------------------------|
| Standard Logic Modules for PanelView Plus Terminals | Standard Logic Modules for PanelView Plus Terminals                            |
|                                                     | 2711P-RP Logic module without flash/RAM memory, DC input                       |
|                                                     | 2711P-RPD Logic module, without memory, isolated DC input, marine certified    |
|                                                     | 2711P-RPA Logic module without flash/RAM memory, AC input, marine certified    |
|                                                     | 2711P-RP1 Logic module with 64 MB flash/64 MB RAM, DC input                    |
|                                                     | 2711P-RP1A Logic module with 64 MB flash/64 MB RAM, AC input, marine certified |
|                                                     | 2711P-RP1D Logic module with 64MB, isolated DC input, marine certified         |
| 2711P-RP2                                           | Logic module with 128 MB flash/128 MB RAM, DC input  (1)                       |
| 2711P-RP2A                                          | Logic module with 128 MB flash/128 MB RAM, AC input, marine certified  (1)     |
| 2711P-RP2D                                          | Logic module with 128MB, isolated DC input, marine certified  (1)              |
| 2711P-RP2DK                                         | Conformal-coated logic module with 128MB, isolated DC input  (1)               |
| 2711P-RP2K                                          | Conformal-coated logic module with 128 MB flash/128 MB RAM, DC input  (1)      |
| 2711P-RP3                                           | Logic module with 256 MB flash/256 MB RAM, DC input  (1)                       |
| 2711P-RP3A                                          | Logic module with 256 MB flash/256 MB RAM, AC input, marine certified  (1)     |
| 2711P-RP3D                                          | Logic module with 256MB, isolated DC input, marine certified  (1)              |
| CE Logic Modules for PanelView Plus CE Terminals    | CE Logic Modules for PanelView Plus CE Terminals                               |
| 2711P-RP6                                           | CE logic module with 128 MB flash/128 MB RAM, DC input  (1)                    |
| 2711P-RP6A                                          | CE logic module with 128 MB flash/128 MB RAM, AC input, marine certified (1)   |
| 2711P-RP6D                                          | CE logic module with 128MB, isolated DC input, marine certified (1)            |
| 2711P-RP6DK                                         | CE conformal-coated logic module with 128MB, isolated DC input (1)             |
| 2711P-RP6K                                          | CE conformal-coated logic module with 128 MB flash/128 MB RAM, DC input (1)    |
| 2711P-RP7                                           | CE logic module with 256 MB flash/256 MB RAM, DC input  (1)                    |
| 2711P-RP7A                                          | CE logic module with 256 MB flash/256 MB RAM, AC input, marine certified (1)   |
| 2711P-RP7D                                          | CE logic module with 256 MB, isolated DC input, marine certified (1)           |

## Communication Modules

| Terminal Type Cat. No. Description   |                                                               |
|--------------------------------------|---------------------------------------------------------------|
| 400 and 600                          | 2711P-RN3 DH-485 communication module                         |
| 400 and 600                          | 2711P-RN8 DH+ communication module                            |
| 400 and 600                          | 2711P-RN15C ControlNet communication module                   |
| 400 and 600                          | 2711P-RN22C RS-232 isolated communication module              |
| 700 to 1500                          | 2711P-RN6 DH+/DH-485 communication module                     |
| 700 to 1500                          | 2711P-RN6K Conformal-coated DH+/DH-485 communication module   |
| 700 to 1500                          | 2711P-RN15S ControlNet communication module, marine certified |
| 700 to 1500                          | 2711P-RN15SK Conformal-coated ControlNet communication module |

## Internal Compact Flash

| Cat. No. Description                                            |
|-----------------------------------------------------------------|
| 2711P-RW1 64 MB CompactFlash with FactoryTalk View ME software  |
| 2711P-RW2 128 MB CompactFlash with FactoryTalk View ME software |
| 2711P-RW3 256 MB CompactFlash with FactoryTalk View ME software |

## Internal Compact Flash

| Cat. No. Description                                                                                                             |
|----------------------------------------------------------------------------------------------------------------------------------|
| 2711P-RW6 128 MB CompactFlash with FactoryTalk View ME software and the open Windows CE operating system for the CE logic module |
| 2711P-RW7 256 MB CompactFlash with FactoryTalk View ME software and the open Windows CE operating system for the CE logic module |
| 2711P-RW8 512 MB CompactFlash with FactoryTalk View ME software and the open Windows CE operating system for the CE logic module |

## RAM Memory (700 to 1500 only)

| Cat. No. Description             |
|----------------------------------|
| 2711P-RR64 64 MB SODIMM memory   |
| 2711P-RR128 128 MB SODIMM memory |
| 2711P-RR256 256 MB SODIMM memory |

## Compact Flash Cards (Blank)

| Cat. No. Description                     |
|------------------------------------------|
| 2711P-RC2 128 MB blank CompactFlash card |
| 2711P-RC3 256 MB blank CompactFlash card |
| 2711P-RC4 512 MB blank CompactFlash card |
| 2711P-RCH CompactFlash to PCMCIA adapter |

## Legend Kits

| Cat. No. Description                                            |
|-----------------------------------------------------------------|
| 2711P-RFK6 Replacement legends strips for 600 keypad terminal   |
| 2711P-RFK7 Replacement legends strips for 700 keypad terminal   |
| 2711P-RFK10 Replacement legends strips for 1000 keypad terminal |
| 2711P-RFK12 Replacement legends strips for 1250 keypad terminal |
| 2711P-RFK15 Replacement legends strips for 1500 keypad terminal |

## Backlights (700 to 1500 only)

| Cat. No. Description                                                            |
|---------------------------------------------------------------------------------|
| 2711P-RL7C Replacement color backlight for 700 series A and B display modules   |
| 2711P-RL7C2 Replacement color backlight for 700 series C and D display modules  |
| 2711P-RL10C Replacement color backlight for 1000 series A display modules       |
| 2711P-RL10C2 Replacement color backlight for 1000 series B display modules      |
| 2711P-RL12C Replacement color backlight for 1250 series A and B display modules |
| 2711P-RL12C2 Replacement color backlight for 1250 series C display modules      |
| 2711P-RL15C Replacement color backlight for 1500 series B display modules       |

## Replacement Bezels

| Cat. No. Description                                                   |
|------------------------------------------------------------------------|
| 2711P-RBK7 Replacement bezel for 700 keypad terminal                   |
| 2711P-RBT7 Replacement bezel for 700 touch terminal                    |
| 2711P-RBB7 Replacement bezel for 700 keypad or keypad/touch terminal   |
| 2711P-RBK10 Replacement bezel for 1000 keypad terminal                 |
| 2711P-RBT10 Replacement bezel for 1000 touch terminal                  |
| 2711P-RBB10 Replacement bezel for 1000 keypad or keypad/touch terminal |
| 2711P-RBK12 Replacement bezel for 1250 keypad terminal                 |
| 2711P-RBT12 Replacement bezel for 1250 touch terminal                  |
| 2711P-RBT12H Replacement bezel for 1250 high-bright touch terminal     |
| 2711P-RBB12 Replacement bezel for 1250 keypad or keypad/touch terminal |
| 2711P-RBK15 Replacement bezel for 1500 keypad terminal                 |
| 2711P-RBT15 Replacement bezel for 1500 touch terminal                  |
| 2711P-RBB15 Replacement bezel for 1500 keypad or keypad/touch terminal |

## Protective Antiglare Overlays

| Cat. No.(1)  Description                                                                   |
|--------------------------------------------------------------------------------------------|
| 2711P-RGK4 Antiglare overlay for PanelView Plus 400 grayscale terminal                     |
| 2711P-RGB4 Antiglare overlay for PanelView Plus 400 color keypad/touch terminal            |
| 2711P-RGK6 Antiglare overlay for PanelView Plus 600 keypad or keypad/touch terminal        |
| 2711P-RGT6 Antiglare overlay for PanelView Plus 600 touch terminal                         |
| 2711P-RGK7 Antiglare overlay for PanelView Plus 700 keypad or keypad/touch terminal        |
| 2711P-RGT7 Antiglare overlay for PanelView Plus 700 touch terminal                         |
| 2711P-RGK10 Antiglare overlay for PanelView Plus 1000 keypad or keypad/touch terminal      |
| 2711P-RGT10 Antiglare overlay for PanelView Plus 1000 touch terminal                       |
| 2711-RGK12 Antiglare overlay for PanelView Plus 1250 keypad or keypad/touch terminal       |
| 2711P-RGT12 Antiglare overlay for PanelView Plus 1250 touch and high-bright touch terminal |
| 2711P-RGK15 Antiglare overlay for PanelView Plus 1500 keypad or keypad/touch terminal      |
| 2711P-RGT15 Antiglare overlay for PanelView Plus 1500 touch terminal                       |

## Adapter Plates

| Cat. No. Description                                                                             |
|--------------------------------------------------------------------------------------------------|
| 2711P-RAK4 Adapts a PanelView Plus 400 keypad terminal to a PanelView Standard 550 keypad cutout |
| 2711P-RAK6 Adapts a PanelView Plus 600 keypad terminal to a PanelView Standard 600 keypad cutout |
| 2711P-RAK7 Adapts a PanelView Plus 700 keypad terminal to a PanelView Standard 900 keypad cutout |
| 2711P-RAT7 Adapts a PanelView Plus 700 touch terminal to a PanelView Standard 900 touch cutout   |

## Adapter Plates

| Cat. No. Description                                                                                                   |
|------------------------------------------------------------------------------------------------------------------------|
| 2711P-RAK10 Adapts a PanelView Plus 1000 keypad terminal to a PanelView 1000/1000E keypad cutout                       |
| 2711P-RAT10 Adapts a PanelView Plus 1000 touch terminal to a PanelView 1000/1000E touch cutout                         |
| 2711P-RAK12E Adapts a PanelView Plus 1250 (or PV1000/1000E) keypad terminal to a PanelView 1200/1400E keypad cutout    |
| 2711P-RAT12E2 Adapts a PanelView Plus 1250 (or PV1000/1000E) touch terminal to a PanelView 1200E touch cutout          |
| 2711P-RAT12E Adapts a PanelView Plus 1250 (or PV1000/1000E) touch terminal to a PanelView 1400E touch cutout           |
| 2711P-RAK12S Adapts a PanelView Plus 1250 (or PV1000/1000E) keypad terminal to a PanelView Standard 1400 keypad cutout |
| 2711P-RAT12S Adapts a PanelView Plus 1250 (or PV1000/1000E) touch terminal to a PanelView Standard 1400 touch cutout   |
| 2711P-RAK15 Adapts a PanelView Plus 1500 keypad or keypad/touch terminal to a PanelView 1200E/1400E keypad terminal    |
| 2711P-RAT15 Adapts a PanelView Plus 1500 touch terminal to a PanelView 1400E touch cutout                              |

## Cables

| Cat. No. Description                                                                          |
|-----------------------------------------------------------------------------------------------|
| 2711-NC13 RS-232 operating/programming cable (9-pin D-shell to 9-pin D-shell), 5 m (16.4 ft)  |
| 2711-NC14 RS-232 operating/programming cable (9-pin D-shell to 9-pin D-shell), 10 m (32.7 ft) |
| 2711-NC17 Remote RS-232 serial cable (9-pin D-shell to 9-pin D-shell)                         |
| 2711-NC21 RS-232 operating cable (9-pin D-shell to 8-pin mini DIN), 5 m (16.4 ft)             |
| 2711-NC22 RS-232 operating cable (9-pin D-shell to 8-pin mini DIN), 10 m (32.7 ft)            |
| 1761-CBL-AS03 DH-485 operating cable (6-pin Phoenix to RJ45), 3 m (10 ft)                     |
| 1761-CBL-AS09 DH-485 operating cable (6-pin Phoenix to RJ45), 9 m (30 ft)                     |
| 1746-C10 DH-485 network interface cable (SDL AMP to RJ45), 1.83 m (6 ft)                      |
| 1746-C11 DH-485 network interface cable (SDL AMP to RJ45), .3 m (1 ft.)                       |
| 1784-CP14 DH-485 network interface cable (5-pin Phoenix to RJ45)                              |
| 2711P-CBL-EX04 Ethernet CAT5 crossover cable, industrial grade, 4.3 m (14 ft)                 |

## Communication Adapters

| Cat. No. Description                                                                                   |
|--------------------------------------------------------------------------------------------------------|
| 1761-NET-AIC AIC+ advanced interface converter                                                         |
| 1747-AIC DH-485 isolated link coupler for use with DH-485 communication modules (2711P-RN3, 2711P-RN6) |

## Remote AC Power Supply (700 to 1500 only)

| Cat. No. Description                                               |
|--------------------------------------------------------------------|
| 1606-XLE120E DIN-rail power supply, AC-to-DC, 85…265V AC, 47…63 Hz |

## Miscellaneous

| Cat. No. Description                                                                  |
|---------------------------------------------------------------------------------------|
| 2711P-RVT12 Solar visor for outdoor high-bright 1250 touch screen display modules     |
| 2711P-RY2032 Replacement battery for 700 to 1500 terminals                            |
| 2711P-RTMC Replacement mounting clips for 700 to 1500 terminals, quantity of 8        |
| 2711P-RTFC Replacement mounting levers for 400 and 600 terminals, quantity of 8       |
| 2711P-RVAC Replacement AC power terminal block for 400 and 600 terminals              |
| 2711-TBDC Replacement DC power terminal block for 400 and 600 terminals               |
| 2711P-RTBDC3 (1) Three-position terminal block for DC logic modules, series A to D    |
| 2711P-RTBDC2 (1)  Two-position terminal block for DC logic modules, series E or later |
| 2711P-RTBAC3(1)  Three-position terminal block for all AC logic modules               |

## Firmware Upgrade Kits

|             | Cat. No. Description                                                                                                                                  |
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
|             | 2711P-RU310 PanelView Plus media kit includes firmware upgrade wizard, one firmware license, certificate of authenticity, end user license agreement. |
|             | 2711P-RUA310 PanelView Plus advanced media kit includes the 2711P-RU310 media kit, PCMCIA to compact flash adapter, and 32 MB CompactFlash card.      |
| 2711P-RUL01 | Firmware upgrade license kit with one PanelView Plus firmware license. (1)                                                                            |
| 2711P-RUL05 | Firmware upgrade license kit with five PanelView Plus firmware licenses. (1)                                                                          |
| 2711P-RUL10 | Firmware upgrade license kit with 10 PanelView Plus firmware licenses. (1)                                                                            |
| 2711P-RUL25 | Firmware upgrade license kit with 25 PanelView Plus firmware licenses. (1)                                                                            |
| 2711P-RUL50 | Firmware upgrade license kit with 50 PanelView Plus firmware licenses. (1)                                                                            |

## Notes:

## Chapter Objectives

## Hazardous Locations

## Installation

This chapter provides pre-installation information and procedures on how to install the terminals.

-  Hazardous locations
-  Environment and enclosure
-  Outdoor installation for 1250 high-bright display module
-  Required tools
-  Clearances
-  Panel cutout dimensions
-  Mount the 400 or 600 terminal in a panel
-  Mount the 700 to 1500 terminals in a panel
-  Product dimensions

When marked, this equipment is suitable for use in these locations:

-  Class I, Division 2, Groups A, B, C, D
-  Class I, Zone 2, Group IIC
-  Class II, Division 2, Groups F, G
-  Class III
-  ordinary, nonhazardous locations

The following statement applies to use in hazardous locations.

## WARNING

<!-- image -->

## Explosion Hazard

-  Do not disconnect equipment unless power has been removed and area is known to be nonhazardous.
-  Do not disconnect connections to this equipment unless power has been removed and the area is known to be nonhazardous.
-  Substitution of components may impair suitability for Class 1, Division 2.
-  Peripheral equipment must be suitable for the location it is used in.
-  The battery or realtime clock module in this product must only be changed in an area known to be nonhazardous.
-  All wiring must be in accordance with Class I, Division 2, Class II, Division 2, or Class III, Division 2 wiring methods of Articles 501, 502 or 503, as appropriate, of the National Electrical Code and/or in accordance with Section 18-1J2 of the Canadian Electrical Code, and in accordance with the authority having jurisdiction.

<!-- image -->

The terminals have a temperature code of T4 when operating in a 55 °C (131 °F) maximum ambient temperature. Do not install the terminals in environments where atmospheric gases have ignition temperatures less than 135 °C (275 °F).

## USB Ports

The terminals contain universal serial bus (USB) ports that comply with hazardous location environments. This section details the field-wiring compliance requirements and is provided in accordance with the National Electrical Code, article 500.

## PanelView Plus 400, 600, and 700 to 1500 Terminals Control Drawing

<!-- image -->

Table 1 - PanelView Plus 400, 600, and 700 to 1500 USB Port Circuit Parameters

|                                                     |                                          |      | C a            | C a            | L a            | L a            |
|-----------------------------------------------------|------------------------------------------|------|----------------|----------------|----------------|----------------|
| Display Size                                        | V oc                                     | I sc | Groups A and B | Groups C and D | Groups A and B | Groups C and D |
| 400 and 600 Series A and B                          | 5.25V DC 1.68 A 10 μF 10 μF 15 μH 15 μH  |      |                |                |                |                |
| 400 and 600 Series C or later                       | 5.25V DC 1.68 A 10 μF 10 μF 3.5 μH 15 μH |      |                |                |                |                |
| 700 to 1500 5.25V DC 1.68 A 10 μF 10 μF 15 μH 15 μH |                                          |      |                |                |                |                |

Selected nonincendive field wiring apparatus must have nonincendive circuit parameters conforming with Table 2.

Table 2 - Required Circuit Parameters for the USB Peripheral Device

| V max         |    | V oc   |
|---------------|-----|--------|
| I max         |    | I sc   |
| C i + C cable |    | C a    |
| L i + L cable |    | L a    |

## Application Information

Per the National Electrical Code the circuit parameters of nonincendive field wiring apparatus for use in hazardous locations shall be coordinated with the associated nonincendive field wiring apparatus such that their combination remains nonincendive. The PanelView Plus terminal and the USB peripheral device shall be treated in this manner.

The circuit parameters of the PanelView Plus terminal USB port are given in Table 1. The USB peripheral device and its associated cabling shall have circuit parameters with the limits given in Table 2 for them to remain nonincendive when used with the PanelView Plus terminal USB port. If cable capacitance and inductance are not known the following values from ANSI/ISA-RP 12.06.01-2003 may be used:

<!-- formula-not-decoded -->

Nonincendive field wiring must be wired and separated in accordance with 501.10(B)(3) of the National Electrical Code (NEC) ANSI/NFPA 70 or other local codes as applicable.

This associated nonincendive field wiring apparatus has not been evaluated for use in combination with another associated nonincendive field wiring apparatus.

## Symbol Definitions

| V oc   | Open circuit voltage of the host USB port.                                                                                                                                                                                        |
|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| I sc   | Maximum output current of the host USB port.                                                                                                                                                                                      |
| V max  | Maximum applied voltage rating of the USB peripheral device. V max  shall be greater than or equal to V oc  in Table 1. (V max   V oc ).                                                                                         |
| I max  | Maximum current to which the USB peripheral device can be subjected. I max  shall be greater than or equal to I sc  in Table 1. (I max   I sc ).                                                                                 |
| C i    | Maximum internal capacitance of the USB peripheral device.                                                                                                                                                                        |
| C a    | Maximum allowed capacitance of the USB peripheral device and its associated cable. The sum of C i of the USB peripheral device and Ccable of the associated cable shall be less than or equal to C a  . (C i + C cable  C a ). |
| L i    | Maximum internal inductance of the USB peripheral device.                                                                                                                                                                         |
| L a    | Maximum allowed inductance of the USB peripheral device and its associated cable. The sum of L i of the USB peripheral device and Lcable of the associated cable shall be less than or equal to L a  . (L i + L cable  L a ).  |

## Environment and Enclosure

## Outdoor Installation for High-bright Displays

## ATTENTION

<!-- image -->

This equipment is intended for use in a Pollution Degree 2 industrial environment, in overvoltage Category II applications (as defined in IEC 60664-1), at altitudes up to 2000 m (6561 ft) without derating.

The terminals are intended for use with programmable logic controllers. Terminals that are AC powered must be connected to the secondary of an isolating transformer. Terminals that are DC Class 2 powered may be supplied from an isolated DC source when used with the indicated fuse kit.

This equipment is considered Group 1, Class A industrial equipment according to IEC/CISPR 11. Without appropriate precautions, there may be difficulties ensuring electromagnetic compatibility in residential and other environments due to conducted or radiated disturbances.

This equipment is supplied as open-type equipment. It must be mounted within an enclosure that is suitably designed for those specific environmental conditions that will be present and appropriately designed to prevent personal injury resulting from accessibility to live parts. The interior of the enclosure must be accessible only by the use of a tool. The terminals meet specified NEMA Type and IEC ratings only when mounted in a panel or enclosure with the equivalent rating. Subsequent sections of this publication may contain additional information regarding specific enclosure type ratings that are required to comply with certain product safety certifications.

In addition to this publication, see:

-  Industrial Automation Wiring and Grounding Guidelines, publication 1770-4.1, for additional installation requirements.
-  NEMA Standards 250 and IEC 60529, as applicable, for explanations of the degrees of protection provided by different types of enclosure.

For more enclosure and certification information, refer to the PanelView Plus/PanelView Plus CE Outdoor High-bright Display Modules Installation Instructions, publication 2711P-IN026 .

When using the high-bright display module, cat. no. 2711P-RDT12H, outdoors, considerations in maximizing the field life of the front bezel and display are:

-  selecting the proper enclosure.
-  orientation of the terminal.

Both ultraviolet and infrared radiation can reduce the field life of any electronic device. While the materials used in the terminal bezels provide long field life, that life can be extended by proper installation.

Ultraviolet radiation from the sun causes all plastics to fade or yellow and become brittle over time. Using an antiglare overlay, cat. no. 2711P-RGT12, will protect the front of the terminal from direct exposure to UV radiation and greatly increase its field life.

When installing the high-bright display module in an environment where the front of the terminal will be in direct sunlight during the hottest part of the day and the external ambient temperature can exceed 40 °C (104 °F), use the visor kit, cat. no. 2711P-RVT12. The visor reduces the solar load on the front of the display and helps to maintain internal temperatures within specification.

The high-bright display module has a built-in temperature sensor that automatically reduces the backlight intensity if the temperature inside the cabinet exceeds 55 °C (131 °F). This reduces the risk of damage to the display.

The paint color, size, and power dissipated by the internal components of an enclosure affect the temperature rise inside the cabinet. Hoffman, a Rockwell Automation Encompass Partner, has information to assist you with enclosure selection and heating/cooling accessories to meet the temperature requirements of the installed equipment. See website http://www.hoffmanonline.com.

Stirring fans or active cooling may be required in high altitude and high ambient temperature locations to keep the internal enclosure temperature below 55 °C (131 °F). Use a heater in installations where the ambient temperature is below 0 °C (32 °F).

The backlight of the high-bright display generates a significant amount of heat when set to full intensity. To minimize the amount of heat generated and extend the life of the backlight, decrease the display intensity by using the screen saver with a 5…10 minute delay.

Avoid placing the terminal on the south (north in the southern hemisphere) or west side of the cabinet, if possible. This will reduce the heat rise due to solar loading during the hottest part of the day.

Mount the terminal vertically to minimize solar loading on the display. Do not mount the terminal in a sloped enclosure if it will be exposed to direct sunlight.

## Required Tools

## Clearances

## Cutout Dimensions

These tools are required for panel installation:

-  Panel cutout tools
-  Small, slotted screwdriver
-  Torque wrench (lb·in) for tightening the mounting clips on the PanelView Plus 700 to 1500 and PanelView Plus CE terminals

Allow adequate clearance around the terminal, inside the enclosure, for adequate ventilation. Consider heat produced by other devices in the enclosure. The ambient temperature around the terminals must be between 0…55 °C (32…131 ºF).

|         | Clearance Area 400 and 600 Terminals 700 to 1500 Terminals   |               |
|---------|--------------------------------------------------------------|---------------|
|         | Top 51 mm (2 in.) 51 mm (2 in.)                              |               |
|         | Bottom 102 mm (4 in.) 51 mm (2 in.)                          |               |
| Side(1) | 25 mm (1 in.)                                                | 25 mm (1 in.) |
| Back    | None                                                         | 25 mm (1 in.) |

Use the full size template shipped with your terminal to mark the cutout dimensions.

| Terminal Type                                              | Height mm (in.) Width mm (in.)                             |
|------------------------------------------------------------|------------------------------------------------------------|
| PanelView Plus 400 and 600 Terminals                       |                                                            |
| 400 Keypad or Keypad and Touch                             | 123 (4.86) 156 (6.15)                                      |
| 600 Keypad or Keypad and Touch                             | 142 (5.61) 241 (9.50)                                      |
| 600 Touch                                                  | 123 (4.86) 156 (6.15)                                      |
| PanelView Plus and PanelView Plus CE 700 to 1500 Terminals | PanelView Plus and PanelView Plus CE 700 to 1500 Terminals |
| 700 Keypad or Keypad and Touch                             | 167 (6.57) 264 (10.39)                                     |
| 700 Touch                                                  | 154 (6.08) 220 (8.67)                                      |
| 1000 Keypad or Keypad and Touch                            | 224 (8.8) 375 (14.75)                                      |
| 1000 Touch                                                 | 224 (8.8) 305 (12.00)                                      |
| 1250 Keypad or Keypad and Touch                            | 257 (10.11) 390 (15.35)                                    |
| 1250 Touch and 1250 High-bright Touch                      | 257 (10.11) 338 (13.29)                                    |
| 1500 Keypad or Keypad and Touch                            | 305 (12.00) 419 (16.50)                                    |
| 1500 Touch                                                 | 305 (12.00) 391 (15.40)                                    |

## Mount the 400 or 600 Terminal in a Panel

Mounting levers secure the terminal to the panel. The number of levers you use (4 or 6) varies by terminal type.

<!-- image -->

<!-- image -->

Disconnect all electrical power from the panel before making the panel cutout.

Make sure the area around the panel cutout is clear.

Take precautions so metal cuttings do not enter any components already installed in the panel.

Failure to follow these warnings may result in personal injury or damage to panel components.

Follow these steps to mount the 400 or 600 terminals in a panel.

1. Cut an opening in the panel by using the panel cutout shipped with the terminal.
2. If a communication module is ordered separately, attach the module to the base unit before panel installation.

Refer to the instructions shipped with module.

3. Make sure the terminal sealing gasket is properly positioned on the terminal.

This gasket forms a compression-type seal. Do not use sealing compounds.

<!-- image -->

4. Install legend strips before installing the terminal if you are using keypad legend strips on a 600 keypad terminal.

Be careful not to pinch legend strip during installation.

5. Place the terminal in the panel cutout.

If installing the terminal in an existing 550 panel cutout, align the terminal with the center of the cutout for best gasket sealing.

6. Insert all mounting levers into the mounting slots on the terminal.

Slide each lever until the flat side of the lever touches the surface of the panel.

<!-- image -->

7. When all levers are in place, slide each lever an additional notch or two until you hear a click.
8. Rotate each lever in the direction indicated until it is in the final latch position.

Follow the latching sequence for the optimum terminal fit.

<!-- image -->

Use this table as a guide to provide an adequate gasket seal between the terminal and the panel.

<!-- image -->

|    | Lever Position Panel Thickness Range  Typical Gauge   |
|----|-------------------------------------------------------|
|  1 | 1.5…2.01 mm (0.060…0.079 in.) 16                      |
|  2 | 2.03…2.64 mm (0.08…0.104 in.) 14                      |
|  3 | 2.67…3.15 mm (0.105…0.124 in.) 12                     |
|  4 | 3.17…3.66 mm (0.125…0.144 in.) 10                     |
|  5 | 3.68…4.16 mm (0.145…0.164 in.) 8/9                    |
|  6 | 4.19…4.75 mm (0.165…0.187 in.) 7                      |

<!-- image -->

Follow instructions to provide a proper seal and to prevent potential damage to the product. Rockwell Automation assumes no responsibility for water or chemical damage to the terminal or other equipment within the enclosure because of improper installation.

## Mount the 700 to 1500 Terminal in a Panel

Mounting clips secure the terminal to the panel. The number of clips you use (4, 6, or 8) varies by terminal type.

<!-- image -->

Disconnect all electrical power from the panel before making the panel cutout.

Make sure the area around the panel cutout is clear.

Take precautions so metal cuttings do not enter any components already installed in the panel.

Failure to follow these warnings may result in personal injury or damage to panel components.

Follow these steps to mount a 700 to 1500 terminal in a panel.

1. Cut an opening in the panel by using the panel cutout shipped with the terminal.
2. Make sure the terminal sealing gasket is properly positioned on the terminal.

This gasket forms a compression-type seal. Do not use sealing compounds.

<!-- image -->

3. Install the legend strips before installing the terminal if you are using keypad legend strips on keypad terminals.

Be careful not to pinch the legend strip during installation.

4. Place the terminal in the panel cutout.

5. Slide the ends of the mounting clips into the slots on the terminal.
6. Tighten the mounting clip screws by hand until the gasket seal contacts the mounting surface uniformly.
7. Tighten the mounting clips screws to a torque of 0.90…1.1 Nm (8…10 lb·in) by using the specified sequence, making sure not to overtighten.

<!-- image -->

<!-- image -->

<!-- image -->

## Product Dimensions

Product dimensions for each terminal are in mm (in.).

## PanelView Plus 400 Dimensions

400 Keypad or Keypad/Touch Terminal

<!-- image -->

## PanelView Plus 600 Dimensions

## 600 Keypad or Keypad/Touch Terminal

<!-- image -->

600 Touch Terminal

<!-- image -->

<!-- image -->

<!-- image -->

The depth dimensions are shown for:

-  base-configured unit (display module and logic module).
-  base-configured unit with communication module.

## PanelView Plus and PanelView Plus CE 700 Dimensions

## 700 Keypad or Keypad/Touch Terminal

a 55 (2.18) Display to Logic Module

<!-- image -->

a

b

700 Touch Screen Terminal

<!-- image -->

a 55 (2.18) Display to Logic Module b 83 (3.27) Display to Communication Module

<!-- image -->

The depth dimensions are shown for:

-  base-configured unit (display module and logic module).
-  base-configured unit with communication module.

## PanelView Plus and PanelView Plus CE 1000 Dimensions

## 1000 Keypad or Keypad/Touch Terminal

<!-- image -->

b

## 1000 Touch Screen Terminal

<!-- image -->

a 55 (2.18) Display to Logic Module b 83 (3.27) Display to Communication Module

<!-- image -->

The depth dimensions are shown for:

-  base-configured unit (display module and logic module).
-  base-configured unit with communication module.

a

a 55 (2.18) Display to Logic Module b 83 (3.27) Display to Communication Module

## PanelView Plus and PanelView Plus CE 1250 Dimensions

## 1250 Keypad or Keypad/Touch Terminal

<!-- image -->

a 55 (2.18) Display to Logic Module b 83 (3.27) Display to Communication Module

<!-- image -->

## 1250 Touch Screen Terminal

<!-- image -->

a 55 (2.18) Display to Logic Module b 83 (3.27) Display to Communication Module

<!-- image -->

The depth dimensions are shown for:

-  base-configured unit (display module and logic module).
-  base-configured unit with communication module.

## PanelView Plus and PanelView Plus CE 1500 Dimensions

## 1500 Keypad or Keypad/Touch Terminal

<!-- image -->

- a 65 (2.55) Display to Logic Module
- b 93 (3.65) Display to Communication Module

<!-- image -->

1500 Touch Screen Terminal

<!-- image -->

## Chapter Objectives

## Wiring and Safety Guidelines

## Power Connections

This chapter covers wiring and safety guidelines, and provides procedures to:

-  remove and install the power terminal block.
-  connect DC power.
-  connect AC power.
-  reset the terminal.

Use publication NFPA 70E Electrical Safety Requirements for Employee Workplaces, IEC 60364 Electrical Installations in Buildings, or other applicable wiring safety requirements for the country of installation when wiring the devices. In addition to the NFPA guidelines:

-  connect the device and other similar electronic equipment to its own branch circuit.
-  protect the input power by a fuse or circuit breaker rated at no more than 15 A.
-  route incoming power to the device by a separate path from the communication lines.
-  cross power and communication lines at right angles if they must cross.
-  Communication lines can be installed in the same conduit as low-level DC I/O lines (less than 10V).
-  shield and ground cables appropriately to avoid electromagnetic interference (EMI).
-  Grounding minimizes noise from EMI and is a safety measure in electrical installations.

For more information on grounding recommendations, refer to the National Electrical Code published by the National Fire Protection Association.

For more information, refer to Wiring and Grounding Guidelines for PanelView Plus Devices, publication 2711P-TD001. You can locate this publication in the literature library at this website http://literature.rockwellautomation.com .

<!-- image -->

## Remove and Install the Power Terminal Block

The terminals are shipped with the power terminal block installed. You can remove the terminal block for ease of installation, wiring, and maintenance.

## WARNING

<!-- image -->

## ATTENTION

<!-- image -->

Explosion Hazard

Substitution of components may impair suitability for hazardous locations.

Do not disconnect equipment unless power has been switched off and area is known to be nonhazardous.

Do not connect or disconnect components unless power has been switched off.

All wiring must comply with N.E.C. articles 501, 502, 503, and/or C.E.C. section 18-1J2 as appropriate.

Peripheral equipment must be suitable for the location in which it is used.

Disconnect all power before installing or replacing components. Failure to disconnect power may result in electrical shock or damage to the terminal.

## 400 and 600 Terminals

## ATTENTION

<!-- image -->

The AC and DC terminal blocks are keyed and marked differently so be sure to follow markings. Do not force terminal blocks into connectors to prevent potential damage to terminal.

Follows these steps to remove the terminal block in the PanelView 400 and 600 terminals.

1. Insert the tip of small, flat-blade, screwdriver into the terminal block access slot.
2. Gently pry the terminal block away from terminal to release the locking mechanism

<!-- image -->

.

Follow these steps to replace the terminal block.

1. Press terminal block base in first with block leaning outward.
2. Gently push the top of the terminal block back to the vertical position to snap in locking tab.

<!-- image -->

## 700 to 1500 Terminals

The terminal block used by the 700 to 1500 terminals depends on the series of the logic module and the power input type.

-  Series A to D, DC logic modules use a 3-position terminal block.
-  Series E or later, DC logic modules use a 2-position terminal block.
-  All logic modules with an AC power input use a 3-position terminal block.

Follow these steps to remove the terminal block.

1. Loosen the two screws that secure the terminal block.
2. Gently pull the terminal block away from the connector.

<!-- image -->

Follow these steps to install the terminal block.

1. Reattach the terminal block to the connector until seated.
2. Tighten the two screws that secure the terminal block to the connector.

## DC Power Connections

PanelView Plus terminals with an integrated, 24V DC power supply have these power ratings

|    | Power Type Terminal Input Range                                |
|----|----------------------------------------------------------------|
| DC | 400 and 600 24V DC nom (18…30 V DC) 25 W max (1.0 A at 24V DC) |

The power supply is internally protected against reverse polarity of the DC+ and DC- connections. Connecting DC+ or DC- to the earth terminal may damage the device.

The input power terminal block is removeable and supports these wire sizes. Wire Specifications for DC Power Terminal Block

| Terminal                                    | Wire Type         | Dual-wire Gauge (1)   | Single-wire Gauge                     | Terminal Screw Torque    |
|---------------------------------------------|-------------------|-----------------------|---------------------------------------|--------------------------|
| 400 and 600                                 | Stranded or solid |                       | Cu 90 °C (194 °F) 22…16 AWG 22…14 AWG | 0.45…0.56 Nm (4…5 lb•in) |
| 700 to 1500 logic module series A to D      | Stranded or solid |                       | Cu 90 °C (194 °F) 22…16 AWG 22…14 AWG | 0.23…0.34 Nm (2…3 lb•in) |
| 700 to 1500 logic module series E and later | Stranded or solid |                       | Cu 90 °C (194 °F) 22…16 AWG 22…14 AWG | 0.56 Nm (5 lb•in)        |

## External Power Supply For Non-insolated DC Terminals

TIP

To identify non-isolated DC logic modules refer to the Logic Modules (700 to 1500 only) table on page 22 .

TIP

All 400 and 600 DC terminals contain non-isolated DC power supplies.

Use a single, 24V DC power supply to power each PanelView Plus device, such as cat. no. 1606-XLE120E. Using a separate, isolated and ungrounded source to power each terminal prevents ground loop currents from damaging the terminals.

The output on the power supply must be isolated from the input and not connected to earth/ground.

The non-isolated power supply does not provide galvanic isolation. A Class 2 or Safety Extra-Low Voltage (SELV) isolated power supply with a 24V DC nominal output voltage is required to power the terminal.

ATTENTION

<!-- image -->

Use a Class 2 or SELV supply as required by local wiring codes for your installation. The Class 2 and SELV power sources provide protection so that under normal and single-fault conditions, the voltage between the conductors, and between the conductors and functional earth or protective earth does not exceed a safe value.

## Multiple AC Power Supplies to Power Multiple DC Terminals

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

## External Power for 700 to 1500 Isolated DC Terminals (2711P-RxxDx Logic Modules)

Use an SELV or PELV 24V DC power supply, such as cat. no. 1606-XLE120E, to power the isolated DC PanelView Plus terminal.

The isolated DC terminals may be powered by the same power source as other equipment, by a DC power bus.

## ATTENTION

<!-- image -->

Use an SELV or PELV supply as required by local wiring codes for your installation. The SELV and PELV power sources provide protection so that under normal and single fault conditions, the voltage between conductors and earth/ground does not exceed a safe value.

## Earth/Ground Connection

PanelView Plus devices with a DC power input have an earth/ground terminal that you must connect to a low-impedance earth/ground.

## IMPORTANT

The earth/ground connection to ground is mandatory. This connection is required for noise immunity, reliability, and Electromagnetic Compliance (EMC) with the European Union (EU) EMC directive for CE-mark conformance and is required for safety by Underwriters Laboratory.

-  The 700 to 1500 terminals have the earth/ground connection on the rear of the display module.
-  The 400 and 600 terminals have the functional earth/ground connection on the power input terminal block.

The earth terminal requires a minimum wire gauge.

## Earth Wire Specifications for DC Power

| Terminal Symbol   |     | Wire Type   | Wire Type                           | Wire Gauge   | Terminal Screw Torque                |
|-------------------|-----|-------------|-------------------------------------|--------------|--------------------------------------|
| 400 and 600       |     |             | Stranded or solid Cu 90 °C (194 °F) | 14…12 AWG    | 0.45…0.56 Nm (4…5 lb•in)             |
| 700 to1500        | GND |             | Stranded or solid Cu 90 °C (194 °F) |              | 14…10 AWG 1.13…1.36 Nm (10…12 lb•in) |

On most PanelView Plus DC terminals, the earth/ground terminal is internally connected to the DC- terminal within the product.

## ATTENTION

<!-- image -->

Damage or malfunction can occur when a voltage potential exists between two separate ground points. Make sure the terminal does not serve as a conductive path between ground points at different potentials.

The PanelView Plus terminals have isolated and nonisolated communication ports. Refer to Communication Port Isolation on page 167 for details.

IMPORTANT

For more information, refer to Wiring and Grounding Guidelines for PanelView Plus Devices, publication 2711P-TD001 .

## Connect DC Power

<!-- image -->

Explosion Hazard - Do not disconnect equipment unless power has been switched off and area is known to be nonhazardous.

Disconnect all power before installing or replacing components. Failure to disconnect power may result in electrical shock or damage to the terminal.

<!-- image -->

Follow these steps to connect the terminal to DC power.

1. Verify that the terminal is not connected to a power source.
2. Secure the DC power wires to the terminal block. Follow the markings on terminal blocks and terminal for proper connections.
3. Secure the earth/ground wire.
4.  On the 400 and 600 terminals, secure the earth/ground wire to the functional earth/ground terminal on the input power terminal block.
5.  On the 700 to 1500 terminals, secure the earth/ground wire to the earth/ground terminal screw at the bottom of the display.

400 and 600 DC Terminals

<!-- image -->

4. Apply 24V DC power to the terminal.

## AC Power Connections

<!-- image -->

PanelView Plus devices with an integrated AC power supply have these power ratings.

| Terminal  Voltage Range Frequency V A      |
|--------------------------------------------|
| 400 and 600 85…264V AC 47…63 Hz 60V A max  |
| 700 to 1500 85…264V AC 47…63 Hz 160V A max |

The input power terminal block supports these wire sizes.

## Wire Specifications for AC Power Terminal Block

| Terminal    | Wire Type         | Wire Type         | Dual-wire Gauge(1)   | Single-wire Gauge Terminal Screw Torque      |
|-------------|-------------------|-------------------|----------------------|----------------------------------------------|
| 400 and 600 | Stranded or solid | Cu 90 °C (194 °F) |                      | 22…16 AWG 22…14 AWG 0.45…0.56 Nm (4…5 lb•in) |
| 700 to 1500 | Stranded or solid | Cu 90 °C (194 °F) |                      | 22…16 AWG 22…14 AWG 0.56 Nm (5 lb•in)        |

## Protective Earth Connection

PanelView Plus devices with an AC power input have a protective earth/ground terminal that you must connect to a low-impedance earth/ground.

<!-- image -->

The protective earth connection is required for both electrical safety and Electromagnetic Compliance (EMC) with the European Union (EU) EMC directive for CE-mark conformance.

<!-- image -->

The protective earth/ground connection is on the power input terminal block. The protective earth terminal requires a minimum wire gauge.

Protective Earth Wire Specifications for AC Power

|             | Terminal PE Symbol   | Wire Type         | Wire Type         | Wire Gauge  Terminal Screw Torque   |
|-------------|----------------------|-------------------|-------------------|-------------------------------------|
| 400 and 600 |                      | Stranded or solid | Cu 90 °C (194 °F) | 14…12 AWG 0.45…0.56 Nm (4…5 lb•in)  |
| 700 to 1500 |                      |                   | Cu 90 °C (194 °F) | 14…12 AWG 0.56 Nm (5 lb•in)         |

## Functional Earth Connection

The PanelView Plus 700 to 1500 devices with an AC power input also have a functional earth connection on the back of the display.

## IMPORTANT

On 700 to 1500 devices, you must connect both protective earth and functional earth to ground.

The functional earth terminal requires a minimum wire gauge.

<!-- image -->

## Functional Earth Wire Specifications for AC Power

|             |     | Terminal FE Symbol Wire Type Wire Gauge Terminal Screw Torque   | Terminal FE Symbol Wire Type Wire Gauge Terminal Screw Torque            |
|-------------|-----|-----------------------------------------------------------------|--------------------------------------------------------------------------|
| 700 to 1500 | GND |                                                                 | Stranded or solid Cu 90 °C (194 °F) 14…10 AWG 1.13…1.36 Nm (10…12 lb•in) |

## ATTENTION

<!-- image -->

The functional earth and protective earth connections to ground are mandatory. The functional earth is required for Electromagnetic Compliance (EMC) with the European Union (EU) EMC directive for CE-mark conformance. The protective earth/ground connection is required for safety and regulatory compliance.

Power Connections

Chapter 3

## Reset the Terminals

## Connect AC Power

## WARNING

<!-- image -->

## ATTENTION

<!-- image -->

Explosion Hazard - Do not disconnect equipment unless power has been switched off and area is known to be nonhazardous.

Disconnect all power before installing or replacing components. Failure to disconnect power may result in electrical shock or damage to the terminal.

Improper wiring of the power terminals may result in voltage at the communication connector shells.

Do not apply power to the terminal until all wiring connections have been made. Failure to do so may result in electrical shock.

Follow these steps to connect the terminal to AC power.

1. Verify that the terminal is not connected to a power source.
2. Secure the AC power wires to the terminal block. Follow the markings on terminal blocks and terminal for proper connections.
3. Secure the protective earth/ground wire to the marked position of the power input terminal block.
4. On the 700 to 1500 devices, also secure the functional earth/ground wire to the functional earth terminal screw on the back of the display to ground bus.
5. Apply AC power to the terminal.

<!-- image -->

Use the reset switch to restart a terminal without having to disconnect and reapply power. After a reset, the terminal performs a series of startup tests and then either:

-  runs the .MER application loaded in the terminal.

-  opens the desktop on CE terminals only.
-  enters Configuration mode.

The action that occurs depends on the startup options configured for your terminal.

Refer to Chapter 9 , T Troubleshoot the System, for a list of startup information and error messages.

<!-- image -->

-  On 400 to 600 terminals, press the reset switch with your finger or a nonconductive object.
-  On 700 to 1500 terminals, insert a thin, nonconductive probe into the hole marked reset and press the switch.

## ATTENTION

<!-- image -->

Use a nonconductive object to press the reset or default switch. Do not use a conducting object such as a paper clip or you may damage the terminal. Do not use the tip of a pencil; graphite may damage the terminal.

## Notes:

## Chapter Objectives

## Access Configuration Mode

## Configuration Mode

This chapter shows how to use the Configuration mode of your PanelView Plus terminal to:

-  perform data entry and navigation.
-  load an application.
-  run an application.
-  modify application settings.
-  modify terminal settings.
-  configure startup shortcuts for PanelView Plus CE devices.

Your PanelView Plus device has onboard software, FactoryTalk View ME Station, to perform and configure terminal operations. When you reset or start the terminal, you automatically enter Configuration mode, unless your .MER application is automatically set to run on startup.

To access Configuration mode from a running application, press the Goto Configuration Mode button. This button is added to the application screen in FactoryTalk View Studio. The application stops running but is still loaded.

## IMPORTANT

To access Configuration mode from a running application, you must add a Goto Configuration Mode button to an application screen.

On PanelView Plus CE devices, you can enter Configuration mode from the Start menu or the desktop.

-  Select Start&gt;Programs&gt;Rockwell Software&gt;FactoryTalk View&gt;FactoryTalkView ME Station.
-  Select the FactoryTalk View ME Station icon on the desktop.

<!-- image -->

## Configuration Mode Main Screen

<!-- image -->

| Terminal Operation Description                                                                                                                                                                                                                                             |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Load Application (F1) Opens another screen where you can select an application to load. Once loaded, the application name will appear under Current Application.                                                                                                           |
| Run Application (F2) Runs the .mer application displayed under Current Application. An application must be loaded before you can run it.                                                                                                                                   |
| Application Settings (F3) Opens a menu of application-specific configuration settings.                                                                                                                                                                                     |
| Terminal Settings (F4) Opens a menu of options to configure non-application, specific terminal settings for the PanelView Plus device.                                                                                                                                     |
| Delete Log Files Before Running (F5) Toggles between Yes and No. If you select Yes, all data log files, alarm history and alarm status file will be deleted before the application is run. If you select No, log files are not deleted first.                              |
| Reset (F7) Resets the terminal. The action that occurs on startup for PanelView Plus CE devices depends on whether you defined shortcut paths in the Windows Startup folder. On other PanelView Plus devices, the action on startup depends on configured startup options. |
| Exit (F8) Exits Configuration mode.                                                                                                                                                                                                                                        |

## Navigation Buttons

Screen buttons are used for data entry and navigation.

-  On touch-screen terminals, tap the button with your finger or stylus.
-  On keypad terminals, select the function key listed on the button, or in some cases, the corresponding key on the keypad.
-  If a mouse is attached, click a button.

In addition to operation specific buttons, most screens have a combination of these buttons.

<!-- image -->

| Navigation Buttons   | Description                                               |
|----------------------|-----------------------------------------------------------|
| Close [F8]           | Returns to the previous screen.                           |
| OK [F7]              | Accepts modified values and returns to previous screen.   |
| Cancel [F8]          | Cancels the current operation without saving any changes. |
|                      | Moves highlight up or down a list.                        |
|                      | Selects a highlighted screen or item from a list.         |

## Enter or Edit Data

Many screens have buttons that access fields where you must enter or edit data. When you press the button or function key, the input panel opens ready for you to enter data. If a field is restricted to a numeric value, only the 0…9 keys will be enabled. If the value is an IP address, the 0…9 and decimal point keys will be enabled. All other buttons will be disabled.

<!-- image -->

| Input Panel Controls   | Function                                                                                                                    |
|------------------------|-----------------------------------------------------------------------------------------------------------------------------|
| SHF                    | Switches keys between their shifted and unshifted state. The initial default is shifted.                                    |
| CAPS                   | Switches keys between lowercase and uppercase characters. The initial default is lowercase.                                 |
| SPACE                  | Enters a space between characters in the Display Area.                                                                      |
| Backspace              | Deletes the previous character (to the left of the cursor) in the Display Area.                                             |
| Select                 | Selects a character and enters it in the Display Area.                                                                      |
|                        | Right, Left, Up, Down Arrow Keys Selects the character to the right, left, above or below the currently selected character. |
| Enter                  | Accepts the entered characters and returns to the previous screen                                                           |
| ESC                    | Cancels the current operation and returns to the previous screen.                                                           |

Follow these steps to enter characters in the display area.

1. Select a character on the character keyboard.
2.  On a touch-screen terminal, tap or press a key.
3.  On a keypad terminal, use the arrow keys on the keypad to select a key.
4.  If a mouse is attached, click a key.
2. Press the Select button to copy the character to the display area.
3. Press Enter when done to exit the input panel.

## Load an Application

You can load a FactoryTalk View ME .MER application from the internal CompactFlash in the terminal or an external CompactFlash card.

<!-- image -->

Follows these steps to load an application.

1. Select Load Application from the main screen.
2. Press the Source button to select the storage location of the application file you want to load.
3.  Internal Storage - the internal CompactFlash in the terminal.
4.  External Storage 1 - the external CompactFlash card loaded in the card slot of the terminal.
5.  External Storage 2 - for future use.

<!-- image -->

FactoryTalk View ME software only recognizes files in the \Rockwell Software\RSViewME\Runtime\ folder.

3. Select an .MER file from the list by using the up and down cursor keys.
4. Press the Load button to load the selected application.

You will be asked if you want to replace the terminal's communication configuration with the configuration in the application.

5. Select Yes or No.

If you select Yes, any changes to the device addresses or driver properties in the RSLinx Communications screen will be lost.

The name of the currently loaded application will appear at the top of the main configuration screen.

## Run an Application

## Application Settings

## Terminal Settings

After loading an .MER application, you can run the application. To load an application, select the Run Application button on the main screen.

Log files are generated by the application. To delete the log files before running an application, select the Delete Log Files Before Running button on the main screen.

You can show device shortcuts defined for the loaded .MER application. For example, your .MER application might have SLC defined as a device shortcut name for the SLC 5/05 controller. Device shortcuts are read-only and cannot be edited. To view device shortcuts, select the Application Settings button from the main screen.

You can modify settings on the terminal that are not specific to the application.

| Terminal Settings   | Description                                                                                                                                                                    |
|---------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Diagnostic          | Forwards diagnostic messages form a remote log destination to a computer running diagnostics.                                                                                  |
| Display             | Shows the temperature of the display, sets the intensity of the backlight, and enables/disables the screen saver.                                                              |
| File Management     | Copies or deletes application files or font files from a storage location.                                                                                                     |
| Font Linking        | Links a font file to a base font loaded on the terminal.                                                                                                                       |
| Input Devices       | Configures settings for the keypad, touch screen, or attached keyboard and mouse.                                                                                              |
|                     | Networks and Communications Configures network connections and communication settings specific to the application (DHPlus, DH-485, remote I/O, ControlNet, DeviceNet, serial). |
| Print Setup         | Configures settings for printing displays, alarm messages, and diagnostics messages generated by the application.                                                              |
| Startup Options     | Specifies whether the terminal starts up in configure or run mode. Also lets you enable/disable tests to run on the terminal at startup.                                       |
| System Event Log    | Displays a list of system events currently logged by the terminal.                                                                                                             |
| System Information  | Displays power, temperature, battery and memory details for the terminal. Also shows the firmware number for FactoryTalk View ME software and technical support information.   |
|                     | Time/Date/Regional Settings Sets the date, time, language, and numeric format used by the terminal and applications.                                                           |

## Configure Communication

Follow these steps to access terminal settings and select a function.

1. Select Terminal Settings from the main screen.
2. Highlight an option by using the up and down cursor buttons.
3.  On touch screen terminals, press the buttons.
4.  On keypad terminals, press a key on the keypad or the corresponding function key.
3. Press the Enter key to access the highlighted function.

<!-- image -->

You configure communication for your application and controller by using RSLinx Enterprise software.

-  Access KEPServer Serial Port ID's.
-  Edit or view the driver settings for the communication protocol used by your .MER application.
-  Edit the device address of the controller on the network.

## KEPServer Serial Port ID's

To access the KEPServer Serial Port ID's screen, you must have KEPServer Enterprise installed on your terminal. Otherwise, you will get an error message when accessing this screen. If you plan on using KEPServer Enterprise and serial communication, you must specify which COM port to use.

To access the KEPServer Serial Port ID screen, select Terminal Settings&gt;Networks and Communications&gt;KEPServer Serial Port ID's.

## Configure Communication Properties

Follow these steps to configure driver settings for the communication protocol used by your application.

1. Select Terminal Settings&gt;Networks and Communications&gt;RSLinx Enterprise Communications.

You see a tree view of installed communication cards and network configurations.

<!-- image -->

2. Select the communication card installed on your terminal.
3. Press the Edit Driver button to view the current properties for the communication driver.
4. Select the property you want to modify, then press the Edit button.
5. Modify the setting and then press the Enter button.

<!-- image -->

You return to the previous screen with the newly entered data.

## DHPlus Properties

| Field  Description                                                                       | Valid Values    |
|------------------------------------------------------------------------------------------|-----------------|
| Jumper ID Identifies the communication card if multiple cards are installed on terminal. | 0…3             |
| Station Number The unique address of the terminal on the DHPlus network.                 | 0…77 (octal)    |
| Baud Rate The communication rate of the DHPlus network. 57,600 (default)                 | 115,200 230,400 |

## DH-485 Properties

| Field  Description                                                                                                                | Valid Values   |
|-----------------------------------------------------------------------------------------------------------------------------------|----------------|
| Jumper ID Identifies the communication card if multiple cards are installed on terminal.                                          | 0…3            |
| Station Number The unique station number of the terminal on the DH-485 network.                                                   | 0…31 (decimal) |
| Baud Rate The communication rate of the DH-485 network. 9600                                                                      | 19,200         |
| MaxStationNumber The maximum station number on the DH-485 network. The value must be greater than or equal to the Station Number. | 0…31 (decimal) |

## Remote I/O Properties

| Field  Description                                                                       | Valid Values    |
|------------------------------------------------------------------------------------------|-----------------|
| Jumper ID Identifies the communication card if multiple cards are installed on terminal. | 0…3             |
| Baud Rate The communication rate of the remote I/O network. 57,600 (default)             | 115,200 230,400 |

## ControlNet Properties

| Field     | Description                                                              | Valid Values   |
|-----------|--------------------------------------------------------------------------|----------------|
| Device ID | Unique address of the PanelView Plus terminal on the ControlNet network. | 1…99           |

## DeviceNet Properties

| Field   | Description                                                                  | Valid Values                         |
|---------|------------------------------------------------------------------------------|--------------------------------------|
| MacID   | Unique address of the terminal on the DeviceNet network.                     | 0…63                                 |
|         | Baud Rate The communication rate at which the DeviceNet driver communicates. | 125 Kbps (default) 250 Kbps 500 Kbps |

## Serial Properties

| Field     | Description                                                                                                                          | Valid Values                                                            |
|-----------|--------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------|
| Device    | The serial device your terminal is connected to. PLC_CH0                                                                             | KF2 SLC_CH0 KF3 KFC KFC15 AC_CH0                                        |
|           | Error Check Type of error checking used. Error checking is automatically configured if Use Auto Config is set to Yes.                | BCC, CRC                                                                |
| Parity    | Type of parity used. The parity is automatically configured if Use Auto Config is set to Yes.                                        | None, Odd, Even                                                         |
| Stop Bits | Number of stop bits used.                                                                                                            | 1 or 2                                                                  |
|           | Ack Timeout Ack/Poll timeout value in ms.                                                                                            | 20…60,000 ms                                                            |
|           | Max Retries Maximum number of retries before the serial driver fails.                                                                | 0…255                                                                   |
| Station   | Station number based on a specific device. PLC_CH0 0…77 (octal)                                                                      | KF2 0…77 (octal) SLC_CH0 0…31 KF3 0…31 KFC 1…99 KFC15 1…99 AC_CH0 0…255 |
|           | Baud Rate Data rate at which serial driver communicates. The baud rate is automatically configured if Use Auto Config is set to Yes. | 110 300 600 1200 4800 9600 19,200                                       |
|           | Use Auto Config Automatically or manually configures the baud rate, parity, and error checking parameters.                           | Yes (auto configure) No (manual configure)                              |
| Com Port  | Communication port used on the terminal. 1 (COM1)                                                                                    | 2 (COM2)                                                                |

## Configure the Controller Address

Follow these steps to edit the device address of the logic controller.

1. From the RSLinx Configuration screen, select a device node.
2. Press the Edit Device button to view the device name and current address of the logic controller.
3. Press the Device Address button to modify the address.

<!-- image -->

The input panel opens with the current address.

4. Use the Input Panel to modify the address and then press the Enter button.

You return to the previous screen with the new address.

5. Press OK.

IMPORTANT

Modified settings do not take effect until the terminal is restarted.

## Configure Network Information

You can configure network information for your terminal.

-  Device name to identify terminal on network
-  IP address of terminal on network
-  Username and password to access network resources

## Define a Device Name for the Terminal

You can configure a device name and description to identify your your terminal on the network.

Follow these steps to enter a device name and description for your terminal.

1. Select Terminal Settings&gt;Networks and Communications&gt;Network Connections&gt;Device Name.
2. Press the Device Name button to enter or edit the device name.
3. Press the Device Description button to enter or edit the description for the device.
4. Press OK.

<!-- image -->

| Field           | Description                                                                  | Valid Values                                                                                                                                                      |
|-----------------|------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Device Name (1) | Name that identifies the terminal to other computers on the network.         | 1…15 characters A leading character in the range of a through z or A through Z. Remaining characters in the range of a through z, A through Z, 0…9, or - (hyphen) |
|                 | Device Description Provides a description of the terminal. 50 characters max |                                                                                                                                                                   |

## Define an Ethernet IP Address

Some networks automatically assign IP addresses to Ethernet devices if DHCP is enabled. If DHCP is not enabled, you can manually enter an IP address for the terminal.

Follow these steps to view or enter an IP address for your terminal.

1. Select Terminal Settings&gt;Networks and Communications&gt;Network Connections&gt;Network Adapters.
2. Press the IP Address button to view or modify the IP address.
3. Press the DHCP button to enable or disable DHCP assignment of addresses.
4. Press the IP address, Subnet Mask, and Gateway buttons, then enter the appropriate information.
5. Press OK when done.

<!-- image -->

<!-- image -->

|                                                                                                                                                                                                                                                                                                                                                                                                                   | Field Description Valid Values                                                                                                                                                                                     |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Use DHCP Enables or disables Dynamic Host Configuration Protocol (DHCP) settings. DHCP automatically allocates network devices and configurations to newly attached devices on the network. If DHCP is set to Yes, the terminal is automatically assigned an IP address, Subnet Mask, and Gateway. The fields are disabled. If DHCP is set to No, you can enter the IP address, Subnet Mask, and Gateway address. | Yes (default) No                                                                                                                                                                                                   |
| IP Address A unique address identifying the terminal on the Ethernet network.                                                                                                                                                                                                                                                                                                                                     | xxx.xxx.xxx.xxx 000.000.000.000 (default) Range of values for the first set of decimal numbers is 1…255 unless all fields are set to 000. The range of values for the last three sets of decimal numbers is 0…255. |
| Subnet Mask Address must be identical to the server subnet mask. xxx.xxx.xxx.xxx                                                                                                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                    |
| Gateway Optional Gateway address. xxx.xxx.xxx.xxx                                                                                                                                                                                                                                                                                                                                                                 |                                                                                                                                                                                                                    |
| Mac ID Read-only field.                                                                                                                                                                                                                                                                                                                                                                                           |                                                                                                                                                                                                                    |

## Define Name Server Addresses

You can define name server addresses for the EtherNet/IP network adapter.

- These addresses are automatically assigned if DHCP is enabled for the network adapter.

<!-- image -->

Follow these steps to define name server address.

1. Select Terminal Settings&gt;Networks and Communications&gt;Network Connections&gt;Network Adapters.
2. Press a button to enter a name server address.
3. Press OK when done.

| Field  Description  Valid Values                                           |
|----------------------------------------------------------------------------|
| Primary DNS The address of the primary DNS resolver. xxx.xxx.xxx.xxx       |
| Secondary DNS The address of the secondary DNS resolver. xxx.xxx.xxx.xxx   |
| Primary WINS The address of the primary WINS resolver. xxx.xxx.xxx.xxx     |
| Secondary WINS The address of the secondary WINS resolver. xxx.xxx.xxx.xxx |

## Configure Diagnostics

## Authorize Terminal to Access Network Resources

The terminal can access network resources with proper identification. A user name, password, and domain must be provided by your network administrator.

1. Select Terminal Settings&gt;Network and Communications&gt;Network Connections&gt;Network Identification.
2. Press the user name, password and domain buttons and enter the information provided by your network administrator.
3. Press OK when done.

<!-- image -->

| Field  Description                                                        | Valid Values            |
|---------------------------------------------------------------------------|-------------------------|
| User Name Identifies the user to the network.                             | 70 characters max       |
| Password Characters that gain access to network along with the user name. | No character limitation |
| Domain Name Provided by network administrator.                            | 15 characters max       |

You can configure diagnostics for the current computer. To access the diagnostic screen, select Terminal Settings&gt;Diagnostic Setup from the main screen. The screen shows a tree view of diagnostic nodes.

<!-- image -->

## Remote Log Destination

The Remote Log Destination forwards messages that it receives to a Windows 2000/XP computer running diagnostics. The location is determined by the IP address and port number.

| Field   | Description                                                            | Valid Values    |
|---------|------------------------------------------------------------------------|-----------------|
|         | Address Address of the remote Windows 2000/XP computer.                | xxx.xxx.xxx.xxx |
| Port    | The port used to communicate with the remote Windows 2000/XP computer. | 4445 (default)  |

## Message Routing

The Message Routing screen lets you access these screens:

-  Remote Log
-  FactoryTalk View Diagnostics List

Each of the above screens shows a list of messages that can be sent to that destination. The list shows the On/Off status of each message type. Use the On/Off button to turn a message type on or off. A message type is enabled if it has a checked box.

<!-- image -->

## Manage Files on the Terminal

The terminal provides operations for managing files that are stored on the terminal.

-  Delete application .MER files, font files, or log files that reside in a storage location on the terminal.
-  Copy application .MER files or font files from one storage location to another.

## Delete an Application File or a Font File

The procedure for deleting an application file or a font file from the terminal is the same except for the type of file you are deleting.

1. Select Terminal Settings&gt;File Management&gt;Delete Files&gt;Delete Applications or Delete Fonts.
2. Press the Source button to choose the storage location of the application or font file you want to delete.
3.  Internal Storage - the internal CompactFlash in the terminal.
4.  External Storage 1 - the external CompactFlash card loaded in the card slot of the terminal.
5.  External Storage 2 - for future use.
3. Select a file from the list.
4. Press the Delete button.
5. Select Yes or No when asked if you want to delete the selected application or font file from the storage location.

<!-- image -->

## Delete Log Files from Terminal

You can delete log files, alarm history files, and alarm status files from the System Default location on the terminal.

1. Select Terminal Settings&gt;File Management&gt;Delete Files&gt;Delete Log Files.

You are asked to confirm the deletion of the files.

Do you want to delete all of the FactoryTalk View ME Station Log Files?

2. Select Yes or No.

Log files not located in the System Default location will not be deleted.

## Copy an Application File or Font File

The procedure for copying an application .MER file or a font file from one storage location on the terminal to another is the same.

1. Select Terminal Settings&gt;File Management&gt;Copy Files&gt;Copy Applications or Copy Fonts.
2. Press the Source button to choose the location of the application or font file you want to copy.
3.  Internal Storage - the internal CompactFlash in the terminal.
4.  External Storage 1 - the external CompactFlash card loaded in the card slot of the terminal.
5.  External Storage 2 - for future use.
3. Select a file from the storage location.

<!-- image -->

4. Press the Destination button on the same screen.
5. Press the Destination button to choose the storage location where you want to copy the application or font file.

<!-- image -->

The destination must be different than the source location.

-  Internal Storage - the internal CompactFlash in the terminal.
-  External Storage 1 - the external CompactFlash card loaded in the card slot of the terminal.
-  External Storage 2 - for future use.
6. Press the Copy button to copy the selected application or font file to the selected destination.

If the file exists, you will receive a warning and will be asked if you want to overwrite the existing application.

7. Select Yes or No.

<!-- image -->

FactoryTalk View ME software looks for .MER files in the \Rockwell Software\RSViewME\Runtime folder and font files in the \Rockwell Software\RSViewME\Fonts\ folder.

## Modify Display Settings

You can access and modify these display settings for your terminal:

-  View display temperature
-  Adjust display contrast
-  Adjust display intensity
-  Configure the screen saver
-  Enable or disable the screen cursor

## View the Display Temperature

To view the current temperature of the display, select Terminal Settings&gt;Display&gt;Display Temperature.

<!-- image -->

The PanelView Plus 600 to 1500 terminals have a cold-cathode fluorescent lamp (CCFL) backlight. This backlight requires temperature control when the internal temperature of the product is below 10 °C (50 °F) or above 60 °C (140 °F). The terminal monitors low and high temperature conditions.

-  If the internal temperature of the product is below 10 °C (50 °F), the backlight is set to overdrive or the full-rated current setting for at least five minutes.
-  If the internal temperature is at or above 60 °C (50 °F), the backlight is set to underdrive; 40% or less of full brightness. This reduces heat generation from the backlight.

Temperature monitoring begins when the terminal powers on, or when the backlight turns on, for example, exiting Screen Saver mode. The temperature control affects only display intensity; it does not restrict the use or operation of the terminal.

When a low or high temperature condition is detected, an error is sent to the system event log. If the temperature control is not functioning, a noncritical error is sent to the system event log but the terminal continues to operate normally.

<!-- image -->

The CCFL backlight temperature control takes precedence over the application Backlight Settings.

## Adjust the Display Contrast

You can view or modify the display contrast for PanelView 400 and 600 grayscale terminals. Displays are shipped with the contrast level set at 50%, which is the optimum setting.

1. Select Terminal Settings&gt;Display&gt;Display Contrast.
2. Press the up an down cursor buttons to adjust the contrast. The current contrast level is shown as a percentage. The change is not permanent until you press OK.
3. Press OK when done.

<!-- image -->

## Adjust the Display Intensity

You can view or modify the intensity of the terminal backlight. You can use the default intensity of 100% or you can set the intensity for runtime operations.

1. Select Terminal Settings&gt;Display&gt;Display Intensity.
2. Press the Startup Intensity button to switch between the Default intensity and the Runtime intensity.
3.  If you choose Runtime, the startup screens will use the runtime intensity.
4.  If you choose Default, the startup screens will use the default setting of 100%
3. Increase or decrease the intensity for runtime operations, by pressing the up or down arrow keys.
6. Intensity changes are not permanent until you press OK.
4. Press OK when done.

<!-- image -->

## Configure the Screen Saver

The terminal screen saver activates after an idle period using a specific intensity. You can adjust the idle timeout and intensity, disable the screen saver, and enable or disable the screen saver bitmap.

1. Select Terminal Settings&gt;Display&gt;Screen Saver.
2. Press the Screen Saver button to select an idle timeout for activating the screen saver.

<!-- image -->

To disable the screen saver, select the Disabled option.

3. Increase or decrease the brightness intensity of the screen saver by pressing the up and down cursor buttons.
4. Press the Advanced Settings button to access the bitmap option.
3.  Select the Screen Saver Image button to enable or disable the screen saver bitmap.
4.  Press OK to return to the previous.
5. Press OK to exit and return to the terminal settings.

## Enable or Disable the Screen Cursor

The terminal has a screen cursor that you can enable or disable.

1. Select Terminal Settings&gt;Display&gt;Cursor.
2. Press the Enable Cursor button to enable or disable the cursor.
3. Press OK to exit and return to Terminal Settings.

<!-- image -->

## Font Linking

<!-- image -->

Font linking lets you run a translated application on the terminal by linking a font file to the base font (for example, linking a Chinese font file to the base font Arial).

For more details on preinstalled terminal fonts and additional fonts available for downloading, see Appendix C .

<!-- image -->

## Configure Keypad, Keyboard, or Mouse

You can configure input devices used with your terminal, including the keyboard, keypad, mouse, and attached keyboard.

## Configure Keyboard Settings

You can adjust settings for the keys on the terminal keypad or for keys on an attached keyboard.

1. Select Terminal Settings&gt;Input Devices&gt;Keyboard.
2. Press the Repeat Rate button to specify the number of times a key is repeated per second when you hold a key down.
3. Valid values for the keypad are 0 and 2…30. The keyboard is device dependent but typical values are the same.
3. Press the Repeat Delay button to select the amount of time that elapses per second before a key is repeated.
5. Values are device dependent. Unsupported values are dimmed.
4. Press OK when done.

<!-- image -->

## Configure Keypad Settings for the Terminal

You can restrict multiple or simultaneous key presses on the keypad of your terminal.

1. Select Terminal Settings&gt;Input Devices&gt;Keypad.
2. Press the Single Key Mode button to select a key option.
3.  If Enabled, any programmable key that is pressed inhibits all keys until the programmable key is pressed again. This includes the Alt, Ctrl, Shift keys.
4.  If Enabled with Abort, any secondary key press will terminate the initial key press immediately.
5.  If Disabled, there are no restrictions on key presses. This is the default.

<!-- image -->

## IMPORTANT

The keypad cannot produce Home, End, Page Up or Page Down when Single Key mode is enabled.

3. Press the Hold Off Time button to enter the length of time, in seconds, to ignore multiple presses of the same key.
4. Press OK when done.

## Configure the Sensitivity of the Mouse

You can set and test the sensitivity for both the speed and physical distance between mouse clicks. The process is identical to setting the double-tap sensitivity for the touch screen.

To set the mouse sensitivity, select Terminal Settings&gt;Input Devices&gt;Mouse.

## Configure the Touch Screen

You can configure these operations for terminals with a touch screen:

-  Calibrate the touch screen
-  Enable or disable Cursor
-  Set the double-tap sensitivity

## Calibrate the Touch-screen

## IMPORTANT

Use a plastic stylus device with a minimum tip radius of 1.3 mm (0.051 in.) to prevent damage to the touch screen.

Follow these steps to calibrate the touch screen.

- 1.
- Select Terminal Settings&gt;Input Devices&gt;Touch Screen&gt;Calibration.

The screen for calibrating the touch screen appears.

- Carefully press and briefly hold stylus on the center of the target. Repeat at as the target moves around the screen.

2. Touch the center of the target (+) each of the four times it appears on the screen.

When the calibration is complete, you will see this message.

Tap the screen to register saved data. Wait for 30 seconds to cancel saved data and keep the current settings.

3. Tap the screen to save the data or wait 30 seconds to cancel the saved data, retaining the current settings.

## Enable or Disable the Cursor on Touch Screens

You can enable or disable the cursor on terminals with a touch screen. Disabling the cursor will not disable the mouse.

1. Select Terminal Settings&gt;Input Devices&gt;Touch Screen&gt;Cursor.
2. Press the Enable Cursor button to enable or disable the cursor.
3. Press OK.

<!-- image -->

## Set the Double-tap Sensitivity

You can set and test the sensitivity for both the speed and physical distance between touch-screen presses. The process is identical to setting the double-tap sensitivity for the mouse.

1. Select Terminal Settings&gt;Input Devices&gt;Touch Screen&gt;Double-tap Sensitivity.
2. Double-tap the Set button to set the sensitivity of touch-screen presses.
3. Double-tap the Test button to test the sensitivity of touch-screen presses. If you double-tap the test button with the time set using the Set button, the Test button will reverse its foreground and background colors.
4. Press OK when done.

<!-- image -->

## Configure Print Options

You can configure settings for printing displays, alarm messages, or diagnostic messages from FactoryTalk View ME .MER applications. The general setup for printing displays and messages is the same, however, the advanced settings are different.

1. Select a Terminal Settings&gt;Networks and Communications&gt;Print Setup&gt; option.
2.  Displays
3.  Alarms
4.  Diagnostic Messages
2. Update properties by selecting the appropriate button and changing the value, if necessary.
3. Press the Advanced button to access additional settings.

<!-- image -->

| Field   | Description                                                                   | Valid Values           |
|---------|-------------------------------------------------------------------------------|------------------------|
|         | PCL Printer Type of printer to use.                                           | Laser (default) Inkjet |
| Port    | Port to use for printing displays, alarm messages, and diagnostic messages.   | Network (default) USB  |
|         | Network Path Network path of printer to use if the Port selection is Network. | 519 characters max     |
|         | Advanced Settings Accesses additional settings.                               |                        |

The advanced settings for printing displays are:

-  print orientation (portrait or landscape).
-  draft mode (enable or disable).

-  The advanced settings for printing diagnostic and alarm messages determines when to print messages that are sent to the network or USB port.
4. Press OK when done.
5. Press OK to return to Terminal Settings.

<!-- image -->

| Print Messages After                                                | Default Value Example          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|---------------------------------------------------------------------|--------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Specified number of messages                                        |                                | 60 messages When the queue has 60 messages, the messages are printed regardless of how long they have been in the queue. You can change the number of messages.                                                                                                                                                                                                                                                                                                         |
| 500 messages or timeout period, whichever is first                  |                                | 168 hours (7 days) If the queue has 350 messages after 168 hours, the 350 messages are printed. You can change the timeout period.                                                                                                                                                                                                                                                                                                                                      |
| Specified number of messages or timeout period, whichever is first. | 60 messages 168 hours (7 days) | If the queue has 60 messages after 24 hours, then the 60 messages are printed. You can change the number of messages and the timeout period. For example, the number of messages is set to 75 and the timeout period is set to 48 hours.   If the queue has 75 messages after 24 hours, then the 75 messages are printed before the set timeout of 48 hours.   If the queue has 15 messages after 48 hours, the 15 messages are printed after the set timeout period. |

## Configure Startup Options

FactoryTalk View ME Station software starts based on shortcuts in the Windows startup folder and whether an application is loaded. You can modify the action the terminal takes on startup.

-  Disable FactoryTalk View ME Station software
-  Go to FactoryTalk View Configure mode
-  Run the current application

## Disable FactoryTalk View ME Station Software on Startup

1. Select Terminal Settings&gt;Startup Options&gt;FactoryTalk View ME Station Startup.
2. Press the On Startup button until Do not start FactoryTalk View ME is selected.
3. Press OK.

<!-- image -->

## Enter Configuration Mode on Startup

Follow these steps to enter Configuration mode on startup.

1. Select Terminal Settings&gt;Startup Options&gt;FactoryTalk View ME Station Startup.
2. Press the On Startup button to select Go to Configuration Mode.
3. Press the Configuration Mode Options button.
4. Press the Load Current Application button to specify whether you want to load the current application on startup.
5. Press the Replace RSLinx Communications button to specify whether to use the communication configuration of the current application or the terminal on startup.
6.  Select No to use the RSLinx configuration of the terminal.
7.  Select Yes to use the configuration of the application. The terminal configuration is replaced with the application settings. Any changes to device addresses or driver properties in RSLinx communication will be lost.
6. Press OK to return to the previous screen.
7. Press OK to return to Terminal Settings.

<!-- image -->

<!-- image -->

## Run the Loaded Application on Startup

Follow these steps to run the loaded application on startup.

1. Select Terminal Settings&gt;Startup Options&gt;FactoryTalk View ME Station Startup.
2. Press the On Startup button to select Run Current Application.

<!-- image -->

<!-- image -->

If an application is not loaded, the options are disabled.

3. Press the Replace RSLinx Communications button to specify what configuration settings to use when running the application.
2.  Select No to use the RSLinx configuration of the terminal.
3.  Select Yes to use the configuration of the application. The terminal configuration is replaced with the application settings. Any changes to device addresses or driver properties in RSLinx communication will be lost.
4. Press the Delete Log Files to specify what action to take with the log files on startup.
5.  Select Yes to delete all log files (data, alarm history, alarm status) generated by the terminal before running application. The files are deleted from the system default location.
6.  Select No to retain all log files.
5. Press OK twice to return to Terminal Settings.

## Startup Shortcuts for PanelView Plus CE Devices

On PanelView Plus CE devices, FactoryTalk View ME Station software starts based on shortcuts in the Windows startup folder and whether an application is loaded. FactoryTalk View ME Station software can start:

-  without loading or running an .MER application.
-  automatically loading an .MER application.
-  automatically loading and running an .MER application.

Start without Loading or Running .MER Application

To start FactoryTalk View ME runtime software without loading or running a CompactFlash application, do one of the following:

-  Open the FactoryTalk View ME Station icon from the desktop.
-  Select FactoryTalk View ME Station from the Start menu.

Programs&gt;Rockwell Software&gt;FactoryTalk View&gt; FactoryTalk View ME Station

-  Type MERuntime.exe and its path in the Run dialog of the Windows Start menu.

Path to MERuntime.exe

If the path to FactoryTalk View ME runtime contains spaces, you must enclose the path in double quotes.

## Example:

" Storage Card\Rockwell Software\RSViewME\MERuntime.exe "

If you copy the FactoryTalk View ME Station shortcut from the desktop to the Windows Startup folder (\Storage Card\Windows\Startup), FactoryTalk View ME Station software will automatically run on startup.

## Example:

" Storage Card\Rockwell Software\RSViewME\MERuntime.exe " " Storage Card\Rockwell Software\RSViewME\Runtime\MYAPP.MER "

If you place a shortcut to the .MER application into the Windows Startup (\Storage Card\Windows\Startup) folder, the ME Runtime will automatically start and load the .MER application on terminal startup.

If the application specified in the Run dialog or the Startup folder does not exist or is corrupted, the main FactoryTalk View ME Configuration Mode screen will open.

## Start FactoryTalk View ME Station and Run .MER Application

To start FactoryTalk View ME Station software and automatically run an .MER application:

-  in FactoryTalk View Studio software, select Tools&gt;Transfer Utility and select Run application when download completes on the Download tab.
-  type the appropriate shortcut path in the Run dialog on the Windows Start menu.

Path to MERuntime.exe, followed by a space, followed by the path to the .MER, followed by /r

If the path to FactoryTalk View ME runtime or the path to the application contains spaces, you must enclose the path in double quotes.

## Example:

" Storage Card\Rockwell Software\RSViewME\MERuntime.exe " " Storage Card\Rockwell Software\RSViewME\Runtime\MYAPP.MER " /r

If you place a shortcut with the above command line in the Windows Startup folder (\Storage Card\Windows\Startup), the ME Runtime will start and automatically run the .MER application.

If the application specified in the Run dialog or the Startup folder does not exist or is corrupted, the main FactoryTalk View ME Configuration Mode screen will open and display the following message:

Unable to load application

## Start FactoryTalk View ME Station Software and Load .MER Application

To start FactoryTalk View ME Station software and automatically load an .MER application, type the appropriate shortcut path in the Run dialog on the Windows Start menu.

Path to MERuntime.exe, followed by a space, followed by the path to the .MER

If the path to FactoryTalk View ME runtime or the path to the application contains spaces, you must enclose the path in double quotes.

## Example:

" Storage Card\Rockwell Software\RSViewME\MERuntime.exe " " Storage Card\Rockwell Software\RSViewME\Runtime\MYAPP.MER " /r/d

-  To run the .MER application and replace the terminal's communication configuration with that of the applications without deleting its log files, use the following path:

Path to MERuntime.exe, followed by a space, followed by the path to the .MER, followed by /r/o

## Example:

" Storage Card\Rockwell\Software\RSViewME\MERuntime.exe " " Storage Card\Rockwell\Software\RSViewME\Runtime\MYAPP.MER " /r/o

-  To run the .MER application, delete its log files, and replace the terminal's communication configuration with that of the applications, use the following path:

Path to MERuntime.exe, followed by a space, followed by the path to the .MER, followed by /r/d/o

## Example:

" Storage Card\Rockwell\Software\RSViewME\MERuntime.exe " " Storage Card\Rockwell\Software\RSViewME\Runtime\MYAPP.MER " /r/d/o

Other Shortcut Paths for FactoryTalk View ME Station Software

## IMPORTANT

If the path to FactoryTalk View ME software or the path to the application contains spaces, you must enclose the path in double quotes.

-  To run the .MER application and delete its log files without replacing the terminal's communication configuration with that of the applications, use the following path:

Path to MERuntime.exe, followed by a space, followed by the path to the .MER, followed by /r/d.

## Configure Startup Tests

The terminal can run extended tests on startup. You can select which test to run and also specify test settings on startup.

## Select Tests to Run on Startup

Follows these steps to select which tests you want to run on startup.

1. Select Terminal Settings&gt;Startup Options&gt;Startup Tests.

<!-- image -->

The screen shows a list of each test that can be performed on the terminal at startup and its current On/Off status. You can turn any test in the list on or off by selecting the On/Off button. The terminal will run tests only with a checked box.

2. Select the tests you want to run on startup.
2.  Use the up and down cursor buttons to highlight a test.
3.  Press the On/Off button to select a test. A checked box means the test is selected to run. Press the button again to clear the check box.
3. Press OK.

## Configure Startup Test Settings

Follow these steps to specify how many times to run the selected tests on startup and to enable extended diagnostics.

## IMPORTANT

Enabling extended diagnostics and setting a high repeat count will increase the time it takes the terminal to reboot.

The tests will run each time you reset or cycle power to the terminal until you disable extended diagnostics. Setting a low repeat count will also decrease the startup time.

1. Select Terminal Settings&gt;Startup Options&gt;Startup Test Settings.
2. Press the Repeat Count button to specify the number of times, 0… 128, to run the selected tests on startup.
3. Press the Enable Extended Diagnostics button to enable or disable extended diagnostics on startup.
4.  Select Yes to enable extended diagnostics.
5.  Select No to disable extended diagnostics.
4. Press OK.

<!-- image -->

## View and Clear the System Event Log

The System Event Log screen displays a list of system events logged by the terminal.

1. Select Terminal Settings&gt;System Event Log.
2. Select an event and then press the More Details button to display system event log details for that event.
3. Press the Clear All button to clear all system event logs.
4. Press OK.

<!-- image -->

## Display Terminal Information

You can view these details for your terminal:

-  Total power on time
-  Processor temperature
-  Battery voltage and battery state
-  Amount of memory on terminal

Follow these steps to display terminal information.

1. Select Terminal Settings&gt;System&gt;Information&gt;Terminal Information.

<!-- image -->

All fields are read-only except for memory allocation.

|         | Battery State PanelView Plus 400 and 600 Terminals PanelView Plus 700 to 1500 Terminals   |                                                      |
|---------|-------------------------------------------------------------------------------------------|------------------------------------------------------|
|         |                                                                                           | Good Good battery condition. Good battery condition. |
| Failing | Does not have a replaceable battery. Replace the terminal.                                | Low battery. Replace the battery.                    |
| Bad     | Does not apply.                                                                           | Battery is missing or bad. Replace the battery.      |

IMPORTANT

For the 400 and 600 terminals, the Battery Voltage indicates the battery state only and the Processor Temperature shows the temperature of the display.

2. Press the Memory Allocation button to view or adjust the:
2.  amount of allocated storage or program memory.
3.  amount of storage or program memory in use.
3. Press the Up or Down button to increase or decrease the allocation of storage or program memory.

<!-- image -->

Each button press changes the allocation by a value of four. If you change the allocation for one type of memory, the other is updated accordingly.

## IMPORTANT

These settings are not retained after a power cycle. The settings return to the defaults.

4. Press OK to return to previous screen.
5. Press OK to return to terminal settings.

## Display FactoryTalk View ME Station Information

You can display the firmware number of FactoryTalk View ME Station software and the Rockwell Automation technical support number.

1. Select Terminal Settings&gt;System&gt;Information&gt;About FactoryTalk View ME Station.
2. Press the Technical Support button, if desired.
3. Press Close.

<!-- image -->

## Modify the Date, Time, or Time Zone

You can adjust the date and time for terminal operations, or change the time zone.

## Change the Date

1. Select Terminal Settings&gt;Time/Date/Regional Settings&gt;Date. The current date appears in the Year, Month, and Day fields.
2. Press the Year, Month, and Day buttons to change the values.
3. Press OK when done.

<!-- image -->

| Field   | Description                                                            | Valid Values   |
|---------|------------------------------------------------------------------------|----------------|
| Year    | The current year in a four-digit format.                               | 1980…2099      |
|         | Month The current month.                                               | 1…12           |
| Day     | The current day. The day of the month is validated based on the month. | 0…31           |

## Change the Time

1. Select Terminal Settings&gt;Time/Date/Regional Settings&gt;Time.

The current time appears in 24-hour format in separate Hour, Minute, and Second fields.

<!-- image -->

2. Press the Hour, Minute, and Seconds buttons to change the values.
3. Press OK when done.

| Field   | Description                                   | Valid Values   |
|---------|-----------------------------------------------|----------------|
| Hour    | The current hour in 24-hour format.           | 0…23           |
|         | Minute The current minute in 24-hour format.  | 0…59           |
|         | Seconds The current second in 24-hour format. | 0…59           |

## Change the Time Zone

You can view or modify the current time zone that is installed on the terminal. Time zones are installed as a part of the operating system. Changing the time zone adjusts the current time and date to match the new time zone.

1. Select Terminal Settings&gt;Time/Date/Regional Settings&gt;Time Zone.
2. Press the up and down cursor buttons to select a time zone.

<!-- image -->

|          | Language Default Time Zone                                    |
|----------|---------------------------------------------------------------|
| English  | (GMT -05:00) Eastern Time (US and Canada)                     |
| French   | (GMT +01:00) Brussels, Copenhagen, Madrid, Paris              |
| German   | (GMT +01:00) Amsterdam, Berlin, Bern, Rome, Stockholm, Vienna |
| Japanese | (GMT +09:00) Osaka, Sapporo, Tokyo                            |

If the selected time zone supports Daylight Savings, you can press the Daylight Savings button.

3. Press the Daylight Savings button to enable or disable daylight savings for the selected time zone.

Daylight Savings is set to Yes for all time zones except for Japanese, which does not support daylight savings. Daylight savings changes are not permanently applied until you close the Time Zone screen.

4. Press the Use Daylight Savings Button to select Yes or No.
5. Click OK when done.

<!-- image -->

## Modify Regional Settings

6. Click OK to return to Terminal Settings.

You can adjust regional settings for a specific language installed on the terminal, including the date, time and numeric formats.

To access regional settings, select Terminal Settings&gt;Time/Date/Regional Settings&gt;Regional Settings.

The current language is shown at the bottom of the Regional Settings screen.

## Select a Language

You can select a language that is installed on the terminal. Languages are installed as a part of the operating system.

1. Select Terminal Settings&gt;Time/Date/Regional Settings&gt;Regional Settings&gt;Language.
2. Select a language by pressing the up and down cursor keys.
3. Press OK.

<!-- image -->

The selected language will appear at the bottom of the Regional Settings screen.

## Change the Decimal Separator for Numeric Formats

You can change the decimal separator used in numerics for the current language. The default decimal separator is a period.

1. Select Terminal Settings&gt;Time/Date/Regional Settings&gt;Regional Settings&gt;Numeric Format.

<!-- image -->

The field shows the default decimal separator. The field will accept a separator up to three characters.

2. Enter up to three characters for the new separator.
3. Click OK.

## Change the Time Format

You can change the time format for the selected language.

1. Select Terminal Settings&gt;Time/Date/Regional Settings&gt;Regional Settings&gt;Time Format.

<!-- image -->

The current time is shown using the currently selected format.

2. Press the appropriate buttons to adjust the formats.
3. Click OK.

| Field Description                                                                                                          | Example                                |
|----------------------------------------------------------------------------------------------------------------------------|----------------------------------------|
| h:mm:ss tt (default) h = hour, no leading zero tt = AM or PM symbol                                                        | 7:23:02 AM or 1:13:31 PM 11:43:59 AM   |
| hh:mm:ss tt hh = hour with leading zero tt = AM or PM symbol                                                               | 07:23:02 AM or 01:13:31 PM 11:43:59 PM |
| H:mm:ss H = hour in 24-hour format, no leading zero                                                                        | 7:03:42 or 1:13:32 23:43:59            |
| HH:mm:ss HH = hour in 24-hour format with leading zero                                                                     | 07:03:42 or 01:13:22 23:43:59          |
| AM Symbol Characters to indicate AM. If the time format is set to h:mm:ss tt or hh:mm:ss tt, you can modify the AM symbol. | AM (default) 12 character max          |
| PM Symbol Characters to indicate PM. If the time format is set to h:mm:ss tt or hh:mm:ss tt, you can modify the PM symbol. | PM (default) 12 character max          |
| Separator Characters that separate fields in time format. : (default)                                                      | 3 character max                        |

## Change the Short Date Format

You can change the short date format for the selected language.

1. Select Terminal Settings&gt;Time/Date/Regional Settings&gt;Regional Settings&gt;Short Date Format.

<!-- image -->

The current date is shown in the selected, short date format.

| Field Short Date Formats                                                                                                        | Example                                                           |
|---------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------|
| Format M/d/yyyy (default) M/d/yy MM/dd/yy MM/dd/yyyy yy/MM/dd yyyy-MM-dd dd-MMM-yy                                              | 1/2/2003 1/2/03 01/02/03 01/02/2003 03/01/02 2003-01-02 02-Jan-03 |
| Separator Character separator for fields in time format. The default separator is either - or / depending on short date format. | - or / (default) 3 character max                                  |

2. Press the Format button to select an available format.
3. Press the Separator button to change the field separator for the date elements.
4. Click OK when done.

## Change the Long Date Format

You can change the long date format used by the selected language.

1. Select Terminal Settings&gt;Time/Date/Regional Settings&gt;Regional Settings&gt;Long Date Format.

<!-- image -->

The current date is shown in the selected long date format.

2. Press the Long Date Format button to select a date format.
3. Click OK when done.

<!-- image -->

| Long Date Formats                                                                                                                                    | Example                  |
|------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------|
| dddd, MMMM, dd, yyyy (default) dddd is name of week day MMMM is name of month dd is two-digit day of month with leading zero yyyy is four-digit year | Monday, January 01, 2003 |
| MMMM dd, yyyy MMMM is name of month dd is two-digit day of month with leading zero yyyy is four-digit year                                           | January 01, 2003         |
| dddd, dd MMMM, yyyy dddd is name of week day dd is two-digit day of month with leading zero MMMM is name of month yyyy is four-digit year            | Monday, 01 January, 2003 |
| dd MMMM, yyyy dd is two-digit day of month with leading zero MMMM is name of month yyyy is four-digit year                                           | 01 January, 2003         |

## Chapter Objectives

## Windows CE .NET Architecture

## Windows CE .NET Operating System

This chapter applies only to PanelView Plus CE terminals and provides information on these topics:

-  Windows CE .NET architecture
-  Windows CE .NET programs for PanelView Plus CE terminals
-  Using Windows CE .NET operating system
-  PanelView Plus CE terminal memory
-  Control panel applications for configuring PanelView Plus CE terminals

The Windows CE .NET operating system from Microsoft provides a portable, scalable, real-time operating system for embedded devices. The modular design of Windows CE .NET allows the platform builder to include only those features required for the specific product application. However, the Windows CE .NET operating system is still a subset of the other Microsoft operating systems, and it runs Win32 applications.

## Windows CE .NET Benefits

There are three major differences between the Windows CE .NET operating system and other Microsoft Windows operating systems. The Windows CE .NET operating system:

-  has a small memory footprint requirement.
-  runs on a wide variety of processor architectures.
-  has a real-time scheduler.

The small memory footprint allows the Windows CE .NET operating system to operate in small solid-state memory devices (8 MB typical). In contrast, computers that run Windows operating systems require hundreds of megabytes of storage space.

The PanelView Plus CE terminal has an x86-based processor to maximize the consistency between Windows 2000/XP and Windows CE .NET applications.

## Windows CE .NET Programs

## Compile Windows CE .NET Applications

While the Windows CE .NET operating system brings a higher level of standardization to embedded computing devices, third-party software applications must still be compiled and tested to run on each Windows CE .NET device. The compilation is required to tailor the software application to the device's processor and unique hardware features.

Microsoft created hardware reference models for the handheld (HPC) and the pocket (PPC) personal computer so that third-party applications can run on these standard platforms. There are no hardware standards for embedded devices.

The PanelView Plus CE terminal is largely compatible with HPC and PPC, so applications that are compiled for the x86 may run on the PanelView Plus CE terminal.

The PanelView Plus CE terminal includes FactoryTalk View ME software. Refer to the user manual and online help shipped with FactoryTalk View Studio software for information about using this software.

The Windows CE .NET operating system and applications are stored on the internal CompactFlash of the PanelView Plus CE terminal for permanent storage and can be accessed as the \Storage Card directory in the Windows Explorer. (They are also available on the PanelView Plus CE Accessory CD). The operating system and FactoryTalk View ME software are loaded into RAM at startup to improve response time.

Additional programs can be installed by using ActiveSync or an external CompactFlash card on the PanelView Plus CE terminal.

The PanelView Plus CE terminal ships with the following programs preloaded.

| Application                                          | Description                                                                                                            |
|------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|
| Microsoft Internet Explorer, version 5.5 Web browser |                                                                                                                        |
| ActiveSync Support                                   | Connects the PanelView Plus CE terminal to a desktop computer running ActiveSync software                              |
| Control Panel                                        | Set of configuration tools for setting up the PanelView Plus CE terminal                                               |
| Windows Explorer (Shell)                             | User interface to the system much like a desktop computer                                                              |
| Remote Desktop Connection                            | Services for thin client applications included on the PanelView Plus CE Accessory CD (formerly Terminal Server Client) |
| WordPad                                              | Text editor                                                                                                            |
| PDF Viewer                                           | Reader for Adobe Acrobat PDF files                                                                                     |

## Windows CE .NET Operating System

Other Windows CE .NET programs are available.

Most of these programs have been written for PPC devices, and some may run on the PanelView Plus CE terminals . For more information on Windows CE .NET programs, see the Knowledgebase at http://support.automation.rockwell.com .

## Install Applications

The PanelView Plus CE terminal allows field-installation of third-party software.

Refer to Chapter 8 for details on how to use Microsoft ActiveSync software to install and remove application programs on the PanelView Plus CE terminal. Each application program must be compiled for the x86 processor.

If the application program literature does not specifically identify the PanelView Plus CE terminal as a compatible hardware platform, take caution if trying to install and run it on the terminal. While the program may operate on the X86 processor, there could be conflicts with running it on the PanelView Plus CE terminal. Testing is essential.

The Windows CE .NET operating system provides a user interface similar to other Microsoft Windows operating systems. This user interface has been simplified to reduce the memory footprint. Therefore, minor differences exist between the desktop Windows interface and the Windows CE .NET interface.

The Windows CE .NET graphical interface simplifies interaction with the computer. You simply select and move objects on the screen by tapping and dragging them using your finger or stylus on the touch screen, or using an external mouse.

<!-- image -->

If you have difficulty selecting objects using the touch screen, run the calibration program.

The PanelView Plus CE terminal has a keypad, touch screen, or input panel for operator input. In addition, an external keyboard or mouse can be connected to one of the USB ports of the terminal.

You may find it convenient to use the following shortcuts. These shortcuts work with the PanelView Plus CE terminal keypad, an attached keyboard, or the input panel.

## Keyboard Shortcuts

| Shortcut       | Description                                                                                |
|----------------|--------------------------------------------------------------------------------------------|
| Ctrl+Esc       | Opens the Windows CE .NET Start menu. Use arrow keys to select a program and Enter to run. |
| Alt+Tab        | Starts the Task Manager.                                                                   |
| Enter          | This key is equivalent to double-tap. In a dialog, you can select Enter or OK.             |
| Shift + Tab or | Selects the previous control in a dialog.                                                  |
| Tab or         | Selects the next control in a dialog.                                                      |
| Ctrl+Tab       | Opens the next tab in a tabbed dialog.                                                     |
| Esc            | Closes a dialog without saving changes.                                                    |
| Arrow keys     | Selects controls or items from a list in a dialog.                                         |
| Alt            | Activates menus.                                                                           |

## Start Menu and Taskbar

Use the Start menu to run programs, configure settings, and open recently-used documents. A single-click on the Start menu button on the bottom left of the screen brings up the menu. Subsequent clicks select the program or item you want to open. The key sequence Ctrl+Esc also activates the Start menu.

The taskbar across the bottom of the screen contains buttons for programs already running, along with a status area and a Desktop icon. You can alternately minimize and maximize an open application by clicking on its taskbar button. Double-clicking on any icon in the status area shows more information about that function. A single-click on the Show Desktop button (far right side of taskbar) minimizes all open windows and displays the PanelView Plus CE computer desktop. You can close an application by clicking with the right mouse button on its taskbar button and choosing Close.

<!-- image -->

## Command Bar

A Windows CE.NET program has a command bar located across its top. This command bar contains pull-down menu names and toolbar buttons for the application.

Click on a menu name or toolbar icon to interact with the specific program. The Help (?) button on the right side of the command bar provides application-specific help. The Exit (X) button on the far right side of the command bar exits the application.

Windows CE .NET command bar does not have a Minimize button. Click the taskbar button to minimize a program window, or use the Show Desktop button to minimize all open program windows.

## Find Files

Select Start&gt;Programs&gt;Windows Explorer to locate files on the PanelView Plus CE terminal . You can alternately double-click the My Computer icon on the Desktop to open the Windows Explorer program. The Windows Explorer web browser lets you browse and manipulate the PanelView Plus CE files and folders. The Edit menu lets you move files from one location to another by using the

Copy or Cut and Paste commands. When you create and save a new file, it is stored in the My Documents folder unless you specify another location.

## TIP

The PanelView Plus CE file system resides in RAM and flash memory. RAM is volatile and is not persistent after a power cycle. Save files that must be persistent to the\Storage Card Folder that resides on the internal CompactFlash card.

## Browse Web Pages

Select Start&gt;Programs&gt;Internet Explorer to view Web pages. You can alternately double-click the Internet Explorer icon on the desktop to open the Internet Explorer program. To access pages stored on the PanelView Plus CE terminal, use the File&gt;Open command and select the Browse button to locate the file. To view Internet or intranet pages, type a URL in the Address box.

Before you can access remote Web pages, the PanelView Plus CE terminal must be connected to a network. See the section on Network and Dialup Connections for details on configuring the Ethernet interface. Additional network settings such as a Proxy Server can be configured in the Internet Explorer application by using the Options command under the View menu.

The Microsoft Internet Explorer application is similar to the personal computer version. It offers many of the same features of the personal computer version, and can be used to view most Internet HTML Web pages. Some advanced Web features may not be fully supported.

## Print

Some PanelView Plus CE software applications may support printing. To print from these applications, select the File&gt;Print command. A PCL compatible printer must be connected to the USB or Ethernet port on the PanelView Plus CE terminal.

## PanelView Plus CE Memory

The PanelView Plus CE has the following memory areas:

-  Boot ROM
-  Internal CompactFlash
-  Dynamic RAM
-  External CompactFlash cards
-  USB mass storage devices

## Boot ROM

The boot ROM is used to start up the PanelView Plus CE terminal, perform power on self tests, and load the Windows CE .NET operating system into dynamic RAM. The boot ROM code is not user accessible.

## Internal CompactFlash

The internal CompactFlash is the main storage memory in the PanelView Plus CE terminal. The Windows CE .NET operating system and user applications are stored in flash memory. On startup, the operating system and any auto-start applications are transferred to dynamic RAM, where they are executed.

The remainder of the flash memory is a FAT partition that appears as a folder named \Storage Card in Windows CE .NET. Files stored here are persistent (saved even after a reset or power cycle).

<!-- image -->

Only programs and files loaded in the \Storage Card folder are permanently saved to flash memory. All other folders or files existing in RAM are lost when power is cycled.

## Dynamic RAM

The RAM memory is split into two segments: Storage and Program memory. The System application in the Control Panel has a slider control that determines the allocation mix between Storage and Program memory.

The Storage memory segment is a virtual RAM disk known as the Object Store. It provides specialized storage for the Windows CE .NET Registry, the file system, and system databases. The RAM-based Storage memory segment is not persistent as in HPC devices, so all files stored here must be recreated at every startup.

The Program memory segment provides traditional computer RAM-like functions for holding application code, heaps, stacks, and data at runtime. The PanelView Plus CE terminal loads the Windows CE .NET operating system and any auto-start applications from flash memory into the Program memory at powerup.

## External CompactFlash Cards

External CompactFlash cards are available for the PanelView Plus CE terminal to increase the space for storing files. When a CompactFlash card is installed in the card slot of the PanelView Plus CE terminal, a StorageCard2 icon is displayed under My Computer, and files on the memory card can be manipulated by using the Windows Explorer program.

The card slot on the PanelView Plus CE terminal supports Type 1 CompactFlash cards. The cards (2711P-RCx) are available in different sizes.

For details on how to install/remove cards from the card slot, refer to page 162 .

## USB Mass Storage Devices

USB devices that comply with the USB Mass Storage Class Specification, version 1.0, are supported to enable a wide variety of USB-based storage devices such as hard drives, floppy disks, CD-ROM drives and ATA flash readers. Up to 10 devices are supported, concurrently. DVD drives are not supported.

## Control Panel Applications

The PanelView Plus CE terminal has user-configurable settings that are accessed from the Windows CE .NET Control Panel applications. These applications are similar to other Microsoft Windows operating systems. Select Start&gt;Settings&gt;Control Panel to open the Control Panel window.

<!-- image -->

| Application       | Description                                                                                                                                             |   See page |
|-------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|------------|
| Certificates      | Manages digital certificates used by some applications for establishing trust and secure communications.                                                |        137 |
| Date/Time         | Sets the date and time on the terminal.                                                                                                                 |        135 |
| Dialing           | Configures dialing rules for telephone and modem communications.                                                                                        |        121 |
| Display           | Configures the display and color settings, the brightness of the backlight, and the screen saver.                                                       |        128 |
|                   | Extended Diagnostics Enables tests to run on the terminal at each startup and the number of times to run each test.                                     |        130 |
| Hardware Monitor  | Views the current voltage and temperature, and system events logged on the terminal.                                                                    |        132 |
| Input Panel       | Configures an input panel for entering/editing data on a touch screen terminal.                                                                         |        127 |
| Internet Options  | Configures start and search pages, clears cache and history, and specifies connection and security settings for Internet Explorer web browser.          |        137 |
| Keyboard          | Configures settings for an attached keyboard.                                                                                                           |        125 |
| Keypad            | Configures settings for keys on the PanelView Plus CE terminal.                                                                                         |        126 |
| Mouse             | Sets the sensitivity of the mouse, if attached.                                                                                                         |        127 |
|                   | Network and Dial-up Connection Configures ActiveSync and Ethernet network connections between your terminal and a computer.                             |        121 |
| Owner             | Configures network and user identification information for your terminal.                                                                               |        120 |
| Password          | Sets a password to protect your terminal against unauthorized use. The password can be enabled at system startup or when the screen saver is activated. |        121 |
| PC Connection     | Selects a configured connection for connecting your PanelView Plus CE terminal to another computer.                                                     |        122 |
| Power             | Provides information on the battery condition of the terminal and other power management features.                                                      |        132 |
| Regional Settings | Sets the clock, date and language, and configures formats for numbers, currency, time, date, and regional settings.                                     |        135 |
| Remove Programs   | Removes programs installed on your terminal.                                                                                                            |        138 |

| Application     | Description                                                                                                           |   See page |
|-----------------|-----------------------------------------------------------------------------------------------------------------------|------------|
| Storage Manager | Displays information on terminal’s hard drive. Also reformats and manages partitions for hard drive.                  |        138 |
| System          | Lists system properties like memory allocation, device information, operating system version.                         |        133 |
| Touch           | Calibrates the touch screen, sets the sensitivity of touch screen taps, and enables/disables the touch screen cursor. |        124 |

## Owner

The Owner dialog provides network and user identification information for your PanelView Plus CE terminal.

## Network ID

The Network ID tab identifies the PanelView Plus CE terminal to a network so it can gain access to network resources. A username, password, and domain may be necessary; if so, contact your system administrator. When done, click OK.

<!-- image -->

## Identification and Notes

The Identification tab defines optional user information for your PanelView Plus CE terminal. Use the Notes tab if it is necessary to document additional information.

<!-- image -->

## Password

The Password dialog lets you define a password to protect your terminal against unauthorized use. You can require that the defined password be entered each time the terminal is restarted and/or when the screen saver is activated. Select OK to activate settings.

<!-- image -->

## Dialing

The Dialing dialog is a standard Windows control-panel application that configures dialing rules for modem communication.

<!-- image -->

## Network and Dial-up Connections

The Network and Dial-up Connections application lets you configure:

-  ActiveSync connection between your PanelView Plus CE terminal and another computer.
-  Ethernet network connection.

## ActiveSync Connection

For details on establishing an ActiveSync connection between your PanelView Plus CE terminal and a computer, see Chapter 8 .

Serial Connect is the default, pre-configured ActiveSync connection.

## Configure Ethernet Connection

Follow these steps to configure an Ethernet network connection.

1. Select the Network and Dial-up Connections application.

2. Click the PCI-E100CE1 icon to configure Ethernet settings.
3. On the IP address tab, select Obtain an IP address via DHCP or Specify an IP Address
3.  IP addresses may be automatically assigned if DHCP is enabled for the Ethernet adapter.
4.  If you select Specify an IP Address, complete the three text boxes with information from your network administrator.
4. Click OK in the title bar.

<!-- image -->

<!-- image -->

A dialog will prompt you to either remove and reinstall your card or restart the device for the new settings to take effect. Click OK in the notification dialog.

5. For the built-in Ethernet Controller, you must restart the terminal.
6. Click OK to close the Network Configuration dialog.

TIP

If DHCP is enabled for the adapter, Name Server addresses may be automatically assigned. You can specify additional WINS or DNS addresses on the Name Servers tab.

## PC Connection

The PC Connection dialog lets you select and enable a configured connection between your PanelView Plus CE terminal and another computer. The current connection is listed at the bottom of the tab. To change the connection to

another computer, click Change. A dialog will open letting you select another configured computer. Click OK when done to activate change.

<!-- image -->

<!-- image -->

Adjusting the PC connection named Serial\_Connect may result in an inability to connect with your desktop computer via ActiveSync software.

## Touch

The Touch Properties dialog lets you perform the following operations for PanelView Plus CE touch screen terminals:

-  Set double-tap sensitivity
-  Calibrate the touch screen

When done performing operations, remember to click OK in the title bar to activate settings.

Double-tap Sensitivity

The Double-tap tab sets the sensitivity for both the speed and physical distance between screen taps. Double-tap the top grid to set the sensitivity. Double-tap the bottom grid to test the setting.

<!-- image -->

## Calibration

The Calibration tab provides instructions on how to calibrate the touch screen. You may have to do this if the terminal is not responding to your taps. Click Recalibrate. Touch the center of the target as it moves around the screen. When the target returns to its initial position, the calibration is complete.

<!-- image -->

## Keyboard

The Keyboard dialog configures key settings for a keyboard that is attached to the USB port of the PanelView Plus CE terminal. You can adjust the:

-  rate for repeating a key press.
-  delay from the first key press to when repeating begins.

To adjust key repeat settings, check the Enable character repeat checkbox. Adjust how often a key repeats by moving the slider between Slow and Fast. To adjust the delay between key repeats, move the slider between Long and Short. Tap the field at the bottom of the dialog and then hold down a key to test the new settings.

When done performing operations, remember to click OK in the title bar to activate settings.

<!-- image -->

## Keypad

Use the Keypad dialog to:

-  configure key settings for keys on the PanelView Plus CE terminal.
-  adjust the rate for repeating a key press and the delay from the first key press to when repeating begins
-  enable/disable multi-key lockout.

When done performing operations, remember to click OK in the title bar to activate settings.

## Key Repeat

To adjust repeat settings for keys on an attached keyboard, check the Enable character repeat checkbox. Then adjust how often a key repeats by moving the slider between Slow and Fast. To adjust the delay between key repeats, move the slider between Long and Short. Tap the field at the bottom of the dialog and then hold down a key to test the new settings.

Multi-Key/Hold-Off Lockout

<!-- image -->

The Multi-Key/Hold-Off tab restricts multiple or simultaneous key presses on the PanelView Plus CE terminal and specifies a hold-off delay between presses of the same key.

<!-- image -->

## Multi-Key Lockout

Under Multi-Key Lockout, select one of the following options:

-  Enabled - any programmable key that is pressed inhibits all keys until the programmable key is pressed again. This includes the Alt, Ctrl, and Shift keys.
-  Enabled with Abort - any secondary key press will terminate the initial key press immediately.
-  Disable - places no restrictions on key presses. Clear both checkboxes.

## IMPORTANT

The keypad cannot produce Home, End, Page Up, or Page Down when Multi-Key Lockout is enabled.

## Hold-Off Delay

If enabled, this option will ignore multiple presses of the same key for a specified length of time. To enable this option, select the Enable Hold-Off mode checkbox. Then adjust the delay time by moving the slider to the left or right to increase or decrease the hold off time.

## Mouse

If a mouse is attached to one of the USB ports of the PanelView Plus CE terminal, you can set the sensitivity for both the speed and physical distance between mouse taps. Double-tap the top grid to set the sensitivity. Double-tap the bottom grid to test the setting. Click OK.

<!-- image -->

## Input Panel

The Input Panel dialog sets properties for the soft Keyboard input panel. Use the Options button to select Large or Small keys, and other soft key options. Click OK after making any changes.

<!-- image -->

## Display

The Display dialog set the following display properties for the PanelView Plus CE terminal.

-  Background
-  Appearance
-  Backlight
-  Screen saver
-  Cursor

When done performing operations, remember to click OK in the title bar to activate settings.

## Background

The Background tab lets you select an image to use for the PanelView Plus CE desktop and whether the image should be tiled.

<!-- image -->

## Appearance

The Appearance tab let you change the color scheme of your desktop.

<!-- image -->

## Backlight

The Backlight tab adjusts the brightness of the terminal's backlight. To adjust the brightness of the terminal's backlight, move the slider to the left or right. To use the adjusted brightness when the terminal starts up, select the Use Brightness during startup checkbox.

<!-- image -->

## Screen Saver

The Screen Saver tab enables and disables the screen saver. To enable the screen saver, check the checkbox and then select an idle time. This will activate the screen saver after the terminal has been idle for the specified time. You can also select a screen saver image. To adjust the brightness of the screen saver, move the slider to the left or right.

<!-- image -->

To add a custom image for the screen saver, copy the bitmap (.bmp file) to the \Storage Card folder and then use the Browse button to select the image. You can disable the screen saver bitmap by selecting (None) from the Image pull-down list.

## Cursor

Use the Cursor tab to enable or disable the visible screen cursor.

<!-- image -->

## Extended Diagnostics

From the Extended Diagnostics dialog, you can:

-  enable/disable extended diagnostics to run on the PanelView Plus CE terminal at each reset or power cycle.
-  select specific tests to run.
-  specify the number of times to repeat each test.

When done performing operations, remember to select OK in the title bar to activate settings.

## Iteration Count

From the Iteration tab, check the Enable Extended Diagnostic checkbox to run selected tests on the PanelView Plus CE terminal at each reset or startup. You can also specify how many times to run each test. The tests are selected from the Tests and More Tests tab.

The selected tests will run each time the PanelView Plus CE terminal is reset until disabled (by unchecking the Enable Extended Diagnostics checkbox).

<!-- image -->

<!-- image -->

Enabling Extended Diagnostics and setting a high Iteration count will increase the time it takes for the terminal to start up.

The tests will run each time you reset or cycle power to the terminal until you disable Extended Diagnostics. Setting a low iteration count will also decrease the start up time.

## Tests

The Tests and More Tests tabs show a list of tests that can be performed on the PanelView Plus CE terminal at startup and the on/off status of each test. The terminal will run only the test with checked boxes. To enable a test, check the checkbox; to disable a test, uncheck the checkbox. Click Clear All if you want to clear all checkboxes.

<!-- image -->

## Hardware Monitor

Use the Hardware Monitor dialog to:

-  view the current battery voltage state and temperature of the display and processor.
-  view and clear all recorded events.

When done performing operations, remember to click OK in the title bar to activate settings.

## Voltages and Temperature

The Voltages and Temp tab shows both the nominal and actual voltage of the battery in the PanelView Plus CE terminal and its current status. The current temperature of the display and the processor is also shown along with its status.

<!-- image -->

## Event Log

The Event Log shows a list of all events that have occurred in the system. Select the Clear Events button to clear all events from the list.

<!-- image -->

## Power

The Battery tab on the Power dialog shows the status of the internal battery in the terminal. Replace the battery in the terminal, when the Battery State is Low or Very Low. For the PanelView Plus CE terminal, you can ignore the other tabs.

<!-- image -->

## System

The System dialog provides system, device, and copyright information for the PanelView Plus CE terminals. It also provides memory allocations for storage and programs. If you make memory adjustments, remember to click OK to activate settings.

## General

The General tab displays system operating and computer information.

<!-- image -->

## Memory

The Memory tab displays the amount of memory allocated and in use for storage and programs. These settings are controlled by the system at startup and can be adjusted by an application program. Normally, it is not necessary to the change the setting unless a program reports a need for more memory. Move the slider to the left to increase the allocation for program memory. The memory allocations are automatically adjusted as you move the slider.

<!-- image -->

## Device Name

The Device Name tab defines a name and description for your PanelView Plus CE terminal. This information identifies your CE terminal to other computers on the Ethernet network. The name must be unique on the network. You must change the name from the initial default the terminal was shipped if more than one PanelView Plus CE terminal is present on your Ethernet network.

The device name must include:

-  1…15 characters.
-  a leading alpha character in the range a through z or A through Z.
-  remaining characters in the range a through z, A through Z, 0 …9 or - (hyphen).

The device description is optional but useful if you want to further describe a specific terminal.

<!-- image -->

## Copyrights

The Copyright tab provides copyright information for your PanelView Plus CE terminal.

<!-- image -->

## Date/Time

The Date/Time dialog sets the current date and time for the selected time zone. Changing the time zone will adjust the date and time accordingly. Check the checkbox if Daylight Savings is in effect for the current time zone.

The time appears according to the format set in the Regional Settings dialog. After making adjustments, click Apply and then OK.

<!-- image -->

## Regional Settings

Use the tabs on the Regional Settings dialog to select a language and then set the format for how the time, date, and numbers appear for the selected language.

When done performing operations, remember to click OK in the title bar to activate settings.

## Language

The Language tab selects a language that is installed on the PanelView Plus CE terminal. Languages are installed as a part of the operating system.

<!-- image -->

## Time

The Time tab configures the time format for the selected language. A sample of the current time format is shown. This sample changes as you make adjustments. You can adjust the time format, the separator between the time fields, and the AM/PM symbol.

<!-- image -->

## Date

The Date tab configures the style of the short date format and the long date format for the selected language. A sample of the current formats is shown. These samples are updated as you make changes.

<!-- image -->

## Number

The Number tab configures how negative and positive numbers will appear for the selected language. The appearance of the current formats is shown for both positive and negative numbers. These samples are updated as you make changes.

<!-- image -->

## Internet Options

The Internet Setting dialog provides tabs to configure parameters for accessing and using the Internet on your PanelView Plus CE device.

<!-- image -->

## Certificates

The Certificates dialog manages digital certificates used by some applications for establishing trust and secure communications. Certificates are signed and issued by certificate authorities and are valid for a prescribed period of time.

<!-- image -->

## Remove Programs

Use the Remove Programs dialog to remove installed programs from your terminal. The dialog shows a list of programs that can be removed. Select a program from the list, click Remove, and then OK.

<!-- image -->

## Storage Manager

Use the Storage Properties dialog to display information about the internal CompactFlash card and other storage devices such as the external CompactFlash card and USB Mass Storage Devices. From this dialog, you can also configure partitions and reformat the device.

<!-- image -->

<!-- image -->

Do not try to alter the internal CompactFlash storage device that is displayed under Storage Info as DSK1: IDE Hard Disk Drive. You may not be able to reboot the terminal if modifying the internal CompactFlash partitions.

## Chapter Objectives

## Required Tools

## Precautions

## Install and Replace Components

This chapter shows how to install, replace, or upgrade various components of the PanelView Plus terminals.

-  Logic module
-  RAM and internal CompactFlash
-  Communication module
-  Display module
-  Battery
-  Display module bezel
-  Backlight
-  Product ID label
-  Keypad legend inserts
-  External CompactFlash card

These tools are required to install and replace components:

-  #00, #1, and #2 Phillips screwdriver
-  Electrostatic Discharge (ESD) wristband

Before installing or replacing any components, disconnect power from the terminal. During installation, take care not to touch any of the exposed electronic components.

## WARNING

<!-- image -->

Disconnect all power from the terminal before installing or replacing any components. Failure to disconnect power may result in electrical shock or damage to the terminal.

## ATTENTION

<!-- image -->

Be careful when touching any of the exposed electronic components to prevent damage from electrostatic discharge (ESD).

Work in a static free environment and wear a properly grounded ESD wristband.

<!-- image -->

## Component Compatibility for PanelView Plus CE Terminals

It is important to match the series of the internal CompactFlash card with the correct series of the logic module and software version. The series of the CompactFlash determines the version of FactoryTalk View ME software and version of the operating system. The logic module is available with or without memory installed.

| Logic Module 6189-RPx, 6189-RPRHx, 6189-RPEHx, x, 2711P-RPx, 2711P-RPx, x, 2711P-RP6x, 2711P-RP7x   | Internal CompactFlash 6189-RW2, -RW3, -RW4 2711P-RW6, -RW7, -RW8   | FactoryTalk View ME & OS Software Version                           |
|-----------------------------------------------------------------------------------------------------|--------------------------------------------------------------------|---------------------------------------------------------------------|
| Series A: 6189-RPxH/A(1)                                                                            |                                                                    | Series B: 6189-RWx/B FactoryTalk View ME 3.0 Windows CE 3.0         |
| Series B: 6189-RPxH/B                                                                               |                                                                    | Series C: 6189-RWx/C FactoryTalk View ME 3.10 Windows CE 4.1        |
| Series B: 6189-RPxH/B Series C: 6189-RPxH/C                                                         | Series D: 6189-RWx/D Series E: 6189-RWx/E                          | FactoryTalk View ME 3.20 Windows CE 4.1                             |
| Series D: 6189-RPxH/D Series E: 6189-RPxHx/E Series F: 2711P-RPxx/F(2)                              | Series F: 6189-RWx/F Series G: 6189-RWx/G Series H: 2711P-RWx/H    | FactoryTalk View ME 4.0 Windows CE 4.1                              |
| Series G: 2711P-RPxxx/G(2) Series H: 2711P-RPxxx/H(2)                                               |                                                                    | Series J: 2711P-RWx/J FactoryTalk View ME 5.0 or 5.1 Windows CE 4.1 |

- (1) When upgrading from FactoryTalk View ME software, version 3.0 to 3.10 or later, the Firmware Upgrade Kit is recommended.

(2) Series F and later logic modules work with PanelView Plus and PanelView Plus CE CompactFlash cards.

## Component Compatibility for PanelView Plus Terminals

It is important that you match the series of the internal CompactFlash card with the correct series of the logic module and software revision. The series of the CompactFlash determines the version of FactoryTalk View ME software. The logic module is available with or without memory installed.

| Logic Module 2711P-RPx, 2711P-RP1x, x, 2711P-RP2x, 2711P-RP3x                                     | Internal CompactFlash 2711P-RW1, -RW2, -RW3                       | FactoryTalk View ME Software Version           |
|---------------------------------------------------------------------------------------------------|-------------------------------------------------------------------|------------------------------------------------|
| Series A: 2711P-RPx/A(1)                                                                          |                                                                   | Series B: 2711P-RWx/B FactoryTalk View ME 3.0  |
| Series B: 2711P-RPx/B                                                                             |                                                                   | Series C: 2711P-RWx/C FactoryTalk View ME 3.10 |
| Series B: 2711P-RPx/B Series C: 2711P-RPx/C                                                       | Series D: 2711P-RWx/D Series E: 2711P-RWx/E                       | FactoryTalk View ME 3.20                       |
| Series D: 2711P-RPx/D Series E: 2711P-RPxx/E Series F: 2711P-RPxx/F(2) Series G: 2711P-RPxxx/G(2) | Series F: 2711P-RWx/F Series G: 2711P-RWx/G Series H: 2711P-RWx/H | FactoryTalk View ME 4.0                        |
| Series H: 2711P-RPxxx/H(2)                                                                        | Series J: 2711P-RWx/J FactoryTalk View ME 5.0                     | or 5.1                                         |

## Install RAM or Internal CompactFlash

## Compatibility After Upgrade

FactoryTalk View ME terminals are compatible with .MER applications that are the same or a previous version. For example, FactoryTalk View ME 3.20 terminals can run .MER applications for FactoryTalk View ME software, versions 3.0, 3.10, and 3.20.

For PanelView Plus CE devices, the appropriate changes are made to the OS, from Windows CE software, version 3.0 to 4.1, when upgrading from FactoryTalk View ME software, version 3.0 to 3.10 or later.

The logic module of the 700 to 1500 terminals is available with or without RAM and internal CompactFlash installed. If ordered as separate components, you must install the memory before attaching the logic module to the display module. The internal CompactFlash contains flash memory, FactoryTalk View ME software, and the operating system for CE devices.

Follow these steps to install or replace RAM or internal CompactFlash.

1. Remove power from the terminal.
2. Place the terminal, display side down, on a flat stable surface.
3. Loosen the six captive screws that secure the logic module.
4. Carefully lift the logic module away from the terminal and turn over to expose the circuit board.

## ATTENTION

<!-- image -->

Wear a properly grounded ESD wristband before touching any of the electronic components in the logic module.

Skip steps 5 and 6 if not replacing RAM.

5. Locate the RAM module on the circuit board, pull the metal retaining clips away from the module, and slide out the module.
6. Insert the new RAM module at a 45° angle and snap down.

<!-- image -->

## Install or Replace the Logic Module

Skip steps 7…11 if not replacing the internal CompactFlash.

7. Unscrew and remove the retaining clip that secures the internal CompactFlash card.
8. Pull out the internal CompactFlash card.
9. Insert the new internal CompactFlash card.
10. Reattach the retaining clip.
11. Attach the logic module by aligning the two connectors on the bottom of module with the connectors on the display module.
12. Push down on the logic module until firmly seated.
13. Tighten the six captive screws that secure the logic module to a torque of 0.58 Nm (5…7 lb·in).

This section shows how to install and replace the logic module for 700 to 1500 terminals. If the display module and logic module are ordered as separate components, attach the logic module to the display module before panel installation.

The logic module is available with or without RAM and internal CompactFlash installed. If ordered as separate components, you must install the memory before attaching the logic module to the display module.

Follow these steps to install a logic module.

1. Disconnect power from the terminal.
2. Set the terminal, display side down, on a clean, flat, stable surface to prevent scratches, if the terminal is removed from panel.
3. Position the logic module over the back of the display module until the two connectors on the bottom of the logic module align with the connectors on the display module.
4. Push down on the logic module until firmly seated.

<!-- image -->

5. Tighten the six captive screws that secure the logic module to the display module to a torque of 0.58 Nm (5…7 lb·in).

<!-- image -->

Before replacing the logic module, you must remove the communication module, if attached. You will also need to remove the Internal RAM and CompactFlash from the logic module to reuse in the new logic module.

Follow these steps to replace a logic module.

1. Disconnect power from the terminal.
2. Disconnect all power and communication cables.
3. Set the terminal, display side down, on a clean, flat, stable surface to prevent scratches, if the terminal is removed from panel.
4. Remove the four screws that attach the communication module, if attached, to the logic module and carefully lift the communication module away from the logic module.
5. Loosen the six captive screws that secure the logic module to the display module.
6. Carefully lift the logic module away from the back of the display module.

<!-- image -->

## ATTENTION

<!-- image -->

Wear a properly grounded ESD wristband before touching any of the electronic components in the logic module.

7. If reusing the memory in the new logic module:
2.  remove the RAM and internal CompactFlash from the logic module.
3.  insert the RAM and internal CompactFlash in the new logic module.
8. Install the new logic module.
9. Attach the communication module, if necessary.

## Install or Replace a Communication Module

This section shows how to install and replace a communication module. The communication module installs over the logic module. The communication modules are available as separate catalog numbers for specific communication protocols.

## PanelView Plus 700 to 1500 Terminals

<!-- image -->

The logic module must be attached to the display module before you attach the communication module.

Follow these steps to install a communication module.

1. Disconnect power from the terminal.
2. Set the terminal, display side down, on a clean, flat, stable surface to prevent scratches if the terminal is removed from panel.
3. Remove the label covering the communication module connector on the logic module.
4. Position the communication module over the logic module so that the connectors on bottom of module align with connectors on the logic module.

<!-- image -->

To prevent ESD between the modules, allow the communication module to touch the logic module before making connection.

<!-- image -->

5. Push down on the communication module until the connectors are firmly seated.
6. Tighten the four screws that secure the communication module to the logic module to a torque of 0.58 Nm (5…7 lb·in).

<!-- image -->

Follow these steps to replace a communication module:

1. Disconnect power from the terminal.
2. Disconnect the communication cables from the module.

## WARNING

<!-- image -->

Do not connect or disconnect any communication cable with power applied to this device or any device on the network. An electrical arc could cause an explosion in hazardous location installations. Be sure that power is removed or the area is nonhazardous before proceeding.

3. Remove the four screws that secure the communication module to the logic module.
4. Carefully lift the communication module away from the logic module and set aside.
5. Install the new communication module.

## PanelView Plus 400 and 600 Terminals

Follow these steps to install a communication module.

1. Disconnect power from the terminal.
2. Set the terminal, display side down, on a clean, flat, stable surface.

3. Remove the label covering the connectors on the base unit of the terminal.
4. Position the communication module over back of the terminal so that the connector on bottom of communication module align with the connector on the base unit.

<!-- image -->

<!-- image -->

5. Push down on the communication module until the connector is firmly seated.
6. Tighten the three captive screws that secure the module to the terminal, starting with the bottom, left screw on the module. Tighten screws to a torque of 0.34…0.45 Nm (3…4 lb·in).

Follow these steps to replace a communication module.

1. Disconnect power from the terminal.
2. Disconnect the communication cables from the module.
3. Loosen the three screws that secure the communication module to the terminal.
4. Carefully lift the communication module away from the terminal and set aside.
5. Install the new communication module.

## Replace the Display Module

This section shows how to replace the display module on 700 to 1500 terminals. It is necessary to remove the communication module from the logic module to perform this operation.

<!-- image -->

Follow these steps to replace the display module.

1. Disconnect power from the terminal.
2. Remove the terminal from the panel.
3. Detach the communication module, if attached, from the logic module by removing the four screws.
4. Loosen the six captive screws that attach the logic module to the display module.
5. Carefully lift the logic module from the terminal.
6. Set the display module aside.

<!-- image -->

7. Position the new logic module over the new display module so that the connectors align.
8. Push down on the logic module until firmly seated.
9. Tighten the six captive screws that secure the logic module to the display module to a torque of 0.58 Nm (5…7 lb·in).
10. Attach the communication module (if necessary) and tighten the four screws to a torque of 0.58 Nm (5…7 lb·in).

<!-- image -->

## Replace the Battery

The terminals have a lithium battery that is used by the real-time clock and static RAM. It is not used for application backup or retention.

-  For the 700 to 1500 terminals, the lithium battery is intended to be replaced during the life of the product.
-  For the 400 and 600 terminals, the lithium battery is permanently connected and should be removed only by trained professionals at the end of product life.

For information on battery removal for 400 and 600 terminals, see Disposal Information on page 221 .

<!-- image -->

## ATTENTION

<!-- image -->

## SHOCK HAZARD

<!-- image -->

## WARNING

<!-- image -->

The 700 to 1500 terminals contain a hermetically sealed lithium battery which may need to be replaced during the life of the product.

At the end of its life, the battery contained in this product should be collected separately from any unsorted municipal waste.

The collection and recycling of batteries helps protect the environment and contributes to the conservation of natural resources as valuable materials are recovered.

To avoid voiding your product warranty, use only the Rockwell Automation Allen-Bradley approved battery. Use of another battery may present a risk of fire or explosion.

Failure to follow proper safety precautions could result in severe electrical shock or damage to the computer.

There is a danger of explosion if the lithium battery is incorrectly replaced. Replace the battery only with the indicated type. Do not replace the battery unless the area is known to be nonhazardous.

For Safety information on the handling of lithium batteries, including handling and disposal of leaking batteries, see Guidelines for Handling Lithium Batteries, publication AG-5.4. Replace the battery only with the indicated catalog number.

Do not dispose of battery in a fire or incinerator. Dispose of used batteries in accordance with local regulations.

Follow these steps to replace the battery.

1. Disconnect power from the terminal.
2. Place the terminal, display side down, on a flat stable surface.
3. Detach the communication module, if attached, from the logic module by removing the four screws.
4. Loosen the six captive screws that attach the logic module to the display module.
5. Carefully lift the logic module away from the terminal and flip over to expose the circuit board.

<!-- image -->

## ATTENTION

<!-- image -->

Wear a properly grounded ESD wristband before touching any of the electronic components in the logic module.

6. Locate the battery on the circuit board.
7. Remove the battery by lifting up the side of the battery.
8. Insert the new battery.

<!-- image -->

IMPORTANT

Use only replacement battery 2711P-RY2032.

## Replace the Bezel

9. Attach the logic module by aligning the two connectors on the bottom of the module with the connectors on the terminal.
10. Push down on the logic module until firmly seated.
11. Tighten the six captive screws that secure the logic module to a torque of 0.58 Nm (5…7 lb·in).
12. Attach the communication module (if necessary) and tighten the four screws to a torque of 0.58 Nm (5…7 lb·in).

<!-- image -->

It is not necessary to remove the logic module or communication module before removing the bezel, except on the PanelView Plus 700 terminal.

## Remove the Display Module Bezel

Follow these steps to remove the display module bezel on a 700 to 1500 terminal.

1. Disconnect power from the terminal.
2. Set the terminal, display side down, on a flat stable surface.

## ATTENTION

<!-- image -->

Wear a properly grounded ESD wristband before touching any of the electronic components in the logic module.

3. On touch-screen only terminals, remove the two screws that secure the small metal plate to the back of the display module.

4. Disconnect the touch screen connector.

<!-- image -->

Touch Screen Connector

5. Remove the screws from the back of the display module.

The number of screws varies for each terminal type.

<!-- image -->

6. Remove the sealing gasket.

<!-- image -->

7. Lift the back of the display module away from the bezel.

Work on a clean, flat, stable surface to protect the display from debris, scratches and damage.

<!-- image -->

8. Detach all connectors, maximum of three.

The number of connectors varies by model.

-  IrDa connector, if present
-  Function key connector
-  Touch screen connector
9. Set the bezel aside.

## Replace the Display Module Bezel

Follow these steps to replace the display module bezel.

1. Make sure the bezel is free of lint and marks before attaching.
2. Attach the connectors.

The number of connectors varies by model.

-  IrDa connector, if present
-  Function key connector
-  Touch screen connector
3. Place the back of the display module over the bezel.

Be careful not to pinch any of the cables. Allow the touch screen connector to extend out of the access opening.

4. Attach the touch screen connector.
5. Replace the sealing gasket.
6. Attach the screws that secure the display module to the bezel and tighten to a torque of 1.35…1.58 Nm (12…14 lb·in).

Display Module Bezel

## Replace the Backlight

7. On touch screen terminals, reattach the small metal plate to the back of the display module using two screws and torque to 0.58 Nm (5…7 lb·in).

This section shows how to replace the backlight for the 700, 1000, 1250, and 1500 terminals. The 1250 high-bright terminals do not have a replaceable backlight.

## Backlights for PanelView Plus 700 to 1500 Displays

| Use Cat. No. For Display Series # of Backlights   |
|---------------------------------------------------|
| 2711P-RL7C 700 A and B 1                          |
| 2711P-RL7C2 C 1                                   |
| 2711P-RL10C 1000 A 1                              |
| 2711P-RL10C2 B and C 1                            |
| 2711P-RL12C 1250 A and B 2                        |
| 2711P-RL12C2 C 1                                  |
| 2711P-RL15C 1500 B 2                              |

## IMPORTANT

Disposal: The backlights for these products contain mercury. Dispose of per applicable laws.

Follow these steps to replace the backlight.

1. Disconnect power from the terminal.
2. Remove the display module bezel.

## IMPORTANT

The 700 series C display is not secured by screws and is only retained by a bracket. Use care not to drop the display once the bezel is removed.

3. Remove the four screws that secure the display bracket for the 700 series C display.
4. Remove the four screws that secure the LCD display for all other displays.
5. Lift the LCD display and detach the display connector from the circuit board.

<!-- image -->

The circuit board layout may vary for each terminal model. The location of the connector varies by model.

<!-- image -->

## 6. Detach the backlight connectors from the circuit board.

The 1250 has one or two backlight connectors depending on the series of the display. The 1500 has four backlight connectors.

<!-- image -->

7. Follow these steps for the PanelView Plus 700 and 1000 displays.
- a. Press the retaining tab that secures the backlight and then pull out the backlight.
- b. Insert the new backlight.
8. Follow these steps for the PanelView Plus 1250 and 1500 displays.
- a. Remove the screws that secure the backlights and remove the backlights.
6. – The two backlights for the 1250 series A and B displays are each secured with two screws. The single backlight for the 1250 series C displays is secured with one screw.

<!-- image -->

<!-- image -->

- – For the 1500 series B displays, remove the tape and then remove the backlights.
- b. Insert the new backlights and then secure each with the same screws from the previous step and torque to 0.117 Nm (1.04 lb·in).
9. Attach the LCD display connector to the circuit board. Refer to step 5.
10. Attach the backlight connector to the circuit board.

<!-- image -->

<!-- image -->

<!-- image -->

Refer to step 6.

11. Secure the LCD display.
- a. Attach the display bracket then secure the display in the bracket for the 700 series C display.
- b. Attach the four screws for all othe displays.
4. Tighten the screws and torque to 0.58 Nm (5…7 lb·in).
12. Replace the display module bezel.

## Remove the Product ID Label

## Replace the Keypad Legend Inserts

You can remove the label on your terminal and attach your own label.

1. Remove the Allen-Bradley label using your fingers or a tweezers.
2. Clean area with damp cloth and isopropyl alcohol.
3. Remove adhesive backing of OEM label and affix over area where label was located.

<!-- image -->

This section shows how to replace the legend inserts in the keypad terminals. The legend strips are available as separate catalog numbers for each keypad terminal, except for the PanelView Plus 400 terminal, which does not support replaceable legend strips. One side of the legend strips have the default key legends and the other side is blank for creating custom legends.

## PanelView Plus 600 Terminal

The legend inserts for function keys F1 through F10 are accessible from the back on the unit and can be replaced with the terminal mounted in the enclosure.

Follow these steps to replace the F1 through F10 function key legends.

1. From the rear of the unit, pull the legend strips out from the slots on the lower side of the terminal.

2. Slide the new insert into the same slot until only the end tab is visible.

600 Terminal

<!-- image -->

## PanelView Plus 700 to 1500 Terminals

The F1-Fxx and K1-Kxx legend inserts on the PanelView Plus 700 to 1500 terminals are accessible when the display module bezel is removed.

1. Remove power from the terminal.
2. Remove the display module bezel.
3. Pull the legend inserts out from the slots on the bezel.
4. Slide the new legend strips into the same slots until only the end tab is visible.
5. Replace the display module bezel.

<!-- image -->

## Use an External CompactFlash Card

All of the terminals have a CompactFlash card slot that supports Type 1 CompactFlash cards that come in different memory sizes.

The orientation of the card slot on the 700 to 1500 terminals varies depending on the series of the logic module.

<!-- image -->

## Insert a CompactFlash Card

Insert the card in the CompactFlash card slot until firmly seated.

<!-- image -->

## Remove a CompactFlash Card

Press the Eject button on the logic module. When the button pops out, press it again to release the card. The location of the button varies depending on the series of the logic module.

The PanelView Plus 400 and 600 terminals do not have an eject button. Secure edge of card with fingers and pull card away from slot.

<!-- image -->

700 to 1500 Terminals

<!-- image -->

## Chapter Objectives

## Wiring and Safety Guidelines

## Terminal Connections

This chapter provides network and device connections for the terminals.

-  Wiring and safety guidelines
-  Logic controller cable charts
-  Communication port isolation
-  USB ports
-  Serial connections on base unit
-  Ethernet (onboard communication)
-  DH-485/DH+/RIO communication module
-  ControlNet communication module
-  DeviceNet communication module

Use publication NFPA 70E, Electrical Safety Requirements for Employee Workplaces, IEC 60364 Electrical Installations in Buildings or other applicable wiring safety requirements for the country of installation when wiring the devices. In addition to the NFPA guidelines.

-  Route communication cables to terminal by a separate path from incoming power.

## IMPORTANT

Do not run signal wiring and power wiring in the same conduit.

-  Cross power and communication lines at right angles if they must cross. Communication lines can be installed in the same conduit as low-level DC I/O lines (less than 10V).
-  Shield and ground cables appropriately to avoid electromagnetic interference (EMI).

Grounding minimizes noise from EMI and is a safety measure in electrical installations.

For more information on grounding recommendations, refer to the National Electrical Code published by the National Fire Protection.

<!-- image -->

## Logic Controller Cable Charts

The charts provide a summary of terminal connections to controllers and network interface modules.

## Runtime Communication Cables - To Controller

## PanelView Plus and PanelView Plus CE Terminals to SLC Controllers

|               |                                                                                                        | Cables: PanelView Plus and PanelView Plus CE to SLC Controllers   | Cables: PanelView Plus and PanelView Plus CE to SLC Controllers    | Cables: PanelView Plus and PanelView Plus CE to SLC Controllers   | Cables: PanelView Plus and PanelView Plus CE to SLC Controllers   | Cables: PanelView Plus and PanelView Plus CE to SLC Controllers   |
|---------------|--------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------|--------------------------------------------------------------------|-------------------------------------------------------------------|-------------------------------------------------------------------|-------------------------------------------------------------------|
| Protocol      | PanelView Plus Comm Port                                                                               | SLC-500, 5/01, 5/02 CH1 RJ45 (DH-485)                             | SLC-5/03, 5/04, 5/05 CH0 (9-pin RS-232) (DF1 or DH-485)            | SLC 5/03 CH1 (RJ45) (DH-485)                                      | SLC 5/04 CH1 (DH+)                                                | SLC 5/05 CH1 (ENET)                                               |
| DF1 (any)     | RS-232 (DF1) Port (9-pin) PanelView Plus 400 to 1500 2711P-RN22C                                       | N/A                                                               | 2711-NC13 (5 m/16 ft) 2711-NC14 (10 m/32 ft) 2706-NC13 (3 m/10 ft) | N/A                                                               | N/A                                                               | N/A                                                               |
| DH-485 (any)  | RS-232 (DH-485) Port (9-pin) PanelView Plus 400 to 1500 2711P-RN22C                                    | Use AIC+ Module (1761-NET-AIC) Connect to Port 1 or 2             | 2711-NC13 (5 m/16 ft) 2711-NC14 (10 m/32 ft) 2706-NC13 (3 m/10 ft) | Use AIC+ Module (1761-NET-AIC) Connect to Port 1 or 2             | N/A                                                               | N/A                                                               |
|               | DH-485 Port PanelView Plus 400 and 600 2711P-RN3(2)                                                    | 1747-C10 (2 m/6 ft) 1747-C11 (0.3 m/1 ft) 1747-C20 (6 m/20 ft)    | Use AIC+ Module (1761-NET-AIC) Connect to Port 3                   | 1747-C10 (2 m/6 ft) 1747-C11 (0.3 m/1 ft) 1747-C20 (6 m/20 ft)    |                                                                   | N/A N/A                                                           |
|               | DH-485 Port PanelView Plus 700 to 1500 2711P-RN6, -RN6K                                                | 1761-CBL-AS03 (3 m/10 ft) 1761-CBL-AS09 (9 m/30 ft)               | Use AIC+ Module (1761-NET-AIC) Connect to Port 3                   | 1761-CBL-AS03 (3 m/10 ft) 1761-CBL-AS09 (9 m/30 ft)               |                                                                   | N/A N/A                                                           |
| ControlNet    | ControlNet Port PanelView Plus 400 and 600 2711P-RN15C PanelView Plus 700 to 1500 2711P-RN15S, -RN15SK | N/A                                                               | 1747-KFC15A or 1747-SCRNR/A Module with ControlNet Cable           | 1747-KFC15A or 1747-SCRNR/A Module with ControlNet Cable          | 1747-KFC15A or 1747-SCRNR/A Module with ControlNet Cable          | 1747-KFC15A or 1747-SCRNR/A Module with ControlNet Cable          |
| DeviceNet(1)  | DeviceNet Port PanelView Plus 400 and 600 2711P-RN10C PanelView Plus 700 to 1500 2711P-RN10H           | N/A                                                               | Use 1747-SDN Module with DeviceNet Cable                           | Use 1747-SDN Module with DeviceNet Cable                          | Use 1747-SDN Module with DeviceNet Cable                          | Use 1747-SDN Module with DeviceNet Cable                          |
| EtherNet/IP   | EtherNet/IP Port PanelView Plus 400 to 1500 All except 2711P-xxx5xx                                    | N/A                                                               | Use 1761-NET-ENI Module with Ethernet Cable                        |                                                                   | N/A N/A                                                           | 1585J-M Type Cable or 2711P CBL-EX04 (4 m/14 ft)  (3)                                                                   |
| Remote I/O(1) | Remote I/O Port PanelView Plus 400 to 1500 2711P-RN1, 2711P-RN6                                        | SLC 5/02 only Use 1747-SN with Shielded Twinaxial Cable (1770-CD) | Use 1747-SN Module with Shielded Twinaxial Cable (1770-CD)         | Use 1747-SN Module with Shielded Twinaxial Cable (1770-CD)        | Use 1747-SN Module with Shielded Twinaxial Cable (1770-CD)        | Use 1747-SN Module with Shielded Twinaxial Cable (1770-CD)        |
|               | DH+ DH+ Port PanelView Plus 400 and 600 2711P-RN8 PanelView Plus 700 to 1500 2711P-RN6, -RN6K          |                                                                   |                                                                    | N/A N/A N/A                                                       | Shielded Twinaxial Cable (1770-CD)                                | N/A                                                               |

## PanelView Plus and PanelView Plus CE Terminals to PLC-5 and MicroLogix Controllers

|               |                                                                                                        | Cables: PanelView Plus and PanelView Plus CE to PLC-5 and MicroLogix Controllers                  | Cables: PanelView Plus and PanelView Plus CE to PLC-5 and MicroLogix Controllers   | Cables: PanelView Plus and PanelView Plus CE to PLC-5 and MicroLogix Controllers   | Cables: PanelView Plus and PanelView Plus CE to PLC-5 and MicroLogix Controllers   |
|---------------|--------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|
|               | Protocol PanelView Plus Comm Port                                                                      | PLC-5, PLC-5C, PLC-5E CH0 (25-pin RS-232) (DF1)                                                   | MicroLogix 1400, 1500LRP CH1/CH2 (9-pin RS-232) (DF1 or DH-485)                    | MicroLogix 1000, 1100, 1200, 1400, 1500LSP CH0 (8-pin Mini DIN) (DF1 or DH-485)    | MicroLogix 1100, 1400 Ethernet                                                     |
| DF1 (any)     | RS-232 (DF1) Port (9-pin) PanelView Plus 400 to 1500 2711P-RN22C                                       | 2711-NC13 (5 m/16 ft) 2711-NC14 (10 m/32 ft) 2706-NC13 (3 m/10 ft) (9-to-25 pin adapter required) | 2711-NC13 (5 m/16 ft) 2711-NC14 (10 m/32 ft) 2706-NC13 (3 m/10 ft)                 | 2711-NC21 (5 m/16 ft) 2711-NC22 (15 m/49 ft) (null modem not required)  (4)        | N/A                                                                                |
| DH-485 (any)  | RS-232 (DH-485) Port (9-pin) PanelView Plus 400 to 1500 2711P-RN22C                                    | N/A                                                                                               | 2711-NC13 (5 m/16 ft) 2711-NC14 (10 m/32 ft) 2706-NC13 (3 m/10 ft)                 | 2711-NC21 (5 m/16 ft) 2711-NC22 (15 m/49 ft) (null modem not required)  (4)        | N/A                                                                                |
|               | DH-485 Port PanelView Plus 400 and 600 2711P-RN3(2) PanelView Plus 700 to 1500 2711P-RN6, -RN6K        | N/A                                                                                               | N/A                                                                                | Use AIC+ Module (1761-NET-AIC) Connect to Port 3                                   | N/A                                                                                |
| ControlNet    | ControlNet Port PanelView Plus 400 and 600 2711P-RN15C PanelView Plus 400 to 1500 2711P-RN15S, -RN15SK | To PLC-5C with ControlNet Cable                                                                   | N/A                                                                                | N/A                                                                                | N/A                                                                                |
| DeviceNet(1)  | DeviceNet Port PanelView Plus 400 and 600 2711P-RN10C PanelView Plus 700 to 1500 2711P-RN10H           | Use 1771-SDN Module with DeviceNet Cable                                                          |                                                                                    |                                                                                    | N/A N/A N/A                                                                        |
| EtherNet/IP   | EtherNet/IP Port PanelView Plus 400 to 1500 All except 2711P-xxx5xx                                    | To PLC-5E with 1585J-M Type Cable or 2711P- CBL-EX04 (4 m/14 ft)  (3)                             | Use 1761-NET-ENI Module with Ethernet Cable                                        | Use 1761-NET-ENI Module with Ethernet Cable                                        | 1585J-M Type Cable or 2711P- CBL-EX04 (4 m/14 ft)  (3)                             |
| Remote I/O(1) | Remote I/O Port PanelView Plus 400 to 1500 2711P-RN1, 2711P-RN6                                        | Shielded Twinaxial Cable (1770-CD)                                                                |                                                                                    | N/A N/A N/A                                                                        |                                                                                    |
| DH+           | DH+ Port PanelView Plus 400 and 600 2711P-RN8 PanelView Plus 700 to 1500 2711P-RN6, -RN6K              | Shielded Twinaxial Cable (1770-CD)                                                                | N/A                                                                                | N/A                                                                                | N/A                                                                                |

## PanelView Plus and PanelView Plus CE Terminals to Logix Controllers

|               |                                                                                                        | Cables: PanelView Plus and PanelView Plus CE to Logix Controllers                            | Cables: PanelView Plus and PanelView Plus CE to Logix Controllers                                        |
|---------------|--------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| Protocol      | PanelView Plus Comm Port                                                                               | ControlLogix CH0 (9-pin RS-232) (DF1)                                                        | CompactLogix CH0 (9-pin RS-232) (DF1 or DH-485)                                                          |
| DF1 (any)     | RS-232 (DF1) Port (9-pin) PanelView Plus 400 to 1500 2711P-RN22C                                       | 2711-NC13 (5 m/16 ft) 2711-NC14 (10 m/32 ft) 2706-NC13 (3 m/10 ft)                           | 2711-NC13 (5 m/16 ft) 2711-NC14 (10 m/32 ft) 2706-NC13 (3 m/10 ft)                                       |
| DH-485 (any)  | RS-232 (DH-485) Port (9-pin) PanelView Plus 400 to 1500 2711P-RN22C                                    | N/A                                                                                          | 2711-NC13 (5 m/16 ft) 2711-NC14 (10 m/32 ft) 2706-NC13 (3 m/10 ft)                                       |
|               | DH-485 Port PanelView Plus 400 and 600 2711P-RN3(2) , PanelView Plus 700 to 1500 2711P-RN6, -RN6K      | N/A                                                                                          | Use AIC+ Module (1761-NET-AIC) Connect to Port 3                                                         |
| ControlNet    | ControlNet Port PanelView Plus 400 and 600 2711P-RN15C PanelView Plus 700 to 1500 2711P-RN15S, -RN15SK | Use 1756-CNB Module with ControlNet Cable                                                    | 1769-L35CR, -L32C, -1768-CNB, or 1768-CNBR with ControlNet Cable                                         |
| DeviceNet(1)  | DeviceNet Port PanelView Plus 400 and 600 2711P-RN10C PanelView Plus 700 to 1500 2711P-RN10H           | Use 1756-DNB Module with DeviceNet Cable                                                     | Use 1769-SDN Module with DeviceNet Cable                                                                 |
| EtherNet/IP   | EtherNet/IP Port PanelView Plus 400 to 1500 All except 2711P-xxx5xx                                    | Use 1756-EN2T or 1756-ENBT Module with 1585J-M Type Cable or 2711P- CBL-EX04 (4 m/14 ft) (3) | To 1769-L35E, L23E, L32E, or 1768-ENBT Module with 1585J-M Type Cable or 2711P- CBL-EX04 (4 m/14 ft) (3) |
| Remote I/O(1) | Remote I/O Port PanelView Plus 400 to 1500 2711P-RN1, 2711P-RN6                                        | Use 1756-DHRIO Module with Shielded Twinaxial Cable (1770-CD)                                | N/A                                                                                                      |
|               | DH+ DH+ Port PanelView Plus 400 and 600 2711P-RN8 PanelView Plus 700 to 1500 2711P-RN6, -RN6K          | Use 1756-DHRIO Module with Shielded Twinaxial Cable (1770-CD)                                | N/A                                                                                                      |

## PanelView Plus Terminals to Communication Adapters

|              |                                                                                        | Cables: PanelView Plus to Communication Adapters              | Cables: PanelView Plus to Communication Adapters                   | Cables: PanelView Plus to Communication Adapters   | Cables: PanelView Plus to Communication Adapters                   | Cables: PanelView Plus to Communication Adapters                                 |
|--------------|----------------------------------------------------------------------------------------|---------------------------------------------------------------|--------------------------------------------------------------------|----------------------------------------------------|--------------------------------------------------------------------|----------------------------------------------------------------------------------|
|              |                                                                                        |                                                               | 1761-NET-AIC                                                       | 1761-NET-AIC                                       | 1761-NET-AIC                                                       | 1761-NET-AIC                                                                     |
|              | Protocol PanelView Plus Comm Port                                                      | 1747-AIC                                                      | Port 1 (9-pin)                                                     | Port 2 8-pin Mini DIN()                            | Port 3 (DH-485)                                                    | 1761-NETDNI or 1771-NET-ENI                                                      |
|              | DF1 (any) RS-232 Port (9-pin) PanelView Plus 400 to 1500 2711P-RN22C (for 400 and 600) | N/A                                                           | 2711-NC13 (5 m/16 ft) 2711-NC14 (10 m/32 ft) 2706-NC13 (3 m/10 ft) | 2711-NC21 (5 m/16 ft) 2711-NC22 (15 m/49 ft)       | N/A                                                                | 1761-CBL-AP00 (5 m) 1761-CBL-PM02 (2 m) 2711-CBL-PM05 (5 m) 2711-CBL-PM10 (10 m) |
| DH-485 (any) | RS-232 Port (9-pin) PanelView Plus 400 to 1500 2711P-RN22C (for 400 and 600)           | N/A                                                           | 2711-NC13 (5 m/16 ft) 2711-NC14 (10 m/32 ft) 2706-NC13 (3 m/10 ft) | 2711-NC21 (5 m/16 ft) 2711-NC22 (15 m/49 ft)       | N/A                                                                | N/A                                                                              |
|              | DH-485 Port PanelView Plus 400 and 600 2711P-RN3(1)                                    | 1747-C10 (2 m/6ft) 1747-C11 (0.3 m/1 ft) 1747-C20 (6 m/20 ft) | N/A                                                                | N/A                                                | 1761-CBL-AS03 (3 m/10 ft) 1761-CBL-AS09 (9 m/30 ft) to single AIC+ | N/A                                                                              |
|              | DH-485 Port PanelView Plus 700 to 1500 2711P-RN6, -RN6K                                | Direct Connection to Single AIC with Belden 9842 Cable(2)     | N/A                                                                | N/A                                                | Direct Connection to Single AIC+ with Belden 9842 Cable(2)         | N/A                                                                              |

## Communication Port Isolation

The PanelView Plus and PanelView Plus CE terminals contain integral and modular (externally attached) communication ports. Some of these ports contain electrical isolation depending on the catalog number of the terminal or communication module.

## Integral Communication Port Isolation

|          | Communication Port 400 and 600 Terminal 700 to 1500 Terminal   |             |
|----------|----------------------------------------------------------------|-------------|
|          | RS-232 Nonisolated Isolated                                    |             |
| USB      | Nonisolated                                                    | Nonisolated |
| Ethernet | Isolated                                                       | Isolated    |

## 400 and 600 Modular Communication Port Isolation

| Communication Port Module   |             | Isolation    |
|-----------------------------|-------------|--------------|
| RS-232                      | 2711P-RN22C | Isolated     |
| DH-485                      | 2711P-RN3   | Nonisolated  |
| DH+                         | 2711P-RN8   | Isolated     |
| Remote I/O                  | 2711P-RN1   | Isolated     |
| DeviceNet                   | 2711P-RN10C | Isolated     |
| ControlNet                  | 2711P-RN15C | Isolated (1) |

## 700 to 1500 Modular Communication Port Isolation

| Communication Port Module   |             | Isolation   |
|-----------------------------|-------------|-------------|
| DH-485                      | 2711P-RN6   | Isolated    |
| DH+                         | 2711P-RN6   | Isolated    |
| Remote I/O                  | 2711P-RN6   | Isolated    |
| DeviceNet                   | 2711P-RN10H | Isolated    |
| ControlNet                  | 2711P-RN15S | Isolated    |

## USB Ports

<!-- image -->

The 700 to 1500 terminals have two USB ports. The 400 and 600 terminals have one USB port. The terminals support standard USB keyboard and mouse devices (HID devices) with native device drivers. They also support some USB printers that have Printer Control Language (PCL) capabilities. A vendor specific Windows CE driver is required for all other USB devices.

See Appendix B for a list of compatible USB devices.

Plug the USB device into either one of the two USB ports on the 700 to 1500 terminals.

## USB Connector Pinout

| Pin Signal   |
|--------------|
| 1 USBVCC     |
| 2 USBD              |
| 3 USBD+      |
| 4 USB-GND    |

## WARNING

<!-- image -->

Do not connect or disconnect the communication cable with power applied to the terminal, or the serial device on the other end of the cable. An electrical arc could cause an explosion in hazardous location installations. Be sure that power is removed or the area is nonhazardous before proceeding.

## WARNING

<!-- image -->

USB devices not powered by the USB port must be within the same enclosure and connected to a ground system common with the terminal, or the USB devices must be used with a USB hub that provides galvanic isolation.

If a USB hub is connected to the terminal, an externally powered USB hub is recommended. Before attaching devices to a USB hub, check that the power adapter is connected and powered on.

## Serial Connections

The base-configured unit of all terminals has a multi-purpose serial RS-232 port that supports:

-  DH-485 communication through a serial connection.
-  DF1 full duplex communication with controllers using direct connections or modem connections.
-  third-party point-to-point communication.
-  application uploads/downloads.
-  printing.

The serial port on the base-configured unit of the terminal is a 9-pin, male, RS-232 connector. The table shows the pinout descriptions for this port and how these pins map to the serial ports on the controllers.

<!-- image -->

## Serial Port Connector Pinout

Connector Shell Chassis Gnd

|   PanelView Plus RS-232 Port 9-pin DCE |
|----------------------------------------|
|                                      1 |
|                                      2 |
|                                      3 |
|                                      4 |
|                                      5 |
|                                      6 |
|                                      7 |
|                                      8 |
|                                      9 |

<!-- image -->

The maximum cable length for serial communication is 15.24 m (50 ft).

<!-- image -->

Do not connect or disconnect the communication cable with power applied to the terminal, or the serial device on the other end of the cable. An electrical arc could cause an explosion in hazardous location installations. Be sure that power is removed or the area is nonhazardous before proceeding.

| SLC 9-pin PLC 25-pin   | MicroLogix/ DNI 8-pin DIN   |
|------------------------|-----------------------------|
| 23 4                   |                             |
| 32 7                   |                             |
| 4 20                   |                             |
| 57 2                   |                             |
| 6 6                    |                             |
| 7 4                    |                             |
| 8 5                    |                             |

## Modem Connection

Wire or radio modem communication is possible between the terminal and controller. Each modem must support full duplex communication. Refer to your modem user manual for details on settings and configuration.

<!-- image -->

## Construct a Null Modem Cable

To construct a null modem cable, refer to this pinout.

## Null Modem Pinout

FG (Frame Ground) - - - 1 FG

TD (Transmit Data) 3 2 3 3 RD

RD (Receive Data) 2 3 2 2 TD

RTS (Request to Send) 7 8 7 5 CTS

CTS (Clear to Send) 8 7 8 4 RTS

SG (Signal Ground) 5 5 5 7 SG

DSR (Data Set Ready) 6 4 6 20 DTR

DTR (Data Terminal Ready) 4 6 4 6 DSR

| PanelView Plus 9-pin   | 9-pin Modem   |
|------------------------|---------------|

| PanelView Plus 9-pin   | 25-pin Modem   |
|------------------------|----------------|

## Computer Connections

The RS-232 serial port on the base-configured unit of the terminals supports:

-  application uploads/downloads using a direct connection.
-  printing.

<!-- image -->

| PanelView Plus Printer Port (DCE)   | Computer Port (DTE)   | Computer Port (DTE)   |
|-------------------------------------|-----------------------|-----------------------|
| 9-pin male 9-pin 25-pin             |                       |                       |
| 2  RXD                              | 2 3                   |                       |
| 3  TXD                              | 3 2                   |                       |
| 5  COM                              | 5 7                   |                       |

## Ethernet Connections

The base-configured unit of the 700 to 1500 terminals and the network based unit of the 400 and 600 terminals have an Ethernet port that supports:

-  EtherNet/IP communication.
-  third-party Ethernet communication.
-  network connections.
-  application uploads/downloads.
-  printing.

## Ethernet Connector

The base-configured unit of the terminals has an RJ45, 10/100 Base-T connector for EtherNet/IP or Ethernet TCP/IP network communication.

<!-- image -->

The table shows the connector pinouts.

## Ethernet Connector Pinout

| Pin                              | Pin Pin Name                                                       |
|----------------------------------|--------------------------------------------------------------------|
| Looking into RJ45 Connector 1  8 | 1 TD+                                                              |
| Looking into RJ45 Connector 1  8 | 2 TD                                                                    |
| Looking into RJ45 Connector 1  8 | 3 RD+                                                              |
| Looking into RJ45 Connector 1  8 | 4 NC                                                               |
| Looking into RJ45 Connector 1  8 | 5 NC                                                               |
| Looking into RJ45 Connector 1  8 | 6 RD                                                                    |
| Looking into RJ45 Connector 1  8 | 7 NC                                                               |
| Looking into RJ45 Connector 1  8 | 8 NC                                                               |
|                                  | Shield Connection No direct connection (AC coupled to chassis GND) |

Use point-to-point, 10/100 Base-T cables with cross over pin-outs, such as 2711P-CBL-EX04, when connecting the Ethernet port on the terminal directly to a logic controller's Ethernet port or a computer 10/100 Base-T port.

## Ethernet Cable

For PanelView Plus 700 to 1500 terminals, use Belden 7921A shielded Ethernet Category 5e cable according to TIA 568-B.1 and RJ45 connector according to IEC 60603-7 for compliance with Marine emissions limits and the European Union 89/336/EEC EMC Directive.

The maximum cable length between the terminal's Ethernet port and a 10/100 Base-T port on an Ethernet hub (without repeaters or fiber) is 100 m (328 ft).

<!-- image -->

Do not connect or disconnect any communication cable with power applied to this device or any device on the network. An electrical arc could cause an explosion in hazardous location installations. Be sure that power is removed or the area is nonhazardous before proceeding.

## Security Considerations

IGMP (Internet Group Management Protocol) is used for IPv4 multicast. A multicast is communication between a single sender and multiple receivers on a network. IGMP is used to exchange membership status data between IPv4 routers that support multicasting and members of multicast groups. A router is an intermediary device on a communication network that expedites message delivery by finding the most efficient route for a message packet within a network, or by routing packets from one subnetwork to another. A sub-network is a separate part of an organization's network identified through IP addressing.

PanelView Plus terminals provide level 2 (full) support for IPv4 multicasting (IGMP version 2) as described in RFC 1112 and RFC 2236.

SNMP (Simple Network Management Protocol) is used for internal network management and is not supported.

Ports 137 and 138 are normally open to support the NetBIOS protocol used by Windows CE.NET similar to other Microsoft and IBM network operating systems.

## DH-485/DH+/Remote I/O Module

Terminals with a DH-485/DH+/Remote I/O communication module support communication with these networks.

-  DH+ networks
-  DH-485 networks
-  Remote I/O networks

You can communicate with only one network at one time.

The 700 to 1500 terminals support all protocols on one module. The 400 and 600 terminals require a separate module for each protocol. The DH+, DH-485, and Remote I/O connections are different between the modules for the 400 and 600 and 700 to 1500 terminals.

Module Connections

## IMPORTANT

See your controller documentation for appropriate controller connections.

## 700 to 1500 Terminals

<!-- image -->

## IMPORTANT

<!-- image -->

When using the DH-485 module, catalog number 2711P-RN3, with PanelView Plus 400 and 600 terminals, the cable length must not exceed 30 m (98 ft) to comply with CE requirements. For longer cable lengths, use the 1761-NET-AIC or 1747-AIC module.

## DH+ Status Indicator

| Condition Indication                               |
|----------------------------------------------------|
| Off  Channel is not online.                        |
| Blinking green Device is only node on the network. |
| Solid green Device is online and receiving token.  |
| Blinking red Duplicate node.                       |
| Solid red Failed selftest.                         |

## DH-485 Status Indicator

| Condition Indication                               |
|----------------------------------------------------|
| Off  Channel is not online.                        |
| Blinking green Device is only node on the network. |
| Solid green Device is online and receiving token.  |
| Blinking red Parity error.                         |
| Solid red Failed selftest.                         |

## Remote I/O Scanner Mode Status Indicator

| Condition Indication                                                                 |
|--------------------------------------------------------------------------------------|
| Off  Channel is not online.                                                          |
| Blinking green At least one but not all adapters in the scanlist are not responding. |
| Solid green All adapters in the scanlist are responding.                             |
| Blinking red None of the adapters in the scanlist are responding.                    |
| Solid red Failed selftest.                                                           |

## DH-485 Network Port Wiring for 700 to 1500 Terminals

Use these instructions for wiring Belden cable. If you are using standard Allen-Bradley cables, see the Logic Controller Cable Charts .

## IMPORTANT

A daisy-chained network is recommended. We do not recommend hybrid star/daisy chain networks as shown.

## RS-485 Connector to the Communication Cable

<!-- image -->

Attach the connector to the Belden #3106A or #9842 Cable as shown.

## Single Cable Connection

<!-- image -->

## Multiple Cable Connection

<!-- image -->

The table shows connections for Belden #3106A.

## Belden 3106A Wire Connections

| For this Wire/Pair   | Connect this Wire                              | To this Terminal      |
|----------------------|------------------------------------------------|-----------------------|
| Shield/Drain         | Non-jacketed                                   | Terminal 2 - Shield   |
| Blue                 | Blue                                           | Terminal 3 - (Common) |
| White/Orange         | White with Orange Stripe Terminal 4 - (Data B) |                       |
|                      | Orange with White Stripe Terminal 5 - (Data A) |                       |

## DH-485 Connections for 400 and 600 Terminals

This section shows connections between a 400 and 600 terminal with a DH-485 communication module and an SLC or ControlLogix controller through the AIC+ module.

<!-- image -->

## DH+ Network Connections

Use the Belden 9463 twin axial or equivalent cable (cat. no. 1770-CD), to connect a terminal to a DH+ link.

You can connect a DH+ link in two ways.

-  Trunk line/drop line - from the drop line to the connector screw terminals on the DH+ connectors of the processor
-  Daisy chain - to the connector screw terminals on the DH+ connectors on the processor

Follow these guidelines when installing DH+ communication links.

-  do not exceed these cable lengths:
- – Trunk line-cable length: 3,048 m (10,000 ft).
- – Drop-cable length: 30.4 m (100 ft).

The maximum cable length is determined by baud rate.

-  Do not connect more than 64 stations on a single DH+ link.

<!-- image -->

## Remote I/O Connections

Use the Belden 9463 twin axial or equivalent cable (cat. no. 1770-CD), to connect a terminal to a Remote I/O scanner. The maximum cable length (link distance) is determined by the baud rate.

-  2800 m (10,000 ft) for 57.6 Kbps
-  1400 m (5,000 ft) for 115.2 Kbps
-  700 m (2,500 ft) for 230.4 Kbps

See Industrial Automation Wiring and Grounding Guidelines, publication 1770-4.1. The user manual for the I/O scanner module also provides cabling information.

<!-- image -->

## ControlNet Module

Terminals with a ControlNet communication module support communication and the transfer of applications between devices on a ControlNet network.

## Related Information

For more information on ControlNet products, refer to these publications:

-  NetLinx Selection Guide, publication NETS-SG001
-  ControlNet Coax Media Planning and Installation Guide, publication CNET-IN002
-  ControlNet Communication for PanelView Plus and PanelView Plus CE Terminals User Manual, publication 2711P-UM003

The Rockwell Automation website http://rockwellautomation.com provides information and product descriptions of ControlNet products. Under the Products and Services heading, select Communication.

## ControlNet Protocol

The terminals support Unscheduled and Scheduled messaging, Scheduled I/O, and redundant cabling with PLC-5C and ControlLogix controllers.

The ControlNet architecture supports multiple processors and up to 99 nodes (via taps) anywhere along the trunk cable of the network. There is no minimum tap separation and you can access the ControlNet network from every node (including adapters).

## Compatible ControlNet Controllers

A terminal with a ControlNet Module communicates with a PLC-5C (PCCC commands) or a ControlLogix processor (CIP protocol) using Unscheduled messaging. The following controllers are supported:

-  ControlLogix using 1756-CNB module
-  PLC-5/20C, PLC-5/40C, PLC-5/60C, PLC-5/80C

## Minimum Requirements

The software and firmware must be installed on the development computer and the PanelView Plus terminal to configure and communicate with an Allen-Bradley controller on a ControlNet network.

## ControlNet Unscheduled Communication

| Software/Firmware PanelView Plus 700 to 1500 PanelView Plus 400 or 600                        |                                       |
|-----------------------------------------------------------------------------------------------|---------------------------------------|
| FactoryTalk View Studio Version 3.10 or later Version 4.0 or later                            |                                       |
| FactoryTalk View Machine Edition Runtime Version 3.10 or later Version 4.0 or later           |                                       |
| ControlNet Module Firmware 2711P-RN15S, Series A, Rev A (firmware version 2.07 or later)  (1) | 2711P-RN15C, Series B, Rev A or later |

## ControlNet Scheduled Communications

| Requirements                                                      | PanelView Plus 700 to 1500 PanelView Plus 400 or 600               |                                       |
|-------------------------------------------------------------------|--------------------------------------------------------------------|---------------------------------------|
| FactoryTalk View Studio                                           | Version 3.20 or later                                              | Version 4.0 or later                  |
| FactoryTalk View Machine Edition Runtime Version 3.20.04 or later |                                                                    | Version 4.0 or later                  |
| RSNetWorx for ControlNet                                          | Version 5.11 or later                                              | Version 6.0 or later                  |
| RSLogix 5000                                                      | Version 13.0 or later                                              | Version 15.0 or later                 |
| ControlNet Module Firmware                                        | 2711P-RN15S, Series A, Rev C (firmware version 3.08 or later)  (1) | 2711P-RN15C, Series B, Rev A or later |

<!-- image -->

The ControlNet Communications Module, cat. no. 2711P-RN15S, will not run with FactoryTalk View ME firmware version 3.20.04 or earlier. All ControlNet Modules with version 3.07 firmware must be upgraded to version 3.08 or later; otherwise, outputs may turn on an indeterminate state.

## ControlNet Connections

## 2711P-RN15C ControlNet Module for 400 and 600 Terminals

<!-- image -->

## 2711P-RN15S ControlNet Module for 700 to 1500 Terminals

<!-- image -->

## ATTENTION

<!-- image -->

Do not connect more than one ControlNet network to the Communications Module. If you attempt to connect a second network to the module, your communication system will operate erratically.

## NAP and Redundant Cables

Refer to the ControlNet Coax Media Planning and Installation Guide, publication CNET-IN002, for descriptions of ControlNet components.

| Item                 | Cat. No.                       |
|----------------------|--------------------------------|
| RG-6 quad-shield     | 1786-RG6                       |
| Coax repeater        | 1786-RPT, -RPTD                |
| Coax taps            | 1786-TPR, -TPS, -TPYR, -TPYS   |
| Network access cable | 1786-CP                        |
| Coax tool kit        | 1786-CTK                       |
| Segment terminators  | 1786-XT                        |
| BNC connectors       | 1786-BNC, -BNCJ, -BNCP, -BNCJ1 |

## IMPORTANT

Do not connect to a network using both the redundant cable BNC connector and the Network Access Port (NAP).

## DeviceNet Module

## Connect the Module to the Network

You can connect the ControlNet Module:

-  directly to a ControlNet network, which requires a tap.
-  to a device already connected to the ControlNet network.

## WARNING

<!-- image -->

When used in a Class I, Division 2, hazardous location, this equipment must be mounted in a suitable enclosure with proper wiring that complies with the governing electrical codes.

Do not connect or disconnect any communication cable with power applied to this device or any device on the network. An electrical arc could cause an explosion in hazardous location installations. Be sure that power is removed or the area is nonhazardous before proceeding.

Terminals with a DeviceNet communication module support communication and the transfer of applications between devices on a DeviceNet network.

## Related Information

For more information on DeviceNet products, refer to these publications:

-  NetLinx Selection Guide, publication NETS-SG001B
-  DeviceNet Media Design Installation Guide, publication DNET-UM072

The Rockwell Automation website http://rockwellautomation.com provides information and product descriptions of DeviceNet products. Under the Products and Services heading, select Communications.

## DeviceNet Protocol

The terminals support DeviceNet Scheduled I/O only. This protocol allows direct connection of field devices such as lights, drives, and valves. It also provides a control architecture that supports multiple processors. The DeviceNet network is a trunk/drop or bus-based network that supports up to 64 nodes and operates at 125, 250, or 500 Kbps.

## Compatible DeviceNet Controllers

A terminal with a DeviceNet module communicates with an SLC-500 and PLC-5 (PCCC commands), or a ControlLogix processor (CIP protocol) using Unscheduled messaging. Supported controllers include:

-  ControlLogix using 1756-DNB module.
-  PLC-5 with a 1771-SDN module.
-  SLC 5/03 - SLC 5/05 with a 1747-SDN module.

## Minimum Requirements

| Software/Firmware                                             |                      | PanelView Plus 700 to 1500 PanelView Plus 400 and 600   |
|---------------------------------------------------------------|----------------------|---------------------------------------------------------|
| FactoryTalk View Studio                                       | Version 4.0 or later | Version 4.0 or later                                    |
| FactoryTalk View Machine Edition Runtime Version 4.0 or later |                      | Version 4.0 or later                                    |
| DeviceNet Module                                              | 2711P-RN10H          | 2711P-RN10C                                             |

## DeviceNet Connections

## 2711P-RN10C DeviceNet Module for 400 and 600 Terminals

<!-- image -->

## 2711P-RN10H DeviceNet Module for 700 to 1500 Terminals

<!-- image -->

## WARNING

<!-- image -->

Do not connect or disconnect any communication cable with power applied to this device or any device on the network. An electrical arc could cause an explosion in hazardous location installations. Be sure that power is removed or the area is nonhazardous before proceeding.

## DeviceNet I/O Status Indicator

This bicolor (green/red) LED provides information on the states of inputs and/or outputs.

| Condition Status   |                | Indication                                                                    |
|--------------------|----------------|-------------------------------------------------------------------------------|
| Off                | Outputs active | All outputs are active.                                                       |
|                    | Inputs active  | All inputs are active.                                                        |
| Green              | Outputs active | One or more outputs are active and under control, and no outputs are faulted. |
|                    | Inputs active  | One or more inputs are active and producing data, and no inputs are faulted.  |
| Flashing green (1) | Outputs idle   | One or more outputs are idle, and no outputs are active or faulted.           |

| Condition Status   |                    | Indication                                                               |
|--------------------|--------------------|--------------------------------------------------------------------------|
| Flashing red  (1)  | Outputs faulted    | One or more outputs are faulted, and may be in the fault state.          |
|                    | Inputs faulted     | One or more inputs are faulted, and may be in the fault state.           |
| Red                | Outputs forced off | One or more outputs are forced off (may be an unrecoverable fault).      |
|                    |                    | Input unrecoverable fault One or more inputs has an unrecoverable fault. |

## DeviceNet Module (MOD) Status Indicator

This bicolor (green/red) LED provides device status. It indicates whether or not the device has power and is operating properly.

| Condition Status   |                                                | Indication                                                                                                                    |
|--------------------|------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| Off                | No power                                       | No power applied to device.                                                                                                   |
| Green              | Device operational                             | Device is operating in a normal condition.                                                                                    |
| Flashing green (1) | Device in standby (device needs commissioning) | Device needs commissioning due to configuration missing, incomplete, or incorrect.                                            |
| Flashing red  (1)  | Recoverable fault                              | For example, the device’s scan list configuration does match the actual network configuration.                                |
| Red                | Unrecoverable fault                            | Device has an unrecoverable fault. Cycle power to your computer. If the problem persists, the device may need to be replaced. |
| Red                | Device self testing                            | Device is in self test. Refer to the DeviceNet Specification, Volume II, Identity Object.                                     |

## DeviceNet Network (NET) Status Indicator

This bicolor (green/red) LED indicates the status of the communication link.

| Condition Status   |                       | Indication                                                                                                                                                                                                                                                                                          |
|--------------------|-----------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Off                | Not powered           | Device is not online.                                                                                                                                                                                                                                                                               |
| Off                | Not online            | The device has not completed the Dup_MAC_ID test yet.                                                                                                                                                                                                                                               |
| Off                | Not online            | The device may not be powered; look at the Module Status LED.                                                                                                                                                                                                                                       |
| Flashing green (1) | Online                | Device is online, but has no connections in the established state.                                                                                                                                                                                                                                  |
| Flashing green (1) | Not connected         | The device has passed the Dup_MAC_ID test, is online, but has no established connections to other nodes.                                                                                                                                                                                            |
| Green              |                       | Link okay, online, connected The device is online and has connections in the established state.                                                                                                                                                                                                     |
| Flashing red  (1)  | Connection timeout    | One or more I/O connections are in the timed-out state.                                                                                                                                                                                                                                             |
| Red                | Critical link failure | Failed communication device. The device has detected an error that has rendered it incapable of communicating on the network (Duplicate MAC ID or Bus-off). Check network integrity and baud rate of all devices. Then cycle power to the card by shutting down and cycling power to your computer. |

<!-- image -->

Extensive use of Change-of-State connections, particularly with rapidly changing data, can adversely impact the available DeviceNet network bandwidth. If the network bandwith becomes consumed, some devices may only be able to communicate intermittently. This can result in timeout errors and possible loss of data. If timeouts occur, consider changing the connection type for some of the Change-of-State connections to Cyclic or Polled.

## Chapter Objectives

## Transfer Applications

## Create an ActiveSync Connection

## Upgrade Firmware

This chapter covers these topics:

-  Transfer applications
-  Create an ActiveSync connection
-  Upgrade terminal firmware
-  Upgrade operating system for CE terminals

You can transfer applications using a CompactFlash card or a computer.

PanelView Plus terminals let you copy or load applications in configuration mode using a CompactFlash card, see page 77 .

The PanelView Plus CE terminals let you copy or load applications using a CompactFlash card from Windows Explorer or FactoryTalk View ME configuration mode.

-  To copy files in terminal configuration mode, see page 77 .
-  To copy files in Windows Explorer, see page 115 .

For details on transferring .MER applications from a computer to the PanelView Plus or PanelView Plus CE terminals, refer to FactoryTalk View Studio help or documentation.

This section shows how to create an ActiveSync connection between a computer and a PanelView Plus CE terminal.

Creating an ActiveSync connection is a two-step process.

1. Create a partnership between the devices using a Serial connection.
2. When the partnership is created, you can then connect the devices using an Ethernet network.

## What You Need

-  Computer and a PanelView Plus CE terminal that are connected to an Ethernet network supporting DHCP.
-  ActiveSync software, version 3.7 or later, installed on computer. You can download ActiveSync from the http://www.microsoft.com web site.
-  2711-NC13 or 2706-NC13 serial cable for connecting the PanelView Plus CE terminal to the computer with ActiveSync installed.

<!-- image -->

## Create a Partnership with a Serial Connection

## IMPORTANT

To complete the ActiveSync installation, you must select the Serial Connection initially. After that you can switch between serial and Ethernet connections.

You must also make a valid ActiveSync connection at least once with the computer.

## Install ActiveSync on a Computer

1. Install ActiveSync, version 3.7 or later, on your computer.
2. Connect the PanelView Plus CE terminal to the computer with ActiveSync installed.

Use a 9-pin straight through cable (2711-NC13 or 2706-NC13) for a serial connection or an Ethernet cable.

3. Start ActiveSync.

You will see the Get Connected screen.

## Initiate Serial Connection on PanelView Plus CE Terminals

Select Start&gt;Menu&gt;Programs&gt;Microsoft ActiveSync&gt;Serial.

The Connecting to Async Connection dialog box appears.

## Find ActiveSync Connection and Create a Partnership on a Computer

1. When the Connecting to Async Connection dialog box appears on the PanelView Plus CE terminal, select the Next button on the Getting Connected screen of your computer.

If the Connecting to Async Connection dialog box closes before a connection is established, return to Initiating Connection from the PanelView Plus CE terminal.

2. Select Yes to create the new partnership.
2. When the ActiveSync connection is created, a window opens allowing you

to create a new partnership.

3. Enter the name and press Next.

ActiveSync will prompt you for a device name.

4. Press the Next button.

Select any options you want to synchronize.

5. Press the Next button and then the Finish button.

## Terminate Connection on PanelView Plus CE Terminals

1. Click the ActiveSync connection utility on the taskbar.

The Connection Status dialog box should appear.

## Firmware Upgrade Wizard

2. Press the Disconnect button to terminate the connection, may take 30 seconds.

## Connect via an Ethernet Connection

Now that a partnership is created using a serial connection, you can connect to the PanelView Plus CE using an Ethernet connection.

## ActiveSync Setup on a Computer

Verify that ActiveSync is configured to accept an Ethernet connection. By default, the Ethernet connection is enabled. (It is only necessary to enable the Ethernet connection if it is disabled).

## Connect with the Partnership on PanelView Plus CE Terminals

- 1.
- Select Start&gt;Programs&gt;Microsoft Active Sync&gt;Ethernet.

The ActiveSync dialog box opens. The name of the computer you connected to via the serial connection will appear.

2. Select Connect.

The Connection Status dialog box opens. It remains open as long as the ActiveSync connection is active.

Closing the dialog box will terminate the connection.

The Firmware Upgrade Wizard (FUW) lets you upgrade firmware in a PanelView Plus terminal. Using the FUW, you can:

-  create a firmware upgrade card (CompactFlash card) that you then load in the card slot of the terminal to upgrade firmware.
-  upgrade firmware in a terminal that is connected to your desktop computer using a Serial, Ethernet, or Network connection via RSLinx Enterprise software (for supported protocols).

The FUW is available in FactoryTalk View Studio software or with the Firmware Upgrade Kit.

## Upgrade Firmware with a CompactFlash Card

Before starting the Firmware Upgrade Wizard (FUW), follow these steps to prepare the terminal for a successful upgrade.

1. Backup all .MER files on the terminal to an external storage card or network.
2. Delete all applications on the terminal.
3. Record any Ethernet communication settings, such as IP address, subnet masks, and gateways by selecting Terminal Settings&gt;Networks and Communications&gt;Network Connections&gt;Network Adapters&gt;IP Address.
4. Disable the Auto-start feature on the terminal by selecting Startup Options&gt;FactoryTalk View ME Station Startup and select Go to Configuration Mode.
5. Reset the terminal.

This section shows how to upgrade the firmware in the terminal using a CompactFlash card. This is a two step-process. First, you create a firmware upgrade card with the necessary firmware files. Second, you load this card in the target terminal to upgrade the firmware.

## Create Firmware Upgrade Card

1. Start the Firmware Upgrade Wizard by selecting Start&gt;Rockwell Software&gt;RSView Enterprise&gt;Firmware Upgrade Wizard.
2. Select Create firmware upgrade card.
3.  In the Firmware card location text box, select the destination for the CompactFlash files (folder on the hard drive or physical location of the CompactFlash card, for example, E:\).
4.  From the Existing terminal list, select the type of terminal you are upgrading, then press Next.

<!-- image -->

3. From the Firmware source folder list, select the location of the firmware files.

The default location is C:\Program Files\Rockwell Software\RSView Enterprise\FUPs.

4. From the Upgrade firmware version list, select the version of the firmware you want to upgrade to, then press Next.
5. Select the appropriate KEPServer drivers and press Next.
3. If no KEPServer drivers are needed, just press Next.

<!-- image -->

<!-- image -->

<!-- image -->

If the selected FUP file does not support the KEPServer drivers, this dialog box will not appear.

6. Select Finish to copy the firmware source files to the location specified in step 2.

<!-- image -->

If the files were created in a separate folder on a local hard drive, copy the files to the root directory of the CompactFlash card.

<!-- image -->

## Upgrade Firmware in Terminal with Firmware Upgrade Card

1. Insert the CompactFlash card into the card slot of a powered terminal.

A dialog box indicates the firmware upgrade is about to occur.

<!-- image -->

2. Press Upgrade to begin the firmware upgrade.

## IMPORTANT

Do not remove the CompactFlash card while the upgrade is in process.

If other terminals exist on the same Ethernet network, the following error may display:

Error registering name on network (may be duplicate). Change in system Control Panel and try again.

## Upgrade Firmware with a Network (Ethernet) Connection

- 4.

Ignore this error. It will be corrected during the upgrade. Press OK to acknowledge error and wait for terminal to reset.

<!-- image -->

If a USB mouse is available, you can acknowledge this error by selecting OK.

3. On touch or touch-screen terminals, you must calibrate the touch screen by selecting pointers in all four corners of the screen and pressing the middle of the screen when prompted.

Ignore the following message if it appears. It means FactoryTalk View ME is being installed. Do not touch the two buttons that appear with this message.

Machine edition may be corrupted. Do you want to download firmware?

- Remove the card and press F8 or Exit to reset the terminal.

When the upgrade is complete, a dialog box appears requesting you to remove the CompactFlash card from the card slot.

<!-- image -->

Communication settings are cleared when the terminal is upgraded. If Ethernet communications is used, reconfigure the Ethernet communication settings using the values recorded when preparing the terminal.

5. Replace the .MER files that you backed up before starting the upgrade or download a new .MER file to the terminal.
6. Load the .MER file and run the project.

<!-- image -->

You can configure your application to start automatically on power cycle under Startup Options.

You can upgrade the firmware in a terminal that is connected to a desktop computer using a Serial, Ethernet, or Network with RSLinx Enterprise software connection.

-  Serial connection requires a RAS connection to be set up on computer. During the RAS setup, you select the COM port.
-  Ethernet connection requires that you enter the terminal's IP Address.
-  Network connection requires RSLinx Enterprise software where you select the terminal on an existing network.

Both the Serial and Ethernet connection requires the File Transfer Utility running on the terminal.

This section shows how to upgrade firmware in a terminal using a Network connection via Ethernet communications.

1. Start the Firmware Upgrade Wizard by selecting Start&gt;Rockwell Software&gt;FactoryTalk View Enterprise&gt;Firmware Upgrade Wizard.

<!-- image -->

2. Select Upgrade firmware on terminal and click k OK.
3. Select Network connection and click Next.
3. Use the Ethernet and Serial connections only if the firmware upgrade is unsuccessful.
4. Locate the terminal on your Ethernet network via its IP address. Skip to step 6 if you found the terminal. If you do not see the terminal,
5. right-click the Ethernet driver and add the device to the browse tree.

<!-- image -->

<!-- image -->

5. Double-click EthernetIP Devices and select the appropriate terminal and click OK.
6. Enter the IP address for the terminal and click OK.
7. Select the terminal to be upgraded and click OK.

<!-- image -->

<!-- image -->

<!-- image -->

8. From the Firmware source folder text box, select the location of the firmware files.

The default location is C:\Program Files\Rockwell Software\FactoryTalk View Enterprise\FUPs.

9. From the Upgrade firmware version list, select the version of the firmware you want to upgrade to, then click Next.
10. Select the appropriate KEPServer drivers and click Next. If no KEPServer drivers are needed, just click Next.

<!-- image -->

<!-- image -->

<!-- image -->

If the selected FUP file does not support the KEPServer drivers, this dialog box will not appear.

## 11. Click Finish to start the upgrade.

<!-- image -->

12. Click Yes to continue the upgrade process.

If the terminal was properly prepared for the upgrade, no applications should be running.

<!-- image -->

Firmware files are downloaded to the terminal. This may take several minutes to 15 minutes.

13. When the download is complete, click OK to reset the terminal.

<!-- image -->

If other terminals exist on the same Ethernet network, the following error may display:

Error registering name on network (may be duplicate). Change in system Control Panel and try again.

Ignore this error. It will be corrected during the upgrade. Press OK to acknowledge error and wait for terminal to reset.

<!-- image -->

If a USB mouse is available, you can acknowledge the error by selecting OK.

14. On touch or touch-screen terminals, you must calibrate the touch screen by selecting pointers in all four corners of the screen and pressing the middle of the screen when prompted.

Ignore the following message if it appears. It means FactoryTalk View ME is being installed. Do not touch the two buttons that appear with the message.

Machine edition may be corrupted. Do you want to download firmware? Communication settings are cleared when the terminal is upgraded. If Ethernet communications is used, reconfigure the Ethernet communication settings using the values recorded when preparing the terminal.

15. Replace the .MER files that you backed up before starting the upgrade or download the new .MER files to the terminal.
16. Load the .MER file and run the project.

TIP

You can configure your application to start automatically on power cycle under Startup Options.

## Upgrade the Operating System (OS)

The Operating System (OS) compressed binary image resides in a binary partition of the Internal (IDE) CompactFlash in the logic module for PanelView Plus CE terminals. There are two ways to upgrade the OS:.

-  External CompactFlash card during a reboot
-  LocalOSUpdate (LocalOSUpdate.exe)

## External CompactFlash Card

Follow these steps to upgrade the OS using an external CompactFlash card.

1. Copy the operating system binary file, SYSTEM.BIN, to a CompactFlash card.

The file must be named SYSTEM.BIN.

2. Remove power from the PanelView Plus CE terminal.
3. Insert the CompactFlash card into the external card slot on the terminal.
4. Cycle power to the PanelView Plus CE terminal.

The terminal automatically reboots with the new operating system.

## Local OS Update

1. Copy the operating system binary file to a CompactFlash card.
2. Insert the CompactFlash card into the external card slot of the PanelView Plus CE terminal.
3. At a CMD prompt on the PanelView Plus CE terminal, run: LocalOSUpdate &lt;Pathname and Filename&gt;

Example: LocalOSUpdate “\Storage card2\NewOS.BIN”

The terminal automatically reboots with the new operating system.

4. Verify the new operating system is loaded using the system application in the control panel.

## Load PanelView Plus CE Components

You can load PanelView Plus CE Components by using an:

-  ActiveSync connection.
-  external CompactFlash card.

## ActiveSync Connection

When the new operating system is running, load the PanelView Plus CE components as follows.

1. Establish an ActiveSync connection between your computer and the PanelView Plus CE terminal, using either a serial or Ethernet connection (Ethernet is recommended). Refer to page 189 .
2. Open the PanelView Plus CE Install Utility folder on the PanelView Plus CE Accessory CD and run the InstallFromActiveSync.exe program. This program lets you select which features to install and automatically copies the files from the CD to the PanelView Plus CE terminal. You must run the program from its directory to make sure the program locates all the files correctly.
3. Select the desired components from the list of available components. Use the &gt;&gt; button to install everything. Once installed, components can be optionally removed to free space in the \Storage Card folder.
4. When satisfied with the selections, click Install/Remove. Depending on the options selected and the speed of your ActiveSync connection, the download process may take several minutes. For a serial ActiveSync connection at 19.2 Kbps, the download time can be 30 minutes. When the download is complete, you will see the number of files copied or deleted.
5. Restart the PanelView Plus CE terminal.

## External CompactFlash Card

When the new operating system is running, load the PanelView Plus CE components as follows.

1. Open the PanelView Plus CE Install Utility folder on the PanelView Plus CE Accessory CD and copy the following to an FAT formatted CompactFlash card:
2.  InstallFromStorageCard.exe
3.  pvplusceinstall.ini
4.  Storage Card File folder
2. Insert the CompactFlash card into the external card slot on the terminal.
3. Using Windows Explorer, browse the \Storage Card folder and run InstallFromStorageCard.exe.
4. Select the desired components from the list of available components. Use the &gt;&gt; button to install everything. Once installed, components can be optionally removed to free space in the \Storage Card folder.
5. When satisfied with the selections, click Install/Remove. When the operation is complete, you will see a message box reporting the number of files installed (or removed).
6. Restart the PanelView Plus CE terminal.

## Chapter Objectives

## Status Indicators

## Troubleshoot the System

This chapter provides information on how to isolate and correct common operating problems with system components.

-  Status indicators
-  Isolate the problem
-  Startup error messages
-  Startup information messages
-  Startup sequence
-  Check terminal components
-  Ethernet connection
-  Application does not run
-  File system errors
-  System identification errors
-  Configuration mode access
-  Restart in safe mode

The terminals have two status indicators to isolate operating problems.

-  COMM indicator (green) for communication
-  FAULT indicator (red) for hardware faults

<!-- image -->

<!-- image -->

## Isolate the Problem

This section provides general troubleshooting information to assist you when trying to isolate problems.

## Check for Adequate Power

A terminal that does not receive adequate power could result in unpredictable behavior. Refer to Appendix A, Specifications, for power requirements.

## Check Indicators at Startup

After a successful startup, both status indicators on the terminal are off and controlled by the application running on the terminal.

When the terminal starts, the fault (red) indicator should be off except for a few brief flashes, and the comm (green) indicator on.

-  If the indicators on the 700 to 1500 terminals remain off, the power supply or logic module has failed. Check the power cable. If the power is not within range, replace the power supply. If the power is within range, replace the logic module.
-  If the indicators on the 400 and 600 terminals remain off, check the power cable.

## Indicator States If Terminal Stops During Startup

| Fault (Red) Indicator   | Comm (Green) Indicator   | Description                                                                                                                                              |
|-------------------------|--------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Blinking  (1)           | Off                      | Last firmware download failed. Reload firmware using Firmware Upgrade Wizard (FUW) utility.                                                              |
| Blinking  (1)           |                          | Blinking EBC boot loader firmware failed or is missing. Reload firmware using Firmware Upgrade Wizard (FUW) utility.                                     |
| Blinking  (1)           | On                       | Windows CE OS firmware failed or is missing. Reload firmware using Firmware Upgrade Wizard (FUW) utility.                                                |
| On (2)                  | Off                      | Fatal hardware error occurred. For the 700 to 1500 terminals, replace the logic module. For the 400 or 600 terminals, replace the terminal.              |
| On (2)                  |                          | Blinking Fatal hardware error in display. For the 700 to 1500 terminals, replace the display module. For the 400 or 600 terminals, replace the terminal. |

## Check the Startup Messages for Errors

Record any error message that displays during startup. Refer to Startup Error Messages on page 209 .

## Check Voltages and Temperatures

On the 700 to 1500 terminals, check the battery voltage and the display temperature.

-  Enter Configuration mode and select Terminal Settings&gt;System Information&gt;Terminal Information.
-  For PanelView Plus CE terminals, you can also open the Hardware Monitor control panel application.

The battery voltage must be at least 2.75V DC. Replace the battery if the voltage is less than 2.75V DC.

The display temperatures should be less than 55 °C (131 °F). The CPU temperature should be less than 95 °C. If the temperatures are higher, check for obstructed airflow in the chassis and attempt to moderate the ambient temperatures within the enclosure and surroundings.

## Check the System Event Log

Check the system event log for errors or unexpected reboots.

-  Enter Configuration mode and select Terminal Settings&gt;System Event Log.
-  For PanelView Plus CE terminals, you can also open the Hardware Monitor control application and select the Event Log tab.

## Perform Extended Diagnostics

Use extended diagnostics on the 700 to 1500 terminals to perform more extensive hardware testing at startup.

-  Enter Configuration mode and select Terminal Settings&gt;Startup Tests&gt;Select Tests.
-  For PanelView Plus CE terminals, you can also open the Extended Diagnostics control panel application.

Select one or more of the tests you want to run. Enable extended diagnostics and set the iteration or repeat count. Restart the terminal. The serial port test requires a loopback connector with these connections.

<!-- image -->

Extended diagnostics are performed at every startup until disabled. A failure will momentarily halt startup and display an error message.

Startup Information Messages Startup messages display in a specific sequence on the terminal during startup and
illdilffdThidih typically display for a few seconds. These messages indicate the startup sequence of the terminal, but do not require that you perform any action.

|          | Message # Displayed Message   | Description                                                                                                                                                                                                                 |
|----------|-------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 37 (1)   | Video Initialized             | Configures and initializes the graphics video system.                                                                                                                                                                       |
|          | 30 Watchdog Test              | Tests the watchdog circuitry to verify system integrity.                                                                                                                                                                    |
|          | 1 RAM Test                    | Tests the RAM memory.                                                                                                                                                                                                       |
| 31 (1)   | Stuck Key                     | Checks the integrity of the function key hardware.                                                                                                                                                                          |
| 31.5 (1) | Stuck Touch                   | Checks the integrity of the touch screen hardware.                                                                                                                                                                          |
| 32 (1)   | Battery Test                  | Checks the integrity of the battery hardware.                                                                                                                                                                               |
| 2.5 (1)  | Registry Search               | Locates and loads the most recent, valid registry. Multiple copies of the registry are maintained. If power is lost during a registry update, a valid registry is available the next time power is applied to the terminal. |
|          | 2 Image Search                | Checks for new OS firmware upgrade on the external CompactFlash card and the serial port.                                                                                                                                   |
| 11 (2)   | Downloading Image             | Downloads a new OS firmware upgrade to internal RAM. Message may remain on screen for several minutes.                                                                                                                      |
| 50 (1)   |                               | External CF Transfers a new OS firmware upgrade from the external CompactFlash card to the terminal. Message may display for several minutes.                                                                               |
| 20 (2)   | Transfer Image                | Programs the OS firmware just downloaded into RAM. Message may remain on screen for several minutes.                                                                                                                        |
| 23 (1)   | Internal CF                   | Programs the OS firmware just downloaded into the internal flash memory. Message may display for several minutes.                                                                                                           |
|          | 24 CRC Check                  | Checks the integrity of the OS firmware.                                                                                                                                                                                    |
| 27 (2)   | Decompress System             | Decompresses the compressed OS firmware into RAM.                                                                                                                                                                           |
|          | 28 Starting System            | Launches the operating system (OS).                                                                                                                                                                                         |
|          | 29 System Check ###           | Checks internal file system integrity (### is percent progress indicator).                                                                                                                                                  |
|          | 29.1 System Check             | Disables internal file system integrity check. Contact technical support.                                                                                                                                                   |

## Startup Sequence

This flow chart provides a sequence of startup operations for the terminal and shows system information messages that are displayed on the terminal.

<!-- image -->

## Startup Error Messages

When an error occurs, the terminal displays the error number with a text message. The word ERROR! appears under this line in different languages.

# Displayed Message ERROR! FEHLER! ERREUR! ERRORE!

|          | Error # Displayed Message   | Description                                                           | Recommended Corrective Action                                                                                                                                                               |
|----------|-----------------------------|-----------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|          | 1 RAM Test                  | RAM Test failure                                                      | Reset the terminal. 400 and 600: If error persists, replace the terminal. 700 to 1500: If error persists, reseat the SO-DIMM RAM module. If error still persists, replace the logic module. |
| 14 (1)   | RAM Header Check            | OS firmware that is downloading is not compatible with hardware.      | Check that you are using the correct version and type of firmware upgrade. Reset the terminal and upgrade with the correct firmware version.                                                |
| 20 (1)   | Transfer Image              | Programming the downloaded OS firmware into flash failed.             | Reset the terminal and attempt the firmware upgrade again. If error persists, replace the terminal.                                                                                         |
| 23       | Download Task (1)           | OS firmware that is downloading to the terminal is too large.         | Check that you are using the correct version and type of firmware upgrade. Reset the terminal and upgrade with the correct firmware version.                                                |
| 23       | Internal CF (2)             | Error programming the new OS firmware to internal CompactFlash.       | Reload the firmware. If error persists, replace the internal CompactFlash. If error still persists, replace the logic module.                                                               |
|          |                             | 24 CRC Check Checksum of the OS firmware failed. Reload the firmware. | 400 and 600: If error persists, replace the terminal. 700 to 1500: If error persists, replace the internal CompactFlash card. If error still persists, replace the logic module.            |
| 25 (1)   | Invalid Prod Family         | OS firmware that is downloading is not compatible with terminal.      | Check that you are using the correct version and type of firmware upgrade. Reset the terminal and upgrade with the correct firmware version.                                                |
| 27 (1)   | Decompress System           | Error decompressing the OS firmware from flash to RAM.                | Reload the firmware. If error persists, replace the terminal.                                                                                                                               |
|          | 30 Watchdog Test            | Watchdog test failure                                                 | Reload the firmware. 400 and 600: If error persists, replace the terminal. 700 to 1500: If error persists, replace the logic module.                                                        |
|          | 31 Stuck Key                | Function key failure                                                  | Check that nothing is pressed against a key. Reset the terminal without key presses. If error persists, replace display module.                                                             |
| 31.5 (2) | Stuck Touch                 | Touch screen failure                                                  | Check that nothing is pressed against the touch screen. Reset the terminal without touch screen presses. If error persists, replace the display module.                                     |
| 32 (2)   | Battery Test                | Battery failure                                                       | Replace the battery. If error persists, replace the logic module.                                                                                                                           |
| 33.5 (2) | NVRAM Access                | Nonvolatile memory failure                                            | Upgrade the system firmware to revision 3.10.03 or later.                                                                                                                                   |
| 3a (1)   | Stuck Touch                 | Touch screen failure                                                  | Check that nothing is pressed against the touch screen. Reset the terminal without touch screen presses. If error persists, replace the terminal.                                           |
|          | 40 EXE Check                | System OS firmware is missing or corrupt. Reload the firmware.        | 400 and 600: If error persists, replace the terminal. 700 to 1500: If error persists, replace the internal CompactFlash card. If error still persists, replace the logic module.            |
| 50 (2)   | External CF                 | Error loading the OS firmware from the external CompactFlash card.    | Reload the firmware. If error persists, replace the external CompactFlash card and attempt the firmware upgrade again.                                                                      |

## Check Terminal Components

This section provides tips on how to isolate problems with the display, touch screen, keypad, attached keyboard, or mouse. If you are unable to resolve the problem, replace the display.

## Resolve Problems with Display

| Symptom                                                           | Recommended Action (1)                                                                                                                                                                                                                                                                             | Page   |
|-------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|
|                                                                   | The display is dim or unreadable. Check the brightness setting on 700 to 1500 displays.   Enter Configuration mode and select Terminal Settings>Display>Display Intensity.   On PanelView Plus CE devices, you can also open the Display control panel application and select the Backlight tab. | 80 129 |
|                                                                   | Check the contrast setting on 400 or 600 grayscale terminals.   Enter Configuration mode, and select Terminal Settings>Display>Display Contrast.                                                                                                                                                  | 79     |
| The backlight is turning off or dimming the display unexpectedly. | Check the screen saver settings.   Enter Configuration mode and select Terminal Settings>Display>Screen Saver.   On PanelView Plus CE devices, you can also open the Display control panel application and select the Screen Saver tab.                                                          | 80 129 |
| A startup error appears during startup.                           | Record the message and check the startup error messages table.                                                                                                                                                                                                                                     | 211    |

## Resolve Problems with Touch Screen

| Problem                                                                  | Recommended Action (1)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Page   |
|--------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|
| The touch screen is not operating correctly. Calibrate the touch screen. |   Enter Configuration mode and select Terminal Settings>Input Devices>Touch Screen>Calibration.   On PanelView Plus CE devices, you can also open the Touch control panel application and select the Calibration tab. The calibration requires four user screen touches. When the touches do not converge to a satisfactory calibration, you are asked repeatedly for additional screen touches; the calibration process never terminates. A touch screen that does not calibrate is not present or not functioning properly. Replace the 700 to 1500 display module or the 400 to 600 terminal. | 86 124 |
| The display may not have a touch screen.                                 | Check the catalog number of the unit. Verify that your terminal has a touch screen by looking at the label on the terminal.                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |        |

| Problem                                                                                                   | Recommended Action (1)                                                                                                                                                                                                                                                                                                                                            | Page   |
|-----------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|
|                                                                                                           | The screen cursor is not visible. Verify that the cursor is enabled.   Enter Configuration mode and select Terminal Settings>Input Devices>Touch Screen>Cursor.   In PanelView Plus CE, open the Display control panel application and select the Cursor tab.                                                                                                   | 87 129 |
|                                                                                                           | The touch screen does not accept touch input. Attach a USB mouse to check whether the problem is with the touch screen or the application.   If the mouse works, but the touch screen does not, then the touch driver or touch screen is not functioning properly.   If both the mouse and the touch screen are not working, then it is an application problem. |        |
| Touch input and dragging is inaccurate. The touch screen is present and working but requires calibration. | Calibrate the touch screen.   Enter Configuration mode and select Terminal Settings>Input Devices>Touch Screen>Calibration.   On PanelView Plus CE devices, you can also open the Touch control panel application and select the Calibration tab.                                                                                                               | 86 124 |

## Resolve Problems with Keypad

| Problem                                                                                                                                                                                                            | Recommended Action (1)                                                                                                                                                                                                                                                                                                         | Page   |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|
| The hold-off delay may be longer than expected or multiple key presses might be inhibited by multi-key lockout. Home, End, Page Up or Page Down are not supported when single key or multi-key lockout is enabled. | Check keypad settings.   Enter Configuration mode and select Terminal Settings>Input Devices>Keypad.   On PanelView Plus CE devices, you can also open the Keypad control panel application.                                                                                                                                 | 85 127 |
| The keypad is not accepting key input.                                                                                                                                                                             | Check the key input by attaching a USB keyboard.   If the keyboard works, but the keypad does not, then the keypad driver or keypad is not working.   If both the keypad and keyboard are not working, then the problem may be the application.                                                                              |        |
| Keys on the keypad of a PanelView Plus CE terminal are not mapped correctly.                                                                                                                                       | Check the keypad mapping.   You can remap or disable the keys on the PanelView Plus CE terminal can using the Keypad Configuration Utility (KCU). Use the KCU to check the current keypad configuration.   Restart in Safe mode to use the default keypad mappings.                                                          |        |
| On PanelView Plus CE terminals, problems with keypad input may be the fault of the application.                                                                                                                    | On PanelView Plus CE terminals only:   Press a key outside the application such as an edit box in the shell. If the keypad works outside the application, then the application is at fault.   Press Ctrl+Esc simultaneously to open the Start menu, cursor to run, type numbers and viewable characters into the Run dialog. |        |

## Resolve Problems with Mouse

| Problem Recommended Action Page                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |               |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------|
| The mouse is not operating correctly. Check the USB cable and connection. Detach and then reattach the mouse. Cycle power to the terminal.                                                                                                                                                                                                                                                                                                                                                                           |               |
| The screen cursor may not be visible or the mouse settings may need adjusting. Check if the screen cursor is disabled:   Enter Configuration mode and select Terminal Settings>Input Devices>Touch Screen>Cursor.   For a PanelView Plus CE terminal, you can also open the Display control panel application. Check the mouse settings.   Enter Configuration mode and select Terminal Settings>Input Devices>Mouse.   For a PanelView Plus CE terminal, you can also open the Mouse control panel application. | 87 128 85 127 |
| The mouse is a keyboard/mouse USB composite device. Attach a standalone USB mouse.                                                                                                                                                                                                                                                                                                                                                                                                                                   |               |
| The USB mouse may not be working or noncompliant. Replace the USB mouse. Try a different model or manufacturer. If attaching a new mouse resolves the problem, then the old mouse was not working or noncompliant. Refer to Appendix B for a list of valid USB devices that are compatible with the terminal. You can also check the Knowledgebase at http://support.rockwellautomation.com for a list of USB compatible devices.                                                                                    | 227           |

## Resolve Problems with Keyboard

| Problem                                                                                           | Recommended Action                                                                                                                                                                                                                                                                                                                                                                                                       | Page   |
|---------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|
| The keyboard does not work.                                                                       | Check the USB cable and connector. Detach and reattach the keyboard. Verify a good connection. Cycle power to the terminal.                                                                                                                                                                                                                                                                                              |        |
| Keyboard keys may not be enabled as expected. Check for enabled Alt-Ctrl keys.                    |   Enter Configuration mode and select Terminal Settings>Input Devices>Keyboard.                                                                                                                                                                                                                                                                                                                                         | 84     |
| The keyboard is not accepting key input.                                                          | Check the key input using the keypad.   If the keypad works, but the keyboard does not, then the keyboard driver or keyboard is not working.   If both the keypad and keyboard are not working, then the problem is probably with the application.                                                                                                                                                                     |        |
| On PanelView Plus CE terminals, problems with keyboard input may be the fault of the application. | On PanelView Plus CE terminals only:   Press a key outside the application such as an edit box in the shell. If the keypad works outside the application, then the application is at fault.   Press Ctrl+Esc simultaneously to open the Start menu, cursor to run, type numbers and viewable characters into the Run dialog.                                                                                           |        |
| The keyboard is a keyboard/mouse USB composite device.                                            | Attach a standalone USB keyboard.                                                                                                                                                                                                                                                                                                                                                                                        |        |
|                                                                                                   | The USB keyboard may not be a compliant device. Replace the USB keyboard. Try a different model or manufacturer. If a new keyboard resolves the problem, then the old keyboard was probably noncompliant. Refer to Appendix B for a list of valid USB devices that are compatible with the terminal. You can also check the Knowledgebase at http://support.rockwellautomation.com for a list of compatible USB devices. | 227    |

## Ethernet Connnection

This section provides tips on how to isolate Ethernet problems.

-  Check the status indicators at the Ethernet connector. Green indicates a communication link and should be ON. Amber indicates data activity and should be flashing. Verify that there is a connection to the hub.
-  Check the cable connections and quality of cable. Check for good connections and things such as quality, crimping, hub connection, and uplink ports.
-  Check the IP Address of the Built-in Ethernet Controller. Enter Configuration mode and select Terminal Settings&gt;Networks and Communications&gt;Network Connections&gt;Network Adapters. In PanelView Plus CE, open the Network and Dial-up Connections control panel application

If DHCP is enabled, the device expects a valid IP address to be acquired within a several seconds after startup. The TCP/IP protocol automatically assigns 169.254.nnn.nnn when it fails to acquire an IP address from the server. In general, an IP address that begins with 169 will not support a network connection.

A bad Ethernet connection and the absence of a valid IP address are typically reported in a Communication error message box with the Winsock critical error 10065 - No route to host.

-  Check for conflicting IP addresses. If DHCP is not enabled, make sure the IP address you specify is not in conflict with the address of another device on the network.
-  Check the device name of the terminal. Do not allow devices on the network with same host name. Enter Configuration mode and select Terminal Settings&gt;Communications and Networks&gt;Network Connections&gt;Device Name. In PanelView Plus CE, open the System control panel application
-  Contact your Network Administrator to check peer or server settings . The other side of the Ethernet connection may also be a problem.
-  Use the network utilities Ping.exe and Ipconfig.exe (CE Terminals only)
-  Check the requirements of network applications (CE Terminals only). Network applications may have specific requirements such as Proxy Settings for Internet Explorer and Ethernet Configuration for ActiveSync. In PanelView Plus CE, open the Communications control panel application.
-  Check the multi-homed devices (CE terminals only). Multi-homed (more than one Ethernet node) devices have the same issues as those above but with more potential for confusion and ambiguity. Keep the Network connections as simple as possible.

## Application Does Not Run

## Configuration Mode Access

## File System Errors

If the PanelView Plus application does not start, there may be a problem with the .MER FactoryTalk View ME file. Check for a startup screen and compatible version.

If a PanelView Plus application does not run on the terminal, there may be a problem with the FactoryTalk View ME application. Verify that a startup screen was configured and that the runtime file is a compatible version.

If a PanelView Plus CE application does not run at startup, try to run the application manually. If the application runs manually, then the operating system may be starting up with an invalid shortcut path. Check the shortcuts in the folder:

\Storage Card\Windows\StartUp

Check the syntax of each shortcut path in the Startup folder and verify that a valid target application exists.

Check that the application is not missing components or required DLLs. Remove and reload the application.

To access Configuration mode while an application is running, your FactoryTalk View ME application must contain a screen with a Goto Configure Mode button. When the application is running, you can press this button to access Configuration mode.

If a running application does not contain a Goto Configure Mode button, you can access configuration mode during startup.

1. Restart the terminal.

The terminal goes through its startup sequence and will display a white box in the lower left corner of the display.

2. On touch screen terminals, press the white box.

On keypad terminals, press the F1 key.

The terminal enters Configuration Mode.

TIP

If the terminal is configured to enter Configuration mode at startup and does not, then reload the firmware.

The file system on PanelView Plus CE terminals is checked at startup and errors are reported in a message box. Record the error information and always elect to correct the problem. Typically, the message box will reappear until the error is corrected.

## Advanced Diagnostics for CE Terminals

File system errors are rare and can usually be corrected. The most common cause of lost clusters and file/directory size mismatches within a FAT file system is an unexpected power outage while writing to the file system. Always stop applications before removing power so that data is cleanly flushed out to the file system and the file system is brought to an orderly stop.

Although the FactoryTalk View ME application runs from RAM, applications such as data and event logging, and historical trending, write to flash memory and should be stopped before removing power.

Ping and ipconfig are invaluable for network debugging along with some knowledge of IP and the Winsock error codes.

-  Try to ping the destination host.
-  Check the destination address.
-  Check whether you have a router configured in your network system (your WinSock implementation).
-  Use the tracert command at the command prompt on the desktop to try and determine where the failure occurs along the route between your host and the destination host.
-  Some utility programs are distributed on the Accessories CD. Others can be developed using the software development kit (SDK).
-  Take advantage of alternate connectivity - mouse versus touch screen, keyboard versus keypad, serial communication, and alternate Ethernet connections.
-  Enable the crash logger and examine the EXCEPTIONS.LOG file from the PanelView Plus CE terminal when suspecting an operating system or application crash.
-  Store the current operating system on an external CompactFlash card. You can then use this card to update the terminal in case the operating system is out-of-date or corrupted.
-  Store Autorun.exe utilities on an external CompactFlash card that can be easily run by inserting the card in the external CompactFlash card slot of the terminal.
-  Know useful keyboard shortcuts so that you can navigate around the system without a mouse or touch screen.
-  Check the event log in the Hardware Monitor control panel application or under Terminal Settings&gt;System Event Log in Configuration mode. Look for error conditions or reasons for unexpected reboots.
-  Check the configuration settings in the PanelView Plus CE control panel applications or terminal Configuration mode.

## System Identification Errors

The error messages in this section appear on startup if incorrect or invalid components are used with the 700 to 1500 terminals.

<!-- image -->

Terminals manufactured after January 2007 switch displays without displaying the following error messages.

-  This dialog appears if a PanelView Plus CE logic module is attached to a PanelView display module. We recommend that you use a PanelView Plus CE display module with a PanelView Plus CE logic module. This is a warning letting you continue to operate.
-  This dialog appears if the PanelView Plus logic module contains a 2711P-RWx internal CompactFlash card for the PanelView Plus CE terminal.

<!-- image -->

<!-- image -->

After pressing OK, you will be asked to power off the terminal and insert a valid 2711P-RWx internal CompactFlash card for the PanelView Plus terminal.

-  This dialog appears if the PanelView Plus CE logic module contains a 2711P-RWx internal CompactFlash card for the PanelView Plus terminal.

<!-- image -->

After clicking OK, you will be asked to power off the terminal and insert a valid 2711P-RWx internal CompactFlash card for the PanelView Plus CE terminal.

-  This dialog appears if the internal CompactFlash in the PanelView Plus logic module is corrupt. This is a fatal error.

<!-- image -->

After clicking OK, you will be asked to power off the terminal and insert a valid 2711P-RWx internal CompactFlash card.

## Restart in Safe Mode

On PanelView Plus CE terminals, use the default switch with the reset switch to start the terminal in Safe mode. This diagnostic mode reduces the system to a known state that permits recovery from a software problem. Safe mode ignores all user changes to the system and avoids any problems that are due to interactions with end-user software or changes. Once the system is running in Safe mode, you can repair the offending applications or changes that caused the problem.

When the PanelView Plus CE terminal is restarted in Safe mode, the following occurs:

-  The Persistent Registry is ignored and the Default Registry is used. The Persistent Registry is restored at the next reboot unless the Default Registry is saved (flushed), in which case it becomes the new Persistent Registry.
-  The \Windows\Startup folder is ignored, inhibiting most startup actions. All user applications that launch automatically at startup are shortcuts in the \Startup folder.
-  Depending on the state of the system, the touch screen may be calibrated at startup.
-  All custom key configurations (mappings) generated by the Keypad Configuration Utility (KCU) are ignored.

The switches that control safe mode are on the right side of the logic module above the CompactFlash card slot.

Follow these steps to restart in Safe mode.

1. Insert a thin probe into the hole marked default and press the switch.
2. Insert the probe into the hole marked reset and press the switch. The system will restart immediately into the Safe mode.

If you restart the PanelView Plus terminal in safe mode:

1. The default operating system registry is loaded.
2. The operating system boots but FactoryTalk View ME software is not started.
3. The operating system displays the ME may be corrupt diagnostic screen. Disregard this message. FactoryTalk View ME software is not corrupt; it has not been loaded on this boot cycle.
4. The next time you reset or power up the terminal, the system will start normally and run FactoryTalk View ME software.

TIP

Safe mode indicates that the terminal passes all startup self tests and can successfully launch the operating system. Safe mode is not a diagnostic function for the FactoryTalk View ME application.

## Chapter Objectives

## Clean the Display Window

## Disposal Information

## Maintenance

This chapter provides information on the following topics:

-  Clean the display
-  Disposal information

Use a protective antiglare overlay for easier cleaning of the display window.

## ATTENTION

<!-- image -->

Use of abrasive cleaners or solvents may damage the display. Do not scrub or use brushes.

Follow these steps to clean the display window.

1. Disconnect power from the terminal at the power source.
2. Use a clean sponge or soft cloth with a mild soap or detergent to clean the display.
3. Dry the display with a chamois or moist cellulose sponge to avoid water spots.

Remove fresh paint splashes and grease before drying by rubbing lightly with isopropyl alcohol (70% concentration). Afterward, wash using a mild soap or detergent. Rinse with clean water.

This section contains disposal information for the backlight assembly and the lithium battery in the 400 and 600 terminals.

## Backlight Assembly Disposal

## ATTENTION

<!-- image -->

The backlight assembly of 600 to 1500 terminals contains mercury. At the end of its life, this equipment should be collected separately from any unsorted municipal waste.

## Battery Removal

The lithium battery in the 400 and 600 is non-replaceable and should be removed only at the end of product life.

<!-- image -->

This product contains a hermetically sealed lithium battery which is permanently connected and should be removed only by trained professionals.

At the end of its life, the battery contained in this product should be collected separately from any unsorted municipal waste.

The collection and recycling of batteries helps protect the environment and contributes to the conservation of natural resources as valuable materials are recovered.

Follow these steps to remove the battery on the 400 and 600 terminals.

1. Disconnect power from the terminal.
2. Place the terminal, display side down, on a flat stable surface.
3. Detach the communication module, if attached, from the logic module by removing the three screws.
4. Unlatch the eight retaining tabs (two on each side) on the back cover and remove cover.
5. Locate the yellow battery on the logic board.
6. Remove the battery.

<!-- image -->

For information on battery replacement or removal for 700 to 1500 terminals, see Replace the Battery on page 151 .

## Electrical

## Environmental

## Specifications

| Attribute                    | Value                        |
|------------------------------|------------------------------|
| 400 and 600                  |                              |
| Input voltage, DC            | 24V DC nom (18…30V DC)       |
| Power consumption, DC        | 25 W max (1.0 A at 24V DC)   |
| 700 to 1500                  |                              |
| Input voltage, DC            | 24V DC nom (18…32V DC)       |
| Power consumption, DC        | 70 W max (2.9 A at 24V DC)   |
|                              | 39 W typical (1.6A @ 24V DC) |
| 400 and 600                  |                              |
| Input voltage, AC            | 85…264V AC                   |
| Line frequency               | 47…63 Hz                     |
| Power consumption, AC        | 60V A max                    |
| 700 to 1500                  |                              |
| Input voltage, AC            | 85…264V AC                   |
| Line frequency               | 47…63 Hz                     |
| Power consumption, AC        | 160V A max, 65 VA typical    |
| Remote power 700 to 1500     |                              |
| Input voltage, AC            | 85…264V AC                   |
| Line frequency               | 47…63 Hz                     |
| Power consumption, AC        | 120V A max                   |
| PCI slot max available power |                              |
| Supply, DC                   | 11 W                         |
| Supply, AC                   | 5 W                          |

| Attribute                                | Value                      |
|------------------------------------------|----------------------------|
| Temperature, operating                   | 0…55 °C (32…131 °F)        |
| Temperature, non-operating               | -25…70 °C (-13…158 °F)     |
| Heat dissipation 400 and 600 700 to 1500 | 85 BTU/hr 240 BTU/hr       |
| Relative humidity                        | 5…95% without condensation |
| Altitude, operating                      | 2000 m (6561 ft)           |
| Shock, operating                         | 15 g at 11 ms              |
| Shock, nonoperating                      | 30 g at 11 ms              |

<!-- image -->

## Display

| Vibration             | 10…57 Hz, 0.012 pk-pk displacement 57…500 Hz, 2 g pk acceleration                                                    |
|-----------------------|----------------------------------------------------------------------------------------------------------------------|
| Enclosure Ratings     | NEMA Type 12, 13, 4X (Indoor use only), IP54, IP65                                                                   |
| Airborne Contaminants | For PVP/PVP-CE conformal-coated PCBA level products: ANSI/ISA S71.04 - 1985 Severity Level G3 EN60654-4:1998 Class 3 |

| Attribute                                                                                                                                                          | Value                                                                                                                                                   |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| Display type 400 and 600 grayscale 400…1500 color                                                                                                                  | Grayscale passive matrix, film compensated super-twist nematic (FSTN) Color active matrix, thin-film transistor (TFT) with liquid crystal display (LCD) |
| Display size, diagonal 400 grayscale 400 color 600 700 1000 1250 and 1250 high-bright 1500                                                                         | 3.8 in. 3.5 in. 5.5 in. 6.5 in. 10.4 in. 12.1 in. 15.0 in.                                                                                              |
| 400 grayscale 400 color 600 grayscale and color 700 1000 1250 and 1250 high-bright 1500 Resolution 600 700 1000 1250 and 1250 high-bright 1500 Luminance (typical) | 77 x 58 mm (3.0 x 2.3 in.) 320 x 240 320 x 240 640 x 480                                                                                                |
|                                                                                                                                                                    | 71 x 53 mm (2.8 x 2.1 in.) 112 x 84 mm (4.4 x 3.3 in.) 132 x 99 mm (5.2 x 3.9 in.) 211 x 158 mm (8.3 x 6.2 in.) 246 x 184 mm (9.7 x 7.2 in.)            |
|                                                                                                                                                                    | 1024 x 768 120 cd/m 2 Nits                                                                                                                              |
|                                                                                                                                                                    | 200 cd/m 2 Nits 300 cd/m 2 Nits 2                                                                                                                       |
| 400 grayscale 400 color                                                                                                                                            | Nits                                                                                                                                                    |
| 600                                                                                                                                                                | 300 cd/m                                                                                                                                                |
| 700 to 1500                                                                                                                                                        | 2                                                                                                                                                       |
|                                                                                                                                                                    | 304 x 228 mm (12.0 x 9.0 in.)                                                                                                                           |
| 400 grayscale and 400 color                                                                                                                                        |                                                                                                                                                         |
|                                                                                                                                                                    | 640 x 480                                                                                                                                               |
|                                                                                                                                                                    | 800 x 600                                                                                                                                               |
| 1250 high-bright                                                                                                                                                   | 1000 cd/m Nits                                                                                                                                          |

## Mechanical

| Backlight 400 600…1500 1250 High-bright                   | LED CCFL 50,000 hours life, min. Backlight not replaceable    |
|-----------------------------------------------------------|---------------------------------------------------------------|
| Touch screen Actuation rating Operating force             | Analog resistive 1 million presses 10…110 g                   |
| Keypad function keys (1) Actuation rating Operating force | Function keys, numeric and navigation 1 million presses 340 g |

| Attribute                                                                                                                                                                                                                                                                                | Value                                                                                                                                                                            |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Weight, approx., HxWxD (for base unit without modules)                                                                                                                                                                                                                                   | Weight, approx., HxWxD (for base unit without modules)                                                                                                                           |
| 400 keypad (1)  or keypad and touch 600 keypad or keypad and touch (1) 600 touch(1) 700 keypad or keypad and touch 700 Touch 1000 keypad or keypad and touch 1000 touch 1250 keypad or keypad and touch 1250 touch and 1250 high-bright touch 1500 keypad or keypad and touch 1500 touch | 562 g (1.24 lb) 930 g (2.05 lb) 789 g (1.74 lb) 1.9 kg (4.2 lb) 1.7 kg (3.8 lb) 2.9 kg (6.3 lb) 2.6 kg (5.7 lb) 3.4 kg (7.6 lb) 3.2 kg (7.1 lb) 4.6 kg (10.0 lb) 4.2 kg (9.3 lb) |
| Dimensions, approx. HxWxD (for base unit without communication module)                                                                                                                                                                                                                   | Dimensions, approx. HxWxD (for base unit without communication module)                                                                                                           |
|                                                                                                                                                                                                                                                                                          | 400 keypad or keypad and touch 152 x 185 x 90 mm (6.0 x 7.28 x 3.54 in.)                                                                                                         |
|                                                                                                                                                                                                                                                                                          | 600 keypad or keypad and touch 167 x 266 x 98 mm (6.58 x 10.47 x 3.86 in.)                                                                                                       |
|                                                                                                                                                                                                                                                                                          | 600 touch 152 x 185 x 98 mm (6.0 x 7.28 x 3.86 in.)                                                                                                                              |
|                                                                                                                                                                                                                                                                                          | 700 keypad or keypad and touch 193 x 290 x 55 mm (7.58 x 11.40 x 2.18 in.)                                                                                                       |
|                                                                                                                                                                                                                                                                                          | 700 touch 179 x 246 x 55 mm (7.04 x 9.68 x 2.18 in.)                                                                                                                             |
|                                                                                                                                                                                                                                                                                          | 1000 keypad or keypad and touch 248 x 399 x 55 mm (9.77 x 15.72 x 2.18 in.)                                                                                                      |
|                                                                                                                                                                                                                                                                                          | 1000 touch 248 x 329 x 55 mm (9.77 x 12.97 x 2.18 in.)                                                                                                                           |
|                                                                                                                                                                                                                                                                                          | 1250 keypad or keypad and touch 282 x 416 x 55 mm (11.12 x 16.36 x 2.18 in.)                                                                                                     |
|                                                                                                                                                                                                                                                                                          | 1250 touch 282 x 363 x 55 mm (11.12 x 14.30 x 2.18 in.)                                                                                                                          |
|                                                                                                                                                                                                                                                                                          | 1250 touch High-bright 282 x 363 x 74 mm (11.12 x 14.30 x 2.90 in.)                                                                                                              |
|                                                                                                                                                                                                                                                                                          | 1500 keypad or keypad and touch 330 x 469 x 65 mm (12.97 x 18.46 x 2.55 in.)                                                                                                     |
|                                                                                                                                                                                                                                                                                          | 1500 touch 330 x 416 x 65 mm (12.97 x 16.37 x 2.55 in.)                                                                                                                          |

## General

## Agency Certifications

| Attribute                                                                                                                                                                                                                                                                    | Value                                                       |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------|
| Battery life 400 and 600 700 to 1500                                                                                                                                                                                                                                         | 5 years min. at 25 °C (77 °F) 4 years min. at 25 °C (77 °F) |
| Clock                                                                                                                                                                                                                                                                        | Battery-backed, +/-2 minutes per month                      |
| LED indicators                                                                                                                                                                                                                                                               | COMM (Green), Fault (Red)                                   |
| Application flash memory 400 and 600, series A 400 and 600, series B or later 700 to 1500 logic modules, series A to D 700 to 1500 logic modules, series E or later 2711P-RW1 2711P-RW2 2711P-RW3 700-1500 CE logic modules, series E or later 2711P-RW6 2711P-RW7 2711P-RW8 | 5 MB 10 MB 20 MB 26 MB 72 MB 195 MB 80 MB 203 MB 446 MB     |
| External CompactFlash storage                                                                                                                                                                                                                                                | 512 MB max                                                  |

| Certifications (1)   | Value                                                                                                                                                                                                                                                                                          |
|----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                      | c-UL-us UL Listed Industrial Control Equipment, certified for use in US and Canada. See File E10314. UL Listed Industrial Control Equipment for use in:   Class I, Div 2, Group A, B, C, D   Class I, Zone 2, Group IIC  (2)   Class II, Div 2 Groups F, G   Class III Hazardous Locations |
| CE (EMC)             | European Union 2004/108/EC Directive, compliant with: EN 61000-6-2; Industrial Immunity EN 61000-6-4; Industrial Emissions                                                                                                                                                                     |
| CE (LVD)             | European Union 2006/95/EC Low Voltage Directive, compliant with: EN 61131-2; Programmable Controllers                                                                                                                                                                                          |
| C-Tick               | Australian Radiocommunications Act, compliant with: AS/NZS CISPR 11; Industrial Emissions                                                                                                                                                                                                      |
| Marine (1)           | Products identified with the suffix M in the catalog number, are certified to the requirements of one or more marine societies.                                                                                                                                                                |

## Compatible USB Devices

The following table provides a list of compatible USB devices that can be used on the USB ports of the terminals.

| Device Vendor                             | Model                   | PanelView Plus 700 to 1500   | PanelView Plus 400 and 600   |
|-------------------------------------------|-------------------------|------------------------------|------------------------------|
| USB Keyboard Rockwell Automation          | Cat. No. 6189-KBDEPU1U  | Yes                          | Yes                          |
| Ortek                                     | MCK-600USB              | Yes                          | Yes                          |
| Dell                                      | RT7D10                  | Yes                          | Yes                          |
| USB Keyboard/Mouse Rockwell Automation    | Cat. No. 6189-KBDEPC1U  | Yes                          | No                           |
| USB Mouse Logitec                         | Optical Mouse - M-BJ58  | Yes                          | Yes                          |
| Microsoft                                 | Intellimouse D58-00026  | Yes                          | Yes                          |
| Atek                                      | USB Mouse               | Yes                          | No                           |
| VersaView (Rockwell Automation) USB Mouse |                         | Yes                          | Yes                          |
| USB Hub Belkin                            | USB 4-Port Hub - ESU021 | Yes                          | Yes                          |

<!-- image -->

## Notes:

## Download Fonts to Terminal

## PanelView Plus CE Accessories CD

## Available Fonts for Terminal Applications

The following fonts are pre-installed on PanelViewPlus terminals:

-  True Type fonts (scalable)
- – Tahoma.ttf (proportional)
- – Courier.ttf (fixed width)
- – Arial.ttf (proportional)
-  23 fonts of various sizes migrated from PanelView Standard and PanelView e terminals (various sizes)

To simplify the creation and downloading of .mer application files on these devices, use the above list of fonts when developing screens in FactoryTalk View Studio software.

Additional fonts are available in FactoryTalk View Studio software when developing application screens.

-  If the font used to develop screens is not available on the target device, the closest font is selected.
-  If bold or italics is used, and a separate bold or italics font is unavailable, then the target operating system will use an algorithm to produce these affects.

In either case, the device screens will look different than they do in FactoryTalk View Studio software.

To use additional fonts on a PanelView Plus device, copy any of the font files on the PanelView Plus CE Accessories CD or the Machine Editions Fonts CD to this directory on the computer where FactoryTalk View Studio software is installed:

c:\Documents and Settings\All Users\Documents\RSView Enterprise\ME\Runtime

You can now use the File Transfer Utility in FactoryTalk View Studio software to download the font files to the target device.

1. Select Tools&gt;Transfer Utility.
2. Select Source File&gt;True Type Fonts.
3. Select a font file to download to the device and press the Download button.

The following True Type fonts are included on the PanelView Plus CE Accessories CD:

-  Times New Roman.ttf
-  Symbol.ttf
-  Wingdings.ttf

This CD is not supplied with PanelView Plus terminals.

<!-- image -->

## Machine Edition Fonts CD

Additional fonts are available on the Machine Edition Fonts CD. This CD is available from your local distributor by requesting View-SP006. For additional information, refer to the Rockwell Automation Knowledgebase at http://support.rockwellautomation.com .

## Available Fonts

| Fonts                         | File Name               | Size (Bytes)   |
|-------------------------------|-------------------------|----------------|
| Arial                         |                         |                |
| Arial (Subset 1_30)           | arial_1_30.ttf          | 153,720        |
| Arial Black                   | arialk.ttf              | 117,028        |
| Arial Bold                    | arialbd.ttf             | 288,496        |
| Arial Bold Italic             | arialbi.ttf             | 226,748        |
| Arial Italic                  | ariali.ttf              | 207,808        |
| Comic Sans MS                 |                         |                |
| Comic Sans MS                 | comic.ttf               | 126,364        |
| Comic Sans MS Bold            | comicbd.ttf             | 111,476        |
| Courier New                   |                         |                |
| Courier New (Subset 1_30)     | cour_1_30.ttf           | 162,460        |
| Courier New Bold              | courbd.ttf              | 312,920        |
| Courier New Bold Italic       | courbi.ttf              | 236,148        |
| Courier New Italic            | couri.ttf               | 245,032        |
| Georgia                       |                         |                |
| Georgia                       | georgia.ttf             | 149,628        |
| Georgia Bold                  | georgiab.ttf            | 141,032        |
| Georgia Bold Italic           | georgiaz.ttf            | 159,736        |
| Georgia Italic                | georgiai.ttf            | 157,388        |
| Impact                        | impact.ttf              | 136,076        |
| Kino                          | kino.ttf                | 28,872         |
| MSLogo                        | mslogo.ttf              | 2,500          |
| Symbol                        | symbol.ttf              | 69,464         |
| Tahoma                        |                         |                |
| Tahoma (Subset 1_07)          | tahoma_1_07.ttf 123,980 |                |
| Tahoma Bold                   | tahomabd.ttf            | 295,432        |
| Times New Roman               |                         |                |
| Times New Roman (Subset 1_30) | times_1_30.ttf          | 184,976        |
| Times New Roman Bold          | timesbd.ttf             | 334,944        |
| Times New Roman Bold Italic   | timesbi.ttf             | 239,692        |
| Times New Roman Italic        | timesi.ttf              | 248,368        |

| Fonts                                          | File Name  Size (Bytes)       |
|------------------------------------------------|-------------------------------|
| Trebuchet MS                                   |                               |
| Trebuchet MS trebuc.ttf 69,688                 |                               |
| Trebuchet MS Bold trebucbd.ttf 66,444          |                               |
| Trebuchet MS Bold Italic trebucbi.ttf 66,348   |                               |
| Trebuchet MS Italic trebucit.ttf 72,560        |                               |
| Verdana                                        |                               |
|                                                | Verdana verdana.ttf 149,752   |
| Verdana Bold verdanab.ttf 137,616              |                               |
| Verdana Bold Italic verdanaz.ttf 154,800       |                               |
| Verdana Italic verdanai.ttf 155,076            |                               |
|                                                | Webdings webdings.ttf 118,752 |
|                                                | Wingding wingding.ttf 81,000  |
| Chinese (Simplified) Locale Specific Support   |                               |
| Simsun & NSimSun                               |                               |
| Simsun & NSimSun simsun.ttc 10,500,400         |                               |
| Simsun & NSimSun (Subset 2_50)                 | simsun_2_50.ttc 3,051,024     |
| Simsun & NSimSun (Subset 2_60)                 | simsun_2_60.ttc 3,578,692     |
| Simsun & NSimSun (Subset 2_70)                 | simsun_2_70.ttc 6,975,948     |
| Simsun & NSimSun (Subset 2_80)                 | simsun_2_80.ttc 8,116,188     |
| Simsun & NSimSun (Subset 2_90)                 | simsun_2_90.ttc 9,066,640     |
| SC_Song                                        | sunfon.ttf  4,686,044         |
| Chinese (Traditional) Locale Specific Support  |                               |
| MingLiU & PMingLiU (Choose 1)                  |                               |
| MingLiU & PMingLiU                             | mingliu.ttc  8,822,400        |
| MingLiU & PMingLiU (Subset 2_70)               | mingliu_2_70.ttc 4,786,488    |
| MingLiU & PMingLiU (Subset 2_80)               | mingliu_2_80.ttc 5,772,700    |
| MingLiU & PMingLiU (Subset 2_90)               | mingliu_2_90.ttc 7,354,808    |
| MSMing                                         | msming.ttf  3,172,552         |
| Japanese Locale Specific Support               |                               |
| MS Gothic                                      |                               |
| MS Gothic & P Gothic & UI Gothic               | msgothic.ttc  8,272,028       |
| MS Gothic & P Gothic & UI Gothic (Subset 1_50) | msgothic_1_50.ttc 4,456,536   |
| MS Gothic & P Gothic & UI Gothic (Subset 1_60) | msgothic_1_60.ttc 6,057,400   |
| MS Gothic & P Gothic & UI Gothic (Subset 1_70) | msgothic_1_70.ttc 3,795,500   |
| MS Gothic & P Gothic & UI Gothic (Subset 1_80) | msgothic_1_80.ttc 5,438,776   |
| MS Gothic & P Gothic & UI Gothic (Subset 1_90) | msgothic_1_90.ttc 6,408,352   |
| MS Gothic & P Gothic (Subset 30)               | msgothic30.ttc  4,197,524     |
| MS Gothic & P Gothic (Subset 30_1_19)          | msgothic30_1_19.ttc 3,304,056 |

| Fonts File Name Size (Bytes)                            |
|---------------------------------------------------------|
| Korean Locale Specific Support                          |
| GL_CE gl_ce.ttf 4,130,084                               |
| Gulim & GulimChe (Choose 1)                             |
| Gulim & GulimChe (Subset 1_30) gulim_1_30.ttc 3,010,268 |
| Gulim & GulimChe (Subset 1_40) gulim_1_40.ttc 4,683,896 |
| Gulim & GulimChe (Subset 1_50) gulim_1_50.ttc 7,128,756 |
| Gulim & GulimChe (Subset 1_60) gulim_1_60.ttc 9,360,100 |

## Programmable Key Definitions

The tables in this appendix shows the Windows virtual key code mapping of each programmable function key on the

PanelView Plus CE terminal.

|     |                 |     | Function Key Virtual Key Mapping Function Key Virtual Key Mapping   |
|-----|-----------------|-----|---------------------------------------------------------------------|
| F1  | VK_F1           | K1  | RA + VK_F1                                                          |
| F2  | VK_F2           | K2  | RA + VK_F2                                                          |
| F3  | VK_F3           | K3  | RA + VK_F3                                                          |
| F4  | VK_F4           | K4  | RA + VK_F4                                                          |
| F5  | VK_F5           | K5  | RA + VK_F5                                                          |
| F6  | VK_F6           | K6  | RA + VK_F6                                                          |
| F7  | VK_F7           | K7  | RA + VK_F7                                                          |
| F8  | VK_F8           | K8  | RA + VK_F8                                                          |
| F9  | VK_F9           | K9  | RA + VK_F9                                                          |
| F10 | VK_F10          | K10 | RA + VK_F10                                                         |
| F11 | VK_F11          | K11 | RA + VK_F11                                                         |
| F12 | VK_F12          | K12 | RA + VK_F12                                                         |
| F13 | LS + VK_F1 K13  |     | RS + VK_F1                                                          |
| F14 | LS + VK_F2 K14  |     | RS + VK_F2                                                          |
| F15 | LS + VK_F3 K15  |     | RS + VK_F3                                                          |
| F16 | LS + VK_F4 K16  |     | RS + VK_F4                                                          |
| F17 | LS + VK_F5 K17  |     | RS + VK_F5                                                          |
| F18 | LS + VK_F6 K18  |     | RS + VK_F6                                                          |
| F19 | LS + VK_F7 K19  |     | RS + VK_F7                                                          |
| F20 | LS + VK_F8 K20  |     | RS + VK_F8                                                          |
| F21 | LS + VK_F9 K21  |     | RS + VK_F9                                                          |
| F22 | LS + VK_F10 K22 |     | RS + VK_F10                                                         |

<!-- image -->

The following table provides the Windows virtual-key code mapping for the Alt, Control, and Shift keys on the PanelView Plus CE terminal.

Alt, Control, and Shift Key Mapping

| Keyboard Equivalent Virtual Key Mapping   |
|-------------------------------------------|
| Control VK_LCONTROL                       |
| Shift VK_LSHIFT                           |
| Alt VK_LMENU                              |

## Security Considerations

Ports 137 and 138 are normally open to support the NetBIOS protocol used by Windows CE.NET similar to other Microsoft and IBM network operating systems.

Port 80 is open when the Web server is optionally installed from the PanelView Plus extensions. Otherwise, Port 80 is normally closed.

The FTP server permits a remote computer to run arbitrary commands and read/write files. The FTP server is optionally installed from the VersaView extensions. Otherwise, there is no FTP server on the system.

Simple Network Management Protocol (SNMP) is not supported.

Internet Group Management Protocol (IGMP) is used for IPv4 multicast. A multicast is communication between a single sender and multiple receivers on a network. IGMP is used to exchange membership status data between IPv4 routers that support multicasting and members of multicast groups. A router is an intermediary device on a communication network that expedites message delivery by finding the most efficient route for a message packet within a network, or by routing packets from one subnetwork to another. A subnetwork is a separate part of an organization's network identified through IP addressing.

PanelView Plus CE terminals provide level 2 (full) support for IPv4 multicasting (IGMP version 2) as described in RFC 1112 and RFC 2236.

Security requires a comprehensive application of policies and technology, and an awareness of security needs and potential vulnerabilities. You may also want to consult with Rockwell GMS Network Services for additional assistance.

<!-- image -->

## Notes:

## A

## control panel applications

|                                                                    | date/time  135                                              | date/time  135                                              | date/time  135                                              | date/time  135                                              | date/time  135                                              | date/time  135                                              | date/time  135                                              | date/time  135                                              |
|--------------------------------------------------------------------|-------------------------------------------------------------|-------------------------------------------------------------|-------------------------------------------------------------|-------------------------------------------------------------|-------------------------------------------------------------|-------------------------------------------------------------|-------------------------------------------------------------|-------------------------------------------------------------|
| AC power                                                           | display settings                                            | display settings                                            | display settings                                            | display settings                                            | display settings                                            | display settings                                            | display settings                                            | display settings                                            |
| 400, 600  18                                                       | Ethernet network configuration                              | Ethernet network configuration                              | Ethernet network configuration                              | Ethernet network configuration                              | Ethernet network configuration                              | Ethernet network configuration                              | Ethernet network configuration                              | Ethernet network configuration                              |
| 700 to 1500  18 ,  26                                              | extended diagnostics  130 132                               | extended diagnostics  130 132                               | extended diagnostics  130 132                               | extended diagnostics  130 132                               | extended diagnostics  130 132                               | extended diagnostics  130 132                               | extended diagnostics  130 132                               | extended diagnostics  130 132                               |
| connect  56                                                        | hardware monitor                                            | hardware monitor                                            | hardware monitor                                            | hardware monitor                                            | hardware monitor                                            | hardware monitor                                            | hardware monitor                                            | hardware monitor                                            |
| connections  54                                                    | input panel  127                                            | input panel  127                                            | input panel  127                                            | input panel  127                                            | input panel  127                                            | input panel  127                                            | input panel  127                                            | input panel  127                                            |
| protective-earth connection  54                                    | keyboard settings  125                                      | keyboard settings  125                                      | keyboard settings  125                                      | keyboard settings  125                                      | keyboard settings  125                                      | keyboard settings  125                                      | keyboard settings  125                                      | keyboard settings  125                                      |
| accessories  21                                                    | keypad settings  126                                        | keypad settings  126                                        | keypad settings  126                                        | keypad settings  126                                        | keypad settings  126                                        | keypad settings  126                                        | keypad settings  126                                        | keypad settings  126                                        |
| ActiveSync  c  112 ,  119 ,  121 ,  123 ,  189 ,  190 ,  191       | mouse settings  127                                         | mouse settings  127                                         | mouse settings  127                                         | mouse settings  127                                         | mouse settings  127                                         | mouse settings  127                                         | mouse settings  127                                         | mouse settings  127                                         |
| 203 ,  215                                                         | network  121                                                | network  121                                                | network  121                                                | network  121                                                | network  121                                                | network  121                                                | network  121                                                | network  121                                                |
| adapter plates  25                                                 | regional settings  135                                      | regional settings  135                                      | regional settings  135                                      | regional settings  135                                      | regional settings  135                                      | regional settings  135                                      | regional settings  135                                      | regional settings  135                                      |
| application                                                        | system information  133 124                                 | system information  133 124                                 | system information  133 124                                 | system information  133 124                                 | system information  133 124                                 | system information  133 124                                 | system information  133 124                                 | system information  133 124                                 |
| 113                                                                | touch screen settings                                       | touch screen settings                                       | touch screen settings                                       | touch screen settings                                       | touch screen settings                                       | touch screen settings                                       | touch screen settings                                       | touch screen settings                                       |
| installing  loading .MER  63                                       | ControlNet                                                  | ControlNet                                                  | ControlNet                                                  | ControlNet                                                  | ControlNet                                                  | ControlNet                                                  | ControlNet                                                  | ControlNet                                                  |
| running  64                                                        | ,  compatible controllers  180 ,  184                       | ,  compatible controllers  180 ,  184                       | ,  compatible controllers  180 ,  184                       | ,  compatible controllers  180 ,  184                       | ,  compatible controllers  180 ,  184                       | ,  compatible controllers  180 ,  184                       | ,  compatible controllers  180 ,  184                       | ,  compatible controllers  180 ,  184                       |
| troubleshooting  216                                               | connections  181 ControlNet protocol                        | connections  181 ControlNet protocol                        | connections  181 ControlNet protocol                        | connections  181 ControlNet protocol                        | connections  181 ControlNet protocol                        | connections  181 ControlNet protocol                        | connections  181 ControlNet protocol                        | connections  181 ControlNet protocol                        |
| B                                                                  | modules  181 overview  180                                  | modules  181 overview  180                                  | modules  181 overview  180                                  | modules  181 overview  180                                  | modules  181 overview  180                                  | modules  181 overview  180                                  | modules  181 overview  180                                  | modules  181 overview  180                                  |
| backlight                                                          | Software Requirments  180                                   | Software Requirments  180                                   | Software Requirments  180                                   | Software Requirments  180                                   | Software Requirments  180                                   | Software Requirments  180                                   | Software Requirments  180                                   | Software Requirments  180                                   |
| brightness  80 ,  128 24                                           | copying files                                               | copying files                                               | copying files                                               | copying files                                               | copying files                                               | copying files                                               | copying files                                               | copying files                                               |
| replacement                                                        | applications                                                | applications                                                | applications                                                | applications                                                | applications                                                | applications                                                | applications                                                | applications                                                |
| base unit                                                          | font files  77                                              | font files  77                                              | font files  77                                              | font files  77                                              | font files  77                                              | font files  77                                              | font files  77                                              | font files  77                                              |
| 400-600  11                                                        | cutout dimensions for each terminal                         | cutout dimensions for each terminal                         | cutout dimensions for each terminal                         | cutout dimensions for each terminal                         | cutout dimensions for each terminal                         | cutout dimensions for each terminal                         | cutout dimensions for each terminal                         | cutout dimensions for each terminal                         |
| 700 to 1500  16 27                                                 |                                                             |                                                             |                                                             |                                                             |                                                             |                                                             |                                                             |                                                             |
| battery replacement  ,  151                                        | D date  103 ,  109 ,  135 ,                                 | D date  103 ,  109 ,  135 ,                                 | D date  103 ,  109 ,  135 ,                                 | D date  103 ,  109 ,  135 ,                                 | D date  103 ,  109 ,  135 ,                                 | D date  103 ,  109 ,  135 ,                                 | D date  103 ,  109 ,  135 ,                                 | D date  103 ,  109 ,  135 ,                                 |
| cables  26                                                         | DC power  49 ,  223 connect  53 ,  56                       | DC power  49 ,  223 connect  53 ,  56                       | DC power  49 ,  223 connect  53 ,  56                       | DC power  49 ,  223 connect  53 ,  56                       | DC power  49 ,  223 connect  53 ,  56                       | DC power  49 ,  223 connect  53 ,  56                       | DC power  49 ,  223 connect  53 ,  56                       | DC power  49 ,  223 connect  53 ,  56                       |
|                                                                    | connections  49 deleting files                              | connections  49 deleting files                              | connections  49 deleting files                              | connections  49 deleting files                              | connections  49 deleting files                              | connections  49 deleting files                              | connections  49 deleting files                              | connections  49 deleting files                              |
|                                                                    | applications  76                                            | applications  76                                            | applications  76                                            | applications  76                                            | applications  76                                            | applications  76                                            | applications  76                                            | applications  76                                            |
| runtime communication cables  164 catalog number configuration  21 |                                                             |                                                             |                                                             |                                                             |                                                             |                                                             |                                                             |                                                             |
| CCFL backlight control  79                                         | font files  76                                              | font files  76                                              | font files  76                                              | font files  76                                              | font files  76                                              | font files  76                                              | font files  76                                              | font files  76                                              |
|                                                                    | log files  76                                               | log files  76                                               | log files  76                                               | log files  76                                               | log files  76                                               | log files  76                                               | log files  76                                               | log files  76                                               |
| cleaning display  y  221                                           |                                                             |                                                             |                                                             |                                                             |                                                             |                                                             |                                                             |                                                             |
| communication                                                      | DeviceNet                                                   | DeviceNet                                                   | DeviceNet                                                   | DeviceNet                                                   | DeviceNet                                                   | DeviceNet                                                   | DeviceNet                                                   | DeviceNet                                                   |
| cables  164                                                        | compatible controllers  184 configuration  67               | compatible controllers  184 configuration  67               | compatible controllers  184 configuration  67               | compatible controllers  184 configuration  67               | compatible controllers  184 configuration  67               | compatible controllers  184 configuration  67               | compatible controllers  184 configuration  67               | compatible controllers  184 configuration  67               |
| ControlNet  180                                                    |                                                             |                                                             |                                                             |                                                             |                                                             |                                                             |                                                             |                                                             |
| DH+/DH485/RIO module  174 ,  180                                   | connections  184 I/O status indicator                       | connections  184 I/O status indicator                       | connections  184 I/O status indicator                       | connections  184 I/O status indicator                       | connections  184 I/O status indicator                       | connections  184 I/O status indicator                       | connections  184 I/O status indicator                       | connections  184 I/O status indicator                       |
| DH485  176 DHPlus  178                                             | 185 minimum requirements  184 module  184 185               | 185 minimum requirements  184 module  184 185               | 185 minimum requirements  184 module  184 185               | 185 minimum requirements  184 module  184 185               | 185 minimum requirements  184 module  184 185               | 185 minimum requirements  184 module  184 185               | 185 minimum requirements  184 module  184 185               | 185 minimum requirements  184 module  184 185               |
| Ethernet  172                                                      |                                                             |                                                             |                                                             |                                                             |                                                             |                                                             |                                                             |                                                             |
| Remote I/O  179                                                    | module status indicator  network status indicator           | module status indicator  network status indicator           | module status indicator  network status indicator           | module status indicator  network status indicator           | module status indicator  network status indicator           | module status indicator  network status indicator           | module status indicator  network status indicator           | module status indicator  network status indicator           |
| serial  169                                                        | protocol  183                                               | protocol  183                                               | protocol  183                                               | protocol  183                                               | protocol  183                                               | protocol  183                                               | protocol  183                                               | protocol  183                                               |
| USB ports  168                                                     |                                                             |                                                             |                                                             |                                                             |                                                             |                                                             |                                                             |                                                             |
| communication adapters  26                                         | DF1 cables  164 DH485                                       | DF1 cables  164 DH485                                       | DF1 cables  164 DH485                                       | DF1 cables  164 DH485                                       | DF1 cables  164 DH485                                       | DF1 cables  164 DH485                                       | DF1 cables  164 DH485                                       | DF1 cables  164 DH485                                       |
| communication modules  23 400-600  12 17                           | cables  164 port connectors                                 | cables  164 port connectors                                 | cables  164 port connectors                                 | cables  164 port connectors                                 | cables  164 port connectors                                 | cables  164 port connectors                                 | cables  164 port connectors                                 | cables  164 port connectors                                 |
| ,  700 to 1500  17 installing and replacing  145 ,                 | 174 status indicators  175                                  | 174 status indicators  175                                  | 174 status indicators  175                                  | 174 status indicators  175                                  | 174 status indicators  175                                  | 174 status indicators  175                                  | 174 status indicators  175                                  | 174 status indicators  175                                  |
| 146                                                                |                                                             |                                                             |                                                             |                                                             |                                                             |                                                             |                                                             |                                                             |
| configuration mode                                                 | DHPlus                                                      | DHPlus                                                      | DHPlus                                                      | DHPlus                                                      | DHPlus                                                      | DHPlus                                                      | DHPlus                                                      | DHPlus                                                      |
| accessing  59                                                      |                                                             |                                                             |                                                             |                                                             |                                                             |                                                             |                                                             |                                                             |
|                                                                    | cables  164                                                 | cables  164                                                 | cables  164                                                 | cables  164                                                 | cables  164                                                 | cables  164                                                 | cables  164                                                 | cables  164                                                 |
| loading application  63                                            | network connections  port connectors  174 status indicators | network connections  port connectors  174 status indicators | network connections  port connectors  174 status indicators | network connections  port connectors  174 status indicators | network connections  port connectors  174 status indicators | network connections  port connectors  174 status indicators | network connections  port connectors  174 status indicators | network connections  port connectors  174 status indicators |
|                                                                    | in control panel                                            | in control panel                                            | in control panel                                            | in control panel                                            | in control panel                                            | in control panel                                            | in control panel                                            | in control panel                                            |
| running application  64 terminal settings  64                      |                                                             |                                                             |                                                             |                                                             |                                                             |                                                             |                                                             |                                                             |
|                                                                    | 130                                                         | 130                                                         | 130                                                         | 130                                                         | 130                                                         | 130                                                         | 130                                                         | 130                                                         |
|                                                                    | 175                                                         | 175                                                         | 175                                                         | 175                                                         | 175                                                         | 175                                                         | 175                                                         | 175                                                         |
|                                                                    | diagnostics                                                 | diagnostics                                                 | diagnostics                                                 | diagnostics                                                 | diagnostics                                                 | diagnostics                                                 | diagnostics                                                 | diagnostics                                                 |
|                                                                    | 74                                                          | 74                                                          | 74                                                          | 74                                                          | 74                                                          | 74                                                          | 74                                                          | 74                                                          |
|                                                                    | in RSView                                                   | in RSView                                                   | in RSView                                                   | in RSView                                                   | in RSView                                                   | in RSView                                                   | in RSView                                                   | in RSView                                                   |

## display 400-600

keypad 14

keypad/touch 14

touch screen 13

## display modules

high-bright display 18 , 21 , 32

## display modules 700 to 1500 21

keypad 20

keypad/touch 20

replacing 149

touch screen 18

## display settings

configuration mode 79

in control panel 128

## E

## Ethernet

cables 164

connector pinout 172

network configuration troubleshooting 215

122

external compact flash cards 24 , 118 , 162

## F

FactoryTalk 59

FactoryTalk View software 9 , 59

## firmware upgrade

creating a firmware upgrade card 192

firmware upgrade wizard 191

operating system

202

upgrading from a computer 195

using a firmware upgrade card 194

firmware upgrade kits 27

## fonts

additional fonts 229

linking 83

pre-installed 229

## function keys

keypad terminals 14 , 20

virtual key code mapping 233

## H

hardware monitor 132

hazardous locations 29

400/600 USB port 30

high-bright display 18 , 32

## I

## IGMP Protocol 173 , 235 input devices

input panel 127

keyboard 125

keypad 126

mouse 85 , 88 , 127

touch screen 124

## input panel 62

## installation 29

1000 mounting dimensions 42

1250 mounting dimensions 43

1500 mounting dimensions 44

400 mounting dimensions 39

600 mounting dimensions 40

700 mounting dimensions 40

ambient temperature 34

backlight 156

battery 151

bezel 153

clearances 34

communication module 146

display module 700 to 1500 149

enclosures 32

hazardous locations 29

high-bright display 32

legend inserts 160

mounting levers 400-600 36

panel installation 400-600 35

panel installation 700 to 1500 37

product label 160

intended audience 7

internal compact flash 117

installing and replacing 141

## Internet Group Management Protocol (IGMP)

173 , 235

IP address 71

## K

## keyboard

compatibility 227

mouse compatibility 227

settings 125

troubleshooting 214

keypad legend inserts 24 , 160

keypad settings 126

## L

languages 106 , 135

LED indicators 205

## legend inserts

installation 160

loading application 63

logic module 22

700 to 1500

features 16

installing and replacing 142

## M

## maintenance

battery 151

## memory

allocations 133

boot ROM 117

external compact flash card 118

141

117

dynamic RAM 118 installing and replacing internal compact flash

USB Mass Storage Devices 118

## messages

startup error 211 startup information

209

modular components 700 to 1500 16

mounting clips 700 to 1500 27

mounting dimensions

1000 42

1250 43

1500 44

400 39

600 40

700 40

mounting levers 400-600 27 , 35

mouse 85 , 88 , 127 , 168

compatible 227

multikey lockout 126

## N

NAP 182

network connections 121 , 164

## O

## operating system upgrade

loading PanelView Plus CE components 203 , 204

outdoor installation high-bright displays 32

## P

packing list 7

power supply

400 and 600 49 , 54

power terminal block install 46

remove 46

pre-loaded programs 112

print setup for alarms 89

for diagnostic messages 89

for displays

89

product components 21

protective-earth connection 56

## R

RAM 24

installing and replacing 141

registry settings 117

## Remote I/O

cables 164 , 179 connection 179 port connectors

174

status indicators 175

## reset switch

400-600 57

resetting terminal 60

400-600 57

## S

safe mode 219

screen saver 128

security considerations 235

serial communication

171

computer connection connections 169 DF1 169 DH485 169 null modem cable 170 ports 169 , 172 printing 169 , 171 transferring applications using a modem 170

169

shortcut keys 114

Shortcut paths for startup 96

Simple Network Management Protocol

(SNMP) 173 , 235

SNMP Protocol 173 , 235

software 9 , 113

## specifications

agency certifications electrical 223

environmental 223

mechanical 225

## startup

error messages problems 216 sequence 210

211

information messages 209

tests 131

storage, permanent 116 , 117

stylus, recommended 19

support 102

system event log

99 , 132

information 133

## T

terminal information 100 , 132

226

## terminal settings 64

date 103

diagnostics 74

long date format 110

short date format 109

system event log 99

terminal info 100

time 104

time format 108

time zone 105

time 104 , 135

format 108 , 135

## touch screen

calibration 124

cursor enable 87

double-tap sensitivity 88 , 124

## transferring files 77

## troubleshooting 205

accessing configuration mode 216

advanced 217

Ethernet connection 215

file system 216

general 206

keyboard 214

LED indicators 205

mouse 214

starting in safe mode 219

startup error messages 211

startup information messages 209

## U

## USB devices 227

USB ports

168

400/600 terminals 30

compatible 227

connector pinouts 168

USB Hub 227

USB mass storage devices 118

## V

## ViewPoint software 9

## W

## Windows CE .NET 9 , 111 , 117

applications 112

browsing web pages 116

command bar 115

compiling applications 111 finding files 116 operating system 111 pre-loaded programs 112 printing 116 start menu and taskbar 115 using 113

## wiring and safety guidelines 45 , 163

.

## Rockwell Automation Support

Use the following resources to access support information.

| Technical Support Center                         | Knowledgebase Articles, How-to Videos, FAQs, Chat, User Forums, and Product Notification Updates.                     | https://rockwellautomation.custhelp.com/                                   |
|--------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------|
| Local Technical Support Phone Numbers            | Locate the phone number for your country.                                                                             | http://www.rockwellautomation.com/global/support/get-support now.page                                                                            |
| Direct Dial Codes                                | Find the Direct Dial Code for your product. Use the code to route your call directly to a technical support engineer. | http://www.rockwellautomation.com/global/support/direct-dial.page          |
| Literature Library                               | Installation Instructions, Manuals, Brochures, and Technical Data.                                                    | http://www.rockwellautomation.com/global/literature-library/ overview.page |
| Product Compatibility and Download Center (PCDC) | Get help determining how products interact, check features and capabilities, and find associated firmware.            | http://www.rockwellautomation.com/global/support/pcdc.page                 |

## Documentation Feedback

Your comments will help us serve your documentation needs better. If you have any suggestions on how to improve this document, complete the How Are We Doing? form at http://literature.rockwellautomation.com/idc/groups/literature/ documents/du/ra-du002\_-en-e.pdf. f.

Rockwell Automation maintains current product environmental information on its website at http://www.rockwellautomation.com/rockwellautomation/about-us/sustainability-ethics/product-environmental-compliance.page .

Allen-Bradley, FactoryTalk View, FactoryTalk View ME, FactoryTalk ViewPoint, FactoryTalk View Studio, PanelView Plus, Rockwell Automation, Rockwell Software, RSLinx Enterprise, and TechConnect are trademarks of Rockwell Automation, Inc.

Trademarks not belonging to Rockwell Automation are property of their respective companies.

Rockwell Otomasyon Ticaret A.Ş., Kar Plaza İş Merkezi E Blok Kat:6 34752 İçerenköy, İstanbul, Tel: +90 (216) 5698400