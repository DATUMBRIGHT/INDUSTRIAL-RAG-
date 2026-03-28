<!-- image -->

## DeviceNet Network Configuration

1756 ControlLogix®, 1756 GuardLogix®, 1769 CompactLogix™, 1769 Compact GuardLogix®, 1789 SoftLogix™ , Studio 5000® Logix Emulate™

Rockwell Automation Publication DNET -UM004E -EN -P -March 2022 Supersedes Publication DNET -UM004D -EN -P -September 2020

<!-- image -->

<!-- image -->

## Important User Information

Read this document and the documents listed in the additional resources section about installation, configuration, and operation of this equipment before you install, configure, operate, or maintain this product. Users are required to familiarize themselves with installation and wiring instructions in addition to requirements of all applicable codes, laws, and standards .

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

ATTENTION: Identifies information about practices or circumstances that can lead to personal injury or death, property damage, or economic loss. Attentions help you identify a hazard, avoid a hazard, and recognize the consequence.

IMPORTANT Identifies information that is critical for successful application and understanding of the product.

Labels may also be on or inside the equipment to provide specific precautions.

<!-- image -->

SHOCK HAZARD: Labels may be on or inside the equipment, for example, a drive or motor, to alert people that dangerous voltage may be present.

<!-- image -->

<!-- image -->

BURN HAZARD: Labels may be on or inside the equipment, for example, a drive or motor, to alert people that surfaces may reach dangerous temperatures.

ARC FLASH HAZARD: Labels may be on or inside the equipment, for example, a motor control center, to alert people to potential Arc Flash. Arc Flash will cause severe injury or death. Wear proper Personal Protective Equipment (PPE). Follow ALL Regulatory requirements for safe work practices and for Personal Protective Equipment (PPE).

Rockwell Automation recognizes that some of the terms that are currently used in our industry and in this publication are not in alignment with the movement toward inclusive language in technology. We are proactively collaborating with industry peers to find alternatives to such terms and making changes to our products and content. Please excuse the use of such terms in our content while we implement these changes.

This manual includes new and updated information. Use these reference tables to locate changed information.

Grammatical and editorial style changes are not included in this summary.

## Global changes

This table identifies changes that apply to all information about a subject in the manual and the reason for the change. For example, the addition of new supported hardware, a software design change, or additional reference material would result in changes to all of the topics that deal with that subject.

| Change                                               | Topic                               |
|------------------------------------------------------|-------------------------------------|
| New Studio 5000 Logix Designer® application branding | Studio 5000® environment on page 12 |

## New or enhanced features

None in this release.

## Table of Contents

| Summary of Changes             | Network Configuration   .  ................................ ................................ ..............   1  11          |
|--------------------------------|------------------------------------------------------------------------------------------------------------------------------|
| Preface                        | Studio 5000 environment  ................................ ................................ .........  12                     |
|                                | Additional  Resources   .  ................................ ................................ .................  12           |
|                                | Legal Notices   .  ................................ ................................ ...............................   1  13 |
|                                | Chapter 1                                                                                                                    |
| DeviceNet Overview             | Choose a Single Network or Subnets  ................................ .......................  15                             |
|                                | Single Network   .  ................................ ................................ .....................  15              |
|                                | Advantages to Using a Single Network   .  ................................ ........   1  15                                  |
|                                | Disadvantages to Using a Single Network   .  ................................ ...   1  16                                    |
|                                | Subnets  ................................ ................................ ................................ .   1  16        |
|                                | Advantages to Using Subnets  ................................ .......................   1  16                                |
|                                | Disadvantages to Using Subnets   .  ................................ ..................   1  16                              |
|                                | Choose a Scanner  ................................ ................................ .......................   1  17          |
|                                | Bridge Across Networks   .  ................................ ................................ .............   1  17          |
|                                | Choose a Baud Rate for the Network   .  ................................ ........................   1  19                    |
|                                | Required Software   .  ................................ ................................ ......................   2  21      |
|                                | Chapter 2                                                                                                                    |
| Connect a Computer to the      | Connection Options ................................ ................................ ...................   2  23             |
| DeviceNet Network              | Set Up the DeviceNet Driver   .  ................................ ................................ .....   2  24             |
|                                | Obtain the Driver for the Interface Device  ................................ ........   2  24                                |
|                                | Verify that the Driver Works   .  ................................ ..............................  24                        |
|                                | Chapter 3                                                                                                                    |
| Connect Devices to the Network | Before You Begin ................................ ................................ ........................   2  27          |
|                                | Set the Node Address of a Device  ................................ .............................   2  27                     |
|                                | Set Node Address via Hardware Mechanism ................................ ....   2  28                                        |
|                                | Set Node Address via Software  ................................ ..........................  29                               |
|                                | Set Node Address via DeviceNet Node Commissioning Tool  ..........   3  31                                                   |
|                                | Make Sure Your Devices Are on Your Network   .  ................................ ........ 32                                 |
|                                | Chapter 4                                                                                                                    |
| Configure the Network Offline  | Create a File for the Network   .  ................................ ................................ ....   3  33            |
|                                | Before You Begin ................................ ................................ ........................   3  34          |
|                                | Create Your Network in RSNetWorx for DeviceNet Software   .  ...............   3  34                                         |
|                                | Configure Each Device   .  ................................ ................................ ...............   3  35         |
|                                | Specify a Device Node Address  ................................ ...........................   3  36                          |
|                                | Change a Device Node Address  ................................ ....................   3  37                                  |

|                              | Configure Device Parameters   .  ................................ ............................  38                   |
|------------------------------|----------------------------------------------------------------------------------------------------------------------|
|                              | Configure the Scanner   .  ................................ ................................ ..............  38      |
|                              | Build the Scan List ................................ ................................ ...............   4  40        |
|                              | Set the Alignment Option   .  ................................ ................................ ...  42              |
|                              | SoftLogix 5800 Controller   .  ................................ .............................   4  43                |
|                              | Manually Assign Each Device to a Memory Location   .  ........................   4  43                               |
|                              | Save the Configuration File   .  ................................ ................................ ......  44        |
|                              | Generate an RSNetWorx for DeviceNet Report ................................ ......  44                               |
|                              | Go Online to Your Network  ................................ ................................ ......  46              |
|                              | Download Configuration to Your Network   .  ................................ .............   4  48                   |
|                              | Chapter 5                                                                                                            |
| Configure the Network Online | Before You Begin ................................ ................................ ........................   4  49  |
|                              | Verify Communication Between the Computer and Devices   .  ................   5  50                                  |
|                              | Create a New File for the Network   .  ................................ ............................   5             |
|                              | 51                                                                                                                   |
|                              | Configure Each Device   .  ................................ ................................ ............... 54      |
|                              | Upload the Configuration of a Device   .  ................................ ................ 54                       |
|                              | Change and Download Device Configuration   .  ................................ ... 54                                |
|                              | Configure the Scanner   .  ................................ ................................ ............... 56      |
|                              | Upload the Current Scanner Configuration   .  ................................ ...... 56                             |
|                              | Define the Scanner Properties   .  ................................ ............................   5  57             |
|                              | Build the Scan List ................................ ................................ ...............  58            |
|                              | Set the Alignment Option   .  ................................ ................................ ...   6  60          |
|                              | SoftLogix 5800 Controller   .  ................................ .............................   6  61                |
|                              | Manually Assign Each Device to a Memory Location   .  ........................   6  61                               |
|                              | Download the Configuration to the Scanner   .  ................................ .....   6  63                        |
|                              | Upload and Save the Configuration File ................................ ...................   6  63                  |
|                              | Generate  an RSNetWorx for DeviceNet Report ................................ ......  64                              |
|                              | Chapter 6                                                                                                            |
| Automatically Configure a    | How AutoScan Operates  ................................ ................................ ...........   6  67         |
| DeviceNet Network            | Determine If You Can Use AutoScan  ................................ .......................   6  69                  |
|                              | How AutoScan Affects Your Network  ................................ ......................   7  70                   |
|                              | Install the DeviceNet Node Commissioning Tool  ................................ ..   7  70                           |
|                              | Connect Devices  ................................ ................................ .........................   7  71 |
|                              | Install a Scanner or Network Interface Devices   .  ................................   7  71                         |
|                              | Install Other DeviceNet Devices   .  ................................ ........................  72                   |
|                              | Set the Node Address and Baud Rate with the DeviceNet Node                                                           |
|                              | Commissioning Tool   .  ................................ ................................ ............   7  73       |
|                              | Add the Scanner to the Logix Designer project  ................................ .......   7  73                      |
|                              | Add the Scanner to the I/O Configuration Folder   .  .............................   7  73                           |

|                            | Define the Properties of the Scanner  ................................ .................   7  74                        |
|----------------------------|-------------------------------------------------------------------------------------------------------------------------|
|                            | Enable AutoScan with the Logix Designer application   .  ...........................   7  75                            |
|                            | Initiate AutoScan via the User Program   .  ................................ ................... 76                     |
|                            | Implement AutoScan   .  ................................ ................................ ...........   7  77           |
|                            | Configure I/O Allocation Size Via the User Program  ................  78                                                |
|                            | Configure I/O Allocation Via a DeviceView Configurator .........  78                                                    |
|                            | Initiate AutoScan via the User Program  ................................ ...... 79                                      |
|                            | Initiate AutoScan via the DeviceView Configurator   .  ..................   8  80                                       |
|                            | Additional Considerations Regarding AutoScan  .............................   8  80                                     |
|                            | Access Device Data   .  ................................ ................................ .....................   8  81 |
|                            | Put the Scanner in Run Mode ................................ ................................ ...  82                   |
|                            | Additional Information About AutoScan  ................................ ................  83                            |
|                            | Type of Connection that the Scanner Sets Up  ................................ ..  83                                    |
|                            | Allocating More Memory for Each Device ................................ .........  83                                   |
| Control a Device           | Before You Begin ................................ ................................ ........................   8  85     |
|                            | RSNetWorx Report for the Network  ................................ ..................   8  87                           |
|                            | Data Map for Each of Your Devices  ................................ ...................  87                             |
|                            | Add the Scanner to the Controller’s I/O Configuration   .  .........................  87                                |
|                            | Conserve EtherNet/IP or ControlNet Network Bandwidth  ............  87                                                  |
|                            | Add the Scanner to the I/O Configuration Folder   .  ............................  89                                   |
|                            | Configure the Scanner   .  ................................ ................................ ........  89               |
|                            | Determine the Address of DeviceNet Data  ................................ .............   9  90                         |
|                            | SoftLogix 5800 Controller  ................................ ................................ ..  92                     |
|                            | Determine If a Device Has Failed  ................................ ............................  92                     |
|                            | Place the Scanner in Run Mode ................................ ................................  94                     |
|                            | When to Use an MSG Instruction   .  ................................ ............................  94                   |
|                            | Determine the Parameter Number to Access ................................ ........... 95                                |
|                            | Determine the Configuration of the Parameter   .  ................................ ...... 95                            |
|                            | Test the Parameter  ................................ ................................ ....................  96          |
|                            | Enter Message Logic  ................................ ................................ .................  98            |
|                            | Define the Source or Destination Data  ................................ .............  98                               |
|                            | Enter and Configure the MSG Instruction   .  ................................ .......  99                               |
|                            | Set the Communication Path   .  ................................ ...........................  100                       |
|                            | Chapter 8                                                                                                               |
| Interlock and Share Inputs | Interlock  ................................ ................................ ................................ ...  103  |
|                            | Choose a Master Controller   .  ................................ ...............................  103                   |
|                            | Determine How Much Data to Exchange  ................................ ........   1  104                                 |
|                            | Enable Slave Mode for the Slave Scanner  ................................ ........   1  104                             |
|                            | Map the Slave Mode Data   .  ................................ ................................ ..   1  105              |

|                              | Add the Slave to the Master Scanner’s Scan List  .............................   1  106                                  |
|------------------------------|--------------------------------------------------------------------------------------------------------------------------|
|                              | Map the Data of the Slave   .  ................................ ................................ ..   1  107             |
|                              | Place Both Scanners In Run Mode   .  ................................ ...................  108                           |
|                              | Share Inputs ................................ ................................ .............................  108        |
|                              | Add the Input to the First Scanner  ................................ ..................  108                             |
|                              | Add the Input to the Second Scanner   .  ................................ ..............  108                            |
|                              | Map the Input Data in the Second Scanner   .  ................................ .....   1  109                            |
| Communicate with a PanelView | Choose Data Types   .  ................................ ................................ ....................  111       |
| Standard Terminal            | Choose a Communication Method   .  ................................ ..........................  111                      |
|                              | I/O Slave Communication   .  ................................ ................................ ..   1  112               |
|                              | Explicit Server Communication  ................................ .......................  112                             |
|                              | Explicit Client Communication   .  ................................ ......................... 113                        |
|                              | Plan and Configure I/O Slave Tags  ................................ .......................... 113                       |
|                              | Use a Word/Bit Format for Each Tag  ................................ ................ 113                                |
|                              | For Integers, Skip Every Other Word   .  ................................ ...............  114                           |
|                              | Configure an I/O Slave Tag  ................................ ...............................  114                        |
|                              | Set Up the Terminal on Your Network  ................................ ...................  115                           |
|                              | Set the Protocol  l  ................................ ................................ ..................  115           |
|                              | Set the Node Address and I/O Sizes  ................................ .................  116                              |
|                              | Configure the Scanner to Update I/O Slave Tags  ................................ ... 117                                 |
|                              | Add the Terminal to the Scan  List   .  ................................ ...................... 117                      |
|                              | Edit I/O Parameters   .  ................................ ................................ ...........   1  118          |
|                              | Map Input and Output Data ................................ ..............................  119                           |
|                              | Address I/O Slave Tags in the Logix Designer  Programming Software                                                       |
|                              | Project ................................ ................................ ................................ ........  119 |
|                              | SoftLogix 5800 Controller  ................................ ................................ .  121                      |
|                              | Plan and Configure Explicit Server Tags   .  ................................ ................  121                      |
|                              | Assign Assembly Instances   .  ................................ ................................   1  122                |
|                              | For Integers, Skip Every Other Word   .  ................................ ...............   1  122                       |
|                              | Configure an Explicit Server Tag   .  ................................ ......................   1  123                   |
|                              | Program the Controller to Get/Set Explicit Server Tags   .  .......................   1  124                             |
|                              | Create an Array for the Assembly Instance   .  ................................ ......   1  124                          |
|                              | Enter and Configure the MSG Instruction   .  ................................ ......   1  124                            |
|                              | Set the Communication Path   .  ................................ ............................   1  125                   |
|                              | Configure Explicit Client Tags   .  ................................ ................................   1  126           |
|                              | Determine the Parameter Number to Access  ................................ ..   1  127                                   |
|                              | Determine the Configuration of the Parameter   .  ..............................   1  127                                |
|                              | Configure an Explicit Client Tag  ................................ ......................   1  128                       |

|                               | Chapter 10                                                                                                                 |
|-------------------------------|----------------------------------------------------------------------------------------------------------------------------|
| Communicate with a            | Before You Begin ................................ ................................ ......................  130             |
| FactoryTalk View Project      | Create a Topic for the Device  ................................ ................................ ..  130                   |
|                               | Create a Node   .  ................................ ................................ ............................   1  131 |
|                               | Create a Tag for the Parameter  ................................ ...............................   1  132                  |
|                               | Chapter 11                                                                                                                 |
| Tune the Performance of a     | Factors that Affect Performance   .  ................................ ..............................   1  136              |
| DeviceNet Network             | I/O Parameters of Each Device  ................................ ..........................   1  137                        |
|                               | Background Poll  ................................ ................................ ..................   1  137             |
|                               | Interscan Delay  ................................ ................................ ..................   1  139             |
|                               | Change the Configuration of Your Network   .  ................................ ..........   1  139                         |
|                               | Upload the Current Configuration of the Scanner  .........................   1  139                                        |
|                               | Set the Interscan Delay and Poll Ratio  ................................ .............   1  140                            |
|                               | Set the I/O Parameters of a Device   .  ................................ ...................   1  140                      |
|                               | Change of State or Cyclic Transfer   .  ................................ .............  141                                |
|                               | Strobed Transfer   .  ................................ ................................ ..........   1  142                |
|                               | Polled Transfer   .  ................................ ................................ .............   1  142              |
|                               | Download the Configuration to the Scanner   .  ................................ ...   1  143                               |
|                               | Save the Configuration File   .  ................................ ...............................   1  143                 |
|                               | Chapter 12                                                                                                                 |
| Automate the Replacement of a | Automatic Device Recovery   .  ................................ ................................ ...... 145                |
| Failed Device                 | Set Up Automatic Device Recovery  ................................ ........................  146                           |
|                               | Choose an Electronic Key Level for a Device   .  ................................ ....  146                                |
|                               | Update Your Network Configuration File   .  ................................ ........   1  147                             |
|                               | Define the Electronic Key   .  ................................ ................................ ..   1  147               |
|                               | Enable Auto - Address Recovery for the Scanner  ..............................   1  148                                    |
|                               | Set the ADR Settings for the Device  ................................ .................   1  149                           |
|                               | Download the Changes to the Scanner  ................................ ............   1  150                                |
|                               | Upload and Save the Configuration File  ................................ ..........   1  150                               |
|                               | Appendix A                                                                                                                 |
| Map the Memory Location with  | Give a Value Its Own Memory Location   .  ................................ ..................   1  153                     |
| Advanced Mapping              |                                                                                                                            |

Index

## Network Configuration

This manual describes how you can use DeviceNet modules with your Logix 5000™ controller and communicate with various devices on the DeviceNet network.

You should use this manual if you program applications that use DeviceNet with one of these Logix 5000™ controllers:

- 1756 ControlLogix® controllers
- 1768 CompactLogix™ controllers
- 1769 CompactLogix™ controllers
- 1789 SoftLogix™ 5800 controllers
- PowerFlex® 700S with DriveLogix™ controllers

## You should also understand:

- Networking concepts
- RSNetWorx™ for DeviceNet software
- Logix Designer programming software
- RSLinx® Classic communication software

Rockwell Automation recognizes that some of the terms that are currently used in our industry and in this publication are not in alignment with the movement toward inclusive language in technology. We are proactively collaborating with industry peers to find alternatives to such terms and making changes to our products and content. Please excuse the use of such terms in our content while we implement these changes.

These chapters describe how to set up a DeviceNet network:

- Chapter 2—Connect a Computer to the DeviceNet Network on page 23
- Chapter 3—Connect Devices to the Network on page 71
- Chapter 4—Configure the Network Offline on page 33
- Chapter 5—Configure the Network Online on page 33

