<!-- image -->

## ControlNet Network Configuration

1756 ControlLogix, 1756 GuardLogix, 1769 CompactLogix, 1769 Compact GuardLogix, 1789 SoftLogix, Studio 5000 Logix Emulate

Rockwell Automation Publication CNET -UM001H -EN -P -March 2022 Supersedes Publication CNET -UM001G -EN -P -September 2020

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

| Subject                     | Reason                     |
|-----------------------------|----------------------------|
| Updated the Legal notices . | Legal information changed. |

## New or enhanced features

None in this release.

## Table of Contents

| Summary of Changes            | Studio 5000 environment  ................................ ................................ ...........   9  9                   |
|-------------------------------|---------------------------------------------------------------------------------------------------------------------------------|
| Preface                       | Additional Resources   .  ................................ ................................ .................   1  10           |
|                               | Legal Notices  ................................ ................................ ..............................   1  10         |
| ControlNet Overview           | Use ControlNet Communication Modules in a Control System   .  .............   1  11                                             |
|                               | Bridge Across Networks   .  ................................ ................................ ............  12                  |
|                               | Exchange Information on a ControlNet Network   .  ................................ ...   1  15                                  |
|                               | Network Update Time (NUT)   .  ................................ ..............................   1  16                          |
|                               | Requested Packet Interval (RPI)  ................................ .........................   1  17                             |
|                               | Actual Packet Interval (API)  ................................ ................................   1  18                         |
|                               | Understand the Effect of the NUT on the API   .  .............................   1  18                                          |
|                               | Schedule the Network   .  ................................ ................................ ..........   1  18                  |
|                               | Control of Scheduled I/O ................................ ...............................   1  19                               |
|                               | Understand the Network Keeper   .  ................................ ........................   1  19                            |
|                               | Default Parameters   .  ................................ ................................ .............   2  20                 |
|                               | ControlNet Network Capacity and Topology   .  ................................ ...........   2  21                              |
|                               | Topology   .  ................................ ................................ ................................   2  21        |
|                               | Number of Nodes   .  ................................ ................................ ................. 23                     |
|                               | Lengths   .  ................................ ................................ ................................ .. 23           |
| Connect a Computer to the     | Chapter 2 Configure the ControlNet Communication Driver in RSLinx Classic                                                       |
| ControlNet Network            | Software   .  ................................ ................................ ................................ ......   2  25 |
|                               | Chapter 3                                                                                                                       |
| Configure a ControlNet Module | Use Logix Designer Application  ................................ ...............................   2  27                        |
|                               | Configure the I/O Configuration Tree in Your Project   .  .....................   2  27                                         |
|                               | Add and Configure a Local ControlNet Module  ...............................  27                                                |
|                               | Add and Configure a Remote ControlNet Module   .  ............................   3  31                                          |
|                               | Communication Format ................................ ................................   3  33                                  |
|                               | Download the Project to the Logix 5000 Controller   .  ..........................   3  35                                       |
|                               | Electronic Keying   .  ................................ ................................ .................   3  36              |
|                               | Exact Match   .  ................................ ................................ ....................   3  37                 |
|                               | Compatible Keying  ................................ ................................ .......  38                                |
|                               | Disabled Keying  ................................ ................................ ............   4  40                         |
|                               | Use RSNetWorx for ControlNet Software ................................ ................   4  41                                 |
|                               | Schedule the Network Offline   .  ................................ ............................  42                             |
|                               | Schedule the Network Online  ................................ ............................  46                                  |

|                          | Reschedule a ControlNet Network that has Previously been                                                                                                                                                        |
|--------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                          | Scheduled   .  ................................ ................................ .............................   5  50                                                                                          |
|                          | Chapter 4                                                                                                                                                                                                       |
| Control I/O              | Set Up the Hardware  ................................ ................................ .................   5  53                                                                                                |
|                          | Requested Packet Interval (RPI)   .  ................................ ...............................   5  54                                                                                                   |
|                          | Communication Format   .  ................................ ................................ ............ 54                                                                                                     |
|                          | Direct or Rack - optimized Connections ................................ ..............   5  55                                                                                                                  |
|                          | Direct Connections for I/O Modules   .  ................................ ............ 56                                                                                                                        |
|                          | Rack - optimized Connections for I/O Modules  ...........................   5  57                                                                                                                               |
|                          | Ownership  ................................ ................................ ...........................  58                                                                                                    |
|                          | Choose the Type of Ownership for a Module   .  ............................... 59                                                                                                                               |
|                          | Add a Remote Adapter  ................................ ................................ ............... 59                                                                                                      |
|                          | Add Distributed I/O  ................................ ................................ ..................   6  60                                                                                               |
|                          | Distributed I/O Communication Formats   .  ................................ .........   6  61                                                                                                                   |
|                          | Access Distributed I/O  ................................ ................................ ..............  62                                                                                                    |
|                          | Validate Connections   .  ................................ ................................ ................  64                                                                                                |
|                          | Chapter 5                                                                                                                                                                                                       |
| Produce and Consume Tags | Terminology  ................................ ................................ ...............................   6  67                                                                                          |
| (interlock controllers)  | Set Up  the Hardware  ................................ ................................ .................   6  67                                                                                               |
|                          | Determine Connections for Produced and Consumed Tags  .................   6  68                                                                                                                                 |
|                          | Organize Tags for Produced or Consumed Data   .  ................................ ....   7  70                                                                                                                  |
|                          | Adjust for Bandwidth Limitations   .  ................................ ...........................   7  70 ................................ ................................ ..............................   7 |
|                          | Produce a Tag  71                                                                                                                                                                                               |
|                          | Consume a Tag  ................................ ................................ ...........................   7  74                                                                                            |
|                          | Chapter 6                                                                                                                                                                                                       |
| Messaging                | Set Up the Hardware  ................................ ................................ .................   7  79                                                                                                |
|                          | Guidelines for MSG Instructions  ................................ ............................  80                                                                                                              |
|                          | Determine Connections for Messages ................................ ......................   8  81                                                                                                              |
|                          | Guidelines for Caching Message Connections   .  ................................ ..   8  81                                                                                                                     |
|                          | Enter Message Logic  ................................ ................................ ..................   8  81 Add the ControlNet Modules and Remote Devices to the Local                                    |
|                          | Controller’s I/O Configuration  ................................ ...........................   8  81                                                                                                            |
|                          | Enter a Message  ................................ ................................ ..................  82                                                                                                       |
|                          | Configure a Message Instruction ................................ .............................  82                                                                                                              |
|                          | Stagger the Messages   .  ................................ ................................ ................  84                                                                                                |

|                            | Chapter 7                                                                                                        |
|----------------------------|------------------------------------------------------------------------------------------------------------------|
| Communicate with PanelView | Set Up the Hardware  ................................ ................................ .................   8  85 |
| Terminals                  | Determine Connections to PanelView Terminals   .  ................................ ...   8  86                   |
|                            | Add a PanelView Terminal   .  ................................ ................................ ........   8  86 |
|                            | Organize Controller Data for a PanelView Terminal  .............................   9  90                         |
| Index                      |                                                                                                                  |

## Studio 5000 environment

This manual describes how you can use ControlNet communication modules with your Logix 5000™ controller.

Use this manual if you program applications that use a ControlNet network with one of these Logix 5000 controllers:

- CompactLogix controller
- ControlLogix controller
- PowerFlex 700S with DriveLogix controller
- SoftLogix5800 controller

Also be familiar with the following:

- Networking concepts
- Logix Designer software
- FactoryTalk® Linx™ or RSLinx Classic software
- RSNetWorx for ControlNet software

Rockwell Automation recognizes that some of the terms that are currently used in our industry and in this publication are not in alignment with the movement toward inclusive language in technology. We are proactively collaborating with industry peers to find alternatives to such terms and making changes to our products and content. Please excuse the use of such terms in our content while we implement these changes.

The Studio 5000 Automation Engineering &amp; Design Environment® combines engineering and design elements into a common environment. The first element is the Studio 5000 Logix Designer® application. The Logix Designer application is the rebranding of RSLogix 5000® software and will continue to be the product to program Logix 5000™ controllers for discrete, process, batch, motion, safety, and drive-based solutions.

<!-- image -->

The Studio 5000® environment is the foundation for the future of Rockwell A Automation® engineering design tools and capabilities. The Studio

## Additional Resources

## Legal Notices

5000 environment is the one place for design engineers to develop all elements of their control system.

These documents contain additional information concerning related products from Rockwell Automation.

| Resource                                                                      | Description                                                                                                                     |
|-------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|
| ControlNet Modules Installation Instructions, publication CNET - IN005        | Describes how to install 1756 - CN2, 1756-CN2R, 1756-CN2RXT, 1756 - CNB, 1756-CNBR, 1768-CNB, and 1768-CNBR ControlNet modules. |
| Industrial Automation Wiring and Grounding Guidelines, publication 1770 - 4.1 | Provides general guidelines for installing a Rockwell Automation industrial system.                                             |
| Product Certifications website, http://www.ab.com                             | Provides declarations of conformity, certificates, and other certification details.                                             |

You can view or download publications at http://www.rockwellautomation.com/literature. To order paper copies of technical documentation, contact your local Rockwell Automation distributor or sales representative.

Rockwell Automation publishes legal notices, such as privacy policies, license agreements, trademark disclosures, and other terms and conditions on the Legal Notices page of the Rockwell Automation website.

## End User License Agreement (EULA)

You can view the Rockwell Automation End -User License Agreement ("EULA") by opening the License.rtf file located in your product's install folder on your hard drive.

## Open Source Licenses

The software included in this product contains copyrighted software that is licensed under one or more open source licenses. Copies of those licenses are included with the software. Corresponding Source code for open source packages included in this product are located at their respective web site(s).

Alternately, obtain complete Corresponding Source code by contacting Rockwell Automation via the Contact form on the Rockwell Automation website:

http://www.rockwellautomation.com/global/about-us/contact/contact.page Please include "Open Source" as part of the request text.

A full list of all open source software used in this product and their corresponding licenses can be found in the OPENSOURCE folder. The default installed location of these licenses is C:\Program Files (x86)\Common Files\Rockwell\Help\&lt;Product Name&gt;\Release Notes\OPENSOURCE\index.htm .

## Use ControlNet Communication Modules in a Control System

## ControlNet Overview

The ControlNet network provides high-speed transmission of time-critical I/O and interlocking data and messaging data. This data transfer capability enhances I/O performance and peer-to-peer communication in any system or application.

The ControlNet network is highly deterministic and repeatable and remains unaffected as devices are connected or disconnected from it. This ensures dependable, synchronized, and coordinated real-time performance.

The ControlNet network is most often used in these ways:

- As the default network for the ControlLogix platform
- As a backbone to multiple distributed DeviceNet networks
- As a peer interlocking network

This chapter describes how you can use ControlNet modules in a network control system.

| Topic                                                               | Page          |
|---------------------------------------------------------------------|---------------|
| Use ControlNet Communication Modules in a Control System on page 11 | 9 on page 11  |
| Bridge Across Networks on page 12                                   | 11 on page 12 |
| Exchange Information on a ControlNet Network on page 15             | 14 on page 15 |
| ControlNet Network Capacity and Topology on page 21                 | 21 on page 21 |

You can fit various ControlNet modules into your control system.

Figure 1 on page 10 shows the following:

- The controllers produce and consume tags among themselves.
- The controllers initiate MSG instructions that send/receive data or configure devices.
- The computer uploads and downloads projects to the controllers.
- The computer configures devices on the ControlNet network and configures the network itself.

## Bridge Across Networks

<!-- image -->

Figure 1 - ControlNet Modules and the Control System Overview

|   Item | Description                                                                                      |
|--------|--------------------------------------------------------------------------------------------------|
|      1 | Personal computer running SoftLogix5800 controller with 1784 - PCICS card                        |
|      2 | 1756 - CNB module (as an adapter) with 1756 I/O modules                                          |
|      3 | PowerFlex 700S drive                                                                             |
|      4 | 1794 - ACN15 adapter with 1794 I/O modules                                                       |
|      5 | 1734 - ACNR adapter with 1734 I/O modules                                                        |
|      6 | PanelView terminal                                                                               |
|      7 | CompactLogix 1769 - L35CR controller with local 1769 I/O modules                                 |
|      8 | ControlLogix controller with 1756 - CN2, 1756-CN2R, 1756-CNB, or 1756-CNBR module as the scanner |

IMPORTANT For an enhanced redundancy system, you must use a 1756-CNB, 1756 -CNBR, 1756-CN2 series B, or 1756-CN2R series B communication module. The 1756-CN2 or 1756 -CN2R series A module does not support enhanced redundancy. For more information, refer to the ControlLogix Enhanced Redundancy System User Manual, publication 1756 -UM535 .

Some ControlNet modules support the ability to bridge or route communication to and from different networks, depending on the capabilities of the platform and communication devices.

IMPORTANT You can only bridge across networks to communicate with devices. You cannot bridge across networks to control I/O, even though Logix Designer software can accept such a configuration in the I/O Configuration folder. All I/O control must originate and end on the same physical network.

The following table describes how communication can bridge across networks.

Table 1 - Bridging Across Networks

| A device on this network   | Can communicate with a device on this network   | Can communicate with a device on this network   | Can communicate with a device on this network   | Can communicate with a device on this network   |
|----------------------------|-------------------------------------------------|-------------------------------------------------|-------------------------------------------------|-------------------------------------------------|
|                            | EtherNet/IP                                     | ControlNet                                      | DeviceNet                                       | RS - 232(1)                                     |
| EtherNet/IP                | Yes                                             | Yes                                             | Yes                                             | Yes                                             |
| ControlNet                 | Yes                                             | Yes                                             | Yes                                             | Yes                                             |
| DeviceNet                  | No                                              | No                                              | Yes                                             | No                                              |
| RS - 232                   | Yes                                             | Yes(2)                                          | Yes                                             | Yes                                             |

In Figure 2, a workstation configures a drive on the DeviceNet network. The workstation bridges from the ControlNet network to the DeviceNet network to reach the drive. The bridge is a ControLogix chassis with ControlNet and DeviceNet modules.

<!-- image -->

<!-- image -->

|   Item | Description        |   Item | Description        |
|--------|--------------------|--------|--------------------|
|      1 | Workstation        |      4 | Drive              |
|      2 | PanelView terminal |      5 | DeviceNet network  |
|      3 | Bridge             |      6 | ControlNet network |