You are not required to complete all tasks in each chapter in the exact order presented to set up your DeviceNet application. For example, you can configure your network offline before you connect a computer to the network.

However, there are some requirements related to the order in which you complete tasks. For example, you must complete the tasks in chapters 2 and 3 before you can configure the network online.

This table describes optional and required conditions to consider when determining the order in which you plan to complete tasks in your DeviceNet application.

| Task                              | Optional Conditions                                                                                                                      | Required Conditions                                     |
|-----------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------|
| Connect a computer to the network | • Can be completed before or after connecting devices to the network •  Can be completed before or after configuring the network offline | Must be completed before configuring the network online |

| Task                           | Optional Conditions                                                                                                                                                                                     | Required Conditions                                                                                                                                                  |
|--------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Connect devices to the network | • Can be completed before or after connecting a computer to the network •  Can be completed before or after configuring the network offline                                                             | Must be completed before configuring the network online                                                                                                              |
| Configure the network offline  | • Can be completed before or after connecting a computer to the network •  Can be completed before or after connecting devices to the network •  Can be completed before configuring the network online | None                                                                                                                                                                 |
| Configure the network online   | Can be completed without creating a network configuration file offline                                                                                                                                  | •  Computer must be connected to the network before configuring the network online •  Devices must be connected to the network before configuring the network online |

## Studio 5000 environment

## Additional Resources

The Studio 5000 Automation Engineering &amp; Design Environment® combines engineering and design elements into a common environment. The first element is the Studio 5000 Logix Designer® application. The Logix Designer application is the rebranding of RSLogix 5000® software and will continue to be the product to program Logix 5000™ controllers for discrete, process, batch, motion, safety, and drive-based solutions.

<!-- image -->

The Studio 5000® environment is the foundation for the future of Rockwell A Automation® engineering design tools and capabilities. The Studio 5000® environment is the one place for design engineers to develop all elements of their control system.

For more information on the products included in this publication, use the publications listed in this table.

| Resource                                                              | Description                                                                                 |
|-----------------------------------------------------------------------|---------------------------------------------------------------------------------------------|
| DeviceNet Modules Installation Instructions, publication DNET - IN001 | Describes how to install and set up 1756 - DNB, 1769 - ADN, and 1769-SDN DeviceNet modules. |

## Legal Notices

| Resource                                                                               | Description                                                                                                                                  |
|----------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| DeviceNet Media Design Installation Guide, publication DNET - UM072                    | Describes how to design, install, and troubleshoot a DeviceNet cable system.                                                                 |
| Logix 5000 Controllers Common Procedures Programming Manual, publication 1756 - PM001M | Links to a collection of programming manuals that describe how you can use procedures that are common to all Logix 5000 controller projects. |

Rockwell Automation publishes legal notices, such as privacy policies, license agreements, trademark disclosures, and other terms and conditions on the Legal Notices page of the Rockwell Automation website.

## End User License Agreement (EULA)

You can view the Rockwell Automation End -User License Agreement ("EULA") by opening the License.rtf file located in your product's install folder on your hard drive.

## Open Source Licenses

The software included in this product contains copyrighted software that is licensed under one or more open source licenses. Copies of those licenses are included with the software. Corresponding Source code for open source packages included in this product are located at their respective web site(s).

Alternately, obtain complete Corresponding Source code by contacting Rockwell Automation via the Contact form on the Rockwell Automation website:

http://www.rockwellautomation.com/global/about-us/contact/contact.page Please include "Open Source" as part of the request text.

A full list of all open source software used in this product and their corresponding licenses can be found in the OPENSOURCE folder. The default installed location of these licenses is C:\Program Files (x86)\Common Files\Rockwell\Help\&lt;Product Name&gt;\Release Notes\OPENSOURCE\index.htm .

Choose a Single Network or Subnets Single Network

## DeviceNet Overview

The Logix 5000 family of controllers operates with many DeviceNet communication modules. This chapter describes each communication module and the preliminary tasks you must complete before your configure and program the DeviceNet network.

<!-- image -->

| Topic                              | Page    |
|------------------------------------|---------|
| Choose a Single Network or Subnets | page 15 |
| Choose a Scanner                   | page 16 |
| Bridge Across Networks             | page 17 |
| Choose a Baud Rate for the Network | page 19 |
| Assign an Address to Each Device   | page 20 |

DeviceNet communication modules share these features:

- Interface via cabling systems using either round or flat media that provide both power and communication
- Use network protocols
- Require no network scheduling
- Support messaging, produced/consumed data, and distributed I/O

You can organize the devices on the network in a single network or several, smaller distributed networks known as subnets.

When you use a single network, you place all your devices on a single DeviceNet network and connect the controller directly to the network via a scanner. The graphic shows a single network.

<!-- image -->

## Advantages to Using a Single Network

There are advantages to using a single network for your DeviceNet application:

- The overall cost to install the network is lower than using subnets.
- You need to manage only a single network.
- The Logix 5000 controller is local to the DeviceNet scanner. For example, with a single network in a ControlLogix® application, the 1756-L64 controller is in the same ControlLogix® chassis as the 1756-DNB scanner.

## Disadvantages to Using a Single Network

## Subnets

## Advantages to Using Subnets

## Disadvantages to Using Subnets

There are disadvantages to using a single network for your DeviceNet application:

- The network must use shorter distances from one end to another.
- The more devices on the network, the slower the overall performance of the network.
- Your network may have more power supply requirements than can be handled by one network
- A single network can contain only up to 64 nodes

A subnet configuration is a main network that is connected to distributed subnets using a scanner, or linking device. In this option, you must install a ControlNet® network or EtherNet/IP™ network, also known as a backbone, that connects to distributed subnets using a linking device.

For example, if you choose an EtherNet/IP network backbone, you must use 1788-EN2DN linking devices to connect the subnets.

The graphic shows a subnet network.

<!-- image -->

There are advantages to using subnets for your DeviceNet application:

- Typically, there are shorter runs on subnets, which allow a faster communication rate for the DeviceNet network.
- With fewer devices on each subnet, the overall performance of the network is faster.
- There are simpler power requirements.

There are disadvantages to using subnets for your DeviceNet application:

- The overall cost to install the network is higher than using a single network.
- You must manage multiple networks.
- The Logix 5000™ controller is remote from the linking device. For example, with subnets in a 1768 CompactLogix™ application, a 1768-L45 controller is remote from the 1788 -CN2DN linking device.

## Choose a Scanner

The DeviceNet scanner connects a Logix 5000™ controller to the devices on a DeviceNet network. The graphic shows how a scanner exchanges data between a controller and devices on the DeviceNet network.

<!-- image -->

The table describes how to choose a scanner

| If you are using   | And                                   | Use this scanner                                     |
|--------------------|---------------------------------------|------------------------------------------------------|
| Single network     | 1768 or 1769 CompactLogix™ controller | CompactLogix™ 1769 - SDN modules                     |
|                    | ControlLogix® controller              | ControlLogix® 1756 - DNB modules                     |
|                    | DriveLogix™ controller                | 1788 - DNBO DeviceNet daughtercard                   |
|                    | SoftLogix™ 5800 controller            | 1784 - PCIDS card                                    |
| Subnets            | EtherNet/IP main network              | EtherNet/IP to DeviceNet Linking Device 1788 - EN2DN |
|                    | ControlNet main network               | ControlNet to DeviceNet Linking Device 1788 - CN2DN  |

## Bridge Across Networks

Logix 5000™ controllers can usually communicate with devices on other networks with no additional configuration or programming. A bridge con nects two networks.

IMPORTANT You cannot bridge from a device on a DeviceNet network to a device on a ControlNet nor EtherNet/IP network. You can only bridge from devices on ControlNet or EtherNet/IP networks to devices on DeviceNet networks.

Refer to table Bridging Across Networks on page 17 for more information.

## The bridge is one of these:

- A single device with communication ports for two different networks, such as a 1788 -EN2DN linking device
- A separate communication device in the same chassis

For example, the bridge device shown in the following graphic is connected to both EtherNet/IP and DeviceNet networks. Device 1 on an EtherNet/IP

network can communicate with Device 2 on a DeviceNet network through the bridge.

<!-- image -->

This table describes how communication can bridge the networks.

## Bridging Across Networks

| A device on this network   | Can access a device on this network   | Can access a device on this network   | Can access a device on this network   | Can access a device on this network   |
|----------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|
|                            | EtherNet/IP                           | ControlNet                            | DeviceNet                             | RS - 232(1)                           |
| EtherNet/IP                | yes                                   | yes                                   | yes                                   | yes                                   |
| ControlNet                 | yes                                   | yes                                   | yes                                   | yes                                   |
| DeviceNet                  | no                                    | no                                    | yes                                   | no                                    |
| RS - 232                   | yes                                   | yes(2)                                | yes                                   | yes                                   |

In this example, a computer configures a drive on a DeviceNet network. The workstation bridges an EtherNet/IP network to reach the drive.

<!-- image -->

In this example, the RSLinx® communication software window shows how the DeviceNet bridge links to the EtherNet/IP network.

## Choose a Baud Rate for the Network

<!-- image -->

You must choose a baud rate for the DeviceNet network. There are three rates available for the network:

- 125 kbps—This is the default baud rate for a DeviceNet network. It is the easiest baud rate to use and is usually sufficient.
- 250 kbps
- 500 kbps

This table describes the most common methods to set a baud rate.

| Method                                | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|---------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Autobaud feature                      | At powerup, the device automatically sets its baud rate to the baud rate of the first device it hears on the network. The baud rate remains set until the device powers up again. The network requires at least one device with a fixed baud rate so the autobaud devices have something against which to set. Typically, scanners and network interfaces have a fixed baud rate.                                                                                                                                                                                                                                                            |
| Switches or push button on the device | Some devices have switches or push buttons that set the baud rate as follows: •  The device reads the switch setting at powerup. •  Typically, the switch lets you select either autobaud or a fixed baud rate, that is 125 Kbps, 250 Kbps, or 500 Kbps •  If you change the switch setting, you must cycle power to the device before the change takes effect. There are exceptions. For example, the 1756 - DNB module has a push button that only lets you set the baud rate if the module is disconnected from the network or network power is off. Once you change the baud rate, the module automatically resets to the new baud rate. |
| Software                              | Some devices require a programming device to set its address. For example, you can use the computer and the DeviceNet node commissioning tool to set the baud rate of a device. The node commissioning tool is available in either of the following methods: •  Automatically when you install RSNetWorx™ for DeviceNet software •  As a separate application on the Logix Designer programming software CD, revision 13.0 or later                                                                                                                                                                                                          |

## Assign an Address to Each Device

The length of the trunkline and type of cable determines which baud rates you can use.

| Baud Rate   | Maximum Distance   | Maximum Distance   | Maximum Distance   | Cumulative Drop Line Length   |
|-------------|--------------------|--------------------|--------------------|-------------------------------|
|             | Flat Cable         | Thick Cable        | Thin Cable         |                               |
| 125K bit/s  | 420m (1378 ft)     | 500m (1640 ft)     | 100m (328 ft)      | 156 m (512 ft)                |
| 250K bit/s  | 200m (656 ft)      | 250m (820 ft)      | 100m (328 ft)      | 78m (256 ft)                  |
| 500K bit/s  | 75m (246 ft)       | 100m (328 ft)      | 100m (328 ft)      | 39m (128 ft)                  |

If you change the baud rate of the network, make sure that all devices change to the new baud rate. Mixed baud rates produce communication errors.

Complete the following steps to set the baud rate for the network.

1. Connect the network interface to the network and set its baud rate.
2. Connect the scanner to the network and set its baud rate.
3. For each device that has only y fixed baud rates (no autobaud), set the baud rate and connect it to the network.
4. Connect the remaining devices to the network and enable autobaud for each of them.

| If a device                               | Then                                                                                               |
|-------------------------------------------|----------------------------------------------------------------------------------------------------|
| has a switch to enable autobaud           | 1. Set the switch to autobaud. 2. Connect the device to the network.                               |
| does not have a switch to enable autobaud | 1. Connect the device to the network. 2. Use RSNetWorx™ for DeviceNet software to enable autobaud. |

To communicate on the DeviceNet network, each device requires its own address. In general, a device can use any address in the range of 0…63. However, we recommend that you follow the guidelines in the following table.

| Give this device                             | This address   | Notes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|----------------------------------------------|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Scanner                                      | 0              | If you have multiple scanners, give them the lowest addresses in sequence (0, 1…).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Any device on the network except the scanner | 1…61           | • Give the lower addresses to devices with 15 bytes or more of input or output data. •  Gaps between addresses are OK and have no effect on system performance. If you are uncertain of the final lay - out of your system, leave gaps between addresses. This gives you some flexibility as you develop your system.                                                                                                                                                                                                                                                                                                                                                                           |
| Computer interface to the network            | 62             | If you connect a computer directly to the DeviceNet network, use address 62 for the computer. •  Many computer interface devices use this address as their default. •  The 1784 - U2DN device can connect a computer directly to a DeviceNet network.                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| No device                                    | 63             | Always leave address 63 open. Out of the box, most DeviceNet devices are preset for address 63. •  Some devices have no switches or push button to set the address. They require software, such as RSNetWorx™ for DeviceNet software to change the address. This means that you must first place it on the network at its preset address of 63 before you can change the address. •  If another device is already using address 63, there will be an address conflict and you won’t be able to communicate with the newly connected device. •  Leaving address 63 open makes it possible to configure a new device. •  The auto - address recovery feature also requires address 63 to be open. |

## Required Software

Refer to Chapter 3 on page 29 for more information on how to assign an address to each device.

You must use the correct software with the DeviceNet application.

- To connect your computer to the DeviceNet network, use RSLinx® communication software.
- To program the Logix 5000 controller, use Logix Designer application.
- To the configure the DeviceNet network, use RSNetWorx™ for DeviceNet software.

## Connection Options

## Connect a Computer to the DeviceNet Network

This chapter shows how to connect a computer to the network. After you physically connect a computer to the network, you must configure a driver in RSLinx® communication software to communicate over the network.

| Topic                       | Page    |
|-----------------------------|---------|
| Connection Options          | page 23 |
| Set Up the DeviceNet Driver | page 24 |

After you connect a computer to the network and configure a driver in RSLinx® communication software, you can complete these tasks:

- Configure the devices on the network
- Configure network parameters
- Upload, download, monitor, and program projects for Logix 5000™ controllers

Some networks let you bridge to other networks in your system. This lets you connect to one network and access devices or controllers on other networks.

To access the DeviceNet network, do one of thees options:

- Connect directly to the network via the 1784-U2DN interface device. If you connect directly to a DeviceNet network, you can access only the devices on that network. If you use this method, refer to Set Up the DeviceNet Driver on page 27 .

The graphic shows a computer connected directly to a DeviceNet network.

<!-- image -->

- Connect to a different network and bridge to the desired DeviceNet network. This requires no additional programming.

## Set Up the DeviceNet Driver

## Obtain the Driver for the Interface Device

## Verify that the Driver Works

The graphic shows a computer connected to a DeviceNet network through an EtherNet/IP network used with a ControlLogix® system.

<!-- image -->

For more information about installing modules on the DeviceNet network, refer to the Rockwell Automation Literature Library at:

http://www.rockwellautomation.com/literature/ .

To find the installation publications specific to your module, search by the module's catalog number.

The requirements for setting up the DeviceNet driver depend on your version of RSLinx® Classic software.

| RSLinx® Classic Software Version   | Action                                                                                                                             |
|------------------------------------|------------------------------------------------------------------------------------------------------------------------------------|
| 2.50 or earlier                    | Upgrade to version 2.51 or later to use the 1784 - U2DN interface device.                                                          |
| 2.51, 2.52, or 2.53                | Proceed to Obtain the Driver for the Interface Device on page 27 .                                                                 |
| 2.54 or later                      | The 1784 - U2DN interface device driver is already installed on the computer. Proceed to Verify that the Driver Works on page 27 . |

Follow these steps to download and install the device driver for the 1784-U2DN interface device.

## To obtain the driver for the interface device

1. Visit http://www.rockwellautomation.com/knowledgebase/ .
2. Open tech note ID 53280 and follow the instructions to install the driver.

Complete these steps to verify that the driver for the 1784-U2DN interface device works.

## To verify that the driver works

1. Open RSLinx® Classic software.

2. Select the Browse button and verify that the 1784-U2DN interface appears under USB.

<!-- image -->

## Before You Begin

Set the Node Address of a Device

## Connect Devices to the Network

This chapter describes how to connect a device to the network and set the device's address so it can communicate on the DeviceNet network.

Before you use this chapter, make sure that you can see all your devices on the DeviceNet network. Complete the steps to see your DeviceNet network.

## Before you begin

1. Start RSLinx® communication software.
2. Browse the network.
3. Expand a driver that lets you access the DeviceNet network.
4. Select the DeviceNet network.
5. Verify that you see all the devices that are connected to the DeviceNet network.

<!-- image -->

Use these options to set the node address of DeviceNet devices. However, not all options apply to every DeviceNet device.

For example, you can use all three options with the 1756-DNB ControlLogix®

## Set Node Address via Hardware Mechanism

DeviceNet scanner, but you can use only the second and third methods with the 1769 -SDN Compact I/O™ DeviceNet scanner.

- Set Node Address via Hardware Mechanism on page 28
- Set Node Address via Software on page 29
- Set Node Address via DeviceNet Node Commissioning Tool on page 31

All DeviceNet devices ship with their node addresses set to 63. To avoid duplicate node number conditions on the network, you should change the node address for each device to a unique number as you add it to the network.

| Give this address   | To this device                                                                                                                                                                            |
|---------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0                   | Scanner                                                                                                                                                                                   |
| 1…61                | Devices                                                                                                                                                                                   |
| 62                  | Computer interface to the network, such as a 1784 - U2DN device                                                                                                                           |
| 63                  | None Out of the box, a DeviceNet communication module is preset for address 63. Leaving address 63 open lets you get a new device on the network without conflicting with another device. |

For more information about setting the node address of DeviceNet devices, refer to the Rockwell Automation Literature Library at: http://www.rockwellautomation.com/literature/ .

To find the publications specific to your module, search by the module's catalog number.

Many DeviceNet devices have a hardware mechanism that you can use to set the node address. If a device has a hardware mechanism to set the node address, use that mechanism.

The table describes the two most common hardware mechanisms.

<!-- image -->

<!-- image -->

| Mechanism           | Graphic   | Description                                                                                                                                                                                                                                                                                                               |
|---------------------|-----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Rotary switch       |           | You turn the dials of rotary switches to specific numbers that represent the device’s node address. You usually need a small flathead screwdriver to turn the switches. A device reads the switches when you power it up. If you change the address, you should cycle power to that device for the change to take effect. |
| Push - wheel switch |           | You set the numbers on the push - wheel switch to specific numbers that represent the device’s node address.                                                                                                                                                                                                              |

## Set Node Address via Software

IMPORTANT As long as a device's hardware mechanism sets the node address to 63 or lower, you cannot change the node address with RSNetWorx™ for DeviceNet software or the DeviceNet node commissioning tool.

Make sure each device's node address set by a hardware mechanism matches the node address used in your RSNetWorx™ for DeviceNet software network configuration file, as described on page 40 .

However, if you set a device's hardware mechanism to a number higher than 63, you can use RSNetWorx™ for DeviceNet software or the DeviceNet node commissioning tool to set the node address.

IMPORTANT You must cycle power to the module for node changes set through hardware to take effect.

## You can set a device's node address in RSNetWorx™ for DeviceNet software.

IMPORTANT Setting a device's node address is only one task used when configuring a device with

RSNetWorx™ for DeviceNet software.

For complete information on how to configure all parameters with RSNetWorx ™ for DeviceNet software, including setting a device's node address, refer to Chapter 4 .

Complete the steps to set a device's node address in your network configuration file. This example uses an AC drive.

1. Double -click the device.
2. Enter the DeviceNet address for the device.

3. Select OK to close the configuration window.

<!-- image -->

## Set Node Address via DeviceNet Node Commissioning Tool

Use the DeviceNet node commissioning tool available in RSNetWorx™ for DeviceNet software to set the node addresses of devices on the DeviceNet n etwork. Remember these guidelines when you decide to use the DeviceNet node commissioning tool.

- You can only use this tool with a DeviceNet network that is online.
- You can only use this tool as you add new devices to the network that either do not have hardware mechanisms to set their node address or have their hardware mechanism set to a number higher than 63.

If you add a device to the network with a hardware mechanism setting the node address to 63 or lower, this tool does not change the device's node address.

- You should complete the tasks described in this section each time a new device is added to the network.
- If you add more than one device to the online network before using the DeviceNet node commissioning tool, you will experience duplicate node address conflicts on the network because all new devices initially use node address 63.
- Keep track of the node addresses you set with the DeviceNet node commissioning tool and verify they match the device's configuration in the RSNetWorx™ for DeviceNet software configuration file.

Complete these steps to use the DeviceNet node commissioning tool to set a device's node address. This example uses the 1769-SDN Compact I/O™ DeviceNet Scanner module.

1. Verify that the network is online.
2. Connect a device to the DeviceNet network.
3. Choose Start&gt;Programs&gt;Rockwell Software&gt;RSNetWorx™ for DeviceNet&gt;DeviceNet node commissioning tool .

or

From the Tools pull-down menu in RSNetWorx™ for DeviceNet software, choose Node Commissioning .

4. Select Browse .
5. On the Device Selection dialog box, select the I want to input the address for the device on the selected network box.
6. Browse to the DeviceNet network.
7. Type the current address for the device. Out of the box, devices use address 63.

<!-- image -->

## Make Sure Your Devices Are on Your Network

## 8. Select OK .

<!-- image -->

9. When you return to the Node Commissioning dialog box, enter the new address for the device.
10. S Select Apply .
11. Look for confirmation.
- If you need to use the DeviceNet node commissioning tool to set another device's node address, return to the Set Node Address via Software on page 29 step and repeat the process.

<!-- image -->

Once you have assigned a node address to each device, make sure that the devices are communicating on the network. Complete these steps to make sure your devices are on the network.

1. Start RSLinx® communication software.
2. Go online.
3. Expand a driver that lets you access the DeviceNet network.
4. Browse to the DeviceNet network.
5. Make sure you see all the devices that are connected to the DeviceNet network.

## Create a File for the Network

## Configure the Network Offline

This chapter describes how to configure the network offline with RSNetWorx™ for DeviceNet software.

| Topic                                                    | Page    |
|----------------------------------------------------------|---------|
| Before You Begin                                         | page 49 |
| Create a File for the Network                            | page 33 |
| Create Your Network in RSNetWorx™ for DeviceNet Software | page 34 |
| Configure Each Device                                    | page 35 |
| Configure the Scanner                                    | page 38 |
| Save the Configuration File                              | page 44 |
| Generate an RSNetWorx™ for DeviceNet Report              | page 44 |
| Download Configuration to Your Network                   | page 48 |

Complete these steps to create a DeviceNet configuration file.

## To create a file for the network

1. Start RSNetWorx™ for DeviceNet software.
2. Create a file.
3. Select DeviceNet Configuration .
4. Select OK .
5. Save the file.

<!-- image -->

## Before You Begin

Make sure you give the file a name that identifies this specific DeviceNet network.

Before you configure the DeviceNet network, make sure you have a list of the devices that you put on the DeviceNet network and, at minimum, the address for each. The following table shows an example list of devices.

| Device                 | Address   | Input Size of Device (Bytes)   | Input Memory in Scanner (DINTs)   | Output Size of Device (Bytes)   | Output Memory in Scanner (DINTs)   |
|------------------------|-----------|--------------------------------|-----------------------------------|---------------------------------|------------------------------------|
| scanner                | 0         | n/a                            | n/a                               | n/a                             | n/a                                |
| PanelView™ terminal    | 3         | 128                            | 32                                | 128                             | 32                                 |
| <empty>                |           |                                | 2                                 |                                 | 2                                  |
| I/O adapter w/ modules | 5         | 9                              | 3                                 | 5                               | 2                                  |
| <empty>                |           |                                | 2                                 |                                 | 2                                  |
| drive                  | 7         | 4                              | 1                                 | 4                               | 1                                  |
| <empty>                |           |                                | 2                                 |                                 | 2                                  |
| photoeye               | 9         | 1                              | 1                                 | 0                               | 0                                  |
| computer interface     | 62        | n/a                            | n/a                               | n/a                             | n/a                                |
|                        | 63        |                                |                                   |                                 |                                    |
|                        | Total     |                                | 43                                |                                 | 41                                 |

## Create Your Network in RSNetWorx for DeviceNet Software

Before you configure a DeviceNet communication module in RSNetWorx™ for DeviceNet software, you must add it to the network configuration file.

The finished picture should match the collection of devices that are or will be physically connected to the DeviceNet network. If the network configuration file you create offline does not match the physical collection of devices on the network, you may experience issues when you go online with your project.

Complete these steps to add each device to network configuration file.

1. Browse the hardware list for the device.
2. If there is a [+] sign next to the device, click the sign to expand the choices in that section.
3. Double -click the major revision of the device.
4. We recommend that the major revision of all devices added to the offline network match the devices that will be connected to the online network.
4. For a device without a list of major revisions, that is, no [+] or [-] sign, double -click the device.

## Configure Each Device

<!-- image -->

If the hardware list does not show a device, then RSNetWorx™ for DeviceNet software requires the EDS file for the device.

To add an EDS file, use these steps.

1. To see if an EDS file is available, go to this site:
2. http://www.rockwellautomation.com/resources/eds/
2. Use the EDS wizard of RSNetWorx™ for DeviceNet software to register the file and see it.

<!-- image -->

After adding devices to the network configuration file, as described in Create Your Network in RSNetWorx™ for DeviceNet Software on page 39, you configure parameters for each device to define the modules' behavior.

IMPORTANT You can configure most devices as you add them to the network configuration file or you can add all the devices and then configure them.

Typically, you add a network scanner to the network first. In this case, we recommend that you add all devices to the network configuration file before configuring the scanner. Multiple parameters that need to be configured in the scanner's configuration, for example, building a scan list, require you to choose from devices on the network. Refer to Configure the Scanner on page 44 for more information.

## Specify a Device Node Address

Complete these tasks when configuring DeviceNet communication modules:

- Specify a Device Node Address on page 36
- Configure Device Parameters on page 38

These options are available to set a device's node address:

- Hardware mechanism, as described on page 30
- RSNetWorx™ for DeviceNet software, as described in this chapter
- DeviceNet node commissioning tool, as described on page 33

All DeviceNet devices ship with their node addresses set to 63. To avoid duplicate node number conditions on the network, you should change the node address for each device to unique numbers.

| Give this address   | To this device                                                                                                                                                                            |
|---------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0                   | Scanner                                                                                                                                                                                   |
| 1…61                | Your devices                                                                                                                                                                              |
| 62                  | Computer interface to the network, such as a 1784 - U2DN device                                                                                                                           |
| 63                  | None Out of the box, a DeviceNet communication module is preset for address 63. Leaving address 63 open lets you get a new device on the network without conflicting with another device. |

When you create your network in RSNetWorx™ for DeviceNet software , devices are automatically assigned node addresses based on the order in which they were added to the network. The number appears below the device's graphic on the screen as shown below.

<!-- image -->

As you create the network, consider that if you used a hardware mechanism to assign a node address for a device, that number takes precedence over any number you assign in RSNetWorx™ for DeviceNet software.

Make sure the numbers assigned by the hardware mechanism and in your configuration file are the same for each device. For example, if the node address for a 1756 -DNB ControlLogix® DeviceNet Scanner is set to 2 via a

## Change a Device Node Address

hardware mechanism, but in the RSNetWorx™ for DeviceNet software configuration file, the node address is 0, you need to change the address in the software to 2.

- The node addresses that are automatically assigned as you add devices to the configuration file do not take effect when the project is offline.
- For devices that do not have hardware mechanisms, the node number assigned in the network configuration file takes effect when you download the project to the DeviceNet network, as described on page 55 .

You may need to assign a device's node address that is different from the number automatically assigned when the device is added to the configuration file. Complete these steps to assign a device a specific node address.

1. Double -click the device.
2. Enter the node address for the device.
3. Select OK .

<!-- image -->

<!-- image -->

## Configure Device Parameters

## Configure the Scanner

Complete these steps to configure device parameters.

1. Double -click the device to display the configuration dialog box.
2. Select the appropriate tab.
3. Set a parameter to the desired new value.

<!-- image -->

Typically, there are two methods to set a parameter:

- Choose a parameter from a pull-down menu
- Type a new value
4. Select Apply to apply the change and leave the configuration dialog box open, or select OK to apply the change and close the configuration dialog box.

<!-- image -->

Complete these steps to configure the scanner.

## To configure the scanner

1. Type a name for the scanner.
2. Enter a node number.
3. Enter the slot number.
4. Enter the minor revision.
5. Enter the size of the input and output memory maps that the scanner will allocate for each device it detects on the network.

Valid values range from 0…32 bytes per node.

6. If you need to make additional configuration changes, such as setting the requested packet interval (RPI), check Open Module Properties.
7. Select OK .
8. If the Module Properties dialog box appears, make additional configuration changes.

<!-- image -->

You can change scanner configuration on these tabs:

- General
- Connection
- RSNetWorx™

## Build the Scan List

<!-- image -->

A scan list is a list of devices with which the scanner communicates. For each device in the scanner's scan list, the scanner sets aside input or output memory for the data of the device.

<!-- image -->

Complete these steps to build a scan list.

1. Double -click the scanner to open the configuration dialog box, or, if the scanner configuration has already been uploaded and the configuration dialog box is open, go to step 2.
2. Select the Scanlist tab. The devices on the network appear in the Available Devices column.
3. Clear or select Automap on Add .

<!-- image -->

RSNetWorx™ for DeviceNet software can automatically assign the memory location for each device.

- If you want to leave gaps between devices in the memory, as shown below, clear the box.

Leave Gaps Between Devices

<!-- image -->

- If you want to place devices in sequential DINT's, as shown below, leave the box checked. When you check the box, the software automatically assigns a memory location for each device as you add it to the scan list.

Place Devices in Sequential DINTs

## Place Devices in Sequential DINTS

## Memory

<!-- image -->

| Device at Address 1   |
|-----------------------|
| Device at Address 2   |
| Device at Address 3   |

Move devices from the Available Devices column to the Scanlist column.

## Set the Alignment Option

If you get this warning for a device, see Set the I/O Parameters of a Device on page 140.

<!-- image -->

Choose a data alignment option to map the I/O data so that it is aligned on a boundary, such as a byte, word, or double-word, or efficiently grouped without alignment in the input or output memory map. To map I/O data so it is grouped without alignment, click the Pack Align option.

IMPORTANT The alignment option you choose applies to both the input and output maps.

Complete these steps to select an alignment option.

1. Select the Input tab.
2. Select Options .
3. Select the desired data alignment.
4. Select OK to close the Automap Options dialog box.

<!-- image -->

## SoftLogix 5800 Controller

## Manually Assign Each Device to a Memory Location

The SoftLogix™ 5800 scanner 1784-PCIDS organizes its input and output memory in 16-bit words. For that scanner, click the Word Align option.

<!-- image -->

You can manually assign locations for device data.

IMPORTANT If you configured the software to automatically assign memory locations as devices are added, as described on page 45, skip this section.

1. Select the Input tab.
2. Select the device.
3. In the Start DWord field, enter the element number to which you want to assign the data.

<!-- image -->

This is the starting point for the data. Larger data sizes wrap to several elements. For example, to start the data in . . . Data[3], enter 3 in the Start DWord box.

4. Select Automap .

## Save the Configuration File

## Generate an RSNetWorx for DeviceNet Report

An entry for the device appears in the input array.

<!-- image -->

5. Select the Output tab and repeat the steps above.
6. Select OK to complete the scanner configuration.

Sometimes, a specific input or output value may end up as the upper bytes of a DINT in the scanner.

| Instance 70 Data Format (Basic Speed Control Input Assembly)   | Instance 70 Data Format (Basic Speed Control Input Assembly)   | Instance 70 Data Format (Basic Speed Control Input Assembly)   | Instance 70 Data Format (Basic Speed Control Input Assembly)   | Instance 70 Data Format (Basic Speed Control Input Assembly)   | Instance 70 Data Format (Basic Speed Control Input Assembly)   | Instance 70 Data Format (Basic Speed Control Input Assembly)   | Instance 70 Data Format (Basic Speed Control Input Assembly)   | Instance 70 Data Format (Basic Speed Control Input Assembly)   |
|----------------------------------------------------------------|----------------------------------------------------------------|----------------------------------------------------------------|----------------------------------------------------------------|----------------------------------------------------------------|----------------------------------------------------------------|----------------------------------------------------------------|----------------------------------------------------------------|----------------------------------------------------------------|
| Byte                                                           | Bit 7                                                          | Bit 6                                                          | Bit 5                                                          | Bit 4                                                          | Bit 3                                                          | Bit 2                                                          | Bit 1                                                          | Bit 0                                                          |
|                                                                |                                                                |                                                                |                                                                |                                                                |                                                                | Running1                                                       |                                                                | Fa ulted                                                       |
| 一                                                             |                                                                |                                                                |                                                                |                                                                |                                                                |                                                                |                                                                |                                                                |
| 2                                                              | Speed Actual RPM (Low Byte)                                    | Speed Actual RPM (Low Byte)                                    | Speed Actual RPM (Low Byte)                                    | Speed Actual RPM (Low Byte)                                    | Speed Actual RPM (Low Byte)                                    | Speed Actual RPM (Low Byte)                                    | Speed Actual RPM (Low Byte)                                    | Speed Actual RPM (Low Byte)                                    |
|                                                                | Speed Actual RPM (High Byte)                                   | Speed Actual RPM (High Byte)                                   | Speed Actual RPM (High Byte)                                   | Speed Actual RPM (High Byte)                                   | Speed Actual RPM (High Byte)                                   | Speed Actual RPM (High Byte)                                   | Speed Actual RPM (High Byte)                                   | Speed Actual RPM (High Byte)                                   |

To make your programming easier, use advanced mapping to re-map the value to its own memory location. For more information, see Map the Memory Location with Advanced Mapping on page 153 .

After you make a change to the network, upload the entire network and save the file. This makes sure that the offline configuration file matches the network.

Complete these steps to save the configuration file.

1. From the Network menu, choose Upload from Network.
2. When prompted, select Yes to upload the entire network.
3. Save the file.

An RSNetWorx™ for DeviceNet report shows these items:

- Devices on the network
- Memory addresses of those devices in the scanner
- Device configurations

The report is a useful reference when you program your system. Complete these steps to generate a report.

1. From the File menu in RSNetWorx™ for DeviceNet software, choose Generate Report .
2. Select Generate report for entire network .

<!-- image -->

<!-- image -->

The report appears in your web browser.

<!-- image -->

## Go Online to Your Network

When you go online, RSNetWorx™ for DeviceNet software browses the network once and shows the devices currently on the network in the new network configuration file.

Keep this in mind when you go online:

- RSNetWorx™ for DeviceNet software does not read (upload) or change (download) the parameters of any of the devices on the network.
- The picture that results from browsing remains static. It does not show any changes since the last browse.

## To go online to your network

1. Select Online .
2. Select the DeviceNet network.

3. Select OK .
4. When the pop-up message appears, select OK .
5. Verify that you are online.

<!-- image -->

<!-- image -->

<!-- image -->

## Download Configuration to Your Network

After you go online with the network configuration file you created while offline, you can download the configuration to the network.

IMPORTANT Before you download configuration to the network, make sure the scanner is in Idle mode. To put the scanner in Idle mode, do one of the following:

- Place the controller in program/remote program mode.
- Turn off the …O.CommandRegister.Run bit of the scanner.

Complete these steps to download configuration to the DeviceNet network.

1. From the File menu in Network&gt;Download to Network .
2. When prompted, select Yes to download the entire network.

<!-- image -->

<!-- image -->

## Before You Begin

## Configure the Network Online

This chapter explains how to configure the network online with RSNetWorx™ for DeviceNet software.

| Topic                                                 | Page    |
|-------------------------------------------------------|---------|
| Before You Begin                                      | page 49 |
| Verify Communication Between the Computer and Devices | page 50 |
| Create a New File for the Network                     | page 33 |
| Go Online to Your Network                             | page 46 |
| Configure Each Device                                 | page 35 |
| Configure the Scanner                                 | page 38 |
| Upload and Save the Configuration File                | page 63 |
| Generate an RSNetWorx™ for DeviceNet Report           | page 44 |

Configuring the network online reduces the number of configuration tasks you must complete compared to configuring the network offline. Configuring the network online has these advantages:

- Devices on the network automatically appear in your network configuration file as soon as you go online. You do not need to add the devices to the network configuration file.
- The network configuration file automatically matches the physical setup of devices on the network as well as the major and minor revisions of the online devices.
- The configuration is guaranteed to match the major and minor revisions of the online devices.
- You can easily upload device configurations to your network configuration file, make changes to the configuration parameters, and download them to the device.