IMPORTANT The performance of a CompactLogix controller on a ControlNet network degrades significantly if you use the controller as a bridge. Target bridging over a CompactLogix controller on a ControlNet network toward applications that are not real -time dependent, such as Logix Designer software program downloads.

In the example shown above, you can transfer messages from the DeviceNet network through the Logix 5000 controller to an RSView32 operator interface.

With a CompactLogix controller as a bridge, you can map the data into the DeviceNet I/O image and then use RSLinx OPC to send the data to the Logix 5000 controller over the ControlNet network. This method conserves the limited bridging resources of your CompactLogix controller.

The following example shows how a DeviceNet bridge links to an EtherNet/IP network in RSLinx Classic software.

<!-- image -->

Figure 3 - EtherNet/IP Bridge Linking to a ControlNet Network

<!-- image -->

|   Item | Description                       |   Item | Description                      |
|--------|-----------------------------------|--------|----------------------------------|
|      1 | EtherNet/IP network               |      3 | ControlNet Bridge in 1756 system |
|      2 | EtherNet/IP bridge in 1756 system |      4 | ControlNet network               |

The following tables list the possible bridges between communication networks. Note that you can bridge from a ControlNet network to an Ethernet network and from an Ethernet network to a ControlNet via a SoftLogix virtual chassis. However, the products and methods you must use to do so are more detailed than can be effectively described in the following tables. For more information on how to bridge from one network to another via a SoftLogix virtual chassis, see the SoftLogix5800 System User Manual, publication 1789-UM002 .

Table 2 - Bridges from a ControlNet Network

| Destination Network   | Modules for a 1768 CompactLogix System                                              | Modules for a 1769 CompactLogix System                                                    | Modules for a ControlLogix Chassis                                                                         |
|-----------------------|-------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|
| DeviceNet             | • 1768 - L43 or 1768 - L45 controller •  1768 - CNB(R) module •  1769 - SDN scanner | •  1769 - L32C or 1769 - L35CR controller •  1769 - SDN scanner or 1788 - CN2DN module(1) | •  1756 - CN2 module •  1756 - CN2R module •  1756 - CNB module •  1756 - CNBR module •  1756 - DNB module |

| Destination Network   | Modules for a 1768 CompactLogix System                                              | Modules for a 1769 CompactLogix System   | Modules for a ControlLogix Chassis                                                                                                                                             |
|-----------------------|-------------------------------------------------------------------------------------|------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| EtherNet/IP           | • 1768 - L43 or 1768 - L45 controller •  1768 - CNB(R) module •  1768 - ENBT module | Not applicable                           | • 1756 - CN2 module •  1756 - CN2R module •  1756 - CNB module •  1756 - CNBR module •  1756 - ENBT module •  1756 - EN2T module •  1756 - EN2TR module •  1756 - EN3TR module |

Table 3 - Bridges from an EtherNet/IP Network

| Destination Network   | Modules for a 1768 CompactLogix System                                              | Modules for a 1769 CompactLogix System                                                   | Modules for a ControlLogix Chassis                                                                                                                                             | Modules for a 1769 CompactLogix Packaged Controller System                                                                  |
|-----------------------|-------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|
| ControlNet            | • 1768 - L43 or 1768 - L45 controller •  1768 - ENBT module •  1768 - CNB(R) module | Not applicable                                                                           | • 1756 - CN2 module •  1756 - CN2R module •  1756 - CNB module •  1756 - CNBR module •  1756 - ENBT module •  1756 - EN2T module •  1756 - EN2TR module •  1756 - EN3TR module | Not applicable                                                                                                              |
| DeviceNet             | • 1768 - L43 or 1768 - L45 controller •  1768 - ENBT module •  1769 - SDN scanner   | •  1769 - L32E or 1769 - L35E controller •  1769 - SDN scanner or 1788 - EN2DN module(1) | •  1756 - DNB module •  1756 - ENBT module •  1756 - EN2T module •  1756 - EN2TR module •  1756 - EN3TR module                                                                 | •  1769 - L23E - QB1B controller •  1769 - L23E - QBFC1B controller •  1769 - L23 - QBFC1B controller •  1769 - SDN scanner |

## Exchange Information on a ControlNet Network

ControlNet communication modules use a message-based protocol that implements a relative path to send a message from the producing module in a system to the consuming modules. This protocol also lets you communicate between devices on a ControlNet, DeviceNet, or EtherNet/IP network without writing additional application code.

With unscheduled data, the device from which a message originates, such as a Logix 5000 controller, contains the path information that makes sure the message reaches its consumers.

For a full explanation of unscheduled and scheduled data, see Network Update Time (NUT) on page 16 on page 16 .

Because the producing module holds this information, other modules along the path simply pass the information along and do not need to store it. The significant benefits include the following:

- You do not need to configure routing tables in the bridging module, which greatly simplifies maintenance and module replacement.
- You maintain full control over the route taken by each message, which enables you to select alternative paths for the same end module.

Scheduled data in Logix-based systems use the producer/consumer networking model instead of a source/destination (master/slave) model. The

## Network Update Time (NUT)

producer/consumer model reduces network traffic and increases transmission speed.

In traditional I/O systems, controllers poll input modules to obtain their input status. In a Logix system, digital input modules are not polled by a controller. Instead, they produce (multicast) their data either upon a change of state (COS) or periodically. The frequency of update depends upon the options chosen during configuration and where on the network the input module resides. The input module, therefore, is a producer of input data and the controller is a consumer of the data.

The controller can also produce data for other controllers to consume. The produced and consumed data is accessible by multiple controllers over the Logix backplane and the ControlNet network. This data exchange conforms to the producer/consumer model.

A ControlNet network link's most important function is to transport time -critical control information, such as I/O data and control interlocking. Other information that is not time -critical, such as program uploads and downloads, is also transported but does not interfere with time-critical messages because a ControlNet network can transmit scheduled and unscheduled data.

On a ControlNet network link, nodes transfer information by establishing connections. Each message sent by a producer contains a Connection ID (CID). Nodes that have been configured to recognize the CID consume the message, becoming consumers themselves.

Media access to the network is controlled by a time-slice access algorithm, Concurrent Time Domain Multiple Access (CTDMA), which regulates a node's opportunity to transmit in each network update interval (NUI). You configure how often the NUI repeats by selecting a network update time (NUT) in milliseconds.

The network update time (NUT) is the shortest interval in which data can be sent on a ControlNet network. It represents the fastest possible update rate for scheduled data transfers on that network. For example, a network that runs with a five ms NUT cannot send scheduled data at a rate faster than five ms. It can, however, send data at a slower rate. The minimum NUT you can specify is two ms. The NUT is divided into a three-part structure.

Table 4 - NUT Structure

| Parts of NUT   | Functions                                                                                                                                                   |
|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Scheduled      | On a sequential, rotating basis, every scheduled node can transmit data once per NUT. Time - critical information is sent during this part of the interval. |

| Parts of NUT   | Functions                                                                                                                                                                                                                                                                                                                                                                                                                          |
|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Unscheduled    | All nodes transmit on a sequential, rotating basis, the rotation repeating itself until the time allotted for this portion is used up. The number of scheduled transmissions determines the time available for unscheduled transmissions. On a ControlNet network, at least one node can transmit unscheduled data every NUT. Information that can be delivered without time constraints is sent during this part of the interval. |
| Maintenance    | The node with the lowest address transmits information to keep the other nodes synchronized. This time is automatically subtracted from your NUT. However, the time required for network maintenance is brief (microseconds) when compared to that used for the scheduled and unscheduled portions of the NUT.                                                                                                                     |

| Item                                               | Description                                        |
|----------------------------------------------------|----------------------------------------------------|
| Boundary moves according to scheduled traffic load | 1                                                  |
| Unscheduled traffic                                | 2                                                  |
| Network maintenance                                | 3                                                  |
| 4                                                  | Scheduled traffic. Each device transmits only once |
| Start                                              | 5                                                  |

<!-- image -->

The RPI is the update rate specified for a particular piece of data on the network. By using a rack-optimized connection, the RPI can specify the rate for an entire rack of I/O. With a direct connection, the RPI can specify the rate for a particular module or peer-to-peer data. When you add a module to the I/O configuration of a controller, you must configure the RPI, specifying how often to produce data for that module. For example, if you specify an RPI of 50 ms, every 50 ms the I/O module sends its data to the controller or the controller sends its data to the I/O module.

Set the RPI only as fast as needed by the application. The RPI also determines the number of packets per second that the module will handle on a connection. Each module has a limit of how many packets it can handle per second. If you exceed this limit, the module cannot open any more connections.

A faster RPI consumes more network bandwidth. So, to avoid wasting network bandwidth, set the RPI only as fast as is necessary. For example, if

## Requested Packet Interval (RPI)

## Actual Packet Interval (API)

## Understand the Effect of the NUT on the API

## Schedule the Network

your application uses a thermocouple module that has data change every 100 ms, do not set the RPI for that node at 5 ms because the network bandwidth is used to transmit mostly old data.

## IMPORTANT

You cannot set the RPI to a rate faster than the NUT. The network cannot send data at a rate that is faster than the NUT.

When you run RSNetWorx for ControlNet software, an Actual Packet Interval (API) is calculated. The API is equal to or faster than the RPI.

The API is the actual update rate for a particular piece of data on the network. A ControlNet network sets this rate equal to or faster than the RPI, based on the binary multiple of the NUT, which is the next fastest rate at which a module can send data. If this cannot be done, a ControlNet network provides reports that it cannot support the configuration.

This example illustrates how the NUT affects the API. A module on the network can produce data only at binary multiples of the NUT to a maximum of the NUT multiplied by 128. These multiples are referred to as rates on a ControlNet network. Therefore, with a NUT of 5 ms, the module can send data at these rates.

Table 5 - NUT Example Data Rates

| NUT   |   Multiple | Rate at Which Module Can Send Data   |
|-------|------------|--------------------------------------|
| 5 ms  |          1 | 5 ms                                 |
|       |          2 | 10 ms                                |
|       |          4 | 20 ms                                |
|       |          8 | 40 ms                                |
|       |         16 | 80 ms                                |
|       |         32 | 160 ms                               |
|       |         64 | 320 ms                               |
|       |        128 | 640 ms                               |

In this example, if you specify an RPI of 25 ms, then the network produces an API of 20 ms, which is the next fastest rate at which the module can send data. The module places the data on the network at every fourth network update interval to produce the 20 ms API. Similarly, if you specify an RPI of 150 ms, the network produces an API of 80 ms.

Connections over a ControlNet network can be one of the following:

- Scheduled — Data transferred at specific times.
- Unscheduled — Data transferred when the network can accommodate the transfer.

To use scheduled connections, you must schedule the ControlNet network via RSNetWorx for ControlNet software. For more information on how to schedule a ControlNet network with RSNetWorx for ControlNet software, see the section Use RSNetWorx for ControlNet Software on page 41 on page 44 on page 41 .

## Control of Scheduled I/O

## Understand the Network Keeper

You must use RSNetWorx for ControlNet software to enable any connection in a remote chassis. In addition, RSNetWorx software transfers configuration information for the remote modules, verifies and saves NUT and other userspecified network parameters, and establishes a schedule that is compliant with the RPI and other connection options specified for each module.

## IMPORTANT

RSNetWorx for ControlNet software must be run whenever a scheduled connection is added to, removed from, or changed in your system.

Scheduled connections let you send and receive data repeatedly at a predetermined rate. You can use the 1756-CNB or the 1756-CN2 module to control scheduled I/O when you use it in conjunction with a ControlLogix controller. When you place the module in the I/O configuration list of a ControlLogix controller and configure a second ControlLogix chassis with a remote 1756-CNB or 1756-CN2 module on the same ControlNet network, you can perform remote control operations on the I/O, or to a second controller in the second chassis.

In this case, the ControlLogix controller and the 1756-CN2 module in the local chassis together act as a scanner, while the 1756-CN2 module in the remote chassis with the I/O plays the role of an adapter.

Every ControlNet network requires at least one module to store programmed parameters for the network and configures the network with those parameters when the module is started. This module is called a keeper because it keeps the network configuration. RSNetWorx for ControlNet software configures the keeper.

To avoid a single point of failure, a ControlNet network supports multiple redundant keepers. These ControlNet communication modules are keeper-capable devices:

- 1756-CN2 and 1756 -CN2R modules
- 1756-CNB and 1756 -CNBR modules
- 1768-CNB and 1768 -CNBR modules
- 1769-L32C and 1769 -L35CR controllers
- 1784-PCICS and 1784 -PKTCS cards
- 1788-CNx x cards
- PLC -5C module

On a multi -keeper network, any keeper-capable module can keep the network at any legal node address (01...99). The multi-keeper-capable node with the lowest node address becomes the active keeper provided it is valid. It has been configured by RSNetWorx for ControlNet software and that configuration is the same as that of the first keeper that became active after the network was formed or reconfigured by RSNetWorx software.

## Default Parameters

If the active keeper is taken off the network, a valid back-up keeper can take over for it and continue to act as keeper. As long as at least one valid multi -keeper device is present on the network, new scheduled connections can be established.

To review the valid keeper devices on your network, follow this procedure in RSNetWorx for ControlNet software.

1. From the Network menu, choose Keeper Status .
2. Review the keeper devices on the Keeper Status dialog box.

<!-- image -->

On a typical network, the following must be true:

- There must be only one active valid keeper.
- All other keepers must be valid. If a keeper is not valid, it cannot perform any scheduled communication. However, all unscheduled communication occurs as expected.
- The keeper signature, shown in hex, must be the same for all nodes.

<!-- image -->

When a ControlNet network is first established, it relies on a default set of parameters capable of sending only unscheduled data. Default parameters in all ControlNet devices include the following:

- Network Update Time (NUT) = 100 ms
- Scheduled Maximum Node Address (SMAX) = 1
- The SMAX is the highest network address of a node that can use the scheduled service.
- Unscheduled Maximum Node Address (UMAX) = 99

## ControlNet Network Capacity and Topology

## Topology

Item

<!-- image -->

<!-- image -->

<!-- image -->

The UMAX is the highest network address of a node that can communicate on a ControlNet network. The UMAX must be set equal to or higher than the SMAX.

- Assumed maximum cable lengths and maximum number of repeaters

With this default ControlNet network, you can have unscheduled communication between the various devices on the network by using Logix Designer application and RSLinx software.

IMPORTANT To improve performance, configure a ControlNet network with RSNetWorx for ControlNet software. We recommend these settings:

- Set the Unscheduled Maximum Node Address (UMAX) equal to the highest node address on the network. Leaving this parameter at the default value of 99 wastes bandwidth and reduces system performance.
- Set the Scheduled Maximum Node Address (SMAX) to a value three or four above the highest scheduled node address, so you can expand the network in the future.

Also, be aware that each skipped node will subtract a small amount of bandwidth from the network.

When planning a ControlNet network, consider these factors:

- Topology
- Number of nodes
- Distances
- Connections

A ControlNet network supports a variety of topologies, including trunkline/dropline, star, tree, and ring redundancy. In its simplest form, a ControlNet network is a trunkline to which you connect nodes with a tap and a onemeter dropline.

Figure 5 - Example ControlNet Network Trunkline/Dropline Topology

<!-- image -->

Description

Trunkline

Node

Tap with dropline

Figure 6 - Example ControlNet Network Star Topology

<!-- image -->

<!-- image -->

Tip: Coax repeaters are typically used in trunkline and star topologies. See the ControlNet Coax Media Planning and Installation Guide, publication CNET -IN002, for more specific information on coax topologies you can create.

With fiber media, you can configure your network in trunkline, star, and ring topologies. Only the 1786 -RPFRL and 1786 -RPFRXL repeaters support a ring topology.

For more information, consult the ControlNet Fiber Media Planning and Installation Guide, publication CNET -IN001 .

## Number of Nodes

## Lengths

Figure 7 - Example ControlNet Network Ring Topology

<!-- image -->

| Item                              | Description                                       |
|-----------------------------------|---------------------------------------------------|
| Node                              | 1                                                 |
| Fiber cables                      | 2                                                 |
| Coaxial cable                     | 3                                                 |
| Tap with 1 m (3.28 ft) dropline 4 |                                                   |
| 5                                 | ControlNet Repeater Adapter and Fiber Ring Module |

Each ControlNet network supports up to 99 nodes. Logix 5000 controllers support multiple ControlNet networks, providing the flexibility to add nodes to a ControlNet network or boost performance.

In a ControlNet network, the maximum length depends on the number of nodes on a segment; a segment is a section of trunk between two terminators. Use repeaters to add segments or increase length.

Figure 8 - Maximum Length of a ControlNet Network

Maximum Allowable Segment Length = 1000 m (3280 ft) -16.3 m (53.4 ft) X [Number of Taps -2]

This graph assumes that a 1786 -RG6 cable is being used.

<!-- image -->

Configure the ControlNet Communication Driver in RSLinx Classic Software

## Connect a Computer to the ControlNet Network

This chapter explains how to set up a computer to operate on a ControlNet network.

<!-- image -->

| Topic                                                                               | Page          |
|-------------------------------------------------------------------------------------|---------------|
| Configure the ControlNet Communication Driver in RSLinx Classic Software on page 25 | 26 on page 25 |

You need to load a ControlNet communication driver for a computer to communicate with other devices on a ControlNet network. A computer uses this driver to do the following:

- Upload and download controller projects over ControlNet using Logix Designer software.
- Schedule the ControlNet network via RSNetWorx for ControlNet software.
- Operate an HMI type application.

Depending on the connection device, you can use one of these drivers:

- 1784-PCIC or 1784-PCICS card —Y —You must configure the driver in RSLinx Classic software, as described on page 26 on page 25 .
- USBCIP driver — Use only with a 1784-U2CN USB-to-ControlNet cable. You are not required to configure the driver in RSLinx Classic software.

IMPORTANT If you are running RSLinx Classic software, version 2.51, 2.52, or 2.53, you must manually install the USBCIP driver. To obtain the driver installation package, refer to answer ID 55431 on the Rockwell Automation Knowledgebase at http://support.rockwellautomation.com/Knowledgebase .

If you are running RSLinx Classic software, version 2.54 or later, the USBCIP driver is already installed on the computer.

After preparing the driver for use, connect the card or cable to the computer, and then connect the computer to the network.

To configure a ControlNet communication driver, perform this procedure in RSLinx Classic software.

<!-- image -->

1. From the Communications menu, choose Configure Drivers .

<!-- image -->

2. From the Available Driver Types pull-down menu, choose a driver for a ControlNet device.
3. Click Add New .

<!-- image -->

The Add New RSLinx Driver dialog box appears. The driver name defaults to AB\_xxx .

<!-- image -->

4. Type the name of the new ControlNet driver.
5. Click OK .

The Configure Device dialog box appears. The appearance of this screen varies, depending on the type of card used.

<!-- image -->

6. If your computer contains multiple cards, from the Serial Number (hex) field, choose the correct card.
7. In the Network Address (dec) box, type the correct network address.
8. Click OK .

The driver is now available and you can choose the ControlNet port from Who Active in the Logix Designer application.

## Use Logix Designer Application

## Configure the I/O Configuration Tree in Your Project

## Add and Configure a Local ControlNet Module

## Configure a ControlNet Module

This chapter explains how to configure a ControlNet communication module to operate on a ControlNet network.

| Topic                                            | Page          |
|--------------------------------------------------|---------------|
| Use Logix Designer Software on page 27           | 29 on page 27 |
| Use RSNetWorx for ControlNet Software on page 41 | 44 on page 41 |

IMPORTANT The example configuration process shown in this chapter uses a 1756-CN2R/B ControlLogix ControlNet bridge module in a ControlLogix controller project.

However, the overall configuration process, described in Configure the I/O Configuration Tree in Your Project on page 27, generally applies to any of the ControlNet communication modules covered in this manual.

Use the Logix Designer application to configure the I/O tree in your project.

When you use the Product\_Name\_RSL5K&gt; application to configure a ControlNet communication module, you must perform these tasks.

1. Add and Configure a Local ControlNet Module on page 27 .
2. Add and Configure a Remote ControlNet Module on page 31 .

## IMPORTANT

There are some differences between configuring a local ControlNet communication module and configuring a remote ControlNet communication module. Those differences are covered later in this chapter.

3. Download the Project to the Logix 5000 Controller on page 35 .

After you have started the Logix Designer application and created a controller project, you can add ControlNet communication modules. A local ControlNet module is a module that resides in the same chassis as the controller.

IMPORTANT When you create a new Logix Designer project with the CompactLogix 1769-L32C or 1769 -L35CR controller, the Controller Organizer creates a ControlNet port in the local chassis. In this case, you do not need to add a separate local communication module.

## To add a local ControlNet module

1. In the Logix Designer application, expand the I/O Configuration folder, right-click the backplane, and select New Module .
2. On the Select Module Type dialog box, type ControlNet in the Enter Search Text for Module Type box, choose the local ControlNet communication module, and then click Create .

<!-- image -->

<!-- image -->

This table lists the ControlNet communication modules available locally in the local chassis, computer, or controller with each Logix 5000 controller.

Table 6 -ControlNet Communication Modules Available Locally

| Logix 5000 Controller   | Local ControlNet Communication Module                                      |
|-------------------------|----------------------------------------------------------------------------|
| 1768 CompactLogix       | 1768 - CNB, 1768-CNBR                                                      |
| 1769 CompactLogix       | 1769 - L32C and 1769 - L35CR controllers have a built - in ControlNet port |
| ControlLogix            | 1756 - CN2, 1756-CN2R, 1756-CNB, 1756-CNBR                                 |
| SoftLogix               | 1784 - PCIC, 1784-PCICS                                                    |

3. Complete the fields on the New Module dialog box and then click OK .

<!-- image -->

| Field             | Action                                                                            |
|-------------------|-----------------------------------------------------------------------------------|
| Name              | Type a name for the local ControlNet module.                                      |
| Node              | Enter the module’s node number on the network.                                    |
| Description       | Type a description of the local ControlNet module.                                |
| Slot              | Enter the module’s slot number in the chassis.                                    |
| Revision          | Choose a major and minor revision of Logix Designer software.                     |
| Electronic Keying | Choose a keying option, as described in Electronic Keying on page 37 on page 36 . |

<!-- image -->

4. On the Module Properties dialog box, configure the connection properties and then click Apply .

<!-- image -->

| Connection Property                                             | Action                                                                                                                                                                                                                                                                                                                                            |
|-----------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inhibit Module                                                  | If the module does not need to communicate with the controller, check the checkbox. or If the module needs to communicate with the controller, leave the checkbox cleared. IMPORTANT: When you test this portion of the system, leave the checkbox cleared.                                                                                       |
| Major Fault On Controller If Connection Fails While In Run Mode | If you want the controller to produce a major fault if the connection to the local communication module fails in Run mode, check the checkbox. or If you want the controller to continue operating if the connection to the local communication module fails in Run mode, leave the checkbox cleared. Use ladder logic to monitor the connection. |

<!-- image -->

## Add and Configure a Remote ControlNet Module

After you have added the local ControlNet communication module, you must add remote ControlNet communication modules. A remote ControlNet module is a module that resides in a a chassis separate from the controller.

## To add a remote ControlNet module

1. In the Logix Designer application, right-click the local ControlNet communication module and choose New Module .
2. On the Select Module Type dialog box, type ControlNet in the Enter Search Text for Module Type box, select a remote ControlNet communication module, and then click OK .

<!-- image -->

You can connect any remote ControlNet communication module to a local ControlNet communication module.

<!-- image -->

## IMPORTANT

This procedure shows the New Module dialog box for a 1756-CN2. However, various dialogs appear during configuration depending on the ControlNet module you select. For help configuring a module, refer to the online help in the Logix Designer application.

3. Complete the fields on the New Module dialog box and then click OK .

Field

Name

Node

Description

Chassis Size

Comm Format

Slot

Revision

Electronic Keying

Action

Type a name for the local ControlNet module.

Enter the module's node number on the network.

Type a description of the local ControlNet module.

Enter the total number of slots in the chassis.

Choose a communication format, as described in Communication Format on page 54below

.

You do not need to assign a communication format for 1784

1784

-

PCICS, or 1788-CNx cards.

Enter the module's slot number in the chassis.

Choose a major and minor revision of Logix Designer software.

Choose a keying option, as described in Electronic Keying on page 37 on page 36

.

-

PCIC,

<!-- image -->

## Communication Format

The communication format determines the following:

- What configuration options are available

For example, if the module uses None, then you do not have to configure an RPI rate on the Module Properties dialog box.

- What type of data is transferred between the owner-controller and I/O connected via the communication module
- What tags are generated when configuration is complete
- The type of connection between the owner-controller and the I/O connected via the communication module

The communication format setting also affects the RPI rate.

Table 7 - Communication Formats

| Communication Format   | Function                                                                                                                                                                                                                                                              | Effect on RPI                                                                                                                                                               |
|------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Rack - optimized       | The communication module creates a rack image and returns I/O data in the rack image to the owner - controller. This option is available only for digital I/O modules. Remember that diagnostic I/O modules will not return diagnostic data when you use this format. | You can specify an RPI that meets this criteria: •  Equal to or greater than the NUT •  In the range permitted by Logix Designer programming software, for example 2…750 ms |

| Communication Format                                                                   | Function                                                                                                                                                                                                                                                                                                                    | Effect on RPI                                                                                                                                                                                        | Effect on RPI                                                                                                                                                                                        | Effect on RPI                                                                                                                                                                                        | Effect on RPI                                                                                                                                                                                        | Effect on RPI                                                                                                                                                                                        |
|----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Listen - only rack - optimized (not available on all ControlNet communication modules) | The communication module creates a rack image and returns I/O input data in the rack image to the owner - controller. The difference between this choice and rack - optimized is that the I/O data in the rack image is returned to a controller that does not control the outputs but is listening only to its input data. | When you set the RPI for a remote ControlNet communication module, we recommend you use a rate that is a power of two times the NUT. For example, if your NUT = 5 ms, we recommend these RPI values. | When you set the RPI for a remote ControlNet communication module, we recommend you use a rate that is a power of two times the NUT. For example, if your NUT = 5 ms, we recommend these RPI values. | When you set the RPI for a remote ControlNet communication module, we recommend you use a rate that is a power of two times the NUT. For example, if your NUT = 5 ms, we recommend these RPI values. | When you set the RPI for a remote ControlNet communication module, we recommend you use a rate that is a power of two times the NUT. For example, if your NUT = 5 ms, we recommend these RPI values. | When you set the RPI for a remote ControlNet communication module, we recommend you use a rate that is a power of two times the NUT. For example, if your NUT = 5 ms, we recommend these RPI values. |
| None                                                                                   | No RPI is required.                                                                                                                                                                                                                                                                                                         | The RPI field is dimmed.                                                                                                                                                                             | The RPI field is dimmed.                                                                                                                                                                             | The RPI field is dimmed.                                                                                                                                                                             | The RPI field is dimmed.                                                                                                                                                                             | The RPI field is dimmed.                                                                                                                                                                             |

## 4. On the Module Properties dialog box, configure the connection properties and then click Apply .

| Connection Property                                             | Action                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|-----------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Requested Packet Interval (RPI)                                 | Type the requested packet interval between 2.0…750.0 ms. If your module uses one of the rack - optimized communication formats, the RPI must be equal to or greater than the ControlNet Network Update Time (NUT).                                                                                                                                                                                                                                                                                                                                                                                   |
| Inhibit Module                                                  | If the module does not need to communicate with the controller, check the checkbox. or If the module needs to communicate with the controller, leave the checkbox cleared. IMPORTANT: When you test this portion of the system, leave the checkbox cleared.                                                                                                                                                                                                                                                                                                                                          |
| Major Fault On Controller If Connection Fails While In Run Mode | If you want the controller to produce a major fault if the connection to the local communication module fails in Run mode, check the checkbox. or If you want the controller to continue operating if the connection to the local communication module fails in Run mode, leave the checkbox cleared. Use ladder logic to monitor the connection.                                                                                                                                                                                                                                                    |
| Use Scheduled Connection over ControlNet                        | Check the box if you want to explicitly schedule the network connection. Note the following: •  The checkbox is enabled when the connection for the module crosses ControlNet and the module supports unscheduled connections. •  The checkbox is checked and disabled when the connection to the module crosses ControlNet, and the module does not support unscheduled connections, and therefore, must be scheduled. •  The checkbox is cleared and disabled when the connection to the module does not cross ControlNet, or the connection crosses ControlNet but does not need to be scheduled. |

<!-- image -->

## Download the Project to the Logix 5000 Controller

When you have added the local and remote ControlNet communication modules to your Logix Designer project, download the new configuration to your Logix 5000 controller.

<!-- image -->

To download a project to a Logix 5000 controller, follow this procedure.