Before you configure the network, make sure you have a list of the devices that are on the network and, at minimum, the node address for each of them. The following table shows an example list of devices.

| Device                 | Address   | Input Size of Device (Bytes)   | Input Memory in Scanner (DINTs)   | Output Size of Device (Bytes)   | Output Memory in Scanner (DINTs)   |
|------------------------|-----------|--------------------------------|-----------------------------------|---------------------------------|------------------------------------|
| scanner                | 0         | n/a                            | n/a                               | n/a                             | n/a                                |
| PanelView™ terminal    | 3         | 128                            | 32                                | 128                             | 32                                 |
| <empty>                |           |                                | 2                                 |                                 | 2                                  |
| I/O adapter w/ modules | 5         | 9                              | 3                                 | 5                               | 2                                  |

| Device             | Address   | Input Size of Device (Bytes)   | Input Memory in Scanner (DINTs)   | Output Size of Device (Bytes)   | Output Memory in Scanner (DINTs)   |
|--------------------|-----------|--------------------------------|-----------------------------------|---------------------------------|------------------------------------|
| <empty>            |           |                                | 2                                 |                                 | 2                                  |
| drive              | 7         | 4                              | 1                                 | 4                               | 1                                  |
| <empty>            |           |                                | 2                                 |                                 | 2                                  |
| photoeye           | 9         | 1                              | 1                                 | 0                               | 0                                  |
| computer interface | 62        | n/a                            | n/a                               | n/a                             | n/a                                |
|                    | 63        |                                |                                   |                                 |                                    |
|                    | Total     |                                | 43                                |                                 | 41                                 |

## Verify Communication Between the Computer and Devices

To configure your network online, your computer must be able to communicate with each device on the DeviceNet network. Use RSLinx® communication software to verify that you can communicate with all the devices.

## To verify communication between the computer and devices

1. Start RSLinx® communication software.
2. Select the Online button.
3. Expand a driver that lets you access the DeviceNet network.
4. Select the DeviceNet network.

<!-- image -->

5. Make sure you see all the devices that are connected to the DeviceNet network.

<!-- image -->

IMPORTANT If you cannot view the network, verify that your computer is connected to the network. Refer to Chapter 2 on page 25 for more information on how to connect the computer to the network.

If you can view the network but cannot see all the devices that should be on the network, verify the devices are connected to the network. Refer to Chapter 3 on page 29 for more information on how to connect the devices to the network.

## Create a New File for the Network

Before you go online, you must create a new network configuration file.

## To create a new file for the network

1. Start RSNetWorx™ for DeviceNet software.

2. Create a file.

<!-- image -->

## Go Online to Your Network

When you go online, RSNetWorx™ for DeviceNet software browses the network once and shows the devices currently on the network in the new network configuration file.

Keep this in mind when you go online:

- RSNetWorx™ for DeviceNet software does not read (upload) or change (download) the parameters of any of the devices on the network.
- The picture that results from browsing remains static. It does not show any changes since the last browse.

## To go online to your network

1. Select Online .
2. Select the DeviceNet network.

3. Select OK .
4. When the pop-up message appears, select OK .
5. Verify that you are online.

<!-- image -->

<!-- image -->

<!-- image -->

## Configure Each Device

## Upload the Configuration of a Device

Once the devices on the DeviceNet network appear in the network configuration file, complete these tasks to change the configuration for a a device:

- Upload the Configuration of a Device on page 54
- Change and Download Device Configuration on page 54

When you configure the network online, the devices on the network have parameters configured. Complete these steps to upload configuration from a device to the network configuration file.

## To upload the configuration of a device

1. Double -click the device to open the configuration dialog box.
2. Select the Parameters tab.
3. When prompted, upload the configuration from the device to the network configuration file.

<!-- image -->

<!-- image -->

## Change and Download Device Configuration

After you upload a device's configuration to the network configuration file, you can make changes to the configuration and download it.

Complete these steps to change and download new configuration parameters.

## To change and download device configuration

1. Double -click the device to open the configuration dialog box, or, if the device configuration has already been uploaded and the configuration dialog box is open, go to step 2.

<!-- image -->

The configuration dialog box appears.

2. Select the appropriate tab .
3. Set a parameter to the desired new value.

Typically, there are two methods to change a parameter:

- Choose a parameter from a pull-down menu
- Type a new value
4. Apply the changes.
5. Select OK to close the dialog box.
6. When prompted, download the changes.

<!-- image -->

## Configure the Scanner

<!-- image -->

## Upload the Current Scanner Configuration

A DeviceNet scanner manages input and output data for a controller. The scanner receives input data from I/O devices, organizes the information into scanner data tables, and sends the input data to the controller when the controller requests it. In addition, when the scanner receives output data from the controller, it sends the data to the I/O devices.

A DeviceNet scanner is the only device that can be used as a master on a DeviceNet network. When there is only one scanner on a network, it is the master for that network by default. When there are multiple scanners on the same network, each device can have only one scanner designated as its master, which is the scanner that controls its outputs.

You must configure the scanner to define how it communicates with other devices on the DeviceNet network. When you are configuring the network online, complete these tasks to configure the scanner:

- Upload the Current Scanner Configuration on page 56
- Define the Scanner Properties on page 57
- Build the Scan List on page 39
- Set the Alignment Option on page 42

Scan list-A list in the scanner that identifies the devices with which the scanner communicates. For each device in its scan list, the scanner sets aside input or output memory for the data of the device.

<!-- image -->

Complete these steps to upload the current scanner configuration.

## To upload the current scanner configuration

1. Double -click the scanner to open the configuration dialog box.
2. Select the Module tab.
3. When prompted, upload the configuration from the scanner.

<!-- image -->

<!-- image -->

<!-- image -->

## Define the Scanner Properties

Complete these steps to change the scanner properties, if necessary.

To define the scanner properties

1. Select the Module tab.
2. Make the necessary changes.
3. Select Apply to make the changes.
4. When a message prompts you to indicate whether to download your changes to the scanner, Select No to continue configuring the scanner on additional tabs.

## Build the Scan List

<!-- image -->

<!-- image -->

A scan list is a list of devices with which the scanner communicates. For each device in the scanner's scan list, the scanner sets aside input or output memory for the data of the device.

<!-- image -->

Complete these steps to build a scan list.

1. Double -click the scanner to open the configuration dialog box, or, if the scanner configuration has already been uploaded and the configuration dialog box is open, go to step 2.
2. Select the Scanlist tab. The devices on the network appear in the Available Devices column.

3. Clear or select Automap on Add .

<!-- image -->

RSNetWorx™ for DeviceNet software can automatically assign the memory location for each device.

- If you want to leave gaps between devices in the memory, as shown below, clear the box.

Leave Gaps Between Devices

<!-- image -->

·

## Set the Alignment Option

- If you want to place devices in sequential DINT's, as shown below, leave the box checked. When you check the box, the software automatically assigns a memory location for each device as you add it to the scan list.

Place Devices in Sequential DINTs

<!-- image -->

Move devices from the Available Devices column to the Scanlist column.

If you get this warning for a device, see Set the I/O Parameters of a Device on page 140.

<!-- image -->

Use the alignment option to map the I/O data so that it is aligned on a boundary, such as a byte, word, or double-word, or efficiently grouped without alignment in the input or output memory map. To map I/O data so it is grouped without alignment, click the Pack Align option.

IMPORTANT The alignment option you choose applies to both the input and output maps.

## To set the alignment option

1. Select the Input tab.
2. Select Options .
3. Select the desired data alignment.

## SoftLogix 5800 Controller

## Manually Assign Each Device to a Memory Location

## 4. Select OK .

<!-- image -->

In SoftLogix™ 5800 applications, the 1784-PCIDS scanner organizes its input and output memory in 16-bit words. For that scanner, select Word Align .

<!-- image -->

Manually assign locations for device data.

IMPORTANT If you configured the software to automatically assign memory locations as devices are added, as described on page 70, skip this section.

## To manually assign each device to a memory location

1. Select the Input tab.

2. Select the device.
3. In the Start DWord field, enter the element number to which you want to assign the data.

<!-- image -->

This is the starting point for the data. Larger data sizes wrap to several elements. For example, to start the data in . . . Data[3], type 3 in the Start DWord box.

4. Select Automap .

An entry for the device shows up in the input array.

<!-- image -->

5. Select the Output tab and repeat step through step .
6. Select OK K to complete scanner configuration.

## Download the Configuration to the Scanner

## Upload and Save the Configuration File

Sometimes, a specific input or output value may end up as the upper bytes of a DINT in the scanner.

| Instance 70 Data Format (Basic Speed Control Input Assembly)   | Instance 70 Data Format (Basic Speed Control Input Assembly)   | Instance 70 Data Format (Basic Speed Control Input Assembly)   | Instance 70 Data Format (Basic Speed Control Input Assembly)   | Instance 70 Data Format (Basic Speed Control Input Assembly)   | Instance 70 Data Format (Basic Speed Control Input Assembly)   | Instance 70 Data Format (Basic Speed Control Input Assembly)   | Instance 70 Data Format (Basic Speed Control Input Assembly)   | Instance 70 Data Format (Basic Speed Control Input Assembly)   |
|----------------------------------------------------------------|----------------------------------------------------------------|----------------------------------------------------------------|----------------------------------------------------------------|----------------------------------------------------------------|----------------------------------------------------------------|----------------------------------------------------------------|----------------------------------------------------------------|----------------------------------------------------------------|
| Byte                                                           | Bit 7                                                          | 911                                                            | Bit 5                                                          | Bit 4                                                          | Bit 3                                                          | Bit 2                                                          | Bit 1                                                          | Bit 0                                                          |
|                                                                |                                                                |                                                                |                                                                |                                                                |                                                                | Running1                                                       |                                                                | Fa ulted                                                       |
| 一                                                             |                                                                |                                                                |                                                                |                                                                |                                                                |                                                                |                                                                |                                                                |
|                                                                | Speed Actual RPM ( Low Byte)                                   | Speed Actual RPM ( Low Byte)                                   | Speed Actual RPM ( Low Byte)                                   | Speed Actual RPM ( Low Byte)                                   | Speed Actual RPM ( Low Byte)                                   | Speed Actual RPM ( Low Byte)                                   | Speed Actual RPM ( Low Byte)                                   | Speed Actual RPM ( Low Byte)                                   |
|                                                                | Speed Actual RPM (High Byte)                                   | Speed Actual RPM (High Byte)                                   | Speed Actual RPM (High Byte)                                   | Speed Actual RPM (High Byte)                                   | Speed Actual RPM (High Byte)                                   | Speed Actual RPM (High Byte)                                   | Speed Actual RPM (High Byte)                                   | Speed Actual RPM (High Byte)                                   |

To make your programming easier, use advanced mapping to re-map the value to its own memory location. For more information, see Map the Memory Location with Advanced Mapping on page 153 .

Complete these steps to download the configuration to the scanner.

## To download the configuration to the scanner

1. Select Apply .
2. When prompted, select Yes to download the changes.
3. Select OK .

<!-- image -->

Complete these steps to upload and save the configuration file.

## To upload and save the configuration file

1. Choose Network&gt;Network&gt;Upload .
2. When prompted, select Yes to upload the entire network.
3. Save the file.

## Generate an RSNetWorx for DeviceNet Report

<!-- image -->

An RSNetWorx™ for DeviceNet software report shows these items:

- Devices on the network
- Memory addresses of devices in the scanner
- Device configurations

The report is a useful reference when you program your system. Complete these steps to generate a report.

## To generate an RSNetWrox for DeviceNet report

1. From the File menu in RSNetWorx™ for DeviceNet software, choose Generate Report .
2. Select Generate report for entire network and select OK .

<!-- image -->

<!-- image -->

The report appears in your web browser.

<!-- image -->

## How AutoScan Operates

## Automatically Configure a DeviceNet Network

This chapter provides a quick method for configuring a DeviceNet network. It uses the AutoScan feature to establish communication between the controller and the devices on the DeviceNet network with minimal steps.

| Topic                                                     | Page    |
|-----------------------------------------------------------|---------|
| How AutoScan Operates                                     | page 67 |
| Determine If You Can Use AutoScan                         | page 69 |
| How AutoScan Affects Your Network                         | page 70 |
| Install the DeviceNet Node Commissioning Tool             | page 70 |
| Connect Devices to the Network                            | page 71 |
| Add the Scanner to the Logix Designer application Project | page 73 |
| Enable AutoScan with Logix Designer application           | page 75 |
| Access Device Data                                        | page 81 |
| Put the Scanner in Run Mode                               | page 82 |
| Additional Information About AutoScan                     | page 83 |

The DeviceNet AutoScan feature enables a scanner to automatically map a network of slave devices into its scan list without the use of RSNetWorx™ for DeviceNet software. This greatly improves the ease of setting up a DeviceNet network, especially networks comprised of simple devices.

When the feature is enabled, a DeviceNet scanner continuously searches for devices on the network. Once a qualifying slave device is found, it is added to the scanner's scan list and its I/O data is mapped into a predefined location in the scanner's I/O memory table based on the device's node address.

IMPORTANT AutoScan works only with 1756-DNB and 1769-SDN modules in Logix controller applications.

AutoScan is active when the feature is enabled and the scanner is in Idle mode. When active, the scanner attempts to connect to each device not enabled in the scan list. The scanner only checks for devices with node addresses between 0 and 61, inclusive. The connections to these devices are made on a round -robin basis.

When a device is found, the scanner gets the produced and consumed data sizes from the slave device's Connection Object instances.

- If the produced data size is greater than the configured I/O allocation size, the device is added to the scan list with a produced size set equal to the I/O allocation size.

When this happens, an I/O connection is made with the device, but an error occurs and error code #77 appears on the 1769-SDN for the device's node number.

- If the consumed data size is greater than the configured I/O allocation size, then the node is rejected and not entered into the scan list.

However, you can change the I/O allocation size, as described in Configure I/O Allocation Size Via the User Program on page 78, to accommodate the device with the largest produced and consumed data sizes in your scan list.

For qualifying nodes, the scanner enters the device into the scan list and attempts to allocate an I/O connection using one of these communication format choices in this particular order:

- Change Of State (COS) EPR = 250ms
- Poll EPR = 75ms
- Strobe EPR = 75ms
- Cyclic EPR = 500ms
- EXAMPLE If a photoeye is connected on a network that only supported strobed connections, the scanner executes the following tasks:
- The scanner recognizes that a device exists for which memory is available for the node number with the configured allocation size on a network that is not currently mapped.
- The scanner attempts to initiate both COS and polled connections first, but the strobed connection is selected as that is the only connection that the photoeye supported.

The input and output data is mapped into the scanner's I/O data table based on the device's node address and the configured fixed mapping size. The DINT -based formula that is used with the CompactLogix™ controller for calculating the input or output data location is as follows:

Input (Output) Offset = [(Node Address) x (Allocation Size)] / 4

## Determine If You Can Use AutoScan

EXAMPLE

When using the default fixed mapping size of 4 bytes, the input data for the devices shown in the example below is allocated in the 1769-SDN's input table as shown below. Notice node 1 is in the data map at DINT location 1, node 2 at DINT location 2, and so on.

Notice that, in this example, node 4 is unused. However, the I/O memory slot remains allocated for it.

<!-- image -->

IMPORTANT If you are using a MicroLogix™ 1500 controller with a 1769-SDN scanner, you must use the following WORD -based formula for calculating the input or output data location: Input (Output) Offset = ([(Node Address) x (Allocation Size)] / 2) + Data Offset In this formula the Data Offset = 66 for Input Offset and 2 for Output Offset.

The data offset value is used to account for scanners that have a fixed status field at the start of the input or output data, such as the 1769-SDN scanner.

Make sure your network meets these requirements to use this chapter:

- You have completed all the tasks required to do these tasks:
- Connect a computer and devices to the network.
- Create a network configuration file.
- Go online.
- Download the configuration file to the network.

Refer to Chapter 2 through Chapter 5 to complete the tasks listed above.

- Your DeviceNet scanner must support the AutoScan feature. For more information, refer to your firmware release notes.
- Your application uses the Logix Designer application programming software, version 13 or later.
- The scanner's I/O allocation size is configured to accommodate the input and output data sizes of all devices on your DeviceNet network.

The default AutoScan setting allocates a 4-byte entry in both the input and output memory maps in the scanner for each slave device detected on the network. This default size is chosen to accommodate the default Logix native data size of 32 bits, that is a DINT.

If you use a device that sends more than 4 bytes of input or output data, such as an E3 Solid State Overload Relay (catalog number 193-ECxx), you must change the I/O allocation size.

## How AutoScan Affects Your Network

As you use AutoScan, keep in mind the considerations described in the table.

<!-- image -->

| Consideration                                                  | Description                                                                                                                                                                                                                                                                                                                                                                                         |
|----------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| AutoScan clears the current configuration.                     | With AutoScan, the scanner automatically sets up communication with the devices on your DeviceNet network. When you turn on the AutoScan option, the scanner removes any previous configuration that was done to the scanner.                                                                                                                                                                       |
| AutoScan allocates a fixed memory size for each device.        | At its default setting, AutoScan allocates 1 DINT of input memory and 1 DINT of output memory for each device on the DeviceNet network. The actual data for the device fills the portion that it needs and the rest remains unused. DINT Input Memory Device at Address 0 Device at Address 1                                                                                                       |
| The bytes/node value defines how much memory for each address. | AutoScan lets you specify how much input and output memory to give to each address on your network. For example, if you specify 2 DINTs (8 bytes) per address, the scanner sets aside 2 DINTs for each address. The actual data for the device fills the portion that it needs and the rest remains unused. DINT Input Memory 0 Device at Address 0 1 2 Device at Address 1 3 4 Device at Address 2 |
| New devices are automatically available.                       | While the scanner is in Idle mode, AutoScan continues to establish communication with devices that you connect to the network, as long as the devices use input data and output data sizes that fit in the scanner’s I/O allocation size.                                                                                                                                                           |
| The Automatic Device Recovery (ADR) option is not available.   | You have to use RSNetWorx™ for DeviceNet software to edit the configuration of the scanner to use the Automatic Device Recovery (ADR) option of a DeviceNet scanner. This turns off AutoScan.                                                                                                                                                                                                       |

## Install the DeviceNet Node Commissioning Tool

Use the DeviceNet node commissioning tool to set a device's node address and baud rate when that device does not have a hardware mechanism to do so.

You can skip this step if either of these conditions apply:

- All your devices have hardware mechanisms to set a node address and baud rate. In this case, you do not need the tool.
- You already have the tool installed.

Use these steps to install the node commissioning tool.

1. On the Logix Designer application CD, find the folder for the language of your software:
2. language\Tools\Node Commissioning Tool
3. For example, for software in English, open the ENU folder.

## Connect Devices

## Install a Scanner or Network Interface Devices

2. Follow the instructions in the readmefirst file.

When you use the AutoScan functionality, you should:

- Install and configure the scanner and any network interface devices on the network first.
- Install other devices on the network once the scanner and network interface devices are on the network.

Complete these steps to install a scanner or network interface device on the DeviceNet network.

## To install a scanner or network interface device

1. Connect the scanner and any network interface devices to the network.
2. Set a node address for the scanner and any network interface devices.

Out of the box, a DeviceNet device is preset for node address 63. To avoid address conflicts, connect and configure the devices one at a time. Otherwise, the address conflicts may prevent communication.

These addresses are recommended but not required.

| Give this address   | To this device                                                                                                                                                                                   |
|---------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0                   | Scanner.                                                                                                                                                                                         |
| 1…61                | Your devices.                                                                                                                                                                                    |
| 62                  | Computer interface to the network, such as a 1784 - U2DN or 1788 - PCIDS device.                                                                                                                 |
| 63                  | Leave open. Out of the box, a DeviceNet communication module is preset for address 63. Leaving address 63 open lets you get a new device on the network without conflicting with another device. |

- Refer to Set the Node Address of a Device on page 30 for more information on several options you can use to set the node address.
- Refer to Set the Node Address and Baud Rate with the DeviceNet Node Commissioning Tool on page 87 7 on for more information on how to use just the DeviceNet node commissioning tool.
1. Set a baud rate for the scanner and any network interface devices.

When setting baud rates, consider:

- If you set the baud rate on the scanner or network interface device before you install other devices on the network, you reduce the number of baud rate errors.
- Scanners and network interface devices use a fixed baud rate.
- Sensors and similar DeviceNet communication modules use autobaud to set their baud rate. They wait for another device to

## Install Other DeviceNet Devices

communicate. Then they set their baud rate to the same baud rate as the other device.

- By first placing a scanner or network interface device on the network, the other device has a network baud rate against which to set its baud rate.
- Initially, leave the baud rate of the scanner and network interface at the default setting of 125KBps. If you want to change the baud rate, wait until after you establish communication with all your devices at the default setting (125K).
- Refer to Set the Node Address and Baud Rate with the DeviceNet Node Commissioning Tool on page 87 7 for more information.

Complete these steps to install other devices on the DeviceNet network.

## To install other DeviceNet devices

1. Connect the rest of your devices to the network one at a time.
2. Set a node address for each device after you add it to the network.

Out of the box, a DeviceNet device is preset for node address 63. To avoid address conflicts, connect and configure the devices one at a time. Otherwise, the address conflicts may prevent communication.

These addresses are recommended but not required.

| Give this address   | To this device                                                                                                                                                                                   |
|---------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0                   | Scanner                                                                                                                                                                                          |
| 1…61                | Your devices                                                                                                                                                                                     |
| 62                  | Computer interface to the network, such as a 1784 - U2DN or 1788 - PCIDS device                                                                                                                  |
| 63                  | Leave open. Out of the box, a DeviceNet communication module is preset for address 63. Leaving address 63 open lets you get a new device on the network without conflicting with another device. |

- Refer to Set the Node Address of a Device on page 30 for more information on how to use any of several options to set the node address.
- Refer to Set the Node Address and Baud Rate with the DeviceNet Node Commissioning Tool on page 87 7 for more information on how to use the DeviceNet node commissioning tool.
1. Set a baud rate for each device after you add it to the network.

When setting baud rates, consider:

- Sensors and similar DeviceNet communication modules use autobaud to set their baud rate. They wait for another device to

Set the Node Address and Baud Rate with the DeviceNet Node Commissioning Tool

## Add the Scanner to the Logix Designer application project

Add the Scanner to the I/O Configuration Folder

- communicate. Then they set their baud rate to the same baud rate as the other device.
- If a device has a hardware mechanism to set its baud rate, set it to autobaud, if available. Otherwise, set the device to the baud rate of the network.
- After you change the address or baud rate of a device via a switch, cycle power to the device.
- If a device has no hardware mechanism to set its address or baud rate, Refer to Set the Node Address and Baud Rate with the DeviceNet Node Commissioning Tool on page 87 .
- After you set the address of a device, check its network status indicator. Typically, a solid red indicator signifies an address conflict or problem with the baud rate.

Complete these steps to set a node address and baud rate with the DeviceNet node commissioning tool.

## To set the node address and baud rate with the DeviceNet Node Commissioning Tool

1. Start the node commissioning tool.
2. Select Browse .
3. Select I want to input the address for the device on the selected network .
4. Select the DeviceNet network.
5. Enter the current address for the device. Out of the box, a device uses address 63.
6. Select OK .
7. Enter the new address for the device.
8. Choose the baud rate for the device.
9. Select Apply .

To access the data of the network, add the scanner to the I/O configuration of the controller.

Complete these steps to add the scanner to the I/O configuration file.

## To add the scanner to the I/O Configuration Folder

1. Right-click and choose New Module .
2. Select the type of scanner.
3. Select OK .

## Define the Properties of the Scanner

4. From the Major Revision pull-down menu, choose a major revision number for the scanner.
5. Select OK .

<!-- image -->

<!-- image -->

<!-- image -->

Type a name for the scanner.

## To define the properties of the scanner

1. Enter the scanner node number.
2. Enter the scanner slot number.
3. Enter the scanner minor revision.
4. Enter the size of the input and output memory maps that the scanner will allocate for each device it detects on the network.
5. Valid values range from 0…32 bytes per node.

## Enable AutoScan with the Logix Designer application

5. If you need to make additional configuration changes, such as setting the Requested Packet Interval (RPI), select Open Module Properties .
6. Select OK .
7. If the Module Properties dialog box appears, make any additional configuration changes.

<!-- image -->

To enable AutoScan with the Logix Designer application, use these steps.

## To enable AutoScan with the Logix Designer application

1. Save changes to your project.
2. Download the project to the Logix 5000™ controller.

IMPORTANT In these steps, you clear any existing configuration from the scanner and reconfigure it to communicate with the devices on the network. In the controller, this may change the tag addresses of the devices. If you have already programmed your logic, make sure that it still addresses the correct data.

3. Double -click the scanner in the Controller Organizer to access its properties.
4. Select the Scan List tab. A blue dot in the Nodes in Scan List section indicates a device that the scanner now controls.
5. Select Enable AutoScan .
6. When the Enable AutoScan w warning appears, select OK .

<!-- image -->

## Initiate AutoScan via the User Program

<!-- image -->

<!-- image -->

To enable AutoScan by using the MSG instruction, use the parameters shown below and make sure that the message is sent to the appropriate DeviceNet scanner. The figure shown below is from the Logix Designer application. Refer to the appropriate user manuals to determine how to perform explicit messaging in other PLC platforms.

<!-- image -->

This data tag should be configured as a SINT. Upon execution of the MSG, AutoScan is:

Enabled if tag = 1

Disabled if tag = 0

## Implement AutoScan

To implement this feature, make sure that the appropriate version of DeviceNet scanner is used. See page 80 for the list of compatible products supporting this feature.

This section describes how to set up the feature and how it operates. Notice that explicit messaging is used for some of the steps. An explicit message can be sent on a DeviceNet network in these ways:

- A user ladder program
- External programming/configuration devices, such as the hand-held DeviceNet Configuration Terminal, catalog number 193-DNCT
- RSNetWorx™ for DeviceNet software

Since the purpose of the feature is to eliminate the use of RSNetWorx™ for DeviceNet software, instructions on how to send an explicit message via the class instance editor in the software are not covered in this document.

To implement the feature, use these steps.

## To implement AutoScan

1. Set up the physical network.

Make sure all devices are addressed appropriately. For example, be sure there are no address conflicts and devices are communicating at the same baud rate.

The diagram below shows an example system using the 1756 -DNB scanner.

<!-- image -->

You can commission the node addresses via hardware switches on the devices or through other DeviceNet configurators, such as the

## Configure I/O Allocation Size Via the User Program

hand -held DeviceNet Configuration Terminal. For more information on how to set up the DeviceNet Configuration Terminal's node address, see the DeviceNet Configuration Terminal User Manual, publication 193-UM009A-EN-P .

2. Set up I/O allocation size in the scanner.

<!-- image -->

Tip: This step is optional.

The default AutoScan setting allocates a 4-byte entry in both the input and output memory maps in the scanner for each slave device detected on the network. This default size is chosen to accommodate the default Logix native data size of 32 bits (DINT). If that is adequate for the application, go to step 3.

For applications where you want to customize the I/O allocation size, the 4 -byte allocation can be adjusted through an explicit message to the scanner using the SetAttributeSingle service. The entry allocation can be configured for 1 to 32 bytes per node.

Configure the allocation size using one of these methods:

- Configure I/O Allocation Size Via the User Program on page 78
- Configure I/O Allocation Via a DeviceView™ Configurator on page 78

Use the parameters shown in the Message Configuration dialog box below to adjust the I/O allocation size. Make sure that the message is sent to the appropriate DeviceNet scanner.

<!-- image -->

## Configure I/O Allocation Via a DeviceView Configurator

This data tag should be configured as an SINT, and should contain the value of the desired per -node fixed mapping size (1 -32).

Rockwell Automation offers the hand -held DeviceNet Configuration Terminal, catalog number 193-DNCT, to configure individual devices on a DeviceNet network.

To configure the I/O allocation size, attach a configurator device on the network and send an explicit message to the scanner by using the parameters

## Initiate AutoScan via the User Program

below. Send the desired allocation size (1…32 bytes) to the attribute below to configure the per-node I/O allocation.

| Field        | Value   |
|--------------|---------|
| Service Code | 10 Hex  |
| Class        | 90 Hex  |
| Instance     | 1       |
| Attribute    | 11 Hex  |

For more information on how to use the DeviceNet Configuration Terminal, refer to these publications:

- 193 -DNCT DeviceNet Configuration Terminal Quick Reference, publication 193-QR002A-EN-P
- DeviceNet Programming Terminal User Manual, publication 193 -UM009A-EN-P

IMPORTANT You can change the I/O allocation size only when the scanner is in Idle mode, and the AutoScan feature is disabled.

- Enable AutoScan.

This is accomplished by executing an explicit message to the scanner by using the SetAttributeSingle service. As mentioned before, there are multiple ways to send an explicit message on DeviceNet, including:

- Initiate AutoScan Via the User Program on page 76
- Initiate AutoScan via the DeviceView™ Configurator on page 80

To enable AutoScan by using the MSG instruction, use the parameters shown below and make sure that the message is sent to the appropriate DeviceNet scanner. The figure shown below is from the Logix Designer application. Refer to the appropriate user manuals to determine how to perform explicit messaging in other PLC platforms.

<!-- image -->

This data tag should be configured as a SINT. Upon execution of the MSG, AutoScan is:

Enabled if tag = 1

Disabled if tag = 0

## Initiate AutoScan via the DeviceView Configurator

## Additional Considerations Regarding AutoScan

To enable AutoScan by using a DeviceNet configurator, attach the device on the network and send an explicit message to the scanner using the parameters below. Send a 1 to that attribute to enable the feature, and 0 to disable.

| Field        | Value   |
|--------------|---------|
| Service Code | 10 Hex  |
| Class        | 90 Hex  |
| Instance     | 1       |
| Attribute    | 11 Hex  |

For more information on how to use the DeviceNet Configuration Terminal, refer to these publications:

- 193 -DNCT DeviceNet Configuration Terminal Quick Reference, publication 193-QR002A-EN-P
- DeviceNet Programming Terminal User Manual, publication 193 -UM009A-EN-P .

IMPORTANT You can change the I/O allocation size only when the scanner is in Idle mode, and the AutoScan feature is disabled.

Once the feature is enabled, the scanner scans the network to populate and configure the scan list automatically.

1. Put scanner in RUN mode to begin system operation.

The factory default setting for AutoScan is disabled for all products.

Make sure that input or output data memory size in the scanner is large enough to accommodate the size required based on the number of nodes on the network and the AutoScan I/O allocation size per node.

EXAMPLE If the I/O allocation size per node is configured for 16 bytes and there are 32 slave devices on the network (node addresses 1…32), AutoScan requires 16 bytes x 32 = 512 bytes (128 DINT) of I/O space in both the scanner's input and output table. Assuming it is a ControlLogix® system, the maximum scanner input data table size is 124 DINT and 123 DINT for output. The required space exceeds what the 1756 -DNB can support. You would need to adjust the I/O allocation size or reduce the slave device count on the network to include all of the devices in the scan list.

<!-- image -->

ATTENTION: Devices outside of the scanner's allowable I/O image space will be rejected and will not be included in the scan list.

The AutoScan feature is automatically disabled in the scanner as soon as a scanner property is modified by RSNetWorx™ for DeviceNet software. For example, any manual changes to the scan list using RSNetWorx™ for DeviceNet software disables the AutoScan feature in the scanner.

## Access Device Data

One new status code has been added to the Node Status list. This code is presented in the Node Status Table.

|   Status Code (Decimal) | Description of Status                 |
|-------------------------|---------------------------------------|
|                      65 | AutoScan Active (Scanner only status) |

When the scanner is in Run mode with AutoScan enabled, the scanner display alternates between 65 and the scanner node address.

When a scanner is transitioned from Run mode to Idle mode while AutoScan is enabled, it only scans the network for nodes that are not already in the scan list. However, while in Idle mode, an AutoScan DISABLE to ENABLE transition causes the scanner to erase the existing scan list and scan for all nodes on the network.

The AutoScan feature enables AAR (Auto-Address Recovery) for each of the configured slave devices.

The A AutoScan feature checks for the Quick Connect setting in each slave device and enables Quick Connect in the scanner if it is enabled in the slave devices.

When you add the scanner to the I/O configuration of the controller, the Logix Designer application software automatically creates a set of tags for the input, output, and status data of the network.

<!-- image -->

The tags for your DeviceNet data follow this format.

<!-- image -->

| Where    | Is                                    |
|----------|---------------------------------------|
| location | location of the scanner in the system |

| Where        | Is                                                                              |                                                                                 |                                                                                                                          |
|--------------|---------------------------------------------------------------------------------|---------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|
|              | If you have this scanner                                                        | In a                                                                            | Then location is                                                                                                         |
|              | ControlLogix® 1756 - DNB                                                        | local chassis                                                                   | Local:slot_number_of_scanner                                                                                             |
|              |                                                                                 | remote chassis                                                                  | adapter:slot_number_of_scanner where: adapter is the name of the EtherNet/IP or ControlNet module in the remote chassis. |
| type         | type of data:                                                                   | type of data:                                                                   |                                                                                                                          |
|              | Where                                                                           | Is                                                                              |                                                                                                                          |
|              | input from a device                                                             | I                                                                               |                                                                                                                          |
|              | output to a device                                                              | O                                                                               |                                                                                                                          |
| dnet_address | address of the device on the DeviceNet network (based on only 4 bytes per node) | address of the device on the DeviceNet network (based on only 4 bytes per node) | address of the device on the DeviceNet network (based on only 4 bytes per node)                                          |
| bit          | specific bit within the data of the device                                      | specific bit within the data of the device                                      |                                                                                                                          |

While you can use the input and output tags of the scanner directly in your logic, it is a lot easier to use alias tags. Alias tags can be used whether you use AutoScan or not to configure the scanner.

To run the DeviceNet network, use these steps.

## To put the scanner in Run mode

1. Place the controller in Run or Remote Run mode.

<!-- image -->

Tip: To put the scanner in Run mode, set the …O.CommandRegister.Run bit to 1

- .
2. Set these bits of the output structure for the scanner.
3. Check the scanner for Run mode.

| If you want to                          | Then set this bit                 |   To |
|-----------------------------------------|-----------------------------------|------|
| Run the network                         | …O.CommandRegister.Run            |    1 |
| Not run the network (Idle mode)         | …O.CommandRegister.Run            |    0 |
| Fault the network                       | …O.CommandRegister.Fault          |    1 |
| Not fault the network                   | …O.CommandRegister.Fault          |    0 |
| Disable the network                     | …O.CommandRegister.DisableNetwork |    1 |
| Enable the network                      | …O.CommandRegister.DisableNetwork |    0 |
| Halt the scanner (ceases all operation) | …O.CommandRegister.HaltScanner    |    1 |
| Unhalt the scanner                      | …O.CommandRegister.HaltScanner    |    0 |
| Reset the scanner                       | …O.CommandRegister.Reset          |    1 |
| Resume operation after a reset          | …O.CommandRegister.Reset          |    0 |

| If you have this scanner   | Then this indicator   | Displays                         |
|----------------------------|-----------------------|----------------------------------|
| ControlLogix® 1756 - DNB   | 4 - character display | RUN                              |
| CompactLogix™ 1769 - SDN   | 2 - character display | its node number when in Run mode |

## Put the Scanner in Run Mode

## Additional Information About AutoScan

## Type of Connection that the Scanner Sets Up

## Allocating More Memory for Each Device

The type of update (connection) that the scanner sets up with each device depends on the device. The scanner chooses the first connection type that the device supports in this order:

1. Change-of-state (COS)
2. Polled
3. Strobed
4. Cyclic at 1000 ms

The scanner tries to set up a change-of-state connection. If the device does not support change-of-state, then the scanner tries to set up a polled connection and so on. The type of connection that the scanner sets up may not be the default for the device.

The AutoScan feature is easiest to use if you leave it set to 1 DINT (4 bytes) of input memory and output memory for each address.

<!-- image -->

As an option, you can allocate more memory for each device.

| Consideration                                                                                   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|-------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| The bytes/node value defines the amount of memory for each address.                             | AutoScan lets you specify how much input and output memory to give to each address on the network.                                                                                                                                                                                                                                                                                                                                                               |
| The scanner sets - up communication with any device that fits within the allocated memory size. | The scanner automatically sets up communication with those devices that fit within the memory allocated for each address. •  For example, if you allocate 2 DINTs (8 bytes) per address, the scanner sets up communication with any device that sends or receives 1…8 bytes of data. •  The scanner adds as many device as it can until it runs out of memory. If you give too much memory to each address, you may not have enough memory for all your devices. |