1. Because you must schedule the ControlNet network before by using the new configuration, switch your Logix 5000 controller to Program mode using one of these methods:
- Turn the controller keyswitch to PROG.
- Turn the controller keyswitch to REM and use Logix Designer software.
2. In the Logix Designer application, from the Communications menu, choose Who Active .

<!-- image -->

## Electronic Keying

3. From the Who Active dialog box, browse to and select the controller to which to download a project and click Download .
4. When the Download dialog box appears, click Download .

<!-- image -->

Electronic Keying reduces the possibility of using the wrong device in a control system. Electronic Keying compares the device defined in the project to the installed device. If keying fails, a fault occurs.

These attributes are compared:

| Attribute      | Description                                                             |
|----------------|-------------------------------------------------------------------------|
| Vendor         | The device manufacturer.                                                |
| Device Type    | The general type of the device, for example, digital I/O module.        |
| Product Code   | The specific type of device. The Product Code maps to a catalog number. |
| Major Revision | A number that represents the functional capabilities of a device.       |
| Minor Revision | A number that represents behavior changes in the device.                |

These Electronic Keying options are available:

| Keying Option     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|-------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Compatible Module | Lets the installed device accept the key of the device that is defined in the project when the installed device can emulate the defined device. Typically, use Compatible Module to replace a device with another device that has these characteristics: •  Same catalog number •  Same or higher Major Revision •  Minor Revision: •  If the Major Revision is the same, the Minor Revision must be the same or higher.                                                                                                                                                                                                                                                      |
| Disable Keying    | •  If the Major Revision is higher, the Minor Revision can be any number. Indicates that the keying attributes are not considered when attempting to communicate with a device. With Disable Keying, communication can occur with a device other than the type specified in the project. ATTENTION: Be extremely cautious when using Disable Keying. If used incorrectly, this option can lead to personal injury or death, property damage, or economic loss. We strongly recommend not using Disable Keying . If using Disable Keying, take full responsibility for understanding whether the device being used can fulfill the functional requirements of the application. |
| Exact Match       | Indicates that all keying attributes must match to establish communication. If any attribute does not match precisely, communication with the device does not occur.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |

<!-- image -->

## Carefully consider the implications of each keying option when selecting one.

IMPORTANT Changing Electronic Keying parameters online interrupts connections to the device and any devices that are connected through the device. Connections from other controllers can also be broken.

A loss of data may occur if an I/O connection to a device is interrupted.

Exact Match keying requires all keying attributes, that is, Vendor, Product Type, Product Code (catalog number), Major Revision, and Minor Revision, of the physical module and the module created in the software to match precisely in order to establish communication. If any attribute does not match precisely, I/O communication is not permitted with the module or with modules connected through it, as in the case of a communication module.

Use Exact Match keying when you need the system to verify that the module revisions in use are exactly as specified in the project, such as for use in highly-regulated industries. Exact Match keying is also necessary to enable Automatic Firmware Update for the module via the Firmware Supervisor feature from a Logix 5000 controller.

In the following scenario, Exact Match keying prevents I/O communication.

The module configuration is for a 1756-IB16D module with module revision 3.1. The physical module is a 1756-IB16D module with module revision 3.2. In this case, communication is prevented because the Minor Revision of the module does not match precisely.

## Exact Match

## Example

## Compatible Keying

## Module Configuration:

Vendor = Allen - Bradley Product Type = Digital Input Module Catalog Number = 1756 - IB16D Major Revision = 3

Minor Revision = 1

Communication is prevented.

## Physical Module:

Vendor = Allen -Bradley Product Type = Digital Input Module Catalog Number = 1756 -IB16D Major Revision = 3

Minor Revision = 2

<!-- image -->

<!-- image -->

<!-- image -->

IMPORTANT Changing electronic keying selections online may cause the I/O Communication connection to the module to be disrupted and may result in a loss of data.

Compatible Keying indicates that the module determines whether to accept or reject communication. Different module families, communication adapters, and module types implement the compatibility check differently based on the family capabilities and on prior knowledge of compatible products.

Compatible Keying is the default setting. Compatible Keying allows the physical module to accept the key of the module configured in the software, provided that the configured module is one the physical module is capable of emulating. The exact level of emulation required is product and revision specific.

With Compatible Keying, you can replace a module of a certain Major Revision with one of the same catalog number and the same or later, that is higher, Major Revision. In some cases, the selection makes it possible to use a replacement that is a different catalog number than the original. For example, you can replace a 1756-CNBR module with a 1756-CN2R module. Release notes for individual modules indicate the specific compatibility details.

When a module is created, the module developers consider the module's development history to implement capabilities that emulate those of the previous module. However, the developers cannot know future developments. Because of this, when a system is configured, we recommend that you

configure your module by using the earliest, that is, lowest, revision of the physical module that you believe will be used in the system. By doing this, you can avoid the case of a physical module rejecting the keying request because it is an earlier revision than the one configured in the software.

## Example

## Example

## In the following scenario, Compatible Keying prevents I/O communication:

The module configuration is for a 1756 -IB16D module with module revision 3.3. The physical module is a 1756 -IB16D module with module revision 3.2. In this case, communication is prevented because the minor revision of the module is lower than expected and may not be compatible with 3.3.

## Module Configuration:

Vendor = Allen - Bradley

Product Type = Digital Input Module

Catalog Number = 1756

- IB16D

Major Revision = 3

Minor Revision = 3

Communication is prevented.

## Physical Module:

Vendor = Allen - Bradley

Product Type = Digital Input Module

Catalog Number = 1756

- IB16D

Major Revision = 3

Minor Revision = 2

<!-- image -->

<!-- image -->

<!-- image -->

In the following scenario, Compatible Keying allows I/O communication:

The module configuration is for a 1756 -IB16D module with module revision 2.1. The physical module is a 1756 -IB16D module with module revision 3.2. In this case, communication is allowed because the major revision of the physical module is higher than expected and the module determines that it is compatible with the prior major revision.

## Module Configuration:

Vendor = Allen - Bradley

Product Type = Digital Input Module

Catalog Number = 1756 - IB16D

Major Revision = 2

Minor Revision = 1

Communication is allowed.

<!-- image -->

<!-- image -->

## Disabled Keying

## Example

## Physical Module:

Vendor = Allen - Bradley

Product Type = Digital Input Module

Catalog Number = 1756 - IB16D

Major Revision = 3

Minor Revision = 2

<!-- image -->

IMPORTANT Changing electronic keying selections online may cause the I/O communication connection to the module to be disrupted and may result in a loss of data.

Disabled Keying indicates the keying attributes are not considered when attempting to communicate with a module. Other attributes, such as data size and format, are considered and must be acceptable before I/O communication is established. With Disabled Keying, I/O communication may occur with a module other than the type specified in the I/O Configuration tree with unpredictable results. We generally do not recommend using Disabled Keying.

<!-- image -->

ATTENTION: Be extremely cautious when using Disabled Keying; if used incorrectly, this option can lead to personal injury or dea loss.

If you use Disabled Keying, you must take full responsibility for understanding whether the module being used can fulfill the functional requirements of the application.

In the following scenario, Disable Keying prevents I/O communication:

The module configuration is for a 1756 -IA16 digital input module. The physical module is a 1756 -IF16 analog input module. In this case, communication is prevented because the analog module rejects the data formats that the digital module configuration requests.

## Module Configuration:

Vendor = Allen - Bradley

Product Type = Digital Input Module

Catalog Number = 1756 Major Revision = 3

- IA16

Minor Revision = 1

Communication is prevented.

## Physical Module:

Vendor = Allen - Bradley

Product Type = Analog Input Module Catalog Number = 1756 - IF16

Major Revision = 3

Minor Revision = 2

<!-- image -->

<!-- image -->

<!-- image -->

## Example

## Use RSNetWorx for ControlNet Software

## Schedule a ControlNet Network for the First Time

In the following scenario, Disable Keying allows I/O communication:

The module configuration is for a 1756 -IA16 digital input module. The physical module is a 1756 -IB16 digital input module. In this case, communication is allowed because the two digital modules share common data formats.

## Module Configuration:

Vendor = Allen - Bradley

Product Type = Digital Input Module

Catalog Number = 1756 - IA16

Major Revision = 2

Minor Revision = 1

Communication is allowed.

## Physical Module:

Vendor = Allen -Bradley

Product Type = Digital Input Module

Catalog Number = 1756 -IB16

Major Revision = 3

Minor Revision = 2

<!-- image -->

<!-- image -->

<!-- image -->

IMPORTANT Changing electronic keying selections online may cause the I/O communication connection to the module to be disrupted and may result in a loss of data.

You must use RSNetWorx for ControlNet software to schedule the network in order to activate the configured I/O devices in your application. You must also reschedule the network if a change is made to an already-scheduled network.

RSNetWorx for ControlNet software stores information in keeper devices. These ControlNet communication modules are keeper-cable devices:

- 1756-CN2 and 1756 -CN2R modules
- 1756-CNB and 1756 -CNBR modules
- 1768-CNB and 1768 -CNBR module
- 1769-L32C and 1769 -L35CR controllers
- 1784-PCICS and 1784 -PKTCS cards

If you configure a keeper on one network and then use it on another network, the conflicting information can make it difficult to use RSNetWorx for ControlNet software to schedule the new network. In extreme cases, it may be difficult to go online:

## Schedule the Network Offline

- For more information on the network keeper, see the section Understand the Network Keeper on page 19on page 19 on page 19 .
- For more information on how to reset valid keepers to an unconfigured state to resolve mismatches, refer to the RSNetWorx for ControlNet software online help.
- For more information on how to clear the memory or keeper information in a ControlNet communication module, refer to the Knowledgebase at http://www.rockwellautomation.com/support .

Scheduling a project offline is most useful in the design phase of your project. Scheduling off line can be used to predict performance and measure bandwidth.

<!-- image -->

Tip: To learn more about using Logix Designer and RSNetWorx software offline to predict performance, refer to answer ID 54793 on the Rockwell Automation Knowledgebase at http://support.rockwellautomation.com/Knowledgebase .

Before scheduling a network offline, make sure of the following:

- Your Logix Designer software project uses one controller and one network. We recommend that you use only one 1756-CN2, 1756-CNB, or 1768-CNB module in the local chassis when scheduling the network offline.
- Your Logix Designer software project is complete but has not been downloaded to the controller.

If your network has already been scheduled and you made a change to it, you must reschedule it. For more information, refer to Reschedule a ControlNet Network that has Previously been Scheduled on page 53 on page 50 .

To schedule a network offline, perform this procedure.

1. In your Logix Designer software project, right-click your local ControlNet module and choose Properties .
2. From the Module Properties dialog box, click the RSNetWorx tab.

<!-- image -->

<!-- image -->

3. In the ControlNet file field, type a name for a new ControlNet file.
4. Click Apply .
5. When a message appears prompting you to create the file, click Yes . This action creates the file that RSNetWorx for ControlNet software uses offline to browse and schedule the network.
6. Select Schedule the ControlNet network .
7. Click the icon circled below to launch RSNetWorx for ControlNet software.
8. To enable edits in the schedule, in RSNetWorx for ControlNet software, select Edits Enabled .

<!-- image -->

<!-- image -->

9. To change the network properties from default settings to those that best fit your network, from the Network menu, choose Properties .
10. O On the Network Parameters tab, configure the network parameters, as described in the table below, and click OK .
11. Click the Media Configuration tab.

<!-- image -->

<!-- image -->

| Parameter                | Description                                                                                                                                                                                                                                                                                                          |
|--------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Network Update Time (ms) | The smallest user - configurable repetitive time cycle at which data can be sent on a ControlNet network.                                                                                                                                                                                                            |
| Max Scheduled Address    | This is the node with the highest network address that can use scheduled time on a ControlNet link. I/O data is transferred during scheduled time. RSNetWorx for ControlNet software sets this value. We recommend that you not change it.                                                                           |
| Max Unscheduled Address  | Node with the highest network address that can use unscheduled time on a ControlNet link. Messaging data is transferred during unscheduled time. Nodes set at addresses higher than the maximum unscheduled node do not communicate on the network. For example, they will not display in FactoryTalk Linx software. |
| Media Redundancy         | Designates if the network uses media redundancy.                                                                                                                                                                                                                                                                     |
| Network Name             | User - defined name of the network.                                                                                                                                                                                                                                                                                  |

<!-- image -->

Generally, you can use the default media configuration.

12. A Adjust the configuration if your network is longer or uses repeaters.

## Schedule the Network Online

If the media configuration does not accurately represent the maximum propagation delay between any two nodes, your network may experience errors.

<!-- image -->

13. Click OK .
14. On the Save Configuration dialog box, select Optimize and rewrite the schedule for all connections .
15. Click OK .
16. Return to your Logix Designer software project.
- a. Save your project to update the network file in your Logix Designer project.
- b. Download your project as described in Download the Project to the Logix 5000 Controller on page 36 on page 35 .

<!-- image -->

Prior to scheduling a network online, make sure that all keepers are unconfigured or do not conflict with the current network. If your network has already been scheduled and you made a change to it, you must reschedule it.

Refer to Reschedule a ControlNet Network that has Previously been Scheduled on page 50 on page 53 on page 50 for more information.

To schedule a network online, follow this procedure in RSNetWorx for ControlNet software.

1. From the File menu, choose New .

<!-- image -->

2. From the New File dialog box, select a ControlNet configuration for the new file and click OK .
3. From the Network menu, choose Online .
4. From the Browse for Network dialog box, expand the tree to find and select a communication path to the ControlNet network and click OK .

<!-- image -->

<!-- image -->

<!-- image -->

This example uses a previously configured communication path to the controller. Here, the computer is connected to the ControlNet network via a 1784 -PCIC card. The driver was previously configured via RSLinx software, as described in Connect a Computer to the ControlNet Network on page 25 on page 25 .

5. From the Network menu, choose Single Pass Browse .
6. Check Edits Enabled .

<!-- image -->

When you enable edits, RSNetWorx for ControlNet software reads data in the ControlNet modules and builds a schedule for the network.

<!-- image -->

7. To change the network properties from default settings to those that best fit your network, from the Network menu, choose Properties .
8. On the Network Parameters tab, configure the network parameters as described in the table below.

<!-- image -->

<!-- image -->

| Parameter               | Description                                                                                                                                                                                                                                                                                                    |
|-------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Network Update Time     | The smallest user - configurable repetitive time cycle in milliseconds at which data can be sent on a ControlNet link.                                                                                                                                                                                         |
| Max Scheduled Address   | The node with the highest network address that can use scheduled time on a ControlNet link. I/O data is transferred during scheduled time. RSNetWorx for ControlNet software sets this value. We recommend that you do not change it.                                                                          |
| Max Unscheduled Address | The node with the highest network address that can use unscheduled time on a ControlNet link. Messaging data is transferred during unscheduled time. Nodes set at addresses higher than the maximum unscheduled node do not communicate on the network. For example, they will not display in RSLinx software. |
| Media Redundancy        | Designates if the network uses media redundancy on any of the network communication modules.                                                                                                                                                                                                                   |
| Network Name            | A user - defined name for the network.                                                                                                                                                                                                                                                                         |

<!-- image -->

9. Click the Media Configuration tab, modify the settings if needed, and click OK .

Generally, you can use the default media configuration. Adjust the configuration if your network is longer or uses repeaters.

IMPORTANT

If the media configuration does not accurately represent the maximum propagation delay between any two nodes, your network may experience errors.

<!-- image -->

10. F From the File menu, choose Save .
11. From the Save Configuration dialog box, select Optimize and rewrite the schedule for all connections .

12. Click OK .

<!-- image -->

## Reschedule a ControlNet Network that has Previously been Scheduled

## IMPORTANT

It is better to optimize connections. However, in some cases involving multiple controllers, the Merge changes into existing schedule option is available. This option lets controllers whose connections have not changed to continue uninterrupted operation. When you merge changes into the existing schedule, those controllers whose connections have not changed remain in Run mode rather than changing to Program mode.

13. In the Logix Designer application, save the online project.

If you change a previously scheduled network, you must reschedule the network to apply the changes. For example, if you add I/O to an existing ControlNet network, you must reschedule the network for the I/O to become active.

To reschedule an already scheduled ControlNet network, follow this procedure in RSNetWorx for ControlNet software.

1. From the File menu, choose Open .
2. From the Open dialog box, select the ControlNet file that matches the existing network and click Open .
3. From the Network menu, choose Online .
4. Check Edits Enabled .

<!-- image -->

<!-- image -->

<!-- image -->

When you enable edits, RSNetWorx for ControlNet software reads data in the ControlNet modules and builds a schedule for the network.

<!-- image -->

5. Save the file.

6. From the Save Configuration dialog box, select Optimize and rewrite the schedule for all connections .
7. Click OK .

<!-- image -->

IMPORTANT

It is better to optimize connections. However, in some cases involving multiple controllers, the Merge changes into existing schedule option is available. This option lets controllers whose connections have not changed to continue uninterrupted operation. When you merge changes into the existing schedule, those controllers whose connections have not changed remain in Run mode rather than changing to Program mode.

8. In the Logix Designer application, save the online project.

## Set Up the Hardware

## Control I/O

This chapter explains how a controller controls distributed I/O over a ControlNet network.

<!-- image -->

| Topic                                      | Page          |
|--------------------------------------------|---------------|
| Set Up the Hardware on page 85             | 56 on page 85 |
| Requested Packet Interval (RPI) on page 54 | 56 on page 54 |
| Communication Format on page 54            | 57 on page 54 |
| Add a Remote Adapter on page 59            | 63 on page 59 |
| Add Distributed I/O on page 60             | 63 on page 60 |
| Access Distributed I/O on page 62          | 65 on page 62 |
| Validate Connections on page 64            | 68 on page 64 |

To control distributed I/O over a ControlNet network, you must do the following:

- Add local and remote ControlNet communication modules to your Logix Designer project.

When you create a new Logix Designer project with the CompactLogix 1769-L32C or 1769-L35CR controller, the Controller Organizer creates a ControlNet port in the local chassis. In this case, you do not need to add a separate local communication module.

- Add distributed I/O to your Logix Designer project.
- Schedule the ControlNet network via RSNetWorx for ControlNet software.
- Use the I/O information in the Logix Designer application.

You can also validate connections to distributed I/O when controlling it over a ControlNet network. This task is particularly useful when one or more of the connections are not working but is not required, especially when all connections appear to work normally.

In this example, the Logix 5000 controller uses a ControlNet communication module in the local chassis to connect to the ControlNet network. The distributed (remote) I/O has a ControlNet adapter to connect it to the ControlNet network.

## Requested Packet Interval (RPI)

## Communication Format

Figure 10 - Overview of ControlNet I/O Distribution

<!-- image -->

Make sure of the following:

- All wiring and cabling are properly connected.
- The communication driver is configured for the programming workstation.

When you configure an I/O module, you define the RPI for the module. The RPI specifies the interval at which data updates over a connection. For example, an input module sends data to a controller at the RPI that you assign to the module. Configure the RPI in milliseconds.

RPI is used only for a module that produces or consumes data. For example, a local ControlNet communication module does not require an RPI because it is not a data -producing member of the system, but only a bridge.

In Logix 5000 controllers, I/O values update at an interval that you configure via the I/O configuration folder of the project. The values update asynchronously to the execution of logic. At the specified interval, the controller updates a value independently from the execution of logic.

When you configure a remote ControlNet communication module or an I/O module, you choose a communication format. The chosen communication format determines the data structure for tags associated with the module. Many I/O modules support different formats. Each format uses a different data structure.

The chosen communication format also determines the following:

- Direct or rack -optimized connection
- Ownership of outputs

| Communication Format with a Remote ControlNet Communication Module   | Criteria for Use                                                                                                                                                                                                                                                                                                                      |
|----------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| None                                                                 | • When all of the remote I/O communicating with a controller via the remote ControlNet communication module use a Direct Connection communication format •  When the connection is used for scheduled peer interlocking •  When I/O will be mostly direct connections •  When multiple controllers control the outputs in the chassis |
| Rack - optimized                                                     | • When some or all of the remote I/O communicating with a controller via the remote ControlNet communication module use a rack - optimized communication format •  To minimize ControlNet network bandwidth when using large volume of digital I/O •  If only one controller will control the I/O                                     |
| Rack - optimized — Listen only                                       | When some or all of the remote I/O communicating with a controller via the remote ControlNet communication module use a rack - optimized communication format                                                                                                                                                                         |

I/O module type determines the available communication formats.

Table 10 - Communication Format for Module Types

| I/O Module Type   | Desired Connection                                                                                                                                                     | Required Communication Format                                                                                                                                                                                                                                                                                                                                   |
|-------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Digital module    | Rack - optimized connection                                                                                                                                            | Rack - optimized                                                                                                                                                                                                                                                                                                                                                |
|                   | Direct connection or to use specialty features of the module, such as diagnostics, timestamps, or electronic fuses or Connection for listening to data from the module | •  The data your controller needs from the I/O module. For example, if your application uses a 1756 - IA16I module in a remote chassis that must provide timestamped input data, choose the CST Timestamped Input Data communication format. •  A listen - only communication format that matches the data the I/O module is broadcasting to other controllers. |
| Analog module     | Direct connection or to use specialty features of the module, such as diagnostics, timestamps, or electronic fuses or Connection for listening to data from the module | •  The data your controller needs from the I/O module. For example, if your application uses a 1756 - OF6CI module in a remote chassis that must provide floating point output data, choose the Float Data communication format. •  A listen - only communication format that matches the data the I/O module is broadcasting to other controllers.             |

## Direct or Rack -optimized Connections

Logix 5000 controllers use connections to transmit I/O data. These connections can be direct or rack -optimized connections.

| Term              | Definition                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|-------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Direct connection | A direct connection is a real - time, data-transfer link between the controller and an analog or digital I/O module that enables your controller to collect more data from an I/O module. For example, with a direct connection, the controller can collect diagnostic status data from a 1756 - IA8D module that would not be collected in a rack - optimized connection. The controller maintains and monitors the connection with the I/O module. Any break in the connection, such as a module fault or the removal of a module while under power, sets fault bits in the data area associated with the module. |

<!-- image -->

## Direct Connections for I/O Modules

In this example, assume that each distributed I/O module is configured for a direct connection to the controller.

## Rack-optimized Connections for I/O Modules

<!-- image -->

The table below calculates the connections in this example.

Table 11 - Connection Calculations

| System Connections                                  | Amount    |
|-----------------------------------------------------|-----------|
| Controller to local ControlNet communication module | 0         |
| Controller to ControlNet adapter(1)                 | 0         |
| Direct connection for digital I/O modules           | 5 digital |
| Direct connection for analog I/O modules            | 2 analog  |
| Total connections used                              | 7         |

<!-- image -->

Tip: Direct connections to many modules may not be feasible because the module supports a finite number of connections, and direct connections may require more resources than the module has available. In this case, use rack-optimized connections. Refer to Rack -optimized Connections for I/O Modules on page 60 on page 57 for more information on how to limit connection use and network traffic.

In this example, assume that each digital I/O module is configured for a rack -optimized connection to the controller. Analog modules must be configured for direct connections.

<!-- image -->

This table calculates the connections in this example.

Table 12 - Connection Calculations

| System Connections                                  |   Amount |
|-----------------------------------------------------|----------|
| Controller to local ControlNet communication module |        0 |

## Ownership

| System Connections                                                                                   |   Amount |
|------------------------------------------------------------------------------------------------------|----------|
| Controller to ControlNet adapters with digital modules (rack - optimized connection to each adapter) |        2 |
| Controller to ControlNet adapter with analog modules (direct connection for each analog I/O module)  |        2 |
| Total connections used                                                                               |        4 |

The rack -optimized connection limits connections, but can also limit the status and diagnostic information that is available from the digital I/O modules.

To increase the number of available connections, use a rack-optimized connection to any remote adapter with multiple digital I/O modules that permit rack-optimized connections, instead of direct connections to those I/O modules.

In a Logix 5000 system, modules multicast data. This means that multiple controllers can receive the same data at the same time from a single module. When you choose a communication format, you have to choose whether to establish an owner or listen -only relationship with the module.

<!-- image -->

<!-- image -->

## Choose the Type of

Table 13 - Module Ownership

| Module Type  ship for  Controller  dule Module Type Controll Ownership for a Module               | Module Type  ship for  Controller  dule Module Type Controll Ownership for a Module                         | Desired Function                                                                            | Required Connection Type                                                                 |
|---------------|-------------------------|---------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------|
| Input module  | Does not own the module | --------------------------------- >                                                         | Owner, such as not listen-only                                                           |
|               | Owns the module         | Maintain communication with the module if it loses communication with the other controller. | Owner, such as not listen-only Use the same configuration as the other owner controller. |
|               |                         | Stop communication with the module if it loses communication with the other controller.     | Listen - only                                                                            |
| Output module | Does not own the module | --------------------------------- >                                                         | Owner, such as not listen-only                                                           |
|               | Owns the module         | --------------------------------- >                                                         | Listen - only                                                                            |

Controlling input modules differs from controlling output modules.

Table 14 - Module Ownership Control

| Module Type    | Ownership     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|----------------|---------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Input modules  | Owner         | The controller that establishes an owner connection to an input module configures that module. This configuring controller is the first controller to establish an owner connection. Once a controller owns and configures an input module, other controllers can establish owner connections to that module. This lets additional owners continue to receive multicasted data if the original owner - controller’s connection to the module breaks. All other additional owners must have the identical configuration data and communication format as the original owner controller, or the connection attempt is rejected. |
|                | Listen - only | Once a controller owns and configures an input module, other controllers can establish a listen - only connection to that module. These controllers can receive multicast data while another controller owns the module. If all owner controllers break their connections to the input module, controllers with listen - only connections no longer receive multicast data.                                                                                                                                                                                                                                                   |
| Output modules | Owner         | The controller that establishes an owner connection to an output module configures that module. Only one owner connection is allowed for an output module. If another controller attempts to establish an owner connection, the connection attempt is rejected.                                                                                                                                                                                                                                                                                                                                                               |
|                | Listen - only | Once a controller owns and configures an output module, other controllers can establish listen - only connections to that module. These controllers can receive multicast data while another controller owns the module. If the owner controller breaks its connection to the output module, all controllers with listen - only connections no longer receive multicast data.                                                                                                                                                                                                                                                 |

## Add a Remote Adapter

The type of distributed I/O determines your choice of a remote ControlNet adapter. Before choosing a remote adapter, you must add local and remote ControlNet modules to a Logix Designer project. For more information on

## Add Distributed I/O

adding ControlNet modules to a project, see Add and Configure a Local ControlNet Module on page 30 on page 27 7 and Add and Configure a Remote ControlNet Module on page 33 on page 31 .

## Table 15 Remote Adapter Options

| Type of Distributed I/O   | Required Remote Adapter                     | Configuration Method       |
|---------------------------|---------------------------------------------|----------------------------|
| 1756 ControlLogix I/O     | 1756 - CN2, 1756-CN2R 1756 - CNB, 1756-CNBR | Logix Designer application |
| 1768 CompactLogix I/O     | 1768 - CNB, 1768-CNBR                       | Logix Designer application |
| 1794 FLEX I/O             | 1794 - ACN15, 1794-ACNR15                   | Logix Designer application |
| 1797 FLEX Ex I/O          | 1797 - ANCR                                 | Logix Designer application |
| 1734 POINT I/O            | 1734 - ACNR                                 | Logix Designer application |
| 1738 - ArmorPOINT         | 1738 - ACNR                                 | Logix Designer application |

To communicate with I/O modules in your system, you add a bridge, adapter, and I/O modules to the I/O Configuration folder of the controller. Within the folder, you organize modules into a hierarchy of tree/branch and parent/child.

<!-- image -->

To add distributed I/O to your Logix Designer project, perform this procedure.

1. Add the local and remote ControlNet communication modules. For more information, refer to Add and Configure a Local ControlNet Module on page 30 on page 27 7 and Add and Configure a Remote ControlNet Module on page 33 on page 31 .

## Distributed I/O Communication Formats

2. In Logix Designer application, right-click your remote ControlNet communication module and choose New Module .
3. From the Module Properties dialog box, configure the distributed I/O module.

<!-- image -->

IMPORTANT This procedure shows the Module Properties dialog box for a 1794-IB16XOB16P/A digital combo module. However, various dialogs appear during configuration depending on the type of distributed I/O. For help configuring a module, refer to the online help in Logix Designer application.

<!-- image -->

Your selection of communication format when you add distributed I/O modules is based on whether you want rack-optimized or direct connections to each distributed I/O module and corresponds directly with the communication format you chose for your remote adapter.

| Remote Adapter Communication Format   | Distributed I/O Communication Format      |
|---------------------------------------|-------------------------------------------|
| Rack Optimization                     | Rack Optimization                         |
| None                                  | An appropriate direct - connection format |