| Consideration                                      | Description                                                                                                                                                                                                                                                                                                                                                                                                                           |
|----------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| The scanner skips devices that are too large.      | If a device needs more memory than is allocated, the scanner skips it and does not set up communication with it. For example, if you specify 2 DINTs (8 bytes) per address but a device sends 9 bytes, the scanner does not add the device to the scan list.                                                                                                                                                                          |
| Manually editing the scan list turns off AutoScan. | If you use RSNetWorx™ for DeviceNet software to edit the configuration of the scanner, the scanner turns off AutoScan. Do not turn it back on or you will clear the configuration that you just entered. For example, if you use RSNetWorx™ for DeviceNet software to manually add a device to the scan list, the scanner turns off AutoScan. If turn on AutoScan again, the scanner clears it current configuration and starts over. |

## Before You Begin

## Control a Device

Use this chapter to develop the logic that examines and controls your devices.

| Topic                                        | Page    |
|----------------------------------------------|---------|
| Before You Begin                             | page 27 |
| Determine the Address of DeviceNet Data      | page 90 |
| Determine If a Device Has Failed             | page 92 |
| Place the Scanner in Run Mode                | page 93 |
| When to Use a MSG Instruction                | page 94 |
| Determine the Parameter Number to Access     | page 95 |
| Determine the Configuration of the Parameter | page 95 |
| Test the Parameter                           | page 96 |
| Enter Message Logic                          | page 97 |

Before you use this chapter, make sure that you can see all your devices on the DeviceNet network. Complete the steps to see your DeviceNet network.

## Before you begin

1. Start RSLinx® communication software.
2. Browse the network.
3. Expand a driver that lets you access the DeviceNet network.
4. Select the DeviceNet network.

5. Verify that you see all the devices that are connected to the DeviceNet network.

<!-- image -->

## RSNetWorx Report for the Network

## Data Map for Each of Your Devices

## Add the Scanner to the Controller's I/O Configuration

## Conserve EtherNet/IP or ControlNet Network Bandwidth

<!-- image -->

<!-- image -->

To access the data of the network, add the scanner to the controller's I/O configuration in the Logix Designer application. However, you may need to conserve bandwidth on the EtherNet/IP or ControlNet network.

The default configuration of the scanner gives you the maximum amount of input, output, and status data, as shown in the graphic.

<!-- image -->

If the scanner communicates with the controller via an EtherNet/IP or ControlNet network and you need to conserve bandwidth over that network, consider reducing the input, output, or status sizes.

- Set the input and output sizes = the number of input and output DINTs in the scanner that actually store device data.
- If you are not going to use all the status information, set the status size to the minimum required.

EXAMPLE If you want to use only the ASCII representation of scanner status/display, set the status size to 10.

If you also want to read the status code of the scanner, set the status size to 11.

See Table 1 -Set the Status Size for a Scanner on page 106 for more information on how to change the status size of a scanner from the default values.

## Set the Status Size for a Scanner

| If you want this information                                                                                                                                                                                                                 | Set the status size (DINTs) to the value   | This setting gives you the parameter values.   | This setting gives you the parameter values.   |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------|------------------------------------------------|------------------------------------------------|
|                                                                                                                                                                                                                                              | Set the status size (DINTs) to the value   | Member                                         | Data Type                                      |
| Count of I/O scans                                                                                                                                                                                                                           | 10                                         | ScanCounter                                    | DINT                                           |
| Indication that a device has failed: •  There is 1 bit for each address on the DeviceNet network (0 - 63). •  The position of a bit = address of a device. •  If a bit = 1, then the device at that address has failed.                      |                                            | DeviceFailureRegister                          | SINT[8]                                        |
| Indication that the data size of a device does not match the amount of memory allocated for the device in the scanner: •  There is 1 bit for each address on the DeviceNet network (0 - 63). •  The position of a bit = address of a device. |                                            | AutoverifyFailureRegister                      | SINT[8]                                        |
| Indication that a device is idle: •  There is 1 bit for each address on the DeviceNet network (0 - 63). •  The position of a bit = address of a device. •  If a bit = 1, then the device at that address is idle.                            |                                            | DeviceIdleRegister                             | SINT[8]                                        |
| Indication that a device is online: •  There is 1 bit for each address on the DeviceNet network (0 - 63). •  The position of a bit = address of a device. •  If a bit = 1, then the device at that address is online.                        |                                            | ActiveNodeRegister                             | SINT[8]                                        |
| ASCII representation of scanner status/display                                                                                                                                                                                               |                                            | StatusDisplay                                  | SINT[4]                                        |
| Address of the scanner                                                                                                                                                                                                                       | 11                                         | ScannerAddress                                 | SINT                                           |
| Status code of scanner                                                                                                                                                                                                                       |                                            | ScannerStatus                                  | SINT                                           |
| Address with an error: •  Scrolls through the addresses with errors •  ScrollingDeviceStatus member shows the status code                                                                                                                    |                                            | ScrollingDeviceAddress                         | SINT                                           |
| Status code of an address with an error: •  Scrolls through addresses with errors •  ScrollingDeviceAddress member shows the address                                                                                                         |                                            | ScrollingDeviceStatus                          | SINT                                           |
| Possible future expansion of the structure — 5 DINTs                                                                                                                                                                                         | 16                                         |                                                |                                                |
| Status code of lower 32 devices — 1 byte per device                                                                                                                                                                                          | 24                                         | DeviceStatus                                   | SINT[32]                                       |
| Status code of all devices — 1 byte per device                                                                                                                                                                                               | 32                                         | DeviceStatus                                   | SINT[64]                                       |

## Add the Scanner to the I/O Configuration Folder

## Configure the Scanner

Complete these steps to add the scanner to the I/O configuration file.

## To add the scanner to the I/O Configuration Folder

1. Right-click and choose New Module .
2. Select the type of scanner.
3. Select OK .
4. From the Major Revision pull-down menu, choose a major revision number for the scanner.
5. Select OK .

<!-- image -->

<!-- image -->

<!-- image -->

Complete these steps to configure the scanner.

## Determine the Address of DeviceNet Data

## To configure the scanner

1. Type a name for the scanner.
2. Enter a node number.
3. Enter the slot number.
4. Enter the minor revision.
5. Enter the size of the input and output memory maps that the scanner will allocate for each device it detects on the network.

Valid values range from 0…32 bytes per node.

6. If you need to make additional configuration changes, such as setting the requested packet interval (RPI), check Open Module Properties.
7. Select OK .
8. If the Module Properties dialog box appears, make additional configuration changes.

<!-- image -->

You can change scanner configuration on these tabs:

- General
- Connection
- RSNetWorx™

When you add the scanner to the I/O configuration of the controller, the Logix Designer application programming software automatically creates a set of tags for the input, output, and status data of the network.

<!-- image -->

Chapter 7

Control a Device

## The tags for your DeviceNet data follow this format.

The scanner memory uses this format...

which is this tag in the controller.

slot

type

.Data

[element]

.bit

location

:type

.Data

[element]

.bit

- [ ] = Optional

Where

Is

Slot

The slot number of the scanner

Location

If you have this scanner

Then location is

Local ControlLogix® 1756 - DNB

Local:slot\_number\_of\_scanner

Remote ControlLogix® 1756 - DNB

name\_of\_remote\_bridge:slot\_number\_of\_scanner

CompactLogix™ 1769 - SDN

Local:slot\_number\_of\_scanner

SoftLogix™ 5800 1784 - PCIDS

Local:slot\_number\_of\_scanner

Linking Device 1788 - EN2DN or 1788 - CN2DN

The name of the linking device in the I/O configuration of the controller

Type

If the data is

Then type is

Input from a device

I

Output to a device

O

The status of the network

S

Element

A specific DINT (DWord, 32 - bit integer) within the array

Bit

A specific bit within an integer

Complete these steps to determine the tag name, or address, for DeviceNet data.

1. On the RSNetWorx™ report for the network, find the memory address for the input or output data of the device.
2. Find the corresponding tag in the controller-scoped tags of the controller.
3. Find the required data within the controller tag.

Use the data map for the device as a reference.

<!-- image -->

<!-- image -->

## SoftLogix 5800 Controller

## Determine If a Device Has Failed

The SoftLogix™ 5800 scanner 1784-PCIDS organizes input and output memory in 16-bit words. It uses address format word.bit.

| Where   | Is                                                  |
|---------|-----------------------------------------------------|
| Word    | INT (16-bit integer) with the memory of the scanner |
| Bit     | A specific bit within an integer                    |

While you can use the input and output tags of the scanner directly in your logic, it is easier to use alias tags.

If a DeviceNet communication device stops communicating, such as because of a device failure, the tag for the device stays at its last value. To make sure that your input data is valid, we recommend that you buffer the input data and examine the device failure register.

- 1 Indication that a device has failed.

There is 1 bit for each address on the DeviceNet network.

- If a bit = 1, then the device at that address has failed.
- 2 Addresses 0 to 7
- 3 Address 0
- 4 Address 1

<!-- image -->

## Place the Scanner in Run Mode

## When to Use an MSG Instruction

## Complete these steps to run the DeviceNet network.

<!-- image -->

Tip: To put the scanner in Run mode, set the …O.CommandRegister.Run bit to 1 .

1. Set the bit of the output structure for the scanner.
2. Place the controller in Run or Remote Run mode.

| If you want to                          | Set this bit                      |   To |
|-----------------------------------------|-----------------------------------|------|
| Run the network                         | …O.CommandRegister.Run            |    1 |
| Not run the network (idle mode)         | …O.CommandRegister.Run            |    0 |
| Fault the network                       | …O.CommandRegister.Fault          |    1 |
| Not fault the network                   | …O.CommandRegister.Fault          |    0 |
| Disable the network                     | …O.CommandRegister.DisableNetwork |    1 |
| Enable the network                      | …O.CommandRegister.DisableNetwork |    0 |
| Halt the scanner (ceases all operation) | …O.CommandRegister.HaltScanner    |    1 |
| Unhalt the scanner                      | …O.CommandRegister.HaltScanner    |    0 |
| Reset the scanner                       | …O.CommandRegister.Reset          |    1 |
| Resume operation after a reset          | …O.CommandRegister.Reset          |    0 |

If you want to set or get a parameter based on conditions in your logic, use a Message (MSG) instruction in ladder logic to access the parameter.

<!-- image -->

Some parameters do not require ongoing updates. For example, initializing configuration parameters may occur only when the controller goes to Run mode. By using a MSG instruction for those parameters, you save bandwidth on the DeviceNet network for more critical or ongoing data.

## Determine the Parameter Number to Access

## Determine the Configuration of the Parameter

Use RSNetWorx™ for DeviceNet software to determine the parameter number that you want to access. Some parameters are read-only and are shown with a lock symbol.

<!-- image -->

Find the information about the parameters listed in the table to get or set a parameter.

| Item                                                                               | Value   |
|------------------------------------------------------------------------------------|---------|
| Class # (hex)                                                                      |         |
| Instance # (hex)                                                                   |         |
| Attribute # (hex)                                                                  |         |
| Number of bytes (size)                                                             |         |
| Minimum value                                                                      |         |
| Maximum value                                                                      |         |
| Decimal places Some devices assume a specific number of decimal places in a value. |         |

## Test the Parameter

In addition to the documentation for the device, the EDS file may also give you the required information.

<!-- image -->

A simple way to make sure that you have the correct configuration for a parameter, such as data size or values, is to use the Class Instance editor in RSNetWorx™ for DeviceNet software.

Complete these steps to test the parameter.

1. In RSNetWorx™ for DeviceNet software, go online to the DeviceNet network.
2. Right-click the device and choose Class Instance Editor .
3. Type the class, instance, and attribute for the parameter.
4. Change the parameter.
- a. Choose Set Single Attribute .
- b. Choose the number of bytes.
- c. Type the new value in hexadecimal format.

V

<!-- image -->

5. From the Description pull-down menu, choose Get Single Attribute to read the parameter.
6. Select Execute .
7. To change how output data is displayed, choose the size and format.

<!-- image -->

## Enter Message Logic

Change the current limit of the drive.

<!-- image -->

You must complete these tasks to configure the MSG instruction:

- Define the Source or Destination Data a on page 98
- Enter and Configure the MSG Instruction on page 99
- Set the Communication Path on page 100

Tag that controls the instruction.

- Scope — Controller.
- Data type — MESSAGE.

The tag cannot be part of an array or a user -defined data type.

Source or destination for the data that the instruction sets or gets.

- Scope — Controller.
- Data type — In general, use the DINT data type, even when you set or get less than 4 bytes.
- Value — Make sure the source value stays within the minimum and maximum values for the parameter that you are setting.

Number of bytes (only if setting a value).

## Define the Source or Destination Data

<!-- image -->

To access the parameter of a device (get or set the parameter), configure the MSG instruction as CIP Generic.

## Enter and Configure the MSG Instruction

## In general, use these guidelines:

- Use the DINT data type for the source or destination tag, even when you set or get less than 4 bytes.
- Make sure the source value stays within the minimum and maximum values for the parameter that you are setting.

When setting a value, the CIP Generic MSG instruction takes only the specified number of bits from the source tag.

<!-- image -->

To increase the efficiency of your logic, minimize the use of SINT or INT data types. Whenever possible, use the DINT data type for integers.

- A Logix 5000™ controller typically compares or manipulates values as 32 -bit values (DINTs or REALs).
- The controller typically converts a SINT or INT value to a DINT or REAL value before it uses the value.
- If the destination is a SINT or INT tag, the controller typically converts the value back to a SINT or INT value.
- The conversion to or from SINTs or INTs occurs automatically with no extra programming. However, it takes extra execution time and memory.

Complete these steps to enter and configure the MSG instruction.

## To enter and configure the MSG instruction

1. Enter a condition for the data transfer, such as the DN bit of a timer.
2. Enter an MSG instruction.
3. Select CIP Generic .
4. Complete the configuration to send output data.
- d. From the Service Type pull-down menu, choose Set Attribute Single .
- e. From the Source Element pull-down menu, choose the array that has the data.
- f. In the Source Length field, enter the number of bytes that you have addressed in the PanelView™ instance (words x 2).
- g. In the Class field, type 4.

<!-- image -->

## Set the Communication Path

- h. In the Instance field, type the assembly instance of the data in the PanelView™ terminal. Convert it to hexadecimal format.
- i. In the Attribute field, type 3.
5. Complete the configuration to get input data.
- j. From the Service Type pull-down menu, choose Get Attribute Single .
- k. From the Destination pull-down menu, choose the array to store the data.
- l. In the Class field, type 4.
- m. I In the Instance field, type the assembly instance of the data in the PanelView™ terminal. Convert it to hexadecimal format.
- n. In the Attribute field, type 3.

<!-- image -->

<!-- image -->

The communication path specifies the route to the PanelView™ terminal. A communication path uses this format:

scanner\_name,2,device\_address

| Where          | Is                                                                         |
|----------------|----------------------------------------------------------------------------|
| scanner_name   | The name of the scanner in the I/O Configuration folder of the controller. |
| device_address | The address of the device on the DeviceNet network.                        |

Complete these steps to set the communication path.

1. Select the Communication tab.
2. Select the Browse button and select the scanner.
3. Type the rest of the path.
4. Select OK .

<!-- image -->

For more information on programming MSG instructions, see the Logix 5000 Controller General Instructions Reference Manual, publication 1756-RM003 .

## Interlock

## Choose a Master Controller

## Interlock and Share Inputs

The chapter describes how to interlock and share inputs over a DeviceNet network.

| Topic        | Page     |
|--------------|----------|
| Interlock    | page 103 |
| Share Inputs | page 108 |

<!-- image -->

To set up an interlock between two controllers over a DeviceNet network, complete these tasks:

- Choose a Master Controller on page 103
- Determine How Much Data to Exchange on page 104
- Enable Slave Mode for the Slave Scanner on page 104
- Map the Slave Mode Data a on page 105
- Add the Slave to the Master Scanner's Scan List on page 106
- Map the Data of the Slave on page 107
- Place Both Scanners In Run Mode on page 108

## Determine How Much Data to Exchange

## Enable Slave Mode for the Slave Scanner

To interlock, choose a controller to serve as the master. The other controller becomes a slave to the master. This defines the relationship between the controllers. The scanners of each controller still scan and control their own devices, if desired.

<!-- image -->

Before you configure the scanners for the interlock, determine how much data you want to exchange between the controllers.

<!-- image -->

Complete these steps to enable Slave mode.

## To enable Slave Mode for the slave scanner

1. In RSNetWorx™ for DeviceNet software, double-click the slave scanner to open its properties.
2. Select the Module tab.
3. Select Slave Mode .
4. Select the Enable Slave Mode check box.

## Map the Slave Mode Data

## 5. Define the I/O parameters.

Complete these steps to map Slave mode data.

<!-- image -->

## To map the Slave Mode data

1. Map the Slave mode data to the input memory of the slave scanner. This is the data that the scanner (controller) gets from the master.

## Add the Slave to the Master Scanner's Scan List

2. Repeat for the data that the slave scanner (controller) sends to the master.

<!-- image -->

Complete these steps to add the slave to the master's scan list.

## To add the slave to the master scanner's scan list

1. In RSNetWorx™ for DeviceNet software, double-click the master scanner to open its properties.

## Map the Data of the Slave

2. Add the slave to the scan list.

<!-- image -->

Complete these steps to map the data.

## To map the data of the slave

1. Map the slave scanner to the input memory of the master scanner. This is the data that the scanner (controller) gets from the slave.

Place Both Scanners In Run Mode

Share Inputs

Add the Input to the First Scanner

Add the Input to the Second Scanner

2. Repeat for the data that the master scanner (controller) sends to the slave.

<!-- image -->

To exchange data, place both scanners in Run mode. Refer to Place the Scanner in Run Mode on page 113 for more information on placing both scanners in Run mode.

To let multiple scanners (controllers) consume input data from the same input device, complete the tasks in this section.

Establish communication between the input and one of the scanners. Use one of these sections to establish communication:

- Configure the Network Offline on page 33
- Configure the Network Online on page 33

Complete these steps to add the input to the second scanner.

## To add the input to the second scanner

1. In RSNetWorx™ for DeviceNet software, display the scan list for the second scanner.
2. In the Available Devices list, right-click and choose Shared Inputs .

## 3. Add the input to the scan list.

<!-- image -->

## Choose Data Types

## Communicate with a PanelView Standard Terminal

This chapter describes how to configure and program communication with a PanelView™ Standard terminal on a DeviceNet network.

| Topic                                                                                 | Page     |
|---------------------------------------------------------------------------------------|----------|
| Choose Data Types                                                                     | page 111 |
| Choose a Communication Method                                                         | page 111 |
| Plan and Configure I/O Slave Tags                                                     | page 113 |
| Set Up the Terminal on Your Network                                                   | page 115 |
| Configure the Scanner to Update I/O Slave Tags                                        | page 117 |
| Address I/O Slave Tags in the Logix Designer application Programming Software Project | page 119 |
| Plan and Configure Explicit Server Tags                                               | page 121 |
| Program the Controller to Get/Set Explicit Server Tags                                | page 124 |
| Configure Explicit Client Tags                                                        | page 126 |