## Access Distributed I/O

I/O information is presented as a structure of multiple fields dependent on the specific features of the I/O module. The name of the structure is based on the location of the I/O module in the system. Each I/O tag is automatically created when you configure the I/O module in Logix Designer software. Each tag name follows this format:

Location:SlotNumber:Type.MemberName.SubMemberName.Bit

| Address Variable   | Definition                                                                                                                                                                                                                                        |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Location           | Identifies the network location by using one of these values: •  LOCAL — Local DIN rail or chassis •  ADAPTER_NAME — Remote adapter or bridge that you specify                                                                                    |
| SlotNumber         | Slot number of I/O module location in its chassis.                                                                                                                                                                                                |
| Type               | Identifies one of these types of data: •  I — Input •  O — Output •  C — Configuration •  S — Status                                                                                                                                              |
| MemberName         | Specific data from the I/O module depending on the type of data the module can store. For example, Data and Fault are possible fields of data for an I/O module. Data is the common name for values that are sent to or received from I/O points. |
| SubMemberName      | Specific data related to a MemberName.                                                                                                                                                                                                            |
| Bit (optional)     | Specific point on the I/O module depending on the size of the I/O module (0...31 for a 32 - point module).                                                                                                                                        |

I/O information is available in the Controller Tags portion of your Logix Designer project. You can monitor or edit the tags.

To access distributed I/O, within the Controller Organizer of Logix Designer application, double-click Controller Tags .

<!-- image -->

## The Controller Tags dialog box appears.

<!-- image -->

This example contains a tag named

Remote\_FLEX\_CNET\_adapter:1:C.Filter\_0.

<!-- image -->

| Address Variable   | Definition               |
|--------------------|--------------------------|
| Location           | Remote_FLEX_CNET_adapter |
| SlotNumber         | 1                        |
| Type               | Configuration            |
| MemberName         | Filter_0                 |

This example shows an I/O tree configured with a remote FLEX X I/O adapter and two remote FLEX I/O modules.

<!-- image -->

Table 16 Example Tag Names 1

|   Example | Example Tag   | Module                                                                  | Example Tag Names Created by Logix Designer Software                                                |
|-----------|---------------|-------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
|         1 | Example 1     | Remote 1794 - ACN15 adapter FLEX_adapter                                | FLEX_adapter:I FLEX_adapter:I.SlotStatusBits FLEX_adapter:I.Data FLEX_adapter:O FLEX_adapter:O.Data |
|         2 | Example 2     | Remote 1794 - IA16 Input_module in slot 1 rack - optimized connection   | FLEX_adapter:1:C FLEX_adapter:1:C.Config FLEX_adapter:1:C.DelayTime_0 FLEX_adapter:1:I              |
|         3 | Example 3     | Remote 1794 - OB16D Output_module in slot 2 rack - optimized connection | FLEX_adapter:2:C FLEX_adapter:2:C.SSData FLEX_adapter:2:O FLEX_adapter:2:O                          |

## Validate Connections

You need to verify that the controller can communicate with the devices that you have just configured.

To validate connections, perform this procedure.

1. Determine if communication has been established with the devices.

| If a warning symbol                               | Then                                                                      |
|---------------------------------------------------|---------------------------------------------------------------------------|
| Appears over the I/O Configuration folder         | The controller cannot communicate with the device. Go to step .           |
| Does not appear over the I/O Configuration folder | The controller can communicate with the device and connections are valid. |

2. Identify any faults in communication modules by working down through the I/O configuration tree.

<!-- image -->

In this example, faults occurred at the remote 1756-CN2/A module and the I/O modules added below it.

3. Identify the fault codes, specifically the fault at the module that is highest in the I/O tree.
4. Right-click the module and choose Properties .

<!-- image -->

5. From the Module Properties dialog box, click the Connection tab.
6. Identify the fault in the Module Fault area.
7. To interpret the fault codes, return to the Logix Designer application and from the Help menu, choose Contents .
8. In the Search box, type module fault .
9. In the list of search results, click range for the module fault codes you just identified.
10. F Follow the recommendations for your fault code.

<!-- image -->

<!-- image -->

## Terminology

## Produce and Consume Tags (interlock controllers)

This chapter explains how to interlock (produce and consume tags) controllers via a ControlNet network.

| Topic                                                           | Page          |
|-----------------------------------------------------------------|---------------|
| Terminology on page 67                                          | 71 on page 67 |
| Set Up the Hardware on page 85                                  | 72 on page 85 |
| Determine Connections for Produced and Consumed Tags on page 68 | 73 on page 68 |
| Organize Tags for Produced or Consumed Data on page 70          | 75 on page 70 |
| Adjust for Bandwidth Limitations on page 70                     | 76 on page 70 |
| Produce a Tag on page 71                                        | 77 on page 71 |
| Consume a Tag on page 74                                        | 79 on page 74 |

Interlocking controllers is the preferred method of sharing scheduled data between controllers when data needs to be delivered regularly, quickly and at a set interval.

A Logix 5000 controller lets you produce (broadcast) and consume (receive) system -shared tags.

| Term         | Definition                                                                                                                                                                                                                                                                                                     |
|--------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Produced tag | A tag that a controller makes available for use by other controllers. Multiple controllers can simultaneously consume (receive) the data. A produced tag sends its data to one or more consumed tags (consumers) without using logic. The produced tag sends its data at the RPI of the fastest consuming tag. |
| Consumed tag | A tag that receives a produced tag’s data. The data type of the consumed tag must match the data type, including any array dimensions, of the produced tag. The RPI of the fastest consumed tag determines the rate at which the produced tag is produced.                                                     |

For two controllers to share produced or consumed tags, they must reside on the same ControlNet network.

## Set Up the Hardware

In this example, the controller in the first chassis produces a tag that is consumed by the controller in the second chassis.

## Item

<!-- image -->

## Determine Connections for Produced and Consumed Tags

<!-- image -->

## Description

Chassis 1 can contain any of these combinations:

- 1756 ControlLogix controller with a 1756 -CN2 or 1756 -CN2R communication module in the chassis.
- 1756 ControlLogix controller with a 1756 -CNB or 1756 -CNBR communication module in the chassis.
- 1768 -L43 CompactLogix controller with a 1768 -CNB or 1768 -CNBR communication module in the chassis.
- 1769 -L32C or 1769 -L35CR CompactLogix controller.
- 1789 SoftLogix controller with a 1784 -PCICS communication card.
- PowerFlex 700S with DriveLogix controller and a 1788 -CNx ControlNet communication card.
- Non -Logix 5000 controller or other device connected to ControlNet via a ControlNet scanner card.
- Chassis 2 can contain any of these combinations: 2
- 1756 ControlLogix controller with a 1756 -CN2 or 1756 -CN2R communication module in the chassis.
- 1756 ControlLogix controller with a 1756 -CNB or 1756 -CNBR communication module in the chassis.
- 1768 -L43 CompactLogix controller with a 1768 -CNB or 1768 -CNBR communication module in the chassis.
- 1769 -L32C or 1769 -L35CR CompactLogix controller.
- 1789 SoftLogix controller with a 1784 -PCICS communication card.
- PowerFlex 700S with DriveLogix controller and a 1788 -CNx ControlNet communication card.
- Non -Logix 5000 controller or other device connected to ControlNet via a ControlNet scanner card.
- Programming terminal 3

## Make sure of the following:

- The ControlNet communication modules are connected to a scheduled ControlNet network.
- All wiring and cabling are properly connected.
- The communication driver is configured for the programming workstation.

## Tip:

If you are sharing tags only between ControlLogix controllers, the controllers are not controlling any I/O modules. You can set the communication format of the 1756 -CN2, 1756-CN2R, 1756-CNB, or 1756 -CNBR modules in the remote chassis to None. This limits connection usage and network traffic.

Logix controllers can produce (broadcast) and consume (receive) system -shared tags that are sent and received via the ControlNet communication module. Each produced and consumed tag requires

## connections.

Table 17 - Tag Type and Connections

| Tag Type   | Required Connections                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Produced   | The produced tag requires two connections. The producing controller must have one connection for the produced tag and the first consumer and one connection for each additional consumer (heartbeat). The heartbeat is a small scheduled packet the consumer sends to indicate that it is getting the produced data. As you increase the number of controllers that can consume a produced tag, you also reduce the number of available controller connections for other operations, such as communication and I/O. |
| Consumed   | Each consumed tag requires one connection for the controller that is consuming the tag.                                                                                                                                                                                                                                                                                                                                                                                                                             |

All ControlNet modules support at least 32 connections. The number of available connections limits the number of tags that can be produced or consumed. If the communication module uses all of its connections for I/O and other communication modules, no connections are left for produced and consumed tags.

Table 18 - Produced and Consumed Tags and Number of Connections

| Controller                                                                                               | Available Connections                                                                                                                        | Connections Used by a Produced Tag   | Connections Used by a Consumed Tag   |
|----------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------|--------------------------------------|
| CompactLogix PowerFlex 700S with DriveLogix software                                                     | 100                                                                                                                                          | Number of consumers + 1              | 1                                    |
| ControlLogix SoftLogix5800                                                                               | 250                                                                                                                                          | Number of consumers + 1              | 1                                    |
| Communication Card                                                                                       | Available Connections                                                                                                                        | Connections Used by a Produced Tag   | Connections Used by a Consumed Tag   |
| ControlNet port on the CompactLogix controller                                                           | 32                                                                                                                                           | Number of consumers                  | 1                                    |
| 1768 - CNB and 1768 - CNBR CompactLogix ControlNet modules                                               | 48                                                                                                                                           | Number of consumers                  |                                      |
| 1788 - CNx card in PowerFlex 700S with DriveLogix controller                                             | 32 total ControlNet connections, 22 of which can be scheduled and used for producing and consuming tags.                                     | Number of consumers                  |                                      |
| 1756 - CN2 and 1756 - CN2R series B ControlNet modules in the local chassis of a ControlLogix controller | 131 Note that 3 of the 131 connections are always reserved for redundant control. Therefore, 128 connections are available for standard use. | Number of consumers                  |                                      |
| 1756 - CNB and 1756 - CNBR ControlNet modules in the local chassis of a ControlLogix controller          | 64 We recommend that you do not use more than 40…48 scheduled connections.                                                                   | Number of consumers                  |                                      |
| 1784 - PCICS card in a SoftLogix5800 controller                                                          | 127                                                                                                                                          | Number of consumers                  |                                      |

## Organize Tags for Produced or Consumed Data

Follow these guidelines as you organize your tags for produced or consumed data (shared data).

Table 19 - Guidelines for Produced or Consumed Data Tags

| Function                                                                                  | Guidelines                                                                                                                                                                                                                                 | Guidelines                                                                                                                                                                                                                                 | Guidelines                                                                                                                                                                                                                                 | Guidelines                                                                                                                                                                                                                                 |
|-------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Create the tags at the controller scope.                                                  | You can produce and consume only controller - scoped tags.                                                                                                                                                                                 | You can produce and consume only controller - scoped tags.                                                                                                                                                                                 | You can produce and consume only controller - scoped tags.                                                                                                                                                                                 | You can produce and consume only controller - scoped tags.                                                                                                                                                                                 |
| Produce and consume specific tags.                                                        | You cannot produce or consume these types: •  Alias •  Axis type •  BOOL •  Consumed •  I/O •  INT Message                                                                                                                                 | You cannot produce or consume these types: •  Alias •  Axis type •  BOOL •  Consumed •  I/O •  INT Message                                                                                                                                 | You cannot produce or consume these types: •  Alias •  Axis type •  BOOL •  Consumed •  I/O •  INT Message                                                                                                                                 | You cannot produce or consume these types: •  Alias •  Axis type •  BOOL •  Consumed •  I/O •  INT Message                                                                                                                                 |
| Use one of these data types: •  DINT •  REAL •  Array of DINTs or REALs •  User - defined | To share other data types, create a user-defined data type that contains the required data. Use the same data type for the produced tag and corresponding consumed tag or tags.                                                            | To share other data types, create a user-defined data type that contains the required data. Use the same data type for the produced tag and corresponding consumed tag or tags.                                                            | To share other data types, create a user-defined data type that contains the required data. Use the same data type for the produced tag and corresponding consumed tag or tags.                                                            | To share other data types, create a user-defined data type that contains the required data. Use the same data type for the produced tag and corresponding consumed tag or tags.                                                            |
| Limit the size of the tag to ≤ 480 bytes.                                                 | If you must transfer more than 480 bytes, create logic to transfer the data in smaller packets or create multiple produce/consume tags.                                                                                                    | If you must transfer more than 480 bytes, create logic to transfer the data in smaller packets or create multiple produce/consume tags.                                                                                                    | If you must transfer more than 480 bytes, create logic to transfer the data in smaller packets or create multiple produce/consume tags.                                                                                                    | If you must transfer more than 480 bytes, create logic to transfer the data in smaller packets or create multiple produce/consume tags.                                                                                                    |
| To share tags with a PLC - 5C controller, use a user - defined data type.                 | To                                                                                                                                                                                                                                         | This                                                                                                                                                                                                                                       | Then                                                                                                                                                                                                                                       | Then                                                                                                                                                                                                                                       |
| To share tags with a PLC - 5C controller, use a user - defined data type.                 | Produce                                                                                                                                                                                                                                    | Integers, BOOLs or combinations of both                                                                                                                                                                                                    | Create a user - defined data type that contains an array of INTs with an even number of elements, such as INT[2].                                                                                                                          | Create a user - defined data type that contains an array of INTs with an even number of elements, such as INT[2].                                                                                                                          |
| To share tags with a PLC - 5C controller, use a user - defined data type.                 | Produce                                                                                                                                                                                                                                    | Only one REAL value                                                                                                                                                                                                                        | Use the REAL data type.                                                                                                                                                                                                                    | Use the REAL data type.                                                                                                                                                                                                                    |
| To share tags with a PLC - 5C controller, use a user - defined data type.                 | Produce                                                                                                                                                                                                                                    | More than one REAL value                                                                                                                                                                                                                   | Create a user - defined data type that contains an array of REALs.                                                                                                                                                                         | Create a user - defined data type that contains an array of REALs.                                                                                                                                                                         |
| To share tags with a PLC - 5C controller, use a user - defined data type.                 |                                                                                                                                                                                                                                            |                                                                                                                                                                                                                                            | Create a user - defined data type that contains these members:                                                                                                                                                                             | Create a user - defined data type that contains these members:                                                                                                                                                                             |
| To share tags with a PLC - 5C controller, use a user - defined data type.                 |                                                                                                                                                                                                                                            |                                                                                                                                                                                                                                            | Data type                                                                                                                                                                                                                                  | Description                                                                                                                                                                                                                                |
| To share tags with a PLC - 5C controller, use a user - defined data type.                 |                                                                                                                                                                                                                                            |                                                                                                                                                                                                                                            | DINT                                                                                                                                                                                                                                       | Status BIT 0 •  0 PLC5 in PROG mode •  1 PLC5 in RUN mode                                                                                                                                                                                  |
| To share tags with a PLC - 5C controller, use a user - defined data type.                 |                                                                                                                                                                                                                                            |                                                                                                                                                                                                                                            | INT[x], where x is the output size of the data from the PLC - 5C controller. If you are consuming only one INT, omit x. x.                                                                                                                 | Data produced by a PLC - 5C controller                                                                                                                                                                                                     |
| Use the highest permissible RPI for your application.                                     | If the controller consumes the tag over a ControlNet network, use a binary multiple of the ControlNet network update time                                                                                                                  | (NUT). For example, if the NUT is 5 ms, use an RPI of 5, 10, 20, or 40 ms.                                                                                                                                                                 | If the controller consumes the tag over a ControlNet network, use a binary multiple of the ControlNet network update time                                                                                                                  | If the controller consumes the tag over a ControlNet network, use a binary multiple of the ControlNet network update time                                                                                                                  |
|                                                                                           | Combine data that goes to the same controller. If you are producing several tags for the same controller, group the data in these ways: •  To reduce the number of connections, group the data into one or more user - defined data types. | Combine data that goes to the same controller. If you are producing several tags for the same controller, group the data in these ways: •  To reduce the number of connections, group the data into one or more user - defined data types. | Combine data that goes to the same controller. If you are producing several tags for the same controller, group the data in these ways: •  To reduce the number of connections, group the data into one or more user - defined data types. | Combine data that goes to the same controller. If you are producing several tags for the same controller, group the data in these ways: •  To reduce the number of connections, group the data into one or more user - defined data types. |

## Adjust for Bandwidth Limitations

When you share a tag over a ControlNet network, the tag must fit within the bandwidth of the network:

- As the number of connections over a ControlNet network increases, several connections, including produced or consumed tags, may need to share a network update time (NUT).
- A ControlNet node can transmit approximately 500 bytes of scheduled data in a single NUT.

Depending on system size, your ControlNet network may lack the bandwidth for large tags. If a tag is too large for your ControlNet network, make one or more of these adjustments.

Table 20 - Tag Adjustments

| Adjustment                                                                                                                                                           | Description                                                                                                                                                                                                                                                                                                                                                                            |                                                                                                                                                                                                                                                                                                                                                                                        |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Increase the requested packet interval (RPI) of your connections. This is the recommended method.                                                                    | At higher RPIs, connections can take turns sending data during an update period.                                                                                                                                                                                                                                                                                                       | At higher RPIs, connections can take turns sending data during an update period.                                                                                                                                                                                                                                                                                                       |
| Reduce your network update time (NUT).                                                                                                                               | At a faster NUT, fewer connections have to share an update period.                                                                                                                                                                                                                                                                                                                     | At a faster NUT, fewer connections have to share an update period.                                                                                                                                                                                                                                                                                                                     |
| For a ControlNet 1756 - CN2, 1756-CN2R, 1756-CNB, or 1756 - CNBR bridge module in a remote chassis, choose the most efficient communication format for that chassis. | Are most of the modules in the chassis non-diagnostic, digital I/O modules?                                                                                                                                                                                                                                                                                                            | Then choose this communication format for the remote 1756-CN2 or 1756-CNB module                                                                                                                                                                                                                                                                                                       |
| For a ControlNet 1756 - CN2, 1756-CN2R, 1756-CNB, or 1756 - CNBR bridge module in a remote chassis, choose the most efficient communication format for that chassis. | Yes                                                                                                                                                                                                                                                                                                                                                                                    | Rack optimization                                                                                                                                                                                                                                                                                                                                                                      |
| For a ControlNet 1756 - CN2, 1756-CN2R, 1756-CNB, or 1756 - CNBR bridge module in a remote chassis, choose the most efficient communication format for that chassis. | No                                                                                                                                                                                                                                                                                                                                                                                     | None                                                                                                                                                                                                                                                                                                                                                                                   |
| For a ControlNet 1756 - CN2, 1756-CN2R, 1756-CNB, or 1756 - CNBR bridge module in a remote chassis, choose the most efficient communication format for that chassis. | The rack optimization format uses an additional eight bytes for each slot in its chassis. Analog modules or modules that are sending or receiving diagnostic, fuse, timestamp, or schedule data require direct connections and cannot take advantage of the rack - optimized form. Selecting None frees up the eight bytes per slot for other uses, such as produced or consumed tags. | The rack optimization format uses an additional eight bytes for each slot in its chassis. Analog modules or modules that are sending or receiving diagnostic, fuse, timestamp, or schedule data require direct connections and cannot take advantage of the rack - optimized form. Selecting None frees up the eight bytes per slot for other uses, such as produced or consumed tags. |
| Separate the tag into two or more smaller tags.                                                                                                                      | 1. Group the data according to similar update rates. For example, you could create one tag for data that is critical and another tag for data that is not as critical. 2. Assign a different RPI to each tag.                                                                                                                                                                          | 1. Group the data according to similar update rates. For example, you could create one tag for data that is critical and another tag for data that is not as critical. 2. Assign a different RPI to each tag.                                                                                                                                                                          |
| Create logic to transfer the data in smaller sections (packets).                                                                                                     | For information on how to do this, see the Logix 5000 Controllers Common Procedures Programming Manual, publication 1756 - PM001 .                                                                                                                                                                                                                                                     | For information on how to do this, see the Logix 5000 Controllers Common Procedures Programming Manual, publication 1756 - PM001 .                                                                                                                                                                                                                                                     |

## Produce a Tag

A Logix 5000 controller can produce only controller-scoped, user-created tags in the local controller's tag structure. Logix 5000 controllers cannot produce I/O tags or tags aliased to I/O tags.

## To produce a tag

1. Open the Logix Designer project containing the tag you want to produce.

IMPORTANT

You can create produced tags only when your Logix Designer project is offline.

2. In the Controller Organizer of the Logix Designer application, right-click Controller Tags and choose Edit Tags .
3. From the Controller Tags dialog box, type the name of the new tag in an available Tag Name field.
4. Right-click the new tag name and choose Edit Tag Properties .

<!-- image -->

<!-- image -->

<!-- image -->

5. On the Tag Properties dialog box, from the Type menu, choose Produced .
6. In the Data Type field, type a data type that the controller can produce.

<!-- image -->

A controller cannot produce a tag by using MSG or INT data types.

## Consume a Tag

7. Click the Connection tab.
8. In the Max Consumers field, type a number of consumers.

<!-- image -->

If you are unsure of the maximum number of consumers, use a number higher than the actual number of consumers. Unused connections are deducted from the number of available controller connections.

9. Click OK .

IMPORTANT When your controller produces a tag, any device that interfaces with a ControlNet network can consume the tag. However, when a non -Logix controller, such as a personal computer using a 1784 -PKTCS card, consumes the tag produced by a Logix controller, you must perform additional tasks in RSNetWorx for ControlNet software. See this document for more information:

https://rockwellautomation.custhelp.com/app/answers/answer\_view/a\_id/34171

Logix 5000 controllers can consume only controller-scoped user-created tags from another controller's tag structure. The Logix 5000 controllers cannot consume I/O tags or tags aliased to I/O tags.

IMPORTANT You can create consumed tags only when your Logix Designer project is offline.

To consume a tag, perform this procedure.

1. Open the Logix Designer project that contains the controller that you want to consume the produced tag.
2. Make sure the controller producing the tag to be consumed is in the consuming controller's I/O configuration, as shown in this example.

<!-- image -->

- Local ControlNet module in consuming controller's chassis
- Remote ControlNet module
- Producing controller
3. Make sure the communication format for the remote ControlNet module is None.
4. In the Controller Organizer of the Logix Designer application, right-click Controller Tags and choose Edit Tags .
5. From the Controller Tags dialog box, type the name of the new tag in an available Tag Name field.

<!-- image -->

<!-- image -->

6. Right-click the new tag name and choose Edit Properties .
7. From the Tag Properties dialog box, complete these fields:
- From the Type pull-down menu, choose Consumed .
- In the Data Type field, type a data type that the controller can produce. A controller cannot produce a tag by using the MSG or INT data types.

<!-- image -->

<!-- image -->

8. Click Connection .
9. From the Consumed Tag Connection dialog box, complete these fields:
- From the Producer pull-down menu, choose Producing\_controller. This menu contains all possible paths to previously configured controllers in the I/O tree.
- In the Remote Data a field, type the name of the produced tag in the producing controller.
- In the RPI field, enter the rate at which the tag will be produced.
10. C Click OK .
11. Use RSNetWorx for ControlNet software to schedule the network.

<!-- image -->

## Set Up the Hardware

<!-- image -->

<!-- image -->

## Messaging

This chapter explains how to use MSG instructions to send data to and receive data from other modules on a ControlNet network.

<!-- image -->

| Topic                                         | Page          |
|-----------------------------------------------|---------------|
| Set Up the Hardware on page 85                | 84 on page 85 |
| Guidelines for MSG Instructions on page 80    | 85 on page 80 |
| Determine Connections for Messages on page 81 | 86 on page 81 |
| Enter Message Logic on page 81                | 86 on page 81 |
| Configure a Message Instruction on page 82    | 88 on page 82 |
| Stagger the Messages on page 84               | 90 on page 84 |

Use peer -to-peer messaging when these conditions apply:

- Data is sent when a specific condition occurs in your application.
- Data is sent at a slower rate than is required by produced and consumed tags.
- Data is sent to devices that communicate only with unscheduled data.

In this example, the controller in the local chassis uses a MSG instruction to send a message to another module, which can be a controller, on the ControlNet network.

<!-- image -->

|   Item | Description                                                                                                                                                                                                                                                     |
|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|      1 | Remote chassis with any of these configurations: •  PLCs, SLC, or Logix 5000 controllers on a ControlNet or other network •  I/O modules, such as ControlLogix analog module configuration data on a ControlNet or other network •  1771 block transfer modules |
|      2 | Programming terminal                                                                                                                                                                                                                                            |

| Item   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|--------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|        | Local chassis with any of these combinations: •  1756 ControlLogix controller with a 1756 - CN2 or 1756 - CN2R communication module in the chassis •  1756 ControlLogix controller with a 1756 - CNB or 1756 - CNBR communication module in the chassis •  1768 - L43 CompactLogix controller with a 1768 - CNB or 1768 - CNBR communication module in the chassis •  1769 - L32C or 1769 - L35CR CompactLogix controller •  1789 SoftLogix controller with a 1784 - PCICS communication card •  PowerFlex 700S with DriveLogix controller and a 1788 - CNx ControlNet communication card •  Non - Logix 5000 controller or other device connected to ControlNet via a ControlNet scanner card |

| IMPORTANT   | The 1769 - L32C and 1769 - L35CR controllers can produce and consume tags over a ControlNet network to other Logix 5000 controllers. However, Compact I/O modules that are local to the 1769 - L32C and 1769 - L35CR controllers are not accessible to other Logix 5000 controllers.   |
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

## Make sure of the following:

- The ControlNet modules are connected to a ControlNet network.
- All wiring and cabling are properly connected.
- The communication driver is configured for the programming workstation.

Follow these guidelines as you work with message instructions.

Table 21 - Guidelines for MSG Instructions

## Guidelines for MSG Instructions

| Function                                                                                                                  | Guidelines                                                                                                                                                                                                                                                                                                                                                                                 |
|---------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| For each MSG instruction, create a control tag.                                                                           | Each MSG instruction requires its own control tag. This tag contains control elements for messages, such as DN and EN, error codes, and information to execute the message, such as destination path and number of words to transfer: •  Data type = MESSAGE •  Scope = controller •  The tag cannot be part of an array or a user - defined data type                                     |
| Keep the source or destination data at the controller scope.                                                              | A MSG instruction can access only tags that are in the Controller Tags folder (controller scope).                                                                                                                                                                                                                                                                                          |
| If your MSG is to a module that uses 16 - bit integers, use a buffer of INTs in the MSG and DINTs throughout the project. | If your message is to a module that uses 16 - bit integers, such as an SLC 500 controller, and it transfers integers, not REALs, use a buffer of INTs in the message and DINTs throughout the project. This increases the efficiency of your project because Logix 5000 controllers execute more efficiently and use less memory when working with 32 - bit integers (DINTs).              |
| If you want to enable more than 16 MSGs at one time, use some type of management strategy.                                | If you enable more than 16 MSGs at one time, some MSG instructions may experience delays in entering the queue. To guarantee the execution of each message, you can take these actions: •  Enable each message in sequence. •  Enable the messages in smaller groups. •  Program a message to communicate with multiple modules. •  Program logic to coordinate the execution of messages. |
| Cache connected MSGs that execute most frequently.                                                                        | Cache the connection for those MSG instructions that execute most frequently, up to the maximum number permissible for your controller revision. This optimizes execution time because the controller does not have to open a connection each time the message executes.                                                                                                                   |
| Limit the number of unconnected and uncached MSGs to fewer than the number of unconnected buffers.                        | The controller can have 10...40 unconnected outgoing buffers: •  The default number is 10. •  If all the unconnected buffers are in use when an instruction leaves the message queue, the instruction errors and does not transfer the data. •  You can increase the number of unconnected buffers to a maximum of 40.                                                                     |

## Determine Connections for Messages

## Guidelines for Caching Message Connections

For more information on programming MSG instructions, see the Logix 5000 Controllers General Instructions Reference Manual, publication 1756-RM003 . The individual system user manuals for Logix 5000 controllers also provide MSG examples unique to specific controller platforms.

Messages transfer data to other modules, such as other controllers, I/O modules or operator interfaces. Each message uses one connection, regardless of how many modules are in the message path. To conserve connections, you can configure one message to read from or write to multiple modules. Also, you can configure multiple messages for the same path and use only one connection if only one message is active at a time; however, this requires that you write your ladder logic correctly to make sure that only one message is active at any time.

These connected messages can leave the connection open (cache) or close the connection when the message has finished transmitting.