For the tags in the PanelView™ terminal, use the data types described in the table as a starting point.

| If the object on the PanelView™ screen reads or writes   | Then use this data type   |   Which uses this many bits in the PanelView™ Terminal |
|----------------------------------------------------------|---------------------------|--------------------------------------------------------|
| Single bit                                               | Bit                       |                                                      1 |
| Integer                                                  | Unsigned integer          |                                                     16 |

Data types, such as signed integer and float, also work with Logix 5000™ controllers. However, they require additional configuration and programming.

You have three options to send data to and from a PanelView™ terminal .

## Choose a Communication Method

| If you want to                                                                                        | Use this method   | Considerations                                                                                                                                                               |
|-------------------------------------------------------------------------------------------------------|-------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Communicate with the PanelView™ terminal using the regular I/O communication of the DeviceNet network | I/O slave         | • Easiest to use — requires no additional programming. •  Use this as your first choice. •  Higher priority on the network than explicit server and explicit client updates. |
| Communicate with the PanelView™ terminal based on conditions in your logic                            | Explicit server   | • Provides additional data when you use up the I/O slave assemblies. •  Lower priority on the network than I/O slave updates.                                                |

| If you want to                                                                                                 | Use this method   | Considerations                                                                                     |
|----------------------------------------------------------------------------------------------------------------|-------------------|----------------------------------------------------------------------------------------------------|
| Use the PanelView™ terminal to get or set a parameter of a device on your DeviceNet network (not a controller) | Explicit client   | • Does not use the controller or scanner. •  Lower priority on the network than I/O slave updates. |

## I/O Slave Communication

## I/O Slave

Scanner polls PanelView™ terminal for I/O data.

- You define the input and output sizes up to 64 words.
- Assembly instance 1 gives input data to the controller.
- Assembly instance 2 gets output data from the controller.

## Explicit Server Communication

## Explicit Server

Controller executes a MSG instruction that gets or sets data in the PanelView™ terminal .

- 14 assembly instances are available for explicit -server transfers.
- Instance #s are 3…16.
- You define an instance as either input data (I) or output data (O), but not both.
- Each instance provides 64 words of either input or output data for the terminal.

Refer to the I/O slave communication requirements.

<!-- image -->

Refer to the explicit server communication requirements.

<!-- image -->

## Explicit Client Communication

## Explicit Client

PanelView™ terminal sets or gets data in another device on a tag-by-tag basis.

## Plan and Configure I/O Slave Tags

Refer to the explicit client communication requirements.

<!-- image -->

Like the other DeviceNet communication modules, I/O slave tags use space in the input and output maps of the scanner. The scanner gets or sets the data on each scan of the DeviceNet network.

A PanelView™ terminal gives you two blocks of 16-bit words (assembly instances) for I/O slave tags.

<!-- image -->

## Use a Word/Bit Format for Each Tag

Each I/O slave tag requires a specific address in the corresponding assembly instance. A tag address uses the following format:

<!-- image -->

## For Integers, Skip Every Other Word

= Optional

| Where   | Is                                              | Is                                         |
|---------|-------------------------------------------------|--------------------------------------------|
| Type    | Type of tag                                     | Type of tag                                |
|         | If the tag is a                                 | Then use                                   |
|         | Write tag (sends input data to the controller)  | I                                          |
|         | Read tag (gets output data from the controller) | O                                          |
| Word    | Specific 16 - bit word within the assembly      | Specific 16 - bit word within the assembly |
| Bit     | Specific bit within Word (0…15)                 | Specific bit within Word (0…15)            |

Logix 5000™ controllers use 32 -bit integers (DINTs). Complete the steps to lay out your PanelView™ tags in a method that makes programming easier.

1. For bit -level tags, set aside an even number of words.
2. For each integer, set aside 2 words.

Start each integer on an even word. This method lets each integer map to its own element in the scanner/controller.

Word

<!-- image -->

## Configure an I/O Slave Tag

Complete these steps to configure an I/O slave tag.

## To configure an I/O slave tag

1. Type a descriptive name for the tag.
2. Choose the data type for the tag.

## Set Up the Terminal on Your Network

## Set the Protocol

3. Let the scanner update the data.
4. Assign an address for the tag within the input or output assembly.

<!-- image -->

Complete these tasks in PanelBuilder32 software to configure a PanelView™ terminal for communication on a DeviceNet network:

- Set the Protocol on page 115
- Set the Node Address and I/O Sizes on page 116

Complete these steps to set the protocol.

## To set the protocol

1. Double -click Terminal Setup.
2. Choose the auxiliary port usage.

## Set the Node Address and I/O Sizes

## 3. Select OK .

<!-- image -->

Complete these steps to set the node address and I/O sizes.

## To set the node address and I/O sizes

1. Double -click Communication Setup.
2. Type the address of the PanelView™ terminal .
3. Type the number of input words and output words that you will use (64 maximum each).

## Configure the Scanner to Update I/O Slave Tags

## Add the Terminal to the Scan List

## 4. Select OK to close the dialog boxes.

<!-- image -->

Complete these tasks to access I/O slave tags and map the data to the input and output maps of the scanner:

- Add the Terminal to the Scan List on page 117
- Edit I/O Parameters on page 118
- Map Input and Output Data on page 119

Complete these steps to add the terminal to the scanlist.

## To add the terminal to the scan list

1. Select the Scanlist tab.
2. Clear Automap on Add .
3. Add the terminal to the scanlist.

## Edit I/O Parameters

4. Select OK .

<!-- image -->

Complete these steps to edit I/O parameters.

## To edit I/O parameters

1. Select the terminals.
2. Select Edit I/O Parameters .
3. Enter the input and output sizes in bytes. Make sure each number is two times the number you entered in the communication set-up of the terminal (1 word = 2 bytes).
4. Select OK .

<!-- image -->

## Map Input and Output Data

Address I/O Slave Tags in the Logix Designer application Project

<!-- image -->

Complete these steps to map input and output data.

1. Select the Input tab.
2. Select the terminal.
3. Enter the starting element for the data in the input array.
4. Set the alignment option (typically DWord align).
5. Select AutoMap. An entry for the device shows up in the input array.
6. Select the Output tab and repeat steps 2 through 5.

<!-- image -->

You must get this information to find the data for an I/O slave tag in your Logix Designer programming software project:

- RSNetWorx™ for DeviceNet report for the network
- Address for the tag in the PanelView™ terminal

Complete these steps to get the information described previously.

1. On the report for the network, find the memory address for the PanelView™ terminal .

2. Find the corresponding tag in the controller-scoped tags of the controller.
3. Find the data within the controller tag.

Use the tag address as a reference.

<!-- image -->

DeviceNet tags use the format described below.

| Scanner Memory Format         | Tag in Controller                 |
|-------------------------------|-----------------------------------|
| slot:type.Data[ element ].bit | location:type.Data[ element ].bit |

<!-- image -->

| Where    | Is                                    | Is                                    | Is                                                                                                                       |
|----------|---------------------------------------|---------------------------------------|--------------------------------------------------------------------------------------------------------------------------|
| Location | Location of the scanner in the system | Location of the scanner in the system |                                                                                                                          |
|          | If you have this scanner              | Then location is                      | Then location is                                                                                                         |
|          | ControlLogix® 1756 - DNB              | In a                                  | Location is                                                                                                              |
|          |                                       | local chassis                         | Local:slot_number_of_scanner                                                                                             |
|          |                                       | remote chassis                        | adapter:slot_number_of_scanner where: adapter is the name of the EtherNet/IP or ControlNet module in the remote chassis. |
|          | CompactLogix™ 1769 - SDN              | Local:slot_number_of_scanner          | Local:slot_number_of_scanner                                                                                             |
|          | SoftLogix™ 5800 1784 - PCIDS          |                                       |                                                                                                                          |

| Where   | Is                                                         | Is                                                                 | Is                                                                 |
|---------|------------------------------------------------------------|--------------------------------------------------------------------|--------------------------------------------------------------------|
|         | EtherNet/IP to DeviceNet Linking Device (1788-EN2DN)       | The name of the scanner in the I/O configuration of the controller | The name of the scanner in the I/O configuration of the controller |
|         | ControlNet to DeviceNet Linking Device (1788-CN2DN)        |                                                                    |                                                                    |
| Type    |                                                            |                                                                    | Type of data:                                                      |
| Type    |                                                            | Is                                                                 | Where                                                              |
| Type    | Input from a device                                        | I                                                                  |                                                                    |
| Type    | Output to a device                                         | O                                                                  |                                                                    |
| Type    | Status of the network                                      | S                                                                  |                                                                    |
|         | A specific DINT (DWord, 32 - bit integer) within the array | A specific DINT (DWord, 32 - bit integer) within the array         | Element                                                            |
| Bit     | A specific bit within an integer                           | A specific bit within an integer                                   |                                                                    |

## SoftLogix 5800 Controller

## Plan and Configure Explicit Server Tags

The SoftLogix™ 5800 scanner 1784-PCIDS organizes input and output memory in 16-bit words. It uses these address formats.

word.bit

| Where   | Is                                                  |
|---------|-----------------------------------------------------|
| Word    | INT (16-bit integer) with the memory of the scanner |
| Bit     | A specific bit within an integer                    |

Explicit server tags are similar to I/O tags except that the controller initiates the communication with the terminal. Explicit server tags do not show up on the input and output maps of the scanner.

## Assign Assembly Instances

## Refer to the assign assembly instances.

<!-- image -->

Determine how you will use each assembly instance.

|   Instance Number | Input (Write) or Output (Read)   |   Instance Number | Input (Write) or Output (Read)   |
|-------------------|----------------------------------|-------------------|----------------------------------|
|                 1 | input                            |                 9 |                                  |
|                 2 | output                           |                10 |                                  |
|                 3 |                                  |                11 |                                  |
|                 4 |                                  |                12 |                                  |
|                 5 |                                  |                13 |                                  |
|                 6 |                                  |                14 |                                  |
|                 7 |                                  |                15 |                                  |
|                 8 |                                  |                16 |                                  |

## For Integers, Skip Every Other Word

Logix 5000™ controllers use 32 -bit integers (DINTs). Complete the steps to lay out your PanelView™ tags in a method that makes programming easier.

1. For bit -level tags, set aside an even number of words.
2. For each integer, set aside 2 words.

Start each integer on an even word. This method lets each integer map to its own element in the scanner/controller.

<!-- image -->

## Configure an Explicit Server Tag

Complete these steps to configure an Explicit-Server tag.

## To configure an explicit server tag

1. Type a descriptive name for the tag.
2. Choose the data type for the tag.
3. Let the controller initiate the update.
4. Choose the assembly instance for the tag.
5. Assign an address for the tag within the assembly instance.
- Write tag = I:word/bit
- Read tag = O:word/bit

<!-- image -->

## Program the Controller to Get/Set Explicit Server Tags

## Create an Array for the Assembly Instance

## Enter and Configure the MSG Instruction

Complete these tasks to let the controller read or write data from or to an Explicit-Server tag:

- Create an Array for the Assembly Instance on page 124
- Enter and Configure the MSG Instruction on page 99
- Set the Communication Path on page 100

For each assembly instance that you use for explicit server tags, create an array in the Logix Designer project for the data.

<!-- image -->

Complete these steps to enter and configure the MSG instruction.

## To enter and configure the MSG instruction

1. Enter a condition for the data transfer, such as the DN bit of a timer.
2. Enter an MSG instruction.
3. Select CIP Generic .
4. Complete the configuration to send output data.
- o. From the Service Type pull-down menu, choose Set Attribute Single .
- p. From the Source Element pull-down menu, choose the array that has the data.
- q. In the Source Length field, enter the number of bytes that you have addressed in the PanelView™ instance (words x 2).
- r. In the Class field, type 4.
- s. In the Instance field, type the assembly instance of the data in the PanelView™ terminal. Convert it to hexadecimal format.

<!-- image -->

## Set the Communication Path

## t. In the Attribute field, type 3.

<!-- image -->

5. Complete the configuration to get input data.
- u. From the Service Type pull-down menu, choose Get Attribute Single .
- v. From the Destination pull-down menu, choose the array to store the data.
- w. I In the Class field, type 4.
- x. In the Instance field, type the assembly instance of the data in the PanelView™ terminal. Convert it to hexadecimal format.
- y. In the Attribute field, type 3.

<!-- image -->

The communication path specifies the route to the PanelView™ terminal. A communication path uses this format:

scanner\_name,2,device\_address

## Configure Explicit Client Tags

| Where          | Is                                                                         |
|----------------|----------------------------------------------------------------------------|
| scanner_name   | The name of the scanner in the I/O Configuration folder of the controller. |
| device_address | The address of the device on the DeviceNet network.                        |

Complete these steps to set the communication path.

1. Select the Communication tab.
2. Select the Browse button and select the scanner.
3. Type the rest of the path.
4. Select OK .

<!-- image -->

For more information on programming MSG instructions, see the Logix 5000 Controller General Instructions Reference Manual, publication 1756-RM003 .

Use an Explicit Client tag to let the PanelView™ terminal get or set a parameter of another device on the DeviceNet network.

<!-- image -->

An Explicit Client tag does not:

- Show up on the input or output map of the scanner
- Involve the controller
- Use an address in an assembly instance of the PanelView™ terminal

Complete these tasks to configure Explicit Client tags:

- Determine the Parameter Number to Access on page 95
- Determine the Configuration of the Parameter on page 95

## Determine the Parameter Number to Access

## Determine the Configuration of the Parameter

- Configure an Explicit Client Tag on page 128

Use RSNetWorx™ for DeviceNet software to determine the parameter number that you want to access. Some parameters are read-only and are shown with a lock symbol.

<!-- image -->

Find the information about the parameters listed in the table to get or set a parameter.

| Item                                                                               | Value   |
|------------------------------------------------------------------------------------|---------|
| Class # (hex)                                                                      |         |
| Instance # (hex)                                                                   |         |
| Attribute # (hex)                                                                  |         |
| Number of bytes (size)                                                             |         |
| Minimum value                                                                      |         |
| Maximum value                                                                      |         |
| Decimal places Some devices assume a specific number of decimal places in a value. |         |

## Configure an Explicit Client Tag

In addition to the documentation for the device, the EDS file may also give you the required information.

<!-- image -->

Complete these steps to configure an Explicit Client tag.

## To configure an Explicit Client Tag

1. Type a descriptive name for the tag.
2. Choose the data type for the tag. Let the PanelView™ terminal initiate the update.
3. Type the address of the device.
4. If the PanelView™ terminal sets the parameter, select the Write Tag box.
5. Type the number of bytes in the parameter.
6. Type the class, instance, and attribute numbers for the parameter.

<!-- image -->

## Communicate with a FactoryTalk View Project

This chapter describes how use a FactoryTalk® View w project to get or set a parameter of a DeviceNet communication module.

| Topic                          | Page     |
|--------------------------------|----------|
| Before You Begin               | page 27  |
| Create a Topic for the Device  | page 130 |
| Create a Node                  | page 131 |
| Create a Tag for the Parameter | page 132 |

<!-- image -->

Once you add a device to the scan list of a scanner, HMI software such as FactoryTalk® View cannot write to (set) some parameters.

<!-- image -->

Once this device is in the scan list of the scanner, a FactoryTalk® View project cannot set this parameter.

To access the DeviceNet network, either connect the computer with the FactoryTalk® View w application to any of the following networks:

- Same DeviceNet network as the desired device

## Before You Begin

## Create a Topic for the Device

- EtherNet/IP or ControlNet network and bridge communication to the DeviceNet network
- Avoid bridging through a 1768 or 1769 CompactLogix™ controller, or DriveLogix™ controller. They have limited resources for bridging.
- For the controllers mentioned in the previous bullet, use the I/O tags in the controller, if possible.

Before you use this chapter, make sure that you can see all your devices on the DeviceNet network. Complete the steps to see your DeviceNet network.

## Before you begin

1. Start RSLinx® communication software.
2. Browse the network.
3. Expand a driver that lets you access the DeviceNet network.
4. Select the DeviceNet network.
5. Verify that you see all the devices that are connected to the DeviceNet network.

<!-- image -->

Use RSLinx® communication software to create a topic for the DeviceNet communication module that you want to access. Complete these steps to create a topic for the device.

## To create a topic for the device

1. In RSLinx® communication software, browse to the device that you want to access.

## Create a Node

2. Right-click the device and choose Configure New DDE/OPC Topic .
3. Type a name for the topic.
4. To change how often RSLinx® communication software updates the tag, select the Data Collection tab and type a new poll period.
5. Select Done .
6. When prompted, select Yes to update the topic.

<!-- image -->

<!-- image -->

In the FactoryTalk® View w project, create a node for your RSLinx® topics. Complete these steps to create a node.

## Create a Tag for the Parameter

## To create a node

1. Open the list of nodes for the project.
2. Choose OPC Server .
3. Type a name for the node.
4. Select RSLinx® .
5. Select Accept .

<!-- image -->

<!-- image -->

Complete these steps to create a tag for the parameter in FactoryTalk® View software.

## To create a tag for the parameter

1. Type the name of the tag.
2. Choose the type of tag.
3. Choose Device .
4. Select the node that contains the topic for the device.
5. Open the address browser.
6. Browse to the offline list of tags for the topic, that is, device.
7. Select the parameter and select OK .

<!-- image -->

<!-- image -->

## Tune the Performance of a DeviceNet Network

This chapter describes how to improve the performance of the network.

| Topic                                    | Page     |
|------------------------------------------|----------|
| Factors that Affect Performance          | page 135 |
| Change the Configuration of Your Network | page 139 |

As you configure and program the network, use the default settings whenever possible. Once the network is running, determine if you need to improve performance.

To improve the performance of the network, consider the information in the table.

| If                                                                                                                                                                                                           | Then                                                                                                                                                                            |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| A specific device requires a faster update                                                                                                                                                                   | Change the I/O parameters of the device to change of state (COS).                                                                                                               |
| An analog device does either of the following: •  Changes slower than the scan cycle •  Requires a repeatable update period, such as for PID calculations                                                    | Change the I/O parameters of the device to cyclic.                                                                                                                              |
| Multiple devices are input only and I/O parameters are currently set to polled with an input size less than or equal to 8 bytes                                                                              | For each of those devices, change their I/O parameters to strobed.                                                                                                              |
| Two or more devices send or receive large amounts of data, such as the PanelView™ operator terminal                                                                                                          | •  For each of those devices, set their I/O parameters to polled with a poll rate =  background. •  For the scanner, set the poll ratio = 2. Increase the poll ratio if needed. |
| Communication intermittently stops (status code 78) with a device that sends or receives large amounts of data, such as the PanelView™ operator terminal, and has the I/O parameters currently set to polled | Increase the interscan delay.                                                                                                                                                   |