Table 22 - Message Connections and Communication Methods

| Message Type                   | Communication Method   | Connection Required   |
|--------------------------------|------------------------|-----------------------|
| CIP data table read or write   | CIP                    | Yes                   |
| CIP generic                    | CIP                    | Optional(1)           |
| Block - transfer read or write | Not applicable         | Yes                   |

Follow these guidelines to determine whether to cache a connection.

| Message Execution   | Appropriate Action                                                                                                                                                              |
|---------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Repeated            | Cache the connection. This keeps the connection open and optimizes message completion time. Opening a connection during the execution of each message increases execution time. |
| Infrequent          | Do not cache the connection. This closes the connection upon completion of the message, freeing up that connection for other uses.                                              |

## Enter Message Logic

To send or receive data from a ControlNet module via a message, you must program a MSG instruction in the local controller's logic. If the target module is configured in the I/O Configuration folder of the controller, browse to choose the module or manually type the message path in the MSG instruction.

## Add the ControlNet Modules and Remote Devices to the Local Controller's I/O Configuration

Browse to choose the target device of a MSG instruction and add that remote device to the I/O configuration folder of the local controller. Within the I/O configuration folder, organize the local and remote devices into a hierarchy of tree/branch and parent/child.

## Enter a Message

## Configure a Message Instruction

## Example:

| Item                                                  |   Description |
|-------------------------------------------------------|---------------|
| Local controller and communication module             |             1 |
| Remote controller and communication modules           |             2 |
| Local communication module for the local controller   |             3 |
| Remote communication module for the remote controller |             4 |
| Remote controller                                     |             5 |

<!-- image -->

For more information on how to add ControlNet modules and remote devices to the local controller's I/O configuration, see Chapter 4 4.

Use relay ladder logic to enter a MSG instruction. Click to configure the MSG instruction, as shown in the example below.

Enter an MSG instruction as shown below.

ATTENTION: If user\_bit and count\_messages.EN = 0 (MSG instruction is not already enabled), then execute an MSG instruction that sends data to another controller.

<!-- image -->

<!-- image -->

Tip: We recommend an XIO of the MSG control block tag.en, such as the count\_messages.EN portion of this -

- rung, as an in series precondition for all message instructions.

Do not manipulate the control bits of a message instruction.

To configure a MSG instruction, perform this procedure.

1. Click in the MSG box.

<!-- image -->

2. From the Message Type pull-down menu, choose a message type.
3. In the Source Element field, type the appropriate information.
4. In the Number of Elements field, enter the number of elements.
5. From the Destination Element pull-down menu, choose the instruction's destination element.

The message instruction's destination determines how the message is configured.

| Function                | Configuration Box   | Required Information                                                                   |
|-------------------------|---------------------|----------------------------------------------------------------------------------------|
| Read (receive) the data | Message Type        | CIP Data Table Read                                                                    |
|                         | Source Element      | First element of the tag that contains data in the other controller                    |
|                         | Number of Elements  | Number of elements to transfer                                                         |
|                         | Destination Tag     | First element of the controller - scoped tag in this controller for the data           |
| Write (send) the data   | Message Type        | CIP Data Table Write                                                                   |
|                         | Source Tag          | First element of the controller - scoped tag in this controller that contains the data |
|                         | Number of Elements  | Number of elements to transfer                                                         |
|                         | Destination Element | First element of the tag for the data in the other controller                          |

## Stagger the Messages

6. Click the Communication tab.
7. Specify the path of the module for which you sent the message instruction to the I/O configuration tree:
- If the module has been added, click Browse to the choose the path.
- If the module has not been added, type the path in the Path field.

<!-- image -->

## 8. Click OK .

As you add messages to your project, you may have to coordinate the execution of the messages. To avoid errors and assure that each message is processed, follow these rules.

<!-- image -->

| Rule 1   | Enable no more than 16 messages at one time, including block transfers.                                                                                                                                                                |
|----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Rule 2   | Enable no more than 10 of these types of messages at one time: •  CIP data table reads or writes that are not cached •  CIP generic •  PLC - 2, PLC-3, PLC-5, or SLC (all types) •  Block transfer reads or writes that are not cached |

If the number of messages in your application exceeds rules 1 and 2, then stagger the execution of your messages. Here are some options:

- Send each message in sequence.
- Send the messages in groups that are within the limits of rules 1 and 2.
- Program a message to communicate with multiple devices.

## Set Up the Hardware

## Communicate with PanelView Terminals

This chapter explains how a controller uses a ControlNet communication module to communicate with PanelView software products over a ControlNet network.

| Topic                                                        | Page          |
|--------------------------------------------------------------|---------------|
| Set Up the Hardware on page 85                               | 92 on page 85 |
| Determine Connections to PanelView Terminals on page 86      | 93 on page 86 |
| Add a PanelView Terminal on page 86                          | 94 on page 86 |
| Organize Controller Data for a PanelView Terminal on page 90 | 96 on page 90 |

In this example, the controller in the local chassis shares data with an HMI application on a ControlNet network. This application could be running any of these:

- PanelView terminal
- PanelView Plus terminal
- Workstation running RSView 32 software
- Workstation running an RSView Enterprise application, such as RSView Machine Edition software or RSView Supervisory Edition software

<!-- image -->

Figure 14 - Example of Communication with PanelView and RSView Products

|   Item | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|--------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|      1 | Local controller in any of these combinations: •  1756 ControlLogix controller with a 1756 - CN2 or 1756 - CN2R communication module in the chassis •  1756 ControlLogix controller with a 1756 - CNB or 1756 - CNBR communication module in the chassis •  1768 - L43 CompactLogix controller with a 1768 - CNB or 1768 - CNBR communication module in the chassis •  1769 - L32C or 1769 - L35CR CompactLogix controller •  1789 SoftLogix controller with a 1784 - PCICS communication card •  PowerFlex 700S with DriveLogix controller and a 1788 - CNx ControlNet communication card |
|      2 | HMI terminal                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |

## Determine Connections to PanelView Terminals

## Add a PanelView Terminal

Make sure of the following:

- The ControlNet communication modules are connected to a scheduled ControlNet network.
- All wiring and cabling are properly connected.

How you establish communication between a PanelView or PanelView Plus terminal and a Logix 5000 controller over a ControlNet network depends on how you want to use controller connections.

| Communication Type           | PanelView Standard   | PanelView Plus                      |
|------------------------------|----------------------|-------------------------------------|
| Scheduled (always connected) | Supported            | Supported in revision 3.2 and later |
| Unscheduled (connected)      | Not supported        | Supported                           |
| Unscheduled (unconnected)    | Supported            | Not supported                       |

A Logix controller supports up to 40 outgoing and 3 incoming unconnected buffers. This limited number of incoming unconnected buffers limits how many PanelView Standard terminals can request data from a controller.

When you use PanelView terminals with Logix 5000 controllers over a ControlNet network, remember these limitations:

- A maximum of four PanelView Standard terminals can request data from a Logix 5000 controller.
- The number of PanelView Plus terminals that can request data from a Logix 5000 controller is dependent on the number of available unconnected buffers in the Logix 5000 controller.

A typical PanelView Plus application uses 5 unconnected buffers in a Logix 5000 controller. With 32 unconnected buffers available at any time in a Logix 5000 controller, a maximum of 6 PanelView Plus terminals can request data from a Logix 5000 controller. Keep in mind, however, that if 6 PanelView Plus terminals are requesting data from a single Logix 5000 controller, few unconnected buffers remain for anything else.

For scheduled connected communication, you must add the PanelView or PanelView Plus terminal to the I/O configuration tree for the controller project.

Follow these steps to add a PanelView terminal.

## To add a PanelView terminal

1. If your application is online, go offline.

2. In the Logix Designer application, right-click the Backplane and choose New Module .
3. From the Select Module dialog box, select a local ControlNet communication module type and click OK .

<!-- image -->

<!-- image -->

SoftLogix

PCIC (unscheduled data only) or 1784

PCICS (unscheduled data only)

4. From Module Properties dialog box, configure the local ControlNet module.

For information on configuring local ControlNet communication modules, refer to Configure a ControlNet Module on page 29 on page

<!-- image -->

<!-- image -->

5. Right-click the local communication module and choose New Module .

<!-- image -->

6. From the Select Module dialog box, select the PanelView terminal and click OK .
7. From the Module Properties dialog box, configure the terminal. For information on configuring local ControlNet communication modules, refer to Configure a ControlNet Module on page 29 on page
3. 27 .

<!-- image -->

<!-- image -->

## Organize Controller Data for a PanelView Terminal

Organize data for a PanelView or PanelView Plus terminal based on how the data is used.

| Data Type                                                   | Required Actions                                                                                                                                                                                                                                                                                                                                                                                                                          |
|-------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Time - critical scheduled data (PanelView terminals only)   | Use the I/O tags of the terminal. The terminal supports a maximum of 32 input tags and 32 output tags. The tags for this data were created when you added the PanelView terminal to the I/O configuration of the controller. They are similar to the tags of I/O modules.                                                                                                                                                                 |
| Not time - critical (PanelView or PanelView Plus terminals) | Create arrays to store the data. 1. For each screen, create a BOOL array with enough elements for the bit - level objects on the screen. For example, the BOOL[32] array gives you 32 bits for push buttons and indicators. 2. For each screen, create a DINT array with enough elements for the word - level objects on the screen. For example, the DINT[28] array gives you 28 values for numeric entry controls and numeric displays. |

To access the scheduled I/O tags of the PanelView terminal, use these address formats.

| Terminal Function   | Address Definition           |
|---------------------|------------------------------|
| Writes the data     | name_of_terminal:I.Data[x].y |
| Reads the data      | name_of_terminal:O.Data[x].y |

| Address Variable   | Definition                                                      |
|--------------------|-----------------------------------------------------------------|
| name_of_terminal   | Name of the instance in the I/O configuration of the controller |
| x                  | Element of the input (I) or output (O) structure.               |
| y                  | Bit number within the input or output element                   |

## Index

## A

## access

access data 59 produced and consumed data 13 scheduled I/O tags 88

actual packet interval 15, 16

adjust

media configuration 41, 45

tags for bandwidth limitations 69

API. See actual packet interval 15

## B

## bandwidth

limitations 69 rack -optimized communication format 52 requested packet interval rate 52 unscheduled maximum node address 18

## bridge across networks 10

## C

cache message connections 79 capacity of ControlNet network 20 communicate between computer and devices 23 between controller and devices 62 communicate across networks 10 with I/O modules 58 with PanelView products 83

## communication driver 23

## communication format

distributed I/O 59 effect on requested packet interval 52 rack optimized 55 select 52, 59

## communication path 45

## configure

configure ControlNet module 25 ControlNet communication driver 23 message instructions 81

## connection

between computer and ControlNet network 23 for produced and consumed tags 67 validate 62

## consumed tags

creating in Logix Designer software 72

defined 65 determine connections 67 guidelines 68 organize tag data 68

## control I/O 51

## ControlNet module

bridge across networks 10 configure 25 overview 9

## ControlNet network

capacity 20 connect a computer 23 IX ControlNet network topology 18 schedule 16 scheduleIXControlNetnetworkschedule 40

## D

## data types 65, 68, 69, 72 distributed I/O

access data 59 communication formats 59

download Logix Designer project 34

## E

electronic keying 35 enter message logic 79

## I

## I/O

control 51 rack optimized connections 55 scheduled 16

interlocking controllers. See produced tags or consumed tags 65

## K

keeper, network 17 keying, electronic 35

## L

## local ControlNet module 25 Logix 5000 controller

consumed tags 72 direct or rack -optimized connections 53 local ControlNet module 25 produced tags 69 remote ControlNet module 29

## Logix Designer software

add PanelView terminal 84

communication format 52 create consumed tag 72 create produced tag 69 download project 34

## M

## media configuration 41, 45 message instructions

cache message connections 79 configure 81 guidelines 78 staggering messages 82

message logic 79

## N

network keeper 17 network update time 13, 18, 52, 68, 69 NUT. See network update time 14

## O

ownership types 56, 57

P

## PanelView terminal

connection to Logix 5000 controller 84 controller data 88 hardware setup 83 Logix Designer software setup 84 select 84

## peer -to-peer messaging 77 produced tags

defined 65 determine connections 67 guidelines 68 organize tag data 68 produced tags 69

## R

rack-optimized communication format 55

remote ControlNet module 29

requested packet interval 52

RPI. See requested packet interval 52

RSLinx Classic software 23

RSNetWorx for ControlNet software configure network keeper 17 schedule network 40

RSView software 83

## S

schedule ControlNet network 16, 40 scheduled I/O 16

scheduled maximum node address 18

## select

communication driver 23 communication format 52, 59 communication path 45 local communication module 25, 84 remote communication module 29

## set

communication format 52 network schedule parameters 41, 45 requested packet interval 52 scheduled maximum node address 18 unscheduled maximum node address

18

SMAX. See scheduled maximum node address 18

staggering messages in Logix Designer 82

## T

tags. See produced tags or consumed tags

65 topology of ControlNet network 18

## U

UMAX. See unscheduled maximum node address 18 unscheduled maximum node address 18

## V

validate connections 62

## Rockwell Automation support

Use these resources to access support information.

| Technical Support Center                                                             | Find help with how-to videos, FAQs, chat, user forums, and product notification updates.   | rok.auto/support                                                                      |
|--------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------|
| Knowledgebase  Access Knowledgebase articles.                                        | rok.auto/knowledgebase                                                                     |                                                                                       |
| Locate the telephone number for your country.                                        | rok.auto/phonesupport                                                                      | Local Technical Support Phone Numbers                                                 |
| Find installation instructions, manuals, brochures, and technical data publications. | rok.auto/literature                                                                        | Literature Library                                                                    |
| Product Compatibility and Download Center (PCDC) associated firmware.                | rok.auto/pcdc                                                                              | Get help determining how products interact, check features and capabilities, and find |

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

AMERlCAS:RockwellAutomation,1201SouthSec0ndStreet,Milwaukee,Wl53204-2496USA,Tel:(1)414.382.2000,Fax:(1)414.382.4444 EUR0PE/MIDDLEEAST/AFRICA:RockwellAutomationNV,PegasusPark,DeKleetlaan12a,1831Diegem,Belgium,Tel:(32)26630600,Fax:(32)26630640 ASIA PACIFIC:Rockwell Automation,Level14,CoreF,Cyberport 3,100 Cyberport Road,Hong Kong,Tel:(852)2887 4788,Fax:(852)25081846

<!-- image -->