## Factors that Affect Performance

The example shows how different I/O or network parameters affect the performance of the network.

<!-- image -->

<!-- image -->

## I/O Parameters of Each Device

The type of connection (message) that you configure for a device determines when data transfers between the device and the scanner. Consider these points when you configure the type of connection:

- Each device has a default connection type. This is a good starting point.
- Some devices may not offer all connection (message) types.

These table describes the different types of connections (messages) that you can configure for a device.

| Connection (Message) Type   | Description                                                                                                                                                                                                                                                                                                                                                                                                             |
|-----------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Cyclic                      | Data transfers at the period that you specify. The default range is 48…32,000 milliseconds.                                                                                                                                                                                                                                                                                                                             |
| Change of state (COS)       | Both the scanner and the device sends data whenever the data changes. You also specify a heartbeat period for the connection. •  If the data does not change within the heartbeat period, the scanner or device sends the data at the end of the period. •  This lets both the scanner and device know that the other is still operational.                                                                             |
| Strobed                     | The scanner sends a single strobed request to solicit data from the strobed devices. •  The request is 64 - bits long (1 bit for each node). •  In response to the request, each device that is configured for a strobed connection sends its data up to 8 bytes.                                                                                                                                                       |
| Polled                      | A point - to-point data transfer that occurs every I/O scan or as a ratio of the I/O scan (background). •  At the specified poll rate (every scan or background), the scanner sends data to a polled device up to 255 bytes. The data is either output data for the device or a request for input data from the device. •  If the polled device gets a request for input data, it sends its input data up to 255 bytes. |

## Background Poll

The foreground to background poll ratio lets you adjust how often the scanner polls certain devices for their data. In general, use the default values. Change them only if you need to tune the performance of your system.

| Parameter   | Description                                                                                                                                                             | Default Setting   |
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|
| Poll rate   | • Applies to a device with a polled connection. •  Defines whether the scanner polls the device every I/O scan (foreground) or as a ratio of the I/O scan (background). | Every scan        |

| Parameter                           | Description                                                                                                                                                                                                                     |   Default Setting |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|
| Foreground to background poll ratio | •  Applies to devices with a polled connection that is configured for a background poll rate. •  Determines how often the devices are polled. •  By default, the scanner performs background polls every scan (poll ratio = 1). |                 1 |

## This diagram shows the effect of a change to the poll ratio.

<!-- image -->

IMPORTANT When using a foreground to background poll ratio other than 1, the total network time -out value of the EPR may need to be increased so the background devices do not time out.

The expected packet rate (EPR) defaults to 75, which is then multiplied by 4 ms to get a 300 ms timeout for a polled/strobed I/O connection.

## Interscan Delay

## Change the Configuration of Your Network

## Upload the Current Configuration of the Scanner

The interscan delay determines how w long the scanner waits before it starts another I/O scan. Use these guidelines:

- In general, leave the interscan delay at its default value. Change it only if you need to tune the performance of your system.
- Keep the interscan delay ≥ 5 ms. Otherwise, you may have trouble accessing the network.

| Parameter       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Default Setting   |
|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|
| Interscan delay | • Last segment of the I/O scan. •  Starts after the last packet of the poll to the last node in the scanner’s scan list. •  Provides time for larger devices and slower responders to return their polled data. •  Provides time for software, such as RSLinx® and RSNetWorx™, to access the network for uploading, downloading, and browsing, for example. •  Scanner waits for the interscan delay before it strobes or polls devices again. •  A shorter interscan delay may improve the update time of strobed or polled data. | 10 ms             |

Complete these tasks to change the configuration of the network with RSNetWorx™ for DeviceNet software:

- Upload the Current Configuration of the Scanner on page 139
- Set the Interscan Delay and Poll Ratio on page 140
- Set the I/O Parameters of a Device on page 140
- Download the Configuration to the Scanner on page 63
- Save the Configuration File on page 44

Complete these steps to upload the current configuration.

1. Start RSNetWorx™ for DeviceNet software.
2. If necessary, open the file for the network.
3. Go online.
4. Double -click the scanner.
5. Click the Module tab.
6. Click Upload from Scanner.
7. When prompted, upload the configuration from the scanner.

<!-- image -->

<!-- image -->

## Set the Interscan Delay and Poll Ratio

## Set the I/O Parameters of a Device

Change the parameters shown below if needed.

- For information on changing the Interscan Delay parameter, refer to page 165 .
- For information on changing the Foreground to Background Poll Ratio parameter, refer to page 164 .

<!-- image -->

Complete these steps to set the I/O parameters of a device.

## To set the I/O parameters of a device

1. Select the Scanlist tab.

## Change of State or Cyclic Transfer

2. Select the device.
3. Select Edit I/O Parameters to display the Edit I/O Parameters dialog box.

<!-- image -->

Complete these steps to configure the I/O parameters for the Change of State setting.

1. Select Change of State/Cyclic check box.
2. Select the Change of State or Cyclic option.
3. Enter the number of bytes that the devices sends to the controller.
4. Enter the number of bytes that the controller sends to the device.
5. For a cyclic update, enter the period of the update.
6. Select OK .

<!-- image -->

## Strobed Transfer

## Polled Transfer

Complete these steps to configure the I/O parameters for the Strobed Transfer setting.

## To strobed transfer

1. Select Strobed .
2. If the single bit being sent to the strobed device needs to be accessed by the Logix controller, check Use Output Bit.
3. This lets you map the bit into the I/O data being transferred with the controller.
3. Enter the number of bytes that the device sends to the controller.
4. Select OK .

<!-- image -->

Complete these steps to configure the I/O parameters for the Polled setting.

1. Select Polled .
2. Enter the number of bytes that the device sends to the controller.
3. Enter the number of bytes that the controller sends to the device.
4. Choose whether to poll the device every scan or in the background.
5. Select OK .

<!-- image -->

## Download the Configuration to the Scanner

Save the Configuration File

Complete these steps to download the configuration to the scanner.

## To download the configuration to the scanner

1. Select Apply .
2. When prompted, select Yes to download the changes.
3. Select OK .

<!-- image -->

After you make a change to the network, upload the entire network and save the file. This makes sure that the offline configuration file matches the network.

Complete these steps to save the configuration file.

1. From the Network menu, choose Upload from Network.
2. When prompted, select Yes to upload the entire network.
3. Save the file.

## Automatic Device Recovery

## Automate the Replacement of a Failed Device

This chapter describes how to reduce the time it takes to replace a failed device.

| Topic                            | Page     |
|----------------------------------|----------|
| Automatic Device Recovery        | page 145 |
| Set Up Automatic Device Recovery | page 146 |

To reduce system downtime if a device fails, use the automatic device recovery (ADR) option. With ADR, you do not have to use any software tools to get a replacement device configured and online.

IMPORTANT Some devices do not support ADR.

<!-- image -->

## Set Up Automatic Device Recovery

## Choose an Electronic Key Level for a Device

You configure ADR on a device-by-device basis. You can set up the following ADR settings for each device.

| If you want to                                                                                  | And                                                                                                                   | Then select this ADR option for the device                 |
|-------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------|
| Automatically configure a replacement device that matches the electronic key of a failed device | Manually change the address of the replacement device                                                                 | ADR Settings: Configuration Recovery Auto-Address Recovery |
|                                                                                                 | Automatically set the address of the replacement device to the default address (63) of the failed device via software | ADR Settings: Configuration Recovery Auto-Address Recovery |
| Manually configure a replacement device                                                         |                                                                                                                       |                                                            |

<!-- image -->

ATTENTION: If a DeviceNet network has more than one scanner, enable Auto-Address Recovery for only one scanner. If more than one scanner is configured for Auto -Address Recovery, there is no way to determine which scanner will recognize a newly -inserted device on the DeviceNet network.

## Complete these tasks to set up ADR for a device:

- Choose an Electronic Key Level for a Device on page 146
- Update Your Network Configuration File on page 147
- Define the Electronic Key on page 147
- Enable Auto -Address Recovery for the Scanner on page 148
- Set the ADR Settings for the Device on page 149
- Download the Changes to the Scanner on page 150
- Upload and Save the Configuration File on page 63

<!-- image -->

Use the electronic key options to define how closely a replacement device must match a failed device before the scanner applies ADR. The scanner configures/addresses only a device that meets the check box items that are checked in the electronic key of the failed device.

If multiple devices with the same electronic key fail at the same time, the scanner disables auto -address recovery for those devices. This prevents the scanner from changing the address of the wrong device.

## Update Your Network Configuration File

When you set up ADR for a device, RSNetWorx™ for DeviceNet software reads the configuration for the device from the configuration file and stores it in the scanner. Before you set up ADR for a device, make sure the configuration file is up-to-date.

## To update your network configuration file

1. Go online.
2. Configure the device.
3. Right-click and upload the entire network.
4. Save the network configuration.

<!-- image -->

## Define the Electronic Key

Complete these steps to define the electronic key.

## To define the Electronic Key

1. Double -click the scanner.
2. Select the Scanlist tab.
3. Select the device.

4. Check the items that must match before a replacement device receives the configuration/address of the selected device.

<!-- image -->

## Enable Auto-Address Recovery for the Scanner

Complete these steps to enable Auto-Address Recovery.

## To enable Auto-Address Recovery for the scanner

1. Select the ADR tab.
2. Make sure Enable Auto -Address Recovery y is selected.
3. When prompted, select Yes to enable Auto -A -Address Recovery.

## Set the ADR Settings for the Device

<!-- image -->

Complete these steps to set the ADR settings for the device.

## To set the ADR settings for the device

1. Select the device.
2. Select the ADR settings for the device.
3. Read the configuration data of the device into the ADR configuration of the RSNetWorx™ project.

IMPORTANT Make sure you upload all changes made to a device online into the RSNetWorx™ project before you click the Load Device Config button.

<!-- image -->

## Download the Changes to the Scanner

## Upload and Save the Configuration File

Complete these steps to download changes to the scanner.

## To download the changes to the scanner

1. Select Apply .
2. When prompted, select Yes to download the changes.
3. Select OK .

<!-- image -->

Complete these steps to upload and save the configuration file.

## To upload and save the configuration file

1. Choose Network&gt;Upload from Network .
2. When prompted, select Yes to upload the entire network.
3. Save the file.

<!-- image -->

## Map the Memory Location with Advanced Mapping

Sometimes, an input or output value for a device may end up encapsulated within a larger tag. For example, a speed value may end up as the upper 16 bits of a DINT element in the scanner. To access the value, you would have to use additional programming.

<!-- image -->

To make your programming easier, re-map the value to its own tag within the data array of the scanner. This lets you access the value without additional programming.

<!-- image -->

Give a Value Its Own Memory Location

Complete these steps to give a value its own memory location in the input or output memory of the scanner.

## To give a value its own memory location

1. Select the device and select the Advanced button.
2. For the first map entry, specify the first bit of the data.
- a. Choose a connection type.
- z. Enter the starting byte of the data.
5. aa. Enter the starting bit of the data.
3. Specify the map location for the data.
- a. Choose the element number in the map.
- b. Enter the starting bit.
- c. Enter the number of bits.
4. Select Apply Mapping .
5. Select the next map number.
6. Specify the first bit of the data for the next map entry for this device.
- a. Choose a connection type.
- b. Enter the starting byte of the data.
- c. Enter the starting bit of the data.
7. Specify the map location for the data.

<!-- image -->

- a. Choose the element number in the map .
- b. Enter the starting bit.
- c. Enter the number of bits.
8. Select Apply Mapping .
9. Select Close w when you are done.

<!-- image -->

## Index

1

## 1756-DNB

use 17

1769-SDN

use 17

## 1784-PCIDS

data alignment 43, 61 use 17

## 1784-U2DN

driver 24 node address 20, 71

use

23, 36, 72

## 1788-CN2DN

use 17

1788-DNB

use 17

## 1788-EN2DN

use 17

## A

## address

assign 20

automatic recovery 145

device data 90

device replacement 145

options for setting 27

specify offline 36

## ADR

See automatic device recovery 145

## advanced mapping

configure 153

alias tags

use 92

## auto-address recovery

use 145

autobaud use 19

## automatic device recovery

configure 146

use 145

## autoscan

allocation size 83

enable 75

firmware requirements 69

overview 70

when to use 69

## B

## background poll

use 137

## baud rate

cable limits 19

options for setting 19

bridge across networks 17, 23

## C

## change of state

configure 141

overview 137

## class instance editor

use 96

command register use 94

communication card select 23

## computer

connect to network 23

## configuration recovery

use 145

## configure

automatic device recovery 146

change of state 141

cyclic 141

device 35, 54

driver 24

I/O parameters 140

interscan delay 140

message 98

network offline 33

network online 33, 49

poll 142

shared inputs 108

strobed 142

## connect

computer 23

## ControlNet

bridge options 17

COS

## DDE

access parameter 129

## device

access via RSView software 129

address data 90

auto-address recovery 145

automate replacement 145

configuration recovery 145

configure 35, 54

configure I/O parameters 140

configure offline 33

configure online 33, 49

detect failure 92

download configuration 54

get or set parameter 96

get or set parameter via logic 94

I/O parameters 137

specify address offline 36

update options 137

upload configuration 54

## DeviceNet

bridge options 17

cable limts 19 configure PanelView terminal 115

run network 94

## diagnostics

detect failure of device 92

## download

device configuration 54

network configuration 48

scanner configuration 63

## driver

configure 24

## E

## EDS file

interpret 95

## EtherNet/IP

bridge options 17

## explicit client tags

configure 126

explicit server tags access from controller 124

## See change of state 141

## cyclic

configure 141 overview 137

## D

## logic

configure 123

plan 121

## F

## foreground to background poll ratio 137 7

## G

## generate

report 44, 64

## I

## I/O allocation

in CompactLogix controller 67

in MicroLogix 1500 controller 67

## I/O data

define for device 140

## I/O memory

assign slave mode data 105 assign slave scanner 107 autoscan 83

## I/O parameters

configure 140

options 137 overview 137

## interlock

set up 103

## interscan delay

configure 140

examples 136

overview 139

## L

detect failed device detect failed device 92

## M

## message

configure 98

path 100

send from PanelView terminal 126

send to PanelView terminal 124

use 94

## mode

scanner 94

## MSG instruction

See message 98

## multicast input data

set up 108

## N

## network

add devices to diagram 34 configuration file 33, 51 download configuration 48 go online 46 interscan delay 139 run 94 upload configuration 63

## node

See address 20

## node commissioning tool

install 70

## O

## online

go 46

## OPC

access parameter 129

## P

## PanelView terminal

add to scan list 117

address data 119 configure communication 115 configure explicit client tags 126

configure explicit server tags 123

configure I/O slave tags 113

explicit client overview 113

explicit server overview 112

plan explicit server tags 121

select communication method 111

send message 126

send message to 124

## parameter

determine class, instance, attribute numbers 95

## path

## poll

```
define for message 100
```

change poll ratio 140

configure 142

overview 137

rate 137

ratio 137

## R

## report

generate 44, 64

## RS-232

## RSView software

## scan cycle

## scan list

## scanner

## select

## shared input

## slave mode

bridge options 17 access device 129 S examples 136 factors of performance 136 interscan delay 136, 139 add shared input 108 add slave scanner 106 I/O parameters 137 overview 38, 56 set I/O parameters 140 add PanelView terminal 117 adjust the status size 87 change interscan delay 140 change mode 94 change poll ratio 140 configure ADR 146 configure automatically 67 configure I/O parameters for device 140 configure offline 33 configure online 33, 49 download configuration 63 enable auto -address recovery 148 enable slave mode 104 interscan delay 139 scan list 38, 56 select 17 slave mode 103 upload configuration 56 communication card 23 scanner 17 add to scan list 108 enable for scanner 104 map data 105 use 103

## status

adjust scanner status size 87

## strobed

configure 142

overview 137

## U

## U2DN

node address 27

## upload

device configuration 54

network 63

scanner configuration 56

## Rockwell Automation support

Use these resources to access support information.

| Technical Support Center                         | Find help with how-to videos, FAQs, chat, user forums, and product notification updates.                  | rok.auto/support                        |
|--------------------------------------------------|-----------------------------------------------------------------------------------------------------------|-----------------------------------------|
| Knowledgebase                                    | rok.auto/knowledgebase                                                                                    | Access Knowledgebase articles.          |
| Locate the telephone number for your country.    | rok.auto/phonesupport                                                                                     | Local Technical Support Phone Numbers   |
| Literature Library                               | Find installation instructions, manuals, brochures, and technical data publications.  rok.auto/literature |                                         |
| Product Compatibility and Download Center (PCDC) | Get help determining how products interact, check features and capabilities, and                          | find associated firmware. rok.auto/pcdc |

## Documentation feedback

Your comments help us serve your documentation needs better. If you have any suggestions on how to improve our content, complete the form at rok.auto/docfeedback .

## Waste Electrical and Electronic Equipment (WEEE)

<!-- image -->

At the end of life, this equipment should be collected separately from any unsorted municipal waste.

Rockwell Automation maintains current product environmental information on its website at rok.auto/pec .

Allen -Bradley, expanding human possibility, Logix, Rockwell Automation, and Rockwell Software are trademarks of Rockwell Automation, Inc.

EtherNet/IP is a trademark of ODVA, Inc.

Trademarks not belonging to Rockwell Automation are property of their respective companies.

Rockwell Otomayson Ticaret A.Ş. Kar Plaza İş Merkezi E Blok Kat:6 34752, İçerenkÖy, İstanbul, Tel: +90 (216) 5698400 EEE YÖnetmeliğine Uygundur

Connectwithus.

<!-- image -->

<!-- image -->

<!-- image -->

rockwellautomation.com expandinghumanpossibility

AMERICAS:RockwellAutomation,1201SouthSec0ndStreet,Milwaukee,Wl53204-2496USA,Tel:(1)414.382.2000,Fax:(1)414.382.4444 EUR0PE/MIDDLEEAST/AFRICA:RockwellAutomationNV,PegasusPark,DeKleetlaan12a,1831Diegem,Belgium,Tel:(32)26630600,Fax:(32)26630640 ASIA PACIFIC: Rockwell Automation, Level 14, Core F, Cyberport 3,100 Cyberport Road, Hong Kong, Tel:(852)2887 4788,Fax:(852)2508 1846

<!-- image -->